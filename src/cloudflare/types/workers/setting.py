# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..shared import UnnamedSchemaRef3248f24329456e19dfa042fff9986f72
from ..._models import BaseModel
from .settings_item import SettingsItem

__all__ = ["Setting"]


class Setting(BaseModel):
    errors: List[UnnamedSchemaRef3248f24329456e19dfa042fff9986f72]

    messages: List[UnnamedSchemaRef3248f24329456e19dfa042fff9986f72]

    result: SettingsItem

    success: Literal[True]
    """Whether the API call was successful"""
