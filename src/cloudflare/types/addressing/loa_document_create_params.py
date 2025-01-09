# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LOADocumentCreateParams"]


class LOADocumentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier of a Cloudflare account."""

    loa_document: Required[str]
    """LOA document to upload."""
