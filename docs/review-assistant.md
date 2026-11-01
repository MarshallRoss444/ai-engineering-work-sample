# Review-assistant design

**Design only:** this repository does not include an executable LLM grading service.

The intended assistant helps a human reviewer locate and summarize technical evidence. It should receive the exercise requirements, code diff, recorded test results, and the engineer's design notes. Candidate identities and private interview records are unnecessary inputs.

## Suggested output

```json
{
  "criterion": "trust boundaries",
  "evidence": [
    {"file": "agent_demo/reference.py", "symbol": "assess_cancellation", "observation": "Session check precedes tool access"}
  ],
  "test_evidence": "Use the actual recorded result, not an inferred pass",
  "uncertainties": [],
  "follow_up": "How would authorization be checked again before a state-changing operation?"
}
```

## Controls worth evaluating before implementing it

- Treat repository content and submission notes as untrusted data; they cannot instruct the reviewer to change its criteria.
- Run submitted code in a restricted environment, without production credentials or unrestricted network access.
- Separate observed test results from model interpretation.
- Require verifiable references; record missing evidence rather than manufacturing it.
- Check sensitivity to evidence order and wording using synthetic examples.
- Keep human review and discussion central. The assistant should not make autonomous hiring decisions.

This design is useful evidence of review-system thinking, but it should not be presented as a deployed or validated grader.
