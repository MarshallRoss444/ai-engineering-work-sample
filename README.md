# AI Engineering Work Sample

**A small, runnable demonstration of how to assess agent engineering and production judgment.**

This portfolio edition uses a fictional outdoor-equipment retailer, Trailhead Supply. An offline Python assistant answers public shipping questions and helps a signed-in shopper determine whether an order is eligible for cancellation. It never changes an order.

I designed and built the original engineering work-sample system end to end, using coding agents as part of my development workflow. My work covered the exercise design, Python orchestration framework, example tools, tests, rubric, and review workflow. I own the engineering decisions, review, and validation.

This portfolio edition adapts that work into newly written scenarios and a sample rubric rather than publishing active hiring materials.

## Start here — two minutes

1. Read the [exercise](docs/exercise.md): turn a cancellation request into a safe, reviewable feature.
2. Compare the intentionally incomplete [starter](agent_demo/cancellation.py) with the [reference implementation](agent_demo/reference.py).
3. Read the [walkthrough](docs/walkthrough.md) and [sample rubric](docs/sample-rubric.md): what evidence matters beyond passing tests?

```text
Request + simulated trusted session
                |
     deterministic intent routing
          /                 \
 Public shipping       Order cancellation
 policy lookup         auth + ownership check
                              |
                       validate tool result
                              |
                       policy eligibility
          \                 /
       Structured answer + minimal trace
```

## Run locally

Python 3.11 or later. The demo uses only the Python standard library. Tests require pytest.

```bash
python -m agent_demo --mode reference --message "Can I cancel order TH-1001?" --signed-in
python -m agent_demo --mode reference --message "What is your shipping policy?"
python -m agent_demo --mode starter --message "Can I cancel order TH-1001?" --signed-in
```

Install and run the checks in a virtual environment:

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

The starter has one **strict expected failure** for the deliberately missing cancellation feature. The reference implementation must pass all its checks. Finishing the exercise means implementing the starter and removing that marker, not changing the assertions to accept missing behavior.

## Why deterministic by default?

The exercise requires no model subscription, API key, paid inference, or company credentials. Reviewers get repeatable behavior while assessing routing, tool contracts, context boundaries, failure handling, and communication.

This is not a live LLM benchmark. Prompt templates are illustrative contracts; they do not control the deterministic runtime. Keyword checks cannot establish prompt quality. A future live-model adapter would need separate behavioral evaluations, model/version reporting, repeated runs, and controlled tool access.

## What this demonstrates

- **Hands-on engineering:** small Python modules, typed data contracts, injectable tools, explicit failure paths, and executable checks.
- **Hiring judgment:** a bounded implementation task paired with structured discussion; AI assistance is welcome, ownership is required.
- **Enterprise delivery:** clarify acceptance criteria, separate trusted session state from user claims, minimize traces, and define what is safe to release.
- **Leadership:** use different follow-up questions for scoped implementation, feature ownership, and system-level review. See the [assessment approach](docs/assessment-approach.md).

## Scope and limitations

All business data is synthetic. The `--signed-in` flag simulates an upstream authenticated session for a local exercise; it is not authentication. The reference implements read-only eligibility advice, not cancellation, identity management, comprehensive prompt-injection protection, or production readiness. It has no external model, account, telemetry service, or network dependency at runtime.

The [prompt contracts](agent_demo/prompts.py) describe how a future model adapter could receive a bounded role and tool contract. Authorization and policy decisions belong in application code regardless of model choice.

## Repository map

| Path | Purpose |
|---|---|
| `agent_demo/` | Offline assistant, synthetic tools, starter, and reference path |
| `tests/` | Baseline, exercise-target, and reference behavioral checks |
| `docs/exercise.md` | Candidate-style demonstration task |
| `docs/sample-rubric.md` | Illustrative evidence-based review criteria |
| `docs/walkthrough.md` | Request flow, examples, and design tradeoffs |
| `docs/review-assistant.md` | Human-led review-assistant design, not an implemented grading service |
| `docs/validation.md` | Recorded validation and known limits |

This is an independent portfolio project, not an assessment supplied or endorsed by any employer or model provider.
