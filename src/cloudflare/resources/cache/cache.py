# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast, overload

import httpx

from ...types import CachePurgeResponse, cache_purge_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
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
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from .cache_reserve import (
    CacheReserve,
    AsyncCacheReserve,
    CacheReserveWithRawResponse,
    AsyncCacheReserveWithRawResponse,
    CacheReserveWithStreamingResponse,
    AsyncCacheReserveWithStreamingResponse,
)
from ..._base_client import (
    make_request_options,
)
from .smart_tiered_cache import (
    SmartTieredCache,
    AsyncSmartTieredCache,
    SmartTieredCacheWithRawResponse,
    AsyncSmartTieredCacheWithRawResponse,
    SmartTieredCacheWithStreamingResponse,
    AsyncSmartTieredCacheWithStreamingResponse,
)
from .regional_tiered_cache import (
    RegionalTieredCache,
    AsyncRegionalTieredCache,
    RegionalTieredCacheWithRawResponse,
    AsyncRegionalTieredCacheWithRawResponse,
    RegionalTieredCacheWithStreamingResponse,
    AsyncRegionalTieredCacheWithStreamingResponse,
)

__all__ = ["Cache", "AsyncCache"]


class Cache(SyncAPIResource):
    @cached_property
    def cache_reserve(self) -> CacheReserve:
        return CacheReserve(self._client)

    @cached_property
    def smart_tiered_cache(self) -> SmartTieredCache:
        return SmartTieredCache(self._client)

    @cached_property
    def variants(self) -> Variants:
        return Variants(self._client)

    @cached_property
    def regional_tiered_cache(self) -> RegionalTieredCache:
        return RegionalTieredCache(self._client)

    @cached_property
    def with_raw_response(self) -> CacheWithRawResponse:
        return CacheWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CacheWithStreamingResponse:
        return CacheWithStreamingResponse(self)

    @overload
    def purge(
        self,
        *,
        zone_id: str,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CachePurgeResponse]:
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ### Purge Cached Content by URL

        Granularly removes one or more files from Cloudflare's cache by specifying URLs.
        All tiers can purge by URL.

        To purge files with custom cache keys, include the headers used to compute the
        cache key as in the example. If you have a device type or geo in your cache key,
        you will need to include the CF-Device-Type or CF-IPCountry headers. If you have
        lang in your cache key, you will need to include the Accept-Language header.

        **NB:** When including the Origin header, be sure to include the **scheme** and
        **hostname**. The port number can be omitted if it is the default port (80 for
        http, 443 for https), but must be included otherwise.

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix. Only Enterprise
        customers are permitted to purge by Tag, Host or Prefix.

        **NB:** Cache-Tag, host, and prefix purging each have a rate limit of 30,000
        purge API calls in every 24 hour period. You may purge up to 30 tags, hosts, or
        prefixes in one API call. This rate limit can be raised for customers who need
        to purge at higher volume.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def purge(
        self,
        *,
        zone_id: str,
        hosts: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CachePurgeResponse]:
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ### Purge Cached Content by URL

        Granularly removes one or more files from Cloudflare's cache by specifying URLs.
        All tiers can purge by URL.

        To purge files with custom cache keys, include the headers used to compute the
        cache key as in the example. If you have a device type or geo in your cache key,
        you will need to include the CF-Device-Type or CF-IPCountry headers. If you have
        lang in your cache key, you will need to include the Accept-Language header.

        **NB:** When including the Origin header, be sure to include the **scheme** and
        **hostname**. The port number can be omitted if it is the default port (80 for
        http, 443 for https), but must be included otherwise.

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix. Only Enterprise
        customers are permitted to purge by Tag, Host or Prefix.

        **NB:** Cache-Tag, host, and prefix purging each have a rate limit of 30,000
        purge API calls in every 24 hour period. You may purge up to 30 tags, hosts, or
        prefixes in one API call. This rate limit can be raised for customers who need
        to purge at higher volume.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def purge(
        self,
        *,
        zone_id: str,
        prefixes: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CachePurgeResponse]:
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ### Purge Cached Content by URL

        Granularly removes one or more files from Cloudflare's cache by specifying URLs.
        All tiers can purge by URL.

        To purge files with custom cache keys, include the headers used to compute the
        cache key as in the example. If you have a device type or geo in your cache key,
        you will need to include the CF-Device-Type or CF-IPCountry headers. If you have
        lang in your cache key, you will need to include the Accept-Language header.

        **NB:** When including the Origin header, be sure to include the **scheme** and
        **hostname**. The port number can be omitted if it is the default port (80 for
        http, 443 for https), but must be included otherwise.

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix. Only Enterprise
        customers are permitted to purge by Tag, Host or Prefix.

        **NB:** Cache-Tag, host, and prefix purging each have a rate limit of 30,000
        purge API calls in every 24 hour period. You may purge up to 30 tags, hosts, or
        prefixes in one API call. This rate limit can be raised for customers who need
        to purge at higher volume.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def purge(
        self,
        *,
        zone_id: str,
        purge_everything: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CachePurgeResponse]:
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ### Purge Cached Content by URL

        Granularly removes one or more files from Cloudflare's cache by specifying URLs.
        All tiers can purge by URL.

        To purge files with custom cache keys, include the headers used to compute the
        cache key as in the example. If you have a device type or geo in your cache key,
        you will need to include the CF-Device-Type or CF-IPCountry headers. If you have
        lang in your cache key, you will need to include the Accept-Language header.

        **NB:** When including the Origin header, be sure to include the **scheme** and
        **hostname**. The port number can be omitted if it is the default port (80 for
        http, 443 for https), but must be included otherwise.

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix. Only Enterprise
        customers are permitted to purge by Tag, Host or Prefix.

        **NB:** Cache-Tag, host, and prefix purging each have a rate limit of 30,000
        purge API calls in every 24 hour period. You may purge up to 30 tags, hosts, or
        prefixes in one API call. This rate limit can be raised for customers who need
        to purge at higher volume.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def purge(
        self,
        *,
        zone_id: str,
        files: List[cache_purge_params.CachePurgeFilesFile] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CachePurgeResponse]:
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ### Purge Cached Content by URL

        Granularly removes one or more files from Cloudflare's cache by specifying URLs.
        All tiers can purge by URL.

        To purge files with custom cache keys, include the headers used to compute the
        cache key as in the example. If you have a device type or geo in your cache key,
        you will need to include the CF-Device-Type or CF-IPCountry headers. If you have
        lang in your cache key, you will need to include the Accept-Language header.

        **NB:** When including the Origin header, be sure to include the **scheme** and
        **hostname**. The port number can be omitted if it is the default port (80 for
        http, 443 for https), but must be included otherwise.

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix. Only Enterprise
        customers are permitted to purge by Tag, Host or Prefix.

        **NB:** Cache-Tag, host, and prefix purging each have a rate limit of 30,000
        purge API calls in every 24 hour period. You may purge up to 30 tags, hosts, or
        prefixes in one API call. This rate limit can be raised for customers who need
        to purge at higher volume.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"], ["zone_id"], ["zone_id"], ["zone_id"], ["zone_id"])
    def purge(
        self,
        *,
        zone_id: str,
        tags: List[str] | NotGiven = NOT_GIVEN,
        hosts: List[str] | NotGiven = NOT_GIVEN,
        prefixes: List[str] | NotGiven = NOT_GIVEN,
        purge_everything: bool | NotGiven = NOT_GIVEN,
        files: List[cache_purge_params.CachePurgeFilesFile] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CachePurgeResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/purge_cache",
            body=maybe_transform(
                {
                    "tags": tags,
                    "hosts": hosts,
                    "prefixes": prefixes,
                    "purge_everything": purge_everything,
                    "files": files,
                },
                cache_purge_params.CachePurgeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CachePurgeResponse]], ResultWrapper[CachePurgeResponse]),
        )


