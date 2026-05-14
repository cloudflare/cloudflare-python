# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .status import (
    StatusResource,
    AsyncStatusResource,
    StatusResourceWithRawResponse,
    AsyncStatusResourceWithRawResponse,
    StatusResourceWithStreamingResponse,
    AsyncStatusResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .prefixes.prefixes import (
    PrefixesResource,
    AsyncPrefixesResource,
    PrefixesResourceWithRawResponse,
    AsyncPrefixesResourceWithRawResponse,
    PrefixesResourceWithStreamingResponse,
    AsyncPrefixesResourceWithStreamingResponse,
)
from .allowlist.allowlist import (
    AllowlistResource,
    AsyncAllowlistResource,
    AllowlistResourceWithRawResponse,
    AsyncAllowlistResourceWithRawResponse,
    AllowlistResourceWithStreamingResponse,
    AsyncAllowlistResourceWithStreamingResponse,
)
from .syn_protection.syn_protection import (
    SynProtectionResource,
    AsyncSynProtectionResource,
    SynProtectionResourceWithRawResponse,
    AsyncSynProtectionResourceWithRawResponse,
    SynProtectionResourceWithStreamingResponse,
    AsyncSynProtectionResourceWithStreamingResponse,
)
from .tcp_flow_protection.tcp_flow_protection import (
    TCPFlowProtectionResource,
    AsyncTCPFlowProtectionResource,
    TCPFlowProtectionResourceWithRawResponse,
    AsyncTCPFlowProtectionResourceWithRawResponse,
    TCPFlowProtectionResourceWithStreamingResponse,
    AsyncTCPFlowProtectionResourceWithStreamingResponse,
)

__all__ = ["AdvancedTCPProtectionResource", "AsyncAdvancedTCPProtectionResource"]


class AdvancedTCPProtectionResource(SyncAPIResource):
    @cached_property
    def allowlist(self) -> AllowlistResource:
        return AllowlistResource(self._client)

    @cached_property
    def prefixes(self) -> PrefixesResource:
        return PrefixesResource(self._client)

    @cached_property
    def syn_protection(self) -> SynProtectionResource:
        return SynProtectionResource(self._client)

    @cached_property
    def tcp_flow_protection(self) -> TCPFlowProtectionResource:
        return TCPFlowProtectionResource(self._client)

    @cached_property
    def status(self) -> StatusResource:
        return StatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdvancedTCPProtectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AdvancedTCPProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdvancedTCPProtectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AdvancedTCPProtectionResourceWithStreamingResponse(self)


class AsyncAdvancedTCPProtectionResource(AsyncAPIResource):
    @cached_property
    def allowlist(self) -> AsyncAllowlistResource:
        return AsyncAllowlistResource(self._client)

    @cached_property
    def prefixes(self) -> AsyncPrefixesResource:
        return AsyncPrefixesResource(self._client)

    @cached_property
    def syn_protection(self) -> AsyncSynProtectionResource:
        return AsyncSynProtectionResource(self._client)

    @cached_property
    def tcp_flow_protection(self) -> AsyncTCPFlowProtectionResource:
        return AsyncTCPFlowProtectionResource(self._client)

    @cached_property
    def status(self) -> AsyncStatusResource:
        return AsyncStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdvancedTCPProtectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdvancedTCPProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdvancedTCPProtectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAdvancedTCPProtectionResourceWithStreamingResponse(self)


class AdvancedTCPProtectionResourceWithRawResponse:
    def __init__(self, advanced_tcp_protection: AdvancedTCPProtectionResource) -> None:
        self._advanced_tcp_protection = advanced_tcp_protection

    @cached_property
    def allowlist(self) -> AllowlistResourceWithRawResponse:
        return AllowlistResourceWithRawResponse(self._advanced_tcp_protection.allowlist)

    @cached_property
    def prefixes(self) -> PrefixesResourceWithRawResponse:
        return PrefixesResourceWithRawResponse(self._advanced_tcp_protection.prefixes)

    @cached_property
    def syn_protection(self) -> SynProtectionResourceWithRawResponse:
        return SynProtectionResourceWithRawResponse(self._advanced_tcp_protection.syn_protection)

    @cached_property
    def tcp_flow_protection(self) -> TCPFlowProtectionResourceWithRawResponse:
        return TCPFlowProtectionResourceWithRawResponse(self._advanced_tcp_protection.tcp_flow_protection)

    @cached_property
    def status(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self._advanced_tcp_protection.status)


