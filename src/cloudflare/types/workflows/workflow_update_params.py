# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WorkflowUpdateParams"]


class WorkflowUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    class_name: Required[str]

    script_name: Required[str]
