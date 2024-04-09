# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ConsumerScriptItem"]


class ConsumerScriptItem(BaseModel):
    service: str
    """Name of Worker that is to be the consumer."""

    environment: Optional[str] = None
    """Optional environment if the Worker utilizes one."""

    namespace: Optional[str] = None
    """Optional dispatch namespace the script belongs to."""
