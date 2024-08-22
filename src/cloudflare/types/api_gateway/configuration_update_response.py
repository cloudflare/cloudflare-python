# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from .message import Message

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ConfigurationUpdateResponse"]

class ConfigurationUpdateResponse(BaseModel):
    errors: Message

    messages: Message

    success: Literal[True]
    """Whether the API call was successful"""