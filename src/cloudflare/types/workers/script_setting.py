# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .scripts import ConsumerScript
from ..._models import BaseModel

__all__ = ["ScriptSetting"]


class ScriptSetting(BaseModel):
    logpush: Optional[bool] = None
    """Whether Logpush is turned on for the Worker."""

    tail_consumers: Optional[List[ConsumerScript]] = None
    """List of Workers that will consume logs from the attached Worker."""
