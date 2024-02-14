# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from datetime import datetime

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = [
    "ProjectGetResponse",
    "BuildConfig",
    "CanonicalDeployment",
    "CanonicalDeploymentDeploymentTrigger",
    "CanonicalDeploymentDeploymentTriggerMetadata",
    "CanonicalDeploymentStage",
    "DeploymentConfigs",
    "DeploymentConfigsPreview",
    "DeploymentConfigsPreviewAIBindings",
    "DeploymentConfigsPreviewAIBindingsAIBinding",
    "DeploymentConfigsPreviewAnalyticsEngineDatasets",
    "DeploymentConfigsPreviewAnalyticsEngineDatasetsAnalyticsEngineBinding",
    "DeploymentConfigsPreviewD1Databases",
    "DeploymentConfigsPreviewD1DatabasesD1Binding",
    "DeploymentConfigsPreviewDurableObjectNamespaces",
    "DeploymentConfigsPreviewDurableObjectNamespacesDoBinding",
    "DeploymentConfigsPreviewEnvVars",
    "DeploymentConfigsPreviewEnvVarsEnvironmentVariable",
    "DeploymentConfigsPreviewKvNamespaces",
    "DeploymentConfigsPreviewKvNamespacesKvBinding",
    "DeploymentConfigsPreviewPlacement",
    "DeploymentConfigsPreviewQueueProducers",
    "DeploymentConfigsPreviewQueueProducersQueueProducerBinding",
    "DeploymentConfigsPreviewR2Buckets",
    "DeploymentConfigsPreviewR2BucketsR2Binding",
    "DeploymentConfigsPreviewServiceBindings",
    "DeploymentConfigsPreviewServiceBindingsServiceBinding",
    "DeploymentConfigsProduction",
    "DeploymentConfigsProductionAIBindings",
    "DeploymentConfigsProductionAIBindingsAIBinding",
    "DeploymentConfigsProductionAnalyticsEngineDatasets",
    "DeploymentConfigsProductionAnalyticsEngineDatasetsAnalyticsEngineBinding",
    "DeploymentConfigsProductionD1Databases",
    "DeploymentConfigsProductionD1DatabasesD1Binding",
    "DeploymentConfigsProductionDurableObjectNamespaces",
    "DeploymentConfigsProductionDurableObjectNamespacesDoBinding",
    "DeploymentConfigsProductionEnvVars",
    "DeploymentConfigsProductionEnvVarsEnvironmentVariable",
    "DeploymentConfigsProductionKvNamespaces",
    "DeploymentConfigsProductionKvNamespacesKvBinding",
    "DeploymentConfigsProductionPlacement",
    "DeploymentConfigsProductionQueueProducers",
    "DeploymentConfigsProductionQueueProducersQueueProducerBinding",
    "DeploymentConfigsProductionR2Buckets",
    "DeploymentConfigsProductionR2BucketsR2Binding",
    "DeploymentConfigsProductionServiceBindings",
    "DeploymentConfigsProductionServiceBindingsServiceBinding",
    "LatestDeployment",
    "LatestDeploymentDeploymentTrigger",
    "LatestDeploymentDeploymentTriggerMetadata",
    "LatestDeploymentStage",
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


class CanonicalDeploymentDeploymentTriggerMetadata(BaseModel):
    branch: Optional[str] = None
    """Where the trigger happened."""

    commit_hash: Optional[str] = None
    """Hash of the deployment trigger commit."""

    commit_message: Optional[str] = None
    """Message of the deployment trigger commit."""


class CanonicalDeploymentDeploymentTrigger(BaseModel):
    metadata: Optional[CanonicalDeploymentDeploymentTriggerMetadata] = None
    """Additional info about the trigger."""

    type: Optional[str] = None
    """What caused the deployment."""


class CanonicalDeploymentStage(BaseModel):
    ended_on: Optional[datetime] = None
    """When the stage ended."""

    name: Optional[str] = None
    """The current build stage."""

    started_on: Optional[datetime] = None
    """When the stage started."""

    status: Optional[str] = None
    """State of the current stage."""


class CanonicalDeployment(BaseModel):
    id: Optional[str] = None
    """Id of the deployment."""

    aliases: Optional[List[object]] = None
    """A list of alias URLs pointing to this deployment."""

    build_config: Optional[object] = None

    created_on: Optional[datetime] = None
    """When the deployment was created."""

    deployment_trigger: Optional[CanonicalDeploymentDeploymentTrigger] = None
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

    stages: Optional[List[CanonicalDeploymentStage]] = None
    """List of past stages."""

    url: Optional[str] = None
    """The live URL to view this deployment."""


class DeploymentConfigsPreviewAIBindingsAIBinding(BaseModel):
    project_id: Optional[object] = None


class DeploymentConfigsPreviewAIBindings(BaseModel):
    ai_binding: Optional[DeploymentConfigsPreviewAIBindingsAIBinding] = FieldInfo(alias="AI_BINDING", default=None)
    """AI binding."""


class DeploymentConfigsPreviewAnalyticsEngineDatasetsAnalyticsEngineBinding(BaseModel):
    dataset: Optional[str] = None
    """Name of the dataset."""


class DeploymentConfigsPreviewAnalyticsEngineDatasets(BaseModel):
    analytics_engine_binding: Optional[
        DeploymentConfigsPreviewAnalyticsEngineDatasetsAnalyticsEngineBinding
    ] = FieldInfo(alias="ANALYTICS_ENGINE_BINDING", default=None)
    """Analytics Engine binding."""


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


class DeploymentConfigsPreviewKvNamespacesKvBinding(BaseModel):
    namespace_id: Optional[str] = None
    """ID of the KV namespace."""


class DeploymentConfigsPreviewKvNamespaces(BaseModel):
    kv_binding: Optional[DeploymentConfigsPreviewKvNamespacesKvBinding] = FieldInfo(alias="KV_BINDING", default=None)
    """KV binding."""


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
    name: Optional[str] = None
    """Name of the R2 bucket."""


class DeploymentConfigsPreviewR2Buckets(BaseModel):
    r2_binding: Optional[DeploymentConfigsPreviewR2BucketsR2Binding] = FieldInfo(alias="R2_BINDING", default=None)
    """R2 binding."""


class DeploymentConfigsPreviewServiceBindingsServiceBinding(BaseModel):
    environment: Optional[str] = None
    """The Service environment."""

    service: Optional[str] = None
    """The Service name."""


class DeploymentConfigsPreviewServiceBindings(BaseModel):
    service_binding: Optional[DeploymentConfigsPreviewServiceBindingsServiceBinding] = FieldInfo(
        alias="SERVICE_BINDING", default=None
    )
    """Service binding."""


class DeploymentConfigsPreview(BaseModel):
    ai_bindings: Optional[DeploymentConfigsPreviewAIBindings] = None
    """Constellation bindings used for Pages Functions."""

    analytics_engine_datasets: Optional[DeploymentConfigsPreviewAnalyticsEngineDatasets] = None
    """Analytics Engine bindings used for Pages Functions."""

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

    kv_namespaces: Optional[DeploymentConfigsPreviewKvNamespaces] = None
    """KV namespaces used for Pages Functions."""

    placement: Optional[DeploymentConfigsPreviewPlacement] = None
    """Placement setting used for Pages Functions."""

    queue_producers: Optional[DeploymentConfigsPreviewQueueProducers] = None
    """Queue Producer bindings used for Pages Functions."""

    r2_buckets: Optional[DeploymentConfigsPreviewR2Buckets] = None
    """R2 buckets used for Pages Functions."""

    service_bindings: Optional[DeploymentConfigsPreviewServiceBindings] = None
    """Services used for Pages Functions."""


class DeploymentConfigsProductionAIBindingsAIBinding(BaseModel):
    project_id: Optional[object] = None


class DeploymentConfigsProductionAIBindings(BaseModel):
    ai_binding: Optional[DeploymentConfigsProductionAIBindingsAIBinding] = FieldInfo(alias="AI_BINDING", default=None)
    """AI binding."""


class DeploymentConfigsProductionAnalyticsEngineDatasetsAnalyticsEngineBinding(BaseModel):
    dataset: Optional[str] = None
    """Name of the dataset."""


class DeploymentConfigsProductionAnalyticsEngineDatasets(BaseModel):
    analytics_engine_binding: Optional[
        DeploymentConfigsProductionAnalyticsEngineDatasetsAnalyticsEngineBinding
    ] = FieldInfo(alias="ANALYTICS_ENGINE_BINDING", default=None)
    """Analytics Engine binding."""


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


class DeploymentConfigsProductionKvNamespacesKvBinding(BaseModel):
    namespace_id: Optional[str] = None
    """ID of the KV namespace."""


class DeploymentConfigsProductionKvNamespaces(BaseModel):
    kv_binding: Optional[DeploymentConfigsProductionKvNamespacesKvBinding] = FieldInfo(alias="KV_BINDING", default=None)
    """KV binding."""


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
    name: Optional[str] = None
    """Name of the R2 bucket."""


class DeploymentConfigsProductionR2Buckets(BaseModel):
    r2_binding: Optional[DeploymentConfigsProductionR2BucketsR2Binding] = FieldInfo(alias="R2_BINDING", default=None)
    """R2 binding."""


class DeploymentConfigsProductionServiceBindingsServiceBinding(BaseModel):
    environment: Optional[str] = None
    """The Service environment."""

    service: Optional[str] = None
    """The Service name."""


class DeploymentConfigsProductionServiceBindings(BaseModel):
    service_binding: Optional[DeploymentConfigsProductionServiceBindingsServiceBinding] = FieldInfo(
        alias="SERVICE_BINDING", default=None
    )
    """Service binding."""


class DeploymentConfigsProduction(BaseModel):
    ai_bindings: Optional[DeploymentConfigsProductionAIBindings] = None
    """Constellation bindings used for Pages Functions."""

    analytics_engine_datasets: Optional[DeploymentConfigsProductionAnalyticsEngineDatasets] = None
    """Analytics Engine bindings used for Pages Functions."""

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

    kv_namespaces: Optional[DeploymentConfigsProductionKvNamespaces] = None
    """KV namespaces used for Pages Functions."""

    placement: Optional[DeploymentConfigsProductionPlacement] = None
    """Placement setting used for Pages Functions."""

    queue_producers: Optional[DeploymentConfigsProductionQueueProducers] = None
    """Queue Producer bindings used for Pages Functions."""

    r2_buckets: Optional[DeploymentConfigsProductionR2Buckets] = None
    """R2 buckets used for Pages Functions."""

    service_bindings: Optional[DeploymentConfigsProductionServiceBindings] = None
    """Services used for Pages Functions."""


class DeploymentConfigs(BaseModel):
    preview: Optional[DeploymentConfigsPreview] = None
    """Configs for preview deploys."""

    production: Optional[DeploymentConfigsProduction] = None
    """Configs for production deploys."""


class LatestDeploymentDeploymentTriggerMetadata(BaseModel):
    branch: Optional[str] = None
    """Where the trigger happened."""

    commit_hash: Optional[str] = None
    """Hash of the deployment trigger commit."""

    commit_message: Optional[str] = None
    """Message of the deployment trigger commit."""


class LatestDeploymentDeploymentTrigger(BaseModel):
    metadata: Optional[LatestDeploymentDeploymentTriggerMetadata] = None
    """Additional info about the trigger."""

    type: Optional[str] = None
    """What caused the deployment."""


class LatestDeploymentStage(BaseModel):
    ended_on: Optional[datetime] = None
    """When the stage ended."""

    name: Optional[str] = None
    """The current build stage."""

    started_on: Optional[datetime] = None
    """When the stage started."""

    status: Optional[str] = None
    """State of the current stage."""


class LatestDeployment(BaseModel):
    id: Optional[str] = None
    """Id of the deployment."""

    aliases: Optional[List[object]] = None
    """A list of alias URLs pointing to this deployment."""

    build_config: Optional[object] = None

    created_on: Optional[datetime] = None
    """When the deployment was created."""

    deployment_trigger: Optional[LatestDeploymentDeploymentTrigger] = None
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

    stages: Optional[List[LatestDeploymentStage]] = None
    """List of past stages."""

    url: Optional[str] = None
    """The live URL to view this deployment."""


class ProjectGetResponse(BaseModel):
    id: Optional[str] = None
    """Id of the project."""

    build_config: Optional[BuildConfig] = None
    """Configs for the project build process."""

    canonical_deployment: Optional[CanonicalDeployment] = None

    created_on: Optional[datetime] = None
    """When the project was created."""

    deployment_configs: Optional[DeploymentConfigs] = None
    """Configs for deployments in a project."""

    domains: Optional[List[object]] = None
    """A list of associated custom domains for the project."""

    latest_deployment: Optional[LatestDeployment] = None

    name: Optional[str] = None
    """Name of the project."""

    production_branch: Optional[str] = None
    """Production branch of the project. Used to identify production deployments."""

    source: Optional[object] = None

    subdomain: Optional[str] = None
    """The Cloudflare subdomain associated with the project."""
