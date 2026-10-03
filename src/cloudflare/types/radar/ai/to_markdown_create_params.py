# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import FileTypes, SequenceNotStr

__all__ = ["ToMarkdownCreateParams"]


class ToMarkdownCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID used for this AI model request."""

    files: Required[SequenceNotStr[FileTypes]]
    """Files to convert, supplied as multipart file uploads."""
