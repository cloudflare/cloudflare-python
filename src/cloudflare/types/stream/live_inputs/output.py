# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["Output"]


class Output(BaseModel):
    enabled: Optional[bool] = None
    """
    When enabled, live video streamed to the associated live input will be sent to
    the output URL. When disabled, live video will not be sent to the output URL,
    even when streaming to the associated live input. Use this to control precisely
    when you start and stop simulcasting to specific destinations like YouTube and
    Twitch.
    """

    stream_key: Optional[str] = FieldInfo(alias="streamKey", default=None)
    """The streamKey used to authenticate against an output's target."""

    uid: Optional[str] = None
    """A unique identifier for the output."""

    url: Optional[str] = None
    """The URL an output uses to restream."""
