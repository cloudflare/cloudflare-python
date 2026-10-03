# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast
from typing_extensions import overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
from .variants import (
    VariantsResource,
    AsyncVariantsResource,
    VariantsResourceWithRawResponse,
    AsyncVariantsResourceWithRawResponse,
    VariantsResourceWithStreamingResponse,
    AsyncVariantsResourceWithStreamingResponse,
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
from ...types.cache import (
    cache_purge_params,
    cache_invalidate_params,
    cache_purge_environment_params,
    cache_invalidate_environment_params,
)
from .cache_reserve import (
    CacheReserveResource,
    AsyncCacheReserveResource,
    CacheReserveResourceWithRawResponse,
    AsyncCacheReserveResourceWithRawResponse,
    CacheReserveResourceWithStreamingResponse,
    AsyncCacheReserveResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .smart_tiered_cache import (
    SmartTieredCacheResource,
    AsyncSmartTieredCacheResource,
    SmartTieredCacheResourceWithRawResponse,
    AsyncSmartTieredCacheResourceWithRawResponse,
    SmartTieredCacheResourceWithStreamingResponse,
    AsyncSmartTieredCacheResourceWithStreamingResponse,
)
from .origin_cloud_regions import (
    OriginCloudRegionsResource,
    AsyncOriginCloudRegionsResource,
    OriginCloudRegionsResourceWithRawResponse,
    AsyncOriginCloudRegionsResourceWithRawResponse,
    OriginCloudRegionsResourceWithStreamingResponse,
    AsyncOriginCloudRegionsResourceWithStreamingResponse,
)
from .regional_tiered_cache import (
    RegionalTieredCacheResource,
    AsyncRegionalTieredCacheResource,
    RegionalTieredCacheResourceWithRawResponse,
    AsyncRegionalTieredCacheResourceWithRawResponse,
    RegionalTieredCacheResourceWithStreamingResponse,
    AsyncRegionalTieredCacheResourceWithStreamingResponse,
)
from ...types.cache.cache_purge_response import CachePurgeResponse
from ...types.cache.cache_invalidate_response import CacheInvalidateResponse
from ...types.cache.cache_purge_environment_response import CachePurgeEnvironmentResponse
from ...types.cache.cache_invalidate_environment_response import CacheInvalidateEnvironmentResponse

__all__ = ["CacheResource", "AsyncCacheResource"]


class CacheResource(SyncAPIResource):
    @cached_property
    def cache_reserve(self) -> CacheReserveResource:
        return CacheReserveResource(self._client)

    @cached_property
    def smart_tiered_cache(self) -> SmartTieredCacheResource:
        return SmartTieredCacheResource(self._client)

    @cached_property
    def variants(self) -> VariantsResource:
        return VariantsResource(self._client)

    @cached_property
    def regional_tiered_cache(self) -> RegionalTieredCacheResource:
        return RegionalTieredCacheResource(self._client)

    @cached_property
    def origin_cloud_regions(self) -> OriginCloudRegionsResource:
        return OriginCloudRegionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CacheResourceWithStreamingResponse(self)

    @overload
    def invalidate(
        self,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateResponse]:
        """
        Marks cached content as stale in every Cloudflare data center and cache tier,
        including Cache Reserve. The content stays in cache. The next request for it
        makes Cloudflare revalidate it with your origin, using the `ETag` and
        `Last-Modified` values it was cached with:

        - If your origin answers `304 Not Modified`, Cloudflare serves the cached copy
          without downloading it again, and `CF-Cache-Status` is `REVALIDATED`.
        - If your origin sends a full response, Cloudflare serves and caches the new
          content, and `CF-Cache-Status` is `EXPIRED`.

        With Tiered Cache, each tier revalidates with the tier above it, so a visitor
        can see `EXPIRED` even when your origin answered `304`.

        Until content is revalidated, your `stale-while-revalidate` and `stale-if-error`
        directives still apply, counted from the time you invalidated it. For example,
        if your origin fails during revalidation, Cloudflare can keep serving the stale
        copy for the `stale-if-error` window.

        ### Invalidate or purge?

        - **Invalidate** when content may not have changed, for example after a deploy.
          Unchanged content costs your origin a `304` instead of a full response. That
          saving needs an origin that sends `ETag` or `Last-Modified` and answers
          conditional requests. Otherwise, every revalidation downloads the full
          response.
        - **Purge**, with `POST /zones/{zone_id}/purge_cache`, when content must not be
          served again, for example content you removed for legal or security reasons.

        Invalidating takes the same request bodies as purging, needs the same
        permission, and counts against the same rate limits. After a broad invalidation,
        such as `purge_everything`, expect more conditional requests to your origin
        while visitors request the invalidated content again.

        ### Choose what to invalidate

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. To
        check, request an invalidated URL and confirm that the `CF-Cache-Status`
        response header is `REVALIDATED` or `EXPIRED`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          tags: Cache tags. Targets all content whose `Cache-Tag` response header contains at
              least one of these tags. See
              [Purge cache by cache-tags](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def invalidate(
        self,
        *,
        zone_id: str,
        hosts: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateResponse]:
        """
        Marks cached content as stale in every Cloudflare data center and cache tier,
        including Cache Reserve. The content stays in cache. The next request for it
        makes Cloudflare revalidate it with your origin, using the `ETag` and
        `Last-Modified` values it was cached with:

        - If your origin answers `304 Not Modified`, Cloudflare serves the cached copy
          without downloading it again, and `CF-Cache-Status` is `REVALIDATED`.
        - If your origin sends a full response, Cloudflare serves and caches the new
          content, and `CF-Cache-Status` is `EXPIRED`.

        With Tiered Cache, each tier revalidates with the tier above it, so a visitor
        can see `EXPIRED` even when your origin answered `304`.

        Until content is revalidated, your `stale-while-revalidate` and `stale-if-error`
        directives still apply, counted from the time you invalidated it. For example,
        if your origin fails during revalidation, Cloudflare can keep serving the stale
        copy for the `stale-if-error` window.

        ### Invalidate or purge?

        - **Invalidate** when content may not have changed, for example after a deploy.
          Unchanged content costs your origin a `304` instead of a full response. That
          saving needs an origin that sends `ETag` or `Last-Modified` and answers
          conditional requests. Otherwise, every revalidation downloads the full
          response.
        - **Purge**, with `POST /zones/{zone_id}/purge_cache`, when content must not be
          served again, for example content you removed for legal or security reasons.

        Invalidating takes the same request bodies as purging, needs the same
        permission, and counts against the same rate limits. After a broad invalidation,
        such as `purge_everything`, expect more conditional requests to your origin
        while visitors request the invalidated content again.

        ### Choose what to invalidate

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. To
        check, request an invalidated URL and confirm that the `CF-Cache-Status`
        response header is `REVALIDATED` or `EXPIRED`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          hosts: Hostnames, such as `www.example.com`. Targets all content cached for these
              hostnames. See
              [Purge cache by hostname](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def invalidate(
        self,
        *,
        zone_id: str,
        prefixes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateResponse]:
        """
        Marks cached content as stale in every Cloudflare data center and cache tier,
        including Cache Reserve. The content stays in cache. The next request for it
        makes Cloudflare revalidate it with your origin, using the `ETag` and
        `Last-Modified` values it was cached with:

        - If your origin answers `304 Not Modified`, Cloudflare serves the cached copy
          without downloading it again, and `CF-Cache-Status` is `REVALIDATED`.
        - If your origin sends a full response, Cloudflare serves and caches the new
          content, and `CF-Cache-Status` is `EXPIRED`.

        With Tiered Cache, each tier revalidates with the tier above it, so a visitor
        can see `EXPIRED` even when your origin answered `304`.

        Until content is revalidated, your `stale-while-revalidate` and `stale-if-error`
        directives still apply, counted from the time you invalidated it. For example,
        if your origin fails during revalidation, Cloudflare can keep serving the stale
        copy for the `stale-if-error` window.

        ### Invalidate or purge?

        - **Invalidate** when content may not have changed, for example after a deploy.
          Unchanged content costs your origin a `304` instead of a full response. That
          saving needs an origin that sends `ETag` or `Last-Modified` and answers
          conditional requests. Otherwise, every revalidation downloads the full
          response.
        - **Purge**, with `POST /zones/{zone_id}/purge_cache`, when content must not be
          served again, for example content you removed for legal or security reasons.

        Invalidating takes the same request bodies as purging, needs the same
        permission, and counts against the same rate limits. After a broad invalidation,
        such as `purge_everything`, expect more conditional requests to your origin
        while visitors request the invalidated content again.

        ### Choose what to invalidate

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. To
        check, request an invalidated URL and confirm that the `CF-Cache-Status`
        response header is `REVALIDATED` or `EXPIRED`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          prefixes: URL prefixes, each a hostname followed by a path, such as
              `www.example.com/blog/`. Targets all content whose URL starts with one of these
              prefixes. Do not include a scheme, query string, or fragment. See
              [Purge cache by prefix](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def invalidate(
        self,
        *,
        zone_id: str,
        purge_everything: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateResponse]:
        """
        Marks cached content as stale in every Cloudflare data center and cache tier,
        including Cache Reserve. The content stays in cache. The next request for it
        makes Cloudflare revalidate it with your origin, using the `ETag` and
        `Last-Modified` values it was cached with:

        - If your origin answers `304 Not Modified`, Cloudflare serves the cached copy
          without downloading it again, and `CF-Cache-Status` is `REVALIDATED`.
        - If your origin sends a full response, Cloudflare serves and caches the new
          content, and `CF-Cache-Status` is `EXPIRED`.

        With Tiered Cache, each tier revalidates with the tier above it, so a visitor
        can see `EXPIRED` even when your origin answered `304`.

        Until content is revalidated, your `stale-while-revalidate` and `stale-if-error`
        directives still apply, counted from the time you invalidated it. For example,
        if your origin fails during revalidation, Cloudflare can keep serving the stale
        copy for the `stale-if-error` window.

        ### Invalidate or purge?

        - **Invalidate** when content may not have changed, for example after a deploy.
          Unchanged content costs your origin a `304` instead of a full response. That
          saving needs an origin that sends `ETag` or `Last-Modified` and answers
          conditional requests. Otherwise, every revalidation downloads the full
          response.
        - **Purge**, with `POST /zones/{zone_id}/purge_cache`, when content must not be
          served again, for example content you removed for legal or security reasons.

        Invalidating takes the same request bodies as purging, needs the same
        permission, and counts against the same rate limits. After a broad invalidation,
        such as `purge_everything`, expect more conditional requests to your origin
        while visitors request the invalidated content again.

        ### Choose what to invalidate

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. To
        check, request an invalidated URL and confirm that the `CF-Cache-Status`
        response header is `REVALIDATED` or `EXPIRED`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          purge_everything: Set to `true` to target all cached content in the zone, or in the environment
              for the environment endpoints. Must be the only field in the request. See
              [Purge everything](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def invalidate(
        self,
        *,
        zone_id: str,
        files: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateResponse]:
        """
        Marks cached content as stale in every Cloudflare data center and cache tier,
        including Cache Reserve. The content stays in cache. The next request for it
        makes Cloudflare revalidate it with your origin, using the `ETag` and
        `Last-Modified` values it was cached with:

        - If your origin answers `304 Not Modified`, Cloudflare serves the cached copy
          without downloading it again, and `CF-Cache-Status` is `REVALIDATED`.
        - If your origin sends a full response, Cloudflare serves and caches the new
          content, and `CF-Cache-Status` is `EXPIRED`.

        With Tiered Cache, each tier revalidates with the tier above it, so a visitor
        can see `EXPIRED` even when your origin answered `304`.

        Until content is revalidated, your `stale-while-revalidate` and `stale-if-error`
        directives still apply, counted from the time you invalidated it. For example,
        if your origin fails during revalidation, Cloudflare can keep serving the stale
        copy for the `stale-if-error` window.

        ### Invalidate or purge?

        - **Invalidate** when content may not have changed, for example after a deploy.
          Unchanged content costs your origin a `304` instead of a full response. That
          saving needs an origin that sends `ETag` or `Last-Modified` and answers
          conditional requests. Otherwise, every revalidation downloads the full
          response.
        - **Purge**, with `POST /zones/{zone_id}/purge_cache`, when content must not be
          served again, for example content you removed for legal or security reasons.

        Invalidating takes the same request bodies as purging, needs the same
        permission, and counts against the same rate limits. After a broad invalidation,
        such as `purge_everything`, expect more conditional requests to your origin
        while visitors request the invalidated content again.

        ### Choose what to invalidate

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. To
        check, request an invalidated URL and confirm that the `CF-Cache-Status`
        response header is `REVALIDATED` or `EXPIRED`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: Full URLs, such as `https://www.example.com/css/styles.css`. Targets the content
              cached for each URL. If your cache key includes request headers, send objects
              with `url` and `headers` instead. See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def invalidate(
        self,
        *,
        zone_id: str,
        files: Iterable[cache_invalidate_params.CachePurgeSingleFileWithURLAndHeadersFile] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateResponse]:
        """
        Marks cached content as stale in every Cloudflare data center and cache tier,
        including Cache Reserve. The content stays in cache. The next request for it
        makes Cloudflare revalidate it with your origin, using the `ETag` and
        `Last-Modified` values it was cached with:

        - If your origin answers `304 Not Modified`, Cloudflare serves the cached copy
          without downloading it again, and `CF-Cache-Status` is `REVALIDATED`.
        - If your origin sends a full response, Cloudflare serves and caches the new
          content, and `CF-Cache-Status` is `EXPIRED`.

        With Tiered Cache, each tier revalidates with the tier above it, so a visitor
        can see `EXPIRED` even when your origin answered `304`.

        Until content is revalidated, your `stale-while-revalidate` and `stale-if-error`
        directives still apply, counted from the time you invalidated it. For example,
        if your origin fails during revalidation, Cloudflare can keep serving the stale
        copy for the `stale-if-error` window.

        ### Invalidate or purge?

        - **Invalidate** when content may not have changed, for example after a deploy.
          Unchanged content costs your origin a `304` instead of a full response. That
          saving needs an origin that sends `ETag` or `Last-Modified` and answers
          conditional requests. Otherwise, every revalidation downloads the full
          response.
        - **Purge**, with `POST /zones/{zone_id}/purge_cache`, when content must not be
          served again, for example content you removed for legal or security reasons.

        Invalidating takes the same request bodies as purging, needs the same
        permission, and counts against the same rate limits. After a broad invalidation,
        such as `purge_everything`, expect more conditional requests to your origin
        while visitors request the invalidated content again.

        ### Choose what to invalidate

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. To
        check, request an invalidated URL and confirm that the `CF-Cache-Status`
        response header is `REVALIDATED` or `EXPIRED`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: URLs with the request headers your cache key uses. Use this form when your cache
              key includes request headers, or the visitor's device type, country, or
              language: send the header values each URL was cached with, such as
              `CF-Device-Type`, `CF-IPCountry`, or `Accept-Language`.

              When you send the `Origin` header, include the scheme and hostname. Include the
              port unless it is the default for the scheme: 80 for `http`, 443 for `https`.

              See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    def invalidate(
        self,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        hosts: SequenceNotStr[str] | Omit = omit,
        prefixes: SequenceNotStr[str] | Omit = omit,
        purge_everything: bool | Omit = omit,
        files: SequenceNotStr[str]
        | Iterable[cache_invalidate_params.CachePurgeSingleFileWithURLAndHeadersFile]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            path_template("/zones/{zone_id}/invalidate_cache", zone_id=zone_id),
            body=maybe_transform(
                {
                    "tags": tags,
                    "hosts": hosts,
                    "prefixes": prefixes,
                    "purge_everything": purge_everything,
                    "files": files,
                },
                cache_invalidate_params.CacheInvalidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CacheInvalidateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CacheInvalidateResponse]], ResultWrapper[CacheInvalidateResponse]),
        )

    @overload
    def invalidate_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateEnvironmentResponse]:
        """Marks cached content as stale for one environment of the zone.

        Content cached
        for the zone's other environments, including production, is not affected.
        Otherwise this works like `POST /zones/{zone_id}/invalidate_cache`: the next
        request for invalidated content makes Cloudflare revalidate it with your origin,
        and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        delete the content instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/purge_cache`.

        Invalidating by URL (`files`) does not work for environments that select
        requests by IP address, country, ASN, or threat score, and fails with error
        `1136`. Use `tags`, `hosts`, `prefixes`, or `purge_everything` for those
        environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          tags: Cache tags. Targets all content whose `Cache-Tag` response header contains at
              least one of these tags. See
              [Purge cache by cache-tags](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def invalidate_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        hosts: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateEnvironmentResponse]:
        """Marks cached content as stale for one environment of the zone.

        Content cached
        for the zone's other environments, including production, is not affected.
        Otherwise this works like `POST /zones/{zone_id}/invalidate_cache`: the next
        request for invalidated content makes Cloudflare revalidate it with your origin,
        and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        delete the content instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/purge_cache`.

        Invalidating by URL (`files`) does not work for environments that select
        requests by IP address, country, ASN, or threat score, and fails with error
        `1136`. Use `tags`, `hosts`, `prefixes`, or `purge_everything` for those
        environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          hosts: Hostnames, such as `www.example.com`. Targets all content cached for these
              hostnames. See
              [Purge cache by hostname](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def invalidate_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        prefixes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateEnvironmentResponse]:
        """Marks cached content as stale for one environment of the zone.

        Content cached
        for the zone's other environments, including production, is not affected.
        Otherwise this works like `POST /zones/{zone_id}/invalidate_cache`: the next
        request for invalidated content makes Cloudflare revalidate it with your origin,
        and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        delete the content instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/purge_cache`.

        Invalidating by URL (`files`) does not work for environments that select
        requests by IP address, country, ASN, or threat score, and fails with error
        `1136`. Use `tags`, `hosts`, `prefixes`, or `purge_everything` for those
        environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          prefixes: URL prefixes, each a hostname followed by a path, such as
              `www.example.com/blog/`. Targets all content whose URL starts with one of these
              prefixes. Do not include a scheme, query string, or fragment. See
              [Purge cache by prefix](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def invalidate_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        purge_everything: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateEnvironmentResponse]:
        """Marks cached content as stale for one environment of the zone.

        Content cached
        for the zone's other environments, including production, is not affected.
        Otherwise this works like `POST /zones/{zone_id}/invalidate_cache`: the next
        request for invalidated content makes Cloudflare revalidate it with your origin,
        and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        delete the content instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/purge_cache`.

        Invalidating by URL (`files`) does not work for environments that select
        requests by IP address, country, ASN, or threat score, and fails with error
        `1136`. Use `tags`, `hosts`, `prefixes`, or `purge_everything` for those
        environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          purge_everything: Set to `true` to target all cached content in the zone, or in the environment
              for the environment endpoints. Must be the only field in the request. See
              [Purge everything](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def invalidate_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        files: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateEnvironmentResponse]:
        """Marks cached content as stale for one environment of the zone.

        Content cached
        for the zone's other environments, including production, is not affected.
        Otherwise this works like `POST /zones/{zone_id}/invalidate_cache`: the next
        request for invalidated content makes Cloudflare revalidate it with your origin,
        and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        delete the content instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/purge_cache`.

        Invalidating by URL (`files`) does not work for environments that select
        requests by IP address, country, ASN, or threat score, and fails with error
        `1136`. Use `tags`, `hosts`, `prefixes`, or `purge_everything` for those
        environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: Full URLs, such as `https://www.example.com/css/styles.css`. Targets the content
              cached for each URL. If your cache key includes request headers, send objects
              with `url` and `headers` instead. See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def invalidate_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        files: Iterable[cache_invalidate_environment_params.CachePurgeSingleFileWithURLAndHeadersFile] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateEnvironmentResponse]:
        """Marks cached content as stale for one environment of the zone.

        Content cached
        for the zone's other environments, including production, is not affected.
        Otherwise this works like `POST /zones/{zone_id}/invalidate_cache`: the next
        request for invalidated content makes Cloudflare revalidate it with your origin,
        and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        delete the content instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/purge_cache`.

        Invalidating by URL (`files`) does not work for environments that select
        requests by IP address, country, ASN, or threat score, and fails with error
        `1136`. Use `tags`, `hosts`, `prefixes`, or `purge_everything` for those
        environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: URLs with the request headers your cache key uses. Use this form when your cache
              key includes request headers, or the visitor's device type, country, or
              language: send the header values each URL was cached with, such as
              `CF-Device-Type`, `CF-IPCountry`, or `Accept-Language`.

              When you send the `Origin` header, include the scheme and hostname. Include the
              port unless it is the default for the scheme: 80 for `http`, 443 for `https`.

              See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    def invalidate_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        hosts: SequenceNotStr[str] | Omit = omit,
        prefixes: SequenceNotStr[str] | Omit = omit,
        purge_everything: bool | Omit = omit,
        files: SequenceNotStr[str]
        | Iterable[cache_invalidate_environment_params.CachePurgeSingleFileWithURLAndHeadersFile]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateEnvironmentResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not environment_id:
            raise ValueError(f"Expected a non-empty value for `environment_id` but received {environment_id!r}")
        return self._post(
            path_template(
                "/zones/{zone_id}/environments/{environment_id}/invalidate_cache",
                zone_id=zone_id,
                environment_id=environment_id,
            ),
            body=maybe_transform(
                {
                    "tags": tags,
                    "hosts": hosts,
                    "prefixes": prefixes,
                    "purge_everything": purge_everything,
                    "files": files,
                },
                cache_invalidate_environment_params.CacheInvalidateEnvironmentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CacheInvalidateEnvironmentResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[CacheInvalidateEnvironmentResponse]], ResultWrapper[CacheInvalidateEnvironmentResponse]
            ),
        )

    @overload
    def purge(
        self,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeResponse]:
        """
        Deletes cached content in every Cloudflare data center and cache tier, including
        Cache Reserve. The next request for purged content is a cache `MISS`: Cloudflare
        fetches the full response from your origin and caches it again. Cloudflare does
        not serve purged content from cache again, even if your origin is unavailable.

        To keep content cached and have Cloudflare revalidate it with your origin
        instead, use `POST /zones/{zone_id}/invalidate_cache`.

        ### Choose what to purge

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. It
        does not confirm that any content was cached or removed. To check, request a
        purged URL and confirm that the `CF-Cache-Status` response header is `MISS`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          tags: Cache tags. Targets all content whose `Cache-Tag` response header contains at
              least one of these tags. See
              [Purge cache by cache-tags](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/).

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
        hosts: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeResponse]:
        """
        Deletes cached content in every Cloudflare data center and cache tier, including
        Cache Reserve. The next request for purged content is a cache `MISS`: Cloudflare
        fetches the full response from your origin and caches it again. Cloudflare does
        not serve purged content from cache again, even if your origin is unavailable.

        To keep content cached and have Cloudflare revalidate it with your origin
        instead, use `POST /zones/{zone_id}/invalidate_cache`.

        ### Choose what to purge

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. It
        does not confirm that any content was cached or removed. To check, request a
        purged URL and confirm that the `CF-Cache-Status` response header is `MISS`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          hosts: Hostnames, such as `www.example.com`. Targets all content cached for these
              hostnames. See
              [Purge cache by hostname](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/).

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
        prefixes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeResponse]:
        """
        Deletes cached content in every Cloudflare data center and cache tier, including
        Cache Reserve. The next request for purged content is a cache `MISS`: Cloudflare
        fetches the full response from your origin and caches it again. Cloudflare does
        not serve purged content from cache again, even if your origin is unavailable.

        To keep content cached and have Cloudflare revalidate it with your origin
        instead, use `POST /zones/{zone_id}/invalidate_cache`.

        ### Choose what to purge

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. It
        does not confirm that any content was cached or removed. To check, request a
        purged URL and confirm that the `CF-Cache-Status` response header is `MISS`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          prefixes: URL prefixes, each a hostname followed by a path, such as
              `www.example.com/blog/`. Targets all content whose URL starts with one of these
              prefixes. Do not include a scheme, query string, or fragment. See
              [Purge cache by prefix](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/).

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
        purge_everything: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeResponse]:
        """
        Deletes cached content in every Cloudflare data center and cache tier, including
        Cache Reserve. The next request for purged content is a cache `MISS`: Cloudflare
        fetches the full response from your origin and caches it again. Cloudflare does
        not serve purged content from cache again, even if your origin is unavailable.

        To keep content cached and have Cloudflare revalidate it with your origin
        instead, use `POST /zones/{zone_id}/invalidate_cache`.

        ### Choose what to purge

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. It
        does not confirm that any content was cached or removed. To check, request a
        purged URL and confirm that the `CF-Cache-Status` response header is `MISS`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          purge_everything: Set to `true` to target all cached content in the zone, or in the environment
              for the environment endpoints. Must be the only field in the request. See
              [Purge everything](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/).

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
        files: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeResponse]:
        """
        Deletes cached content in every Cloudflare data center and cache tier, including
        Cache Reserve. The next request for purged content is a cache `MISS`: Cloudflare
        fetches the full response from your origin and caches it again. Cloudflare does
        not serve purged content from cache again, even if your origin is unavailable.

        To keep content cached and have Cloudflare revalidate it with your origin
        instead, use `POST /zones/{zone_id}/invalidate_cache`.

        ### Choose what to purge

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. It
        does not confirm that any content was cached or removed. To check, request a
        purged URL and confirm that the `CF-Cache-Status` response header is `MISS`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: Full URLs, such as `https://www.example.com/css/styles.css`. Targets the content
              cached for each URL. If your cache key includes request headers, send objects
              with `url` and `headers` instead. See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

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
        files: Iterable[cache_purge_params.CachePurgeSingleFileWithURLAndHeadersFile] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeResponse]:
        """
        Deletes cached content in every Cloudflare data center and cache tier, including
        Cache Reserve. The next request for purged content is a cache `MISS`: Cloudflare
        fetches the full response from your origin and caches it again. Cloudflare does
        not serve purged content from cache again, even if your origin is unavailable.

        To keep content cached and have Cloudflare revalidate it with your origin
        instead, use `POST /zones/{zone_id}/invalidate_cache`.

        ### Choose what to purge

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. It
        does not confirm that any content was cached or removed. To check, request a
        purged URL and confirm that the `CF-Cache-Status` response header is `MISS`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: URLs with the request headers your cache key uses. Use this form when your cache
              key includes request headers, or the visitor's device type, country, or
              language: send the header values each URL was cached with, such as
              `CF-Device-Type`, `CF-IPCountry`, or `Accept-Language`.

              When you send the `Origin` header, include the scheme and hostname. Include the
              port unless it is the default for the scheme: 80 for `http`, 443 for `https`.

              See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    def purge(
        self,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        hosts: SequenceNotStr[str] | Omit = omit,
        prefixes: SequenceNotStr[str] | Omit = omit,
        purge_everything: bool | Omit = omit,
        files: SequenceNotStr[str]
        | Iterable[cache_purge_params.CachePurgeSingleFileWithURLAndHeadersFile]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            path_template("/zones/{zone_id}/purge_cache", zone_id=zone_id),
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
                post_parser=ResultWrapper[Optional[CachePurgeResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CachePurgeResponse]], ResultWrapper[CachePurgeResponse]),
        )

    @overload
    def purge_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeEnvironmentResponse]:
        """Deletes cached content for one environment of the zone.

        Content cached for the
        zone's other environments, including production, is not affected. Otherwise this
        works like `POST /zones/{zone_id}/purge_cache`: the next request for purged
        content is a cache `MISS`, and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        keep content cached and have Cloudflare revalidate it instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/invalidate_cache`.

        Purging by URL (`files`) does not work for environments that select requests by
        IP address, country, ASN, or threat score, and fails with error `1136`. Use
        `tags`, `hosts`, `prefixes`, or `purge_everything` for those environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          tags: Cache tags. Targets all content whose `Cache-Tag` response header contains at
              least one of these tags. See
              [Purge cache by cache-tags](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def purge_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        hosts: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeEnvironmentResponse]:
        """Deletes cached content for one environment of the zone.

        Content cached for the
        zone's other environments, including production, is not affected. Otherwise this
        works like `POST /zones/{zone_id}/purge_cache`: the next request for purged
        content is a cache `MISS`, and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        keep content cached and have Cloudflare revalidate it instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/invalidate_cache`.

        Purging by URL (`files`) does not work for environments that select requests by
        IP address, country, ASN, or threat score, and fails with error `1136`. Use
        `tags`, `hosts`, `prefixes`, or `purge_everything` for those environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          hosts: Hostnames, such as `www.example.com`. Targets all content cached for these
              hostnames. See
              [Purge cache by hostname](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def purge_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        prefixes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeEnvironmentResponse]:
        """Deletes cached content for one environment of the zone.

        Content cached for the
        zone's other environments, including production, is not affected. Otherwise this
        works like `POST /zones/{zone_id}/purge_cache`: the next request for purged
        content is a cache `MISS`, and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        keep content cached and have Cloudflare revalidate it instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/invalidate_cache`.

        Purging by URL (`files`) does not work for environments that select requests by
        IP address, country, ASN, or threat score, and fails with error `1136`. Use
        `tags`, `hosts`, `prefixes`, or `purge_everything` for those environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          prefixes: URL prefixes, each a hostname followed by a path, such as
              `www.example.com/blog/`. Targets all content whose URL starts with one of these
              prefixes. Do not include a scheme, query string, or fragment. See
              [Purge cache by prefix](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def purge_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        purge_everything: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeEnvironmentResponse]:
        """Deletes cached content for one environment of the zone.

        Content cached for the
        zone's other environments, including production, is not affected. Otherwise this
        works like `POST /zones/{zone_id}/purge_cache`: the next request for purged
        content is a cache `MISS`, and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        keep content cached and have Cloudflare revalidate it instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/invalidate_cache`.

        Purging by URL (`files`) does not work for environments that select requests by
        IP address, country, ASN, or threat score, and fails with error `1136`. Use
        `tags`, `hosts`, `prefixes`, or `purge_everything` for those environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          purge_everything: Set to `true` to target all cached content in the zone, or in the environment
              for the environment endpoints. Must be the only field in the request. See
              [Purge everything](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def purge_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        files: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeEnvironmentResponse]:
        """Deletes cached content for one environment of the zone.

        Content cached for the
        zone's other environments, including production, is not affected. Otherwise this
        works like `POST /zones/{zone_id}/purge_cache`: the next request for purged
        content is a cache `MISS`, and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        keep content cached and have Cloudflare revalidate it instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/invalidate_cache`.

        Purging by URL (`files`) does not work for environments that select requests by
        IP address, country, ASN, or threat score, and fails with error `1136`. Use
        `tags`, `hosts`, `prefixes`, or `purge_everything` for those environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: Full URLs, such as `https://www.example.com/css/styles.css`. Targets the content
              cached for each URL. If your cache key includes request headers, send objects
              with `url` and `headers` instead. See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def purge_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        files: Iterable[cache_purge_environment_params.CachePurgeSingleFileWithURLAndHeadersFile] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeEnvironmentResponse]:
        """Deletes cached content for one environment of the zone.

        Content cached for the
        zone's other environments, including production, is not affected. Otherwise this
        works like `POST /zones/{zone_id}/purge_cache`: the next request for purged
        content is a cache `MISS`, and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        keep content cached and have Cloudflare revalidate it instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/invalidate_cache`.

        Purging by URL (`files`) does not work for environments that select requests by
        IP address, country, ASN, or threat score, and fails with error `1136`. Use
        `tags`, `hosts`, `prefixes`, or `purge_everything` for those environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: URLs with the request headers your cache key uses. Use this form when your cache
              key includes request headers, or the visitor's device type, country, or
              language: send the header values each URL was cached with, such as
              `CF-Device-Type`, `CF-IPCountry`, or `Accept-Language`.

              When you send the `Origin` header, include the scheme and hostname. Include the
              port unless it is the default for the scheme: 80 for `http`, 443 for `https`.

              See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    def purge_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        hosts: SequenceNotStr[str] | Omit = omit,
        prefixes: SequenceNotStr[str] | Omit = omit,
        purge_everything: bool | Omit = omit,
        files: SequenceNotStr[str]
        | Iterable[cache_purge_environment_params.CachePurgeSingleFileWithURLAndHeadersFile]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeEnvironmentResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not environment_id:
            raise ValueError(f"Expected a non-empty value for `environment_id` but received {environment_id!r}")
        return self._post(
            path_template(
                "/zones/{zone_id}/environments/{environment_id}/purge_cache",
                zone_id=zone_id,
                environment_id=environment_id,
            ),
            body=maybe_transform(
                {
                    "tags": tags,
                    "hosts": hosts,
                    "prefixes": prefixes,
                    "purge_everything": purge_everything,
                    "files": files,
                },
                cache_purge_environment_params.CachePurgeEnvironmentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CachePurgeEnvironmentResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CachePurgeEnvironmentResponse]], ResultWrapper[CachePurgeEnvironmentResponse]),
        )


class AsyncCacheResource(AsyncAPIResource):
    @cached_property
    def cache_reserve(self) -> AsyncCacheReserveResource:
        return AsyncCacheReserveResource(self._client)

    @cached_property
    def smart_tiered_cache(self) -> AsyncSmartTieredCacheResource:
        return AsyncSmartTieredCacheResource(self._client)

    @cached_property
    def variants(self) -> AsyncVariantsResource:
        return AsyncVariantsResource(self._client)

    @cached_property
    def regional_tiered_cache(self) -> AsyncRegionalTieredCacheResource:
        return AsyncRegionalTieredCacheResource(self._client)

    @cached_property
    def origin_cloud_regions(self) -> AsyncOriginCloudRegionsResource:
        return AsyncOriginCloudRegionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCacheResourceWithStreamingResponse(self)

    @overload
    async def invalidate(
        self,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateResponse]:
        """
        Marks cached content as stale in every Cloudflare data center and cache tier,
        including Cache Reserve. The content stays in cache. The next request for it
        makes Cloudflare revalidate it with your origin, using the `ETag` and
        `Last-Modified` values it was cached with:

        - If your origin answers `304 Not Modified`, Cloudflare serves the cached copy
          without downloading it again, and `CF-Cache-Status` is `REVALIDATED`.
        - If your origin sends a full response, Cloudflare serves and caches the new
          content, and `CF-Cache-Status` is `EXPIRED`.

        With Tiered Cache, each tier revalidates with the tier above it, so a visitor
        can see `EXPIRED` even when your origin answered `304`.

        Until content is revalidated, your `stale-while-revalidate` and `stale-if-error`
        directives still apply, counted from the time you invalidated it. For example,
        if your origin fails during revalidation, Cloudflare can keep serving the stale
        copy for the `stale-if-error` window.

        ### Invalidate or purge?

        - **Invalidate** when content may not have changed, for example after a deploy.
          Unchanged content costs your origin a `304` instead of a full response. That
          saving needs an origin that sends `ETag` or `Last-Modified` and answers
          conditional requests. Otherwise, every revalidation downloads the full
          response.
        - **Purge**, with `POST /zones/{zone_id}/purge_cache`, when content must not be
          served again, for example content you removed for legal or security reasons.

        Invalidating takes the same request bodies as purging, needs the same
        permission, and counts against the same rate limits. After a broad invalidation,
        such as `purge_everything`, expect more conditional requests to your origin
        while visitors request the invalidated content again.

        ### Choose what to invalidate

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. To
        check, request an invalidated URL and confirm that the `CF-Cache-Status`
        response header is `REVALIDATED` or `EXPIRED`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          tags: Cache tags. Targets all content whose `Cache-Tag` response header contains at
              least one of these tags. See
              [Purge cache by cache-tags](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def invalidate(
        self,
        *,
        zone_id: str,
        hosts: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateResponse]:
        """
        Marks cached content as stale in every Cloudflare data center and cache tier,
        including Cache Reserve. The content stays in cache. The next request for it
        makes Cloudflare revalidate it with your origin, using the `ETag` and
        `Last-Modified` values it was cached with:

        - If your origin answers `304 Not Modified`, Cloudflare serves the cached copy
          without downloading it again, and `CF-Cache-Status` is `REVALIDATED`.
        - If your origin sends a full response, Cloudflare serves and caches the new
          content, and `CF-Cache-Status` is `EXPIRED`.

        With Tiered Cache, each tier revalidates with the tier above it, so a visitor
        can see `EXPIRED` even when your origin answered `304`.

        Until content is revalidated, your `stale-while-revalidate` and `stale-if-error`
        directives still apply, counted from the time you invalidated it. For example,
        if your origin fails during revalidation, Cloudflare can keep serving the stale
        copy for the `stale-if-error` window.

        ### Invalidate or purge?

        - **Invalidate** when content may not have changed, for example after a deploy.
          Unchanged content costs your origin a `304` instead of a full response. That
          saving needs an origin that sends `ETag` or `Last-Modified` and answers
          conditional requests. Otherwise, every revalidation downloads the full
          response.
        - **Purge**, with `POST /zones/{zone_id}/purge_cache`, when content must not be
          served again, for example content you removed for legal or security reasons.

        Invalidating takes the same request bodies as purging, needs the same
        permission, and counts against the same rate limits. After a broad invalidation,
        such as `purge_everything`, expect more conditional requests to your origin
        while visitors request the invalidated content again.

        ### Choose what to invalidate

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. To
        check, request an invalidated URL and confirm that the `CF-Cache-Status`
        response header is `REVALIDATED` or `EXPIRED`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          hosts: Hostnames, such as `www.example.com`. Targets all content cached for these
              hostnames. See
              [Purge cache by hostname](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def invalidate(
        self,
        *,
        zone_id: str,
        prefixes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateResponse]:
        """
        Marks cached content as stale in every Cloudflare data center and cache tier,
        including Cache Reserve. The content stays in cache. The next request for it
        makes Cloudflare revalidate it with your origin, using the `ETag` and
        `Last-Modified` values it was cached with:

        - If your origin answers `304 Not Modified`, Cloudflare serves the cached copy
          without downloading it again, and `CF-Cache-Status` is `REVALIDATED`.
        - If your origin sends a full response, Cloudflare serves and caches the new
          content, and `CF-Cache-Status` is `EXPIRED`.

        With Tiered Cache, each tier revalidates with the tier above it, so a visitor
        can see `EXPIRED` even when your origin answered `304`.

        Until content is revalidated, your `stale-while-revalidate` and `stale-if-error`
        directives still apply, counted from the time you invalidated it. For example,
        if your origin fails during revalidation, Cloudflare can keep serving the stale
        copy for the `stale-if-error` window.

        ### Invalidate or purge?

        - **Invalidate** when content may not have changed, for example after a deploy.
          Unchanged content costs your origin a `304` instead of a full response. That
          saving needs an origin that sends `ETag` or `Last-Modified` and answers
          conditional requests. Otherwise, every revalidation downloads the full
          response.
        - **Purge**, with `POST /zones/{zone_id}/purge_cache`, when content must not be
          served again, for example content you removed for legal or security reasons.

        Invalidating takes the same request bodies as purging, needs the same
        permission, and counts against the same rate limits. After a broad invalidation,
        such as `purge_everything`, expect more conditional requests to your origin
        while visitors request the invalidated content again.

        ### Choose what to invalidate

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. To
        check, request an invalidated URL and confirm that the `CF-Cache-Status`
        response header is `REVALIDATED` or `EXPIRED`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          prefixes: URL prefixes, each a hostname followed by a path, such as
              `www.example.com/blog/`. Targets all content whose URL starts with one of these
              prefixes. Do not include a scheme, query string, or fragment. See
              [Purge cache by prefix](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def invalidate(
        self,
        *,
        zone_id: str,
        purge_everything: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateResponse]:
        """
        Marks cached content as stale in every Cloudflare data center and cache tier,
        including Cache Reserve. The content stays in cache. The next request for it
        makes Cloudflare revalidate it with your origin, using the `ETag` and
        `Last-Modified` values it was cached with:

        - If your origin answers `304 Not Modified`, Cloudflare serves the cached copy
          without downloading it again, and `CF-Cache-Status` is `REVALIDATED`.
        - If your origin sends a full response, Cloudflare serves and caches the new
          content, and `CF-Cache-Status` is `EXPIRED`.

        With Tiered Cache, each tier revalidates with the tier above it, so a visitor
        can see `EXPIRED` even when your origin answered `304`.

        Until content is revalidated, your `stale-while-revalidate` and `stale-if-error`
        directives still apply, counted from the time you invalidated it. For example,
        if your origin fails during revalidation, Cloudflare can keep serving the stale
        copy for the `stale-if-error` window.

        ### Invalidate or purge?

        - **Invalidate** when content may not have changed, for example after a deploy.
          Unchanged content costs your origin a `304` instead of a full response. That
          saving needs an origin that sends `ETag` or `Last-Modified` and answers
          conditional requests. Otherwise, every revalidation downloads the full
          response.
        - **Purge**, with `POST /zones/{zone_id}/purge_cache`, when content must not be
          served again, for example content you removed for legal or security reasons.

        Invalidating takes the same request bodies as purging, needs the same
        permission, and counts against the same rate limits. After a broad invalidation,
        such as `purge_everything`, expect more conditional requests to your origin
        while visitors request the invalidated content again.

        ### Choose what to invalidate

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. To
        check, request an invalidated URL and confirm that the `CF-Cache-Status`
        response header is `REVALIDATED` or `EXPIRED`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          purge_everything: Set to `true` to target all cached content in the zone, or in the environment
              for the environment endpoints. Must be the only field in the request. See
              [Purge everything](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def invalidate(
        self,
        *,
        zone_id: str,
        files: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateResponse]:
        """
        Marks cached content as stale in every Cloudflare data center and cache tier,
        including Cache Reserve. The content stays in cache. The next request for it
        makes Cloudflare revalidate it with your origin, using the `ETag` and
        `Last-Modified` values it was cached with:

        - If your origin answers `304 Not Modified`, Cloudflare serves the cached copy
          without downloading it again, and `CF-Cache-Status` is `REVALIDATED`.
        - If your origin sends a full response, Cloudflare serves and caches the new
          content, and `CF-Cache-Status` is `EXPIRED`.

        With Tiered Cache, each tier revalidates with the tier above it, so a visitor
        can see `EXPIRED` even when your origin answered `304`.

        Until content is revalidated, your `stale-while-revalidate` and `stale-if-error`
        directives still apply, counted from the time you invalidated it. For example,
        if your origin fails during revalidation, Cloudflare can keep serving the stale
        copy for the `stale-if-error` window.

        ### Invalidate or purge?

        - **Invalidate** when content may not have changed, for example after a deploy.
          Unchanged content costs your origin a `304` instead of a full response. That
          saving needs an origin that sends `ETag` or `Last-Modified` and answers
          conditional requests. Otherwise, every revalidation downloads the full
          response.
        - **Purge**, with `POST /zones/{zone_id}/purge_cache`, when content must not be
          served again, for example content you removed for legal or security reasons.

        Invalidating takes the same request bodies as purging, needs the same
        permission, and counts against the same rate limits. After a broad invalidation,
        such as `purge_everything`, expect more conditional requests to your origin
        while visitors request the invalidated content again.

        ### Choose what to invalidate

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. To
        check, request an invalidated URL and confirm that the `CF-Cache-Status`
        response header is `REVALIDATED` or `EXPIRED`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: Full URLs, such as `https://www.example.com/css/styles.css`. Targets the content
              cached for each URL. If your cache key includes request headers, send objects
              with `url` and `headers` instead. See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def invalidate(
        self,
        *,
        zone_id: str,
        files: Iterable[cache_invalidate_params.CachePurgeSingleFileWithURLAndHeadersFile] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateResponse]:
        """
        Marks cached content as stale in every Cloudflare data center and cache tier,
        including Cache Reserve. The content stays in cache. The next request for it
        makes Cloudflare revalidate it with your origin, using the `ETag` and
        `Last-Modified` values it was cached with:

        - If your origin answers `304 Not Modified`, Cloudflare serves the cached copy
          without downloading it again, and `CF-Cache-Status` is `REVALIDATED`.
        - If your origin sends a full response, Cloudflare serves and caches the new
          content, and `CF-Cache-Status` is `EXPIRED`.

        With Tiered Cache, each tier revalidates with the tier above it, so a visitor
        can see `EXPIRED` even when your origin answered `304`.

        Until content is revalidated, your `stale-while-revalidate` and `stale-if-error`
        directives still apply, counted from the time you invalidated it. For example,
        if your origin fails during revalidation, Cloudflare can keep serving the stale
        copy for the `stale-if-error` window.

        ### Invalidate or purge?

        - **Invalidate** when content may not have changed, for example after a deploy.
          Unchanged content costs your origin a `304` instead of a full response. That
          saving needs an origin that sends `ETag` or `Last-Modified` and answers
          conditional requests. Otherwise, every revalidation downloads the full
          response.
        - **Purge**, with `POST /zones/{zone_id}/purge_cache`, when content must not be
          served again, for example content you removed for legal or security reasons.

        Invalidating takes the same request bodies as purging, needs the same
        permission, and counts against the same rate limits. After a broad invalidation,
        such as `purge_everything`, expect more conditional requests to your origin
        while visitors request the invalidated content again.

        ### Choose what to invalidate

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. To
        check, request an invalidated URL and confirm that the `CF-Cache-Status`
        response header is `REVALIDATED` or `EXPIRED`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: URLs with the request headers your cache key uses. Use this form when your cache
              key includes request headers, or the visitor's device type, country, or
              language: send the header values each URL was cached with, such as
              `CF-Device-Type`, `CF-IPCountry`, or `Accept-Language`.

              When you send the `Origin` header, include the scheme and hostname. Include the
              port unless it is the default for the scheme: 80 for `http`, 443 for `https`.

              See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    async def invalidate(
        self,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        hosts: SequenceNotStr[str] | Omit = omit,
        prefixes: SequenceNotStr[str] | Omit = omit,
        purge_everything: bool | Omit = omit,
        files: SequenceNotStr[str]
        | Iterable[cache_invalidate_params.CachePurgeSingleFileWithURLAndHeadersFile]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            path_template("/zones/{zone_id}/invalidate_cache", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "tags": tags,
                    "hosts": hosts,
                    "prefixes": prefixes,
                    "purge_everything": purge_everything,
                    "files": files,
                },
                cache_invalidate_params.CacheInvalidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CacheInvalidateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CacheInvalidateResponse]], ResultWrapper[CacheInvalidateResponse]),
        )

    @overload
    async def invalidate_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateEnvironmentResponse]:
        """Marks cached content as stale for one environment of the zone.

        Content cached
        for the zone's other environments, including production, is not affected.
        Otherwise this works like `POST /zones/{zone_id}/invalidate_cache`: the next
        request for invalidated content makes Cloudflare revalidate it with your origin,
        and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        delete the content instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/purge_cache`.

        Invalidating by URL (`files`) does not work for environments that select
        requests by IP address, country, ASN, or threat score, and fails with error
        `1136`. Use `tags`, `hosts`, `prefixes`, or `purge_everything` for those
        environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          tags: Cache tags. Targets all content whose `Cache-Tag` response header contains at
              least one of these tags. See
              [Purge cache by cache-tags](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def invalidate_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        hosts: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateEnvironmentResponse]:
        """Marks cached content as stale for one environment of the zone.

        Content cached
        for the zone's other environments, including production, is not affected.
        Otherwise this works like `POST /zones/{zone_id}/invalidate_cache`: the next
        request for invalidated content makes Cloudflare revalidate it with your origin,
        and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        delete the content instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/purge_cache`.

        Invalidating by URL (`files`) does not work for environments that select
        requests by IP address, country, ASN, or threat score, and fails with error
        `1136`. Use `tags`, `hosts`, `prefixes`, or `purge_everything` for those
        environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          hosts: Hostnames, such as `www.example.com`. Targets all content cached for these
              hostnames. See
              [Purge cache by hostname](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def invalidate_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        prefixes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateEnvironmentResponse]:
        """Marks cached content as stale for one environment of the zone.

        Content cached
        for the zone's other environments, including production, is not affected.
        Otherwise this works like `POST /zones/{zone_id}/invalidate_cache`: the next
        request for invalidated content makes Cloudflare revalidate it with your origin,
        and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        delete the content instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/purge_cache`.

        Invalidating by URL (`files`) does not work for environments that select
        requests by IP address, country, ASN, or threat score, and fails with error
        `1136`. Use `tags`, `hosts`, `prefixes`, or `purge_everything` for those
        environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          prefixes: URL prefixes, each a hostname followed by a path, such as
              `www.example.com/blog/`. Targets all content whose URL starts with one of these
              prefixes. Do not include a scheme, query string, or fragment. See
              [Purge cache by prefix](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def invalidate_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        purge_everything: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateEnvironmentResponse]:
        """Marks cached content as stale for one environment of the zone.

        Content cached
        for the zone's other environments, including production, is not affected.
        Otherwise this works like `POST /zones/{zone_id}/invalidate_cache`: the next
        request for invalidated content makes Cloudflare revalidate it with your origin,
        and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        delete the content instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/purge_cache`.

        Invalidating by URL (`files`) does not work for environments that select
        requests by IP address, country, ASN, or threat score, and fails with error
        `1136`. Use `tags`, `hosts`, `prefixes`, or `purge_everything` for those
        environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          purge_everything: Set to `true` to target all cached content in the zone, or in the environment
              for the environment endpoints. Must be the only field in the request. See
              [Purge everything](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def invalidate_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        files: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateEnvironmentResponse]:
        """Marks cached content as stale for one environment of the zone.

        Content cached
        for the zone's other environments, including production, is not affected.
        Otherwise this works like `POST /zones/{zone_id}/invalidate_cache`: the next
        request for invalidated content makes Cloudflare revalidate it with your origin,
        and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        delete the content instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/purge_cache`.

        Invalidating by URL (`files`) does not work for environments that select
        requests by IP address, country, ASN, or threat score, and fails with error
        `1136`. Use `tags`, `hosts`, `prefixes`, or `purge_everything` for those
        environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: Full URLs, such as `https://www.example.com/css/styles.css`. Targets the content
              cached for each URL. If your cache key includes request headers, send objects
              with `url` and `headers` instead. See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def invalidate_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        files: Iterable[cache_invalidate_environment_params.CachePurgeSingleFileWithURLAndHeadersFile] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateEnvironmentResponse]:
        """Marks cached content as stale for one environment of the zone.

        Content cached
        for the zone's other environments, including production, is not affected.
        Otherwise this works like `POST /zones/{zone_id}/invalidate_cache`: the next
        request for invalidated content makes Cloudflare revalidate it with your origin,
        and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        delete the content instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/purge_cache`.

        Invalidating by URL (`files`) does not work for environments that select
        requests by IP address, country, ASN, or threat score, and fails with error
        `1136`. Use `tags`, `hosts`, `prefixes`, or `purge_everything` for those
        environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: URLs with the request headers your cache key uses. Use this form when your cache
              key includes request headers, or the visitor's device type, country, or
              language: send the header values each URL was cached with, such as
              `CF-Device-Type`, `CF-IPCountry`, or `Accept-Language`.

              When you send the `Origin` header, include the scheme and hostname. Include the
              port unless it is the default for the scheme: 80 for `http`, 443 for `https`.

              See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    async def invalidate_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        hosts: SequenceNotStr[str] | Omit = omit,
        prefixes: SequenceNotStr[str] | Omit = omit,
        purge_everything: bool | Omit = omit,
        files: SequenceNotStr[str]
        | Iterable[cache_invalidate_environment_params.CachePurgeSingleFileWithURLAndHeadersFile]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CacheInvalidateEnvironmentResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not environment_id:
            raise ValueError(f"Expected a non-empty value for `environment_id` but received {environment_id!r}")
        return await self._post(
            path_template(
                "/zones/{zone_id}/environments/{environment_id}/invalidate_cache",
                zone_id=zone_id,
                environment_id=environment_id,
            ),
            body=await async_maybe_transform(
                {
                    "tags": tags,
                    "hosts": hosts,
                    "prefixes": prefixes,
                    "purge_everything": purge_everything,
                    "files": files,
                },
                cache_invalidate_environment_params.CacheInvalidateEnvironmentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CacheInvalidateEnvironmentResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[CacheInvalidateEnvironmentResponse]], ResultWrapper[CacheInvalidateEnvironmentResponse]
            ),
        )

    @overload
    async def purge(
        self,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeResponse]:
        """
        Deletes cached content in every Cloudflare data center and cache tier, including
        Cache Reserve. The next request for purged content is a cache `MISS`: Cloudflare
        fetches the full response from your origin and caches it again. Cloudflare does
        not serve purged content from cache again, even if your origin is unavailable.

        To keep content cached and have Cloudflare revalidate it with your origin
        instead, use `POST /zones/{zone_id}/invalidate_cache`.

        ### Choose what to purge

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. It
        does not confirm that any content was cached or removed. To check, request a
        purged URL and confirm that the `CF-Cache-Status` response header is `MISS`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          tags: Cache tags. Targets all content whose `Cache-Tag` response header contains at
              least one of these tags. See
              [Purge cache by cache-tags](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/).

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
        hosts: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeResponse]:
        """
        Deletes cached content in every Cloudflare data center and cache tier, including
        Cache Reserve. The next request for purged content is a cache `MISS`: Cloudflare
        fetches the full response from your origin and caches it again. Cloudflare does
        not serve purged content from cache again, even if your origin is unavailable.

        To keep content cached and have Cloudflare revalidate it with your origin
        instead, use `POST /zones/{zone_id}/invalidate_cache`.

        ### Choose what to purge

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. It
        does not confirm that any content was cached or removed. To check, request a
        purged URL and confirm that the `CF-Cache-Status` response header is `MISS`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          hosts: Hostnames, such as `www.example.com`. Targets all content cached for these
              hostnames. See
              [Purge cache by hostname](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/).

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
        prefixes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeResponse]:
        """
        Deletes cached content in every Cloudflare data center and cache tier, including
        Cache Reserve. The next request for purged content is a cache `MISS`: Cloudflare
        fetches the full response from your origin and caches it again. Cloudflare does
        not serve purged content from cache again, even if your origin is unavailable.

        To keep content cached and have Cloudflare revalidate it with your origin
        instead, use `POST /zones/{zone_id}/invalidate_cache`.

        ### Choose what to purge

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. It
        does not confirm that any content was cached or removed. To check, request a
        purged URL and confirm that the `CF-Cache-Status` response header is `MISS`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          prefixes: URL prefixes, each a hostname followed by a path, such as
              `www.example.com/blog/`. Targets all content whose URL starts with one of these
              prefixes. Do not include a scheme, query string, or fragment. See
              [Purge cache by prefix](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/).

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
        purge_everything: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeResponse]:
        """
        Deletes cached content in every Cloudflare data center and cache tier, including
        Cache Reserve. The next request for purged content is a cache `MISS`: Cloudflare
        fetches the full response from your origin and caches it again. Cloudflare does
        not serve purged content from cache again, even if your origin is unavailable.

        To keep content cached and have Cloudflare revalidate it with your origin
        instead, use `POST /zones/{zone_id}/invalidate_cache`.

        ### Choose what to purge

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. It
        does not confirm that any content was cached or removed. To check, request a
        purged URL and confirm that the `CF-Cache-Status` response header is `MISS`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          purge_everything: Set to `true` to target all cached content in the zone, or in the environment
              for the environment endpoints. Must be the only field in the request. See
              [Purge everything](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/).

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
        files: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeResponse]:
        """
        Deletes cached content in every Cloudflare data center and cache tier, including
        Cache Reserve. The next request for purged content is a cache `MISS`: Cloudflare
        fetches the full response from your origin and caches it again. Cloudflare does
        not serve purged content from cache again, even if your origin is unavailable.

        To keep content cached and have Cloudflare revalidate it with your origin
        instead, use `POST /zones/{zone_id}/invalidate_cache`.

        ### Choose what to purge

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. It
        does not confirm that any content was cached or removed. To check, request a
        purged URL and confirm that the `CF-Cache-Status` response header is `MISS`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: Full URLs, such as `https://www.example.com/css/styles.css`. Targets the content
              cached for each URL. If your cache key includes request headers, send objects
              with `url` and `headers` instead. See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

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
        files: Iterable[cache_purge_params.CachePurgeSingleFileWithURLAndHeadersFile] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeResponse]:
        """
        Deletes cached content in every Cloudflare data center and cache tier, including
        Cache Reserve. The next request for purged content is a cache `MISS`: Cloudflare
        fetches the full response from your origin and caches it again. Cloudflare does
        not serve purged content from cache again, even if your origin is unavailable.

        To keep content cached and have Cloudflare revalidate it with your origin
        instead, use `POST /zones/{zone_id}/invalidate_cache`.

        ### Choose what to purge

        Send one of these fields in the request body:

        - `files`: specific URLs. If your cache key includes request headers, send each
          URL with the header values it was cached with.
        - `tags`: all content whose `Cache-Tag` response header contains one of the
          tags.
        - `hosts`: all content cached for the hostnames.
        - `prefixes`: all content whose URL starts with one of the prefixes.
        - `purge_everything`: all cached content in the zone.

        ### Check the result

        A `200` response with `success: true` means Cloudflare accepted the request. It
        does not confirm that any content was cached or removed. To check, request a
        purged URL and confirm that the `CF-Cache-Status` response header is `MISS`.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: URLs with the request headers your cache key uses. Use this form when your cache
              key includes request headers, or the visitor's device type, country, or
              language: send the header values each URL was cached with, such as
              `CF-Device-Type`, `CF-IPCountry`, or `Accept-Language`.

              When you send the `Origin` header, include the scheme and hostname. Include the
              port unless it is the default for the scheme: 80 for `http`, 443 for `https`.

              See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    async def purge(
        self,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        hosts: SequenceNotStr[str] | Omit = omit,
        prefixes: SequenceNotStr[str] | Omit = omit,
        purge_everything: bool | Omit = omit,
        files: SequenceNotStr[str]
        | Iterable[cache_purge_params.CachePurgeSingleFileWithURLAndHeadersFile]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            path_template("/zones/{zone_id}/purge_cache", zone_id=zone_id),
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
                post_parser=ResultWrapper[Optional[CachePurgeResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CachePurgeResponse]], ResultWrapper[CachePurgeResponse]),
        )

    @overload
    async def purge_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeEnvironmentResponse]:
        """Deletes cached content for one environment of the zone.

        Content cached for the
        zone's other environments, including production, is not affected. Otherwise this
        works like `POST /zones/{zone_id}/purge_cache`: the next request for purged
        content is a cache `MISS`, and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        keep content cached and have Cloudflare revalidate it instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/invalidate_cache`.

        Purging by URL (`files`) does not work for environments that select requests by
        IP address, country, ASN, or threat score, and fails with error `1136`. Use
        `tags`, `hosts`, `prefixes`, or `purge_everything` for those environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          tags: Cache tags. Targets all content whose `Cache-Tag` response header contains at
              least one of these tags. See
              [Purge cache by cache-tags](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def purge_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        hosts: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeEnvironmentResponse]:
        """Deletes cached content for one environment of the zone.

        Content cached for the
        zone's other environments, including production, is not affected. Otherwise this
        works like `POST /zones/{zone_id}/purge_cache`: the next request for purged
        content is a cache `MISS`, and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        keep content cached and have Cloudflare revalidate it instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/invalidate_cache`.

        Purging by URL (`files`) does not work for environments that select requests by
        IP address, country, ASN, or threat score, and fails with error `1136`. Use
        `tags`, `hosts`, `prefixes`, or `purge_everything` for those environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          hosts: Hostnames, such as `www.example.com`. Targets all content cached for these
              hostnames. See
              [Purge cache by hostname](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def purge_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        prefixes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeEnvironmentResponse]:
        """Deletes cached content for one environment of the zone.

        Content cached for the
        zone's other environments, including production, is not affected. Otherwise this
        works like `POST /zones/{zone_id}/purge_cache`: the next request for purged
        content is a cache `MISS`, and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        keep content cached and have Cloudflare revalidate it instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/invalidate_cache`.

        Purging by URL (`files`) does not work for environments that select requests by
        IP address, country, ASN, or threat score, and fails with error `1136`. Use
        `tags`, `hosts`, `prefixes`, or `purge_everything` for those environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          prefixes: URL prefixes, each a hostname followed by a path, such as
              `www.example.com/blog/`. Targets all content whose URL starts with one of these
              prefixes. Do not include a scheme, query string, or fragment. See
              [Purge cache by prefix](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def purge_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        purge_everything: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeEnvironmentResponse]:
        """Deletes cached content for one environment of the zone.

        Content cached for the
        zone's other environments, including production, is not affected. Otherwise this
        works like `POST /zones/{zone_id}/purge_cache`: the next request for purged
        content is a cache `MISS`, and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        keep content cached and have Cloudflare revalidate it instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/invalidate_cache`.

        Purging by URL (`files`) does not work for environments that select requests by
        IP address, country, ASN, or threat score, and fails with error `1136`. Use
        `tags`, `hosts`, `prefixes`, or `purge_everything` for those environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          purge_everything: Set to `true` to target all cached content in the zone, or in the environment
              for the environment endpoints. Must be the only field in the request. See
              [Purge everything](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def purge_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        files: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeEnvironmentResponse]:
        """Deletes cached content for one environment of the zone.

        Content cached for the
        zone's other environments, including production, is not affected. Otherwise this
        works like `POST /zones/{zone_id}/purge_cache`: the next request for purged
        content is a cache `MISS`, and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        keep content cached and have Cloudflare revalidate it instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/invalidate_cache`.

        Purging by URL (`files`) does not work for environments that select requests by
        IP address, country, ASN, or threat score, and fails with error `1136`. Use
        `tags`, `hosts`, `prefixes`, or `purge_everything` for those environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: Full URLs, such as `https://www.example.com/css/styles.css`. Targets the content
              cached for each URL. If your cache key includes request headers, send objects
              with `url` and `headers` instead. See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def purge_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        files: Iterable[cache_purge_environment_params.CachePurgeSingleFileWithURLAndHeadersFile] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeEnvironmentResponse]:
        """Deletes cached content for one environment of the zone.

        Content cached for the
        zone's other environments, including production, is not affected. Otherwise this
        works like `POST /zones/{zone_id}/purge_cache`: the next request for purged
        content is a cache `MISS`, and the request body takes the same fields.

        Environments are part of
        [Version Management](https://developers.cloudflare.com/version-management/). To
        keep content cached and have Cloudflare revalidate it instead, use
        `POST /zones/{zone_id}/environments/{environment_id}/invalidate_cache`.

        Purging by URL (`files`) does not work for environments that select requests by
        IP address, country, ASN, or threat score, and fails with error `1136`. Use
        `tags`, `hosts`, `prefixes`, or `purge_everything` for those environments.

        ### Availability and limits

        Rate limits and the number of items you can send in one request depend on your
        plan. See
        [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: URLs with the request headers your cache key uses. Use this form when your cache
              key includes request headers, or the visitor's device type, country, or
              language: send the header values each URL was cached with, such as
              `CF-Device-Type`, `CF-IPCountry`, or `Accept-Language`.

              When you send the `Origin` header, include the scheme and hostname. Include the
              port unless it is the default for the scheme: 80 for `http`, 443 for `https`.

              See
              [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    async def purge_environment(
        self,
        environment_id: str,
        *,
        zone_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        hosts: SequenceNotStr[str] | Omit = omit,
        prefixes: SequenceNotStr[str] | Omit = omit,
        purge_everything: bool | Omit = omit,
        files: SequenceNotStr[str]
        | Iterable[cache_purge_environment_params.CachePurgeSingleFileWithURLAndHeadersFile]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CachePurgeEnvironmentResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not environment_id:
            raise ValueError(f"Expected a non-empty value for `environment_id` but received {environment_id!r}")
        return await self._post(
            path_template(
                "/zones/{zone_id}/environments/{environment_id}/purge_cache",
                zone_id=zone_id,
                environment_id=environment_id,
            ),
            body=await async_maybe_transform(
                {
                    "tags": tags,
                    "hosts": hosts,
                    "prefixes": prefixes,
                    "purge_everything": purge_everything,
                    "files": files,
                },
                cache_purge_environment_params.CachePurgeEnvironmentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CachePurgeEnvironmentResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CachePurgeEnvironmentResponse]], ResultWrapper[CachePurgeEnvironmentResponse]),
        )


class CacheResourceWithRawResponse:
    def __init__(self, cache: CacheResource) -> None:
        self._cache = cache

        self.invalidate = to_raw_response_wrapper(
            cache.invalidate,
        )
        self.invalidate_environment = to_raw_response_wrapper(
            cache.invalidate_environment,
        )
        self.purge = to_raw_response_wrapper(
            cache.purge,
        )
        self.purge_environment = to_raw_response_wrapper(
            cache.purge_environment,
        )

    @cached_property
    def cache_reserve(self) -> CacheReserveResourceWithRawResponse:
        return CacheReserveResourceWithRawResponse(self._cache.cache_reserve)

    @cached_property
    def smart_tiered_cache(self) -> SmartTieredCacheResourceWithRawResponse:
        return SmartTieredCacheResourceWithRawResponse(self._cache.smart_tiered_cache)

    @cached_property
    def variants(self) -> VariantsResourceWithRawResponse:
        return VariantsResourceWithRawResponse(self._cache.variants)

    @cached_property
    def regional_tiered_cache(self) -> RegionalTieredCacheResourceWithRawResponse:
        return RegionalTieredCacheResourceWithRawResponse(self._cache.regional_tiered_cache)

    @cached_property
    def origin_cloud_regions(self) -> OriginCloudRegionsResourceWithRawResponse:
        return OriginCloudRegionsResourceWithRawResponse(self._cache.origin_cloud_regions)


class AsyncCacheResourceWithRawResponse:
    def __init__(self, cache: AsyncCacheResource) -> None:
        self._cache = cache

        self.invalidate = async_to_raw_response_wrapper(
            cache.invalidate,
        )
        self.invalidate_environment = async_to_raw_response_wrapper(
            cache.invalidate_environment,
        )
        self.purge = async_to_raw_response_wrapper(
            cache.purge,
        )
        self.purge_environment = async_to_raw_response_wrapper(
            cache.purge_environment,
        )

    @cached_property
    def cache_reserve(self) -> AsyncCacheReserveResourceWithRawResponse:
        return AsyncCacheReserveResourceWithRawResponse(self._cache.cache_reserve)

    @cached_property
    def smart_tiered_cache(self) -> AsyncSmartTieredCacheResourceWithRawResponse:
        return AsyncSmartTieredCacheResourceWithRawResponse(self._cache.smart_tiered_cache)

    @cached_property
    def variants(self) -> AsyncVariantsResourceWithRawResponse:
        return AsyncVariantsResourceWithRawResponse(self._cache.variants)

    @cached_property
    def regional_tiered_cache(self) -> AsyncRegionalTieredCacheResourceWithRawResponse:
        return AsyncRegionalTieredCacheResourceWithRawResponse(self._cache.regional_tiered_cache)

    @cached_property
    def origin_cloud_regions(self) -> AsyncOriginCloudRegionsResourceWithRawResponse:
        return AsyncOriginCloudRegionsResourceWithRawResponse(self._cache.origin_cloud_regions)


class CacheResourceWithStreamingResponse:
    def __init__(self, cache: CacheResource) -> None:
        self._cache = cache

        self.invalidate = to_streamed_response_wrapper(
            cache.invalidate,
        )
        self.invalidate_environment = to_streamed_response_wrapper(
            cache.invalidate_environment,
        )
        self.purge = to_streamed_response_wrapper(
            cache.purge,
        )
        self.purge_environment = to_streamed_response_wrapper(
            cache.purge_environment,
        )

    @cached_property
    def cache_reserve(self) -> CacheReserveResourceWithStreamingResponse:
        return CacheReserveResourceWithStreamingResponse(self._cache.cache_reserve)

    @cached_property
    def smart_tiered_cache(self) -> SmartTieredCacheResourceWithStreamingResponse:
        return SmartTieredCacheResourceWithStreamingResponse(self._cache.smart_tiered_cache)

    @cached_property
    def variants(self) -> VariantsResourceWithStreamingResponse:
        return VariantsResourceWithStreamingResponse(self._cache.variants)

    @cached_property
    def regional_tiered_cache(self) -> RegionalTieredCacheResourceWithStreamingResponse:
        return RegionalTieredCacheResourceWithStreamingResponse(self._cache.regional_tiered_cache)

    @cached_property
    def origin_cloud_regions(self) -> OriginCloudRegionsResourceWithStreamingResponse:
        return OriginCloudRegionsResourceWithStreamingResponse(self._cache.origin_cloud_regions)


class AsyncCacheResourceWithStreamingResponse:
    def __init__(self, cache: AsyncCacheResource) -> None:
        self._cache = cache

        self.invalidate = async_to_streamed_response_wrapper(
            cache.invalidate,
        )
        self.invalidate_environment = async_to_streamed_response_wrapper(
            cache.invalidate_environment,
        )
        self.purge = async_to_streamed_response_wrapper(
            cache.purge,
        )
        self.purge_environment = async_to_streamed_response_wrapper(
            cache.purge_environment,
        )

    @cached_property
    def cache_reserve(self) -> AsyncCacheReserveResourceWithStreamingResponse:
        return AsyncCacheReserveResourceWithStreamingResponse(self._cache.cache_reserve)

    @cached_property
    def smart_tiered_cache(self) -> AsyncSmartTieredCacheResourceWithStreamingResponse:
        return AsyncSmartTieredCacheResourceWithStreamingResponse(self._cache.smart_tiered_cache)

    @cached_property
    def variants(self) -> AsyncVariantsResourceWithStreamingResponse:
        return AsyncVariantsResourceWithStreamingResponse(self._cache.variants)

    @cached_property
    def regional_tiered_cache(self) -> AsyncRegionalTieredCacheResourceWithStreamingResponse:
        return AsyncRegionalTieredCacheResourceWithStreamingResponse(self._cache.regional_tiered_cache)

    @cached_property
    def origin_cloud_regions(self) -> AsyncOriginCloudRegionsResourceWithStreamingResponse:
        return AsyncOriginCloudRegionsResourceWithStreamingResponse(self._cache.origin_cloud_regions)
