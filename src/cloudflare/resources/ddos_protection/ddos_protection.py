# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .advanced_tcp_protection.advanced_tcp_protection import (
    AdvancedTCPProtectionResource,
    AsyncAdvancedTCPProtectionResource,
    AdvancedTCPProtectionResourceWithRawResponse,
    AsyncAdvancedTCPProtectionResourceWithRawResponse,
    AdvancedTCPProtectionResourceWithStreamingResponse,
    AsyncAdvancedTCPProtectionResourceWithStreamingResponse,
)

__all__ = ["DDoSProtectionResource", "AsyncDDoSProtectionResource"]


class DDoSProtectionResource(SyncAPIResource):
    @cached_property
    def advanced_tcp_protection(self) -> AdvancedTCPProtectionResource:
        return AdvancedTCPProtectionResource(self._client)

    @cached_property
    def with_raw_response(self) -> DDoSProtectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DDoSProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DDoSProtectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DDoSProtectionResourceWithStreamingResponse(self)


class AsyncDDoSProtectionResource(AsyncAPIResource):
    @cached_property
    def advanced_tcp_protection(self) -> AsyncAdvancedTCPProtectionResource:
        return AsyncAdvancedTCPProtectionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDDoSProtectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDDoSProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDDoSProtectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDDoSProtectionResourceWithStreamingResponse(self)


class DDoSProtectionResourceWithRawResponse:
    def __init__(self, ddos_protection: DDoSProtectionResource) -> None:
        self._ddos_protection = ddos_protection

    @cached_property
    def advanced_tcp_protection(self) -> AdvancedTCPProtectionResourceWithRawResponse:
        return AdvancedTCPProtectionResourceWithRawResponse(self._ddos_protection.advanced_tcp_protection)


class AsyncDDoSProtectionResourceWithRawResponse:
    def __init__(self, ddos_protection: AsyncDDoSProtectionResource) -> None:
        self._ddos_protection = ddos_protection

    @cached_property
    def advanced_tcp_protection(self) -> AsyncAdvancedTCPProtectionResourceWithRawResponse:
        return AsyncAdvancedTCPProtectionResourceWithRawResponse(self._ddos_protection.advanced_tcp_protection)


class DDoSProtectionResourceWithStreamingResponse:
    def __init__(self, ddos_protection: DDoSProtectionResource) -> None:
        self._ddos_protection = ddos_protection

    @cached_property
    def advanced_tcp_protection(self) -> AdvancedTCPProtectionResourceWithStreamingResponse:
        return AdvancedTCPProtectionResourceWithStreamingResponse(self._ddos_protection.advanced_tcp_protection)


class AsyncDDoSProtectionResourceWithStreamingResponse:
    def __init__(self, ddos_protection: AsyncDDoSProtectionResource) -> None:
        self._ddos_protection = ddos_protection

    @cached_property
    def advanced_tcp_protection(self) -> AsyncAdvancedTCPProtectionResourceWithStreamingResponse:
        return AsyncAdvancedTCPProtectionResourceWithStreamingResponse(self._ddos_protection.advanced_tcp_protection)
