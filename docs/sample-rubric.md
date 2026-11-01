# Sample review rubric

This illustrative rubric accompanies the demonstration exercise. It does not reproduce an active hiring scorecard. Review the work and the engineer's explanation together; avoid treating test count as a complete assessment.

| Dimension | Evidence to look for | Follow-up when evidence is incomplete |
|---|---|---|
| Functional ownership | A coherent path from request to policy decision, including missing and failing tools | Walk through a failure that the happy path does not cover |
| Trust boundaries | Caller-provided identity, customer-scoped lookup, no claim-based authentication | Explain what prevents a user from requesting another customer's order |
| Verification | Tests assert unwanted effects do not occur, not only that an answer exists | Show how a plausible regression would be caught |
| Operational judgment | Useful categorical traces, clear limitations, safe rollout thinking | Propose a signal that would distinguish failure modes in production |
| Communication and AI-assisted ownership | Specific design rationale, honest omissions, ability to explain accepted code | Explain one coding-agent suggestion you changed or rejected |

Use qualitative notes for each dimension: **demonstrated**, **partially demonstrated**, or **needs more evidence**. Cite the relevant code, test result, or discussion. An uncertain judgment should result in a focused follow-up, not an invented conclusion.

## Example evidence note — synthetic

> The implementation checks session identity before calling the order tool, and its test verifies that no tool call occurs for an unauthenticated request. The reference also rechecks the returned owner. This demonstrates an explicit trust boundary within the limits of the simulated session.

## Human decision

Review assistance can organize evidence. A human reviewer remains responsible for interpretation and any hiring decision. Do not infer personal characteristics from coding style or score people on characteristics unrelated to the task.
