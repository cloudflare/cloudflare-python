# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .scripts.consumer_script import ConsumerScript

__all__ = ["ScriptSetting"]


class ScriptSetting(BaseModel):
    logpush: Optional[bool] = None
    """Whether Logpush is turned on for the Worker."""

    tail_consumers: Optional[List[ConsumerScript]] = None
    """List of Workers that will consume logs from the attached Worker."""
