# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .packages import (
    PackagesResource,
    AsyncPackagesResource,
    PackagesResourceWithRawResponse,
    AsyncPackagesResourceWithRawResponse,
    PackagesResourceWithStreamingResponse,
    AsyncPackagesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .packages.packages import PackagesResource, AsyncPackagesResource

__all__ = ["WAFResource", "AsyncWAFResource"]


class WAFResource(SyncAPIResource):
    @cached_property
    def packages(self) -> PackagesResource:
        return PackagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> WAFResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return WAFResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WAFResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return WAFResourceWithStreamingResponse(self)


class AsyncWAFResource(AsyncAPIResource):
    @cached_property
    def packages(self) -> AsyncPackagesResource:
        return AsyncPackagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWAFResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWAFResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWAFResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncWAFResourceWithStreamingResponse(self)


class WAFResourceWithRawResponse:
    def __init__(self, waf: WAFResource) -> None:
        self._waf = waf

    @cached_property
    def packages(self) -> PackagesResourceWithRawResponse:
        return PackagesResourceWithRawResponse(self._waf.packages)


class AsyncWAFResourceWithRawResponse:
    def __init__(self, waf: AsyncWAFResource) -> None:
        self._waf = waf

    @cached_property
    def packages(self) -> AsyncPackagesResourceWithRawResponse:
        return AsyncPackagesResourceWithRawResponse(self._waf.packages)


class WAFResourceWithStreamingResponse:
    def __init__(self, waf: WAFResource) -> None:
        self._waf = waf

    @cached_property
    def packages(self) -> PackagesResourceWithStreamingResponse:
        return PackagesResourceWithStreamingResponse(self._waf.packages)


class AsyncWAFResourceWithStreamingResponse:
    def __init__(self, waf: AsyncWAFResource) -> None:
        self._waf = waf

    @cached_property
    def packages(self) -> AsyncPackagesResourceWithStreamingResponse:
        return AsyncPackagesResourceWithStreamingResponse(self._waf.packages)
