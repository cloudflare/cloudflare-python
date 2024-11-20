# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["LeakedCredentialCheckListResponse"]


class LeakedCredentialCheckListResponse(BaseModel):
    enabled: Optional[bool] = None
    """Whether or not Leaked Credential Checks are enabled"""
