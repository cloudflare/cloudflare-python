# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SchemaCreateParams"]


class SchemaCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    kind: Required[Literal["openapi_v3"]]
    """The kind of the schema"""

    name: Required[str]
    """A human-readable name for the schema"""

    source: Required[str]
    """The raw schema, e.g., the OpenAPI schema, either as JSON or YAML"""

    validation_enabled: Required[bool]
    """An indicator if this schema is enabled"""
