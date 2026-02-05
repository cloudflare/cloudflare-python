# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OrganizationProfileUpdateParams"]


class OrganizationProfileUpdateParams(TypedDict, total=False):
    business_address: Required[str]

    business_email: Required[str]

    business_name: Required[str]

    business_phone: Required[str]

    external_metadata: Required[str]
