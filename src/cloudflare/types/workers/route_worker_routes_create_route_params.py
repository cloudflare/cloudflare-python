# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RouteWorkerRoutesCreateRouteParams"]


class RouteWorkerRoutesCreateRouteParams(TypedDict, total=False):
    pattern: Required[str]

    script: str
    """Name of the script, used in URLs and route configuration."""
