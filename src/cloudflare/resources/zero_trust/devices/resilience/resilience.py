# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .global_warp_override import (
    GlobalWARPOverrideResource,
    AsyncGlobalWARPOverrideResource,
    GlobalWARPOverrideResourceWithRawResponse,
    AsyncGlobalWARPOverrideResourceWithRawResponse,
    GlobalWARPOverrideResourceWithStreamingResponse,
    AsyncGlobalWARPOverrideResourceWithStreamingResponse,
)

__all__ = ["ResilienceResource", "AsyncResilienceResource"]


class ResilienceResource(SyncAPIResource):
    @cached_property
    def global_warp_override(self) -> GlobalWARPOverrideResource:
        return GlobalWARPOverrideResource(self._client)

    @cached_property
    def with_raw_response(self) -> ResilienceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ResilienceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResilienceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ResilienceResourceWithStreamingResponse(self)


class AsyncResilienceResource(AsyncAPIResource):
    @cached_property
    def global_warp_override(self) -> AsyncGlobalWARPOverrideResource:
        return AsyncGlobalWARPOverrideResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncResilienceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResilienceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResilienceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncResilienceResourceWithStreamingResponse(self)


class ResilienceResourceWithRawResponse:
    def __init__(self, resilience: ResilienceResource) -> None:
        self._resilience = resilience

    @cached_property
    def global_warp_override(self) -> GlobalWARPOverrideResourceWithRawResponse:
        return GlobalWARPOverrideResourceWithRawResponse(self._resilience.global_warp_override)


class AsyncResilienceResourceWithRawResponse:
    def __init__(self, resilience: AsyncResilienceResource) -> None:
        self._resilience = resilience

    @cached_property
    def global_warp_override(self) -> AsyncGlobalWARPOverrideResourceWithRawResponse:
        return AsyncGlobalWARPOverrideResourceWithRawResponse(self._resilience.global_warp_override)


class ResilienceResourceWithStreamingResponse:
    def __init__(self, resilience: ResilienceResource) -> None:
        self._resilience = resilience

    @cached_property
    def global_warp_override(self) -> GlobalWARPOverrideResourceWithStreamingResponse:
        return GlobalWARPOverrideResourceWithStreamingResponse(self._resilience.global_warp_override)


class AsyncResilienceResourceWithStreamingResponse:
    def __init__(self, resilience: AsyncResilienceResource) -> None:
        self._resilience = resilience

    @cached_property
    def global_warp_override(self) -> AsyncGlobalWARPOverrideResourceWithStreamingResponse:
        return AsyncGlobalWARPOverrideResourceWithStreamingResponse(self._resilience.global_warp_override)
