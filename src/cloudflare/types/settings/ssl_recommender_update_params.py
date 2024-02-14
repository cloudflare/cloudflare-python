# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SSLRecommenderUpdateParams", "Value"]


class SSLRecommenderUpdateParams(TypedDict, total=False):
    value: Required[Value]
    """
    Enrollment in the SSL/TLS Recommender service which tries to detect and
    recommend (by sending periodic emails) the most secure SSL/TLS setting your
    origin servers support.
    """


class Value(TypedDict, total=False):
    id: Literal["ssl_recommender"]
    """Enrollment value for SSL/TLS Recommender."""

    enabled: bool
    """ssl-recommender enrollment setting."""
