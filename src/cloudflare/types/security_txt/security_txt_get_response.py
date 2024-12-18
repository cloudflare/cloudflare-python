# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SecurityTXTGetResponse"]


class SecurityTXTGetResponse(BaseModel):
    acknowledgments: Optional[List[str]] = None

    canonical: Optional[List[str]] = None

    contact: Optional[List[str]] = None

    enabled: Optional[bool] = None

    encryption: Optional[List[str]] = None

    expires: Optional[datetime] = None

    hiring: Optional[List[str]] = None

    policy: Optional[List[str]] = None

    preferred_languages: Optional[str] = FieldInfo(alias="preferredLanguages", default=None)
