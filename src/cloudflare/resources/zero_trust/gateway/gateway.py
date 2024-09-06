# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .audit_ssh_settings import AuditSSHSettingsResource, AsyncAuditSSHSettingsResource

from ...._compat import cached_property

from .categories import CategoriesResource, AsyncCategoriesResource

from .app_types import AppTypesResource, AsyncAppTypesResource

from .configurations.configurations import ConfigurationsResource, AsyncConfigurationsResource

from .lists.lists import ListsResource, AsyncListsResource

from .locations import LocationsResource, AsyncLocationsResource

from .logging import LoggingResource, AsyncLoggingResource

from .proxy_endpoints import ProxyEndpointsResource, AsyncProxyEndpointsResource

from .rules import RulesResource, AsyncRulesResource

from .certificates import CertificatesResource, AsyncCertificatesResource

from ....types.zero_trust.gateway_create_response import GatewayCreateResponse

from ...._wrappers import ResultWrapper

from typing import Optional, Type

from ...._base_client import make_request_options

from ....types.zero_trust.gateway_list_response import GatewayListResponse

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .audit_ssh_settings import (
    AuditSSHSettingsResource,
    AsyncAuditSSHSettingsResource,
    AuditSSHSettingsResourceWithRawResponse,
    AsyncAuditSSHSettingsResourceWithRawResponse,
    AuditSSHSettingsResourceWithStreamingResponse,
    AsyncAuditSSHSettingsResourceWithStreamingResponse,
)
from .categories import (
    CategoriesResource,
    AsyncCategoriesResource,
    CategoriesResourceWithRawResponse,
    AsyncCategoriesResourceWithRawResponse,
    CategoriesResourceWithStreamingResponse,
    AsyncCategoriesResourceWithStreamingResponse,
)
from .app_types import (
    AppTypesResource,
    AsyncAppTypesResource,
    AppTypesResourceWithRawResponse,
    AsyncAppTypesResourceWithRawResponse,
    AppTypesResourceWithStreamingResponse,
    AsyncAppTypesResourceWithStreamingResponse,
)
from .configurations import (
    ConfigurationsResource,
    AsyncConfigurationsResource,
    ConfigurationsResourceWithRawResponse,
    AsyncConfigurationsResourceWithRawResponse,
    ConfigurationsResourceWithStreamingResponse,
    AsyncConfigurationsResourceWithStreamingResponse,
)
from .lists import (
    ListsResource,
    AsyncListsResource,
    ListsResourceWithRawResponse,
    AsyncListsResourceWithRawResponse,
    ListsResourceWithStreamingResponse,
    AsyncListsResourceWithStreamingResponse,
)
from .locations import (
    LocationsResource,
    AsyncLocationsResource,
    LocationsResourceWithRawResponse,
    AsyncLocationsResourceWithRawResponse,
    LocationsResourceWithStreamingResponse,
    AsyncLocationsResourceWithStreamingResponse,
)
from .logging import (
    LoggingResource,
    AsyncLoggingResource,
    LoggingResourceWithRawResponse,
    AsyncLoggingResourceWithRawResponse,
    LoggingResourceWithStreamingResponse,
    AsyncLoggingResourceWithStreamingResponse,
)
from .proxy_endpoints import (
    ProxyEndpointsResource,
    AsyncProxyEndpointsResource,
    ProxyEndpointsResourceWithRawResponse,
    AsyncProxyEndpointsResourceWithRawResponse,
    ProxyEndpointsResourceWithStreamingResponse,
    AsyncProxyEndpointsResourceWithStreamingResponse,
)
from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from .certificates import (
    CertificatesResource,
    AsyncCertificatesResource,
    CertificatesResourceWithRawResponse,
    AsyncCertificatesResourceWithRawResponse,
    CertificatesResourceWithStreamingResponse,
    AsyncCertificatesResourceWithStreamingResponse,
)
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["GatewayResource", "AsyncGatewayResource"]


