# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ManagedUpdateResponse"]


class ManagedUpdateResponse(BaseModel):
    bucket_id: str = FieldInfo(alias="bucketId")
    """Bucket ID"""

    domain: str
    """Domain name of the bucket's r2.dev domain"""

    enabled: bool
    """Whether this bucket is publicly accessible at the r2.dev domain"""
