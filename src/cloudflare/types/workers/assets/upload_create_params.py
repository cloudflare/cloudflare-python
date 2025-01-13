# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UploadCreateParams"]


class UploadCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    base64: Required[Literal[True]]
    """Whether the file contents are base64-encoded. Must be `true`."""

    any_file_hash: Annotated[List[str], PropertyInfo(alias="<any file hash>")]
    """Base-64 encoded contents of the file.

    The content type of the file should be included to ensure a valid "Content-Type"
    header is included in asset responses.
    """
