from dataclasses import asdict, dataclass, field
from typing import Callable


@dataclass(frozen=True)
class Session:
    """Trusted input supplied by the caller; never inferred from user text."""

    customer_id: str | None = None


@dataclass(frozen=True)
class Result:
    status: str
    answer: str
    sources: tuple[str, ...] = ()
    trace: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)


# The customer scope is part of the tool contract, not an LLM-supplied identity.
OrderLookup = Callable[[str, str], object]
