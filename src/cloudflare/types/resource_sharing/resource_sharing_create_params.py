# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResourceSharingCreateParams", "Recipient", "Resource"]


class ResourceSharingCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier."""

    name: Required[str]
    """The name of the share."""

    recipients: Required[Iterable[Recipient]]

    resources: Required[Iterable[Resource]]


class Recipient(TypedDict, total=False):
    account_id: str
    """Account identifier."""

    organization_id: str
    """Organization identifier."""


class Resource(TypedDict, total=False):
    meta: Required[object]
    """Resource Metadata."""

    resource_account_id: Required[str]
    """Account identifier."""

    resource_id: Required[str]
    """Share Resource identifier."""

    resource_type: Required[Literal["custom-ruleset", "widget"]]
    """Resource Type."""
