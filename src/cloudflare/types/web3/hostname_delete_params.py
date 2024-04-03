# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HostnameDeleteParams"]


class HostnameDeleteParams(TypedDict, total=False):
    zone_identifier: Required[str]
    """Identifier"""

    body: Required[object]
