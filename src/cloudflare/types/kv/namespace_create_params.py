# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NamespaceCreateParams"]


class NamespaceCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    title: Required[str]
    """A human-readable string name for a Namespace."""

    jurisdiction: Literal["eu", "fedramp", "us"]
    """
    Specify the jurisdiction to restrict the KV namespace to durably store data
    within. Can only be set at namespace creation time.
    """
