# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WorkflowUpdateParams", "Limits"]


class WorkflowUpdateParams(TypedDict, total=False):
    account_id: str

    class_name: Required[str]

    script_name: Required[str]

    limits: Limits


class Limits(TypedDict, total=False):
    steps: int
