# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TemporaryCredentialCreateResponse"]


class TemporaryCredentialCreateResponse(BaseModel):
    access_key_id: Optional[str] = FieldInfo(alias="accessKeyId", default=None)
    """ID for new access key"""

    secret_access_key: Optional[str] = FieldInfo(alias="secretAccessKey", default=None)
    """Secret access key"""

    session_token: Optional[str] = FieldInfo(alias="sessionToken", default=None)
    """Security token"""
