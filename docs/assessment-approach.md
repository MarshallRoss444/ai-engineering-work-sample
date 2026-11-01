# One system, different levels of judgment

The original assessment approach separates three kinds of evidence. This portfolio edition illustrates that approach without including active interview packets or reviewer-only answers.

| Level of work | Representative extension to this demo | Discussion focus |
|---|---|---|
| Scoped implementation | Add a clearly bounded public policy lookup and test it | Understanding the repository, contracts, and a small change |
| End-to-end ownership | Complete the cancellation-eligibility path described in the exercise | Trust boundaries, tool failures, verification, and release readiness |
| System-level leadership | Review whether read-only eligibility advice should become a state-changing cancellation capability | Authorization, confirmation, idempotency, stale state, monitoring, rollback or compensating actions, and team ownership |

The senior discussion does not require writing a larger quantity of code. A written analysis that prioritizes concrete risks and connects recommendations to evidence can be sufficient. An optional small patch may support the reasoning.

## Why use work samples?

A shared task gives interviewers something concrete to discuss. The follow-up matters: an engineer should explain choices, recognize limitations, and adapt when a requirement changes. A passing test suite alone cannot establish those capabilities.

Keep setup separate from the exercise, communicate the timebox, allow coding agents, and avoid requiring paid model access. Make success criteria visible while reserving active assessment details for the actual hiring process.

## Relevance to forward deployment

The sample starts from a customer need, translates it into acceptance criteria, and exposes practical integration and operating decisions. For a delivery leader, the useful evidence includes how an engineer clarifies scope, communicates risk, and defines a credible next release—not just whether they can generate code.
