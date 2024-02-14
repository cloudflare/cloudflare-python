# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .variants import (
    Variants,
    AsyncVariants,
    VariantsWithRawResponse,
    AsyncVariantsWithRawResponse,
    VariantsWithStreamingResponse,
    AsyncVariantsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .cache_reserves import (
    CacheReserves,
    AsyncCacheReserves,
    CacheReservesWithRawResponse,
    AsyncCacheReservesWithRawResponse,
    CacheReservesWithStreamingResponse,
    AsyncCacheReservesWithStreamingResponse,
)
from .tiered_cache_smart_topology_enables import (
    TieredCacheSmartTopologyEnables,
    AsyncTieredCacheSmartTopologyEnables,
    TieredCacheSmartTopologyEnablesWithRawResponse,
    AsyncTieredCacheSmartTopologyEnablesWithRawResponse,
    TieredCacheSmartTopologyEnablesWithStreamingResponse,
    AsyncTieredCacheSmartTopologyEnablesWithStreamingResponse,
)

__all__ = ["Caches", "AsyncCaches"]


class Caches(SyncAPIResource):
    @cached_property
    def cache_reserves(self) -> CacheReserves:
        return CacheReserves(self._client)

    @cached_property
    def tiered_cache_smart_topology_enables(self) -> TieredCacheSmartTopologyEnables:
        return TieredCacheSmartTopologyEnables(self._client)

    @cached_property
    def variants(self) -> Variants:
        return Variants(self._client)

    @cached_property
    def with_raw_response(self) -> CachesWithRawResponse:
        return CachesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CachesWithStreamingResponse:
        return CachesWithStreamingResponse(self)


class AsyncCaches(AsyncAPIResource):
    @cached_property
    def cache_reserves(self) -> AsyncCacheReserves:
        return AsyncCacheReserves(self._client)

    @cached_property
    def tiered_cache_smart_topology_enables(self) -> AsyncTieredCacheSmartTopologyEnables:
        return AsyncTieredCacheSmartTopologyEnables(self._client)

    @cached_property
    def variants(self) -> AsyncVariants:
        return AsyncVariants(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCachesWithRawResponse:
        return AsyncCachesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCachesWithStreamingResponse:
        return AsyncCachesWithStreamingResponse(self)


class CachesWithRawResponse:
    def __init__(self, caches: Caches) -> None:
        self._caches = caches

    @cached_property
    def cache_reserves(self) -> CacheReservesWithRawResponse:
        return CacheReservesWithRawResponse(self._caches.cache_reserves)

    @cached_property
    def tiered_cache_smart_topology_enables(self) -> TieredCacheSmartTopologyEnablesWithRawResponse:
        return TieredCacheSmartTopologyEnablesWithRawResponse(self._caches.tiered_cache_smart_topology_enables)

    @cached_property
    def variants(self) -> VariantsWithRawResponse:
        return VariantsWithRawResponse(self._caches.variants)


class AsyncCachesWithRawResponse:
    def __init__(self, caches: AsyncCaches) -> None:
        self._caches = caches

    @cached_property
    def cache_reserves(self) -> AsyncCacheReservesWithRawResponse:
        return AsyncCacheReservesWithRawResponse(self._caches.cache_reserves)

    @cached_property
    def tiered_cache_smart_topology_enables(self) -> AsyncTieredCacheSmartTopologyEnablesWithRawResponse:
        return AsyncTieredCacheSmartTopologyEnablesWithRawResponse(self._caches.tiered_cache_smart_topology_enables)

    @cached_property
    def variants(self) -> AsyncVariantsWithRawResponse:
        return AsyncVariantsWithRawResponse(self._caches.variants)


class CachesWithStreamingResponse:
    def __init__(self, caches: Caches) -> None:
        self._caches = caches

    @cached_property
    def cache_reserves(self) -> CacheReservesWithStreamingResponse:
        return CacheReservesWithStreamingResponse(self._caches.cache_reserves)

    @cached_property
    def tiered_cache_smart_topology_enables(self) -> TieredCacheSmartTopologyEnablesWithStreamingResponse:
        return TieredCacheSmartTopologyEnablesWithStreamingResponse(self._caches.tiered_cache_smart_topology_enables)

    @cached_property
    def variants(self) -> VariantsWithStreamingResponse:
        return VariantsWithStreamingResponse(self._caches.variants)


class AsyncCachesWithStreamingResponse:
    def __init__(self, caches: AsyncCaches) -> None:
        self._caches = caches

    @cached_property
    def cache_reserves(self) -> AsyncCacheReservesWithStreamingResponse:
        return AsyncCacheReservesWithStreamingResponse(self._caches.cache_reserves)

    @cached_property
    def tiered_cache_smart_topology_enables(self) -> AsyncTieredCacheSmartTopologyEnablesWithStreamingResponse:
        return AsyncTieredCacheSmartTopologyEnablesWithStreamingResponse(
            self._caches.tiered_cache_smart_topology_enables
        )

    @cached_property
    def variants(self) -> AsyncVariantsWithStreamingResponse:
        return AsyncVariantsWithStreamingResponse(self._caches.variants)
