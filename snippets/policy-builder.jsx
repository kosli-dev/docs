/*
 * Interactive Kosli environment-policy builder.
 *
 * Self-contained Mintlify React component (see
 * https://www.mintlify.com/docs/customize/react-components):
 *   - named export only, no `export default`
 *   - no third-party imports (YAML is hand-rolled below)
 *   - only the pre-injected hooks are used (useState, useMemo)
 *
 * IMPORTANT — Mintlify sandbox scope: the sandbox evaluates only the exported
 * component's body together with the pre-injected hooks. Module-level helpers,
 * constants, and other components are NOT in scope at runtime, and capitalized
 * <Tags> resolve through Mintlify's MDX component registry rather than local
 * scope. So EVERYTHING this component needs is defined inside the function
 * below, and the UI sub-pieces are plain functions invoked directly
 * (e.g. {termEditor(...)}) rather than JSX elements.
 *
 * The serialization and expression-building logic mirrors the CLI policy
 * wizard (kosli-dev/cli: internal/policywizard, internal/policy). The YAML
 * body mirrors the CLI's `policy.ToYAML()` (gopkg.in/yaml.v3, 4-space indent),
 * with a leading `# yaml-language-server` schema directive prepended so the
 * pasted file gets validation and autocomplete in schema-aware editors. Keep
 * this file in sync with the v1 policy schema at
 * https://docs.kosli.com/schemas/policy/v1
 */

