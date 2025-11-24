# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .stage import Stage
from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ProjectEditResponse",
    "CanonicalDeployment",
    "CanonicalDeploymentBuildConfig",
    "CanonicalDeploymentDeploymentTrigger",
    "CanonicalDeploymentDeploymentTriggerMetadata",
    "CanonicalDeploymentEnvVars",
    "CanonicalDeploymentEnvVarsPagesPlainTextEnvVar",
    "CanonicalDeploymentEnvVarsPagesSecretTextEnvVar",
    "CanonicalDeploymentSource",
    "CanonicalDeploymentSourceConfig",
    "DeploymentConfigs",
    "DeploymentConfigsPreview",
    "DeploymentConfigsPreviewEnvVars",
    "DeploymentConfigsPreviewEnvVarsPagesPlainTextEnvVar",
    "DeploymentConfigsPreviewEnvVarsPagesSecretTextEnvVar",
    "DeploymentConfigsPreviewAIBindings",
    "DeploymentConfigsPreviewAnalyticsEngineDatasets",
    "DeploymentConfigsPreviewBrowsers",
    "DeploymentConfigsPreviewD1Databases",
    "DeploymentConfigsPreviewDurableObjectNamespaces",
    "DeploymentConfigsPreviewHyperdriveBindings",
    "DeploymentConfigsPreviewKVNamespaces",
    "DeploymentConfigsPreviewLimits",
    "DeploymentConfigsPreviewMTLSCertificates",
    "DeploymentConfigsPreviewPlacement",
    "DeploymentConfigsPreviewQueueProducers",
    "DeploymentConfigsPreviewR2Buckets",
    "DeploymentConfigsPreviewServices",
    "DeploymentConfigsPreviewVectorizeBindings",
    "DeploymentConfigsProduction",
    "DeploymentConfigsProductionEnvVars",
    "DeploymentConfigsProductionEnvVarsPagesPlainTextEnvVar",
    "DeploymentConfigsProductionEnvVarsPagesSecretTextEnvVar",
    "DeploymentConfigsProductionAIBindings",
    "DeploymentConfigsProductionAnalyticsEngineDatasets",
    "DeploymentConfigsProductionBrowsers",
    "DeploymentConfigsProductionD1Databases",
    "DeploymentConfigsProductionDurableObjectNamespaces",
    "DeploymentConfigsProductionHyperdriveBindings",
    "DeploymentConfigsProductionKVNamespaces",
    "DeploymentConfigsProductionLimits",
    "DeploymentConfigsProductionMTLSCertificates",
    "DeploymentConfigsProductionPlacement",
    "DeploymentConfigsProductionQueueProducers",
    "DeploymentConfigsProductionR2Buckets",
    "DeploymentConfigsProductionServices",
    "DeploymentConfigsProductionVectorizeBindings",
    "LatestDeployment",
    "LatestDeploymentBuildConfig",
    "LatestDeploymentDeploymentTrigger",
    "LatestDeploymentDeploymentTriggerMetadata",
    "LatestDeploymentEnvVars",
    "LatestDeploymentEnvVarsPagesPlainTextEnvVar",
    "LatestDeploymentEnvVarsPagesSecretTextEnvVar",
    "LatestDeploymentSource",
    "LatestDeploymentSourceConfig",
    "BuildConfig",
    "Source",
    "SourceConfig",
]


class CanonicalDeploymentBuildConfig(BaseModel):
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


class CanonicalDeploymentDeploymentTriggerMetadata(BaseModel):
    branch: str
    """Where the trigger happened."""

    commit_dirty: bool
    """Whether the deployment trigger commit was dirty."""

    commit_hash: str
    """Hash of the deployment trigger commit."""

    commit_message: str
    """Message of the deployment trigger commit."""


class CanonicalDeploymentDeploymentTrigger(BaseModel):
    metadata: CanonicalDeploymentDeploymentTriggerMetadata
    """Additional info about the trigger."""

    type: Literal["github:push", "ad_hoc", "deploy_hook"]
    """What caused the deployment."""


