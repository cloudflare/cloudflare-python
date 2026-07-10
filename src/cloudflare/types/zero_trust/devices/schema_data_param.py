# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SchemaDataParam"]


class SchemaDataParam(TypedDict, total=False):
    """
    The configuration object which contains the details for the WARP client to conduct the test.
    """

    host: Required[str]
    """The desired endpoint to test."""

    kind: Required[Literal["http", "traceroute"]]
    """The type of test."""

    method: Literal["GET"]
    """The HTTP request method type."""
