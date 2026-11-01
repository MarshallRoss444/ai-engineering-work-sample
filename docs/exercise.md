# Demonstration exercise: cancellation eligibility

This is a portfolio example. The solution and review criteria are intentionally available for inspection. It is not a confidential hiring assessment.

## The customer problem

Trailhead Supply shoppers need to know whether they can request cancellation of an order. The assistant already answers public shipping-policy questions. Its cancellation handler is deliberately incomplete.

Implement `agent_demo/cancellation.py` without changing the public response contract. Use `python -m agent_demo --mode starter` to try your work. The independent reference implementation is provided for reviewers; someone using this as a learning exercise can defer reading it until afterward.

## Acceptance criteria

1. Public shipping guidance works without signing in.
2. Order-specific information requires a caller-supplied session. User text claiming to be authenticated is not proof.
3. Look up an order only within that session's customer scope. Do not disclose whether another customer's order exists.
4. Only a `processing` order is eligible for a cancellation request. `shipped` and `delivered` orders are ineligible.
5. Unknown orders, malformed tool results, and tool errors produce useful, bounded responses.
6. The assistant advises; it does not cancel an order or imply that it did.
7. Responses and traces exclude raw order payloads, identities, and internal-only fields.

## Deliverables

- A working starter implementation and focused tests.
- A brief design note describing trust boundaries, failure handling, and known limitations.
- A proposed production release check and one useful operational signal.

For self-study, allow up to 90 minutes and stop at that point. Incomplete work plus clear prioritization is useful evidence. There is no expectation to spend additional unpaid time.

AI coding tools are welcome. Explain which decisions they helped with, what you reviewed, and how you verified the result. Be prepared to explain every submitted change.

## What this exercise does not test

It does not measure live-model reasoning, prompt effectiveness, distributed-service operation, or actual identity verification. Those require different evidence. The CLI session flag is only a local simulation.

## Suggested follow-up

- Why does the application supply customer identity rather than the planner?
- How would you distinguish tool failures from legitimate missing orders in operational traces without exposing customer data?
- What would change if the assistant could actually cancel an order?
- What evidence would you require before replacing deterministic routing with a live model?
