# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .deployment import Deployment

__all__ = [
    "Project",
    "BuildConfig",
    "DeploymentConfigs",
    "DeploymentConfigsPreview",
    "DeploymentConfigsPreviewAIBindings",
    "DeploymentConfigsPreviewAIBindingsAIBinding",
    "DeploymentConfigsPreviewAnalyticsEngineDatasets",
    "DeploymentConfigsPreviewAnalyticsEngineDatasetsAnalyticsEngineBinding",
    "DeploymentConfigsPreviewBrowsers",
    "DeploymentConfigsPreviewD1Databases",
    "DeploymentConfigsPreviewD1DatabasesD1Binding",
    "DeploymentConfigsPreviewDurableObjectNamespaces",
    "DeploymentConfigsPreviewDurableObjectNamespacesDoBinding",
    "DeploymentConfigsPreviewEnvVars",
    "DeploymentConfigsPreviewEnvVarsEnvironmentVariable",
    "DeploymentConfigsPreviewHyperdriveBindings",
    "DeploymentConfigsPreviewHyperdriveBindingsHyperdrive",
    "DeploymentConfigsPreviewKVNamespaces",
    "DeploymentConfigsPreviewKVNamespacesKVBinding",
    "DeploymentConfigsPreviewMTLSCertificates",
    "DeploymentConfigsPreviewMTLSCertificatesMTLS",
    "DeploymentConfigsPreviewPlacement",
    "DeploymentConfigsPreviewQueueProducers",
    "DeploymentConfigsPreviewQueueProducersQueueProducerBinding",
    "DeploymentConfigsPreviewR2Buckets",
    "DeploymentConfigsPreviewR2BucketsR2Binding",
    "DeploymentConfigsPreviewServices",
    "DeploymentConfigsPreviewServicesServiceBinding",
    "DeploymentConfigsPreviewVectorizeBindings",
    "DeploymentConfigsPreviewVectorizeBindingsVectorize",
    "DeploymentConfigsProduction",
    "DeploymentConfigsProductionAIBindings",
    "DeploymentConfigsProductionAIBindingsAIBinding",
    "DeploymentConfigsProductionAnalyticsEngineDatasets",
    "DeploymentConfigsProductionAnalyticsEngineDatasetsAnalyticsEngineBinding",
    "DeploymentConfigsProductionBrowsers",
    "DeploymentConfigsProductionD1Databases",
    "DeploymentConfigsProductionD1DatabasesD1Binding",
    "DeploymentConfigsProductionDurableObjectNamespaces",
    "DeploymentConfigsProductionDurableObjectNamespacesDoBinding",
    "DeploymentConfigsProductionEnvVars",
    "DeploymentConfigsProductionEnvVarsEnvironmentVariable",
    "DeploymentConfigsProductionHyperdriveBindings",
    "DeploymentConfigsProductionHyperdriveBindingsHyperdrive",
    "DeploymentConfigsProductionKVNamespaces",
    "DeploymentConfigsProductionKVNamespacesKVBinding",
    "DeploymentConfigsProductionMTLSCertificates",
    "DeploymentConfigsProductionMTLSCertificatesMTLS",
    "DeploymentConfigsProductionPlacement",
    "DeploymentConfigsProductionQueueProducers",
    "DeploymentConfigsProductionQueueProducersQueueProducerBinding",
    "DeploymentConfigsProductionR2Buckets",
    "DeploymentConfigsProductionR2BucketsR2Binding",
    "DeploymentConfigsProductionServices",
    "DeploymentConfigsProductionServicesServiceBinding",
    "DeploymentConfigsProductionVectorizeBindings",
    "DeploymentConfigsProductionVectorizeBindingsVectorize",
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


class DeploymentConfigsPreviewAIBindingsAIBinding(BaseModel):
    project_id: Optional[object] = None


class DeploymentConfigsPreviewAIBindings(BaseModel):
    ai_binding: Optional[DeploymentConfigsPreviewAIBindingsAIBinding] = FieldInfo(alias="AI_BINDING", default=None)
    """AI binding."""


class DeploymentConfigsPreviewAnalyticsEngineDatasetsAnalyticsEngineBinding(BaseModel):
    dataset: Optional[str] = None
    """Name of the dataset."""


class DeploymentConfigsPreviewAnalyticsEngineDatasets(BaseModel):
    analytics_engine_binding: Optional[DeploymentConfigsPreviewAnalyticsEngineDatasetsAnalyticsEngineBinding] = (
        FieldInfo(alias="ANALYTICS_ENGINE_BINDING", default=None)
    )
    """Analytics Engine binding."""


class DeploymentConfigsPreviewBrowsers(BaseModel):
    browser: Optional[object] = FieldInfo(alias="BROWSER", default=None)
    """Browser binding."""


class DeploymentConfigsPreviewD1DatabasesD1Binding(BaseModel):
    id: Optional[str] = None
    """UUID of the D1 database."""


class DeploymentConfigsPreviewD1Databases(BaseModel):
    d1_binding: Optional[DeploymentConfigsPreviewD1DatabasesD1Binding] = FieldInfo(alias="D1_BINDING", default=None)
    """D1 binding."""


class DeploymentConfigsPreviewDurableObjectNamespacesDoBinding(BaseModel):
    namespace_id: Optional[str] = None
    """ID of the Durabble Object namespace."""


class DeploymentConfigsPreviewDurableObjectNamespaces(BaseModel):
    do_binding: Optional[DeploymentConfigsPreviewDurableObjectNamespacesDoBinding] = FieldInfo(
        alias="DO_BINDING", default=None
    )
    """Durabble Object binding."""


class DeploymentConfigsPreviewEnvVarsEnvironmentVariable(BaseModel):
    type: Optional[Literal["plain_text", "secret_text"]] = None
    """The type of environment variable (plain text or secret)"""

    value: Optional[str] = None
    """Environment variable value."""


class DeploymentConfigsPreviewEnvVars(BaseModel):
    environment_variable: Optional[DeploymentConfigsPreviewEnvVarsEnvironmentVariable] = FieldInfo(
        alias="ENVIRONMENT_VARIABLE", default=None
    )
    """Environment variable."""


class DeploymentConfigsPreviewHyperdriveBindingsHyperdrive(BaseModel):
    id: Optional[str] = None


class DeploymentConfigsPreviewHyperdriveBindings(BaseModel):
    hyperdrive: Optional[DeploymentConfigsPreviewHyperdriveBindingsHyperdrive] = FieldInfo(
        alias="HYPERDRIVE", default=None
    )
    """Hyperdrive binding."""


class DeploymentConfigsPreviewKVNamespacesKVBinding(BaseModel):
    namespace_id: Optional[str] = None
    """ID of the KV namespace."""


class DeploymentConfigsPreviewKVNamespaces(BaseModel):
    kv_binding: Optional[DeploymentConfigsPreviewKVNamespacesKVBinding] = FieldInfo(alias="KV_BINDING", default=None)
    """KV binding."""


class DeploymentConfigsPreviewMTLSCertificatesMTLS(BaseModel):
    certificate_id: Optional[str] = None


class DeploymentConfigsPreviewMTLSCertificates(BaseModel):
    mtls: Optional[DeploymentConfigsPreviewMTLSCertificatesMTLS] = FieldInfo(alias="MTLS", default=None)
    """mTLS binding."""


class DeploymentConfigsPreviewPlacement(BaseModel):
    mode: Optional[str] = None
    """Placement mode."""


class DeploymentConfigsPreviewQueueProducersQueueProducerBinding(BaseModel):
    name: Optional[str] = None
    """Name of the Queue."""


class DeploymentConfigsPreviewQueueProducers(BaseModel):
    queue_producer_binding: Optional[DeploymentConfigsPreviewQueueProducersQueueProducerBinding] = FieldInfo(
        alias="QUEUE_PRODUCER_BINDING", default=None
    )
    """Queue Producer binding."""


class DeploymentConfigsPreviewR2BucketsR2Binding(BaseModel):
    jurisdiction: Optional[str] = None
    """Jurisdiction of the R2 bucket."""

    name: Optional[str] = None
    """Name of the R2 bucket."""


class DeploymentConfigsPreviewR2Buckets(BaseModel):
    r2_binding: Optional[DeploymentConfigsPreviewR2BucketsR2Binding] = FieldInfo(alias="R2_BINDING", default=None)
    """R2 binding."""


class DeploymentConfigsPreviewServicesServiceBinding(BaseModel):
    entrypoint: Optional[str] = None
    """The entrypoint to bind to."""

    environment: Optional[str] = None
    """The Service environment."""

    service: Optional[str] = None
    """The Service name."""


class DeploymentConfigsPreviewServices(BaseModel):
    service_binding: Optional[DeploymentConfigsPreviewServicesServiceBinding] = FieldInfo(
        alias="SERVICE_BINDING", default=None
    )
    """Service binding."""


class DeploymentConfigsPreviewVectorizeBindingsVectorize(BaseModel):
    index_name: Optional[str] = None


class DeploymentConfigsPreviewVectorizeBindings(BaseModel):
    vectorize: Optional[DeploymentConfigsPreviewVectorizeBindingsVectorize] = FieldInfo(alias="VECTORIZE", default=None)
    """Vectorize binding."""


class DeploymentConfigsPreview(BaseModel):
    ai_bindings: Optional[DeploymentConfigsPreviewAIBindings] = None
    """Constellation bindings used for Pages Functions."""

    analytics_engine_datasets: Optional[DeploymentConfigsPreviewAnalyticsEngineDatasets] = None
    """Analytics Engine bindings used for Pages Functions."""

    browsers: Optional[DeploymentConfigsPreviewBrowsers] = None
    """Browser bindings used for Pages Functions."""

    compatibility_date: Optional[str] = None
    """Compatibility date used for Pages Functions."""

    compatibility_flags: Optional[List[object]] = None
    """Compatibility flags used for Pages Functions."""

    d1_databases: Optional[DeploymentConfigsPreviewD1Databases] = None
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[DeploymentConfigsPreviewDurableObjectNamespaces] = None
    """Durabble Object namespaces used for Pages Functions."""

    env_vars: Optional[DeploymentConfigsPreviewEnvVars] = None
    """Environment variables for build configs."""

    hyperdrive_bindings: Optional[DeploymentConfigsPreviewHyperdriveBindings] = None
    """Hyperdrive bindings used for Pages Functions."""

    kv_namespaces: Optional[DeploymentConfigsPreviewKVNamespaces] = None
    """KV namespaces used for Pages Functions."""

    mtls_certificates: Optional[DeploymentConfigsPreviewMTLSCertificates] = None
    """mTLS bindings used for Pages Functions."""

    placement: Optional[DeploymentConfigsPreviewPlacement] = None
    """Placement setting used for Pages Functions."""

    queue_producers: Optional[DeploymentConfigsPreviewQueueProducers] = None
    """Queue Producer bindings used for Pages Functions."""

    r2_buckets: Optional[DeploymentConfigsPreviewR2Buckets] = None
    """R2 buckets used for Pages Functions."""

    services: Optional[DeploymentConfigsPreviewServices] = None
    """Services used for Pages Functions."""

    vectorize_bindings: Optional[DeploymentConfigsPreviewVectorizeBindings] = None
    """Vectorize bindings used for Pages Functions."""


class DeploymentConfigsProductionAIBindingsAIBinding(BaseModel):
    project_id: Optional[object] = None


class DeploymentConfigsProductionAIBindings(BaseModel):
    ai_binding: Optional[DeploymentConfigsProductionAIBindingsAIBinding] = FieldInfo(alias="AI_BINDING", default=None)
    """AI binding."""


class DeploymentConfigsProductionAnalyticsEngineDatasetsAnalyticsEngineBinding(BaseModel):
    dataset: Optional[str] = None
    """Name of the dataset."""


class DeploymentConfigsProductionAnalyticsEngineDatasets(BaseModel):
    analytics_engine_binding: Optional[DeploymentConfigsProductionAnalyticsEngineDatasetsAnalyticsEngineBinding] = (
        FieldInfo(alias="ANALYTICS_ENGINE_BINDING", default=None)
    )
    """Analytics Engine binding."""


class DeploymentConfigsProductionBrowsers(BaseModel):
    browser: Optional[object] = FieldInfo(alias="BROWSER", default=None)
    """Browser binding."""


class DeploymentConfigsProductionD1DatabasesD1Binding(BaseModel):
    id: Optional[str] = None
    """UUID of the D1 database."""


class DeploymentConfigsProductionD1Databases(BaseModel):
    d1_binding: Optional[DeploymentConfigsProductionD1DatabasesD1Binding] = FieldInfo(alias="D1_BINDING", default=None)
    """D1 binding."""


class DeploymentConfigsProductionDurableObjectNamespacesDoBinding(BaseModel):
    namespace_id: Optional[str] = None
    """ID of the Durabble Object namespace."""


class DeploymentConfigsProductionDurableObjectNamespaces(BaseModel):
    do_binding: Optional[DeploymentConfigsProductionDurableObjectNamespacesDoBinding] = FieldInfo(
        alias="DO_BINDING", default=None
    )
    """Durabble Object binding."""


class DeploymentConfigsProductionEnvVarsEnvironmentVariable(BaseModel):
    type: Optional[Literal["plain_text", "secret_text"]] = None
    """The type of environment variable (plain text or secret)"""

    value: Optional[str] = None
    """Environment variable value."""


class DeploymentConfigsProductionEnvVars(BaseModel):
    environment_variable: Optional[DeploymentConfigsProductionEnvVarsEnvironmentVariable] = FieldInfo(
        alias="ENVIRONMENT_VARIABLE", default=None
    )
    """Environment variable."""


class DeploymentConfigsProductionHyperdriveBindingsHyperdrive(BaseModel):
    id: Optional[str] = None


class DeploymentConfigsProductionHyperdriveBindings(BaseModel):
    hyperdrive: Optional[DeploymentConfigsProductionHyperdriveBindingsHyperdrive] = FieldInfo(
        alias="HYPERDRIVE", default=None
    )
    """Hyperdrive binding."""


class DeploymentConfigsProductionKVNamespacesKVBinding(BaseModel):
    namespace_id: Optional[str] = None
    """ID of the KV namespace."""


class DeploymentConfigsProductionKVNamespaces(BaseModel):
    kv_binding: Optional[DeploymentConfigsProductionKVNamespacesKVBinding] = FieldInfo(alias="KV_BINDING", default=None)
    """KV binding."""


class DeploymentConfigsProductionMTLSCertificatesMTLS(BaseModel):
    certificate_id: Optional[str] = None


class DeploymentConfigsProductionMTLSCertificates(BaseModel):
    mtls: Optional[DeploymentConfigsProductionMTLSCertificatesMTLS] = FieldInfo(alias="MTLS", default=None)
    """mTLS binding."""


class DeploymentConfigsProductionPlacement(BaseModel):
    mode: Optional[str] = None
    """Placement mode."""


class DeploymentConfigsProductionQueueProducersQueueProducerBinding(BaseModel):
    name: Optional[str] = None
    """Name of the Queue."""


class DeploymentConfigsProductionQueueProducers(BaseModel):
    queue_producer_binding: Optional[DeploymentConfigsProductionQueueProducersQueueProducerBinding] = FieldInfo(
        alias="QUEUE_PRODUCER_BINDING", default=None
    )
    """Queue Producer binding."""


class DeploymentConfigsProductionR2BucketsR2Binding(BaseModel):
    jurisdiction: Optional[str] = None
    """Jurisdiction of the R2 bucket."""

    name: Optional[str] = None
    """Name of the R2 bucket."""


class DeploymentConfigsProductionR2Buckets(BaseModel):
    r2_binding: Optional[DeploymentConfigsProductionR2BucketsR2Binding] = FieldInfo(alias="R2_BINDING", default=None)
    """R2 binding."""


class DeploymentConfigsProductionServicesServiceBinding(BaseModel):
    entrypoint: Optional[str] = None
    """The entrypoint to bind to."""

    environment: Optional[str] = None
    """The Service environment."""

    service: Optional[str] = None
    """The Service name."""


class DeploymentConfigsProductionServices(BaseModel):
    service_binding: Optional[DeploymentConfigsProductionServicesServiceBinding] = FieldInfo(
        alias="SERVICE_BINDING", default=None
    )
    """Service binding."""


class DeploymentConfigsProductionVectorizeBindingsVectorize(BaseModel):
    index_name: Optional[str] = None


class DeploymentConfigsProductionVectorizeBindings(BaseModel):
    vectorize: Optional[DeploymentConfigsProductionVectorizeBindingsVectorize] = FieldInfo(
        alias="VECTORIZE", default=None
    )
    """Vectorize binding."""


class DeploymentConfigsProduction(BaseModel):
    ai_bindings: Optional[DeploymentConfigsProductionAIBindings] = None
    """Constellation bindings used for Pages Functions."""

    analytics_engine_datasets: Optional[DeploymentConfigsProductionAnalyticsEngineDatasets] = None
    """Analytics Engine bindings used for Pages Functions."""

    browsers: Optional[DeploymentConfigsProductionBrowsers] = None
    """Browser bindings used for Pages Functions."""

    compatibility_date: Optional[str] = None
    """Compatibility date used for Pages Functions."""

    compatibility_flags: Optional[List[object]] = None
    """Compatibility flags used for Pages Functions."""

    d1_databases: Optional[DeploymentConfigsProductionD1Databases] = None
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[DeploymentConfigsProductionDurableObjectNamespaces] = None
    """Durabble Object namespaces used for Pages Functions."""

    env_vars: Optional[DeploymentConfigsProductionEnvVars] = None
    """Environment variables for build configs."""

    hyperdrive_bindings: Optional[DeploymentConfigsProductionHyperdriveBindings] = None
    """Hyperdrive bindings used for Pages Functions."""

    kv_namespaces: Optional[DeploymentConfigsProductionKVNamespaces] = None
    """KV namespaces used for Pages Functions."""

    mtls_certificates: Optional[DeploymentConfigsProductionMTLSCertificates] = None
    """mTLS bindings used for Pages Functions."""

    placement: Optional[DeploymentConfigsProductionPlacement] = None
    """Placement setting used for Pages Functions."""

    queue_producers: Optional[DeploymentConfigsProductionQueueProducers] = None
    """Queue Producer bindings used for Pages Functions."""

    r2_buckets: Optional[DeploymentConfigsProductionR2Buckets] = None
    """R2 buckets used for Pages Functions."""

    services: Optional[DeploymentConfigsProductionServices] = None
    """Services used for Pages Functions."""

    vectorize_bindings: Optional[DeploymentConfigsProductionVectorizeBindings] = None
    """Vectorize bindings used for Pages Functions."""


class DeploymentConfigs(BaseModel):
    preview: Optional[DeploymentConfigsPreview] = None
    """Configs for preview deploys."""

    production: Optional[DeploymentConfigsProduction] = None
    """Configs for production deploys."""


class Project(BaseModel):
    id: Optional[str] = None
    """Id of the project."""

    build_config: Optional[BuildConfig] = None
    """Configs for the project build process."""

    canonical_deployment: Optional[Deployment] = None

    created_on: Optional[datetime] = None
    """When the project was created."""

    deployment_configs: Optional[DeploymentConfigs] = None
    """Configs for deployments in a project."""

    domains: Optional[List[object]] = None
    """A list of associated custom domains for the project."""

    latest_deployment: Optional[Deployment] = None

    name: Optional[str] = None
    """Name of the project."""

    production_branch: Optional[str] = None
    """Production branch of the project. Used to identify production deployments."""

    source: Optional[object] = None

    subdomain: Optional[str] = None
    """The Cloudflare subdomain associated with the project."""