class AsyncCache(AsyncAPIResource):
    @cached_property
    def cache_reserve(self) -> AsyncCacheReserve:
        return AsyncCacheReserve(self._client)

    @cached_property
    def smart_tiered_cache(self) -> AsyncSmartTieredCache:
        return AsyncSmartTieredCache(self._client)

    @cached_property
    def variants(self) -> AsyncVariants:
        return AsyncVariants(self._client)

    @cached_property
    def regional_tiered_cache(self) -> AsyncRegionalTieredCache:
        return AsyncRegionalTieredCache(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCacheWithRawResponse:
        return AsyncCacheWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCacheWithStreamingResponse:
        return AsyncCacheWithStreamingResponse(self)

    @overload
    async def purge(
        self,
        *,
        zone_id: str,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CachePurgeResponse]:
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ### Purge Cached Content by URL

        Granularly removes one or more files from Cloudflare's cache by specifying URLs.
        All tiers can purge by URL.

        To purge files with custom cache keys, include the headers used to compute the
        cache key as in the example. If you have a device type or geo in your cache key,
        you will need to include the CF-Device-Type or CF-IPCountry headers. If you have
        lang in your cache key, you will need to include the Accept-Language header.

        **NB:** When including the Origin header, be sure to include the **scheme** and
        **hostname**. The port number can be omitted if it is the default port (80 for
        http, 443 for https), but must be included otherwise.

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix. Only Enterprise
        customers are permitted to purge by Tag, Host or Prefix.

        **NB:** Cache-Tag, host, and prefix purging each have a rate limit of 30,000
        purge API calls in every 24 hour period. You may purge up to 30 tags, hosts, or
        prefixes in one API call. This rate limit can be raised for customers who need
        to purge at higher volume.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def purge(
        self,
        *,
        zone_id: str,
        hosts: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CachePurgeResponse]:
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ### Purge Cached Content by URL

        Granularly removes one or more files from Cloudflare's cache by specifying URLs.
        All tiers can purge by URL.

        To purge files with custom cache keys, include the headers used to compute the
        cache key as in the example. If you have a device type or geo in your cache key,
        you will need to include the CF-Device-Type or CF-IPCountry headers. If you have
        lang in your cache key, you will need to include the Accept-Language header.

        **NB:** When including the Origin header, be sure to include the **scheme** and
        **hostname**. The port number can be omitted if it is the default port (80 for
        http, 443 for https), but must be included otherwise.

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix. Only Enterprise
        customers are permitted to purge by Tag, Host or Prefix.

        **NB:** Cache-Tag, host, and prefix purging each have a rate limit of 30,000
        purge API calls in every 24 hour period. You may purge up to 30 tags, hosts, or
        prefixes in one API call. This rate limit can be raised for customers who need
        to purge at higher volume.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def purge(
        self,
        *,
        zone_id: str,
        prefixes: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CachePurgeResponse]:
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ### Purge Cached Content by URL

        Granularly removes one or more files from Cloudflare's cache by specifying URLs.
        All tiers can purge by URL.

        To purge files with custom cache keys, include the headers used to compute the
        cache key as in the example. If you have a device type or geo in your cache key,
        you will need to include the CF-Device-Type or CF-IPCountry headers. If you have
        lang in your cache key, you will need to include the Accept-Language header.

        **NB:** When including the Origin header, be sure to include the **scheme** and
        **hostname**. The port number can be omitted if it is the default port (80 for
        http, 443 for https), but must be included otherwise.

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix. Only Enterprise
        customers are permitted to purge by Tag, Host or Prefix.

        **NB:** Cache-Tag, host, and prefix purging each have a rate limit of 30,000
        purge API calls in every 24 hour period. You may purge up to 30 tags, hosts, or
        prefixes in one API call. This rate limit can be raised for customers who need
        to purge at higher volume.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def purge(
        self,
        *,
        zone_id: str,
        purge_everything: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CachePurgeResponse]:
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ### Purge Cached Content by URL

        Granularly removes one or more files from Cloudflare's cache by specifying URLs.
        All tiers can purge by URL.

        To purge files with custom cache keys, include the headers used to compute the
        cache key as in the example. If you have a device type or geo in your cache key,
        you will need to include the CF-Device-Type or CF-IPCountry headers. If you have
        lang in your cache key, you will need to include the Accept-Language header.

        **NB:** When including the Origin header, be sure to include the **scheme** and
        **hostname**. The port number can be omitted if it is the default port (80 for
        http, 443 for https), but must be included otherwise.

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix. Only Enterprise
        customers are permitted to purge by Tag, Host or Prefix.

        **NB:** Cache-Tag, host, and prefix purging each have a rate limit of 30,000
        purge API calls in every 24 hour period. You may purge up to 30 tags, hosts, or
        prefixes in one API call. This rate limit can be raised for customers who need
        to purge at higher volume.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def purge(
        self,
        *,
        zone_id: str,
        files: List[cache_purge_params.CachePurgeFilesFile] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CachePurgeResponse]:
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ### Purge Cached Content by URL

        Granularly removes one or more files from Cloudflare's cache by specifying URLs.
        All tiers can purge by URL.

        To purge files with custom cache keys, include the headers used to compute the
        cache key as in the example. If you have a device type or geo in your cache key,
        you will need to include the CF-Device-Type or CF-IPCountry headers. If you have
        lang in your cache key, you will need to include the Accept-Language header.

        **NB:** When including the Origin header, be sure to include the **scheme** and
        **hostname**. The port number can be omitted if it is the default port (80 for
        http, 443 for https), but must be included otherwise.

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix. Only Enterprise
        customers are permitted to purge by Tag, Host or Prefix.

        **NB:** Cache-Tag, host, and prefix purging each have a rate limit of 30,000
        purge API calls in every 24 hour period. You may purge up to 30 tags, hosts, or
        prefixes in one API call. This rate limit can be raised for customers who need
        to purge at higher volume.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"], ["zone_id"], ["zone_id"], ["zone_id"], ["zone_id"])
    async def purge(
        self,
        *,
        zone_id: str,
        tags: List[str] | NotGiven = NOT_GIVEN,
        hosts: List[str] | NotGiven = NOT_GIVEN,
        prefixes: List[str] | NotGiven = NOT_GIVEN,
        purge_everything: bool | NotGiven = NOT_GIVEN,
        files: List[cache_purge_params.CachePurgeFilesFile] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CachePurgeResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/purge_cache",
            body=await async_maybe_transform(
                {
                    "tags": tags,
                    "hosts": hosts,
                    "prefixes": prefixes,
                    "purge_everything": purge_everything,
                    "files": files,
                },
                cache_purge_params.CachePurgeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CachePurgeResponse]], ResultWrapper[CachePurgeResponse]),
        )


