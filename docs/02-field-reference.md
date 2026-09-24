# Configure tab, field by field

Useful to have open side-by-side with the real thing the first time through.

| Field | What it actually does |
|---|---|
| **Name** | What it's called everywhere it appears — GPT store, conversation header, share links. Name it by the job, not by a personality ("Book Club Picks," not "Bookworm Bot"). |
| **Description** | One sentence, shown under the name in search and sharing. Written for someone deciding whether to open it, not for the GPT itself. |
| **Instructions** | The actual system prompt. Job, process, tone, boundaries — see [docs/01-walkthrough.md, step 3](01-walkthrough.md#3-read-back-what-it-wrote-then-correct-it). |
| **Conversation starters** | Up to 4 suggested first messages shown before anyone types. Write them as the exact sentence a real user would send. |
| **Knowledge** | File uploads the GPT can search mid-conversation. See [docs/01-walkthrough.md, step 4](01-walkthrough.md#4-hand-it-material--this-is-the-training). |
| **Capabilities** | Web browsing, image generation, code interpreter — toggle only what the job needs. |
| **Actions** | Optional, advanced: connects the GPT to an external API so it can do things, not just talk. Skip this on a first build. |
