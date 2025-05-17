# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["MessagePushParams", "MqQueueMessageText", "MqQueueMessageJson"]


class MqQueueMessageText(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    body: str

    content_type: Literal["text"]

    delay_seconds: float
    """
    The number of seconds to wait for attempting to deliver this message to
    consumers
    """


class MqQueueMessageJson(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    body: object

    content_type: Literal["json"]

    delay_seconds: float
    """
    The number of seconds to wait for attempting to deliver this message to
    consumers
    """


MessagePushParams: TypeAlias = Union[MqQueueMessageText, MqQueueMessageJson]
