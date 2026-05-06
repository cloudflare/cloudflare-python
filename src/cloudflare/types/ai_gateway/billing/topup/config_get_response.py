# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ConfigGetResponse"]


class ConfigGetResponse(BaseModel):
    amount: Optional[float] = None

    disabled_reason: Optional[str] = FieldInfo(alias="disabledReason", default=None)

    error: Optional[str] = None

    last_failed_at: Optional[float] = FieldInfo(alias="lastFailedAt", default=None)

    threshold: Optional[float] = None
