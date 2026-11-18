# Writing a product update

[`changelog/product-updates.mdx`](/changelog/product-updates.mdx) is the list of new
features and improvements in the Kosli app. It is not the CLI and Terraform changelog in
`changelog/index.mdx`, which a workflow writes from release tags.

Each entry on the page is also an item in the page's RSS feed,
`https://docs.kosli.com/changelog/product-updates/rss.xml`. The Kosli app reads that feed
and shows the entries in its **What's new** menu, with an unread badge. So an entry is
written for two readers: someone on the docs page, and someone in the app who sees only
the title and a one-sentence summary.

## Add an entry

Add the entry at the top of the page, above the newest one, and open a PR as for any other
docs change. Copy this shape:

```mdx
<Update
  label="November 10, 2026"
  id="new-navigation"
  tags={["new-navigation"]}
  description="Kosli's sidebar is now grouped into Home, Evidence, Control and Governance."
  rss={{
    title: "Finding your way around Kosli's new navigation",
    description: "Kosli's sidebar is now grouped into Home, Evidence, Control and Governance.",
    date: "2026-11-10"
  }}
>

## Finding your way around Kosli's new navigation

What changed and why it matters to the reader, with links to the docs pages that explain
it.

</Update>
```

| Field | What it does | Rules |
|---|---|---|
| `label` | The date shown beside the entry on the docs page. | Month, day and year, for example `November 10, 2026`. |
| `id` | The anchor of the entry, and how the app recognizes it. | Lowercase words joined by hyphens. Unique on the page. **Never change it once published**: the app treats a new `id` as a new update, unread for every user. |
| `tags` | Which organizations see the entry in the app. | See [Show an entry only to some organizations](#show-an-entry-only-to-some-organizations). |
| `description` | Summary kept for the page. | The same sentence as `rss.description`. It is hidden on the page. |
| `rss.title` | The title in the app. | Short, as for the `##` heading. Plain text: markup is removed. |
| `rss.description` | The summary under the title in the app. | One sentence. Plain text: markup is removed. |
| `rss.date` | When the entry was published. The app lists unread entries first, then the newest. | `YYYY-MM-DD`. Add a time (`2026-11-12T08:00:00Z`) only to order two entries on the same day. |

The body is for the docs page only. The app links to it but does not show it.

## Show an entry only to some organizations

Some features are turned on one organization at a time. An entry about such a feature
must only show in the app for organizations that have the feature. A tag does that: the
server maps some tags to a feature flag, and it hides the entry from every organization
where that flag is off. When the flag is turned on for an organization later, the entry
shows there as unread.

These are the tags the server knows:

| Tag | Shows the entry to organizations with |
|---|---|
| `new-navigation` | The new navigation |
| `new-trail-page` | The new trail page |

- **Any other tag is ignored**, and the entry shows to every organization. So check the
  spelling: a mistyped tag shows the entry to everyone.
- **Keep the tag after the feature reaches every organization.** It does no harm, and
  removing it changes nothing in the app.
- **For a new tag**, ask the server team (open an issue in `kosli-dev/server`) before you
  publish. They add it to `PRODUCT_UPDATE_TAG_FLAGS` in `src/lib/feature_flags.py`. Until
  that change is deployed, the entry shows to every organization.

Tags use neutral names, not the names of the feature flags, because the feed is public.

### Turn the feature on for more organizations

An entry with a tag follows its feature flag, so you change who sees it in LaunchDarkly,
not in the docs:

1. Find the flag for the tag in `PRODUCT_UPDATE_TAG_FLAGS` in `src/lib/feature_flags.py`
   in `kosli-dev/server`. Each tag points to the function that checks the flag, and that
   function names the flag.
2. In LaunchDarkly, turn that flag on for the organizations, or ask the team that owns the
   feature to do it. The flag is the feature itself, not only the entry: the organization
   gets the feature and the entry together.
3. The entry shows as unread for the users of those organizations on their next page
   load. Nothing changes in the docs.

The What's new menu itself is behind a flag too, so an organization sees no entry until
the menu is turned on for it. Ask the server team to turn it on.

## After the PR merges

- The app reads the feed every five minutes, so a merged entry shows in the app within a
  few minutes of the docs deploy.
- Each user sees the entry as unread until they open the What's new menu. The first
  time the app shows the menu to a user, every entry published by then counts as read:
  the unread badge is for updates that come after that.
- Entries older than twelve months are never unread.

## Change or remove an entry

- **Fix the text** at any time. Keep the `id`, so users who have read the entry do not
  see it as unread again.
- **Remove an entry** by deleting its `<Update>` block. It leaves the app at the next read
  of the feed.
