# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Route", "Value"]


class Value(BaseModel):
    type: Optional[Literal["temporary", "permanent"]] = None
    """The response type for the URL redirect."""

    url: Optional[str] = None
    """
    The URL to redirect the request to. Notes: ${num} refers to the position of '\\**'
    in the constraint value.
    """


class Route(BaseModel):
    modified_on: Optional[datetime] = None
    """The timestamp of when the override was last modified."""

    name: Optional[Literal["forward_url"]] = None
    """The type of route."""

    value: Optional[Value] = None
