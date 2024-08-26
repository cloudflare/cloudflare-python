# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["MessagePullParams"]

class MessagePullParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    batch_size: float
    """The maximum number of messages to include in a batch."""

    visibility_timeout: float
    """The number of milliseconds that a message is exclusively leased.

    After the timeout, the message becomes available for another attempt.
    """