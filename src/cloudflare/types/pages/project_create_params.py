# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "ProjectCreateParams",
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


class ProjectCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    name: Required[str]
    """Name of the project."""

    production_branch: Required[str]
    """Production branch of the project. Used to identify production deployments."""

    build_config: Optional[BuildConfig]
    """Configs for the project build process."""

    deployment_configs: Optional[DeploymentConfigs]
    """Configs for deployments in a project."""

    source: Source


class BuildConfig(TypedDict, total=False):
    build_caching: Optional[bool]
    """Enable build caching for the project."""

    build_command: Optional[str]
    """Command used to build project."""

    destination_dir: Optional[str]
    """Output directory of the build."""

    root_dir: Optional[str]
    """Directory to run the command."""

    web_analytics_tag: Optional[str]
    """The classifying tag for analytics."""

    web_analytics_token: Optional[str]
    """The auth token for analytics."""


class DeploymentConfigsPreviewAIBindings(TypedDict, total=False):
    project_id: str


class DeploymentConfigsPreviewAnalyticsEngineDatasets(TypedDict, total=False):
    dataset: str
    """Name of the dataset."""


class DeploymentConfigsPreviewBrowsers(TypedDict, total=False):
    pass


class DeploymentConfigsPreviewD1Databases(TypedDict, total=False):
    id: str
    """UUID of the D1 database."""


class DeploymentConfigsPreviewDurableObjectNamespaces(TypedDict, total=False):
    namespace_id: str
    """ID of the Durable Object namespace."""


class DeploymentConfigsPreviewEnvVarsPagesPlainTextEnvVar(TypedDict, total=False):
    type: Required[Literal["plain_text"]]

    value: Required[str]
    """Environment variable value."""


class DeploymentConfigsPreviewEnvVarsPagesSecretTextEnvVar(TypedDict, total=False):
    type: Required[Literal["secret_text"]]

    value: Required[str]
    """Secret value."""


DeploymentConfigsPreviewEnvVars: TypeAlias = Union[
    Optional[DeploymentConfigsPreviewEnvVarsPagesPlainTextEnvVar],
    Optional[DeploymentConfigsPreviewEnvVarsPagesSecretTextEnvVar],
]


class DeploymentConfigsPreviewHyperdriveBindings(TypedDict, total=False):
    id: str


class DeploymentConfigsPreviewKVNamespaces(TypedDict, total=False):
    namespace_id: str
    """ID of the KV namespace."""


class DeploymentConfigsPreviewLimits(TypedDict, total=False):
    cpu_ms: int
    """CPU time limit in milliseconds."""


class DeploymentConfigsPreviewMTLSCertificates(TypedDict, total=False):
    certificate_id: str


class DeploymentConfigsPreviewPlacement(TypedDict, total=False):
    mode: str
    """Placement mode."""


class DeploymentConfigsPreviewQueueProducers(TypedDict, total=False):
    name: str
    """Name of the Queue."""


class DeploymentConfigsPreviewR2Buckets(TypedDict, total=False):
    jurisdiction: Optional[str]
    """Jurisdiction of the R2 bucket."""

    name: str
    """Name of the R2 bucket."""


class DeploymentConfigsPreviewServices(TypedDict, total=False):
    entrypoint: Optional[str]
    """The entrypoint to bind to."""

    environment: str
    """The Service environment."""

    service: str
    """The Service name."""


class DeploymentConfigsPreviewVectorizeBindings(TypedDict, total=False):
    index_name: str


