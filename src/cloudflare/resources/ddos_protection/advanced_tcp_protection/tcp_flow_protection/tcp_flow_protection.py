# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from .rules.rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from .filters.filters import (
    FiltersResource,
    AsyncFiltersResource,
    FiltersResourceWithRawResponse,
    AsyncFiltersResourceWithRawResponse,
    FiltersResourceWithStreamingResponse,
    AsyncFiltersResourceWithStreamingResponse,
)

__all__ = ["TCPFlowProtectionResource", "AsyncTCPFlowProtectionResource"]


class TCPFlowProtectionResource(SyncAPIResource):
    @cached_property
    def filters(self) -> FiltersResource:
        return FiltersResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TCPFlowProtectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TCPFlowProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TCPFlowProtectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TCPFlowProtectionResourceWithStreamingResponse(self)


class AsyncTCPFlowProtectionResource(AsyncAPIResource):
    @cached_property
    def filters(self) -> AsyncFiltersResource:
        return AsyncFiltersResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTCPFlowProtectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTCPFlowProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTCPFlowProtectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTCPFlowProtectionResourceWithStreamingResponse(self)


class TCPFlowProtectionResourceWithRawResponse:
    def __init__(self, tcp_flow_protection: TCPFlowProtectionResource) -> None:
        self._tcp_flow_protection = tcp_flow_protection

    @cached_property
    def filters(self) -> FiltersResourceWithRawResponse:
        return FiltersResourceWithRawResponse(self._tcp_flow_protection.filters)

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._tcp_flow_protection.rules)


class AsyncTCPFlowProtectionResourceWithRawResponse:
    def __init__(self, tcp_flow_protection: AsyncTCPFlowProtectionResource) -> None:
        self._tcp_flow_protection = tcp_flow_protection

    @cached_property
    def filters(self) -> AsyncFiltersResourceWithRawResponse:
        return AsyncFiltersResourceWithRawResponse(self._tcp_flow_protection.filters)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._tcp_flow_protection.rules)


class TCPFlowProtectionResourceWithStreamingResponse:
    def __init__(self, tcp_flow_protection: TCPFlowProtectionResource) -> None:
        self._tcp_flow_protection = tcp_flow_protection

    @cached_property
    def filters(self) -> FiltersResourceWithStreamingResponse:
        return FiltersResourceWithStreamingResponse(self._tcp_flow_protection.filters)

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._tcp_flow_protection.rules)


class AsyncTCPFlowProtectionResourceWithStreamingResponse:
    def __init__(self, tcp_flow_protection: AsyncTCPFlowProtectionResource) -> None:
        self._tcp_flow_protection = tcp_flow_protection

    @cached_property
    def filters(self) -> AsyncFiltersResourceWithStreamingResponse:
        return AsyncFiltersResourceWithStreamingResponse(self._tcp_flow_protection.filters)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._tcp_flow_protection.rules)
