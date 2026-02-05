# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountCreateParams", "Unit"]


class AccountCreateParams(TypedDict, total=False):
    name: Required[str]
    """Account name"""

    type: Literal["standard", "enterprise"]

    unit: Unit
    """
    information related to the tenant unit, and optionally, an id of the unit to
    create the account on. see
    https://developers.cloudflare.com/tenant/how-to/manage-accounts/
    """


class Unit(TypedDict, total=False):
    """
    information related to the tenant unit, and optionally, an id of the unit to create the account on. see https://developers.cloudflare.com/tenant/how-to/manage-accounts/
    """

    id: str
    """Tenant unit ID"""