class DeploymentConfigsPreview(TypedDict, total=False):
    ai_bindings: Optional[Dict[str, Optional[DeploymentConfigsPreviewAIBindings]]]
    """Constellation bindings used for Pages Functions."""

    always_use_latest_compatibility_date: bool
    """Whether to always use the latest compatibility date for Pages Functions."""

    analytics_engine_datasets: Optional[Dict[str, Optional[DeploymentConfigsPreviewAnalyticsEngineDatasets]]]
    """Analytics Engine bindings used for Pages Functions."""

    browsers: Optional[Dict[str, Optional[DeploymentConfigsPreviewBrowsers]]]
    """Browser bindings used for Pages Functions."""

    build_image_major_version: int
    """The major version of the build image to use for Pages Functions."""

    compatibility_date: str
    """Compatibility date used for Pages Functions."""

    compatibility_flags: Optional[SequenceNotStr[str]]
    """Compatibility flags used for Pages Functions."""

    d1_databases: Optional[Dict[str, Optional[DeploymentConfigsPreviewD1Databases]]]
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[Dict[str, Optional[DeploymentConfigsPreviewDurableObjectNamespaces]]]
    """Durable Object namespaces used for Pages Functions."""

    env_vars: Optional[Dict[str, Optional[DeploymentConfigsPreviewEnvVars]]]
    """Environment variables used for builds and Pages Functions."""

    fail_open: bool
    """Whether to fail open when the deployment config cannot be applied."""

    hyperdrive_bindings: Optional[Dict[str, Optional[DeploymentConfigsPreviewHyperdriveBindings]]]
    """Hyperdrive bindings used for Pages Functions."""

    kv_namespaces: Optional[Dict[str, Optional[DeploymentConfigsPreviewKVNamespaces]]]
    """KV namespaces used for Pages Functions."""

    limits: Optional[DeploymentConfigsPreviewLimits]
    """Limits for Pages Functions."""

    mtls_certificates: Optional[Dict[str, Optional[DeploymentConfigsPreviewMTLSCertificates]]]
    """mTLS bindings used for Pages Functions."""

    placement: Optional[DeploymentConfigsPreviewPlacement]
    """Placement setting used for Pages Functions."""

    queue_producers: Optional[Dict[str, Optional[DeploymentConfigsPreviewQueueProducers]]]
    """Queue Producer bindings used for Pages Functions."""

    r2_buckets: Optional[Dict[str, Optional[DeploymentConfigsPreviewR2Buckets]]]
    """R2 buckets used for Pages Functions."""

    services: Optional[Dict[str, Optional[DeploymentConfigsPreviewServices]]]
    """Services used for Pages Functions."""

    usage_model: Literal["standard", "bundled", "unbound"]
    """The usage model for Pages Functions."""

    vectorize_bindings: Optional[Dict[str, Optional[DeploymentConfigsPreviewVectorizeBindings]]]
    """Vectorize bindings used for Pages Functions."""

    wrangler_config_hash: str
    """Hash of the Wrangler configuration used for the deployment."""


class DeploymentConfigsProductionAIBindings(TypedDict, total=False):
    project_id: str


class DeploymentConfigsProductionAnalyticsEngineDatasets(TypedDict, total=False):
    dataset: str
    """Name of the dataset."""


class DeploymentConfigsProductionBrowsers(TypedDict, total=False):
    pass


class DeploymentConfigsProductionD1Databases(TypedDict, total=False):
    id: str
    """UUID of the D1 database."""


class DeploymentConfigsProductionDurableObjectNamespaces(TypedDict, total=False):
    namespace_id: str
    """ID of the Durable Object namespace."""


class DeploymentConfigsProductionEnvVarsPagesPlainTextEnvVar(TypedDict, total=False):
    type: Required[Literal["plain_text"]]

    value: Required[str]
    """Environment variable value."""


class DeploymentConfigsProductionEnvVarsPagesSecretTextEnvVar(TypedDict, total=False):
    type: Required[Literal["secret_text"]]

    value: Required[str]
    """Secret value."""


DeploymentConfigsProductionEnvVars: TypeAlias = Union[
    Optional[DeploymentConfigsProductionEnvVarsPagesPlainTextEnvVar],
    Optional[DeploymentConfigsProductionEnvVarsPagesSecretTextEnvVar],
]


class DeploymentConfigsProductionHyperdriveBindings(TypedDict, total=False):
    id: str


class DeploymentConfigsProductionKVNamespaces(TypedDict, total=False):
    namespace_id: str
    """ID of the KV namespace."""


class DeploymentConfigsProductionLimits(TypedDict, total=False):
    cpu_ms: int
    """CPU time limit in milliseconds."""


class DeploymentConfigsProductionMTLSCertificates(TypedDict, total=False):
    certificate_id: str


class DeploymentConfigsProductionPlacement(TypedDict, total=False):
    mode: str
    """Placement mode."""


class DeploymentConfigsProductionQueueProducers(TypedDict, total=False):
    name: str
    """Name of the Queue."""


class DeploymentConfigsProductionR2Buckets(TypedDict, total=False):
    jurisdiction: Optional[str]
    """Jurisdiction of the R2 bucket."""

    name: str
    """Name of the R2 bucket."""


class DeploymentConfigsProductionServices(TypedDict, total=False):
    entrypoint: Optional[str]
    """The entrypoint to bind to."""

    environment: str
    """The Service environment."""

    service: str
    """The Service name."""


class DeploymentConfigsProductionVectorizeBindings(TypedDict, total=False):
    index_name: str


