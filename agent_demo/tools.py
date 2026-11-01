from copy import deepcopy

SHIPPING_POLICY = "Standard shipping takes 3–5 business days after dispatch."

# Synthetic fixtures. No names, email addresses, phone numbers, or real accounts.
_ORDERS = {
    "TH-1001": {"order_id": "TH-1001", "customer_id": "demo-customer", "status": "processing"},
    "TH-1002": {"order_id": "TH-1002", "customer_id": "demo-customer", "status": "shipped"},
    "TH-1003": {"order_id": "TH-1003", "customer_id": "other-demo-customer", "status": "processing"},
    "TH-1004": {"order_id": "TH-1004", "customer_id": "demo-customer", "status": "delivered"},
}


def lookup_order(order_id: str, customer_id: str) -> object:
    """Apply customer scoping in the tool as well as validating it in the caller."""
    order = _ORDERS.get(order_id)
    if not order or order["customer_id"] != customer_id:
        return None
    return deepcopy(order)
