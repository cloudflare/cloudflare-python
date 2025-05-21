# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["MessageBulkPushParams", "Message", "MessageMqQueueMessageText", "MessageMqQueueMessageJson"]


class MessageBulkPushParams(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    delay_seconds: float
    """The number of seconds to wait for attempting to deliver this batch to consumers"""

    messages: Iterable[Message]


class MessageMqQueueMessageText(TypedDict, total=False):
    body: str

    content_type: Literal["text"]

    delay_seconds: float
    """
    The number of seconds to wait for attempting to deliver this message to
    consumers
    """


class MessageMqQueueMessageJson(TypedDict, total=False):
    body: object

    content_type: Literal["json"]

    delay_seconds: float
    """
    The number of seconds to wait for attempting to deliver this message to
    consumers
    """


Message: TypeAlias = Union[MessageMqQueueMessageText, MessageMqQueueMessageJson]
