# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["AccessRequestListParams"]


class AccessRequestListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    allowed_op: Annotated[Literal["eq", "neq"], PropertyInfo(alias="allowedOp")]
    """Operator for the `allowed` filter."""

    app_type_op: Annotated[Literal["eq", "neq"], PropertyInfo(alias="app_typeOp")]
    """Operator for the `app_type` filter."""

    app_uid_op: Annotated[Literal["eq", "neq"], PropertyInfo(alias="app_uidOp")]
    """Operator for the `app_uid` filter."""

    country_code_op: Annotated[Literal["eq", "neq"], PropertyInfo(alias="country_codeOp")]
    """Operator for the `country_code` filter."""

    direction: Literal["desc", "asc"]
    """The chronological sorting order for the logs."""

    email: str
    """Filter by user email.

    Defaults to substring matching. To force exact matching, set `email_exact=true`.
    Example (default): `email=@example.com` returns all events with that domain.
    Example (exact): `email=user@example.com&email_exact=true` returns only that
    user.
    """

    email_exact: bool
    """When true, `email` is matched exactly instead of substring matching."""

    email_op: Annotated[Literal["eq", "neq"], PropertyInfo(alias="emailOp")]
    """Operator for the `email` filter."""

    fields: str
    """
    Comma-separated list of fields to include in the response. When omitted, all
    fields are returned.
    """

    idp_op: Annotated[Literal["eq", "neq"], PropertyInfo(alias="idpOp")]
    """Operator for the `idp` filter."""

    limit: int
    """The maximum number of log entries to retrieve."""

    non_identity_op: Annotated[Literal["eq", "neq"], PropertyInfo(alias="non_identityOp")]
    """Operator for the `non_identity` filter."""

    page: int
    """Page number of results."""

    per_page: int
    """Number of results per page."""

    rayid_op: Annotated[Literal["eq", "neq"], PropertyInfo(alias="ray_idOp")]
    """Operator for the `ray_id` filter."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The earliest event timestamp to query."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The latest event timestamp to query."""

    user_id: str
    """Filter by user UUID."""

    user_id_op: Annotated[Literal["eq", "neq"], PropertyInfo(alias="user_idOp")]
    """Operator for the `user_id` filter."""
