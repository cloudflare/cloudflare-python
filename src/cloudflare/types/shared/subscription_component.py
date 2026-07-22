# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SubscriptionComponent"]


class SubscriptionComponent(BaseModel):
    """A component value for a subscription."""

    default: Optional[float] = None
    """The default amount assigned."""

    display_name: Optional[str] = None
    """A human-readable version of the component name."""

    kind: Optional[Literal["enum", "sum", "usage"]] = None
    """The type of component value.

    "enum" for discrete values (including boolean on/off toggles where 0=off and
    1=on), "sum" for countable quantities, "usage" for metered billing components.
    """

    name: Optional[str] = None
    """The name of the component value."""

    price: Optional[float] = None
    """The unit price for the component value."""

    value: Optional[float] = None
    """The amount of the component value assigned."""
