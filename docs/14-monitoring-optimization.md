# Monitoring & Optimization

How to see what's working and improve your GPT over time.

## Built-In Metrics

ChatGPT doesn't provide detailed analytics, but you can gather feedback through:

### Conversation Feedback

In the ChatGPT interface, users can thumbs-up or thumbs-down responses. This data is visible only to you (private).

**What to do**:
- Monitor thumbs-down feedback
- When you get consistent thumbs-downs on a type of question, adjust Instructions
- Test the fix in a new conversation

### Example Workflow

```
1. You notice multiple thumbs-downs on tone ("too formal")
2. Edit Instructions to change tone ("Use casual, friendly language")
3. Test with a new conversation
4. Monitor if thumbs-downs decrease
```

---

## Manual Testing

### Test Scenarios

Regularly test your GPT with real questions:

```
Monthly Test Suite:

Core Function Tests:
- [ ] "Main use case #1" — expected: [what it should do]
- [ ] "Main use case #2" — expected: [what it should do]
- [ ] "Boundary case" — expected: [what it should do]

Quality Tests:
- [ ] Tone check: Does it sound like I want?
- [ ] Length check: Is output too long/short?
- [ ] Knowledge check: Is it using Knowledge files correctly?
- [ ] Accuracy check: Is it factually correct?

Edge Case Tests:
- [ ] Out of scope: What does it do?
- [ ] Ambiguous input: Does it ask for clarification?
- [ ] Adversarial prompt: Does it stay on task?
```

### Tracking Results

Keep a simple log:

```markdown
# Testing Log

## 2024-01-15
- Test: "Recommend sci-fi book"
  Result: ✓ Suggested 3 books, good pitches
  
- Test: "Recommend non-fiction"
  Result: ✗ Didn't redirect, gave recommendations
  Action: Strengthen "fiction only" rule in Instructions

## 2024-01-22
- Test: "Recommend non-fiction" (retry)
  Result: ✓ Politely redirected
  
- Test: "Too long books?"
  Result: ✓ Correctly handled edge case
```

---

## Iterative Improvement

### Change 1 Thing at a Time

Avoid making multiple changes at once:

❌ Bad: Rewrite Instructions, add new Knowledge files, change conversation starters all together

✓ Good:
1. Change Instructions
2. Test for 2 weeks
3. If good, move on
4. If not, revert and try differently

### Measure Impact

After a change, test with same scenarios:

```
Before: Recommended books, but 3/5 feedback votes were neutral
Change: Made tone less formal, added more personality
After: Still recommended books, but 5/5 feedback votes were positive
Result: ✓ Improve tone
```

---

## Specific Optimizations

### If Users Don't Get What They Need

**Symptom**: Users often ask follow-up clarifying questions

**Fix**: Instructions need clearer process
```
Add to Instructions:
"When the user's request is unclear, ask exactly these questions:
1. 'What's your specific goal with this?'
2. 'Any preferences I should know about?'
3. 'How much time/effort can you invest?'"
```

### If Responses Are Wrong

**Symptom**: Factual errors or hallucinations

**Fix**: Either reduce scope or add more Knowledge
```
Option 1 (Reduce scope): Narrow what GPT claims to do
"Focus only on questions answered in Knowledge files.
If not in Knowledge, say 'I don't have that information.'"

Option 2 (Add Knowledge): Provide missing information
Upload a Knowledge file covering the topic
```

### If Knowledge Isn't Used

**Symptom**: GPT gives generic answers instead of using Knowledge

**Fix**: Make Knowledge more prominent and test retrieval
```
1. Check if files are actually uploaded (Configure → Knowledge)
2. Test with questions that directly reference file content
3. Add to Instructions: "Always cite the specific document you're referencing"
4. If still not used, rewrite file headers (make them clearer)
```

### If Tone Is Off

**Symptom**: Too formal, too casual, or inconsistent

**Fix**: Rewrite tone examples in Instructions
```
Instead of: "Be friendly"
Write: "Use casual language. Say 'Yeah, I'd suggest...' not 'I would 
recommend...'. Use contractions like 'I'd' and 'don't'."
```

### If Output Format Is Inconsistent

**Symptom**: Sometimes bullet points, sometimes paragraphs

**Fix**: Explicit output format in Instructions
```
"Always structure recommendations as:
- Title: [name]
- Why: [one sentence on why this fits]
- Note: [any caveats]"
```

