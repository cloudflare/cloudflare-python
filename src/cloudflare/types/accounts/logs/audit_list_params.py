# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "AuditListParams",
    "AccountName",
    "ActionResult",
    "ActionType",
    "ActorContext",
    "ActorEmail",
    "ActorID",
    "ActorIPAddress",
    "ActorTokenID",
    "ActorTokenName",
    "ActorType",
    "AuditLogID",
    "RawCfRayID",
    "RawMethod",
    "RawStatusCode",
    "RawURI",
    "ResourceID",
    "ResourceProduct",
    "ResourceScope",
    "ResourceType",
    "ZoneID",
    "ZoneName",
]


class AuditListParams(TypedDict, total=False):
    account_id: Required[str]
    """The unique id that identifies the account."""

    before: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Limits the returned results to logs older than the specified date.

    This can be a date string 2019-04-30 (interpreted in UTC) or an absolute
    timestamp that conforms to RFC3339.
    """

    since: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Limits the returned results to logs newer than the specified date.

    This can be a date string 2019-04-30 (interpreted in UTC) or an absolute
    timestamp that conforms to RFC3339.
    """

    account_name: AccountName

    action_result: ActionResult

    action_type: ActionType

    actor_context: ActorContext

    actor_email: ActorEmail

    actor_id: ActorID

    actor_ip_address: ActorIPAddress

    actor_token_id: ActorTokenID

    actor_token_name: ActorTokenName

    actor_type: ActorType

    audit_log_id: AuditLogID

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

    raw_cf_rayid: Annotated[RawCfRayID, PropertyInfo(alias="raw_cf_ray_id")]

    raw_method: RawMethod

    raw_status_code: RawStatusCode

    raw_uri: RawURI

    resource_id: ResourceID

    resource_product: ResourceProduct

    resource_scope: ResourceScope

    resource_type: ResourceType

    zone_id: ZoneID

    zone_name: ZoneName


_AccountNameReservedKeywords = TypedDict(
    "_AccountNameReservedKeywords",
    {
        "not": List[str],
    },
    total=False,
)


class AccountName(_AccountNameReservedKeywords, total=False):
    pass


_ActionResultReservedKeywords = TypedDict(
    "_ActionResultReservedKeywords",
    {
        "not": List[Literal["success", "failure"]],
    },
    total=False,
)


class ActionResult(_ActionResultReservedKeywords, total=False):
    pass


_ActionTypeReservedKeywords = TypedDict(
    "_ActionTypeReservedKeywords",
    {
        "not": List[Literal["create", "delete", "view", "update"]],
    },
    total=False,
)


class ActionType(_ActionTypeReservedKeywords, total=False):
    pass


_ActorContextReservedKeywords = TypedDict(
    "_ActorContextReservedKeywords",
    {
        "not": List[Literal["api_key", "api_token", "dash", "oauth", "origin_ca_key"]],
    },
    total=False,
)


class ActorContext(_ActorContextReservedKeywords, total=False):
    pass


_ActorEmailReservedKeywords = TypedDict(
    "_ActorEmailReservedKeywords",
    {
        "not": List[str],
    },
    total=False,
)


class ActorEmail(_ActorEmailReservedKeywords, total=False):
    pass


_ActorIDReservedKeywords = TypedDict(
    "_ActorIDReservedKeywords",
    {
        "not": List[str],
    },
    total=False,
)


class ActorID(_ActorIDReservedKeywords, total=False):
    pass


_ActorIPAddressReservedKeywords = TypedDict(
    "_ActorIPAddressReservedKeywords",
    {
        "not": List[str],
    },
    total=False,
)


class ActorIPAddress(_ActorIPAddressReservedKeywords, total=False):
    pass


_ActorTokenIDReservedKeywords = TypedDict(
    "_ActorTokenIDReservedKeywords",
    {
        "not": List[str],
    },
    total=False,
)


class ActorTokenID(_ActorTokenIDReservedKeywords, total=False):
    pass


_ActorTokenNameReservedKeywords = TypedDict(
    "_ActorTokenNameReservedKeywords",
    {
        "not": List[str],
    },
    total=False,
)


class ActorTokenName(_ActorTokenNameReservedKeywords, total=False):
    pass


_ActorTypeReservedKeywords = TypedDict(
    "_ActorTypeReservedKeywords",
    {
        "not": List[Literal["account", "cloudflare_admin", "system", "user"]],
    },
    total=False,
)


class ActorType(_ActorTypeReservedKeywords, total=False):
    pass


_AuditLogIDReservedKeywords = TypedDict(
    "_AuditLogIDReservedKeywords",
    {
        "not": List[str],
    },
    total=False,
)


class AuditLogID(_AuditLogIDReservedKeywords, total=False):
    pass


_RawCfRayIDReservedKeywords = TypedDict(
    "_RawCfRayIDReservedKeywords",
    {
        "not": List[str],
    },
    total=False,
)


class RawCfRayID(_RawCfRayIDReservedKeywords, total=False):
    pass


_RawMethodReservedKeywords = TypedDict(
    "_RawMethodReservedKeywords",
    {
        "not": List[str],
    },
    total=False,
)


class RawMethod(_RawMethodReservedKeywords, total=False):
    pass


_RawStatusCodeReservedKeywords = TypedDict(
    "_RawStatusCodeReservedKeywords",
    {
        "not": Iterable[int],
    },
    total=False,
)


class RawStatusCode(_RawStatusCodeReservedKeywords, total=False):
    pass


_RawURIReservedKeywords = TypedDict(
    "_RawURIReservedKeywords",
    {
        "not": List[str],
    },
    total=False,
)


class RawURI(_RawURIReservedKeywords, total=False):
    pass


_ResourceIDReservedKeywords = TypedDict(
    "_ResourceIDReservedKeywords",
    {
        "not": List[str],
    },
    total=False,
)


class ResourceID(_ResourceIDReservedKeywords, total=False):
    pass


_ResourceProductReservedKeywords = TypedDict(
    "_ResourceProductReservedKeywords",
    {
        "not": List[str],
    },
    total=False,
)


class ResourceProduct(_ResourceProductReservedKeywords, total=False):
    pass


_ResourceScopeReservedKeywords = TypedDict(
    "_ResourceScopeReservedKeywords",
    {
        "not": List[Literal["accounts", "user", "zones"]],
    },
    total=False,
)


class ResourceScope(_ResourceScopeReservedKeywords, total=False):
    pass


_ResourceTypeReservedKeywords = TypedDict(
    "_ResourceTypeReservedKeywords",
    {
        "not": List[str],
    },
    total=False,
)


class ResourceType(_ResourceTypeReservedKeywords, total=False):
    pass


_ZoneIDReservedKeywords = TypedDict(
    "_ZoneIDReservedKeywords",
    {
        "not": List[str],
    },
    total=False,
)


class ZoneID(_ZoneIDReservedKeywords, total=False):
    pass


_ZoneNameReservedKeywords = TypedDict(
    "_ZoneNameReservedKeywords",
    {
        "not": List[str],
    },
    total=False,
)


class ZoneName(_ZoneNameReservedKeywords, total=False):
    pass
