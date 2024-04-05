# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .scope import Scope
from ..._models import BaseModel

__all__ = ["RouteCreateResponse", "Route"]


class Route(BaseModel):
    nexthop: str
    """The next-hop IP Address for the static route."""

    prefix: str
    """IP Prefix in Classless Inter-Domain Routing format."""

    priority: int
    """Priority of the static route."""

    id: Optional[str] = None
    """Identifier"""

    created_on: Optional[datetime] = None
    """When the route was created."""

    description: Optional[str] = None
    """An optional human provided description of the static route."""

    modified_on: Optional[datetime] = None
    """When the route was last modified."""

    scope: Optional[Scope] = None
    """Used only for ECMP routes."""

    weight: Optional[int] = None
    """Optional weight of the ECMP scope - if provided."""


class RouteCreateResponse(BaseModel):
    routes: Optional[List[Route]] = None
