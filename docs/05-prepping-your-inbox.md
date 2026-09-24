# Prepping your inbox before you upload

You don't need a GPT subscription for this part — the sorting and cleaning
happens on your own machine, for free, before anything touches ChatGPT. The
subscription is only needed for the upload step in
[docs/01-walkthrough.md, step 4](01-walkthrough.md#4-hand-it-material--this-is-the-training).

## Why bother cleaning up first

Knowledge search works on what you hand it. A folder of 40 scattered PDFs —
duplicates, empty exports, scanned images with no real text — gives the GPT
a worse shelf to search than 10 clean, well-organized documents would.
"More files" isn't the goal; "material the GPT can actually find the right
passage in" is.

## Run the sorter

```
cd tools
python3 -m venv .venv          # first time only
.venv/bin/pip install -r requirements.txt   # first time only
.venv/bin/python prep_inbox.py ~/Downloads/my-inbox --output ~/Downloads/cleaned
```

What it does, mechanically — no LLM calls, nothing leaves your machine:

- Pulls plain text out of every PDF, DOCX, TXT, MD, and RTF file it finds,
  recursively.
- Drops exact duplicates (same content saved under two names — common with
  downloaded email attachments).
- Skips anything empty after extraction (a scanned PDF with no real text
  layer extracts empty, for instance).
- Flags anything that looks like it contains a password, API key, private
  key, or SSN/credit-card-shaped number — those get reported, **not**
  copied into the output. You decide, per file, whether it's actually safe.
- Writes one clean `.md` file per surviving document, plus an `INDEX.md`
  cataloguing everything: what's ready, what got skipped, what got flagged.

Open `INDEX.md` first. It's the map of what just happened.

## Then: structure, which is where judgment still matters

The script hands you a flat pile of clean files — it doesn't know that
`onboarding-v2-final.md` and `onboarding-actually-final.md` are the same
document, or that six small files about your return policy should really be
one. That part still wants a reader. Two ways to do it:

**Do it yourself**, if the pile is small: skim `INDEX.md`, delete or merge
the obvious overlaps in the output folder, rename anything unclear.

**Hand it to a conversation**, if the pile is bigger: paste `INDEX.md` into
Claude or ChatGPT and ask directly —

> Here's an index of documents I'm about to upload as Knowledge for a
> Custom GPT. Which of these look like duplicates or near-duplicates of
> each other, and which small ones should probably get merged into one
> file before I upload them?

That's the same conversational-prompting skill from
[docs/04-example-prompts.md](04-example-prompts.md), aimed at your own
material instead of the GPT's instructions.

## What "properly structured" actually means for Knowledge

- **One topic per file**, roughly. A single 60-page document covering five
  unrelated subjects searches worse than five focused ones.
- **A clear filename.** `returns-policy.md` beats `doc4.md` — Knowledge
  search can use the filename as a signal, and so can you six months from
  now.
- **No orphaned context.** If a file says "see the table above" or "as
  discussed in the meeting," that reference means nothing once it's an
  isolated search result. Strip or rewrite anything that depended on
  surrounding material that didn't make the cut.
