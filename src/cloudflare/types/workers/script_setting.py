# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from .scripts.consumer_script import ConsumerScript

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ScriptSetting"]

class ScriptSetting(BaseModel):
    logpush: Optional[bool] = None
    """Whether Logpush is turned on for the Worker."""

    tail_consumers: Optional[List[ConsumerScript]] = None
    """List of Workers that will consume logs from the attached Worker."""