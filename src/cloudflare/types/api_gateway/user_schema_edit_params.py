# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["UserSchemaEditParams"]


class UserSchemaEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    validation_enabled: Literal[True]
    """Flag whether schema is enabled for validation."""
