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
    ],
    PropertyInfo(discriminator="type"),
]


class DeploymentConfigsPreviewHyperdriveBindings(BaseModel):
    id: Optional[str] = None


class DeploymentConfigsPreviewKVNamespaces(BaseModel):
    namespace_id: Optional[str] = None
    """ID of the KV namespace."""


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

    analytics_engine_datasets: Optional[Dict[str, Optional[DeploymentConfigsPreviewAnalyticsEngineDatasets]]] = None
    """Analytics Engine bindings used for Pages Functions."""

    browsers: Optional[Dict[str, Optional[DeploymentConfigsPreviewBrowsers]]] = None
    """Browser bindings used for Pages Functions."""

    compatibility_date: Optional[str] = None
    """Compatibility date used for Pages Functions."""

    compatibility_flags: Optional[List[str]] = None
    """Compatibility flags used for Pages Functions."""

    d1_databases: Optional[Dict[str, Optional[DeploymentConfigsPreviewD1Databases]]] = None
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[Dict[str, Optional[DeploymentConfigsPreviewDurableObjectNamespaces]]] = None
    """Durable Object namespaces used for Pages Functions."""

    env_vars: Optional[Dict[str, DeploymentConfigsPreviewEnvVars]] = None
    """Environment variables used for builds and Pages Functions."""

    hyperdrive_bindings: Optional[Dict[str, Optional[DeploymentConfigsPreviewHyperdriveBindings]]] = None
    """Hyperdrive bindings used for Pages Functions."""

    kv_namespaces: Optional[Dict[str, Optional[DeploymentConfigsPreviewKVNamespaces]]] = None
    """KV namespaces used for Pages Functions."""

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

    vectorize_bindings: Optional[Dict[str, Optional[DeploymentConfigsPreviewVectorizeBindings]]] = None
    """Vectorize bindings used for Pages Functions."""


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
    ],
    PropertyInfo(discriminator="type"),
]


class DeploymentConfigsProductionHyperdriveBindings(BaseModel):
    id: Optional[str] = None


class DeploymentConfigsProductionKVNamespaces(BaseModel):
    namespace_id: Optional[str] = None
    """ID of the KV namespace."""


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

    analytics_engine_datasets: Optional[Dict[str, Optional[DeploymentConfigsProductionAnalyticsEngineDatasets]]] = None
    """Analytics Engine bindings used for Pages Functions."""

    browsers: Optional[Dict[str, Optional[DeploymentConfigsProductionBrowsers]]] = None
    """Browser bindings used for Pages Functions."""

    compatibility_date: Optional[str] = None
    """Compatibility date used for Pages Functions."""

    compatibility_flags: Optional[List[str]] = None
    """Compatibility flags used for Pages Functions."""

    d1_databases: Optional[Dict[str, Optional[DeploymentConfigsProductionD1Databases]]] = None
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[Dict[str, Optional[DeploymentConfigsProductionDurableObjectNamespaces]]] = None
    """Durable Object namespaces used for Pages Functions."""

    env_vars: Optional[Dict[str, DeploymentConfigsProductionEnvVars]] = None
    """Environment variables used for builds and Pages Functions."""

    hyperdrive_bindings: Optional[Dict[str, Optional[DeploymentConfigsProductionHyperdriveBindings]]] = None
    """Hyperdrive bindings used for Pages Functions."""

    kv_namespaces: Optional[Dict[str, Optional[DeploymentConfigsProductionKVNamespaces]]] = None
    """KV namespaces used for Pages Functions."""

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

    vectorize_bindings: Optional[Dict[str, Optional[DeploymentConfigsProductionVectorizeBindings]]] = None
    """Vectorize bindings used for Pages Functions."""


class DeploymentConfigs(BaseModel):
    preview: Optional[DeploymentConfigsPreview] = None
    """Configs for preview deploys."""

    production: Optional[DeploymentConfigsProduction] = None
    """Configs for production deploys."""


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


class Project(BaseModel):
    id: Optional[str] = None
    """Id of the project."""

    build_config: Optional[BuildConfig] = None
    """Configs for the project build process."""

    canonical_deployment: Optional[Deployment] = None
    """Most recent deployment to the repo."""

    created_on: Optional[datetime] = None
    """When the project was created."""

    deployment_configs: Optional[DeploymentConfigs] = None
    """Configs for deployments in a project."""

    domains: Optional[List[str]] = None
    """A list of associated custom domains for the project."""

    latest_deployment: Optional[Deployment] = None
    """Most recent deployment to the repo."""

    name: Optional[str] = None
    """Name of the project."""

    production_branch: Optional[str] = None
    """Production branch of the project. Used to identify production deployments."""

    source: Optional[Source] = None

    subdomain: Optional[str] = None
    """The Cloudflare subdomain associated with the project."""
