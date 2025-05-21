# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["LeakedCredentialCheckGetResponse"]


class LeakedCredentialCheckGetResponse(BaseModel):
    enabled: Optional[bool] = None
    """Determines whether or not Leaked Credential Checks are enabled."""
