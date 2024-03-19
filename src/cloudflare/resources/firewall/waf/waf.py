# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .packages import (
    Packages,
    AsyncPackages,
    PackagesWithRawResponse,
    AsyncPackagesWithRawResponse,
    PackagesWithStreamingResponse,
    AsyncPackagesWithStreamingResponse,
)
from .overrides import (
    Overrides,
    AsyncOverrides,
    OverridesWithRawResponse,
    AsyncOverridesWithRawResponse,
    OverridesWithStreamingResponse,
    AsyncOverridesWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .packages.packages import Packages, AsyncPackages

__all__ = ["WAF", "AsyncWAF"]


class WAF(SyncAPIResource):
    @cached_property
    def overrides(self) -> Overrides:
        return Overrides(self._client)

    @cached_property
    def packages(self) -> Packages:
        return Packages(self._client)

    @cached_property
    def with_raw_response(self) -> WAFWithRawResponse:
        return WAFWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WAFWithStreamingResponse:
        return WAFWithStreamingResponse(self)


class AsyncWAF(AsyncAPIResource):
    @cached_property
    def overrides(self) -> AsyncOverrides:
        return AsyncOverrides(self._client)

    @cached_property
    def packages(self) -> AsyncPackages:
        return AsyncPackages(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWAFWithRawResponse:
        return AsyncWAFWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWAFWithStreamingResponse:
        return AsyncWAFWithStreamingResponse(self)


class WAFWithRawResponse:
    def __init__(self, waf: WAF) -> None:
        self._waf = waf

    @cached_property
    def overrides(self) -> OverridesWithRawResponse:
        return OverridesWithRawResponse(self._waf.overrides)

    @cached_property
    def packages(self) -> PackagesWithRawResponse:
        return PackagesWithRawResponse(self._waf.packages)


class AsyncWAFWithRawResponse:
    def __init__(self, waf: AsyncWAF) -> None:
        self._waf = waf

    @cached_property
    def overrides(self) -> AsyncOverridesWithRawResponse:
        return AsyncOverridesWithRawResponse(self._waf.overrides)

    @cached_property
    def packages(self) -> AsyncPackagesWithRawResponse:
        return AsyncPackagesWithRawResponse(self._waf.packages)


class WAFWithStreamingResponse:
    def __init__(self, waf: WAF) -> None:
        self._waf = waf

    @cached_property
    def overrides(self) -> OverridesWithStreamingResponse:
        return OverridesWithStreamingResponse(self._waf.overrides)

    @cached_property
    def packages(self) -> PackagesWithStreamingResponse:
        return PackagesWithStreamingResponse(self._waf.packages)


class AsyncWAFWithStreamingResponse:
    def __init__(self, waf: AsyncWAF) -> None:
        self._waf = waf

    @cached_property
    def overrides(self) -> AsyncOverridesWithStreamingResponse:
        return AsyncOverridesWithStreamingResponse(self._waf.overrides)

    @cached_property
    def packages(self) -> AsyncPackagesWithStreamingResponse:
        return AsyncPackagesWithStreamingResponse(self._waf.packages)
