# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MemberCreateParams", "Body"]


class MemberCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    id: Required[str]
    """The identifier of an existing account Member."""
