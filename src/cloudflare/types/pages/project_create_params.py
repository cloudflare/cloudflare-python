# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ProjectCreateParams",
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


class DeploymentConfigsPreviewAIBindingsAIBinding(TypedDict, total=False):
    project_id: str


class DeploymentConfigsPreviewAIBindings(TypedDict, total=False):
    ai_binding: Annotated[DeploymentConfigsPreviewAIBindingsAIBinding, PropertyInfo(alias="AI_BINDING")]
    """AI binding."""


class DeploymentConfigsPreviewAnalyticsEngineDatasetsAnalyticsEngineBinding(TypedDict, total=False):
    dataset: str
    """Name of the dataset."""


class DeploymentConfigsPreviewAnalyticsEngineDatasets(TypedDict, total=False):
    analytics_engine_binding: Annotated[
        DeploymentConfigsPreviewAnalyticsEngineDatasetsAnalyticsEngineBinding,
        PropertyInfo(alias="ANALYTICS_ENGINE_BINDING"),
    ]
    """Analytics Engine binding."""


class DeploymentConfigsPreviewBrowsers(TypedDict, total=False):
    browser: Annotated[object, PropertyInfo(alias="BROWSER")]
    """Browser binding."""


class DeploymentConfigsPreviewD1DatabasesD1Binding(TypedDict, total=False):
    id: str
    """UUID of the D1 database."""


class DeploymentConfigsPreviewD1Databases(TypedDict, total=False):
    d1_binding: Annotated[DeploymentConfigsPreviewD1DatabasesD1Binding, PropertyInfo(alias="D1_BINDING")]
    """D1 binding."""


class DeploymentConfigsPreviewDurableObjectNamespacesDoBinding(TypedDict, total=False):
    namespace_id: str
    """ID of the Durabble Object namespace."""


class DeploymentConfigsPreviewDurableObjectNamespaces(TypedDict, total=False):
    do_binding: Annotated[DeploymentConfigsPreviewDurableObjectNamespacesDoBinding, PropertyInfo(alias="DO_BINDING")]
    """Durabble Object binding."""


class DeploymentConfigsPreviewEnvVarsEnvironmentVariable(TypedDict, total=False):
    type: Literal["plain_text", "secret_text"]
    """The type of environment variable (plain text or secret)"""

    value: str
    """Environment variable value."""


class DeploymentConfigsPreviewEnvVars(TypedDict, total=False):
    environment_variable: Annotated[
        DeploymentConfigsPreviewEnvVarsEnvironmentVariable, PropertyInfo(alias="ENVIRONMENT_VARIABLE")
    ]
    """Environment variable."""


class DeploymentConfigsPreviewHyperdriveBindingsHyperdrive(TypedDict, total=False):
    id: str


class DeploymentConfigsPreviewHyperdriveBindings(TypedDict, total=False):
    hyperdrive: Annotated[DeploymentConfigsPreviewHyperdriveBindingsHyperdrive, PropertyInfo(alias="HYPERDRIVE")]
    """Hyperdrive binding."""


class DeploymentConfigsPreviewKVNamespacesKVBinding(TypedDict, total=False):
    namespace_id: str
    """ID of the KV namespace."""


class DeploymentConfigsPreviewKVNamespaces(TypedDict, total=False):
    kv_binding: Annotated[DeploymentConfigsPreviewKVNamespacesKVBinding, PropertyInfo(alias="KV_BINDING")]
    """KV binding."""


class DeploymentConfigsPreviewMTLSCertificatesMTLS(TypedDict, total=False):
    certificate_id: str


class DeploymentConfigsPreviewMTLSCertificates(TypedDict, total=False):
    mtls: Annotated[DeploymentConfigsPreviewMTLSCertificatesMTLS, PropertyInfo(alias="MTLS")]
    """mTLS binding."""


class DeploymentConfigsPreviewPlacement(TypedDict, total=False):
    mode: str
    """Placement mode."""


class DeploymentConfigsPreviewQueueProducersQueueProducerBinding(TypedDict, total=False):
    name: str
    """Name of the Queue."""


class DeploymentConfigsPreviewQueueProducers(TypedDict, total=False):
    queue_producer_binding: Annotated[
        DeploymentConfigsPreviewQueueProducersQueueProducerBinding, PropertyInfo(alias="QUEUE_PRODUCER_BINDING")
    ]
    """Queue Producer binding."""


class DeploymentConfigsPreviewR2BucketsR2Binding(TypedDict, total=False):
    jurisdiction: Optional[str]
    """Jurisdiction of the R2 bucket."""

    name: str
    """Name of the R2 bucket."""


class DeploymentConfigsPreviewR2Buckets(TypedDict, total=False):
    r2_binding: Annotated[DeploymentConfigsPreviewR2BucketsR2Binding, PropertyInfo(alias="R2_BINDING")]
    """R2 binding."""


class DeploymentConfigsPreviewServicesServiceBinding(TypedDict, total=False):
    entrypoint: Optional[str]
    """The entrypoint to bind to."""

    environment: str
    """The Service environment."""

    service: str
    """The Service name."""


