# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RecordingPauseResumeStopRecordingParams"]


class RecordingPauseResumeStopRecordingParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]

    action: Required[Literal["stop", "pause", "resume"]]
