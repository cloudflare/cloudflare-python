# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["ServiceTokenRule", "ServiceToken"]


class ServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class ServiceTokenRule(BaseModel):
    """Matches a specific Access Service Token"""

    service_token: ServiceToken
