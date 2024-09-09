# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserSchemaGetParams"]


class UserSchemaGetParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    omit_source: bool
    """Omit the source-files of schemas and only retrieve their meta-data."""
