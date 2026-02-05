# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ActiveSessionCreatePollParams"]


class ActiveSessionCreatePollParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]
    """The app identifier tag."""

    options: Required[SequenceNotStr[str]]
    """Different options for the question"""

    question: Required[str]
    """Question of the poll"""

    anonymous: bool
    """if voters on a poll are anonymous"""

    hide_votes: bool
    """if votes on an option are visible before a person votes"""
