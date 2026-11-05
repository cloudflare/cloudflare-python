# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SpendPolicyCreateParams"]


class SpendPolicyCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Represents a Cloudflare resource identifier tag."""

    action: Required[Literal["notification", "usage_block"]]
    """The action taken when the threshold is reached.

    `notification` sends an email to `notification_email`. `usage_block` blocks
    further usage of the product until the end of the billing period. Raising the
    threshold above the current balance, disabling the policy, or deleting it lifts
    the block early.
    """

    enabled: Required[bool]
    """Whether the policy is evaluated."""

    name: Required[str]
    """Display name of the policy.

    After surrounding whitespace is trimmed, it must be 1 to 200 bytes long. The
    value is stored as sent, untrimmed.
    """

    product_id: Required[Literal["workers", "durable_objects"]]
    """The product the policy applies to: `workers` or `durable_objects`.

    Each product's balance and policies are separate. Both products support
    `notification` and `usage_block` policies on create and update.
    """

    threshold_cents: Required[int]
    """The spend threshold for the current billing period, in US cents.

    Must be greater than zero.
    """

    notification_email: str
    """Email address that receives notifications.

    Required when `action` is `notification`. When set, it must be a bare address
    (`user@example.com`); display-name forms such as `Name <user@example.com>` are
    rejected.
    """
