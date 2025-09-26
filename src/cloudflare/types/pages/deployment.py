# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .stage import Stage
from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "Deployment",
    "BuildConfig",
    "DeploymentTrigger",
    "DeploymentTriggerMetadata",
    "EnvVars",
    "EnvVarsPagesPlainTextEnvVar",
    "EnvVarsPagesSecretTextEnvVar",
    "Source",
    "SourceConfig",
]


class BuildConfig(BaseModel):
    build_caching: Optional[bool] = None
    """Enable build caching for the project."""

    build_command: Optional[str] = None
    """Command used to build project."""

    destination_dir: Optional[str] = None
    """Output directory of the build."""

    root_dir: Optional[str] = None
    """Directory to run the command."""

    web_analytics_tag: Optional[str] = None
    """The classifying tag for analytics."""

    web_analytics_token: Optional[str] = None
    """The auth token for analytics."""


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

    type: Optional[Literal["push", "ad_hoc"]] = None
    """What caused the deployment."""


class EnvVarsPagesPlainTextEnvVar(BaseModel):
    type: Literal["plain_text"]

    value: str
    """Environment variable value."""


class EnvVarsPagesSecretTextEnvVar(BaseModel):
    type: Literal["secret_text"]

    value: str
    """Secret value."""


EnvVars: TypeAlias = Annotated[
    Union[Optional[EnvVarsPagesPlainTextEnvVar], Optional[EnvVarsPagesSecretTextEnvVar]],
    PropertyInfo(discriminator="type"),
]


class SourceConfig(BaseModel):
    deployments_enabled: Optional[bool] = None

    owner: Optional[str] = None

    path_excludes: Optional[List[str]] = None

    path_includes: Optional[List[str]] = None

    pr_comments_enabled: Optional[bool] = None

    preview_branch_excludes: Optional[List[str]] = None

    preview_branch_includes: Optional[List[str]] = None

    preview_deployment_setting: Optional[Literal["all", "none", "custom"]] = None

    production_branch: Optional[str] = None

    production_deployments_enabled: Optional[bool] = None

    repo_name: Optional[str] = None


class Source(BaseModel):
    config: Optional[SourceConfig] = None

    type: Optional[str] = None


class Deployment(BaseModel):
    id: Optional[str] = None
    """Id of the deployment."""

    aliases: Optional[List[str]] = None
    """A list of alias URLs pointing to this deployment."""

    build_config: Optional[BuildConfig] = None
    """Configs for the project build process."""

    created_on: Optional[datetime] = None
    """When the deployment was created."""

    deployment_trigger: Optional[DeploymentTrigger] = None
    """Info about what caused the deployment."""

    env_vars: Optional[Dict[str, EnvVars]] = None
    """Environment variables used for builds and Pages Functions."""

    environment: Optional[Literal["preview", "production"]] = None
    """Type of deploy."""

    is_skipped: Optional[bool] = None
    """If the deployment has been skipped."""

    latest_stage: Optional[Stage] = None
    """The status of the deployment."""

    modified_on: Optional[datetime] = None
    """When the deployment was last modified."""

    project_id: Optional[str] = None
    """Id of the project."""

    project_name: Optional[str] = None
    """Name of the project."""

    short_id: Optional[str] = None
    """Short Id (8 character) of the deployment."""

    source: Optional[Source] = None

    stages: Optional[List[Stage]] = None
    """List of past stages."""

    url: Optional[str] = None
    """The live URL to view this deployment."""
