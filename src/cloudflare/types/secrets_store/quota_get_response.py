# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["QuotaGetResponse", "Secrets"]


class Secrets(BaseModel):
    quota: float
    """The number of secrets the account is entitlted to use"""

    usage: float
    """The number of secrets the account is currently using"""


class QuotaGetResponse(BaseModel):
    secrets: Secrets