class DeploymentConfigsProduction(TypedDict, total=False):
    ai_bindings: Optional[Dict[str, Optional[DeploymentConfigsProductionAIBindings]]]
    """Constellation bindings used for Pages Functions."""

    always_use_latest_compatibility_date: bool
    """Whether to always use the latest compatibility date for Pages Functions."""

    analytics_engine_datasets: Optional[Dict[str, Optional[DeploymentConfigsProductionAnalyticsEngineDatasets]]]
    """Analytics Engine bindings used for Pages Functions."""

    browsers: Optional[Dict[str, Optional[DeploymentConfigsProductionBrowsers]]]
    """Browser bindings used for Pages Functions."""

    build_image_major_version: int
    """The major version of the build image to use for Pages Functions."""

    compatibility_date: str
    """Compatibility date used for Pages Functions."""

    compatibility_flags: Optional[SequenceNotStr[str]]
    """Compatibility flags used for Pages Functions."""

    d1_databases: Optional[Dict[str, Optional[DeploymentConfigsProductionD1Databases]]]
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[Dict[str, Optional[DeploymentConfigsProductionDurableObjectNamespaces]]]
    """Durable Object namespaces used for Pages Functions."""

    env_vars: Optional[Dict[str, Optional[DeploymentConfigsProductionEnvVars]]]
    """Environment variables used for builds and Pages Functions."""

    fail_open: bool
    """Whether to fail open when the deployment config cannot be applied."""

    hyperdrive_bindings: Optional[Dict[str, Optional[DeploymentConfigsProductionHyperdriveBindings]]]
    """Hyperdrive bindings used for Pages Functions."""

    kv_namespaces: Optional[Dict[str, Optional[DeploymentConfigsProductionKVNamespaces]]]
    """KV namespaces used for Pages Functions."""

    limits: Optional[DeploymentConfigsProductionLimits]
    """Limits for Pages Functions."""

    mtls_certificates: Optional[Dict[str, Optional[DeploymentConfigsProductionMTLSCertificates]]]
    """mTLS bindings used for Pages Functions."""

    placement: Optional[DeploymentConfigsProductionPlacement]
    """Placement setting used for Pages Functions."""

    queue_producers: Optional[Dict[str, Optional[DeploymentConfigsProductionQueueProducers]]]
    """Queue Producer bindings used for Pages Functions."""

    r2_buckets: Optional[Dict[str, Optional[DeploymentConfigsProductionR2Buckets]]]
    """R2 buckets used for Pages Functions."""

    services: Optional[Dict[str, Optional[DeploymentConfigsProductionServices]]]
    """Services used for Pages Functions."""

    usage_model: Literal["standard", "bundled", "unbound"]
    """The usage model for Pages Functions."""

    vectorize_bindings: Optional[Dict[str, Optional[DeploymentConfigsProductionVectorizeBindings]]]
    """Vectorize bindings used for Pages Functions."""

    wrangler_config_hash: str
    """Hash of the Wrangler configuration used for the deployment."""


class DeploymentConfigs(TypedDict, total=False):
    preview: Optional[DeploymentConfigsPreview]
    """Configs for preview deploys."""

    production: Optional[DeploymentConfigsProduction]
    """Configs for production deploys."""


class SourceConfig(TypedDict, total=False):
    deployments_enabled: bool
    """
    Whether to enable automatic deployments when pushing to the source repository.
    When disabled, no deployments (production or preview) will be triggered
    automatically.
    """

    owner: str
    """The owner of the repository."""

    path_excludes: SequenceNotStr[str]
    """A list of paths that should be excluded from triggering a preview deployment.

    Wildcard syntax (`*`) is supported.
    """

    path_includes: SequenceNotStr[str]
    """A list of paths that should be watched to trigger a preview deployment.

    Wildcard syntax (`*`) is supported.
    """

    pr_comments_enabled: bool
    """Whether to enable PR comments."""

    preview_branch_excludes: SequenceNotStr[str]
    """A list of branches that should not trigger a preview deployment.

    Wildcard syntax (`*`) is supported. Must be used with
    `preview_deployment_setting` set to `custom`.
    """

    preview_branch_includes: SequenceNotStr[str]
    """A list of branches that should trigger a preview deployment.

    Wildcard syntax (`*`) is supported. Must be used with
    `preview_deployment_setting` set to `custom`.
    """

    preview_deployment_setting: Literal["all", "none", "custom"]
    """Controls whether commits to preview branches trigger a preview deployment."""

    production_branch: str
    """The production branch of the repository."""

    production_deployments_enabled: bool
    """Whether to trigger a production deployment on commits to the production branch."""

    repo_name: str
    """The name of the repository."""


class Source(TypedDict, total=False):
    config: SourceConfig

    type: Literal["github", "gitlab"]
    """The source control management provider."""
