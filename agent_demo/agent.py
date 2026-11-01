from . import cancellation, reference, tools
from .contracts import OrderLookup, Result, Session
from .planner import plan


def run(message: str, session: Session | None = None, *, mode: str = "starter", lookup: OrderLookup | None = None) -> Result:
    if mode not in {"starter", "reference"}:
        raise ValueError("mode must be starter or reference")
    session = session if session is not None else Session()
    next_step = plan(message)
    if next_step.route == "shipping_policy":
        return Result("answered", tools.SHIPPING_POLICY, ("policy:shipping-v1",), {"route": "shipping_policy"})
    if next_step.route == "clarify_order":
        return Result("clarification_required", "Please provide exactly one order ID, such as TH-1001.", trace={"route": "clarify_order"})
    if next_step.route == "cancellation":
        handler = reference.assess_cancellation if mode == "reference" else cancellation.assess_cancellation
        return handler(next_step.order_id, session, lookup if lookup is not None else tools.lookup_order)
    return Result("unsupported", "I can explain shipping policy or check whether an order is eligible for cancellation.", trace={"route": "unsupported"})
