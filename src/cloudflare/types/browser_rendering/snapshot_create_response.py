# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["SnapshotCreateResponse"]


class SnapshotCreateResponse(BaseModel):
    content: str
    """HTML content"""

    screenshot: str
    """Base64 encoded image"""
