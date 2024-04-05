# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .stage import Stage
from ..._models import BaseModel

__all__ = ["Deployment", "DeploymentTrigger", "DeploymentTriggerMetadata"]


class DeploymentTriggerMetadata(BaseModel):
    branch: Optional[str] = None
    """Where the trigger happened."""

    commit_hash: Optional[str] = None
    """Hash of the deployment trigger commit."""

    commit_message: Optional[str] = None
    """Message of the deployment trigger commit."""


class DeploymentTrigger(BaseModel):
    metadata: Optional[DeploymentTriggerMetadata] = None
    """Additional info about the trigger."""

    type: Optional[str] = None
    """What caused the deployment."""


class Deployment(BaseModel):
    id: Optional[str] = None
    """Id of the deployment."""

    aliases: Optional[List[object]] = None
    """A list of alias URLs pointing to this deployment."""

    build_config: Optional[object] = None

    created_on: Optional[datetime] = None
    """When the deployment was created."""

    deployment_trigger: Optional[DeploymentTrigger] = None
    """Info about what caused the deployment."""

    env_vars: Optional[object] = None
    """A dict of env variables to build this deploy."""

    environment: Optional[str] = None
    """Type of deploy."""

    is_skipped: Optional[bool] = None
    """If the deployment has been skipped."""

    latest_stage: Optional[object] = None

    modified_on: Optional[datetime] = None
    """When the deployment was last modified."""

    project_id: Optional[str] = None
    """Id of the project."""

    project_name: Optional[str] = None
    """Name of the project."""

    short_id: Optional[str] = None
    """Short Id (8 character) of the deployment."""

    source: Optional[object] = None

    stages: Optional[List[Stage]] = None
    """List of past stages."""

    url: Optional[str] = None
    """The live URL to view this deployment."""
