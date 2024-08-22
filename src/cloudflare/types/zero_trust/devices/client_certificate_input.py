# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ClientCertificateInput"]

class ClientCertificateInput(BaseModel):
    certificate_id: str
    """UUID of Cloudflare managed certificate."""

    cn: str
    """Common Name that is protected by the certificate"""