class DeploymentConfigsPreviewServices(TypedDict, total=False):
    service_binding: Annotated[DeploymentConfigsPreviewServicesServiceBinding, PropertyInfo(alias="SERVICE_BINDING")]
    """Service binding."""


class DeploymentConfigsPreviewVectorizeBindingsVectorize(TypedDict, total=False):
    index_name: str


class DeploymentConfigsPreviewVectorizeBindings(TypedDict, total=False):
    vectorize: Annotated[DeploymentConfigsPreviewVectorizeBindingsVectorize, PropertyInfo(alias="VECTORIZE")]
    """Vectorize binding."""


class DeploymentConfigsPreview(TypedDict, total=False):
    ai_bindings: Optional[DeploymentConfigsPreviewAIBindings]
    """Constellation bindings used for Pages Functions."""

    analytics_engine_datasets: Optional[DeploymentConfigsPreviewAnalyticsEngineDatasets]
    """Analytics Engine bindings used for Pages Functions."""

    browsers: Optional[DeploymentConfigsPreviewBrowsers]
    """Browser bindings used for Pages Functions."""

    compatibility_date: str
    """Compatibility date used for Pages Functions."""

    compatibility_flags: List[str]
    """Compatibility flags used for Pages Functions."""

    d1_databases: Optional[DeploymentConfigsPreviewD1Databases]
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[DeploymentConfigsPreviewDurableObjectNamespaces]
    """Durabble Object namespaces used for Pages Functions."""

    env_vars: Optional[DeploymentConfigsPreviewEnvVars]
    """Environment variables for build configs."""

    hyperdrive_bindings: Optional[DeploymentConfigsPreviewHyperdriveBindings]
    """Hyperdrive bindings used for Pages Functions."""

    kv_namespaces: DeploymentConfigsPreviewKVNamespaces
    """KV namespaces used for Pages Functions."""

    mtls_certificates: Optional[DeploymentConfigsPreviewMTLSCertificates]
    """mTLS bindings used for Pages Functions."""

    placement: Optional[DeploymentConfigsPreviewPlacement]
    """Placement setting used for Pages Functions."""

    queue_producers: Optional[DeploymentConfigsPreviewQueueProducers]
    """Queue Producer bindings used for Pages Functions."""

    r2_buckets: Optional[DeploymentConfigsPreviewR2Buckets]
    """R2 buckets used for Pages Functions."""

    services: Optional[DeploymentConfigsPreviewServices]
    """Services used for Pages Functions."""

    vectorize_bindings: Optional[DeploymentConfigsPreviewVectorizeBindings]
    """Vectorize bindings used for Pages Functions."""


class DeploymentConfigsProductionAIBindingsAIBinding(TypedDict, total=False):
    project_id: str


class DeploymentConfigsProductionAIBindings(TypedDict, total=False):
    ai_binding: Annotated[DeploymentConfigsProductionAIBindingsAIBinding, PropertyInfo(alias="AI_BINDING")]
    """AI binding."""


class DeploymentConfigsProductionAnalyticsEngineDatasetsAnalyticsEngineBinding(TypedDict, total=False):
    dataset: str
    """Name of the dataset."""


class DeploymentConfigsProductionAnalyticsEngineDatasets(TypedDict, total=False):
    analytics_engine_binding: Annotated[
        DeploymentConfigsProductionAnalyticsEngineDatasetsAnalyticsEngineBinding,
        PropertyInfo(alias="ANALYTICS_ENGINE_BINDING"),
    ]
    """Analytics Engine binding."""


class DeploymentConfigsProductionBrowsers(TypedDict, total=False):
    browser: Annotated[object, PropertyInfo(alias="BROWSER")]
    """Browser binding."""


class DeploymentConfigsProductionD1DatabasesD1Binding(TypedDict, total=False):
    id: str
    """UUID of the D1 database."""


class DeploymentConfigsProductionD1Databases(TypedDict, total=False):
    d1_binding: Annotated[DeploymentConfigsProductionD1DatabasesD1Binding, PropertyInfo(alias="D1_BINDING")]
    """D1 binding."""


class DeploymentConfigsProductionDurableObjectNamespacesDoBinding(TypedDict, total=False):
    namespace_id: str
    """ID of the Durabble Object namespace."""


class DeploymentConfigsProductionDurableObjectNamespaces(TypedDict, total=False):
    do_binding: Annotated[DeploymentConfigsProductionDurableObjectNamespacesDoBinding, PropertyInfo(alias="DO_BINDING")]
    """Durabble Object binding."""


class DeploymentConfigsProductionEnvVarsEnvironmentVariable(TypedDict, total=False):
    type: Literal["plain_text", "secret_text"]
    """The type of environment variable (plain text or secret)"""

    value: str
    """Environment variable value."""


class DeploymentConfigsProductionEnvVars(TypedDict, total=False):
    environment_variable: Annotated[
        DeploymentConfigsProductionEnvVarsEnvironmentVariable, PropertyInfo(alias="ENVIRONMENT_VARIABLE")
    ]
    """Environment variable."""


class DeploymentConfigsProductionHyperdriveBindingsHyperdrive(TypedDict, total=False):
    id: str