class CacheWithRawResponse:
    def __init__(self, cache: Cache) -> None:
        self._cache = cache

        self.purge = to_raw_response_wrapper(
            cache.purge,
        )

    @cached_property
    def cache_reserve(self) -> CacheReserveWithRawResponse:
        return CacheReserveWithRawResponse(self._cache.cache_reserve)

    @cached_property
    def smart_tiered_cache(self) -> SmartTieredCacheWithRawResponse:
        return SmartTieredCacheWithRawResponse(self._cache.smart_tiered_cache)

    @cached_property
    def variants(self) -> VariantsWithRawResponse:
        return VariantsWithRawResponse(self._cache.variants)

    @cached_property
    def regional_tiered_cache(self) -> RegionalTieredCacheWithRawResponse:
        return RegionalTieredCacheWithRawResponse(self._cache.regional_tiered_cache)


class AsyncCacheWithRawResponse:
    def __init__(self, cache: AsyncCache) -> None:
        self._cache = cache

        self.purge = async_to_raw_response_wrapper(
            cache.purge,
        )

    @cached_property
    def cache_reserve(self) -> AsyncCacheReserveWithRawResponse:
        return AsyncCacheReserveWithRawResponse(self._cache.cache_reserve)

    @cached_property
    def smart_tiered_cache(self) -> AsyncSmartTieredCacheWithRawResponse:
        return AsyncSmartTieredCacheWithRawResponse(self._cache.smart_tiered_cache)

    @cached_property
    def variants(self) -> AsyncVariantsWithRawResponse:
        return AsyncVariantsWithRawResponse(self._cache.variants)

    @cached_property
    def regional_tiered_cache(self) -> AsyncRegionalTieredCacheWithRawResponse:
        return AsyncRegionalTieredCacheWithRawResponse(self._cache.regional_tiered_cache)


