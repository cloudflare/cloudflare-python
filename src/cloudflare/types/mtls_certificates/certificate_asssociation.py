# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["CertificateAsssociation"]

class CertificateAsssociation(BaseModel):
    service: Optional[str] = None
    """The service using the certificate."""

    status: Optional[str] = None
    """Certificate deployment status for the given service."""