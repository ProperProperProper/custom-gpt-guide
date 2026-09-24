# Building a Custom GPT

A walkthrough for teaching someone — no ML background required — how to build
a Custom GPT in ChatGPT: describing it into existence by talking to the GPT
Builder, then handing it reference material to draw on.

No code, no API key, about 20 minutes with a coffee.

## Before you start

Set expectations correctly, because this is where people get confused: a
Custom GPT is **not** a fine-tuned model. Nothing about the underlying model's
weights changes. You're configuring a saved *preset* — a system prompt, a set
of behavioral rules, and a folder of reference files the model can search —
that GPT-4 or GPT-5 reads at the start of every conversation. That's the whole
mechanism. Say this out loud before your friend starts imagining something
heavier.

**Requirements:** a ChatGPT Plus, Team, or Enterprise account. Start at
[chatgpt.com](https://chatgpt.com) → sidebar → **Explore GPTs** → **Create**.

## Contents

1. **[The walkthrough](docs/01-walkthrough.md)** — the full step-by-step, start to finish
2. **[Configure tab field reference](docs/02-field-reference.md)** — what every field in the setup screen actually does
3. **[Common mistakes](docs/03-common-mistakes.md)** — what to head off before your friend hits them
4. **[Example prompts](docs/04-example-prompts.md)** — copy-paste starting points for the Builder conversation
5. **[Prepping your inbox](docs/05-prepping-your-inbox.md)** — turning a messy folder of documents into clean Knowledge material, using the sorter in `tools/`

## tools/prep_inbox.py

A script that sorts and cleans a folder of documents — de-duplicates,
extracts text from PDF/DOCX/TXT/MD/RTF, flags anything that looks
sensitive, and writes clean files plus an index ready to hand off for
upload. Runs entirely on your own machine, no API key needed. See
[docs/05-prepping-your-inbox.md](docs/05-prepping-your-inbox.md) for the
full walkthrough, or just:

```
cd tools
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python prep_inbox.py ~/Downloads/my-inbox --output ~/Downloads/cleaned
```

## Quick start

If you only read one thing: open the Builder, describe the job in plain
language (not a spec — a briefing, like you're onboarding a new hire), let it
draft instructions, then read those instructions back out loud together and
tighten anything vague. That loop — describe, read back, tighten — is most of
what building one well actually is. The full detail is in
[docs/01-walkthrough.md](docs/01-walkthrough.md).

---

*Configure tab fields and limits reflect OpenAI's GPT Builder as of early
2026 — this screen gets adjusted periodically, so a label or limit may have
shifted slightly by the time you sit down together.*
