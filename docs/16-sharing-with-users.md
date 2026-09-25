# Sharing Your GPT with Users

How to share your Custom GPT so users can ask questions and get answers based on your knowledge.

## The Three Sharing Levels

When you publish a Custom GPT, you choose **who can access it**:

### 1. Only Me (Private)

- **Who can access**: Only you (the creator)
- **Use case**: Testing, development, personal use
- **URL**: Not shareable (no link works)
- **Best for**: Before launch, while building

### 2. Anyone with a Link (Shareable)

- **Who can access**: Anyone you give the link to
- **Use case**: Business team, paying customers, trusted group
- **URL**: https://chatgpt.com/g/g-[ID] (you control who knows it)
- **Best for**: Business use, private access for specific users

### 3. GPT Store (Public)

- **Who can access**: Anyone can find and use it
- **Use case**: Public tools, published expertise, open source
- **URL**: Listed in GPT Store, searchable
- **Best for**: Public audience, thought leadership

---

## How to Share (Step-by-Step)

### Step 1: Publish Your GPT

1. In the Builder, click **Create** (top right)
2. Choose visibility level:
   - **Only me** → just testing
   - **Anyone with a link** → share specific URL with team/customers
   - **GPT Store** → make it public (searchable)
3. Click **Publish**

### Step 2: Get the Shareable Link

Once published, your GPT has a unique URL:

```
https://chatgpt.com/g/g-ABC123XYZ
```

**Find it**:
1. Go to [chatgpt.com/gpts/your-gpts](https://chatgpt.com/gpts/your-gpts)
2. Find your GPT in the list
3. Click the three dots (...) → **Copy link**

### Step 3: Share with Users

**Send them**:
- The link: `https://chatgpt.com/g/g-ABC123XYZ`
- Brief instructions: "Click the link, then ask me questions about [topic]"

**Users do this**:
1. Click the link (no login required)
2. ChatGPT opens with your GPT active
3. They type a question in the chat
4. Your GPT answers based on the knowledge you've provided

---

## User Access Workflow

### What Users See

When a user opens your GPT link:

```
┌─────────────────────────────────────────┐
│  [Your GPT Name]                        │
│  [Your description]                     │
│                                         │
│  [4 conversation starters you set]      │
│                                         │
│  Message input: "Ask me anything..."    │
└─────────────────────────────────────────┘
```

### How Users Ask Questions

They can:
1. **Click a starter** — one of your pre-written example questions
2. **Type their own** — ask anything related to your GPT's knowledge
3. **Upload files** — if you enabled file upload in Instructions

### What Users Get

Your GPT answers based on:
- **Knowledge files** you uploaded (the cleaned documents)
- **Instructions** you wrote (the rules and tone)
- **Training data** (GPT-4's general knowledge, supplemented by your files)

---

## Best Practices for Sharing

### For Business Teams (Internal Use)

**Visibility**: "Anyone with a link"

**Share via**:
- Email: "Here's our company knowledge GPT: [link]"
- Slack: Pinned message with the link
- Wiki/docs: "For X, ask our GPT: [link]"
- Onboarding: New employees get the link on day 1

**Tell them**:
```
Hi team,

I've built a Custom GPT that answers questions about our [policies/products/processes].
Access it here: [link]

Just ask it anything, and it'll pull from our official docs.
Much faster than searching wikis!
```

### For Customers (Subscription Model)

**Visibility**: "Anyone with a link" (you control distribution)

**Share via**:
- Email after signup: "Welcome! Here's access to our help GPT: [link]"
- Customer portal: Link in dashboard
- Documentation: "For quick answers, try our GPT: [link]"

**Tell them**:
```
Your Custom GPT is ready!

It answers questions about:
- How to use our product
- Troubleshooting common issues
- Billing and subscriptions

Just ask it anything: [link]

For complex issues, you can still reach support@company.com
```

### For Public Use (GPT Store)

**Visibility**: "GPT Store"

**Share via**:
- Marketing materials: "Download our free GPT from the GPT Store"
- Twitter/LinkedIn: "Excited to announce our new Custom GPT: [link]"
- Website: "Try our AI assistant: [link]"

**Tell them**:
```
We've built a Custom GPT for [your expertise].

It's free, no login required, and trained on [what you're an expert in].

Try it here: [link]
```

---

## What Happens When Users Ask Questions

### Real Example

**User asks**:
```
"What's your vacation policy?"
```

**Your GPT**:
1. Searches your Knowledge files for "vacation"
2. Finds the vacation policy document
3. Extracts the relevant answer
4. Responds in the tone you specified

**Answer**:
```
"You're entitled to 20 days of vacation per year. 
To request time off, submit to your manager 2 weeks in advance.
See the full policy for details about rollovers and blackout dates."
```

The user gets an answer **instantly**, based on your knowledge.

---

## Updating After Launch

Once shared, you can still:

**Update Knowledge**:
- Add new files (Configure → Knowledge → Add files)
- Remove old files (Configure → Knowledge → Delete)
- Changes take effect immediately

**Update Instructions**:
- Edit tone, rules, process
- Changes take effect immediately
- Existing conversations with users don't change

**Update Conversation Starters**:
- Change the 4 suggested opening questions
- Only affects new conversations

**Monitor Usage** (limited):
- ChatGPT shows thumbs up/down feedback on responses
- You can see this in the GPT settings

---

## Troubleshooting User Access

### User Can't Open the Link

**Problem**: "This link doesn't work" or "404 not found"

**Cause**: GPT not published yet or wrong visibility setting

**Fix**:
1. Confirm GPT is published (Configure tab → save)
2. Check visibility is "Anyone with a link" or "GPT Store"
3. Resend the correct link

### User Opens It But It's Wrong GPT

**Problem**: User clicks link, gets a different GPT

**Cause**: Link is old or from wrong GPT version

**Fix**:
1. Go to [chatgpt.com/gpts/your-gpts](https://chatgpt.com/gpts/your-gpts)
2. Find your GPT
3. Copy the fresh link (three dots → Copy link)
4. Resend to user

### User Says GPT Doesn't Know [Topic]

**Problem**: User asks about something, GPT says "I don't know"

**Cause**: Topic not in Knowledge files or Instructions

**Fix**:
1. Check if the topic is in your Knowledge files
2. If not, add a file covering that topic
3. Wait a few seconds for index to update
4. User asks again

---

## Sharing Levels Comparison

| Feature | Only Me | Anyone with Link | GPT Store |
|---|---|---|---|
| **Access** | You only | Link users | Anyone |
| **Best for** | Testing | Business | Public |
| **Login needed** | — | No | No |
| **Discoverable** | No | No | Yes (searchable) |
| **Can share** | No | Yes (give link) | Yes (anyone finds it) |
| **Modify after** | Yes | Yes | Yes |

---

## Security & Privacy Reminders

### What Users Can See

Users can:
- See your GPT name and description
- Access your Knowledge files (they can ask the GPT to quote them)
- See your tone and personality (from Instructions)

Users **cannot**:
- See your Instructions (only the effect)
- Download your Knowledge files directly
- Access the "Configure" screen

### What Users Cannot Do

- They can't modify your GPT
- They can't see who else is using it
- They can't access other GPTs from yours

---

## Next Steps

1. **Publish your GPT** (Choose visibility → Publish)
2. **Copy the link** (your-gpts → find it → copy link)
3. **Share with users** (send the link + brief explanation)
4. **Users ask questions** (they click link, ask in chat)
5. **Monitor & iterate** (update Knowledge as needed)

---

**That's it.** Your users now have instant access to your expertise via ChatGPT.
