# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["OrganizationProfile"]


class OrganizationProfile(BaseModel):
    business_address: str

    business_email: str

    business_name: str

    business_phone: str

    external_metadata: str
