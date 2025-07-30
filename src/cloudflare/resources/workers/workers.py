# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .routes import (
    RoutesResource,
    AsyncRoutesResource,
    RoutesResourceWithRawResponse,
    AsyncRoutesResourceWithRawResponse,
    RoutesResourceWithStreamingResponse,
    AsyncRoutesResourceWithStreamingResponse,
)
from .domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .subdomains import (
    SubdomainsResource,
    AsyncSubdomainsResource,
    SubdomainsResourceWithRawResponse,
    AsyncSubdomainsResourceWithRawResponse,
    SubdomainsResourceWithStreamingResponse,
    AsyncSubdomainsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .assets.assets import (
    AssetsResource,
    AsyncAssetsResource,
    AssetsResourceWithRawResponse,
    AsyncAssetsResourceWithRawResponse,
    AssetsResourceWithStreamingResponse,
    AsyncAssetsResourceWithStreamingResponse,
)
from .scripts.scripts import (
    ScriptsResource,
    AsyncScriptsResource,
    ScriptsResourceWithRawResponse,
    AsyncScriptsResourceWithRawResponse,
    ScriptsResourceWithStreamingResponse,
    AsyncScriptsResourceWithStreamingResponse,
)
from .account_settings import (
    AccountSettingsResource,
    AsyncAccountSettingsResource,
    AccountSettingsResourceWithRawResponse,
    AsyncAccountSettingsResourceWithRawResponse,
    AccountSettingsResourceWithStreamingResponse,
    AsyncAccountSettingsResourceWithStreamingResponse,
)

__all__ = ["WorkersResource", "AsyncWorkersResource"]


class WorkersResource(SyncAPIResource):
    @cached_property
    def routes(self) -> RoutesResource:
        return RoutesResource(self._client)

    @cached_property
    def assets(self) -> AssetsResource:
        return AssetsResource(self._client)

    @cached_property
    def scripts(self) -> ScriptsResource:
        return ScriptsResource(self._client)

    @cached_property
    def account_settings(self) -> AccountSettingsResource:
        return AccountSettingsResource(self._client)

    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def subdomains(self) -> SubdomainsResource:
        return SubdomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return WorkersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return WorkersResourceWithStreamingResponse(self)


class AsyncWorkersResource(AsyncAPIResource):
    @cached_property
    def routes(self) -> AsyncRoutesResource:
        return AsyncRoutesResource(self._client)

    @cached_property
    def assets(self) -> AsyncAssetsResource:
        return AsyncAssetsResource(self._client)

    @cached_property
    def scripts(self) -> AsyncScriptsResource:
        return AsyncScriptsResource(self._client)

    @cached_property
    def account_settings(self) -> AsyncAccountSettingsResource:
        return AsyncAccountSettingsResource(self._client)

    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def subdomains(self) -> AsyncSubdomainsResource:
        return AsyncSubdomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncWorkersResourceWithStreamingResponse(self)


class WorkersResourceWithRawResponse:
    def __init__(self, workers: WorkersResource) -> None:
        self._workers = workers

    @cached_property
    def routes(self) -> RoutesResourceWithRawResponse:
        return RoutesResourceWithRawResponse(self._workers.routes)

    @cached_property
    def assets(self) -> AssetsResourceWithRawResponse:
        return AssetsResourceWithRawResponse(self._workers.assets)

    @cached_property
    def scripts(self) -> ScriptsResourceWithRawResponse:
        return ScriptsResourceWithRawResponse(self._workers.scripts)

    @cached_property
    def account_settings(self) -> AccountSettingsResourceWithRawResponse:
        return AccountSettingsResourceWithRawResponse(self._workers.account_settings)

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._workers.domains)

    @cached_property
    def subdomains(self) -> SubdomainsResourceWithRawResponse:
        return SubdomainsResourceWithRawResponse(self._workers.subdomains)


class AsyncWorkersResourceWithRawResponse:
    def __init__(self, workers: AsyncWorkersResource) -> None:
        self._workers = workers

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithRawResponse:
        return AsyncRoutesResourceWithRawResponse(self._workers.routes)

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithRawResponse:
        return AsyncAssetsResourceWithRawResponse(self._workers.assets)

    @cached_property
    def scripts(self) -> AsyncScriptsResourceWithRawResponse:
        return AsyncScriptsResourceWithRawResponse(self._workers.scripts)

    @cached_property
    def account_settings(self) -> AsyncAccountSettingsResourceWithRawResponse:
        return AsyncAccountSettingsResourceWithRawResponse(self._workers.account_settings)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._workers.domains)

    @cached_property
    def subdomains(self) -> AsyncSubdomainsResourceWithRawResponse:
        return AsyncSubdomainsResourceWithRawResponse(self._workers.subdomains)


class WorkersResourceWithStreamingResponse:
    def __init__(self, workers: WorkersResource) -> None:
        self._workers = workers

    @cached_property
    def routes(self) -> RoutesResourceWithStreamingResponse:
        return RoutesResourceWithStreamingResponse(self._workers.routes)

    @cached_property
    def assets(self) -> AssetsResourceWithStreamingResponse:
        return AssetsResourceWithStreamingResponse(self._workers.assets)

    @cached_property
    def scripts(self) -> ScriptsResourceWithStreamingResponse:
        return ScriptsResourceWithStreamingResponse(self._workers.scripts)

    @cached_property
    def account_settings(self) -> AccountSettingsResourceWithStreamingResponse:
        return AccountSettingsResourceWithStreamingResponse(self._workers.account_settings)

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._workers.domains)

    @cached_property
    def subdomains(self) -> SubdomainsResourceWithStreamingResponse:
        return SubdomainsResourceWithStreamingResponse(self._workers.subdomains)


class AsyncWorkersResourceWithStreamingResponse:
    def __init__(self, workers: AsyncWorkersResource) -> None:
        self._workers = workers

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithStreamingResponse:
        return AsyncRoutesResourceWithStreamingResponse(self._workers.routes)

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithStreamingResponse:
        return AsyncAssetsResourceWithStreamingResponse(self._workers.assets)

    @cached_property
    def scripts(self) -> AsyncScriptsResourceWithStreamingResponse:
        return AsyncScriptsResourceWithStreamingResponse(self._workers.scripts)

    @cached_property
    def account_settings(self) -> AsyncAccountSettingsResourceWithStreamingResponse:
        return AsyncAccountSettingsResourceWithStreamingResponse(self._workers.account_settings)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._workers.domains)

    @cached_property
    def subdomains(self) -> AsyncSubdomainsResourceWithStreamingResponse:
        return AsyncSubdomainsResourceWithStreamingResponse(self._workers.subdomains)
