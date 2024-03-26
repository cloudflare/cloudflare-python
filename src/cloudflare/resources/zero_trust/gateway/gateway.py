# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from .lists import (
    Lists,
    AsyncLists,
    ListsWithRawResponse,
    AsyncListsWithRawResponse,
    ListsWithStreamingResponse,
    AsyncListsWithStreamingResponse,
)
from .rules import (
    Rules,
    AsyncRules,
    RulesWithRawResponse,
    AsyncRulesWithRawResponse,
    RulesWithStreamingResponse,
    AsyncRulesWithStreamingResponse,
)
from .logging import (
    Logging,
    AsyncLogging,
    LoggingWithRawResponse,
    AsyncLoggingWithRawResponse,
    LoggingWithStreamingResponse,
    AsyncLoggingWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .app_types import (
    AppTypes,
    AsyncAppTypes,
    AppTypesWithRawResponse,
    AsyncAppTypesWithRawResponse,
    AppTypesWithStreamingResponse,
    AsyncAppTypesWithStreamingResponse,
)
from .locations import (
    Locations,
    AsyncLocations,
    LocationsWithRawResponse,
    AsyncLocationsWithRawResponse,
    LocationsWithStreamingResponse,
    AsyncLocationsWithStreamingResponse,
)
from ...._compat import cached_property
from .categories import (
    Categories,
    AsyncCategories,
    CategoriesWithRawResponse,
    AsyncCategoriesWithRawResponse,
    CategoriesWithStreamingResponse,
    AsyncCategoriesWithStreamingResponse,
)
from .lists.lists import Lists, AsyncLists
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from .configurations import (
    Configurations,
    AsyncConfigurations,
    ConfigurationsWithRawResponse,
    AsyncConfigurationsWithRawResponse,
    ConfigurationsWithStreamingResponse,
    AsyncConfigurationsWithStreamingResponse,
)
from ...._base_client import (
    make_request_options,
)
from .proxy_endpoints import (
    ProxyEndpoints,
    AsyncProxyEndpoints,
    ProxyEndpointsWithRawResponse,
    AsyncProxyEndpointsWithRawResponse,
    ProxyEndpointsWithStreamingResponse,
    AsyncProxyEndpointsWithStreamingResponse,
)
from .audit_ssh_settings import (
    AuditSSHSettings,
    AsyncAuditSSHSettings,
    AuditSSHSettingsWithRawResponse,
    AsyncAuditSSHSettingsWithRawResponse,
    AuditSSHSettingsWithStreamingResponse,
    AsyncAuditSSHSettingsWithStreamingResponse,
)
from ....types.zero_trust import GatewayListResponse, GatewayCreateResponse

__all__ = ["Gateway", "AsyncGateway"]


class Gateway(SyncAPIResource):
    @cached_property
    def audit_ssh_settings(self) -> AuditSSHSettings:
        return AuditSSHSettings(self._client)

    @cached_property
    def categories(self) -> Categories:
        return Categories(self._client)

    @cached_property
    def app_types(self) -> AppTypes:
        return AppTypes(self._client)

    @cached_property
    def configurations(self) -> Configurations:
        return Configurations(self._client)

    @cached_property
    def lists(self) -> Lists:
        return Lists(self._client)

    @cached_property
    def locations(self) -> Locations:
        return Locations(self._client)

    @cached_property
    def logging(self) -> Logging:
        return Logging(self._client)

    @cached_property
    def proxy_endpoints(self) -> ProxyEndpoints:
        return ProxyEndpoints(self._client)

    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def with_raw_response(self) -> GatewayWithRawResponse:
        return GatewayWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GatewayWithStreamingResponse:
        return GatewayWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GatewayCreateResponse:
        """
        Creates a Zero Trust account with an existing Cloudflare account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/gateway",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GatewayCreateResponse], ResultWrapper[GatewayCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GatewayListResponse:
        """
        Gets information about the current Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/gateway",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GatewayListResponse], ResultWrapper[GatewayListResponse]),
        )


