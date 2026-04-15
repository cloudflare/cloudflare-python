# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["UserSchemaEditParams"]


class UserSchemaEditParams(TypedDict, total=False):
    zone_id: str
    """Identifier."""

    validation_enabled: Literal[True]
    """Flag whether schema is enabled for validation."""
