# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["PolicyUpdateResponse", "Actions", "ActionsRemediationType", "ActionsWebhookConfig"]


class ActionsRemediationType(BaseModel):
    """A remediation type configured for the policy."""

    display_name: str
    """Display name/label of the remediation type."""

    remediation_type: str
    """The system name of the remediation type."""

    remediation_type_id: str
    """Unique identifier for the remediation type."""


class ActionsWebhookConfig(BaseModel):
    """A webhook configuration associated with the policy."""

    display_name: str
    """Display name/label of the webhook configuration."""

    webhook_config_id: str
    """Unique identifier for the webhook configuration."""


class Actions(BaseModel):
    """The actions configured for this policy."""

    remediation_types: List[ActionsRemediationType]
    """List of remediation types that will be executed."""

    webhook_configs: List[ActionsWebhookConfig]
    """List of webhook configurations that will be triggered."""


class PolicyUpdateResponse(BaseModel):
    """Response body for a policy configuration."""

    id: str
    """Unique identifier for the policy configuration."""

    actions: Actions
    """The actions configured for this policy."""

    applies_to_all_integrations: bool
    """When true, the policy applies to all integrations for the account.

    When false, it applies only to the specified integration_ids.
    """

    created_at: datetime
    """Timestamp when the policy was created."""

    description: str
    """User-set description of what this policy does. Limited to 1000 characters."""

    display_name: str
    """Display name for the policy configuration. Limited to 255 characters."""

    enabled: bool
    """Whether the policy is enabled.

    Derived from disabled_at (enabled when disabled_at is unset).
    """

    finding_type_id: str
    """The finding type this policy is associated with.

    Immutable after creation; attempts to change it via update are rejected.
    """

    integration_ids: List[str]
    """The integrations this policy applies to."""

    updated_at: datetime
    """Timestamp when the policy was last updated."""

    disabled_at: Optional[datetime] = None
    """Timestamp when the policy was disabled.

    Omitted from the response when the policy is enabled.
    """

    last_triggered_at: Optional[datetime] = None
    """Timestamp of the most recent successful policy invocation.

    Omitted from the response when the policy has never been successfully triggered.
    Only populated on GET responses; absent on responses from create/update
    endpoints.
    """
