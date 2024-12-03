# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .scope_param import ScopeParam

__all__ = ["RouteBulkUpdateParams", "Route"]


class RouteBulkUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    routes: Required[Iterable[Route]]


class Route(TypedDict, total=False):
    id: Required[str]
    """Identifier"""

    nexthop: Required[str]
    """The next-hop IP Address for the static route."""

    prefix: Required[str]
    """IP Prefix in Classless Inter-Domain Routing format."""

    priority: Required[int]
    """Priority of the static route."""

    description: str
    """An optional human provided description of the static route."""

    scope: ScopeParam
    """Used only for ECMP routes."""

    weight: int
    """Optional weight of the ECMP scope - if provided."""
