# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr
from .override_url import OverrideURL

__all__ = ["OverrideCreateParams"]


class OverrideCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Defines an identifier."""

    urls: Required[SequenceNotStr[OverrideURL]]
    """The URLs to include in the current WAF override.

    You can use wildcards. Each entered URL will be escaped before use, which means
    you can only use simple wildcard patterns.
    """
