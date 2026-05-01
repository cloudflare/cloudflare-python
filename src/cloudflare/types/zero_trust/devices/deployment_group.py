# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["DeploymentGroup", "VersionConfig"]


class VersionConfig(BaseModel):
    target_environment: Optional[str] = None
    """The target environment for the client version (e.g., windows, macos)."""

    version: str
    """The specific client version to deploy."""


class DeploymentGroup(BaseModel):
    id: str
    """The ID of the deployment group."""

    created_at: str
    """The RFC3339Nano timestamp when the deployment group was created."""

    name: str
    """A user-friendly name for the deployment group."""

    updated_at: str
    """The RFC3339Nano timestamp when the deployment group was last updated."""

    version_config: List[VersionConfig]
    """Contains version configurations for different target environments."""

    policy_ids: Optional[List[str]] = None
    """Contains a list of policy IDs assigned to this deployment group."""
