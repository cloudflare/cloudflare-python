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

__all__ = ["BrandProtections", "AsyncBrandProtections"]


class BrandProtections(SyncAPIResource):
    @cached_property
    def submits(self) -> Submits:
        return Submits(self._client)

    @cached_property
    def url_infos(self) -> URLInfos:
        return URLInfos(self._client)

    @cached_property
    def with_raw_response(self) -> BrandProtectionsWithRawResponse:
        return BrandProtectionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandProtectionsWithStreamingResponse:
        return BrandProtectionsWithStreamingResponse(self)


class AsyncBrandProtections(AsyncAPIResource):
    @cached_property
    def submits(self) -> AsyncSubmits:
        return AsyncSubmits(self._client)

    @cached_property
    def url_infos(self) -> AsyncURLInfos:
        return AsyncURLInfos(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBrandProtectionsWithRawResponse:
        return AsyncBrandProtectionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandProtectionsWithStreamingResponse:
        return AsyncBrandProtectionsWithStreamingResponse(self)


class BrandProtectionsWithRawResponse:
    def __init__(self, brand_protections: BrandProtections) -> None:
        self._brand_protections = brand_protections

    @cached_property
    def submits(self) -> SubmitsWithRawResponse:
        return SubmitsWithRawResponse(self._brand_protections.submits)

    @cached_property
    def url_infos(self) -> URLInfosWithRawResponse:
        return URLInfosWithRawResponse(self._brand_protections.url_infos)


class AsyncBrandProtectionsWithRawResponse:
    def __init__(self, brand_protections: AsyncBrandProtections) -> None:
        self._brand_protections = brand_protections

    @cached_property
    def submits(self) -> AsyncSubmitsWithRawResponse:
        return AsyncSubmitsWithRawResponse(self._brand_protections.submits)

    @cached_property
    def url_infos(self) -> AsyncURLInfosWithRawResponse:
        return AsyncURLInfosWithRawResponse(self._brand_protections.url_infos)


class BrandProtectionsWithStreamingResponse:
    def __init__(self, brand_protections: BrandProtections) -> None:
        self._brand_protections = brand_protections

    @cached_property
    def submits(self) -> SubmitsWithStreamingResponse:
        return SubmitsWithStreamingResponse(self._brand_protections.submits)

    @cached_property
    def url_infos(self) -> URLInfosWithStreamingResponse:
        return URLInfosWithStreamingResponse(self._brand_protections.url_infos)


class AsyncBrandProtectionsWithStreamingResponse:
    def __init__(self, brand_protections: AsyncBrandProtections) -> None:
        self._brand_protections = brand_protections

    @cached_property
    def submits(self) -> AsyncSubmitsWithStreamingResponse:
        return AsyncSubmitsWithStreamingResponse(self._brand_protections.submits)

    @cached_property
    def url_infos(self) -> AsyncURLInfosWithStreamingResponse:
        return AsyncURLInfosWithStreamingResponse(self._brand_protections.url_infos)
