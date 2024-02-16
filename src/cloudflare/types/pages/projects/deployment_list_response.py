# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = [
    "DeploymentListResponse",
    "DeploymentListResponseItem",
    "DeploymentListResponseItemDeploymentTrigger",
    "DeploymentListResponseItemDeploymentTriggerMetadata",
    "DeploymentListResponseItemStage",
]


class DeploymentListResponseItemDeploymentTriggerMetadata(BaseModel):
    branch: Optional[str] = None
    """Where the trigger happened."""

    commit_hash: Optional[str] = None
    """Hash of the deployment trigger commit."""

    commit_message: Optional[str] = None
    """Message of the deployment trigger commit."""


class DeploymentListResponseItemDeploymentTrigger(BaseModel):
    metadata: Optional[DeploymentListResponseItemDeploymentTriggerMetadata] = None
    """Additional info about the trigger."""

    type: Optional[str] = None
    """What caused the deployment."""


class DeploymentListResponseItemStage(BaseModel):
    ended_on: Optional[datetime] = None
    """When the stage ended."""

    name: Optional[str] = None
    """The current build stage."""

    started_on: Optional[datetime] = None
    """When the stage started."""

    status: Optional[str] = None
    """State of the current stage."""


class DeploymentListResponseItem(BaseModel):
    id: Optional[str] = None
    """Id of the deployment."""

    aliases: Optional[List[object]] = None
    """A list of alias URLs pointing to this deployment."""

    build_config: Optional[object] = None

    created_on: Optional[datetime] = None
    """When the deployment was created."""

    deployment_trigger: Optional[DeploymentListResponseItemDeploymentTrigger] = None
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

    stages: Optional[List[DeploymentListResponseItemStage]] = None
    """List of past stages."""

    url: Optional[str] = None
    """The live URL to view this deployment."""


DeploymentListResponse = List[DeploymentListResponseItem]
