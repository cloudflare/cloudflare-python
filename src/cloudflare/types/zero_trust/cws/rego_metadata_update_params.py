# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RegoMetadataUpdateParams"]


class RegoMetadataUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID (32-character hexadecimal string)"""

    data: Required[object]

    import_path: Required[str]
    """
    Unique Rego import path in the form metadata.<segment>, with one alphanumeric or
    underscore segment. Reference it as data.<import_path>.
    """

    name: Required[str]
    """Name of the rego metadata document (unique per account)"""
