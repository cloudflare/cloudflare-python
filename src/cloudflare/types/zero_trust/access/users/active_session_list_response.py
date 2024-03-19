# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ....._models import BaseModel

__all__ = [
    "ActiveSessionListResponse",
    "ActiveSessionListResponseItem",
    "ActiveSessionListResponseItemMetadata",
    "ActiveSessionListResponseItemMetadataApps",
]


class ActiveSessionListResponseItemMetadataApps(BaseModel):
    hostname: Optional[str] = None

    name: Optional[str] = None

    type: Optional[str] = None

    uid: Optional[str] = None


class ActiveSessionListResponseItemMetadata(BaseModel):
    apps: Optional[Dict[str, ActiveSessionListResponseItemMetadataApps]] = None

    expires: Optional[int] = None

    iat: Optional[int] = None

    nonce: Optional[str] = None

    ttl: Optional[int] = None


class ActiveSessionListResponseItem(BaseModel):
    expiration: Optional[int] = None

    metadata: Optional[ActiveSessionListResponseItemMetadata] = None

    name: Optional[str] = None


ActiveSessionListResponse = List[ActiveSessionListResponseItem]
