# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .scripts.consumer_script import ConsumerScript

__all__ = ["ScriptSetting", "Observability"]


class Observability(BaseModel):
    enabled: bool
    """Whether observability is enabled for the Worker."""

    head_sampling_rate: Optional[float] = None
    """The sampling rate for incoming requests.

    From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.
    """


class ScriptSetting(BaseModel):
    logpush: Optional[bool] = None
    """Whether Logpush is turned on for the Worker."""

    observability: Optional[Observability] = None
    """Observability settings for the Worker."""

    tail_consumers: Optional[List[ConsumerScript]] = None
    """List of Workers that will consume logs from the attached Worker."""
