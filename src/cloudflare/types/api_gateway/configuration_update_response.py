# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .message import Message
from ..._models import BaseModel

__all__ = ["ConfigurationUpdateResponse"]


class ConfigurationUpdateResponse(BaseModel):
    errors: Message

    messages: Message

    success: Literal[True]
    """Whether the API call was successful"""
