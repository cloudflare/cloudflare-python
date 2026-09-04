# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TransformationsC2paEditParams"]


class TransformationsC2paEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    value: Required[Literal["off", "on"]]
    """Whether C2PA signing is enabled for image transformations."""
