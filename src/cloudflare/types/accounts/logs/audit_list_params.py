# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AuditListParams"]


class AuditListParams(TypedDict, total=False):
    account_id: Required[str]
    """The unique id that identifies the account."""

    before: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """
    Filters actions based on a given timestamp in the format yyyy-mm-dd, returning
    only logs that occurred on and before the specified date.
    """

    since: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """
    Filters actions based on a given timestamp in the format yyyy-mm-dd, returning
    only logs that occurred on and after the specified date.
    """

    account_name: str
    """Filters by the account name."""

    action_result: Literal["success", "failure"]
    """Whether the action was successful or not."""

    action_type: Literal["create", "delete", "view", "update"]
    """Filters by the action type."""

    actor_context: Literal["api_key", "api_token", "dash", "oauth", "origin_ca_key"]
    """Filters by the actor context."""

    actor_email: str
    """Filters by the actor's email address."""

    actor_id: str
    """Filters by the actor ID. This can be either the Account ID or User ID."""

    actor_ip_address: str
    """The IP address where the action was initiated."""

    actor_token_id: str
    """Filters by the API token ID when the actor context is an api_token or oauth."""

    actor_token_name: str
    """Filters by the API token name when the actor context is an api_token or oauth."""

    actor_type: Literal["cloudflare_admin", "account", "user"]
    """Filters by the actor type."""

    audit_log_id: str
    """Finds a specific log by its ID."""

    cursor: str
    """The cursor is an opaque token used to paginate through large sets of records.

    It indicates the position from which to continue when requesting the next set of
    records. A valid cursor value can be obtained from the cursor object in the
    result_info structure of a previous response.
    """

    direction: Literal["desc", "asc"]
    """Sets sorting order."""

    limit: float
    """The number limits the objects to return.

    The cursor attribute may be used to iterate over the next batch of objects if
    there are more than the limit.
    """

    raw_cf_rayid: Annotated[str, PropertyInfo(alias="raw_cf_ray_id")]
    """Filters by the response CF Ray ID."""

    raw_method: str
    """The HTTP method for the API call."""

    raw_status_code: int
    """The response status code that was returned."""

    raw_uri: str
    """Filters by the request URI."""

    resource_id: str
    """Filters by the resource ID."""

    resource_product: str
    """
    Filters audit logs by the Cloudflare product associated with the changed
    resource.
    """

    resource_scope: Literal["accounts", "user", "zones"]
    """
    Filters by the resource scope, specifying whether the resource is associated
    with an user, an account, or a zone.
    """

    resource_type: str
    """Filters audit logs based on the unique type of resource changed by the action."""

    zone_id: str
    """Filters by the zone ID."""

    zone_name: str
    """Filters by the zone name associated with the change."""
