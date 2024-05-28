# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional

from .message import Message
from ..._models import BaseModel

__all__ = ["Schema"]


class Schema(BaseModel):
    errors: Message

    messages: Message

    result: Union[Optional[str], Optional[object]]

    success: bool
    """Whether the API call was successful"""
