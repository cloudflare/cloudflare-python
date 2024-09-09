# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["IPListParams"]


class IPListParams(TypedDict, total=False):
    networks: str
    """Specified as `jdcloud` to list IPs used by JD Cloud data centers."""
