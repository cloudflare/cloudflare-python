# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RouteEmptyParams", "Route"]


class RouteEmptyParams(TypedDict, total=False):
    routes: Required[Iterable[Route]]


class Route(TypedDict, total=False):
    pass
