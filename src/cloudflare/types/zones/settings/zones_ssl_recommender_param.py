# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ZonesSSLRecommenderParam"]


class ZonesSSLRecommenderParam(TypedDict, total=False):
    id: Literal["ssl_recommender"]
    """Enrollment value for SSL/TLS Recommender."""

    enabled: bool
    """ssl-recommender enrollment setting."""