class CanonicalDeploymentEnvVarsPagesPlainTextEnvVar(BaseModel):
    type: Literal["plain_text"]

    value: str
    """Environment variable value."""


class CanonicalDeploymentEnvVarsPagesSecretTextEnvVar(BaseModel):
    type: Literal["secret_text"]

    value: str
    """Secret value."""


CanonicalDeploymentEnvVars: TypeAlias = Annotated[
    Union[
        Optional[CanonicalDeploymentEnvVarsPagesPlainTextEnvVar],
        Optional[CanonicalDeploymentEnvVarsPagesSecretTextEnvVar],
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class CanonicalDeploymentSourceConfig(BaseModel):
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


class CanonicalDeploymentSource(BaseModel):
    config: CanonicalDeploymentSourceConfig

    type: Literal["github", "gitlab"]
    """The source control management provider."""


class CanonicalDeployment(BaseModel):
    id: str
    """Id of the deployment."""

    aliases: Optional[List[str]] = None
    """A list of alias URLs pointing to this deployment."""

    build_config: CanonicalDeploymentBuildConfig
    """Configs for the project build process."""

    created_on: datetime
    """When the deployment was created."""

    deployment_trigger: CanonicalDeploymentDeploymentTrigger
    """Info about what caused the deployment."""

    env_vars: Optional[Dict[str, Optional[CanonicalDeploymentEnvVars]]] = None
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

    source: CanonicalDeploymentSource
    """Configs for the project source control."""

    stages: List[Stage]
    """List of past stages."""

    url: str
    """The live URL to view this deployment."""

    uses_functions: Optional[bool] = None
    """Whether the deployment uses functions."""


class DeploymentConfigsPreviewEnvVarsPagesPlainTextEnvVar(BaseModel):
    type: Literal["plain_text"]

    value: str
    """Environment variable value."""


class DeploymentConfigsPreviewEnvVarsPagesSecretTextEnvVar(BaseModel):
    type: Literal["secret_text"]

    value: str
    """Secret value."""


DeploymentConfigsPreviewEnvVars: TypeAlias = Annotated[
    Union[
        Optional[DeploymentConfigsPreviewEnvVarsPagesPlainTextEnvVar],
        Optional[DeploymentConfigsPreviewEnvVarsPagesSecretTextEnvVar],
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class DeploymentConfigsPreviewAIBindings(BaseModel):
    project_id: str


class DeploymentConfigsPreviewAnalyticsEngineDatasets(BaseModel):
    dataset: str
    """Name of the dataset."""


class DeploymentConfigsPreviewBrowsers(BaseModel):
    pass


class DeploymentConfigsPreviewD1Databases(BaseModel):
    id: str
    """UUID of the D1 database."""


class DeploymentConfigsPreviewDurableObjectNamespaces(BaseModel):
    namespace_id: str
    """ID of the Durable Object namespace."""


class DeploymentConfigsPreviewHyperdriveBindings(BaseModel):
    id: str


class DeploymentConfigsPreviewKVNamespaces(BaseModel):
    namespace_id: str
    """ID of the KV namespace."""


class DeploymentConfigsPreviewLimits(BaseModel):
    cpu_ms: int
    """CPU time limit in milliseconds."""


class DeploymentConfigsPreviewMTLSCertificates(BaseModel):
    certificate_id: str


class DeploymentConfigsPreviewPlacement(BaseModel):
    mode: str
    """Placement mode."""


class DeploymentConfigsPreviewQueueProducers(BaseModel):
    name: str
    """Name of the Queue."""


class DeploymentConfigsPreviewR2Buckets(BaseModel):
    name: str
    """Name of the R2 bucket."""

    jurisdiction: Optional[str] = None
    """Jurisdiction of the R2 bucket."""


class DeploymentConfigsPreviewServices(BaseModel):
    environment: str
    """The Service environment."""

    service: str
    """The Service name."""

    entrypoint: Optional[str] = None
    """The entrypoint to bind to."""


class DeploymentConfigsPreviewVectorizeBindings(BaseModel):
    index_name: str


class DeploymentConfigsPreview(BaseModel):
    always_use_latest_compatibility_date: bool
    """Whether to always use the latest compatibility date for Pages Functions."""

    build_image_major_version: int
    """The major version of the build image to use for Pages Functions."""

    compatibility_date: str
    """Compatibility date used for Pages Functions."""

    compatibility_flags: List[str]
    """Compatibility flags used for Pages Functions."""

    env_vars: Optional[Dict[str, Optional[DeploymentConfigsPreviewEnvVars]]] = None
    """Environment variables used for builds and Pages Functions."""

    fail_open: bool
    """Whether to fail open when the deployment config cannot be applied."""

    usage_model: Literal["standard", "bundled", "unbound"]
    """The usage model for Pages Functions."""

    ai_bindings: Optional[Dict[str, DeploymentConfigsPreviewAIBindings]] = None
    """Constellation bindings used for Pages Functions."""

    analytics_engine_datasets: Optional[Dict[str, DeploymentConfigsPreviewAnalyticsEngineDatasets]] = None
    """Analytics Engine bindings used for Pages Functions."""

    browsers: Optional[Dict[str, Optional[DeploymentConfigsPreviewBrowsers]]] = None
    """Browser bindings used for Pages Functions."""

    d1_databases: Optional[Dict[str, DeploymentConfigsPreviewD1Databases]] = None
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[Dict[str, DeploymentConfigsPreviewDurableObjectNamespaces]] = None
    """Durable Object namespaces used for Pages Functions."""

    hyperdrive_bindings: Optional[Dict[str, DeploymentConfigsPreviewHyperdriveBindings]] = None
    """Hyperdrive bindings used for Pages Functions."""

    kv_namespaces: Optional[Dict[str, DeploymentConfigsPreviewKVNamespaces]] = None
    """KV namespaces used for Pages Functions."""

    limits: Optional[DeploymentConfigsPreviewLimits] = None
    """Limits for Pages Functions."""

    mtls_certificates: Optional[Dict[str, DeploymentConfigsPreviewMTLSCertificates]] = None
    """mTLS bindings used for Pages Functions."""

    placement: Optional[DeploymentConfigsPreviewPlacement] = None
    """Placement setting used for Pages Functions."""

    queue_producers: Optional[Dict[str, DeploymentConfigsPreviewQueueProducers]] = None
    """Queue Producer bindings used for Pages Functions."""

    r2_buckets: Optional[Dict[str, DeploymentConfigsPreviewR2Buckets]] = None
    """R2 buckets used for Pages Functions."""

    services: Optional[Dict[str, DeploymentConfigsPreviewServices]] = None
    """Services used for Pages Functions."""

    vectorize_bindings: Optional[Dict[str, DeploymentConfigsPreviewVectorizeBindings]] = None
    """Vectorize bindings used for Pages Functions."""

    wrangler_config_hash: Optional[str] = None
    """Hash of the Wrangler configuration used for the deployment."""


class DeploymentConfigsProductionEnvVarsPagesPlainTextEnvVar(BaseModel):
    type: Literal["plain_text"]

    value: str
    """Environment variable value."""


class DeploymentConfigsProductionEnvVarsPagesSecretTextEnvVar(BaseModel):
    type: Literal["secret_text"]

    value: str
    """Secret value."""


DeploymentConfigsProductionEnvVars: TypeAlias = Annotated[
    Union[
        Optional[DeploymentConfigsProductionEnvVarsPagesPlainTextEnvVar],
        Optional[DeploymentConfigsProductionEnvVarsPagesSecretTextEnvVar],
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class DeploymentConfigsProductionAIBindings(BaseModel):
    project_id: str


class DeploymentConfigsProductionAnalyticsEngineDatasets(BaseModel):
    dataset: str
    """Name of the dataset."""


class DeploymentConfigsProductionBrowsers(BaseModel):
    pass


class DeploymentConfigsProductionD1Databases(BaseModel):
    id: str
    """UUID of the D1 database."""


class DeploymentConfigsProductionDurableObjectNamespaces(BaseModel):
    namespace_id: str
    """ID of the Durable Object namespace."""


class DeploymentConfigsProductionHyperdriveBindings(BaseModel):
    id: str


class DeploymentConfigsProductionKVNamespaces(BaseModel):
    namespace_id: str
    """ID of the KV namespace."""


class DeploymentConfigsProductionLimits(BaseModel):
    cpu_ms: int
    """CPU time limit in milliseconds."""


class DeploymentConfigsProductionMTLSCertificates(BaseModel):
    certificate_id: str


class DeploymentConfigsProductionPlacement(BaseModel):
    mode: str
    """Placement mode."""


class DeploymentConfigsProductionQueueProducers(BaseModel):
    name: str
    """Name of the Queue."""


class DeploymentConfigsProductionR2Buckets(BaseModel):
    name: str
    """Name of the R2 bucket."""

    jurisdiction: Optional[str] = None
    """Jurisdiction of the R2 bucket."""


class DeploymentConfigsProductionServices(BaseModel):
    environment: str
    """The Service environment."""

    service: str
    """The Service name."""

    entrypoint: Optional[str] = None
    """The entrypoint to bind to."""


class DeploymentConfigsProductionVectorizeBindings(BaseModel):
    index_name: str


class DeploymentConfigsProduction(BaseModel):
    always_use_latest_compatibility_date: bool
    """Whether to always use the latest compatibility date for Pages Functions."""

    build_image_major_version: int
    """The major version of the build image to use for Pages Functions."""

    compatibility_date: str
    """Compatibility date used for Pages Functions."""

    compatibility_flags: List[str]
    """Compatibility flags used for Pages Functions."""

    env_vars: Optional[Dict[str, Optional[DeploymentConfigsProductionEnvVars]]] = None
    """Environment variables used for builds and Pages Functions."""

    fail_open: bool
    """Whether to fail open when the deployment config cannot be applied."""

    usage_model: Literal["standard", "bundled", "unbound"]
    """The usage model for Pages Functions."""

    ai_bindings: Optional[Dict[str, DeploymentConfigsProductionAIBindings]] = None
    """Constellation bindings used for Pages Functions."""

    analytics_engine_datasets: Optional[Dict[str, DeploymentConfigsProductionAnalyticsEngineDatasets]] = None
    """Analytics Engine bindings used for Pages Functions."""

    browsers: Optional[Dict[str, Optional[DeploymentConfigsProductionBrowsers]]] = None
    """Browser bindings used for Pages Functions."""

    d1_databases: Optional[Dict[str, DeploymentConfigsProductionD1Databases]] = None
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[Dict[str, DeploymentConfigsProductionDurableObjectNamespaces]] = None
    """Durable Object namespaces used for Pages Functions."""

    hyperdrive_bindings: Optional[Dict[str, DeploymentConfigsProductionHyperdriveBindings]] = None
    """Hyperdrive bindings used for Pages Functions."""

    kv_namespaces: Optional[Dict[str, DeploymentConfigsProductionKVNamespaces]] = None
    """KV namespaces used for Pages Functions."""

    limits: Optional[DeploymentConfigsProductionLimits] = None
    """Limits for Pages Functions."""

    mtls_certificates: Optional[Dict[str, DeploymentConfigsProductionMTLSCertificates]] = None
    """mTLS bindings used for Pages Functions."""

    placement: Optional[DeploymentConfigsProductionPlacement] = None
    """Placement setting used for Pages Functions."""

    queue_producers: Optional[Dict[str, DeploymentConfigsProductionQueueProducers]] = None
    """Queue Producer bindings used for Pages Functions."""

    r2_buckets: Optional[Dict[str, DeploymentConfigsProductionR2Buckets]] = None
    """R2 buckets used for Pages Functions."""

    services: Optional[Dict[str, DeploymentConfigsProductionServices]] = None
    """Services used for Pages Functions."""

    vectorize_bindings: Optional[Dict[str, DeploymentConfigsProductionVectorizeBindings]] = None
    """Vectorize bindings used for Pages Functions."""

    wrangler_config_hash: Optional[str] = None
    """Hash of the Wrangler configuration used for the deployment."""


class DeploymentConfigs(BaseModel):
    preview: DeploymentConfigsPreview
    """Configs for preview deploys."""

    production: DeploymentConfigsProduction
    """Configs for production deploys."""


class LatestDeploymentBuildConfig(BaseModel):
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


class LatestDeploymentDeploymentTriggerMetadata(BaseModel):
    branch: str
    """Where the trigger happened."""

    commit_dirty: bool
    """Whether the deployment trigger commit was dirty."""

    commit_hash: str
    """Hash of the deployment trigger commit."""

    commit_message: str
    """Message of the deployment trigger commit."""


class LatestDeploymentDeploymentTrigger(BaseModel):
    metadata: LatestDeploymentDeploymentTriggerMetadata
    """Additional info about the trigger."""

    type: Literal["github:push", "ad_hoc", "deploy_hook"]
    """What caused the deployment."""


class LatestDeploymentEnvVarsPagesPlainTextEnvVar(BaseModel):
    type: Literal["plain_text"]

    value: str
    """Environment variable value."""


class LatestDeploymentEnvVarsPagesSecretTextEnvVar(BaseModel):
    type: Literal["secret_text"]

    value: str
    """Secret value."""


LatestDeploymentEnvVars: TypeAlias = Annotated[
    Union[
        Optional[LatestDeploymentEnvVarsPagesPlainTextEnvVar],
        Optional[LatestDeploymentEnvVarsPagesSecretTextEnvVar],
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class LatestDeploymentSourceConfig(BaseModel):
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


class LatestDeploymentSource(BaseModel):
    config: LatestDeploymentSourceConfig

    type: Literal["github", "gitlab"]
    """The source control management provider."""


class LatestDeployment(BaseModel):
    id: str
    """Id of the deployment."""

    aliases: Optional[List[str]] = None
    """A list of alias URLs pointing to this deployment."""

    build_config: LatestDeploymentBuildConfig
    """Configs for the project build process."""

    created_on: datetime
    """When the deployment was created."""

    deployment_trigger: LatestDeploymentDeploymentTrigger
    """Info about what caused the deployment."""

    env_vars: Optional[Dict[str, Optional[LatestDeploymentEnvVars]]] = None
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

    source: LatestDeploymentSource
    """Configs for the project source control."""

    stages: List[Stage]
    """List of past stages."""

    url: str
    """The live URL to view this deployment."""

    uses_functions: Optional[bool] = None
    """Whether the deployment uses functions."""


class BuildConfig(BaseModel):
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
    config: SourceConfig

    type: Literal["github", "gitlab"]
    """The source control management provider."""


class ProjectEditResponse(BaseModel):
    id: str
    """ID of the project."""

    canonical_deployment: Optional[CanonicalDeployment] = None
    """Most recent production deployment of the project."""

    created_on: datetime
    """When the project was created."""

    deployment_configs: DeploymentConfigs
    """Configs for deployments in a project."""

    framework: str
    """Framework the project is using."""

    framework_version: str
    """Version of the framework the project is using."""

    latest_deployment: Optional[LatestDeployment] = None
    """Most recent deployment of the project."""

    name: str
    """Name of the project."""

    preview_script_name: str
    """Name of the preview script."""

    production_branch: str
    """Production branch of the project. Used to identify production deployments."""

    production_script_name: str
    """Name of the production script."""

    uses_functions: Optional[bool] = None
    """Whether the project uses functions."""

    build_config: Optional[BuildConfig] = None
    """Configs for the project build process."""

    domains: Optional[List[str]] = None
    """A list of associated custom domains for the project."""

    source: Optional[Source] = None
    """Configs for the project source control."""

    subdomain: Optional[str] = None
    """The Cloudflare subdomain associated with the project."""
