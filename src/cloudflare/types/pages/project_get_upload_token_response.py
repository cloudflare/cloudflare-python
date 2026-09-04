# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ProjectGetUploadTokenResponse"]


class ProjectGetUploadTokenResponse(BaseModel):
    jwt: str
    """Short-lived JWT used to authenticate Pages Direct Upload asset operations."""
