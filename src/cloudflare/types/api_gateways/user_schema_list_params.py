# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserSchemaListParams"]


class UserSchemaListParams(TypedDict, total=False):
    omit_source: bool
    """Omit the source-files of schemas and only retrieve their meta-data."""

    page: object
    """Page number of paginated results."""

    per_page: object
    """Maximum number of results per page."""

    validation_enabled: bool
    """Flag whether schema is enabled for validation."""
