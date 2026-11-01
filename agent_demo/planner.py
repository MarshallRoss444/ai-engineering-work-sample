"""Small, explicitly limited deterministic router. No model inference."""

import re
from dataclasses import dataclass

ORDER_PATTERN = re.compile(r"\bTH-\d{4}\b", re.IGNORECASE)
CANCEL_PATTERN = re.compile(r"\b(cancel\w*|stop|halt)\b", re.IGNORECASE)


@dataclass(frozen=True)
class Plan:
    route: str
    order_id: str | None = None


def plan(message: str) -> Plan:
    ids = sorted(set(m.upper() for m in ORDER_PATTERN.findall(message)))
    if CANCEL_PATTERN.search(message):
        if len(ids) != 1:
            return Plan("clarify_order")
        return Plan("cancellation", ids[0])
    if "shipping" in message.lower() or "delivery time" in message.lower():
        return Plan("shipping_policy")
    return Plan("unsupported")
