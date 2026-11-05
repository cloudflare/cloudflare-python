# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SearchSearchParams"]


class SearchSearchParams(TypedDict, total=False):
    account_id: Required[str]

    query: Required[str]
    """Keyword and semantic article-search text, from 1 to 1000 characters."""

    feed_id: str
    """Optional feed UUID that restricts results to articles from that feed."""

    max_results: Union[Literal[""], str]
    """Maximum search matches to request, an integer from 1 to 50.

    Defaults to 20 when omitted or empty; multiple matches from one article can
    produce fewer returned articles.
    """
