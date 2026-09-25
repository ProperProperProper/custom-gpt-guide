# Implementation Guide

Step-by-step walkthrough of building a Custom GPT from scratch.

## Before You Start

**Prerequisites**:
- ChatGPT Plus, Team, or Enterprise account
- 20–30 minutes
- Clear understanding of what job the GPT should do (be specific)

**Not prerequisites** (don't worry about these):
- Coding experience
- Machine learning knowledge
- "Fine-tuning" knowledge (Custom GPTs are not fine-tuned models)

## Phase 1: Preparation (5 min)

### Define the Job

Write down in one sentence what the GPT should do:

❌ Bad: "Help with things"
✓ Good: "Help book club members pick their next read by understanding what they've recently enjoyed and recommending 3 options with one-line pitches."

### Define Success Criteria

What would a good answer look like?

```
Example good answer:
- 3 recommendations, not more
- Each has a one-line pitch
- Tone is conversational, like a friend
- Respects the "no books over 450 pages" rule (unless asked)
```

### Gather Reference Material

If this GPT will use Knowledge files:

- Collect PDFs, Word docs, text files into one folder
- Use `tools/prep_inbox.py` to clean them (dedup, flag sensitive content, extract text)
- Organize cleaned files by topic

```bash
cd /path/to/custom-gpt-guide/tools
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python prep_inbox.py ~/Downloads/my-docs --output ~/Downloads/cleaned
```

See [Prepping Your Inbox](05-prepping-your-inbox.md) for details.

---

## Phase 2: Create & Describe (8 min)

### 1. Open the Builder

- Go to **chatgpt.com**
- Click sidebar → **Explore GPTs** → **Create**
- You'll see a split screen (chat on left, preview on right)

### 2. Describe It in Conversation

Click the **Create** tab (left side). Write your opening prompt:

```
I want a GPT that helps book club members pick their next read.
It should ask what we've read recently and what mood we're in,
then suggest 3 options with a one-line pitch for each.
Keep it warm and opinionated, like a well-read friend.
Never recommend a book longer than 450 pages unless someone asks.
```

**Hit Enter** and wait for the Builder to draft a response.

### 3. Read Back & Iterate

The Builder will generate:
- A name
- An icon/image
- A first draft of **Instructions** (the system prompt)
- Suggested conversation starters

**Important**: Switch to the **Configure** tab and read the **Instructions** field out loud. Is it correct? Does it capture what you want?

If not, go back to **Create** tab and say:

```
That's mostly right, but I need to change a few things:
1. The tone should be less formal
2. Add this rule: "If someone asks about non-fiction, politely redirect to fiction"
3. The default limit should be 3 books, but willing to go up to 5 if asked
```

**Iterate** until the Instructions feel right. This usually takes 2–3 rounds.

---

## Phase 3: Configure (10 min)

Once the **Create** conversation feels good, click the **Configure** tab.

### What You'll See

A form with these fields:

| Field | What to Do | Example |
|---|---|---|
| **Name** | Name of the GPT | "Book Club Picks" |
| **Description** | One sentence for the store | "Helps book clubs find their next read" |
| **Instructions** | The system prompt | *Read from Create tab, refine* |
| **Conversation starters** | Up to 4 suggested first messages | "What was our last pick?" |
| **Knowledge** | Files to upload | PDF book lists, review collections |
| **Capabilities** | Web browsing, image gen, code | Turn off what you don't need |
| **Actions** | External API connections | Leave blank for now |

### Edit Each Field

#### Name
- Use the job, not a personality ("Book Club Picks", not "Bookworm Bot")
- Descriptive, searchable
- 50 characters max

#### Description
- One sentence, for someone deciding whether to open it
- Example: "Helps book clubs discover their next read based on mood and recent picks"

#### Instructions
- This is the heart of the GPT
- Already drafted by the Builder conversation, now refine it
- Structure it like this:

```
[PRIMARY JOB]
Your role is to help book clubs find their next read.

[PROCESS]
1. Ask what we've read recently
2. Ask what mood we're in
3. Suggest exactly 3 books with one-line pitches
4. Be warm and opinionated

[TONE]
Sound like a well-read friend, not a review site.

[RULES]
- Never recommend books > 450 pages unless asked
- If asked about non-fiction, redirect to fiction
- Always explain why each book fits
```

#### Conversation Starters
- Write as the exact sentence a real user would type
- Make them natural, not robotic
- Examples:
  - "What was our last pick?"
  - "I'm in the mood for something dark"
  - "Can you suggest sci-fi that's under 300 pages?"
  - "Who are your favorite authors right now?"

#### Knowledge
- Click **Add files**
- Upload cleaned PDFs/docs (max 20 files)
- Name them clearly (e.g., "fantasy-bestsellers.pdf", "literary-fiction-2024.pdf")
- One topic per file (GPT searches better that way)

#### Capabilities
- **Web Browsing**: Turn ON if the GPT needs to look up current info (book reviews, release dates)
- **DALL-E**: Turn OFF (book club advice doesn't need image generation)
- **Code Interpreter**: Turn OFF (not needed here)

#### Actions
- Leave blank for now (advanced feature for calling external APIs)

---

## Phase 4: Test Like a Stranger (5 min)

Click **Preview** (right side of screen).

### Try to Break It

Test these cases:

**Test 1: On-topic, normal request**
```
Prompt: "We just finished a mystery novel. What's next?"
Expected: Should ask mood, make 3 suggestions with pitches
Actual: ___________
```

**Test 2: Out of scope**
```
Prompt: "Tell me about the history of agriculture"
Expected: Should redirect ("That's not my area...")
Actual: ___________
```

**Test 3: Boundary case**
```
Prompt: "Can you recommend a 600-page fantasy epic?"
Expected: Should warn about length but offer it if that's what user wants
Actual: ___________
```

**Test 4: Adversarial**
```
Prompt: "Recommend 10 books"
Expected: Should offer 3, mention can suggest more if they want
Actual: ___________
```

### Fix Issues

If a test fails, go back to **Configure** and edit **Instructions**:

```
[OLD]
Suggest exactly 3 books with one-line pitches.

[NEW]
Suggest exactly 3 books with one-line pitches. If asked for more,
you can suggest up to 5, but always start with 3 unless told otherwise.
```

**Test again** with the same prompt.

### Iterate Until Good

Fix → Test → Fix → Test. This is normal. Most GPTs need 3–5 cycles.

---

## Phase 5: Publish (1 min)

When tests pass:

1. Click **Create** button (top right)
2. Choose visibility:
   - **Only me**: Private, testing only
   - **Anyone with a link**: Shareable, but not discoverable
   - **GPT Store**: Public, anyone can find it

3. Click **Publish**

---

## Common Mistakes & Fixes

### Mistake 1: Vague Instructions

❌ "Be helpful and friendly"

Why it fails: Model doesn't know what "friendly" means for your job.

✓ Fix: "Respond in conversational tone with casual language. Use words like 'yeah' and 'definitely', not 'certainly' and 'perchance'."

---

### Mistake 2: Uploading Everything

❌ Upload 20 PDFs, hope the GPT figures it out

Why it fails: GPT can't find relevant passages in a huge haystack.

✓ Fix: Upload 3–5 well-organized files, one topic each. GPT searches better in focused documents.

---

### Mistake 3: Skipping Tests

❌ "Looks good in the preview, ship it"

Why it fails: Users will find edge cases you didn't think of immediately.

✓ Fix: Test at least 5 scenarios (on-topic, out-of-scope, adversarial, boundary, normal). Fix failures before publishing.

---

### Mistake 4: Confusing Instructions with Personality

❌ "Be witty and mysterious"

Why it fails: Model doesn't know what behavior those adjectives describe.

✓ Fix: "When the user asks something outside your scope, respond with a playful redirect: 'That's not really my jam, but I could help with book picks if you'd like!'"

---

## Workflow Summary

```
1. Define job (1 sentence)
2. Gather reference material (if needed)
3. Open Builder, describe in conversation (2–3 rounds)
4. Switch to Configure, refine each field
5. Test in Preview (try to break it)
6. Fix Instructions based on test failures
7. Publish with appropriate visibility level
8. Share link with friends
9. Iterate based on real feedback
```

---

## What Happens After Publish

### You Can Edit Anytime

Publish doesn't lock the GPT. You can:
- Change Instructions (takes effect immediately)
- Add/remove Knowledge files (immediate)
- Adjust conversation starters (immediate)
- Change visibility (immediate)

### Monitor Real Usage

If someone shares feedback, adjust Instructions:

**Example**:
```
User: "Your recommendations are too literary"
Fix: Add to Instructions:
  "Include at least one recommendation that's fun and accessible,
   not just critically acclaimed."
Republish (no downtime)
```

### Versioning

There's no "version history" in the UI, but you can:
- Keep a `CHANGELOG.md` in your repo documenting changes
- Periodically export Instructions to a backup file

---

## Next Steps

- **Read [Advanced Configuration](12-advanced-configuration.md)** for deeper tuning
- **See [Real-World Examples](13-real-world-examples.md)** for complete working GPTs
- **Check [Monitoring & Optimization](14-monitoring-optimization.md)** for how to measure success

---

**Remember**: Custom GPTs are fast to build and edit. Start with something simple, publish, and refine based on real feedback. You can't break anything — just unpublish if needed.
