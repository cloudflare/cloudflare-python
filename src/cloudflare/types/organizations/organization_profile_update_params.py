# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["OrganizationProfileUpdateParams"]


class OrganizationProfileUpdateParams(TypedDict, total=False):
    business_address: Optional[str]

    business_email: Optional[str]

    business_name: Optional[str]

    business_phone: Optional[str]

    external_metadata: Optional[str]
