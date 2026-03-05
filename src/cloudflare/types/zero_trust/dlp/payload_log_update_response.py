# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["PayloadLogUpdateResponse"]


class PayloadLogUpdateResponse(BaseModel):
    updated_at: datetime

    masking_level: Optional[Literal["full", "partial", "clear", "default"]] = None
    """Masking level for payload logs.

    - `full`: The entire payload is masked.
    - `partial`: Only partial payload content is masked.
    - `clear`: No masking is applied to the payload content.
    - `default`: DLP uses its default masking behavior.
    """

    public_key: Optional[str] = None
    """Base64-encoded public key for encrypting payload logs.

    Null when payload logging is disabled.
    """
