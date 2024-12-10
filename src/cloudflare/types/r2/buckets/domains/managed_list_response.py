# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ManagedListResponse"]


class ManagedListResponse(BaseModel):
    bucket_id: str = FieldInfo(alias="bucketId")
    """Bucket ID"""

    domain: str
    """Domain name of the bucket's r2.dev domain"""

    enabled: bool
    """Whether this bucket is publicly accessible at the r2.dev domain"""
