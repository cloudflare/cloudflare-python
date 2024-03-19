# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RouteEmptyParams", "Route"]


class RouteEmptyParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    routes: Required[Iterable[Route]]


class Route(TypedDict, total=False):
    pass
