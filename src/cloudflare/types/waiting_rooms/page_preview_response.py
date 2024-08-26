# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PagePreviewResponse"]

class PagePreviewResponse(BaseModel):
    preview_url: Optional[str] = None
    """URL where the custom waiting room page can temporarily be previewed."""