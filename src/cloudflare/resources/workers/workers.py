# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ai import (
    AI,
    AsyncAI,
    AIWithRawResponse,
    AsyncAIWithRawResponse,
    AIWithStreamingResponse,
    AsyncAIWithStreamingResponse,
)
from .routes import (
    Routes,
    AsyncRoutes,
    RoutesWithRawResponse,
    AsyncRoutesWithRawResponse,
    RoutesWithStreamingResponse,
    AsyncRoutesWithStreamingResponse,
)
from .domains import (
    Domains,
    AsyncDomains,
    DomainsWithRawResponse,
    AsyncDomainsWithRawResponse,
    DomainsWithStreamingResponse,
    AsyncDomainsWithStreamingResponse,
)
from .filters import (
    Filters,
    AsyncFilters,
    FiltersWithRawResponse,
    AsyncFiltersWithRawResponse,
    FiltersWithStreamingResponse,
    AsyncFiltersWithStreamingResponse,
)
from .scripts import (
    Scripts,
    AsyncScripts,
    ScriptsWithRawResponse,
    AsyncScriptsWithRawResponse,
    ScriptsWithStreamingResponse,
    AsyncScriptsWithStreamingResponse,
)
from .services import (
    Services,
    AsyncServices,
    ServicesWithRawResponse,
    AsyncServicesWithRawResponse,
    ServicesWithStreamingResponse,
    AsyncServicesWithStreamingResponse,
)
from ..._compat import cached_property
from .subdomains import (
    Subdomains,
    AsyncSubdomains,
    SubdomainsWithRawResponse,
    AsyncSubdomainsWithRawResponse,
    SubdomainsWithStreamingResponse,
    AsyncSubdomainsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .deployments import (
    Deployments,
    AsyncDeployments,
    DeploymentsWithRawResponse,
    AsyncDeploymentsWithRawResponse,
    DeploymentsWithStreamingResponse,
    AsyncDeploymentsWithStreamingResponse,
)
from .scripts.scripts import Scripts, AsyncScripts
from .account_settings import (
    AccountSettings,
    AsyncAccountSettings,
    AccountSettingsWithRawResponse,
    AsyncAccountSettingsWithRawResponse,
    AccountSettingsWithStreamingResponse,
    AsyncAccountSettingsWithStreamingResponse,
)
from .services.services import Services, AsyncServices
from .deployments.deployments import Deployments, AsyncDeployments

__all__ = ["Workers", "AsyncWorkers"]


class Workers(SyncAPIResource):
    @cached_property
    def ai(self) -> AI:
        return AI(self._client)

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
    def subdomains(self) -> Subdomains:
        return Subdomains(self._client)

    @cached_property
    def services(self) -> Services:
        return Services(self._client)

    @cached_property
    def with_raw_response(self) -> WorkersWithRawResponse:
        return WorkersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkersWithStreamingResponse:
        return WorkersWithStreamingResponse(self)


class AsyncWorkers(AsyncAPIResource):
    @cached_property
    def ai(self) -> AsyncAI:
        return AsyncAI(self._client)

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
    def subdomains(self) -> AsyncSubdomains:
        return AsyncSubdomains(self._client)

    @cached_property
    def services(self) -> AsyncServices:
        return AsyncServices(self._client)

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
    def ai(self) -> AIWithRawResponse:
        return AIWithRawResponse(self._workers.ai)

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
    def subdomains(self) -> SubdomainsWithRawResponse:
        return SubdomainsWithRawResponse(self._workers.subdomains)

    @cached_property
    def services(self) -> ServicesWithRawResponse:
        return ServicesWithRawResponse(self._workers.services)


class AsyncWorkersWithRawResponse:
    def __init__(self, workers: AsyncWorkers) -> None:
        self._workers = workers

    @cached_property
    def ai(self) -> AsyncAIWithRawResponse:
        return AsyncAIWithRawResponse(self._workers.ai)

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
    def subdomains(self) -> AsyncSubdomainsWithRawResponse:
        return AsyncSubdomainsWithRawResponse(self._workers.subdomains)

    @cached_property
    def services(self) -> AsyncServicesWithRawResponse:
        return AsyncServicesWithRawResponse(self._workers.services)


class WorkersWithStreamingResponse:
    def __init__(self, workers: Workers) -> None:
        self._workers = workers

    @cached_property
    def ai(self) -> AIWithStreamingResponse:
        return AIWithStreamingResponse(self._workers.ai)

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
    def subdomains(self) -> SubdomainsWithStreamingResponse:
        return SubdomainsWithStreamingResponse(self._workers.subdomains)

    @cached_property
    def services(self) -> ServicesWithStreamingResponse:
        return ServicesWithStreamingResponse(self._workers.services)


class AsyncWorkersWithStreamingResponse:
    def __init__(self, workers: AsyncWorkers) -> None:
        self._workers = workers

    @cached_property
    def ai(self) -> AsyncAIWithStreamingResponse:
        return AsyncAIWithStreamingResponse(self._workers.ai)

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
    def subdomains(self) -> AsyncSubdomainsWithStreamingResponse:
        return AsyncSubdomainsWithStreamingResponse(self._workers.subdomains)

    @cached_property
    def services(self) -> AsyncServicesWithStreamingResponse:
        return AsyncServicesWithStreamingResponse(self._workers.services)
