# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ......types import shared_params
from .....workers import ScriptSettingParam

__all__ = ["SettingEditParams"]


class SettingEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    errors: Required[Iterable[shared_params.UnnamedSchemaRef3248f24329456e19dfa042fff9986f72]]

    messages: Required[Iterable[shared_params.UnnamedSchemaRef3248f24329456e19dfa042fff9986f72]]

    result: Required[ScriptSettingParam]

    success: Required[Literal[True]]
    """Whether the API call was successful"""
