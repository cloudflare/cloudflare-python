# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SchemaDataParam"]


class SchemaDataParam(TypedDict, total=False):
    host: str
    """The desired endpoint to test."""

    kind: str
    """The type of test."""

    method: str
    """The HTTP request method type."""
