# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["SettingEditParams", "TailConsumer"]


class SettingEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    tail_consumers: Iterable[TailConsumer]
    """List of Workers that will consume logs from the attached Worker."""


class TailConsumer(TypedDict, total=False):
    service: Required[str]
    """Name of Worker that is to be the consumer."""

    environment: str
    """Optional environment if the Worker utilizes one."""

    namespace: str
    """Optional dispatch namespace the script belongs to."""