class AsyncGateway(AsyncAPIResource):
    @cached_property
    def audit_ssh_settings(self) -> AsyncAuditSSHSettings:
        return AsyncAuditSSHSettings(self._client)

    @cached_property
    def categories(self) -> AsyncCategories:
        return AsyncCategories(self._client)

    @cached_property
    def app_types(self) -> AsyncAppTypes:
        return AsyncAppTypes(self._client)

    @cached_property
    def configurations(self) -> AsyncConfigurations:
        return AsyncConfigurations(self._client)

    @cached_property
    def lists(self) -> AsyncLists:
        return AsyncLists(self._client)

    @cached_property
    def locations(self) -> AsyncLocations:
        return AsyncLocations(self._client)

    @cached_property
    def logging(self) -> AsyncLogging:
        return AsyncLogging(self._client)

    @cached_property
    def proxy_endpoints(self) -> AsyncProxyEndpoints:
        return AsyncProxyEndpoints(self._client)

    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGatewayWithRawResponse:
        return AsyncGatewayWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGatewayWithStreamingResponse:
        return AsyncGatewayWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GatewayCreateResponse:
        """
        Creates a Zero Trust account with an existing Cloudflare account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/gateway",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GatewayCreateResponse], ResultWrapper[GatewayCreateResponse]),
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GatewayListResponse:
        """
        Gets information about the current Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/gateway",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GatewayListResponse], ResultWrapper[GatewayListResponse]),
        )


class GatewayWithRawResponse:
    def __init__(self, gateway: Gateway) -> None:
        self._gateway = gateway

        self.create = to_raw_response_wrapper(
            gateway.create,
        )
        self.list = to_raw_response_wrapper(
            gateway.list,
        )

    @cached_property
    def audit_ssh_settings(self) -> AuditSSHSettingsWithRawResponse:
        return AuditSSHSettingsWithRawResponse(self._gateway.audit_ssh_settings)

    @cached_property
    def categories(self) -> CategoriesWithRawResponse:
        return CategoriesWithRawResponse(self._gateway.categories)

    @cached_property
    def app_types(self) -> AppTypesWithRawResponse:
        return AppTypesWithRawResponse(self._gateway.app_types)

    @cached_property
    def configurations(self) -> ConfigurationsWithRawResponse:
        return ConfigurationsWithRawResponse(self._gateway.configurations)

    @cached_property
    def lists(self) -> ListsWithRawResponse:
        return ListsWithRawResponse(self._gateway.lists)

    @cached_property
    def locations(self) -> LocationsWithRawResponse:
        return LocationsWithRawResponse(self._gateway.locations)

    @cached_property
    def logging(self) -> LoggingWithRawResponse:
        return LoggingWithRawResponse(self._gateway.logging)

    @cached_property
    def proxy_endpoints(self) -> ProxyEndpointsWithRawResponse:
        return ProxyEndpointsWithRawResponse(self._gateway.proxy_endpoints)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._gateway.rules)


class AsyncGatewayWithRawResponse:
    def __init__(self, gateway: AsyncGateway) -> None:
        self._gateway = gateway

        self.create = async_to_raw_response_wrapper(
            gateway.create,
        )
        self.list = async_to_raw_response_wrapper(
            gateway.list,
        )

    @cached_property
    def audit_ssh_settings(self) -> AsyncAuditSSHSettingsWithRawResponse:
        return AsyncAuditSSHSettingsWithRawResponse(self._gateway.audit_ssh_settings)

    @cached_property
    def categories(self) -> AsyncCategoriesWithRawResponse:
        return AsyncCategoriesWithRawResponse(self._gateway.categories)

    @cached_property
    def app_types(self) -> AsyncAppTypesWithRawResponse:
        return AsyncAppTypesWithRawResponse(self._gateway.app_types)

    @cached_property
    def configurations(self) -> AsyncConfigurationsWithRawResponse:
        return AsyncConfigurationsWithRawResponse(self._gateway.configurations)

    @cached_property
    def lists(self) -> AsyncListsWithRawResponse:
        return AsyncListsWithRawResponse(self._gateway.lists)

    @cached_property
    def locations(self) -> AsyncLocationsWithRawResponse:
        return AsyncLocationsWithRawResponse(self._gateway.locations)

    @cached_property
    def logging(self) -> AsyncLoggingWithRawResponse:
        return AsyncLoggingWithRawResponse(self._gateway.logging)

    @cached_property
    def proxy_endpoints(self) -> AsyncProxyEndpointsWithRawResponse:
        return AsyncProxyEndpointsWithRawResponse(self._gateway.proxy_endpoints)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._gateway.rules)


