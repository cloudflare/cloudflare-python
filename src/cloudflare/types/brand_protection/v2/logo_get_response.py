# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["LogoGetResponse", "LogoGetResponseItem"]


class LogoGetResponseItem(BaseModel):
    id: int

    r2_path: str

    similarity_threshold: float

    tag: str

    uploaded_at: Optional[str] = None

    content_type: Optional[str] = None
    """MIME type of the image (only present when download=true)"""

    image_data: Optional[str] = None
    """Base64-encoded image data (only present when download=true)"""


LogoGetResponse: TypeAlias = List[LogoGetResponseItem]
