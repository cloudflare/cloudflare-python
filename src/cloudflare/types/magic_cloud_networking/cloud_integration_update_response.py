# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "CloudIntegrationUpdateResponse",
    "Status",
    "StatusDiscoveryProgress",
    "StatusDiscoveryProgressV2",
    "StatusInUseBy",
]


class StatusDiscoveryProgress(BaseModel):
    done: int

    total: int

    unit: str


class StatusDiscoveryProgressV2(BaseModel):
    done: int

    total: int

    unit: str


class StatusInUseBy(BaseModel):
    id: str

    client_type: Literal["MAGIC_WAN_CLOUD_ONRAMP"]

    name: str


class Status(BaseModel):
    discovery_progress: StatusDiscoveryProgress

    discovery_progress_v2: StatusDiscoveryProgressV2

    last_discovery_status: Literal["UNSPECIFIED", "PENDING", "DISCOVERING", "FAILED", "SUCCEEDED"]

    last_discovery_status_v2: Literal["UNSPECIFIED", "PENDING", "DISCOVERING", "FAILED", "SUCCEEDED"]

    regions: List[str]

    credentials_good_since: Optional[str] = None

    credentials_missing_since: Optional[str] = None

    credentials_rejected_since: Optional[str] = None

    discovery_message: Optional[str] = None

    discovery_message_v2: Optional[str] = None

    in_use_by: Optional[List[StatusInUseBy]] = None

    last_discovery_completed_at: Optional[str] = None

    last_discovery_completed_at_v2: Optional[str] = None

    last_discovery_started_at: Optional[str] = None

    last_discovery_started_at_v2: Optional[str] = None

    last_updated: Optional[str] = None


class CloudIntegrationUpdateResponse(BaseModel):
    id: str

    cloud_type: Literal["AWS", "AZURE", "GOOGLE", "CLOUDFLARE"]

    friendly_name: str

    last_updated: str

    lifecycle_state: Literal["ACTIVE", "PENDING_SETUP", "RETIRED"]

    state: Literal["UNSPECIFIED", "PENDING", "DISCOVERING", "FAILED", "SUCCEEDED"]

    state_v2: Literal["UNSPECIFIED", "PENDING", "DISCOVERING", "FAILED", "SUCCEEDED"]

    aws_arn: Optional[str] = None

    azure_subscription_id: Optional[str] = None

    azure_tenant_id: Optional[str] = None

    description: Optional[str] = None

    gcp_project_id: Optional[str] = None

    gcp_service_account_email: Optional[str] = None

    status: Optional[Status] = None
