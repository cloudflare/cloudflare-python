# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountCreateParams", "Unit"]


class AccountCreateParams(TypedDict, total=False):
    name: Required[str]
    """Account name, limited to 65 UTF-8 bytes."""

    standalone: Literal[True]
    """Set to `true` and omit `unit` to create a standalone Free Account.

    If provided, this field must be `true`.
    """

    type: Literal["standard", "enterprise"]
    """the type of account being created.

    For self-serve customers, use standard. for enterprise customers, use
    enterprise.
    """

    unit: Unit
    """Information related to the tenant unit.

    Provide its ID and omit `standalone` to create the Account within an
    Organization. See
    https://developers.cloudflare.com/tenant/how-to/manage-accounts/.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Unit(TypedDict, total=False):
    """Information related to the tenant unit.

    Provide its ID and omit `standalone` to create the Account within an Organization. See https://developers.cloudflare.com/tenant/how-to/manage-accounts/.
    """

    id: str
    """Tenant unit ID"""
