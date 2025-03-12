# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DatasetCreateParams"]


class DatasetCreateParams(TypedDict, total=False):
    account_id: Required[float]
    """Account ID"""

    is_public: Required[Annotated[bool, PropertyInfo(alias="isPublic")]]
    """If true, then anyone can search the dataset.

    If false, then its limited to the account.
    """

    name: Required[str]
    """Used to describe the dataset within the account context"""
