# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RouteMagicStaticRoutesUpdateManyRoutesParams", "Route", "RouteScope"]


class RouteMagicStaticRoutesUpdateManyRoutesParams(TypedDict, total=False):
    routes: Required[Iterable[Route]]


class RouteScope(TypedDict, total=False):
    colo_names: List[str]
    """List of colo names for the ECMP scope."""

    colo_regions: List[str]
    """List of colo regions for the ECMP scope."""


class Route(TypedDict, total=False):
    nexthop: Required[str]
    """The next-hop IP Address for the static route."""

    prefix: Required[str]
    """IP Prefix in Classless Inter-Domain Routing format."""

    priority: Required[int]
    """Priority of the static route."""

    description: str
    """An optional human provided description of the static route."""

    scope: RouteScope
    """Used only for ECMP routes."""

    weight: int
    """Optional weight of the ECMP scope - if provided."""
