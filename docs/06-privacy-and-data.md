# Privacy and data: what's actually local

Worth reading before you upload anything, not after. "Local" and "shared"
don't apply uniformly to this whole process — some parts genuinely never
leave your machine, and one part (the point of the whole exercise) is
specifically designed to send files to OpenAI's servers. Knowing which is
which matters more than any single setting.

## The honest map

| Stage | Where the data actually goes |
|---|---|
| `tools/prep_inbox.py` sorting your inbox | **Stays on your machine.** No network calls — see [Verifying this yourself](#verifying-this-yourself) below. |
| This guide's git repo | **Stays on your machine**, unless you push it to a remote (GitHub, etc.) yourself. `git remote -v` with no output means nothing to push to. |
| Talking to the GPT Builder (Create tab) | **Sent to OpenAI.** It's a ChatGPT conversation like any other. |
| Instructions you write in Configure | **Stored by OpenAI**, as part of your GPT's configuration. |
| Files you upload to Knowledge | **Uploaded to and stored on OpenAI's servers.** This is the whole mechanism Knowledge search relies on — the GPT can't search a file that only exists on your laptop. There is no local-only Knowledge option. |
| Conversations other people have with your published GPT | Sent to OpenAI. You (the builder) do **not** see the content of other users' conversations with your GPT by default. |

The prep tool being local is what lets you review and redact *before* the
one step that isn't local. That's the whole reason it exists as a separate
step instead of uploading your raw inbox directly.

## Does OpenAI train on what you upload?

This depends on account type and a setting, not on Custom GPTs specifically:

- **ChatGPT Free and Plus (personal accounts):** by default, content you
  submit — including messages and Knowledge files — **may** be used to
  improve OpenAI's models, unless you turn this off. Check **Settings →
  Data Controls → Improve the model for everyone** and switch it off if you
  don't want that.
- **ChatGPT Team, Enterprise, and Edu (workspace accounts):** OpenAI does
  **not** use your content to train models by default — this is a
  contractual guarantee of the plan, not a toggle you need to set.

If you or your friend are on a personal account and uploading anything even
mildly sensitive, check that setting first. It's a one-time toggle, not
something you manage per GPT.

## Who can see a GPT's Knowledge once it's shared

The **Only me / Anyone with a link / GPT Store** choice from
[docs/01-walkthrough.md, step 7](01-walkthrough.md#7-decide-who-gets-to-see-it)
is a privacy decision, not just a distribution one — revisit it with that
lens:

- Anyone who can open the GPT can potentially get it to quote or closely
  paraphrase its Knowledge files through ordinary conversation. This isn't
  a bug to route around; it's how retrieval works. Treat Knowledge as
  **readable by anyone with access to the GPT**, full stop.
- "Only me" while testing is the safe default. Move to link-sharing or the
  GPT Store only once you've reviewed what's actually in the Knowledge
  folder and are comfortable with any of it surfacing verbatim.
- You can remove or replace Knowledge files after publishing, but treat
  that like taking down a public webpage: anyone who already saw the
  content in a conversation still has it in their own chat history.

## Before you upload: a real checklist

Walk this against `INDEX.md` from the prep tool, not against your memory of
what's in the folder:

- [ ] Anything flagged by `prep_inbox.py` — actually opened and reviewed,
      not just skipped past.
- [ ] No real credentials, even old/rotated ones (they still confirm a
      format or a username).
- [ ] No personal data about anyone who isn't you or didn't agree to it —
      names, contact info, anything from someone else's private
      correspondence.
- [ ] Nothing you'd mind a stranger reading back to them in a chat, if the
      GPT ends up shared more widely than planned.
- [ ] For a workspace account: confirmed you're actually on Team/Enterprise
      and not accidentally using a personal login.

## Verifying this yourself

Don't take "it's local" on faith — for `prep_inbox.py` specifically, you can
check it directly:

- **Read the source.** It's about 200 lines, all in `tools/prep_inbox.py`.
  There's no `requests`, `urllib`, `socket`, or any other networking import
  anywhere in the file — grep it yourself: `grep -n "import" tools/prep_inbox.py`.
- **Run it with your network off.** Turn off Wi-Fi, run it against a test
  folder, confirm it still works. A script that needs the network to
  function won't.
- **Watch it with Little Snitch or a similar outbound-connection monitor**,
  if you want to see the absence of network activity directly rather than
  infer it from the source.

None of this applies to the ChatGPT side of the process — once you're
talking to the Builder or uploading to Knowledge, you're inside OpenAI's
product, sending data to OpenAI's servers, governed by their privacy policy
and the account-type rules above, not this guide's.
