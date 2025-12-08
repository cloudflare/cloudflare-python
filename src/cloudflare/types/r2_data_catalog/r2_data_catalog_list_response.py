# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "R2DataCatalogListResponse",
    "Warehouse",
    "WarehouseMaintenanceConfig",
    "WarehouseMaintenanceConfigCompaction",
]


class WarehouseMaintenanceConfigCompaction(BaseModel):
    """Configures compaction for catalog maintenance."""

    state: Literal["enabled", "disabled"]
    """Specifies the state of maintenance operations."""

    target_size_mb: Literal["64", "128", "256", "512"]
    """Sets the target file size for compaction in megabytes."""


class WarehouseMaintenanceConfig(BaseModel):
    """Configures maintenance for the catalog."""

    compaction: Optional[WarehouseMaintenanceConfigCompaction] = None
    """Configures compaction for catalog maintenance."""


class Warehouse(BaseModel):
    """Contains R2 Data Catalog information."""

    id: str
    """Use this to uniquely identify the catalog."""

    bucket: str
    """Specifies the associated R2 bucket name."""

    name: str
    """Specifies the catalog name (generated from account and bucket name)."""

    status: Literal["active", "inactive"]
    """Indicates the status of the catalog."""

    credential_status: Optional[Literal["present", "absent"]] = None
    """Shows the credential configuration status."""

    maintenance_config: Optional[WarehouseMaintenanceConfig] = None
    """Configures maintenance for the catalog."""


class R2DataCatalogListResponse(BaseModel):
    """Contains the list of catalogs."""

    warehouses: List[Warehouse]
    """Lists catalogs in the account."""
