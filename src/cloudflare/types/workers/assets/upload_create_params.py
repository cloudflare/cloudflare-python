# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["UploadCreateParams"]


class UploadCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    base64: Required[Literal[True]]
    """Whether the file contents are base64-encoded. Must be `true`."""

    body: Required[Dict[str, str]]
