# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["FilterGetResponse"]


class FilterGetResponse(BaseModel):
    id: str
    """The unique identifier of the filter."""

    expression: str
    """The filter expression.

    For more information, refer to
    [Expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/).
    """

    paused: bool
    """When true, indicates that the filter is currently paused."""

    description: Optional[str] = None
    """An informative summary of the filter."""

    ref: Optional[str] = None
    """A short reference tag. Allows you to select related filters."""
