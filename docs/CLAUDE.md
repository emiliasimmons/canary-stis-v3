It is **critically important** to load /canonize:canon immediately, if not yet done.
Never read a file from `./raw/` without either:
- Being explicitly instructed (by a skill or user)
- Determining that reading raw content is relevant **ONLY** if reading its cataloged entry
    in `./pages/` is insufficient.

# Conventions

## Commit

- Cataloging: commit once per batch.
- Every other write: one commit per logical write, structured message (`catalog: <title>`,
  `curate: <what>`).

## Sourcing

- PDF extraction: docling approved. It reconstructs two-column layout and tables, and
  installs ~1 GB on first use. Run it without a prompt. The six entries cataloged before
  this was settled were extracted with pymupdf.
- Academic sources, in order: `raw/canary-stis.bib` first, then PDFs dropped into `raw/`,
  then the Zotero library. Search OpenAlex or anywhere else only when asked directly.
- PDFs and .docx files under `raw/` are git-ignored and exist only on this machine. Commit
  the extracted `content.md`, `metadata.json` and tables beside them. A page's `local:`
  path can point at a document nobody else has, so a claim that matters belongs in the
  page or in the extracted text.

## Tags

A tag marks a cross-cutting theme with 3 or more expected members. Short and general beats
compound or qualified: `hiv` not `hiv-incidence`, `modeling` not `mathematical-modeling`.
The qualifier belongs in the page's description. Atomic tags intersect to capture what a
compound tag would (`antibiotic` + `resistance` + `modeling`).

## Sign-off

A tag that extends an existing family is added on your own and reported. A tag that opens
a new dimension, a tag split, merge, or rename, and a new page type each need the user's
sign-off first.
