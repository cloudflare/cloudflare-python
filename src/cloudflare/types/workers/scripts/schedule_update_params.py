# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ScheduleUpdateParams", "Body"]


class ScheduleUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    cron: Required[str]