class DeploymentConfigsProductionHyperdriveBindings(TypedDict, total=False):
    hyperdrive: Annotated[DeploymentConfigsProductionHyperdriveBindingsHyperdrive, PropertyInfo(alias="HYPERDRIVE")]
    """Hyperdrive binding."""


class DeploymentConfigsProductionKVNamespacesKVBinding(TypedDict, total=False):
    namespace_id: str
    """ID of the KV namespace."""


class DeploymentConfigsProductionKVNamespaces(TypedDict, total=False):
    kv_binding: Annotated[DeploymentConfigsProductionKVNamespacesKVBinding, PropertyInfo(alias="KV_BINDING")]
    """KV binding."""


class DeploymentConfigsProductionMTLSCertificatesMTLS(TypedDict, total=False):
    certificate_id: str


class DeploymentConfigsProductionMTLSCertificates(TypedDict, total=False):
    mtls: Annotated[DeploymentConfigsProductionMTLSCertificatesMTLS, PropertyInfo(alias="MTLS")]
    """mTLS binding."""


class DeploymentConfigsProductionPlacement(TypedDict, total=False):
    mode: str
    """Placement mode."""


class DeploymentConfigsProductionQueueProducersQueueProducerBinding(TypedDict, total=False):
    name: str
    """Name of the Queue."""


class DeploymentConfigsProductionQueueProducers(TypedDict, total=False):
    queue_producer_binding: Annotated[
        DeploymentConfigsProductionQueueProducersQueueProducerBinding, PropertyInfo(alias="QUEUE_PRODUCER_BINDING")
    ]
    """Queue Producer binding."""


class DeploymentConfigsProductionR2BucketsR2Binding(TypedDict, total=False):
    jurisdiction: Optional[str]
    """Jurisdiction of the R2 bucket."""

    name: str
    """Name of the R2 bucket."""


class DeploymentConfigsProductionR2Buckets(TypedDict, total=False):
    r2_binding: Annotated[DeploymentConfigsProductionR2BucketsR2Binding, PropertyInfo(alias="R2_BINDING")]
    """R2 binding."""


class DeploymentConfigsProductionServicesServiceBinding(TypedDict, total=False):
    entrypoint: Optional[str]
    """The entrypoint to bind to."""

    environment: str
    """The Service environment."""

    service: str
    """The Service name."""


class DeploymentConfigsProductionServices(TypedDict, total=False):
    service_binding: Annotated[DeploymentConfigsProductionServicesServiceBinding, PropertyInfo(alias="SERVICE_BINDING")]
    """Service binding."""


class DeploymentConfigsProductionVectorizeBindingsVectorize(TypedDict, total=False):
    index_name: str


class DeploymentConfigsProductionVectorizeBindings(TypedDict, total=False):
    vectorize: Annotated[DeploymentConfigsProductionVectorizeBindingsVectorize, PropertyInfo(alias="VECTORIZE")]
    """Vectorize binding."""


class DeploymentConfigsProduction(TypedDict, total=False):
    ai_bindings: Optional[DeploymentConfigsProductionAIBindings]
    """Constellation bindings used for Pages Functions."""

    analytics_engine_datasets: Optional[DeploymentConfigsProductionAnalyticsEngineDatasets]
    """Analytics Engine bindings used for Pages Functions."""

    browsers: Optional[DeploymentConfigsProductionBrowsers]
    """Browser bindings used for Pages Functions."""

    compatibility_date: str
    """Compatibility date used for Pages Functions."""

    compatibility_flags: List[str]
    """Compatibility flags used for Pages Functions."""

    d1_databases: Optional[DeploymentConfigsProductionD1Databases]
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[DeploymentConfigsProductionDurableObjectNamespaces]
    """Durabble Object namespaces used for Pages Functions."""

    env_vars: Optional[DeploymentConfigsProductionEnvVars]
    """Environment variables for build configs."""

    hyperdrive_bindings: Optional[DeploymentConfigsProductionHyperdriveBindings]
    """Hyperdrive bindings used for Pages Functions."""

    kv_namespaces: DeploymentConfigsProductionKVNamespaces
    """KV namespaces used for Pages Functions."""

    mtls_certificates: Optional[DeploymentConfigsProductionMTLSCertificates]
    """mTLS bindings used for Pages Functions."""

    placement: Optional[DeploymentConfigsProductionPlacement]
    """Placement setting used for Pages Functions."""

    queue_producers: Optional[DeploymentConfigsProductionQueueProducers]
    """Queue Producer bindings used for Pages Functions."""

    r2_buckets: Optional[DeploymentConfigsProductionR2Buckets]
    """R2 buckets used for Pages Functions."""

    services: Optional[DeploymentConfigsProductionServices]
    """Services used for Pages Functions."""

    vectorize_bindings: Optional[DeploymentConfigsProductionVectorizeBindings]
    """Vectorize bindings used for Pages Functions."""


class DeploymentConfigs(TypedDict, total=False):
    preview: DeploymentConfigsPreview
    """Configs for preview deploys."""

    production: DeploymentConfigsProduction
    """Configs for production deploys."""
