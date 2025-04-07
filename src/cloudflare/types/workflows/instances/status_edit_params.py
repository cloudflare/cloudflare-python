# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["StatusEditParams"]


class StatusEditParams(TypedDict, total=False):
    account_id: Required[str]

    workflow_name: Required[str]

    status: Required[Literal["resume", "pause", "terminate"]]
    """Possible actions to apply to instance"""
