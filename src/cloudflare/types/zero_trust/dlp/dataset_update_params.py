# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasetUpdateParams"]


class DatasetUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    description: Optional[str]
    """The description of the dataset"""

    name: Optional[str]
    """The name of the dataset, must be unique"""