class AsyncAdvancedTCPProtectionResourceWithRawResponse:
    def __init__(self, advanced_tcp_protection: AsyncAdvancedTCPProtectionResource) -> None:
        self._advanced_tcp_protection = advanced_tcp_protection

    @cached_property
    def allowlist(self) -> AsyncAllowlistResourceWithRawResponse:
        return AsyncAllowlistResourceWithRawResponse(self._advanced_tcp_protection.allowlist)

    @cached_property
    def prefixes(self) -> AsyncPrefixesResourceWithRawResponse:
        return AsyncPrefixesResourceWithRawResponse(self._advanced_tcp_protection.prefixes)

    @cached_property
    def syn_protection(self) -> AsyncSynProtectionResourceWithRawResponse:
        return AsyncSynProtectionResourceWithRawResponse(self._advanced_tcp_protection.syn_protection)

    @cached_property
    def tcp_flow_protection(self) -> AsyncTCPFlowProtectionResourceWithRawResponse:
        return AsyncTCPFlowProtectionResourceWithRawResponse(self._advanced_tcp_protection.tcp_flow_protection)

    @cached_property
    def status(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self._advanced_tcp_protection.status)


class AdvancedTCPProtectionResourceWithStreamingResponse:
    def __init__(self, advanced_tcp_protection: AdvancedTCPProtectionResource) -> None:
        self._advanced_tcp_protection = advanced_tcp_protection

    @cached_property
    def allowlist(self) -> AllowlistResourceWithStreamingResponse:
        return AllowlistResourceWithStreamingResponse(self._advanced_tcp_protection.allowlist)

    @cached_property
    def prefixes(self) -> PrefixesResourceWithStreamingResponse:
        return PrefixesResourceWithStreamingResponse(self._advanced_tcp_protection.prefixes)

    @cached_property
    def syn_protection(self) -> SynProtectionResourceWithStreamingResponse:
        return SynProtectionResourceWithStreamingResponse(self._advanced_tcp_protection.syn_protection)

    @cached_property
    def tcp_flow_protection(self) -> TCPFlowProtectionResourceWithStreamingResponse:
        return TCPFlowProtectionResourceWithStreamingResponse(self._advanced_tcp_protection.tcp_flow_protection)

    @cached_property
    def status(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self._advanced_tcp_protection.status)


class AsyncAdvancedTCPProtectionResourceWithStreamingResponse:
    def __init__(self, advanced_tcp_protection: AsyncAdvancedTCPProtectionResource) -> None:
        self._advanced_tcp_protection = advanced_tcp_protection

    @cached_property
    def allowlist(self) -> AsyncAllowlistResourceWithStreamingResponse:
        return AsyncAllowlistResourceWithStreamingResponse(self._advanced_tcp_protection.allowlist)

    @cached_property
    def prefixes(self) -> AsyncPrefixesResourceWithStreamingResponse:
        return AsyncPrefixesResourceWithStreamingResponse(self._advanced_tcp_protection.prefixes)

    @cached_property
    def syn_protection(self) -> AsyncSynProtectionResourceWithStreamingResponse:
        return AsyncSynProtectionResourceWithStreamingResponse(self._advanced_tcp_protection.syn_protection)

    @cached_property
    def tcp_flow_protection(self) -> AsyncTCPFlowProtectionResourceWithStreamingResponse:
        return AsyncTCPFlowProtectionResourceWithStreamingResponse(self._advanced_tcp_protection.tcp_flow_protection)

    @cached_property
    def status(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self._advanced_tcp_protection.status)
