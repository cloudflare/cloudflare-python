# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RouteParam", "Value"]

class Value(TypedDict, total=False):
    type: Literal["temporary", "permanent"]
    """The response type for the URL redirect."""

    url: str
    """
    The URL to redirect the request to. Notes: ${num} refers to the position of '\\**'
    in the constraint value.
    """

class RouteParam(TypedDict, total=False):
    name: Literal["forward_url"]
    """The type of route."""

    value: Value