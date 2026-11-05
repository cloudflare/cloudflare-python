# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SpendPolicyGetResponse", "CurrentState", "CurrentStateEnforcement"]


class CurrentStateEnforcement(BaseModel):
    """
    Durable desired cap and delivery bookkeeping for this policy, or null if no owned effect exists. Separate from threshold evaluation: pending/leased/retry can lag the new billing period. Succeeded with equal generations means delivery completed, not an EWC readback.
    """

    applied_generation: int

    delivery_status: Literal["pending", "leased", "retry", "succeeded"]

    desired_generation: int

    desired_state: Literal["active", "inactive"]

    expires_at: Optional[datetime] = None


class CurrentState(BaseModel):
    """
    Read-only state on list/get responses, evaluated from the latest owning projector snapshot at request time, independently of the API replica. Configuration enabled/version/ETag do not change when a cycle rolls over. Audit history remains unchanged. Missing during a rolling upgrade or on mutation responses; clients must treat missing state as unavailable. Balances are asynchronous estimates, not a synchronous usage read.
    """

    balance_cents: Optional[int] = None

    billing_period_end: Optional[datetime] = None

    billing_period_start: Optional[datetime] = None

    enforcement: Optional[CurrentStateEnforcement] = None
    """
    Durable desired cap and delivery bookkeeping for this policy, or null if no
    owned effect exists. Separate from threshold evaluation: pending/leased/retry
    can lag the new billing period. Succeeded with equal generations means delivery
    completed, not an EWC readback.
    """

    evaluated_at: datetime
    """Evaluation time; not the timestamp of the latest usage event."""

    status: Literal["disabled", "no_current_period", "unavailable", "below_limit", "limit_reached"]
    """Threshold evaluation, not proof of an edge cap.

    No current active period yields no_current_period for enabled policies; failed
    aggregate reads yield unavailable for enabled policies. Disabled policies report
    disabled. Neither no_current_period nor unavailable implies a zero balance or
    below-limit state. Operators may disable current-state reads, in which case
    current_state is omitted.
    """


class SpendPolicyGetResponse(BaseModel):
    """A spend policy."""

    id: str
    """The unique identifier of the spend policy."""

    account_id: int
    """Internal numeric ID of the account that owns the policy.

    This is not the account tag used in the path.
    """

    action: Literal["notification", "usage_block"]
    """The action taken when the threshold is reached.

    `notification` sends an email to `notification_email`. `usage_block` blocks
    further usage of the product until the end of the billing period. Raising the
    threshold above the current balance, disabling the policy, or deleting it lifts
    the block early.
    """

    enabled: bool
    """Whether the policy is evaluated."""

    name: str
    """Display name of the policy."""

    notification_email: str
    """Email address that receives notifications. An empty string when none is set."""

    product_id: Literal["workers", "durable_objects"]
    """The product the policy applies to: `workers` or `durable_objects`.

    Each product's balance and policies are separate. Both products support
    `notification` and `usage_block` policies on create and update.
    """

    threshold_cents: int
    """The spend threshold for the current billing period, in US cents."""

    version: int
    """Optimistic-concurrency version.

    It starts at 1 and goes up by one on every update or delete. This value is also
    returned in `ETag`.
    """

    current_state: Optional[CurrentState] = None
    """
    Read-only state on list/get responses, evaluated from the latest owning
    projector snapshot at request time, independently of the API replica.
    Configuration enabled/version/ETag do not change when a cycle rolls over. Audit
    history remains unchanged. Missing during a rolling upgrade or on mutation
    responses; clients must treat missing state as unavailable. Balances are
    asynchronous estimates, not a synchronous usage read.
    """
