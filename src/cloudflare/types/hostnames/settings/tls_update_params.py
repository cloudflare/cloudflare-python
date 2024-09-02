# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from .setting_value_param import SettingValueParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["TLSUpdateParams"]


class TLSUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    setting_id: Required[Literal["ciphers", "min_tls_version", "http2"]]
    """The TLS Setting name."""

    value: Required[SettingValueParam]
    """The tls setting value."""
