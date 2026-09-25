# Advanced Configuration

Deep dive into each Configure tab field and how to use it for maximum effect.

## Instructions: The System Prompt

The most important field. This is what shapes everything else.

### Structure That Works

```
[ROLE & PRIMARY JOB]
You are a [role] that helps with [specific task].
Your job is to [outcome], not [what it shouldn't do].

[PROCESS / STEP-BY-STEP]
When given a request, follow this process:
1. [First step]
2. [Second step]
3. [Output step]

[TONE & PERSONALITY]
Respond in [adjective] tone. Examples:
- Use language like "[example phrase]"
- Avoid "[example of what not to do]"
- When uncertain, [what to do instead]

[RULES / BOUNDARIES]
Always:
- [Must always do]
- [Must not do]

Never:
- [Absolutely forbidden]

If asked about [out-of-scope topic], [how to respond].

[OUTPUT FORMAT]
Structure your response as:
- [Item 1]: [what it contains]
- [Item 2]: [what it contains]

Keep responses to [length].
```

### Real Example: Research Assistant GPT

```
[ROLE & PRIMARY JOB]
You are a research assistant that helps academics find and summarize 
peer-reviewed papers on a specific topic. Your goal is to save researchers 
time by doing initial literature review work.

[PROCESS]
When asked for research on a topic:
1. Ask the user to clarify their focus (e.g., "machine learning" vs "neural networks")
2. Suggest 3-5 highly relevant papers from your Knowledge base
3. Provide a one-paragraph summary of each
4. Identify common themes across the papers
5. Ask follow-up questions to help refine the search

[TONE]
Respond in academic but approachable tone. Be precise but not pedantic.
Use phrases like "Here's what the literature shows..." and "A few key findings...".
Avoid jargon unexplained; define technical terms on first use.

[RULES]
Always cite the paper name and authors.
Never make up citations or papers that don't exist.
If you don't know a paper, say so explicitly.
Never summarize from secondary sources; stick to the papers in Knowledge.

If asked for papers outside your area (e.g., ancient history when you have neuroscience 
papers), politely redirect: "That's outside my current research collection. 
I focus on [your area]. For that topic, I'd recommend searching PubMed directly."

[OUTPUT FORMAT]
For each recommendation, provide:
- Title: [paper name]
- Authors: [key authors]
- Year: [publication year]
- Summary: [one paragraph, 100 words max]
- Relevance: Why this paper matters for your question

Keep the full response to 500 words unless asked for more detail.
```

### Instruction Anti-Patterns

**Don't do this**:

❌ "Be helpful and kind"
❌ "Answer questions about anything"
❌ "Use a professional tone"
❌ "Make the output look nice"

**Do this instead**:

✓ "When the user provides incomplete information, ask clarifying questions before attempting to answer. Use phrases like 'Just to make sure I understand...' and 'So you're looking for...'"

✓ "Focus exclusively on [your domain]. If asked about unrelated topics, say 'That's outside my area, but I can help with [your domain].'"

✓ "Use formal academic tone: complete sentences, passive voice where appropriate, no contractions (never 'don't', always 'do not'). Example response structure: [show example]."

✓ "Format the output as a numbered list with clear section headers. Use markdown: **bold** for key concepts, `code blocks` for commands."

---

## Name & Description

### Name (Most Important)

**Rules**:
- Describe the **job**, not the personality
- Searchable and findable
- Specific to your use case
- 50 characters max

**Examples**:

| ❌ Poor | ✓ Good | Why |
|---|---|---|
| "ChatBot" | "Research Paper Finder" | Describes what it does |
| "Smart Assistant" | "Code Review Assistant" | Specific use case |
| "Helper" | "Tax Deduction Explainer" | Clear job |
| "Mr. Knowledge" | "Company Policy Q&A" | Avoids personality, shows function |

**Format**:
- If it's a role: "[Role] [Domain]" (e.g., "Data Analyst Interview Coach")
- If it's a task: "[Action] [Domain]" (e.g., "Legal Brief Generator")
- If it's a tool: "[Purpose] [Scope]" (e.g., "Product Copy Writer")

### Description (Gallery Subtitle)

One sentence, for the GPT Store gallery. Someone is deciding whether to open it.

**Rules**:
- Complete sentence
- Explain the value, not the mechanism
- Action-oriented
- 120 characters max

**Examples**:

| ❌ Poor | ✓ Good | Why |
|---|---|---|
| "A GPT that uses AI" | "Analyzes job postings and suggests skills to develop" | Shows outcome |
| "Helps with writing" | "Writes professional emails in your personal voice" | Specific benefit |
| "Research tool" | "Finds peer-reviewed papers and summarizes them" | Clear action + benefit |

---

## Conversation Starters

Up to 4 suggested first messages shown before the user types anything.

### What They're For

- **Lower friction**: User doesn't have to think of a first message
- **Show use cases**: Demonstrate different ways to use the GPT
- **Set expectations**: Give examples of what the GPT can do

### How to Write Them

Write as if a real user is typing:

**❌ Wrong (too formal or generic)**:
- "Please provide research assistance"
- "I would like your help with writing"
- "Can you assist me in understanding this topic?"

**✓ Right (natural, realistic)**:
- "What skills would help me land a product manager role?"
- "Here's an email I wrote. Does it sound professional?"
- "Explain quantum entanglement to a 10-year-old"

### Format

- Present tense ("What are...")
- Ask a real question
- Show a realistic scenario
- Specific enough to trigger the GPT's specialty

**Examples by GPT type**:

**Recommendation GPT**:
- "I loved *Educated* — what should I read next?"
- "I'm in the mood for something funny and short"
- "Recommend a sci-fi series I can binge"