export const PolicyBuilder = () => {
  const SCHEMA_URL = "https://docs.kosli.com/schemas/policy/v1";

  const BUILTIN_TYPES = [
    "generic",
    "junit",
    "snyk",
    "pull_request",
    "jira",
    "sonar",
    "*",
  ];

  const TERM_KINDS = [
    { value: "flow_name", label: "Flow name" },
    { value: "flow_tag", label: "Flow tag" },
    { value: "artifact_name", label: "Artifact name pattern" },
    { value: "custom", label: "Custom comparison" },
    { value: "raw", label: "Raw expression" },
  ];

  const COMPARE_OPS = ["==", "!=", ">", "<", ">=", "<="];
  const CUSTOM_OPS = ["==", "!=", ">", "<", ">=", "<=", "matches", "exists"];
  const CUSTOM_CONTEXTS = [
    "flow.name",
    "flow.tags.<key>",
    "artifact.name",
    "artifact.fingerprint",
  ];

  // -------------------------------------------------------------------------
  // YAML serialization — mirrors gopkg.in/yaml.v3 default output.
  // -------------------------------------------------------------------------

  // yamlScalar quotes a scalar only when a plain (unquoted) form would be
  // ambiguous, matching yaml.v3's preference for single quotes (`*` -> '*').
  function yamlScalar(s) {
    if (s === "") return "''";
    const reserved = ["true", "false", "null", "yes", "no", "on", "off", "~"];
    const needsQuote =
      /^\s|\s$/.test(s) || // leading/trailing whitespace
      /^[-?:,\[\]{}#&*!|>'"%@`]/.test(s) || // indicator at start
      /:(\s|$)/.test(s) || // colon followed by space or end-of-string
      /\s#/.test(s) || // space then comment indicator
      /[\n\t]/.test(s) ||
      reserved.includes(s.toLowerCase()) ||
      (/^[0-9.+-]/.test(s) && !Number.isNaN(Number(s))); // looks numeric
    if (!needsQuote) return s;
    return "'" + s.replace(/'/g, "''") + "'";
  }

  // serializePolicy renders the policy state to a YAML string. Blocks are only
  // emitted when meaningful, exactly as the CLI wizard builds the policy object.
  function serializePolicy(state) {
    const lines = [
      "# yaml-language-server: $schema=" + SCHEMA_URL + ".json",
      "_schema: " + SCHEMA_URL,
    ];

    const provOn = state.provReq;
    const trailOn = state.trailReq;
    const validAtts = state.atts.filter((a) => attestationIsValid(a));

    if (!provOn && !trailOn && validAtts.length === 0) {
      return lines.join("\n") + "\n";
    }

    lines.push("artifacts:");

    const booleanBlock = (key, required, exceptions) => {
      lines.push("    " + key + ":");
      lines.push("        required: " + (required ? "true" : "false"));
      const exprs = exceptions
        .map((e) => serializeExpr(e))
        .filter((s) => s !== "");
      if (exprs.length > 0) {
        lines.push("        exceptions:");
        exprs.forEach((expr) => {
          lines.push("            - if: " + yamlScalar(expr));
        });
      }
    };

    if (provOn) booleanBlock("provenance", true, state.provExc);
    if (trailOn) booleanBlock("trail-compliance", true, state.trailExc);

    if (validAtts.length > 0) {
      lines.push("    attestations:");
      validAtts.forEach((a) => {
        const type = a.type === "custom" ? "custom:" + a.customType : a.type;
        lines.push("        - type: " + yamlScalar(type));
        // `name` defaults to `*` in the v1 schema, so only emit it when the
        // user requires a specific name.
        const name = (a.name || "").trim();
        if (name !== "" && name !== "*") {
          lines.push("          name: " + yamlScalar(name));
        }
        if (a.condEnabled) {
          const expr = serializeExpr(a.cond);
          if (expr !== "") lines.push("          if: " + yamlScalar(expr));
        }
      });
    }

    return lines.join("\n") + "\n";
  }

  // -------------------------------------------------------------------------
  // Expression building — mirrors internal/policy/expression.go.
  // -------------------------------------------------------------------------

  function unwrapExpr(expr) {
    let s = (expr || "").trim();
    if (s.startsWith("${{")) s = s.slice(3);
    if (s.endsWith("}}")) s = s.slice(0, -2);
    return s.trim();
  }

  function termToInner(term) {
    let inner = "";
    switch (term.kind) {
      case "flow_name":
        inner = `flow.name == "${term.flowName || ""}"`;
        break;
      case "flow_tag":
        inner = `flow.tags.${term.tagKey || ""} ${term.tagOp} "${
          term.tagValue || ""
        }"`;
        break;
      case "artifact_name":
        inner = `matches(artifact.name, "${term.artifactRegex || ""}")`;
        break;
      case "custom": {
        const ctx =
          term.customCtx === "flow.tags.<key>"
            ? "flow.tags." + (term.customTagKey || "")
            : term.customCtx;
        if (term.customOp === "exists") {
          inner = `exists(${ctx})`;
        } else if (term.customOp === "matches") {
          inner = `matches(${ctx}, "${term.customValue || ""}")`;
        } else {
          inner = `${ctx} ${term.customOp} "${term.customValue || ""}"`;
        }
        break;
      }
      case "raw":
        inner = unwrapExpr(term.raw);
        break;
      default:
        inner = "";
    }
    if (inner === "") return "";
    // NegateExpr wraps in parentheses regardless of precedence.
    return term.negate ? `not (${inner})` : inner;
  }

  // serializeExpr combines a term list with a logical operator, wrapping the
  // result in ${{ }} — matching CombineExprs + WrapExpr in the Go wizard.
  function serializeExpr(expr) {
    if (!expr) return "";
    const inners = (expr.terms || []).map(termToInner).filter((s) => s !== "");
    if (inners.length === 0) return "";
    if (inners.length === 1) return "${{ " + inners[0] + " }}";
    return "${{ " + inners.join(" " + (expr.combine || "and") + " ") + " }}";
  }

  // -------------------------------------------------------------------------
  // State factories
  // -------------------------------------------------------------------------

  // uid hands out stable, monotonic ids for React keys on the dynamic term /
  // exception / attestation lists. Index keys would let React reuse the wrong
  // DOM node when an item is removed from the middle of a list. idBox lives in
  // useState's lazy initializer (run once), so it persists across renders
  // without a ref hook — only useState/useMemo exist in the Mintlify sandbox.
  const idBox = useState(() => ({ n: 0 }))[0];
  function uid() {
    idBox.n += 1;
    return idBox.n;
  }

  function newTerm() {
    return {
      id: uid(),
      kind: "flow_name",
      negate: false,
      flowName: "",
      tagKey: "",
      tagOp: "==",
      tagValue: "",
      artifactRegex: "",
      customCtx: "flow.name",
      customTagKey: "",
      customOp: "==",
      customValue: "",
      raw: "",
    };
  }

  function newExpr() {
    return { id: uid(), combine: "and", terms: [newTerm()] };
  }

  function newAttestation() {
    return {
      id: uid(),
      type: "snyk",
      customType: "",
      name: "*",
      condEnabled: false,
      cond: newExpr(),
    };
  }

  function attestationIsValid(a) {
    const type = a.type === "custom" ? "custom:" + (a.customType || "") : a.type;
    if (a.type === "custom" && !a.customType) return false;
    if (type === "*" && (a.name || "*") === "*") return false;
    return true;
  }

  // -------------------------------------------------------------------------
  // Styles — theme-neutral inline styles so the component renders consistently
  // regardless of the surrounding Mintlify CSS.
  // -------------------------------------------------------------------------

  const S = {
    wrap: {
      display: "grid",
      gridTemplateColumns: "minmax(0, 1fr) minmax(0, 1fr)",
      gap: "1.25rem",
      alignItems: "start",
    },
    panel: {
      border: "1px solid var(--gray-200, #e5e7eb)",
      borderRadius: "0.5rem",
      padding: "1rem",
    },
    section: { marginBottom: "1.25rem" },
    legend: { fontWeight: 600, marginBottom: "0.5rem", fontSize: "0.95rem" },
    row: {
      display: "flex",
      gap: "0.5rem",
      alignItems: "center",
      flexWrap: "wrap",
      marginBottom: "0.5rem",
    },
    label: {
      display: "flex",
      alignItems: "center",
      gap: "0.4rem",
      fontSize: "0.9rem",
    },
    input: {
      padding: "0.35rem 0.5rem",
      border: "1px solid var(--gray-300, #d1d5db)",
      borderRadius: "0.375rem",
      fontSize: "0.85rem",
      background: "var(--background, transparent)",
      color: "inherit",
    },
    select: {
      padding: "0.35rem 0.5rem",
      border: "1px solid var(--gray-300, #d1d5db)",
      borderRadius: "0.375rem",
      fontSize: "0.85rem",
      background: "var(--background, transparent)",
      color: "inherit",
    },
    btn: {
      padding: "0.3rem 0.7rem",
      border: "1px solid var(--gray-300, #d1d5db)",
      borderRadius: "0.375rem",
      fontSize: "0.8rem",
      cursor: "pointer",
      background: "transparent",
      color: "inherit",
    },
    btnPrimary: {
      padding: "0.3rem 0.7rem",
      border: "none",
      borderRadius: "0.375rem",
      fontSize: "0.8rem",
      cursor: "pointer",
      background: "#2563eb",
      color: "#fff",
    },
    card: {
      border: "1px solid var(--gray-200, #e5e7eb)",
      borderRadius: "0.375rem",
      padding: "0.75rem",
      marginBottom: "0.75rem",
    },
    pre: {
      margin: 0,
      padding: "1rem",
      borderRadius: "0.5rem",
      background: "#0d1117",
      color: "#e6edf3",
      fontFamily:
        "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace",
      fontSize: "0.8rem",
      lineHeight: 1.5,
      overflowX: "auto",
      whiteSpace: "pre",
    },
    warn: { color: "#b45309", fontSize: "0.8rem", margin: "0.25rem 0 0.5rem" },
    muted: { fontSize: "0.8rem", opacity: 0.7 },
    fieldLabel: { fontWeight: 600, fontSize: "0.85rem", minWidth: "3rem" },
  };

  // -------------------------------------------------------------------------
  // Render helpers — plain functions returning JSX (see header note). Each
  // function used inside a list sets `key` on its returned root element.
  // -------------------------------------------------------------------------

  function termEditor({ term, onChange, onRemove, removable, keyId }) {
    const set = (patch) => onChange({ ...term, ...patch });
    return (
      <div key={keyId} style={S.card}>
        <div style={S.row}>
          <select
            style={S.select}
            value={term.kind}
            onChange={(e) => set({ kind: e.target.value })}
          >
            {TERM_KINDS.map((k) => (
              <option key={k.value} value={k.value}>
                {k.label}
              </option>
            ))}
          </select>
          <label style={S.label}>
            <input
              type="checkbox"
              checked={term.negate}
              onChange={(e) => set({ negate: e.target.checked })}
            />
            not
          </label>
          {removable && (
            <button type="button" style={S.btn} onClick={onRemove}>
              Remove
            </button>
          )}
        </div>

        {term.kind === "flow_name" && (
          <div style={S.row}>
            <span style={S.muted}>flow.name ==</span>
            <input
              style={S.input}
              placeholder="flow name"
              value={term.flowName}
              onChange={(e) => set({ flowName: e.target.value })}
            />
          </div>
        )}

        {term.kind === "flow_tag" && (
          <div style={S.row}>
            <span style={S.muted}>flow.tags.</span>
            <input
              style={{ ...S.input, width: "8rem" }}
              placeholder="key"
              value={term.tagKey}
              onChange={(e) => set({ tagKey: e.target.value })}
            />
            <select
              style={S.select}
              value={term.tagOp}
              onChange={(e) => set({ tagOp: e.target.value })}
            >
              {COMPARE_OPS.map((op) => (
                <option key={op} value={op}>
                  {op}
                </option>
              ))}
            </select>
            <input
              style={S.input}
              placeholder="value"
              value={term.tagValue}
              onChange={(e) => set({ tagValue: e.target.value })}
            />
          </div>
        )}

        {term.kind === "artifact_name" && (
          <div style={S.row}>
            <span style={S.muted}>matches(artifact.name,</span>
            <input
              style={S.input}
              placeholder="^datadog:.*"
              value={term.artifactRegex}
              onChange={(e) => set({ artifactRegex: e.target.value })}
            />
            <span style={S.muted}>)</span>
          </div>
        )}

        {term.kind === "custom" && (
          <div style={S.row}>
            <select
              style={S.select}
              value={term.customCtx}
              onChange={(e) => set({ customCtx: e.target.value })}
            >
              {CUSTOM_CONTEXTS.map((c) => (
                <option key={c} value={c}>
                  {c}
                </option>
              ))}
            </select>
            {term.customCtx === "flow.tags.<key>" && (
              <input
                style={{ ...S.input, width: "8rem" }}
                placeholder="tag key"
                value={term.customTagKey}
                onChange={(e) => set({ customTagKey: e.target.value })}
              />
            )}
            <select
              style={S.select}
              value={term.customOp}
              onChange={(e) => set({ customOp: e.target.value })}
            >
              {CUSTOM_OPS.map((op) => (
                <option key={op} value={op}>
                  {op}
                </option>
              ))}
            </select>
            {term.customOp !== "exists" && (
              <input
                style={S.input}
                placeholder={term.customOp === "matches" ? "regex" : "value"}
                value={term.customValue}
                onChange={(e) => set({ customValue: e.target.value })}
              />
            )}
          </div>
        )}

        {term.kind === "raw" && (
          <div style={S.row}>
            <input
              style={{ ...S.input, width: "100%" }}
              placeholder={'flow.name == "prod" and artifact.name == "svc"'}
              value={term.raw}
              onChange={(e) => set({ raw: e.target.value })}
            />
          </div>
        )}
      </div>
    );
  }

  function expressionEditor({ expr, onChange, keyId }) {
    const setTerm = (i, term) => {
      const terms = expr.terms.slice();
      terms[i] = term;
      onChange({ ...expr, terms });
    };
    const removeTerm = (i) => {
      const terms = expr.terms.filter((_, idx) => idx !== i);
      onChange({ ...expr, terms: terms.length ? terms : [newTerm()] });
    };
    const addTerm = () =>
      onChange({ ...expr, terms: [...expr.terms, newTerm()] });

    return (
      <div key={keyId}>
        {expr.terms.length > 1 && (
          <div style={S.row}>
            <span style={S.muted}>Combine terms with</span>
            <select
              style={S.select}
              value={expr.combine}
              onChange={(e) => onChange({ ...expr, combine: e.target.value })}
            >
              <option value="and">and</option>
              <option value="or">or</option>
            </select>
          </div>
        )}
        {expr.terms.map((term, i) =>
          termEditor({
            term,
            keyId: term.id,
            onChange: (t) => setTerm(i, t),
            onRemove: () => removeTerm(i),
            removable: expr.terms.length > 1,
          })
        )}
        <button type="button" style={S.btn} onClick={addTerm}>
          + Add term
        </button>
      </div>
    );
  }

  function exceptionList({ exceptions, onChange, label }) {
    const add = () => onChange([...exceptions, newExpr()]);
    const remove = (i) => onChange(exceptions.filter((_, idx) => idx !== i));
    const update = (i, expr) => {
      const next = exceptions.slice();
      next[i] = expr;
      onChange(next);
    };
    return (
      <div>
        {exceptions.map((expr, i) => (
          <div key={expr.id} style={S.card}>
            <div style={S.row}>
              <strong style={{ fontSize: "0.85rem" }}>
                {label} exception {i + 1}
              </strong>
              <button type="button" style={S.btn} onClick={() => remove(i)}>
                Remove
              </button>
            </div>
            {expressionEditor({ expr, onChange: (e) => update(i, e) })}
          </div>
        ))}
        <button type="button" style={S.btn} onClick={add}>
          + Add {label} exception
        </button>
      </div>
    );
  }

  function attestationRow({ att, onChange, onRemove, index }) {
    const set = (patch) => onChange({ ...att, ...patch });
    const valid = attestationIsValid(att);
    const typeValue = att.type === "custom" ? "custom" : att.type;
    return (
      <div key={att.id} style={S.card}>
        <div style={S.row}>
          <strong style={{ fontSize: "0.85rem" }}>
            Attestation {index + 1}
          </strong>
          <button type="button" style={S.btn} onClick={onRemove}>
            Remove
          </button>
        </div>
        <div style={S.row}>
          <strong style={S.fieldLabel}>type</strong>
          <select
            style={S.select}
            value={typeValue}
            onChange={(e) => set({ type: e.target.value })}
          >
            {BUILTIN_TYPES.map((t) => (
              <option key={t} value={t}>
                {t}
              </option>
            ))}
            <option value="custom">custom:&lt;name&gt;</option>
          </select>
          {att.type === "custom" && (
            <input
              style={S.input}
              placeholder="coverage-metrics"
              value={att.customType}
              onChange={(e) => set({ customType: e.target.value })}
            />
          )}
        </div>
        <div style={S.row}>
          <strong style={S.fieldLabel}>name</strong>
          <input
            style={S.input}
            placeholder="*"
            value={att.name}
            onChange={(e) => set({ name: e.target.value })}
          />
        </div>
        {!valid && (
          <p style={S.warn}>
            {att.type === "custom" && !att.customType
              ? "Enter a custom type name."
              : "type and name cannot both be * — give the attestation a name."}
          </p>
        )}
        <label style={S.label}>
          <input
            type="checkbox"
            checked={att.condEnabled}
            onChange={(e) => set({ condEnabled: e.target.checked })}
          />
          Only require when a condition is met
        </label>
        {att.condEnabled && (
          <div style={{ marginTop: "0.5rem" }}>
            {expressionEditor({
              expr: att.cond,
              onChange: (cond) => set({ cond }),
            })}
          </div>
        )}
      </div>
    );
  }

  // -------------------------------------------------------------------------
  // YAML syntax highlighting — hand-rolled, no third-party packages. Tuned for
  // the structured output this builder produces against the dark preview pane.
  // -------------------------------------------------------------------------

  const YAML = {
    key: "#79c0ff",
    string: "#a5d6ff",
    bool: "#ff7b72",
    expr: "#d2a8ff",
    punct: "#8b949e",
  };

  function highlightValue(value) {
    if (value === "true" || value === "false") {
      return <span style={{ color: YAML.bool }}>{value}</span>;
    }
    if (value.includes("${{")) {
      return <span style={{ color: YAML.expr }}>{value}</span>;
    }
    return <span style={{ color: YAML.string }}>{value}</span>;
  }

  // Each line is rendered as its own block element so line breaks survive
  // Mintlify's MDX whitespace handling (newline text nodes get collapsed).
  function highlightYaml(text) {
    const rows = text.replace(/\n$/, "").split("\n");
    return rows.map((line, i) => {
      if (/^\s*#/.test(line)) {
        return (
          <div key={i} style={{ whiteSpace: "pre", color: YAML.punct }}>
            {line}
          </div>
        );
      }
      const m = line.match(/^(\s*)(- )?([A-Za-z0-9_.-]+):( ?)(.*)$/);
      let content;
      if (!m) {
        content = line === "" ? " " : line;
      } else {
        const indent = m[1];
        const dash = m[2];
        const key = m[3];
        const space = m[4];
        const value = m[5];
        content = (
          <>
            {indent}
            {dash ? <span style={{ color: YAML.punct }}>{dash}</span> : null}
            <span style={{ color: YAML.key }}>{key}</span>
            <span style={{ color: YAML.punct }}>:</span>
            {space}
            {value !== "" ? highlightValue(value) : null}
          </>
        );
      }
      return (
        <div key={i} style={{ whiteSpace: "pre" }}>
          {content}
        </div>
      );
    });
  }

  // -------------------------------------------------------------------------
  // State + render
  // -------------------------------------------------------------------------

  const [provReq, setProvReq] = useState(false);
  const [provExc, setProvExc] = useState([]);
  const [trailReq, setTrailReq] = useState(false);
  const [trailExc, setTrailExc] = useState([]);
  const [atts, setAtts] = useState([]);
  const [copied, setCopied] = useState(false);

  const yaml = useMemo(
    () => serializePolicy({ provReq, provExc, trailReq, trailExc, atts }),
    [provReq, provExc, trailReq, trailExc, atts]
  );

  const invalidCount = atts.filter((a) => !attestationIsValid(a)).length;

  const copy = () => {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(yaml).then(() => {
        setCopied(true);
        setTimeout(() => setCopied(false), 1500);
      });
    }
  };

  return (
    <div style={S.wrap}>
      <div style={S.panel}>
        {/* Provenance */}
        <div style={S.section}>
          <div style={S.legend}>Provenance</div>
          <label style={S.label}>
            <input
              type="checkbox"
              checked={provReq}
              onChange={(e) => {
                setProvReq(e.target.checked);
                if (!e.target.checked) setProvExc([]);
              }}
            />
            Require artifact provenance
          </label>
          {provReq && (
            <div style={{ marginTop: "0.5rem" }}>
              {exceptionList({
                exceptions: provExc,
                onChange: setProvExc,
                label: "provenance",
              })}
            </div>
          )}
        </div>

        {/* Trail compliance */}
        <div style={S.section}>
          <div style={S.legend}>Trail compliance</div>
          <label style={S.label}>
            <input
              type="checkbox"
              checked={trailReq}
              onChange={(e) => {
                setTrailReq(e.target.checked);
                if (!e.target.checked) setTrailExc([]);
              }}
            />
            Require trail compliance
          </label>
          {trailReq && (
            <div style={{ marginTop: "0.5rem" }}>
              {exceptionList({
                exceptions: trailExc,
                onChange: setTrailExc,
                label: "trail-compliance",
              })}
            </div>
          )}
        </div>

        {/* Attestations */}
        <div style={S.section}>
          <div style={S.legend}>Required attestations</div>
          {atts.map((att, i) =>
            attestationRow({
              att,
              index: i,
              onChange: (next) => {
                const arr = atts.slice();
                arr[i] = next;
                setAtts(arr);
              },
              onRemove: () => setAtts(atts.filter((_, idx) => idx !== i)),
            })
          )}
          <button
            type="button"
            style={S.btn}
            onClick={() => setAtts([...atts, newAttestation()])}
          >
            + Add attestation
          </button>
        </div>
      </div>

      <div style={S.panel}>
        <div style={S.row}>
          <div style={{ ...S.legend, marginBottom: 0, flex: 1 }}>
            policy.yaml
          </div>
          <button type="button" style={S.btnPrimary} onClick={copy}>
            {copied ? "Copied!" : "Copy"}
          </button>
        </div>
        {invalidCount > 0 && (
          <p style={S.warn}>
            {invalidCount} attestation rule{invalidCount > 1 ? "s are" : " is"}{" "}
            incomplete and excluded from the output.
          </p>
        )}
        <div style={S.pre}>{highlightYaml(yaml)}</div>
      </div>
    </div>
  );
};
