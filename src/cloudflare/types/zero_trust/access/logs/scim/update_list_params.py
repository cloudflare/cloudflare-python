# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["UpdateListParams"]


class UpdateListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    idp_id: Required[List[str]]
    """The unique Id of the IdP that has SCIM enabled."""

    cf_resource_id: str
    """The unique Cloudflare-generated Id of the SCIM resource."""

    direction: Literal["desc", "asc"]
    """The chronological order used to sort the logs."""

    idp_resource_id: str
    """The IdP-generated Id of the SCIM resource."""

    limit: int
    """The maximum number of update logs to retrieve."""

    request_method: List[Literal["DELETE", "PATCH", "POST", "PUT"]]
    """The request method of the SCIM request."""

    resource_group_name: str
    """The display name of the SCIM Group resource."""

    resource_type: List[Literal["USER", "GROUP"]]
    """The resource type of the SCIM request."""

    resource_user_email: str
    """The email address of the SCIM User resource."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """the timestamp of the earliest update log."""

    status: List[Literal["FAILURE", "SUCCESS"]]
    """The status of the SCIM request."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """the timestamp of the most-recent update log."""
