# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .consumer_script_param import ConsumerScriptParam

__all__ = ["SettingEditParams"]


class SettingEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    tail_consumers: Iterable[ConsumerScriptParam]
    """List of Workers that will consume logs from the attached Worker."""
