# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasetCreateParams"]


class DatasetCreateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]

    description: Optional[str]
    """The description of the dataset"""

    encoding_version: int
    """Dataset encoding version

    Non-secret custom word lists with no header are always version 1. Secret EDM
    lists with no header are version 1. Multicolumn CSV with headers are version 2.
    Omitting this field provides the default value 0, which is interpreted the same
    as 1.
    """

    secret: bool
    """Generate a secret dataset.

    If true, the response will include a secret to use with the EDM encoder. If
    false, the response has no secret and the dataset is uploaded in plaintext.
    """
