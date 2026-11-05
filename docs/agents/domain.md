# Domain Docs

The project's vocabulary and decisions live in the canonize canon: `docs/glossary.md` and
decision pages in `docs/pages/`, governed by `/canonize:canon`. The repo keeps no ADRs and
no root `GLOSSARY.md`. Where an engineering skill would write either, propose the canon
glossary term or canon decision to Emilia for `/canonize` to write.

## Before exploring, read these

- **`docs/glossary.md`**: model and project terms above its `## Tags` list (the tags are
  canon compilation vocabulary).
- **Canon decision pages** (listed in `docs/index.md`) that touch the area you're about to
  work in, such as which pathways an arm contrast isolates or how the POC arm replaces
  syndromic management.

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal,
a hypothesis, a test name), use the term as `docs/glossary.md` defines it. Don't drift to
synonyms the glossary avoids.

If the concept you need isn't in the glossary, either you're inventing language the
project doesn't use (reconsider) or there's a real gap (raise it with Emilia for the
canon).

## Flag decision conflicts

If your output contradicts a canon decision, name the decision page and surface the
conflict explicitly instead of silently overriding it.