class CacheWithStreamingResponse:
    def __init__(self, cache: Cache) -> None:
        self._cache = cache

        self.purge = to_streamed_response_wrapper(
            cache.purge,
        )

    @cached_property
    def cache_reserve(self) -> CacheReserveWithStreamingResponse:
        return CacheReserveWithStreamingResponse(self._cache.cache_reserve)

    @cached_property
    def smart_tiered_cache(self) -> SmartTieredCacheWithStreamingResponse:
        return SmartTieredCacheWithStreamingResponse(self._cache.smart_tiered_cache)

    @cached_property
    def variants(self) -> VariantsWithStreamingResponse:
        return VariantsWithStreamingResponse(self._cache.variants)

    @cached_property
    def regional_tiered_cache(self) -> RegionalTieredCacheWithStreamingResponse:
        return RegionalTieredCacheWithStreamingResponse(self._cache.regional_tiered_cache)


class AsyncCacheWithStreamingResponse:
    def __init__(self, cache: AsyncCache) -> None:
        self._cache = cache

        self.purge = async_to_streamed_response_wrapper(
            cache.purge,
        )

    @cached_property
    def cache_reserve(self) -> AsyncCacheReserveWithStreamingResponse:
        return AsyncCacheReserveWithStreamingResponse(self._cache.cache_reserve)

    @cached_property
    def smart_tiered_cache(self) -> AsyncSmartTieredCacheWithStreamingResponse:
        return AsyncSmartTieredCacheWithStreamingResponse(self._cache.smart_tiered_cache)

    @cached_property
    def variants(self) -> AsyncVariantsWithStreamingResponse:
        return AsyncVariantsWithStreamingResponse(self._cache.variants)

    @cached_property
    def regional_tiered_cache(self) -> AsyncRegionalTieredCacheWithStreamingResponse:
        return AsyncRegionalTieredCacheWithStreamingResponse(self._cache.regional_tiered_cache)
