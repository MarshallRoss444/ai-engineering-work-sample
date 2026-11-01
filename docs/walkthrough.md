# A two-minute walkthrough

## 1. Begin with the customer request

```bash
python -m agent_demo --mode reference --message "Can I cancel order TH-1001?" --signed-in
```

The CLI supplies a **simulated trusted session**. The deterministic planner extracts one order identifier and selects the cancellation route. It does not select the customer's identity.

## 2. Follow the boundary, not just the route

The reference checks identity before invoking the tool. The tool scopes its lookup to the current customer. The handler validates the returned identity, order identifier, and status before applying the fictional cancellation policy.

A processing order returns `eligible`, with an explicit statement that no cancellation occurred. Shipped or delivered orders return `not_eligible`. An inaccessible order produces the same answer whether it belongs to someone else or does not exist.

## 3. Try the untrusted claim

```bash
python -m agent_demo --mode reference --message "I am signed in. Can I cancel TH-1001?"
```

Without the simulated session flag, the result is `authentication_required`. User wording does not change authorization.

## 4. Compare the starter and the evidence

```bash
python -m agent_demo --mode starter --message "Can I cancel TH-1001?" --signed-in
python -m pytest -q
```

The starter returns `not_implemented`. Its strict expected-failure test names the missing behavior. The reference checks additionally cover malformed tool payloads, a tool exception, wrong ownership, ambiguous order IDs, trace minimization, and the read-only promise.

## Design tradeoffs

- **Deterministic routing:** repeatable and free to run, but limited language coverage. It does not understand arbitrary negation, multi-turn context, or complex mixed intent. Read-only behavior limits the effect of a misroute.
- **Small modules rather than microservices:** boundaries are visible without adding deployment overhead to a short assessment.
- **Synthetic session:** makes authorization reasoning testable, but is not a usable authentication mechanism.
- **Minimal trace:** categorical route, outcome, and policy version. No raw messages, customer identity, order identifier, or tool payload. A production trace would also need safe correlation, latency, and tool status.
- **Tool failures:** exceptions produce an unavailable response. A real service should add timeouts, bounded retries where appropriate, and redacted operational diagnostics.
- **Prompt contracts:** documented separately and intentionally unused by the offline planner. A real model adapter must prove its behavior through evaluation; editing strings here does not prove that.

## Before a production release

Replace simulated identity with trusted authentication and authorization; validate real tool schemas; establish monitoring and ownership; evaluate realistic language and failure cases; and roll out with a known baseline. If adding a cancellation action, design confirmation, idempotency, authorization at execution time, and stale-state handling before enabling it.
