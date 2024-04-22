# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .ssl_recommender_param import SSLRecommenderParam

__all__ = ["SSLRecommenderEditParams"]


class SSLRecommenderEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[SSLRecommenderParam]
    """
    Enrollment in the SSL/TLS Recommender service which tries to detect and
    recommend (by sending periodic emails) the most secure SSL/TLS setting your
    origin servers support.
    """
