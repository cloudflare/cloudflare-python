# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .setting_value_param import SettingValueParam

__all__ = ["TLSUpdateParams"]


class TLSUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    setting_id: Required[Literal["ciphers", "min_tls_version", "http2"]]
    """The TLS Setting name."""

    value: Required[SettingValueParam]
    """The tls setting value."""
