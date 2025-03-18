# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

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
    "DeploymentConfigsProductionMTLSCertificates",
    "DeploymentConfigsProductionPlacement",
    "DeploymentConfigsProductionQueueProducers",
    "DeploymentConfigsProductionR2Buckets",
    "DeploymentConfigsProductionServices",
    "DeploymentConfigsProductionVectorizeBindings",
]


class ProjectCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    build_config: BuildConfig
    """Configs for the project build process."""

    deployment_configs: DeploymentConfigs
    """Configs for deployments in a project."""

    name: str
    """Name of the project."""

    production_branch: str
    """Production branch of the project. Used to identify production deployments."""


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

    analytics_engine_datasets: Optional[Dict[str, Optional[DeploymentConfigsPreviewAnalyticsEngineDatasets]]]
    """Analytics Engine bindings used for Pages Functions."""

    browsers: Optional[Dict[str, Optional[DeploymentConfigsPreviewBrowsers]]]
    """Browser bindings used for Pages Functions."""

    compatibility_date: str
    """Compatibility date used for Pages Functions."""

    compatibility_flags: List[str]
    """Compatibility flags used for Pages Functions."""

    d1_databases: Optional[Dict[str, Optional[DeploymentConfigsPreviewD1Databases]]]
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[Dict[str, Optional[DeploymentConfigsPreviewDurableObjectNamespaces]]]
    """Durable Object namespaces used for Pages Functions."""

    env_vars: Dict[str, DeploymentConfigsPreviewEnvVars]
    """Environment variables used for builds and Pages Functions."""

    hyperdrive_bindings: Optional[Dict[str, Optional[DeploymentConfigsPreviewHyperdriveBindings]]]
    """Hyperdrive bindings used for Pages Functions."""

    kv_namespaces: Optional[Dict[str, Optional[DeploymentConfigsPreviewKVNamespaces]]]
    """KV namespaces used for Pages Functions."""

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

    vectorize_bindings: Optional[Dict[str, Optional[DeploymentConfigsPreviewVectorizeBindings]]]
    """Vectorize bindings used for Pages Functions."""


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

    analytics_engine_datasets: Optional[Dict[str, Optional[DeploymentConfigsProductionAnalyticsEngineDatasets]]]
    """Analytics Engine bindings used for Pages Functions."""

    browsers: Optional[Dict[str, Optional[DeploymentConfigsProductionBrowsers]]]
    """Browser bindings used for Pages Functions."""

    compatibility_date: str
    """Compatibility date used for Pages Functions."""

    compatibility_flags: List[str]
    """Compatibility flags used for Pages Functions."""

    d1_databases: Optional[Dict[str, Optional[DeploymentConfigsProductionD1Databases]]]
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[Dict[str, Optional[DeploymentConfigsProductionDurableObjectNamespaces]]]
    """Durable Object namespaces used for Pages Functions."""

    env_vars: Dict[str, DeploymentConfigsProductionEnvVars]
    """Environment variables used for builds and Pages Functions."""

    hyperdrive_bindings: Optional[Dict[str, Optional[DeploymentConfigsProductionHyperdriveBindings]]]
    """Hyperdrive bindings used for Pages Functions."""

    kv_namespaces: Optional[Dict[str, Optional[DeploymentConfigsProductionKVNamespaces]]]
    """KV namespaces used for Pages Functions."""

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

    vectorize_bindings: Optional[Dict[str, Optional[DeploymentConfigsProductionVectorizeBindings]]]
    """Vectorize bindings used for Pages Functions."""


class DeploymentConfigs(TypedDict, total=False):
    preview: DeploymentConfigsPreview
    """Configs for preview deploys."""

    production: DeploymentConfigsProduction
    """Configs for production deploys."""
