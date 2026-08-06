# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MessagePurgeParams", "Ref"]


class MessagePurgeParams(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    refs: Required[Iterable[Ref]]


class Ref(TypedDict, total=False):
    ref: Required[str]
    """An opaque reference to a peeked message.

    You must hold on to this value and use it to purge the message.
    """
