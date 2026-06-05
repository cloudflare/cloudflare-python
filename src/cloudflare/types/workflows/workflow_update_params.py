# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["WorkflowUpdateParams", "Limits", "Schedule"]


class WorkflowUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    class_name: Required[str]

    script_name: Required[str]

    limits: Limits

    schedules: Iterable[Schedule]


class Limits(TypedDict, total=False):
    steps: int


class Schedule(TypedDict, total=False):
    cron: Required[str]
