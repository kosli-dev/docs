# Proposed Policies UI — wireframe mockups

Sources for the mockup images used by
[`tutorials/evaluate_policies_server_side.mdx`](../../tutorials/evaluate_policies_server_side.mdx).
They depict a **proposed** UI that does not exist yet, so every rendered page carries a
"Mockup · proposed design" marker.

Chrome and palette were matched against the real Controls screenshots in
`images/tutorials/controls-*.png` (sidebar `#101c2b`, primary `#1e55cd`, compliant `#3ca36f`,
non-compliant `#ce4a3e`). `logo.png` / `logo-footer.png` are crops of the real logo with the ICC
profile stripped, so they blend with the CSS colors.

## Regenerate

```bash
python3 build.py   # also writes kosli-mock.css (gitignored)
for p in policy-list policy-source policy-decisions policy-decision-detail; do
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
    --window-size=1535,1011 --screenshot="$p.png" "file://$PWD/$p.html"
done
cp policy-*.png ../../images/tutorials/
```

1535x1011 at 1x matches the existing Controls screenshots.
