# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .scripts.scripts import Scripts, AsyncScripts

from ..._compat import cached_property

from .filters import Filters, AsyncFilters

from .routes import Routes, AsyncRoutes

from .account_settings import AccountSettings, AsyncAccountSettings

from .deployments.deployments import Deployments, AsyncDeployments

from .domains import Domains, AsyncDomains

from .durable_objects.durable_objects import DurableObjects, AsyncDurableObjects

from .queues.queues import Queues, AsyncQueues

from .subdomains import Subdomains, AsyncSubdomains

from .deployments_by_script import DeploymentsByScript, AsyncDeploymentsByScript

from .services.services import Services, AsyncServices

from .script import Script, AsyncScript

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from .scripts import (
    Scripts,
    AsyncScripts,
    ScriptsWithRawResponse,
    AsyncScriptsWithRawResponse,
    ScriptsWithStreamingResponse,
    AsyncScriptsWithStreamingResponse,
)
from .filters import (
    Filters,
    AsyncFilters,
    FiltersWithRawResponse,
    AsyncFiltersWithRawResponse,
    FiltersWithStreamingResponse,
    AsyncFiltersWithStreamingResponse,
)
from .routes import (
    Routes,
    AsyncRoutes,
    RoutesWithRawResponse,
    AsyncRoutesWithRawResponse,
    RoutesWithStreamingResponse,
    AsyncRoutesWithStreamingResponse,
)
from .account_settings import (
    AccountSettings,
    AsyncAccountSettings,
    AccountSettingsWithRawResponse,
    AsyncAccountSettingsWithRawResponse,
    AccountSettingsWithStreamingResponse,
    AsyncAccountSettingsWithStreamingResponse,
)
from .deployments import (
    Deployments,
    AsyncDeployments,
    DeploymentsWithRawResponse,
    AsyncDeploymentsWithRawResponse,
    DeploymentsWithStreamingResponse,
    AsyncDeploymentsWithStreamingResponse,
)
from .domains import (
    Domains,
    AsyncDomains,
    DomainsWithRawResponse,
    AsyncDomainsWithRawResponse,
    DomainsWithStreamingResponse,
    AsyncDomainsWithStreamingResponse,
)
from .durable_objects import (
    DurableObjects,
    AsyncDurableObjects,
    DurableObjectsWithRawResponse,
    AsyncDurableObjectsWithRawResponse,
    DurableObjectsWithStreamingResponse,
    AsyncDurableObjectsWithStreamingResponse,
)
from .queues import (
    Queues,
    AsyncQueues,
    QueuesWithRawResponse,
    AsyncQueuesWithRawResponse,
    QueuesWithStreamingResponse,
    AsyncQueuesWithStreamingResponse,
)
from .subdomains import (
    Subdomains,
    AsyncSubdomains,
    SubdomainsWithRawResponse,
    AsyncSubdomainsWithRawResponse,
    SubdomainsWithStreamingResponse,
    AsyncSubdomainsWithStreamingResponse,
)
from .deployments_by_script import (
    DeploymentsByScript,
    AsyncDeploymentsByScript,
    DeploymentsByScriptWithRawResponse,
    AsyncDeploymentsByScriptWithRawResponse,
    DeploymentsByScriptWithStreamingResponse,
    AsyncDeploymentsByScriptWithStreamingResponse,
)
from .services import (
    Services,
    AsyncServices,
    ServicesWithRawResponse,
    AsyncServicesWithRawResponse,
    ServicesWithStreamingResponse,
    AsyncServicesWithStreamingResponse,
)
from .script import (
    Script,
    AsyncScript,
    ScriptWithRawResponse,
    AsyncScriptWithRawResponse,
    ScriptWithStreamingResponse,
    AsyncScriptWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Workers", "AsyncWorkers"]


class Workers(SyncAPIResource):
    @cached_property
    def scripts(self) -> Scripts:
        return Scripts(self._client)

    @cached_property
    def filters(self) -> Filters:
        return Filters(self._client)

    @cached_property
    def routes(self) -> Routes:
        return Routes(self._client)

    @cached_property
    def account_settings(self) -> AccountSettings:
        return AccountSettings(self._client)

    @cached_property
    def deployments(self) -> Deployments:
        return Deployments(self._client)

    @cached_property
    def domains(self) -> Domains:
        return Domains(self._client)

    @cached_property
    def durable_objects(self) -> DurableObjects:
        return DurableObjects(self._client)

    @cached_property
    def queues(self) -> Queues:
        return Queues(self._client)

    @cached_property
    def subdomains(self) -> Subdomains:
        return Subdomains(self._client)

    @cached_property
    def deployments_by_script(self) -> DeploymentsByScript:
        return DeploymentsByScript(self._client)

    @cached_property
    def services(self) -> Services:
        return Services(self._client)

    @cached_property
    def script(self) -> Script:
        return Script(self._client)

    @cached_property
    def with_raw_response(self) -> WorkersWithRawResponse:
        return WorkersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkersWithStreamingResponse:
        return WorkersWithStreamingResponse(self)


class AsyncWorkers(AsyncAPIResource):
    @cached_property
    def scripts(self) -> AsyncScripts:
        return AsyncScripts(self._client)

    @cached_property
    def filters(self) -> AsyncFilters:
        return AsyncFilters(self._client)

    @cached_property
    def routes(self) -> AsyncRoutes:
        return AsyncRoutes(self._client)

    @cached_property
    def account_settings(self) -> AsyncAccountSettings:
        return AsyncAccountSettings(self._client)

    @cached_property
    def deployments(self) -> AsyncDeployments:
        return AsyncDeployments(self._client)

    @cached_property
    def domains(self) -> AsyncDomains:
        return AsyncDomains(self._client)

    @cached_property
    def durable_objects(self) -> AsyncDurableObjects:
        return AsyncDurableObjects(self._client)

    @cached_property
    def queues(self) -> AsyncQueues:
        return AsyncQueues(self._client)

    @cached_property
    def subdomains(self) -> AsyncSubdomains:
        return AsyncSubdomains(self._client)

    @cached_property
    def deployments_by_script(self) -> AsyncDeploymentsByScript:
        return AsyncDeploymentsByScript(self._client)

    @cached_property
    def services(self) -> AsyncServices:
        return AsyncServices(self._client)

    @cached_property
    def script(self) -> AsyncScript:
        return AsyncScript(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkersWithRawResponse:
        return AsyncWorkersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkersWithStreamingResponse:
        return AsyncWorkersWithStreamingResponse(self)


class WorkersWithRawResponse:
    def __init__(self, workers: Workers) -> None:
        self._workers = workers

    @cached_property
    def scripts(self) -> ScriptsWithRawResponse:
        return ScriptsWithRawResponse(self._workers.scripts)

    @cached_property
    def filters(self) -> FiltersWithRawResponse:
        return FiltersWithRawResponse(self._workers.filters)

    @cached_property
    def routes(self) -> RoutesWithRawResponse:
        return RoutesWithRawResponse(self._workers.routes)

    @cached_property
    def account_settings(self) -> AccountSettingsWithRawResponse:
        return AccountSettingsWithRawResponse(self._workers.account_settings)

    @cached_property
    def deployments(self) -> DeploymentsWithRawResponse:
        return DeploymentsWithRawResponse(self._workers.deployments)

    @cached_property
    def domains(self) -> DomainsWithRawResponse:
        return DomainsWithRawResponse(self._workers.domains)

    @cached_property
    def durable_objects(self) -> DurableObjectsWithRawResponse:
        return DurableObjectsWithRawResponse(self._workers.durable_objects)

    @cached_property
    def queues(self) -> QueuesWithRawResponse:
        return QueuesWithRawResponse(self._workers.queues)

    @cached_property
    def subdomains(self) -> SubdomainsWithRawResponse:
        return SubdomainsWithRawResponse(self._workers.subdomains)

    @cached_property
    def deployments_by_script(self) -> DeploymentsByScriptWithRawResponse:
        return DeploymentsByScriptWithRawResponse(self._workers.deployments_by_script)

    @cached_property
    def services(self) -> ServicesWithRawResponse:
        return ServicesWithRawResponse(self._workers.services)

    @cached_property
    def script(self) -> ScriptWithRawResponse:
        return ScriptWithRawResponse(self._workers.script)


class AsyncWorkersWithRawResponse:
    def __init__(self, workers: AsyncWorkers) -> None:
        self._workers = workers

    @cached_property
    def scripts(self) -> AsyncScriptsWithRawResponse:
        return AsyncScriptsWithRawResponse(self._workers.scripts)

    @cached_property
    def filters(self) -> AsyncFiltersWithRawResponse:
        return AsyncFiltersWithRawResponse(self._workers.filters)

    @cached_property
    def routes(self) -> AsyncRoutesWithRawResponse:
        return AsyncRoutesWithRawResponse(self._workers.routes)

    @cached_property
    def account_settings(self) -> AsyncAccountSettingsWithRawResponse:
        return AsyncAccountSettingsWithRawResponse(self._workers.account_settings)

    @cached_property
    def deployments(self) -> AsyncDeploymentsWithRawResponse:
        return AsyncDeploymentsWithRawResponse(self._workers.deployments)

    @cached_property
    def domains(self) -> AsyncDomainsWithRawResponse:
        return AsyncDomainsWithRawResponse(self._workers.domains)

    @cached_property
    def durable_objects(self) -> AsyncDurableObjectsWithRawResponse:
        return AsyncDurableObjectsWithRawResponse(self._workers.durable_objects)

    @cached_property
    def queues(self) -> AsyncQueuesWithRawResponse:
        return AsyncQueuesWithRawResponse(self._workers.queues)

    @cached_property
    def subdomains(self) -> AsyncSubdomainsWithRawResponse:
        return AsyncSubdomainsWithRawResponse(self._workers.subdomains)

    @cached_property
    def deployments_by_script(self) -> AsyncDeploymentsByScriptWithRawResponse:
        return AsyncDeploymentsByScriptWithRawResponse(self._workers.deployments_by_script)

    @cached_property
    def services(self) -> AsyncServicesWithRawResponse:
        return AsyncServicesWithRawResponse(self._workers.services)

    @cached_property
    def script(self) -> AsyncScriptWithRawResponse:
        return AsyncScriptWithRawResponse(self._workers.script)


class WorkersWithStreamingResponse:
    def __init__(self, workers: Workers) -> None:
        self._workers = workers

    @cached_property
    def scripts(self) -> ScriptsWithStreamingResponse:
        return ScriptsWithStreamingResponse(self._workers.scripts)

    @cached_property
    def filters(self) -> FiltersWithStreamingResponse:
        return FiltersWithStreamingResponse(self._workers.filters)

    @cached_property
    def routes(self) -> RoutesWithStreamingResponse:
        return RoutesWithStreamingResponse(self._workers.routes)

    @cached_property
    def account_settings(self) -> AccountSettingsWithStreamingResponse:
        return AccountSettingsWithStreamingResponse(self._workers.account_settings)

    @cached_property
    def deployments(self) -> DeploymentsWithStreamingResponse:
        return DeploymentsWithStreamingResponse(self._workers.deployments)

    @cached_property
    def domains(self) -> DomainsWithStreamingResponse:
        return DomainsWithStreamingResponse(self._workers.domains)

    @cached_property
    def durable_objects(self) -> DurableObjectsWithStreamingResponse:
        return DurableObjectsWithStreamingResponse(self._workers.durable_objects)

    @cached_property
    def queues(self) -> QueuesWithStreamingResponse:
        return QueuesWithStreamingResponse(self._workers.queues)

    @cached_property
    def subdomains(self) -> SubdomainsWithStreamingResponse:
        return SubdomainsWithStreamingResponse(self._workers.subdomains)

    @cached_property
    def deployments_by_script(self) -> DeploymentsByScriptWithStreamingResponse:
        return DeploymentsByScriptWithStreamingResponse(self._workers.deployments_by_script)

    @cached_property
    def services(self) -> ServicesWithStreamingResponse:
        return ServicesWithStreamingResponse(self._workers.services)

    @cached_property
    def script(self) -> ScriptWithStreamingResponse:
        return ScriptWithStreamingResponse(self._workers.script)


class AsyncWorkersWithStreamingResponse:
    def __init__(self, workers: AsyncWorkers) -> None:
        self._workers = workers

    @cached_property
    def scripts(self) -> AsyncScriptsWithStreamingResponse:
        return AsyncScriptsWithStreamingResponse(self._workers.scripts)

    @cached_property
    def filters(self) -> AsyncFiltersWithStreamingResponse:
        return AsyncFiltersWithStreamingResponse(self._workers.filters)

    @cached_property
    def routes(self) -> AsyncRoutesWithStreamingResponse:
        return AsyncRoutesWithStreamingResponse(self._workers.routes)

    @cached_property
    def account_settings(self) -> AsyncAccountSettingsWithStreamingResponse:
        return AsyncAccountSettingsWithStreamingResponse(self._workers.account_settings)

    @cached_property
    def deployments(self) -> AsyncDeploymentsWithStreamingResponse:
        return AsyncDeploymentsWithStreamingResponse(self._workers.deployments)

    @cached_property
    def domains(self) -> AsyncDomainsWithStreamingResponse:
        return AsyncDomainsWithStreamingResponse(self._workers.domains)

    @cached_property
    def durable_objects(self) -> AsyncDurableObjectsWithStreamingResponse:
        return AsyncDurableObjectsWithStreamingResponse(self._workers.durable_objects)

    @cached_property
    def queues(self) -> AsyncQueuesWithStreamingResponse:
        return AsyncQueuesWithStreamingResponse(self._workers.queues)

    @cached_property
    def subdomains(self) -> AsyncSubdomainsWithStreamingResponse:
        return AsyncSubdomainsWithStreamingResponse(self._workers.subdomains)

    @cached_property
    def deployments_by_script(self) -> AsyncDeploymentsByScriptWithStreamingResponse:
        return AsyncDeploymentsByScriptWithStreamingResponse(self._workers.deployments_by_script)

    @cached_property
    def services(self) -> AsyncServicesWithStreamingResponse:
        return AsyncServicesWithStreamingResponse(self._workers.services)

    @cached_property
    def script(self) -> AsyncScriptWithStreamingResponse:
        return AsyncScriptWithStreamingResponse(self._workers.script)
