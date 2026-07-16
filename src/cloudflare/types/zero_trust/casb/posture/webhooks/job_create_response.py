# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["JobCreateResponse", "Created", "CreatedParameters", "Failed"]


class CreatedParameters(BaseModel):
    """Parameters for a webhook job."""

    finding_instance_id: str
    """ID of the finding instance."""


class Created(BaseModel):
    """Information about a webhook job."""

    id: str
    """Unique identifier for the webhook job."""

    asset_data: Dict[str, object]
    """Asset data associated with this webhook job."""

    created_at: datetime
    """When the webhook job was created."""

    integration_id: str
    """ID of the integration."""

    last_updated_at: datetime
    """When the webhook job was last updated."""

    parameters: CreatedParameters
    """Parameters for a webhook job."""

    status: Literal["pending", "processing", "completed", "failed"]
    """Status of a webhook job."""

    triggered_by_actor: Literal["user", "account_token"]
    """Type of actor that triggered the webhook job."""

    triggered_by_id: str
    """ID of the actor that triggered the job."""

    webhook_id: str
    """ID of the webhook configuration."""

    failure_details: Optional[Dict[str, object]] = None
    """Additional details about the failure."""

    failure_reason: Optional[
        Literal["Permission Denied", "Integration Unavailable", "Service Temporarily Unavailable", "System Error"]
    ] = None
    """Reason for webhook job failure."""


class Failed(BaseModel):
    """Information about a failed webhook job creation."""

    error: str
    """Error message describing the failure."""

    finding_instance_id: str
    """ID of the finding instance that failed to create a webhook job."""

    webhook_id: str
    """ID of the webhook configuration."""


class JobCreateResponse(BaseModel):
    created: List[Created]
    """Successfully created webhook jobs."""

    failed: List[Failed]
    """Failed webhook job creation attempts."""
