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
    """
    Optionally specify `recipient_account_id` to target a specific account, or `organization_id` to target the caller's whole organization. If neither is provided, the caller's organization is used.
    The legacy field `account_id` is accepted as a synonym for `recipient_account_id` during the deprecation period (see `x-sunset` on that field).
    """

    account_id: str
    """Deprecated alias for `recipient_account_id`.

    Use `recipient_account_id` instead. The body field collided with the URL path
    parameter of the same name, which prevented SDK generators from distinguishing
    the source account (in the URL) from the recipient account (in the body). Both
    names will continue to be accepted until 2027-05-26 (see `x-sunset`).
    """

    organization_id: str
    """Organization identifier."""

    recipient_account_id: str
    """The account that will receive the share."""


class Resource(TypedDict, total=False):
    meta: Required[object]
    """Resource Metadata."""

    resource_account_id: Required[str]
    """Account identifier."""

    resource_id: Required[str]
    """Share Resource identifier."""

    resource_type: Required[
        Literal[
            "custom-ruleset",
            "gateway-policy",
            "gateway-destination-ip",
            "gateway-block-page-settings",
            "gateway-extended-email-matching",
            "idp-federation-grant",
        ]
    ]
    """Resource Type."""
