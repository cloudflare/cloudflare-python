# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .targets import (
    TargetsResource,
    AsyncTargetsResource,
    TargetsResourceWithRawResponse,
    AsyncTargetsResourceWithRawResponse,
    TargetsResourceWithStreamingResponse,
    AsyncTargetsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["InfrastructureResource", "AsyncInfrastructureResource"]


class InfrastructureResource(SyncAPIResource):
    @cached_property
    def targets(self) -> TargetsResource:
        return TargetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> InfrastructureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return InfrastructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InfrastructureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return InfrastructureResourceWithStreamingResponse(self)


class AsyncInfrastructureResource(AsyncAPIResource):
    @cached_property
    def targets(self) -> AsyncTargetsResource:
        return AsyncTargetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInfrastructureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInfrastructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInfrastructureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncInfrastructureResourceWithStreamingResponse(self)


class InfrastructureResourceWithRawResponse:
    def __init__(self, infrastructure: InfrastructureResource) -> None:
        self._infrastructure = infrastructure

    @cached_property
    def targets(self) -> TargetsResourceWithRawResponse:
        return TargetsResourceWithRawResponse(self._infrastructure.targets)


class AsyncInfrastructureResourceWithRawResponse:
    def __init__(self, infrastructure: AsyncInfrastructureResource) -> None:
        self._infrastructure = infrastructure

    @cached_property
    def targets(self) -> AsyncTargetsResourceWithRawResponse:
        return AsyncTargetsResourceWithRawResponse(self._infrastructure.targets)


class InfrastructureResourceWithStreamingResponse:
    def __init__(self, infrastructure: InfrastructureResource) -> None:
        self._infrastructure = infrastructure

    @cached_property
    def targets(self) -> TargetsResourceWithStreamingResponse:
        return TargetsResourceWithStreamingResponse(self._infrastructure.targets)


class AsyncInfrastructureResourceWithStreamingResponse:
    def __init__(self, infrastructure: AsyncInfrastructureResource) -> None:
        self._infrastructure = infrastructure

    @cached_property
    def targets(self) -> AsyncTargetsResourceWithStreamingResponse:
        return AsyncTargetsResourceWithStreamingResponse(self._infrastructure.targets)
