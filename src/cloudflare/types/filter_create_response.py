# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["FilterCreateResponse", "FilterCreateResponseItem"]


class FilterCreateResponseItem(BaseModel):
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


FilterCreateResponse = List[FilterCreateResponseItem]
