# Knowledge Base Best Practices

How to structure and prepare Knowledge files so your GPT searches them effectively.

## The One Rule

**One topic per file.**

A single 60-page document covering five unrelated subjects searches worse than five focused 12-page documents.

Why? GPT retrieves passages, not whole documents. If a file has mixed content, the retrieved passage might be from the wrong section.

---

## File Structure Template

Use this structure for any Knowledge file:

```markdown
# [Topic Title]

## Overview
One-paragraph summary of what this document covers.

## Table of Contents
1. [Section 1]
2. [Section 2]
3. [Section 3]

## Section 1: [Name]
[Detailed content]

### Subsection 1.1
[More detail]

## Section 2: [Name]
[Detailed content]

## FAQ
Common questions about this topic:
- Q: ...
- A: ...

## Related Topics
Links to other relevant documents (reference by name).
```

### Why This Structure?

- **Markdown headings** help GPT understand document hierarchy
- **Table of contents** lets GPT find sections quickly
- **FAQ section** prepares for common queries
- **Related topics** helps GPT link related knowledge

---

## Real Examples

### Example 1: Company Policy Document

**File**: `company-vacation-policy.md`

```markdown
# Vacation Policy

## Overview
Guidelines for requesting and taking time off at Acme Corp.

## Table of Contents
1. Eligibility
2. Accrual & Banks
3. Requesting Time Off
4. Blackout Dates
5. Unused Vacation

## Eligibility
### Full-Time Employees
- Eligible after 90-day probation
- Accrue 20 days/year (standard)
- Executive team accrues 25 days/year

### Part-Time Employees
- Eligible after 6 months
- Prorated accrual (10 days/year for 50% time)

## Accrual & Banks
Accrual is monthly (annual total ÷ 12).
Unused vacation rolls over to next year, max 10 days.

[etc...]

## FAQ
Q: Can I carry over vacation to next year?
A: Yes, up to 10 days.

Q: What if I leave the company?
A: Unused vacation is paid out.

## Related Topics
See also: Sick Leave Policy, Remote Work Policy
```

### Example 2: Product Specification

**File**: `product-api-reference.md`

```markdown
# API Reference

## Overview
Complete reference for the Acme API v2.

## Table of Contents
1. Authentication
2. Rate Limits
3. Endpoints
4. Error Codes
5. Examples

## Authentication
All requests require an API key in the header:
```
Authorization: Bearer YOUR_API_KEY
```

### Getting Your API Key
1. Go to dashboard.acme.com/settings/api
2. Click "Generate Key"
3. Copy the key (shown only once)

## Rate Limits
- Public endpoints: 100 req/min per IP
- Authenticated: 1000 req/min per API key
- If exceeded: 429 Too Many Requests

[Endpoints detail...]

## Error Codes
- 400: Bad Request (check your input)
- 401: Unauthorized (check API key)
- 404: Not Found (endpoint or resource doesn't exist)
- 429: Rate limit exceeded

## Examples
### Create User
```
POST /users
{
  "name": "Jane Doe",
  "email": "jane@example.com"
}
```
Response:
```
{
  "id": "usr_123",
  "created_at": "2024-01-15T10:30:00Z"
}
```

## Related Topics
See also: Authentication Guide, Webhooks Reference
```

---

## Common Mistakes

### Mistake 1: Mixed Topics in One File

❌ **File**: `policies.pdf`
- Vacation policy (section 1)
- Sick leave policy (section 2)
- Remote work policy (section 3)
- Expense policy (section 4)
- Ethics policy (section 5)

Why it fails: User asks "Can I work from home?" and GPT pulls the wrong section or mixes answers.

✓ **Fix**: Split into:
- `vacation-policy.md`
- `sick-leave-policy.md`
- `remote-work-policy.md`
- `expense-policy.md`
- `ethics-policy.md`

---

### Mistake 2: No Clear Section Headers

❌ **File**: `procedures.txt`
```
To reset a password, use the admin tool. In the admin
tool, click "Users" then "Manage". Find the user and
click "Reset Password"...
```

Why it fails: No structure for GPT to understand what section covers what.

✓ **Fix**: Use clear headers
```markdown
# Procedures

## Resetting a User Password

To reset a password:
1. Open the Admin Tool
2. Click "Users" → "Manage"
3. Search for the user
4. Click "Reset Password"
...

## Changing User Permissions

To change permissions:
[etc...]
```

---

### Mistake 3: Vague File Names

❌ File names:
- `doc1.pdf`
- `notes.txt`
- `final_version.docx`
- `backup.pdf`

Why it fails: GPT can't tell what each file contains; user can't find what they need.

✓ File names:
- `employee-handbook.pdf`
- `api-authentication-guide.txt`
- `product-roadmap-2024.docx`
- `sales-pitch-framework.pdf`

---

### Mistake 4: Orphaned References

❌ **File**: `procedures.md` mentions
> "For details, see the section above on User Roles."

But User Roles was in a different file that wasn't uploaded.

Why it fails: User asks about user roles, GPT says "see the section above" but there's no section above in that conversation.

✓ **Fix**: Use **Related Topics** section
```markdown
## Related Topics
See also: User Roles & Permissions (separate document)
```

---

## Optimization Tips

### For Search Accuracy

