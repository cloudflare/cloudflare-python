# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AnalyzeCreateParams"]


class AnalyzeCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    bundle_method: object

    certificate: str
    """The zone's SSL certificate or certificate and the intermediate(s)."""
