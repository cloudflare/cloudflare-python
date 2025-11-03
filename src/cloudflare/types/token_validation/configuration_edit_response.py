# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ConfigurationEditResponse"]


class ConfigurationEditResponse(BaseModel):
    description: Optional[str] = None

    title: Optional[str] = None

    token_sources: Optional[List[str]] = None
