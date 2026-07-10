# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .configs import (
    ConfigsResource,
    AsyncConfigsResource,
    ConfigsResourceWithRawResponse,
    AsyncConfigsResourceWithRawResponse,
    ConfigsResourceWithStreamingResponse,
    AsyncConfigsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["HyperdriveResource", "AsyncHyperdriveResource"]


class HyperdriveResource(SyncAPIResource):
    @cached_property
    def configs(self) -> ConfigsResource:
        return ConfigsResource(self._client)

    @cached_property
    def with_raw_response(self) -> HyperdriveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return HyperdriveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HyperdriveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return HyperdriveResourceWithStreamingResponse(self)


class AsyncHyperdriveResource(AsyncAPIResource):
    @cached_property
    def configs(self) -> AsyncConfigsResource:
        return AsyncConfigsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHyperdriveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHyperdriveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHyperdriveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncHyperdriveResourceWithStreamingResponse(self)


class HyperdriveResourceWithRawResponse:
    def __init__(self, hyperdrive: HyperdriveResource) -> None:
        self._hyperdrive = hyperdrive

    @cached_property
    def configs(self) -> ConfigsResourceWithRawResponse:
        return ConfigsResourceWithRawResponse(self._hyperdrive.configs)


class AsyncHyperdriveResourceWithRawResponse:
    def __init__(self, hyperdrive: AsyncHyperdriveResource) -> None:
        self._hyperdrive = hyperdrive

    @cached_property
    def configs(self) -> AsyncConfigsResourceWithRawResponse:
        return AsyncConfigsResourceWithRawResponse(self._hyperdrive.configs)


class HyperdriveResourceWithStreamingResponse:
    def __init__(self, hyperdrive: HyperdriveResource) -> None:
        self._hyperdrive = hyperdrive

    @cached_property
    def configs(self) -> ConfigsResourceWithStreamingResponse:
        return ConfigsResourceWithStreamingResponse(self._hyperdrive.configs)


class AsyncHyperdriveResourceWithStreamingResponse:
    def __init__(self, hyperdrive: AsyncHyperdriveResource) -> None:
        self._hyperdrive = hyperdrive

    @cached_property
    def configs(self) -> AsyncConfigsResourceWithStreamingResponse:
        return AsyncConfigsResourceWithStreamingResponse(self._hyperdrive.configs)
