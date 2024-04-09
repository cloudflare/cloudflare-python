# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ConfigurationParam"]


class ConfigurationParam(TypedDict, total=False):
    default_sampling: Required[float]
    """Fallback sampling rate of flow messages being sent in packets per second.

    This should match the packet sampling rate configured on the router.
    """

    name: Required[str]
    """The account name."""

    router_ips: Required[List[str]]
