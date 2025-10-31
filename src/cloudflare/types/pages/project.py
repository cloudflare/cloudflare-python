# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .deployment import Deployment

__all__ = [
    "Project",
    "BuildConfig",
    "DeploymentConfigs",
    "DeploymentConfigsPreview",
    "DeploymentConfigsPreviewAIBindings",
    "DeploymentConfigsPreviewAnalyticsEngineDatasets",
    "DeploymentConfigsPreviewBrowsers",
    "DeploymentConfigsPreviewD1Databases",
    "DeploymentConfigsPreviewDurableObjectNamespaces",
    "DeploymentConfigsPreviewEnvVars",
    "DeploymentConfigsPreviewEnvVarsPagesPlainTextEnvVar",
    "DeploymentConfigsPreviewEnvVarsPagesSecretTextEnvVar",
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
    "DeploymentConfigsProductionAIBindings",
    "DeploymentConfigsProductionAnalyticsEngineDatasets",
    "DeploymentConfigsProductionBrowsers",
    "DeploymentConfigsProductionD1Databases",
    "DeploymentConfigsProductionDurableObjectNamespaces",
    "DeploymentConfigsProductionEnvVars",
    "DeploymentConfigsProductionEnvVarsPagesPlainTextEnvVar",
    "DeploymentConfigsProductionEnvVarsPagesSecretTextEnvVar",
    "DeploymentConfigsProductionHyperdriveBindings",
    "DeploymentConfigsProductionKVNamespaces",
    "DeploymentConfigsProductionLimits",
    "DeploymentConfigsProductionMTLSCertificates",
    "DeploymentConfigsProductionPlacement",
    "DeploymentConfigsProductionQueueProducers",
    "DeploymentConfigsProductionR2Buckets",
    "DeploymentConfigsProductionServices",
    "DeploymentConfigsProductionVectorizeBindings",
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


class DeploymentConfigsPreviewAIBindings(BaseModel):
    project_id: Optional[str] = None


class DeploymentConfigsPreviewAnalyticsEngineDatasets(BaseModel):
    dataset: Optional[str] = None
    """Name of the dataset."""


class DeploymentConfigsPreviewBrowsers(BaseModel):
    pass


class DeploymentConfigsPreviewD1Databases(BaseModel):
    id: Optional[str] = None
    """UUID of the D1 database."""


class DeploymentConfigsPreviewDurableObjectNamespaces(BaseModel):
    namespace_id: Optional[str] = None
    """ID of the Durable Object namespace."""


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


class DeploymentConfigsPreviewHyperdriveBindings(BaseModel):
    id: Optional[str] = None


class DeploymentConfigsPreviewKVNamespaces(BaseModel):
    namespace_id: Optional[str] = None
    """ID of the KV namespace."""


class DeploymentConfigsPreviewLimits(BaseModel):
    cpu_ms: Optional[int] = None
    """CPU time limit in milliseconds."""


class DeploymentConfigsPreviewMTLSCertificates(BaseModel):
    certificate_id: Optional[str] = None


class DeploymentConfigsPreviewPlacement(BaseModel):
    mode: Optional[str] = None
    """Placement mode."""


class DeploymentConfigsPreviewQueueProducers(BaseModel):
    name: Optional[str] = None
    """Name of the Queue."""


class DeploymentConfigsPreviewR2Buckets(BaseModel):
    jurisdiction: Optional[str] = None
    """Jurisdiction of the R2 bucket."""

    name: Optional[str] = None
    """Name of the R2 bucket."""


class DeploymentConfigsPreviewServices(BaseModel):
    entrypoint: Optional[str] = None
    """The entrypoint to bind to."""

    environment: Optional[str] = None
    """The Service environment."""

    service: Optional[str] = None
    """The Service name."""


class DeploymentConfigsPreviewVectorizeBindings(BaseModel):
    index_name: Optional[str] = None


class DeploymentConfigsPreview(BaseModel):
    ai_bindings: Optional[Dict[str, Optional[DeploymentConfigsPreviewAIBindings]]] = None
    """Constellation bindings used for Pages Functions."""

    always_use_latest_compatibility_date: Optional[bool] = None
    """Whether to always use the latest compatibility date for Pages Functions."""

    analytics_engine_datasets: Optional[Dict[str, Optional[DeploymentConfigsPreviewAnalyticsEngineDatasets]]] = None
    """Analytics Engine bindings used for Pages Functions."""

    browsers: Optional[Dict[str, Optional[DeploymentConfigsPreviewBrowsers]]] = None
    """Browser bindings used for Pages Functions."""

    build_image_major_version: Optional[int] = None
    """The major version of the build image to use for Pages Functions."""

    compatibility_date: Optional[str] = None
    """Compatibility date used for Pages Functions."""

    compatibility_flags: Optional[List[str]] = None
    """Compatibility flags used for Pages Functions."""

    d1_databases: Optional[Dict[str, Optional[DeploymentConfigsPreviewD1Databases]]] = None
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[Dict[str, Optional[DeploymentConfigsPreviewDurableObjectNamespaces]]] = None
    """Durable Object namespaces used for Pages Functions."""

    env_vars: Optional[Dict[str, Optional[DeploymentConfigsPreviewEnvVars]]] = None
    """Environment variables used for builds and Pages Functions."""

    fail_open: Optional[bool] = None
    """Whether to fail open when the deployment config cannot be applied."""

    hyperdrive_bindings: Optional[Dict[str, Optional[DeploymentConfigsPreviewHyperdriveBindings]]] = None
    """Hyperdrive bindings used for Pages Functions."""

    kv_namespaces: Optional[Dict[str, Optional[DeploymentConfigsPreviewKVNamespaces]]] = None
    """KV namespaces used for Pages Functions."""

    limits: Optional[DeploymentConfigsPreviewLimits] = None
    """Limits for Pages Functions."""

    mtls_certificates: Optional[Dict[str, Optional[DeploymentConfigsPreviewMTLSCertificates]]] = None
    """mTLS bindings used for Pages Functions."""

    placement: Optional[DeploymentConfigsPreviewPlacement] = None
    """Placement setting used for Pages Functions."""

    queue_producers: Optional[Dict[str, Optional[DeploymentConfigsPreviewQueueProducers]]] = None
    """Queue Producer bindings used for Pages Functions."""

    r2_buckets: Optional[Dict[str, Optional[DeploymentConfigsPreviewR2Buckets]]] = None
    """R2 buckets used for Pages Functions."""

    services: Optional[Dict[str, Optional[DeploymentConfigsPreviewServices]]] = None
    """Services used for Pages Functions."""

    usage_model: Optional[Literal["standard", "bundled", "unbound"]] = None
    """The usage model for Pages Functions."""

    vectorize_bindings: Optional[Dict[str, Optional[DeploymentConfigsPreviewVectorizeBindings]]] = None
    """Vectorize bindings used for Pages Functions."""

    wrangler_config_hash: Optional[str] = None
    """Hash of the Wrangler configuration used for the deployment."""


class DeploymentConfigsProductionAIBindings(BaseModel):
    project_id: Optional[str] = None


class DeploymentConfigsProductionAnalyticsEngineDatasets(BaseModel):
    dataset: Optional[str] = None
    """Name of the dataset."""


class DeploymentConfigsProductionBrowsers(BaseModel):
    pass


class DeploymentConfigsProductionD1Databases(BaseModel):
    id: Optional[str] = None
    """UUID of the D1 database."""


class DeploymentConfigsProductionDurableObjectNamespaces(BaseModel):
    namespace_id: Optional[str] = None
    """ID of the Durable Object namespace."""


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


class DeploymentConfigsProductionHyperdriveBindings(BaseModel):
    id: Optional[str] = None


class DeploymentConfigsProductionKVNamespaces(BaseModel):
    namespace_id: Optional[str] = None
    """ID of the KV namespace."""


class DeploymentConfigsProductionLimits(BaseModel):
    cpu_ms: Optional[int] = None
    """CPU time limit in milliseconds."""


class DeploymentConfigsProductionMTLSCertificates(BaseModel):
    certificate_id: Optional[str] = None


class DeploymentConfigsProductionPlacement(BaseModel):
    mode: Optional[str] = None
    """Placement mode."""


class DeploymentConfigsProductionQueueProducers(BaseModel):
    name: Optional[str] = None
    """Name of the Queue."""


class DeploymentConfigsProductionR2Buckets(BaseModel):
    jurisdiction: Optional[str] = None
    """Jurisdiction of the R2 bucket."""

    name: Optional[str] = None
    """Name of the R2 bucket."""


class DeploymentConfigsProductionServices(BaseModel):
    entrypoint: Optional[str] = None
    """The entrypoint to bind to."""

    environment: Optional[str] = None
    """The Service environment."""

    service: Optional[str] = None
    """The Service name."""


class DeploymentConfigsProductionVectorizeBindings(BaseModel):
    index_name: Optional[str] = None


class DeploymentConfigsProduction(BaseModel):
    ai_bindings: Optional[Dict[str, Optional[DeploymentConfigsProductionAIBindings]]] = None
    """Constellation bindings used for Pages Functions."""

    always_use_latest_compatibility_date: Optional[bool] = None
    """Whether to always use the latest compatibility date for Pages Functions."""

    analytics_engine_datasets: Optional[Dict[str, Optional[DeploymentConfigsProductionAnalyticsEngineDatasets]]] = None
    """Analytics Engine bindings used for Pages Functions."""

    browsers: Optional[Dict[str, Optional[DeploymentConfigsProductionBrowsers]]] = None
    """Browser bindings used for Pages Functions."""

    build_image_major_version: Optional[int] = None
    """The major version of the build image to use for Pages Functions."""

    compatibility_date: Optional[str] = None
    """Compatibility date used for Pages Functions."""

    compatibility_flags: Optional[List[str]] = None
    """Compatibility flags used for Pages Functions."""

    d1_databases: Optional[Dict[str, Optional[DeploymentConfigsProductionD1Databases]]] = None
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[Dict[str, Optional[DeploymentConfigsProductionDurableObjectNamespaces]]] = None
    """Durable Object namespaces used for Pages Functions."""

    env_vars: Optional[Dict[str, Optional[DeploymentConfigsProductionEnvVars]]] = None
    """Environment variables used for builds and Pages Functions."""

    fail_open: Optional[bool] = None
    """Whether to fail open when the deployment config cannot be applied."""

    hyperdrive_bindings: Optional[Dict[str, Optional[DeploymentConfigsProductionHyperdriveBindings]]] = None
    """Hyperdrive bindings used for Pages Functions."""

    kv_namespaces: Optional[Dict[str, Optional[DeploymentConfigsProductionKVNamespaces]]] = None
    """KV namespaces used for Pages Functions."""

    limits: Optional[DeploymentConfigsProductionLimits] = None
    """Limits for Pages Functions."""

    mtls_certificates: Optional[Dict[str, Optional[DeploymentConfigsProductionMTLSCertificates]]] = None
    """mTLS bindings used for Pages Functions."""

    placement: Optional[DeploymentConfigsProductionPlacement] = None
    """Placement setting used for Pages Functions."""

    queue_producers: Optional[Dict[str, Optional[DeploymentConfigsProductionQueueProducers]]] = None
    """Queue Producer bindings used for Pages Functions."""

    r2_buckets: Optional[Dict[str, Optional[DeploymentConfigsProductionR2Buckets]]] = None
    """R2 buckets used for Pages Functions."""

    services: Optional[Dict[str, Optional[DeploymentConfigsProductionServices]]] = None
    """Services used for Pages Functions."""

    usage_model: Optional[Literal["standard", "bundled", "unbound"]] = None
    """The usage model for Pages Functions."""

    vectorize_bindings: Optional[Dict[str, Optional[DeploymentConfigsProductionVectorizeBindings]]] = None
    """Vectorize bindings used for Pages Functions."""

    wrangler_config_hash: Optional[str] = None
    """Hash of the Wrangler configuration used for the deployment."""


class DeploymentConfigs(BaseModel):
    preview: Optional[DeploymentConfigsPreview] = None
    """Configs for preview deploys."""

    production: Optional[DeploymentConfigsProduction] = None
    """Configs for production deploys."""


class SourceConfig(BaseModel):
    deployments_enabled: Optional[bool] = None
    """
    Whether to enable automatic deployments when pushing to the source repository.
    When disabled, no deployments (production or preview) will be triggered
    automatically.
    """

    owner: Optional[str] = None
    """The owner of the repository."""

    path_excludes: Optional[List[str]] = None
    """A list of paths that should be excluded from triggering a preview deployment.

    Wildcard syntax (`*`) is supported.
    """

    path_includes: Optional[List[str]] = None
    """A list of paths that should be watched to trigger a preview deployment.

    Wildcard syntax (`*`) is supported.
    """

    pr_comments_enabled: Optional[bool] = None
    """Whether to enable PR comments."""

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

    production_branch: Optional[str] = None
    """The production branch of the repository."""

    production_deployments_enabled: Optional[bool] = None
    """Whether to trigger a production deployment on commits to the production branch."""

    repo_name: Optional[str] = None
    """The name of the repository."""


class Source(BaseModel):
    config: Optional[SourceConfig] = None

    type: Optional[Literal["github", "gitlab"]] = None
    """The source control management provider."""


class Project(BaseModel):
    id: str
    """ID of the project."""

    name: str
    """Name of the project."""

    production_branch: str
    """Production branch of the project. Used to identify production deployments."""

    build_config: Optional[BuildConfig] = None
    """Configs for the project build process."""

    canonical_deployment: Optional[Deployment] = None
    """Most recent production deployment of the project."""

    created_on: Optional[datetime] = None
    """When the project was created."""

    deployment_configs: Optional[DeploymentConfigs] = None
    """Configs for deployments in a project."""

    domains: Optional[List[str]] = None
    """A list of associated custom domains for the project."""

    framework: Optional[str] = None
    """Framework the project is using."""

    framework_version: Optional[str] = None
    """Version of the framework the project is using."""

    latest_deployment: Optional[Deployment] = None
    """Most recent deployment of the project."""

    preview_script_name: Optional[str] = None
    """Name of the preview script."""

    production_script_name: Optional[str] = None
    """Name of the production script."""

    source: Optional[Source] = None

    subdomain: Optional[str] = None
    """The Cloudflare subdomain associated with the project."""

    uses_functions: Optional[bool] = None
    """Whether the project uses functions."""
