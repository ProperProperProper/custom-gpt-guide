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

> **Local vs. shared, in one line:** sorting your documents (`tools/`) never
> leaves your machine; uploading them to Knowledge sends them to OpenAI's
> servers, on purpose — that's how the GPT searches them. Full breakdown,
> including whether OpenAI trains on what you upload and who can see it once
> shared: **[docs/06-privacy-and-data.md](docs/06-privacy-and-data.md)**.

## Contents

### Getting Started
1. **[The walkthrough](docs/01-walkthrough.md)** — the full step-by-step, start to finish
2. **[Configure tab field reference](docs/02-field-reference.md)** — what every field in the setup screen actually does
3. **[Common mistakes](docs/03-common-mistakes.md)** — what to head off before your friend hits them
4. **[Example prompts](docs/04-example-prompts.md)** — copy-paste starting points for the Builder conversation
5. **[Prepping your inbox](docs/05-prepping-your-inbox.md)** — turning a messy folder of documents into clean Knowledge material, using the sorter in `tools/`
6. **[Privacy and data](docs/06-privacy-and-data.md)** — what's local, what's sent to OpenAI, training defaults by account type, and who can see a GPT's Knowledge once it's shared

### Build & Operate
7. **[Implementation guide](docs/07-implementation-guide.md)** — phase-by-phase walkthrough (20 min from idea to published GPT)
8. **[Advanced configuration](docs/12-advanced-configuration.md)** — deep dive into each Configure field and how to use it
9. **[Knowledge base best practices](docs/13-knowledge-base-best-practices.md)** — how to structure files so your GPT searches them correctly
10. **[Monitoring & optimization](docs/14-monitoring-optimization.md)** — how to measure success and improve over time

### Reference & Examples
11. **[Troubleshooting & real-world examples](docs/15-troubleshooting-examples.md)** — common issues + 3 complete working GPT configurations
12. **[Sharing with users](docs/16-sharing-with-users.md)** — how to share your GPT so users can access it, ask questions, and get answers

## tools/prep_inbox.py

A script that sorts and cleans a folder of documents — de-duplicates,
extracts text from PDF/DOCX/TXT/MD/RTF, flags anything that looks
sensitive, and writes clean files plus an index ready to hand off for
upload. **Runs entirely on your own machine — no API key, no network calls,
nothing sent anywhere** (see [docs/06-privacy-and-data.md](docs/06-privacy-and-data.md#verifying-this-yourself)
for how to verify that yourself rather than take it on faith). See
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
