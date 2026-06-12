# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["TenantMembership"]


class TenantMembership(BaseModel):
    user_email: str

    user_name: str

    user_tag: str
