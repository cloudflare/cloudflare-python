# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel

__all__ = ["CertificateDeleteResponse"]


class CertificateDeleteResponse(BaseModel):
    id: Optional[str] = None
    """UUID"""