**Explanation GPT**:
- "Why does inflation affect interest rates?"
- "Explain machine learning like I'm five"
- "What's the difference between SSL and TLS?"

**Writing GPT**:
- "Here's my cover letter draft. How does it sound?"
- "I need to ask my boss for a raise. What should I say?"
- "Rewrite this email to be friendlier"

**Analysis GPT**:
- "Is this resume effective for a tech job?"
- "Does this code have any vulnerabilities?"
- "What are the pros and cons of this approach?"

### Pro Tip: Diversity

Make your 4 starters show different use cases:

```
Starter 1: Quick question ("What's the difference between...")
Starter 2: Upload/paste task ("Here's my document...")
Starter 3: Exploratory ("What would happen if...")
Starter 4: Boundary case ("Can you help with...")
```

This teaches users the GPT's full range.

---

## Knowledge Files: Strategic Uploads

Not just "upload everything". Be intentional.

### File Selection Criteria

**Upload these**:
- Reference material the GPT needs to cite
- Proprietary info (internal policies, product specs)
- Correct, vetted information (you've verified it's accurate)
- Stable content (doesn't change weekly)
- Topic-focused (one subject per file)

**Don't upload**:
- Sensitive personal data
- Credentials or API keys
- Outdated info (if a newer version exists)
- Extremely large documents (>20 pages, split them)
- Raw data (structure it first — make it readable)

### File Organization

**Strategy 1: Topic-Based (Recommended)**

```
knowledge-base/
├── company-policies.pdf
├── product-specification.pdf
├── onboarding-guide.pdf
├── faq.pdf
└── sales-pitch-framework.md
```

Each file is self-contained on one topic. GPT searches are faster and more accurate.

**Strategy 2: Source-Based**

```
knowledge-base/
├── employee-handbook.pdf
├── recent-blog-posts.pdf
└── competitor-analysis.pdf
```

Use this when sources are distinct and users need to know which came from where.

### File Naming

Clear, searchable names:

| ❌ Poor | ✓ Good |
|---|---|
| "document1.pdf" | "company-benefits-policy.pdf" |
| "notes.txt" | "product-roadmap-q4-2024.md" |
| "draft v3 final.docx" | "onboarding-procedures-2024.pdf" |

### Size & Format

- **Ideal**: 5–50 pages per file
- **Max**: 100 pages (split longer docs)
- **Formats**: PDF, DOCX, TXT, MD work best

If you have a 200-page manual:
- Split into sections: "Manual Part 1: Basics", "Manual Part 2: Advanced"
- GPT will search both but more accurately

### Upload Workflow

1. Clean files first with `tools/prep_inbox.py`
2. Organize by topic
3. Upload to Knowledge (Configure tab)
4. **Test retrieval** — ask the GPT questions that should pull from the files
5. If GPT misses something, rewrite that section to be clearer

---

## Capabilities: What to Enable

### Web Browsing

**Enable if**:
- GPT needs current information (news, weather, stock prices, release dates)
- Users will ask "What's new in..." or "Current status of..."

**Disable if**:
- Information is static (company policies, how-to guides)
- Users won't need real-time data

**Trade-off**: Web browsing adds latency (searches are slower). Only enable if needed.

### DALL-E Image Generation

**Enable if**:
- GPT creates images as part of output (logo designer, diagram creator)

**Disable if**:
- GPT is text-only (analysis, writing, explanation)

**Most GPTs**: Disable this. Text is faster.

### Code Interpreter

**Enable if**:
- GPT runs code, analyzes data, creates visualizations
- Users will upload files (CSV, JSON) for analysis

**Disable if**:
- GPT is text-only

**Trade-off**: Code interpreter adds latency. Only enable if needed.

---

## Actions (Advanced)

Connects your GPT to an external API so it can do things (book flights, look up inventory, post to social media).

**This is advanced.** For your first GPT, leave it blank.

If you want to add Actions later:

1. Create an API endpoint on your server
2. Write an OpenAPI schema describing it
3. Come back to Configure → Actions
4. Paste the OpenAPI schema
5. Test that the GPT can call your API

Example use case: "Book a flight" GPT that actually books flights via an airline API.

---

## Settings Summary

| Field | What It Does | When to Use |
|---|---|---|
| **Name** | Title in GPT Store | Always — be specific |
| **Description** | Gallery subtitle | Always — show value |
| **Instructions** | System prompt | Always — the hardest part |
| **Conversation Starters** | Suggested first messages | Usually — teach users |
| **Knowledge** | Uploaded reference files | If GPT needs them |
| **Web Browsing** | Real-time web search | If GPT needs current info |
| **DALL-E** | Image generation | If GPT creates images |
| **Code Interpreter** | Python execution | If GPT analyzes/visualizes |
| **Actions** | External API calls | Advanced — leave blank at first |

---

## Testing Configuration Changes

After you edit something:

1. Click **Save** (if there's a button)
2. Go to **Preview** (right side)
3. Start a fresh conversation (clear previous context)
4. Test the change

**Example**:
- Change: Edited Instructions to add a new rule
- Test: Ask a question that triggers that rule
- Expect: GPT follows the new rule

---

## Version Control

Keep a backup:

```bash
# Save your Instructions to a file
cat > my-gpt-instructions.md << 'EOF'
[Your Instructions text here]
EOF

# Git it
git add my-gpt-instructions.md
git commit -m "Update: Added rule about handling edge case X"
```

This way, if you make a change you don't like, you can revert to a known-good version.

---

**Next**: See [Real-World Examples](13-real-world-examples.md) for complete, working GPT configurations you can adapt.
