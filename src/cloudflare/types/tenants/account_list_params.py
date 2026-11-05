# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountListParams", "AccountPubname", "Name"]


class AccountListParams(TypedDict, total=False):
    account_pubname: AccountPubname

    direction: Literal["asc", "desc"]
    """Sort direction for the order_by field.

    Valid values: `asc`, `desc`. Defaults to `asc` when order_by is specified.
    """

    include_total: bool
    """
    Whether to calculate and return the exact `result_info.total_size` for cursor
    pagination. Defaults to true. When false, `total_size` is omitted. Legacy
    `page`/`per_page` requests always calculate `total_count`.
    """

    name: Name

    order_by: Literal["account_name"]
    """Field to order results by. Currently supported values: `account_name`."""

    page: int
    """Legacy offset page number.

    Must be provided with `per_page`. Values below 1 are treated as

    1. Cursor pagination takes precedence when requested.
    """

    page_size: int
    """The amount of items to return. Defaults to 10."""

    page_token: str
    """
    An opaque token returned from the last list response that when provided will
    retrieve the next page.

    Parameters used to filter the retrieved list must remain in subsequent requests
    with a page token.
    """

    per_page: int
    """Legacy offset page size.

    Must be provided with `page`. Values are clamped to the range 1-100. Cursor
    pagination takes precedence when requested.
    """

    status: Literal["active", "deleted"]
    """Filter accounts by lifecycle status. Defaults to `active`."""


class AccountPubname(TypedDict, total=False):
    contains: str
    """
    (case-insensitive) Filter the list of accounts to where the account_pubname
    contains a particular string.
    """

    ends_with: Annotated[str, PropertyInfo(alias="endsWith")]
    """
    (case-insensitive) Filter the list of accounts to where the account_pubname ends
    with a particular string.
    """

    starts_with: Annotated[str, PropertyInfo(alias="startsWith")]
    """
    (case-insensitive) Filter the list of accounts to where the account_pubname
    starts with a particular string.
    """


class Name(TypedDict, total=False):
    contains: str
    """
    (case-insensitive) Filter the list of accounts to where the name contains a
    particular string.
    """

    ends_with: Annotated[str, PropertyInfo(alias="endsWith")]
    """
    (case-insensitive) Filter the list of accounts to where the name ends with a
    particular string.
    """

    starts_with: Annotated[str, PropertyInfo(alias="startsWith")]
    """
    (case-insensitive) Filter the list of accounts to where the name starts with a
    particular string.
    """
