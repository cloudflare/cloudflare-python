# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EventCreateParams"]


class EventCreateParams(TypedDict, total=False):
    account_id: Required[str]

    workflow_name: Required[str]

    instance_id: Required[str]
    """Instance identifier.

    User-created instances match `^[a-zA-Z0-9_][a-zA-Z0-9-_]*$` (max 100
    characters); cron-triggered instances can use a longer, system-generated id
    derived from the cron expression.
    """

    body: object
