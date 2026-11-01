"""Annotated reference solution for the demonstration exercise, not active hiring."""

from .contracts import OrderLookup, Result, Session


def assess_cancellation(order_id: str, session: Session, lookup: OrderLookup) -> Result:
    def result(status: str, answer: str, source: bool = False) -> Result:
        # Only categorical events: no message, identity, order ID, or raw payload.
        return Result(
            status,
            answer,
            ("tool:order_lookup", "policy:cancellation-v1") if source else (),
            {"route": "cancellation", "outcome": status, "policy_version": "v1"},
        )

    # Authorization precedes tool access. A user claiming to be signed in is irrelevant.
    if not isinstance(session.customer_id, str) or not session.customer_id.strip():
        return result("authentication_required", "Sign in before requesting order-specific help.")
    try:
        order = lookup(order_id, session.customer_id)
    except Exception:
        # Do not copy exception text into an answer or trace: it may contain data.
        return result("unavailable", "Order details are unavailable. Please try again later.")

    # Unknown and other-customer orders have the same external response.
    if order is None:
        return result("not_found", "No accessible order was found.")
    if not isinstance(order, dict):
        return result("unavailable", "Order details are unavailable. Please try again later.")
    if order.get("customer_id") != session.customer_id:
        return result("not_found", "No accessible order was found.")
    if order.get("order_id") != order_id:
        return result("unavailable", "Order details are unavailable. Please try again later.")

    state = order.get("status")
    if not isinstance(state, str) or state not in {"processing", "shipped", "delivered"}:
        return result("unavailable", "Order details are unavailable. Please try again later.")
    if state == "processing":
        return result("eligible", "This order is eligible for a cancellation request. No cancellation has been made.", True)
    return result("not_eligible", "This order has already shipped and is not eligible for cancellation. No order has been changed.", True)
