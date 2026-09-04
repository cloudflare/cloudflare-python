# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["WorkflowUpdateParams", "Concurrency", "DefaultRetention", "Limits", "Schedule"]


class WorkflowUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    class_name: Required[str]

    script_name: Required[str]

    concurrency: Concurrency

    default_retention: DefaultRetention
    """
    Default retention applied to instances of this version when they do not set
    their own retention.
    """

    limits: Limits

    schedules: Iterable[Schedule]


class Concurrency(TypedDict, total=False):
    limit: int
    """Maximum number of instances of this workflow that can run concurrently.

    Additional instances are queued and started as running instances complete. Must
    not exceed the account concurrency limit.
    """


class DefaultRetention(TypedDict, total=False):
    """
    Default retention applied to instances of this version when they do not set their own retention.
    """

    error_retention: Union[int, str]
    """Specifies the duration in milliseconds or as a string like '5 minutes'."""

    success_retention: Union[int, str]
    """Specifies the duration in milliseconds or as a string like '5 minutes'."""


class Limits(TypedDict, total=False):
    steps: int


class Schedule(TypedDict, total=False):
    cron: Required[str]
