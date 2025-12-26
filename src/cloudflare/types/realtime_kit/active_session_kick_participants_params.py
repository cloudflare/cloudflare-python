# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ActiveSessionKickParticipantsParams"]


class ActiveSessionKickParticipantsParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]
    """The app identifier tag."""

    custom_participant_ids: Required[SequenceNotStr[str]]

    participant_ids: Required[SequenceNotStr[str]]