class GatewayResource(SyncAPIResource):
    @cached_property
    def audit_ssh_settings(self) -> AuditSSHSettingsResource:
        return AuditSSHSettingsResource(self._client)

    @cached_property
    def categories(self) -> CategoriesResource:
        return CategoriesResource(self._client)

    @cached_property
    def app_types(self) -> AppTypesResource:
        return AppTypesResource(self._client)

    @cached_property
    def configurations(self) -> ConfigurationsResource:
        return ConfigurationsResource(self._client)

    @cached_property
    def lists(self) -> ListsResource:
        return ListsResource(self._client)

    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

    @cached_property
    def logging(self) -> LoggingResource:
        return LoggingResource(self._client)

    @cached_property
    def proxy_endpoints(self) -> ProxyEndpointsResource:
        return ProxyEndpointsResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def certificates(self) -> CertificatesResource:
        return CertificatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> GatewayResourceWithRawResponse:
        return GatewayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GatewayResourceWithStreamingResponse:
        return GatewayResourceWithStreamingResponse(self)

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
    ) -> Optional[GatewayCreateResponse]:
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
                post_parser=ResultWrapper[Optional[GatewayCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayCreateResponse]], ResultWrapper[GatewayCreateResponse]),
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
    ) -> Optional[GatewayListResponse]:
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
                post_parser=ResultWrapper[Optional[GatewayListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayListResponse]], ResultWrapper[GatewayListResponse]),
        )


class AsyncGatewayResource(AsyncAPIResource):
    @cached_property
    def audit_ssh_settings(self) -> AsyncAuditSSHSettingsResource:
        return AsyncAuditSSHSettingsResource(self._client)

    @cached_property
    def categories(self) -> AsyncCategoriesResource:
        return AsyncCategoriesResource(self._client)

    @cached_property
    def app_types(self) -> AsyncAppTypesResource:
        return AsyncAppTypesResource(self._client)

    @cached_property
    def configurations(self) -> AsyncConfigurationsResource:
        return AsyncConfigurationsResource(self._client)

    @cached_property
    def lists(self) -> AsyncListsResource:
        return AsyncListsResource(self._client)

    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

    @cached_property
    def logging(self) -> AsyncLoggingResource:
        return AsyncLoggingResource(self._client)

    @cached_property
    def proxy_endpoints(self) -> AsyncProxyEndpointsResource:
        return AsyncProxyEndpointsResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def certificates(self) -> AsyncCertificatesResource:
        return AsyncCertificatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGatewayResourceWithRawResponse:
        return AsyncGatewayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGatewayResourceWithStreamingResponse:
        return AsyncGatewayResourceWithStreamingResponse(self)

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
    ) -> Optional[GatewayCreateResponse]:
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
                post_parser=ResultWrapper[Optional[GatewayCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayCreateResponse]], ResultWrapper[GatewayCreateResponse]),
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
    ) -> Optional[GatewayListResponse]:
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
                post_parser=ResultWrapper[Optional[GatewayListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayListResponse]], ResultWrapper[GatewayListResponse]),
        )


class GatewayResourceWithRawResponse:
    def __init__(self, gateway: GatewayResource) -> None:
        self._gateway = gateway

        self.create = to_raw_response_wrapper(
            gateway.create,
        )
        self.list = to_raw_response_wrapper(
            gateway.list,
        )

    @cached_property
    def audit_ssh_settings(self) -> AuditSSHSettingsResourceWithRawResponse:
        return AuditSSHSettingsResourceWithRawResponse(self._gateway.audit_ssh_settings)

    @cached_property
    def categories(self) -> CategoriesResourceWithRawResponse:
        return CategoriesResourceWithRawResponse(self._gateway.categories)

    @cached_property
    def app_types(self) -> AppTypesResourceWithRawResponse:
        return AppTypesResourceWithRawResponse(self._gateway.app_types)

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithRawResponse:
        return ConfigurationsResourceWithRawResponse(self._gateway.configurations)

    @cached_property
    def lists(self) -> ListsResourceWithRawResponse:
        return ListsResourceWithRawResponse(self._gateway.lists)

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._gateway.locations)

    @cached_property
    def logging(self) -> LoggingResourceWithRawResponse:
        return LoggingResourceWithRawResponse(self._gateway.logging)

    @cached_property
    def proxy_endpoints(self) -> ProxyEndpointsResourceWithRawResponse:
        return ProxyEndpointsResourceWithRawResponse(self._gateway.proxy_endpoints)

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._gateway.rules)

    @cached_property
    def certificates(self) -> CertificatesResourceWithRawResponse:
        return CertificatesResourceWithRawResponse(self._gateway.certificates)


