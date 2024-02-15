# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FlagLogsReceivedUpdateLogRetentionFlagParams"]


class FlagLogsReceivedUpdateLogRetentionFlagParams(TypedDict, total=False):
    flag: Required[bool]
    """The log retention flag for Logpull API."""
