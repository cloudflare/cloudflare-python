# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ....._types import FileTypes

__all__ = ["ItemUploadParams", "File"]


class ItemUploadParams(TypedDict, total=False):
    account_id: Required[str]

    namespace: Required[str]

    file: Required[File]


class File(TypedDict, total=False):
    file: Required[FileTypes]
    """The file to upload. Filename must not exceed 128 characters."""

    metadata: str
    """JSON string of custom metadata key-value pairs."""

    wait_for_completion: bool
    """Wait for indexing before responding.

    After processing, vector-indexed instances use any time remaining in a 25s wait
    budget to confirm Vectorize ingestion. Processing itself continues uninterrupted
    and can exceed that budget. If confirmation times out, the response returns the
    current item state and background indexing continues. Defaults to false.
    """
