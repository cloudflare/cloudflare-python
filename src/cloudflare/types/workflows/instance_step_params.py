# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InstanceStepParams"]


class InstanceStepParams(TypedDict, total=False):
    account_id: Required[str]

    workflow_name: Required[str]

    name: Required[str]
    """
    Exact step name from the instance logs response, including the generated counter
    suffix.
    """

    type: Required[Literal["step", "waitForEvent"]]
    """
    Step type to disambiguate step.do and waitForEvent entries that share the same
    name.
    """

    attempt: int
    """Specific attempt number to retrieve output or error for."""
