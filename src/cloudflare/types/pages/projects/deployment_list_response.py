# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..stage import Stage
from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = [
    "DeploymentListResponse",
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
    """Configs for the project build process."""

    web_analytics_tag: Optional[str] = None
    """The classifying tag for analytics."""

    web_analytics_token: Optional[str] = None
    """The auth token for analytics."""

    build_caching: Optional[bool] = None
    """Enable build caching for the project."""

    build_command: Optional[str] = None
    """Command used to build project."""

    destination_dir: Optional[str] = None
    """Assets output directory of the build."""

    root_dir: Optional[str] = None
    """Directory to run the command."""


class DeploymentTriggerMetadata(BaseModel):
    """Additional info about the trigger."""

    branch: str
    """Where the trigger happened."""

    commit_dirty: bool
    """Whether the deployment trigger commit was dirty."""

    commit_hash: str
    """Hash of the deployment trigger commit."""

    commit_message: str
    """Message of the deployment trigger commit."""


class DeploymentTrigger(BaseModel):
    """Info about what caused the deployment."""

    metadata: DeploymentTriggerMetadata
    """Additional info about the trigger."""

    type: Literal["github:push", "ad_hoc", "deploy_hook"]
    """What caused the deployment."""


class EnvVarsPagesPlainTextEnvVar(BaseModel):
    """A plaintext environment variable."""

    type: Literal["plain_text"]

    value: str
    """Environment variable value."""


class EnvVarsPagesSecretTextEnvVar(BaseModel):
    """An encrypted environment variable."""

    type: Literal["secret_text"]

    value: str
    """Secret value."""


EnvVars: TypeAlias = Annotated[
    Union[Optional[EnvVarsPagesPlainTextEnvVar], Optional[EnvVarsPagesSecretTextEnvVar], None],
    PropertyInfo(discriminator="type"),
]


class SourceConfig(BaseModel):
    owner: str
    """The owner of the repository."""

    pr_comments_enabled: bool
    """Whether to enable PR comments."""

    production_branch: str
    """The production branch of the repository."""

    repo_name: str
    """The name of the repository."""

    deployments_enabled: Optional[bool] = None
    """
    Whether to enable automatic deployments when pushing to the source repository.
    When disabled, no deployments (production or preview) will be triggered
    automatically.
    """

    owner_id: Optional[str] = None
    """The owner ID of the repository."""

    path_excludes: Optional[List[str]] = None
    """A list of paths that should be excluded from triggering a preview deployment.

    Wildcard syntax (`*`) is supported.
    """

    path_includes: Optional[List[str]] = None
    """A list of paths that should be watched to trigger a preview deployment.

    Wildcard syntax (`*`) is supported.
    """

    preview_branch_excludes: Optional[List[str]] = None
    """A list of branches that should not trigger a preview deployment.

    Wildcard syntax (`*`) is supported. Must be used with
    `preview_deployment_setting` set to `custom`.
    """

    preview_branch_includes: Optional[List[str]] = None
    """A list of branches that should trigger a preview deployment.

    Wildcard syntax (`*`) is supported. Must be used with
    `preview_deployment_setting` set to `custom`.
    """

    preview_deployment_setting: Optional[Literal["all", "none", "custom"]] = None
    """Controls whether commits to preview branches trigger a preview deployment."""

    production_deployments_enabled: Optional[bool] = None
    """Whether to trigger a production deployment on commits to the production branch."""

    repo_id: Optional[str] = None
    """The ID of the repository."""


class Source(BaseModel):
    """Configs for the project source control."""

    config: SourceConfig

    type: Literal["github", "gitlab"]
    """The source control management provider."""


class DeploymentListResponse(BaseModel):
    id: str
    """Id of the deployment."""

    aliases: Optional[List[str]] = None
    """A list of alias URLs pointing to this deployment."""

    build_config: BuildConfig
    """Configs for the project build process."""

    created_on: datetime
    """When the deployment was created."""

    deployment_trigger: DeploymentTrigger
    """Info about what caused the deployment."""

    env_vars: Optional[Dict[str, Optional[EnvVars]]] = None
    """Environment variables used for builds and Pages Functions."""

    environment: Literal["preview", "production"]
    """Type of deploy."""

    is_skipped: bool
    """If the deployment has been skipped."""

    latest_stage: Stage
    """The status of the deployment."""

    modified_on: datetime
    """When the deployment was last modified."""

    project_id: str
    """Id of the project."""

    project_name: str
    """Name of the project."""

    short_id: str
    """Short Id (8 character) of the deployment."""

    source: Source
    """Configs for the project source control."""

    stages: List[Stage]
    """List of past stages."""

    url: str
    """The live URL to view this deployment."""

    uses_functions: Optional[bool] = None
    """Whether the deployment uses functions."""
