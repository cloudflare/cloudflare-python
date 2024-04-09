# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .....types import shared_params
from ...script_setting_param import ScriptSettingParam

__all__ = ["SettingEditParams"]


class SettingEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    service_name: Required[str]
    """Name of Worker to bind to"""

    errors: Required[Iterable[shared_params.UnnamedSchemaRef3248f24329456e19dfa042fff9986f72]]

    messages: Required[Iterable[shared_params.UnnamedSchemaRef3248f24329456e19dfa042fff9986f72]]

    result: Required[ScriptSettingParam]

    success: Required[Literal[True]]
    """Whether the API call was successful"""
