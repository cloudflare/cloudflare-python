# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FirewallFilter"]


class FirewallFilter(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the filter."""

    description: Optional[str] = None
    """An informative summary of the filter."""

    expression: Optional[str] = None
    """The filter expression.

    For more information, refer to
    [Expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/).
    """

    paused: Optional[bool] = None
    """When true, indicates that the filter is currently paused."""

    ref: Optional[str] = None
    """A short reference tag. Allows you to select related filters."""
