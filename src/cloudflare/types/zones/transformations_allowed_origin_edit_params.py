# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransformationsAllowedOriginEditParams"]


class TransformationsAllowedOriginEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    value: Required[str]
    """
    Comma-separated list of allowed origin domains for image and video
    transformations. Use "\\**" to allow all origins (default).
    """
