# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SubdomainGetResponse"]


class SubdomainGetResponse(BaseModel):
    subdomain: Optional[str] = None
