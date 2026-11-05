# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AuditListResponse"]


class AuditListResponse(BaseModel):
    """
    A state transition recorded when the policy was evaluated against the account's balance.
    """

    action: Literal["notification", "usage_block"]
    """The action taken when the threshold is reached.

    `notification` sends an email to `notification_email`. `usage_block` blocks
    further usage of the product until the end of the billing period. Raising the
    threshold above the current balance, disabling the policy, or deleting it lifts
    the block early.
    """

    balance_cents: int
    """The account's balance for the product at evaluation time, in US cents."""

    billing_period_end: datetime
    """Exclusive end of the billing period that was evaluated."""

    billing_period_start: datetime
    """Inclusive start of the billing period that was evaluated."""

    created_at: datetime
    """When the entry was recorded."""

    policy_version: int
    """The policy `version` that was evaluated."""

    reason: str
    """A human-readable explanation of the trigger."""

    source: Literal["kafka", "policy_revision"]
    """What caused the evaluation.

    `kafka` means a balance update. `policy_revision` means a change to the policy.
    """

    threshold_cents: int
    """The policy threshold at evaluation time, in US cents."""

    trigger: str
    """The trigger recorded at evaluation time.

    New evaluations record `limit_reached` when the balance reaches or exceeds the
    configured threshold. Earlier entries retain their recorded trigger.
    """
