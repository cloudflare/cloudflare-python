# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .firewall_filter_param import FirewallFilterParam

__all__ = ["FilterCreateParams"]


class FilterCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Defines an identifier."""

    body: Required[Iterable[FirewallFilterParam]]
