# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["MaintenanceConfigGetResponse", "MaintenanceConfig", "MaintenanceConfigCompaction"]


class MaintenanceConfigCompaction(BaseModel):
    """Configures compaction settings for table optimization."""

    state: Literal["enabled", "disabled"]
    """Specifies the state of maintenance operations."""

    target_size_mb: Literal["64", "128", "256", "512"]
    """Sets the target file size for compaction in megabytes."""


class MaintenanceConfig(BaseModel):
    """Configures maintenance for the table."""

    compaction: Optional[MaintenanceConfigCompaction] = None
    """Configures compaction settings for table optimization."""


class MaintenanceConfigGetResponse(BaseModel):
    """Contains table maintenance configuration."""

    maintenance_config: MaintenanceConfig
    """Configures maintenance for the table."""