---

## Performance by Use Case

### Recommendation GPT

**Track**:
- Do users ask "Any others like this?" (indicator: algorithm good but scope too narrow)
- Do users return? (indicator: quality good)
- Do recommendations match user preferences? (test manually monthly)

**Optimize**:
- If scope too narrow: Broaden categories
- If off-topic: Add clarifying questions to process
- If not memorable: Make pitches punchier

### Analysis/Expert GPT

**Track**:
- Do analyses seem thorough? (test with complex questions)
- Are citations/sources correct? (verify manually)
- Accuracy on domain knowledge? (test quarterly)

**Optimize**:
- If surface-level: Add more detailed Knowledge
- If hallucinating sources: Strengthen "only cite what you know" instruction
- If outdated: Refresh Knowledge files quarterly

### Writing Assistant GPT

**Track**:
- Does output match requested tone? (test with different tones monthly)
- Does it preserve user's voice? (test with personal writing)
- Is it better than user's original? (subjective, but track manually)

**Optimize**:
- If tone off: Rewrite tone examples
- If loses user's voice: Add "preserve original style" to Instructions
- If output too short/long: Add length guidance

---

## Quarterly Review

Every 3 months, do a full audit:

```markdown
# Q1 2024 Review

## Usage
- Approximate conversations: ~200/month
- Approximate users returning: ~30% (OK)
- Feedback: ~50 thumbs-down, 200 thumbs-up (4:1 good ratio)

## Performance by Use Case
- Recommendation requests: Strong (high thumbs-up)
- Analysis requests: Weak (high thumbs-down)
- Writing help: Good (positive feedback)

## Top Issues
1. Analysis GPT sometimes misses nuance (fix: add more Knowledge examples)
2. Tone sometimes too formal (fix: make Instructions more casual)
3. Knowledge files not always used (fix: rewrite file headers)

## Planned Changes for Q2
1. Split analysis instructions into "quick summary" vs "detailed"
2. Add 3 new Knowledge files on emerging trends
3. Rewrite 2 conversation starters to better show use cases

## Metrics
- Thumbs-up ratio: 80% (target: 85%)
- User return rate: 30% (target: 40%)
- Knowledge retrieval rate: 60% (target: 80%)
```

---

## Sharing & Feedback

### With Friends (Trusted Testing)

```
Email to friend:
"I built a GPT that recommends books for book clubs. 
Try it and let me know:
1. Did it understand what you wanted?
2. Were the recommendations good?
3. Anything confusing about how it works?
4. Would you use this?"
```

### Public Feedback (if in GPT Store)

Monitor:
- Store reviews/ratings
- Conversation feedback (thumbs up/down)
- Common questions/complaints

Respond to feedback:
- Negative review → See if it points to a fixable issue
- Low rating → Audit that GPT's performance
- Common complaint → Fix Instructions or Knowledge

---

## Version History

Keep track of changes:

```markdown
# GPT Versions

## v1.0 (Jan 1)
Initial launch
- 3 conversation starters
- No Knowledge files
- Focused on book recommendations

## v1.1 (Jan 8)
Added scoping
- Users complained about non-fiction recommendations
- Added rule: "Fiction only"
- Result: Thumbs-up ratio improved 70% → 85%

## v1.2 (Jan 15)
Improved tone
- Changed from formal to casual
- Added contractions and friendly language
- Result: Users said "friendlier" in feedback

## v1.3 (Feb 1)
Added Knowledge
- Uploaded list of 2024 bestsellers
- Updated Instructions to cite Knowledge
- Result: Recommendations now reference specific books
```

---

## Advanced: Analytics Integration (Optional)

If you want detailed analytics, create a logging system:

1. **After each conversation**, user clicks "Save this" button
2. **Feedback form**: "Was this helpful? Why/why not?"
3. **You aggregate** feedback in a spreadsheet

```
Date | Question Type | Was Helpful? | Feedback | Fix Needed?
------|---|---|---|---
Jan 1 | Recommendation | Yes | Good variety | No
Jan 1 | Recommendation | No | Too literary | Broaden appeal
Jan 2 | Analysis | Yes | Thorough | No
Jan 2 | Analysis | No | Missing context | Add Knowledge
```

Over time, you see patterns.

---

**Remember**: Custom GPTs improve through iterative testing and user feedback. Start simple, measure, adjust, repeat.
