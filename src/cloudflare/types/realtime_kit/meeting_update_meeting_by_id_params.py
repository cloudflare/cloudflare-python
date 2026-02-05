# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["MeetingUpdateMeetingByIDParams", "AIConfig", "AIConfigSummarization", "AIConfigTranscription"]


class MeetingUpdateMeetingByIDParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]
    """The app identifier tag."""

    ai_config: AIConfig
    """
    The AI Config allows you to customize the behavior of meeting transcriptions and
    summaries
    """

    live_stream_on_start: bool
    """Specifies if the meeting should start getting livestreamed on start."""

    persist_chat: bool
    """
    If a meeting is updated to persist_chat, meeting chat would remain for a week
    within the meeting space.
    """

    record_on_start: bool
    """
    Specifies if the meeting should start getting recorded as soon as someone joins
    the meeting.
    """

    session_keep_alive_time_in_secs: float
    """
    Time in seconds, for which a session remains active, after the last participant
    has left the meeting.
    """

    status: Literal["ACTIVE", "INACTIVE"]
    """Whether the meeting is `ACTIVE` or `INACTIVE`.

    Users will not be able to join an `INACTIVE` meeting.
    """

    summarize_on_end: bool
    """Automatically generate summary of meetings using transcripts.

    Requires Transcriptions to be enabled, and can be retrieved via Webhooks or
    summary API.
    """

    title: str
    """Title of the meeting"""


class AIConfigSummarization(TypedDict, total=False):
    """Summary Config"""

    summary_type: Literal[
        "general",
        "team_meeting",
        "sales_call",
        "client_check_in",
        "interview",
        "daily_standup",
        "one_on_one_meeting",
        "lecture",
        "code_review",
    ]
    """Defines the style of the summary, such as general, team meeting, or sales call."""

    text_format: Literal["plain_text", "markdown"]
    """Determines the text format of the summary, such as plain text or markdown."""

    word_limit: int
    """Sets the maximum number of words in the meeting summary."""


class AIConfigTranscription(TypedDict, total=False):
    """Transcription Configurations"""

    keywords: SequenceNotStr[str]
    """Adds specific terms to improve accurate detection during transcription."""

    language: Literal["en-US", "en-IN", "de", "hi", "sv", "ru", "pl", "el", "fr", "nl"]
    """Specifies the language code for transcription to ensure accurate results."""

    profanity_filter: bool
    """Control the inclusion of offensive language in transcriptions."""


class AIConfig(TypedDict, total=False):
    """
    The AI Config allows you to customize the behavior of meeting transcriptions and summaries
    """

    summarization: AIConfigSummarization
    """Summary Config"""

    transcription: AIConfigTranscription
    """Transcription Configurations"""
