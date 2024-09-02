# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing import Optional, Dict

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ActiveSessionListResponse", "Metadata", "MetadataApps"]


class MetadataApps(BaseModel):
    hostname: Optional[str] = None

    name: Optional[str] = None

    type: Optional[str] = None

    uid: Optional[str] = None


class Metadata(BaseModel):
    apps: Optional[Dict[str, MetadataApps]] = None

    expires: Optional[int] = None

    iat: Optional[int] = None

    nonce: Optional[str] = None

    ttl: Optional[int] = None


class ActiveSessionListResponse(BaseModel):
    expiration: Optional[int] = None

    metadata: Optional[Metadata] = None

    name: Optional[str] = None
