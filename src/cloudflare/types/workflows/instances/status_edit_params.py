# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["StatusEditParams", "From"]


class StatusEditParams(TypedDict, total=False):
    account_id: Required[str]

    workflow_name: Required[str]

    status: Required[Literal["resume", "pause", "terminate", "restart"]]
    """Apply action to instance."""

    from_: Annotated[From, PropertyInfo(alias="from")]
    """Step to restart from. Only applicable when status is "restart"."""


class From(TypedDict, total=False):
    """Step to restart from. Only applicable when status is "restart"."""

    name: Required[str]

    count: int

    type: Literal["do", "sleep", "waitForEvent"]
