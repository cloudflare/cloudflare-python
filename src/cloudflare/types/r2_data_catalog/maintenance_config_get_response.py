# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MaintenanceConfigGetResponse", "MaintenanceConfig", "MaintenanceConfigCompaction"]


class MaintenanceConfigCompaction(BaseModel):
    state: Literal["enabled", "disabled"]
    """Specifies the state of maintenance operations."""

    target_size_mb: Literal["64", "128", "256", "512"]
    """Sets the target file size for compaction in megabytes."""


class MaintenanceConfig(BaseModel):
    compaction: Optional[MaintenanceConfigCompaction] = None
    """Configures compaction for catalog maintenance."""


class MaintenanceConfigGetResponse(BaseModel):
    credential_status: Literal["present", "absent"]
    """Shows the credential configuration status."""

    maintenance_config: MaintenanceConfig
    """Configures maintenance for the catalog."""
