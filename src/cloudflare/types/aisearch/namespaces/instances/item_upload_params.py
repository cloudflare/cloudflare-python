# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ....._types import FileTypes

__all__ = ["ItemUploadParams", "File"]


class ItemUploadParams(TypedDict, total=False):
    account_id: str

    name: Required[str]

    file: Required[File]


class File(TypedDict, total=False):
    file: Required[FileTypes]
    """The file to upload (max 4MB). Filename must not exceed 128 characters."""

    metadata: str
    """JSON string of custom metadata key-value pairs."""

    wait_for_completion: bool
    """Wait for indexing to complete before responding. Defaults to false."""
