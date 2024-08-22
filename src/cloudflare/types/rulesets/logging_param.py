# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

__all__ = ["LoggingParam"]

class LoggingParam(TypedDict, total=False):
    enabled: Required[bool]
    """Whether to generate a log when the rule matches."""