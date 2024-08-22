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
from .overrides import (
    OverridesResource,
    AsyncOverridesResource,
    OverridesResourceWithRawResponse,
    AsyncOverridesResourceWithRawResponse,
    OverridesResourceWithStreamingResponse,
    AsyncOverridesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .packages.packages import PackagesResource, AsyncPackagesResource

__all__ = ["WAFResource", "AsyncWAFResource"]


class WAFResource(SyncAPIResource):
    @cached_property
    def overrides(self) -> OverridesResource:
        return OverridesResource(self._client)

    @cached_property
    def packages(self) -> PackagesResource:
        return PackagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> WAFResourceWithRawResponse:
        return WAFResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WAFResourceWithStreamingResponse:
        return WAFResourceWithStreamingResponse(self)


class AsyncWAFResource(AsyncAPIResource):
    @cached_property
    def overrides(self) -> AsyncOverridesResource:
        return AsyncOverridesResource(self._client)

    @cached_property
    def packages(self) -> AsyncPackagesResource:
        return AsyncPackagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWAFResourceWithRawResponse:
        return AsyncWAFResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWAFResourceWithStreamingResponse:
        return AsyncWAFResourceWithStreamingResponse(self)


class WAFResourceWithRawResponse:
    def __init__(self, waf: WAFResource) -> None:
        self._waf = waf

    @cached_property
    def overrides(self) -> OverridesResourceWithRawResponse:
        return OverridesResourceWithRawResponse(self._waf.overrides)

    @cached_property
    def packages(self) -> PackagesResourceWithRawResponse:
        return PackagesResourceWithRawResponse(self._waf.packages)


class AsyncWAFResourceWithRawResponse:
    def __init__(self, waf: AsyncWAFResource) -> None:
        self._waf = waf

    @cached_property
    def overrides(self) -> AsyncOverridesResourceWithRawResponse:
        return AsyncOverridesResourceWithRawResponse(self._waf.overrides)

    @cached_property
    def packages(self) -> AsyncPackagesResourceWithRawResponse:
        return AsyncPackagesResourceWithRawResponse(self._waf.packages)


class WAFResourceWithStreamingResponse:
    def __init__(self, waf: WAFResource) -> None:
        self._waf = waf

    @cached_property
    def overrides(self) -> OverridesResourceWithStreamingResponse:
        return OverridesResourceWithStreamingResponse(self._waf.overrides)

    @cached_property
    def packages(self) -> PackagesResourceWithStreamingResponse:
        return PackagesResourceWithStreamingResponse(self._waf.packages)


class AsyncWAFResourceWithStreamingResponse:
    def __init__(self, waf: AsyncWAFResource) -> None:
        self._waf = waf

    @cached_property
    def overrides(self) -> AsyncOverridesResourceWithStreamingResponse:
        return AsyncOverridesResourceWithStreamingResponse(self._waf.overrides)

    @cached_property
    def packages(self) -> AsyncPackagesResourceWithStreamingResponse:
        return AsyncPackagesResourceWithStreamingResponse(self._waf.packages)
