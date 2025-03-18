# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .cnis import (
    CNIsResource,
    AsyncCNIsResource,
    CNIsResourceWithRawResponse,
    AsyncCNIsResourceWithRawResponse,
    CNIsResourceWithStreamingResponse,
    AsyncCNIsResourceWithStreamingResponse,
)
from .slots import (
    SlotsResource,
    AsyncSlotsResource,
    SlotsResourceWithRawResponse,
    AsyncSlotsResourceWithRawResponse,
    SlotsResourceWithStreamingResponse,
    AsyncSlotsResourceWithStreamingResponse,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .interconnects import (
    InterconnectsResource,
    AsyncInterconnectsResource,
    InterconnectsResourceWithRawResponse,
    AsyncInterconnectsResourceWithRawResponse,
    InterconnectsResourceWithStreamingResponse,
    AsyncInterconnectsResourceWithStreamingResponse,
)

__all__ = ["NetworkInterconnectsResource", "AsyncNetworkInterconnectsResource"]


class NetworkInterconnectsResource(SyncAPIResource):
    @cached_property
    def cnis(self) -> CNIsResource:
        return CNIsResource(self._client)

    @cached_property
    def interconnects(self) -> InterconnectsResource:
        return InterconnectsResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def slots(self) -> SlotsResource:
        return SlotsResource(self._client)

    @cached_property
    def with_raw_response(self) -> NetworkInterconnectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return NetworkInterconnectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworkInterconnectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return NetworkInterconnectsResourceWithStreamingResponse(self)


class AsyncNetworkInterconnectsResource(AsyncAPIResource):
    @cached_property
    def cnis(self) -> AsyncCNIsResource:
        return AsyncCNIsResource(self._client)

    @cached_property
    def interconnects(self) -> AsyncInterconnectsResource:
        return AsyncInterconnectsResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def slots(self) -> AsyncSlotsResource:
        return AsyncSlotsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNetworkInterconnectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworkInterconnectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworkInterconnectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncNetworkInterconnectsResourceWithStreamingResponse(self)


class NetworkInterconnectsResourceWithRawResponse:
    def __init__(self, network_interconnects: NetworkInterconnectsResource) -> None:
        self._network_interconnects = network_interconnects

    @cached_property
    def cnis(self) -> CNIsResourceWithRawResponse:
        return CNIsResourceWithRawResponse(self._network_interconnects.cnis)

    @cached_property
    def interconnects(self) -> InterconnectsResourceWithRawResponse:
        return InterconnectsResourceWithRawResponse(self._network_interconnects.interconnects)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._network_interconnects.settings)

    @cached_property
    def slots(self) -> SlotsResourceWithRawResponse:
        return SlotsResourceWithRawResponse(self._network_interconnects.slots)


class AsyncNetworkInterconnectsResourceWithRawResponse:
    def __init__(self, network_interconnects: AsyncNetworkInterconnectsResource) -> None:
        self._network_interconnects = network_interconnects

    @cached_property
    def cnis(self) -> AsyncCNIsResourceWithRawResponse:
        return AsyncCNIsResourceWithRawResponse(self._network_interconnects.cnis)

    @cached_property
    def interconnects(self) -> AsyncInterconnectsResourceWithRawResponse:
        return AsyncInterconnectsResourceWithRawResponse(self._network_interconnects.interconnects)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._network_interconnects.settings)

    @cached_property
    def slots(self) -> AsyncSlotsResourceWithRawResponse:
        return AsyncSlotsResourceWithRawResponse(self._network_interconnects.slots)


class NetworkInterconnectsResourceWithStreamingResponse:
    def __init__(self, network_interconnects: NetworkInterconnectsResource) -> None:
        self._network_interconnects = network_interconnects

    @cached_property
    def cnis(self) -> CNIsResourceWithStreamingResponse:
        return CNIsResourceWithStreamingResponse(self._network_interconnects.cnis)

    @cached_property
    def interconnects(self) -> InterconnectsResourceWithStreamingResponse:
        return InterconnectsResourceWithStreamingResponse(self._network_interconnects.interconnects)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._network_interconnects.settings)

    @cached_property
    def slots(self) -> SlotsResourceWithStreamingResponse:
        return SlotsResourceWithStreamingResponse(self._network_interconnects.slots)


class AsyncNetworkInterconnectsResourceWithStreamingResponse:
    def __init__(self, network_interconnects: AsyncNetworkInterconnectsResource) -> None:
        self._network_interconnects = network_interconnects

    @cached_property
    def cnis(self) -> AsyncCNIsResourceWithStreamingResponse:
        return AsyncCNIsResourceWithStreamingResponse(self._network_interconnects.cnis)

    @cached_property
    def interconnects(self) -> AsyncInterconnectsResourceWithStreamingResponse:
        return AsyncInterconnectsResourceWithStreamingResponse(self._network_interconnects.interconnects)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._network_interconnects.settings)

    @cached_property
    def slots(self) -> AsyncSlotsResourceWithStreamingResponse:
        return AsyncSlotsResourceWithStreamingResponse(self._network_interconnects.slots)
