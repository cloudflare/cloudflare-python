# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["SilenceCreateParams", "Body"]


class SilenceCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account id"""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    end_time: str
    """When the silence ends."""

    policy_id: str
    """The unique identifier of a notification policy"""

    start_time: str
    """When the silence starts."""
