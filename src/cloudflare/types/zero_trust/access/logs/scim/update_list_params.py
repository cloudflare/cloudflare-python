# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ......_types import SequenceNotStr
from ......_utils import PropertyInfo

__all__ = ["UpdateListParams"]


class UpdateListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    idp_id: Required[SequenceNotStr[str]]
    """The unique Id of the IdP that has SCIM enabled."""

    cf_resource_id: SequenceNotStr[str]
    """The unique Cloudflare-generated Id of the SCIM resource.

    Pass once for a single lookup (`?cf_resource_id=A`) or repeat the parameter
    (`?cf_resource_id=A&cf_resource_id=B`) to filter by multiple resources in one
    request.
    """

    direction: Literal["desc", "asc"]
    """The chronological order used to sort the logs."""

    idp_resource_id: SequenceNotStr[str]
    """The IdP-generated Id of the SCIM resource.

    Pass once for a single lookup (`?idp_resource_id=A`) or repeat the parameter
    (`?idp_resource_id=A&idp_resource_id=B`) to filter by multiple resources in one
    request.
    """

    limit: int
    """The maximum number of update logs to retrieve."""

    page: int
    """Page number of results."""

    per_page: int
    """Number of results per page."""

    request_method: List[Literal["DELETE", "PATCH", "POST", "PUT"]]
    """The request method of the SCIM request."""

    resource_group_name: SequenceNotStr[str]
    """The display name of the SCIM Group resource.

    Pass once for a single lookup (`?resource_group_name=A`) or repeat the parameter
    (`?resource_group_name=A&resource_group_name=B`) to filter by multiple group
    names in one request.
    """

    resource_type: List[Literal["USER", "GROUP"]]
    """The resource type of the SCIM request."""

    resource_user_email: SequenceNotStr[str]
    """The email address of the SCIM User resource.

    Pass once for a single lookup (`?resource_user_email=A`) or repeat the parameter
    (`?resource_user_email=A&resource_user_email=B`) to filter by multiple emails in
    one request.
    """

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """the timestamp of the earliest update log."""

    status: List[Literal["FAILURE", "SUCCESS"]]
    """The status of the SCIM request."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """the timestamp of the most-recent update log."""
