from .contracts import OrderLookup, Result, Session


def assess_cancellation(order_id: str, session: Session, lookup: OrderLookup) -> Result:
    """Exercise target: implement the read-only cancellation eligibility path."""
    return Result(
        "not_implemented",
        "Cancellation eligibility is the exercise task; no order has been changed.",
        trace={"route": "cancellation", "outcome": "not_implemented"},
    )
