# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["BinaryStorageCreateParams"]


class BinaryStorageCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    file: Required[FileTypes]
    """The binary file content to upload."""
