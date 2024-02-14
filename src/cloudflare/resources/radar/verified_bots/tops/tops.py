# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .bots import (
    Bots,
    AsyncBots,
    BotsWithRawResponse,
    AsyncBotsWithRawResponse,
    BotsWithStreamingResponse,
    AsyncBotsWithStreamingResponse,
)
from .categories import (
    Categories,
    AsyncCategories,
    CategoriesWithRawResponse,
    AsyncCategoriesWithRawResponse,
    CategoriesWithStreamingResponse,
    AsyncCategoriesWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Tops", "AsyncTops"]


class Tops(SyncAPIResource):
    @cached_property
    def bots(self) -> Bots:
        return Bots(self._client)

    @cached_property
    def categories(self) -> Categories:
        return Categories(self._client)

    @cached_property
    def with_raw_response(self) -> TopsWithRawResponse:
        return TopsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopsWithStreamingResponse:
        return TopsWithStreamingResponse(self)


class AsyncTops(AsyncAPIResource):
    @cached_property
    def bots(self) -> AsyncBots:
        return AsyncBots(self._client)

    @cached_property
    def categories(self) -> AsyncCategories:
        return AsyncCategories(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTopsWithRawResponse:
        return AsyncTopsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopsWithStreamingResponse:
        return AsyncTopsWithStreamingResponse(self)


class TopsWithRawResponse:
    def __init__(self, tops: Tops) -> None:
        self._tops = tops

    @cached_property
    def bots(self) -> BotsWithRawResponse:
        return BotsWithRawResponse(self._tops.bots)

    @cached_property
    def categories(self) -> CategoriesWithRawResponse:
        return CategoriesWithRawResponse(self._tops.categories)


class AsyncTopsWithRawResponse:
    def __init__(self, tops: AsyncTops) -> None:
        self._tops = tops

    @cached_property
    def bots(self) -> AsyncBotsWithRawResponse:
        return AsyncBotsWithRawResponse(self._tops.bots)

    @cached_property
    def categories(self) -> AsyncCategoriesWithRawResponse:
        return AsyncCategoriesWithRawResponse(self._tops.categories)


class TopsWithStreamingResponse:
    def __init__(self, tops: Tops) -> None:
        self._tops = tops

    @cached_property
    def bots(self) -> BotsWithStreamingResponse:
        return BotsWithStreamingResponse(self._tops.bots)

    @cached_property
    def categories(self) -> CategoriesWithStreamingResponse:
        return CategoriesWithStreamingResponse(self._tops.categories)


class AsyncTopsWithStreamingResponse:
    def __init__(self, tops: AsyncTops) -> None:
        self._tops = tops

    @cached_property
    def bots(self) -> AsyncBotsWithStreamingResponse:
        return AsyncBotsWithStreamingResponse(self._tops.bots)

    @cached_property
    def categories(self) -> AsyncCategoriesWithStreamingResponse:
        return AsyncCategoriesWithStreamingResponse(self._tops.categories)
