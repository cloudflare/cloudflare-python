# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OutputUpdateParams"]


class OutputUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    live_input_identifier: Required[str]
    """A unique identifier for a live input."""

    enabled: Required[bool]
    """
    When enabled, live video streamed to the associated live input will be sent to
    the output URL. When disabled, live video will not be sent to the output URL,
    even when streaming to the associated live input. Use this to control precisely
    when you start and stop simulcasting to specific destinations like YouTube and
    Twitch.
    """
