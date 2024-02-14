# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["CertificateListResponse", "CertificateListResponseItem"]


class CertificateListResponseItem(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    cert_id: Optional[str] = None
    """Identifier"""

    certificate: Optional[str] = None
    """The hostname certificate."""

    enabled: Optional[bool] = None
    """Indicates whether hostname-level authenticated origin pulls is enabled.

    A null value voids the association.
    """

    hostname: Optional[str] = None
    """
    The hostname on the origin for which the client certificate uploaded will be
    used.
    """

    private_key: Optional[str] = None
    """The hostname certificate's private key."""


CertificateListResponse = List[CertificateListResponseItem]