class AsyncGatewayResourceWithRawResponse:
    def __init__(self, gateway: AsyncGatewayResource) -> None:
        self._gateway = gateway

        self.create = async_to_raw_response_wrapper(
            gateway.create,
        )
        self.list = async_to_raw_response_wrapper(
            gateway.list,
        )

    @cached_property
    def audit_ssh_settings(self) -> AsyncAuditSSHSettingsResourceWithRawResponse:
        return AsyncAuditSSHSettingsResourceWithRawResponse(self._gateway.audit_ssh_settings)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithRawResponse:
        return AsyncCategoriesResourceWithRawResponse(self._gateway.categories)

    @cached_property
    def app_types(self) -> AsyncAppTypesResourceWithRawResponse:
        return AsyncAppTypesResourceWithRawResponse(self._gateway.app_types)

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithRawResponse:
        return AsyncConfigurationsResourceWithRawResponse(self._gateway.configurations)

    @cached_property
    def lists(self) -> AsyncListsResourceWithRawResponse:
        return AsyncListsResourceWithRawResponse(self._gateway.lists)

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._gateway.locations)

    @cached_property
    def logging(self) -> AsyncLoggingResourceWithRawResponse:
        return AsyncLoggingResourceWithRawResponse(self._gateway.logging)

    @cached_property
    def proxy_endpoints(self) -> AsyncProxyEndpointsResourceWithRawResponse:
        return AsyncProxyEndpointsResourceWithRawResponse(self._gateway.proxy_endpoints)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._gateway.rules)

    @cached_property
    def certificates(self) -> AsyncCertificatesResourceWithRawResponse:
        return AsyncCertificatesResourceWithRawResponse(self._gateway.certificates)


class GatewayResourceWithStreamingResponse:
    def __init__(self, gateway: GatewayResource) -> None:
        self._gateway = gateway

        self.create = to_streamed_response_wrapper(
            gateway.create,
        )
        self.list = to_streamed_response_wrapper(
            gateway.list,
        )

    @cached_property
    def audit_ssh_settings(self) -> AuditSSHSettingsResourceWithStreamingResponse:
        return AuditSSHSettingsResourceWithStreamingResponse(self._gateway.audit_ssh_settings)

    @cached_property
    def categories(self) -> CategoriesResourceWithStreamingResponse:
        return CategoriesResourceWithStreamingResponse(self._gateway.categories)

    @cached_property
    def app_types(self) -> AppTypesResourceWithStreamingResponse:
        return AppTypesResourceWithStreamingResponse(self._gateway.app_types)

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithStreamingResponse:
        return ConfigurationsResourceWithStreamingResponse(self._gateway.configurations)

    @cached_property
    def lists(self) -> ListsResourceWithStreamingResponse:
        return ListsResourceWithStreamingResponse(self._gateway.lists)

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._gateway.locations)

    @cached_property
    def logging(self) -> LoggingResourceWithStreamingResponse:
        return LoggingResourceWithStreamingResponse(self._gateway.logging)

    @cached_property
    def proxy_endpoints(self) -> ProxyEndpointsResourceWithStreamingResponse:
        return ProxyEndpointsResourceWithStreamingResponse(self._gateway.proxy_endpoints)

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._gateway.rules)

    @cached_property
    def certificates(self) -> CertificatesResourceWithStreamingResponse:
        return CertificatesResourceWithStreamingResponse(self._gateway.certificates)


class AsyncGatewayResourceWithStreamingResponse:
    def __init__(self, gateway: AsyncGatewayResource) -> None:
        self._gateway = gateway

        self.create = async_to_streamed_response_wrapper(
            gateway.create,
        )
        self.list = async_to_streamed_response_wrapper(
            gateway.list,
        )

    @cached_property
    def audit_ssh_settings(self) -> AsyncAuditSSHSettingsResourceWithStreamingResponse:
        return AsyncAuditSSHSettingsResourceWithStreamingResponse(self._gateway.audit_ssh_settings)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithStreamingResponse:
        return AsyncCategoriesResourceWithStreamingResponse(self._gateway.categories)

    @cached_property
    def app_types(self) -> AsyncAppTypesResourceWithStreamingResponse:
        return AsyncAppTypesResourceWithStreamingResponse(self._gateway.app_types)

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        return AsyncConfigurationsResourceWithStreamingResponse(self._gateway.configurations)

    @cached_property
    def lists(self) -> AsyncListsResourceWithStreamingResponse:
        return AsyncListsResourceWithStreamingResponse(self._gateway.lists)

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._gateway.locations)

    @cached_property
    def logging(self) -> AsyncLoggingResourceWithStreamingResponse:
        return AsyncLoggingResourceWithStreamingResponse(self._gateway.logging)

    @cached_property
    def proxy_endpoints(self) -> AsyncProxyEndpointsResourceWithStreamingResponse:
        return AsyncProxyEndpointsResourceWithStreamingResponse(self._gateway.proxy_endpoints)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._gateway.rules)

    @cached_property
    def certificates(self) -> AsyncCertificatesResourceWithStreamingResponse:
        return AsyncCertificatesResourceWithStreamingResponse(self._gateway.certificates)
