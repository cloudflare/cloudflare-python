# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .unique_devices import (
    UniqueDevicesResource,
    AsyncUniqueDevicesResource,
    UniqueDevicesResourceWithRawResponse,
    AsyncUniqueDevicesResourceWithRawResponse,
    UniqueDevicesResourceWithStreamingResponse,
    AsyncUniqueDevicesResourceWithStreamingResponse,
)

__all__ = ["TestsResource", "AsyncTestsResource"]


class TestsResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def unique_devices(self) -> UniqueDevicesResource:
        return UniqueDevicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TestsResourceWithStreamingResponse(self)


class AsyncTestsResource(AsyncAPIResource):
    @cached_property
    def unique_devices(self) -> AsyncUniqueDevicesResource:
        return AsyncUniqueDevicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTestsResourceWithStreamingResponse(self)


class TestsResourceWithRawResponse:
    __test__ = False

    def __init__(self, tests: TestsResource) -> None:
        self._tests = tests

    @cached_property
    def unique_devices(self) -> UniqueDevicesResourceWithRawResponse:
        return UniqueDevicesResourceWithRawResponse(self._tests.unique_devices)


class AsyncTestsResourceWithRawResponse:
    def __init__(self, tests: AsyncTestsResource) -> None:
        self._tests = tests

    @cached_property
    def unique_devices(self) -> AsyncUniqueDevicesResourceWithRawResponse:
        return AsyncUniqueDevicesResourceWithRawResponse(self._tests.unique_devices)


class TestsResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, tests: TestsResource) -> None:
        self._tests = tests

    @cached_property
    def unique_devices(self) -> UniqueDevicesResourceWithStreamingResponse:
        return UniqueDevicesResourceWithStreamingResponse(self._tests.unique_devices)


class AsyncTestsResourceWithStreamingResponse:
    def __init__(self, tests: AsyncTestsResource) -> None:
        self._tests = tests

    @cached_property
    def unique_devices(self) -> AsyncUniqueDevicesResourceWithStreamingResponse:
        return AsyncUniqueDevicesResourceWithStreamingResponse(self._tests.unique_devices)
