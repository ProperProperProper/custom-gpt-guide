# The walkthrough

## 1. Get into the Builder

From any ChatGPT conversation: sidebar → **Explore GPTs** → **Create**. That
opens a split screen — a chat panel on the left, a live **Preview** of the
GPT on the right. The left panel has two tabs, **Create** and **Configure**.
Create is where the conversation happens; Configure is the form underneath it
that the conversation is quietly filling in. Point this out early — it
demystifies the rest of the process.

## 2. Describe it before you configure it

The instinct is to click straight into Configure and start filling boxes.
Resist that with your friend — the Create tab exists because describing a
GPT in plain language, back and forth, produces better instructions than
writing them cold. The Builder asks clarifying questions; answer them like
you're briefing a new hire, not writing a spec.

See [docs/04-example-prompts.md](04-example-prompts.md) for a full example to
try together. Notice what a good opening prompt does: a job, a process, a
tone, and an explicit constraint. That's the shape worth teaching — vague
briefs produce vague GPTs.

## 3. Read back what it wrote, then correct it

After a round or two the Builder drafts a name, an icon, and a first pass at
**Instructions** — flip to the Configure tab and read that field out loud
together. This is the actual teaching moment: instructions are just a system
prompt, so anything you'd fix in a system prompt applies here. Push for
specifics instead of accepting the first draft:

- Replace "be helpful and friendly" with what helpful actually means for
  *this* job — what it should always do, always avoid, and how it should
  handle the request it can't fulfill.
- Give it a boundary: what should it say when someone asks for something
  outside its lane? ("If asked about anything other than book picks, say so
  and redirect.")
- If output has a shape — a list of exactly 3, a specific format — spell that
  out explicitly. Models follow explicit structure far more reliably than
  implied structure.

You can edit the Instructions box directly, or keep talking to the Builder
and say what to change — both write to the same field.

## 4. Hand it material — this is the "training"

This is what most people mean by "training it with material," so name the
mechanism plainly: uploaded files go under **Knowledge** in the Configure
tab, and when a conversation might need one, the GPT searches those files and
pulls in relevant passages before it answers — a technique usually called
*retrieval*. The model itself never gets retrained on the content. It's
closer to giving someone a reference shelf than teaching them the material by
heart.

> **This is the step where files leave your machine.** Everything before
> this point — sorting the inbox with `tools/prep_inbox.py`, writing this
> guide's own repo — stayed local. A Knowledge upload is sent to and stored
> on OpenAI's servers; that's the only way retrieval can work. If you
> haven't already, run the inbox through the sorter and read its flagged-
> file report first — see [docs/05](05-prepping-your-inbox.md) and
> [docs/06](06-privacy-and-data.md) for the full detail on what happens to
> a file once it's uploaded and who can end up seeing it.

**What's worth knowing before uploading:**

- PDFs, Word docs, plain text, CSVs, and a handful of other formats all work.
- Up to 20 files per GPT, and ChatGPT can also reference their raw content
  directly for smaller files, not just search excerpts.
- Quality beats volume — one well-organized 40-page PDF outperforms ten
  scattered ones. If two files disagree, the GPT has no way to know which one
  you trust more, so it'll guess.

**Worth flagging explicitly:** anything uploaded can potentially surface in a
conversation, sometimes close to verbatim — Knowledge is not a private vault.
Nothing containing passwords, personal data about other people, or anything
they wouldn't want a stranger reading back to them.

## 5. Flip on what it actually needs

Further down Configure, under **Capabilities**, three toggles: **Web
Browsing**, **DALL·E Image Generation**, **Code Interpreter & Data
Analysis**. Turn on only what the job needs — a book-recommendation GPT has
no use for a code sandbox, and every extra capability is one more way the
conversation can wander off-task.

## 6. Test it like a stranger would use it

Switch to the **Preview** pane and try to break it before calling it done.
The genuinely useful test isn't "does it work" — it's the edge cases:

- Ask for something outside its scope. Does it redirect gracefully, the way
  you specified, or does it just answer anyway?
- Ask it something the Knowledge files should cover. Does the answer actually
  draw from them, or default to generic training knowledge?
- Give it a genuinely odd or adversarial request. Does the tone hold?

Every miss is a one-line addition to Instructions, not a reason to start
over — that loop, test → patch the instructions → test again, is most of
what building one well actually is.

## 7. Decide who gets to see it

The **Create** button in the top right offers three visibility levels:
**Only me**, **Anyone with a link**, or (workspace accounts) publish it into
the org's private GPT store. Start with link-sharing while testing with a
couple of real people before deciding whether it's worth publishing further.
