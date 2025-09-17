# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ......_types import SequenceNotStr

__all__ = ["TagUpdateParams"]


class TagUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    body: Required[SequenceNotStr[str]]
    """Tags associated with the Worker."""
