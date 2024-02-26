# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .submits import (
    Submits,
    AsyncSubmits,
    SubmitsWithRawResponse,
    AsyncSubmitsWithRawResponse,
    SubmitsWithStreamingResponse,
    AsyncSubmitsWithStreamingResponse,
)
from ..._compat import cached_property
from .url_infos import (
    URLInfos,
    AsyncURLInfos,
    URLInfosWithRawResponse,
    AsyncURLInfosWithRawResponse,
    URLInfosWithStreamingResponse,
    AsyncURLInfosWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BrandProtection", "AsyncBrandProtection"]


class BrandProtection(SyncAPIResource):
    @cached_property
    def submits(self) -> Submits:
        return Submits(self._client)

    @cached_property
    def url_infos(self) -> URLInfos:
        return URLInfos(self._client)

    @cached_property
    def with_raw_response(self) -> BrandProtectionWithRawResponse:
        return BrandProtectionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandProtectionWithStreamingResponse:
        return BrandProtectionWithStreamingResponse(self)


class AsyncBrandProtection(AsyncAPIResource):
    @cached_property
    def submits(self) -> AsyncSubmits:
        return AsyncSubmits(self._client)

    @cached_property
    def url_infos(self) -> AsyncURLInfos:
        return AsyncURLInfos(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBrandProtectionWithRawResponse:
        return AsyncBrandProtectionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandProtectionWithStreamingResponse:
        return AsyncBrandProtectionWithStreamingResponse(self)


class BrandProtectionWithRawResponse:
    def __init__(self, brand_protection: BrandProtection) -> None:
        self._brand_protection = brand_protection

    @cached_property
    def submits(self) -> SubmitsWithRawResponse:
        return SubmitsWithRawResponse(self._brand_protection.submits)

    @cached_property
    def url_infos(self) -> URLInfosWithRawResponse:
        return URLInfosWithRawResponse(self._brand_protection.url_infos)


class AsyncBrandProtectionWithRawResponse:
    def __init__(self, brand_protection: AsyncBrandProtection) -> None:
        self._brand_protection = brand_protection

    @cached_property
    def submits(self) -> AsyncSubmitsWithRawResponse:
        return AsyncSubmitsWithRawResponse(self._brand_protection.submits)

    @cached_property
    def url_infos(self) -> AsyncURLInfosWithRawResponse:
        return AsyncURLInfosWithRawResponse(self._brand_protection.url_infos)


class BrandProtectionWithStreamingResponse:
    def __init__(self, brand_protection: BrandProtection) -> None:
        self._brand_protection = brand_protection

    @cached_property
    def submits(self) -> SubmitsWithStreamingResponse:
        return SubmitsWithStreamingResponse(self._brand_protection.submits)

    @cached_property
    def url_infos(self) -> URLInfosWithStreamingResponse:
        return URLInfosWithStreamingResponse(self._brand_protection.url_infos)


class AsyncBrandProtectionWithStreamingResponse:
    def __init__(self, brand_protection: AsyncBrandProtection) -> None:
        self._brand_protection = brand_protection

    @cached_property
    def submits(self) -> AsyncSubmitsWithStreamingResponse:
        return AsyncSubmitsWithStreamingResponse(self._brand_protection.submits)

    @cached_property
    def url_infos(self) -> AsyncURLInfosWithStreamingResponse:
        return AsyncURLInfosWithStreamingResponse(self._brand_protection.url_infos)