**Before uploading, check**:
- [ ] Each file covers one topic only
- [ ] File name describes the content clearly
- [ ] Headers are descriptive (not just "1. Introduction")
- [ ] Important keywords appear early
- [ ] No orphaned references to missing files

**Example of good keywords**:
```markdown
# Remote Work Policy

## Eligibility
Who can work remotely and when?

### Core Hours
All employees must be available 10am–3pm Eastern.

### Equipment
Company provides laptop, monitor, mouse, keyboard.
```

GPT will find this when users ask "What equipment does the company provide for remote work?"

### For Clarity

**Make facts scannable**:

❌ Paragraph form
```
Employees are entitled to 20 days of vacation per year. 
This includes holidays. Requests must be submitted two 
weeks in advance to your manager.
```

✓ Structured
```
**Vacation Allowance**: 20 days/year
**Includes**: Company holidays
**Request Notice**: 2 weeks advance to manager
```

---

## File Preparation Workflow

### Step 1: Clean Files

Use `tools/prep_inbox.py`:

```bash
cd /path/to/custom-gpt-guide/tools
.venv/bin/python prep_inbox.py ~/Downloads/raw-docs --output ~/Downloads/cleaned
```

This:
- Extracts text from PDFs/Word docs
- Deduplicates exact copies
- Flags sensitive content
- Produces clean markdown

See [Prepping Your Inbox](05-prepping-your-inbox.md) for details.

### Step 2: Organize by Topic

Create folder structure:

```
knowledge/
├── company-policies/
│   ├── vacation-policy.md
│   ├── sick-leave-policy.md
│   └── remote-work-policy.md
├── product-docs/
│   ├── api-reference.md
│   ├── authentication-guide.md
│   └── webhook-setup.md
└── onboarding/
    ├── first-day-checklist.md
    └── systems-setup.md
```

### Step 3: Review Each File

For each file, ensure:
- **Title is clear** (what is this?)
- **Sections have headers** (H2, H3 hierarchy)
- **Keywords appear early** (don't bury key info)
- **No orphaned references** (use Related Topics section)
- **Format is clean** (markdown or plain text, not mixed)

### Step 4: Upload to GPT

1. Go to Configure tab
2. Click "Add files" under Knowledge
3. Upload files (up to 20)
4. Test retrieval (ask the GPT questions that should pull from files)

### Step 5: Test Retrieval

Ask your GPT test questions:

```
Test 1: "What's the vacation policy?"
Expected: GPT retrieves vacation-policy.md, answers question
Actual: ___________

Test 2: "How do I set up webhooks?"
Expected: GPT retrieves webhook-setup.md
Actual: ___________

Test 3: "What's the salary?"
Expected: GPT says "That's not in my knowledge base"
Actual: ___________
```

If retrieval fails, rewrite that section of the file (make keywords more prominent, add context).

---

## Advanced: Optimizing for Your Use Case

### For Q&A GPT

Structure files as FAQ:

```markdown
# Support Q&A

## Billing Questions

### Q: How do I update my payment method?
A: [Clear steps]

### Q: What payment methods do you accept?
A: [List]

### Q: Can I get a refund?
A: [Policy]

## Account Questions

### Q: How do I change my password?
A: [Steps]
```

GPT will find answers quickly with this format.

### For Analysis/Research GPT

Structure as summaries + citations:

```markdown
# Market Research 2024

## Key Findings
1. Market size grew 15% YoY
2. Top players: Company A (35%), Company B (28%)
3. Emerging trend: AI-driven automation

## Detailed Analysis

### Market Size
[Paragraph with data and sources]
Citations: Industry Report Q4 2024, p. 12

### Competitive Landscape
[Paragraph with analysis]
Citations: Competitor A's 10-K filing, p. 45
```

GPT can cite sources when it retrieves this.

### For Instruction/Guide GPT

Structure with steps + examples:

```markdown
# How to Deploy on AWS

## Quick Start (5 min)
1. Create S3 bucket
2. Upload files
3. Done

## Full Guide

### Prerequisites
- AWS account
- AWS CLI installed

### Step 1: Create S3 Bucket
```bash
aws s3 mb s3://my-bucket
```

### Step 2: Upload Files
```bash
aws s3 sync ./local-folder s3://my-bucket
```

### Troubleshooting
Common issues and fixes...

### Examples
- Deploying a static website
- Uploading large files
- Setting up CDN
```

Clear steps + examples help GPT give step-by-step instructions.

---

## Size Guidelines

| File Size | Recommendation |
|---|---|
| < 10 pages | Upload as-is |
| 10–50 pages | Ideal size |
| 50–100 pages | Upload if focused; split if mixed topics |
| > 100 pages | Split into multiple files by chapter/section |

---

## Maintenance

### Update Outdated Files

If Knowledge becomes stale:

1. Delete the old file (Configure → Knowledge → Delete)
2. Upload the new version
3. Test retrieval with updated info

### Add New Topics

As your GPT's job evolves:

1. Create new Knowledge file
2. Upload it
3. Update Instructions if needed (add mention of new topic)

### Remove Unused Files

If users never ask about certain topics:

1. Remove file from Knowledge
2. Simplify GPT if relevant sections of Instructions reference it

---

**Next**: See [Monitoring & Optimization](14-monitoring-optimization.md) to measure how well your Knowledge base is being used.
