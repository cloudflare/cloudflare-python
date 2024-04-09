# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .scripts import ConsumerScriptItemParam

__all__ = ["ScriptSettingParam"]


class ScriptSettingParam(TypedDict, total=False):
    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    tail_consumers: Iterable[ConsumerScriptItemParam]
    """List of Workers that will consume logs from the attached Worker."""
