# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FeedPollParams"]


class FeedPollParams(TypedDict, total=False):
    account_id: Required[str]

    feed_id: Union[str, Literal["all"]]