class GatewayWithStreamingResponse:
    def __init__(self, gateway: Gateway) -> None:
        self._gateway = gateway

        self.create = to_streamed_response_wrapper(
            gateway.create,
        )
        self.list = to_streamed_response_wrapper(
            gateway.list,
        )

    @cached_property
    def audit_ssh_settings(self) -> AuditSSHSettingsWithStreamingResponse:
        return AuditSSHSettingsWithStreamingResponse(self._gateway.audit_ssh_settings)

    @cached_property
    def categories(self) -> CategoriesWithStreamingResponse:
        return CategoriesWithStreamingResponse(self._gateway.categories)

    @cached_property
    def app_types(self) -> AppTypesWithStreamingResponse:
        return AppTypesWithStreamingResponse(self._gateway.app_types)

    @cached_property
    def configurations(self) -> ConfigurationsWithStreamingResponse:
        return ConfigurationsWithStreamingResponse(self._gateway.configurations)

    @cached_property
    def lists(self) -> ListsWithStreamingResponse:
        return ListsWithStreamingResponse(self._gateway.lists)

    @cached_property
    def locations(self) -> LocationsWithStreamingResponse:
        return LocationsWithStreamingResponse(self._gateway.locations)

    @cached_property
    def logging(self) -> LoggingWithStreamingResponse:
        return LoggingWithStreamingResponse(self._gateway.logging)

    @cached_property
    def proxy_endpoints(self) -> ProxyEndpointsWithStreamingResponse:
        return ProxyEndpointsWithStreamingResponse(self._gateway.proxy_endpoints)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._gateway.rules)


class AsyncGatewayWithStreamingResponse:
    def __init__(self, gateway: AsyncGateway) -> None:
        self._gateway = gateway

        self.create = async_to_streamed_response_wrapper(
            gateway.create,
        )
        self.list = async_to_streamed_response_wrapper(
            gateway.list,
        )

    @cached_property
    def audit_ssh_settings(self) -> AsyncAuditSSHSettingsWithStreamingResponse:
        return AsyncAuditSSHSettingsWithStreamingResponse(self._gateway.audit_ssh_settings)

    @cached_property
    def categories(self) -> AsyncCategoriesWithStreamingResponse:
        return AsyncCategoriesWithStreamingResponse(self._gateway.categories)

    @cached_property
    def app_types(self) -> AsyncAppTypesWithStreamingResponse:
        return AsyncAppTypesWithStreamingResponse(self._gateway.app_types)

    @cached_property
    def configurations(self) -> AsyncConfigurationsWithStreamingResponse:
        return AsyncConfigurationsWithStreamingResponse(self._gateway.configurations)

    @cached_property
    def lists(self) -> AsyncListsWithStreamingResponse:
        return AsyncListsWithStreamingResponse(self._gateway.lists)

    @cached_property
    def locations(self) -> AsyncLocationsWithStreamingResponse:
        return AsyncLocationsWithStreamingResponse(self._gateway.locations)

    @cached_property
    def logging(self) -> AsyncLoggingWithStreamingResponse:
        return AsyncLoggingWithStreamingResponse(self._gateway.logging)

    @cached_property
    def proxy_endpoints(self) -> AsyncProxyEndpointsWithStreamingResponse:
        return AsyncProxyEndpointsWithStreamingResponse(self._gateway.proxy_endpoints)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._gateway.rules)
