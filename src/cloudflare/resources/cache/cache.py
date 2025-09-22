# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast
from typing_extensions import overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.cache import cache_purge_params
from ..._base_client import make_request_options
from ...types.cache.cache_purge_response import CachePurgeResponse

__all__ = ["CacheResource", "AsyncCacheResource"]


class CacheResource(SyncAPIResource):
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
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ```
        {"purge_everything": true}
        ```

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

        Single file purge example with files:

        ```
        {"files": ["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"]}
        ```

        Single file purge example with url and header pairs:

        ```
        {
            "files": [
                {
                    url: "http://www.example.com/cat_picture.jpg",
                    headers: {"CF-IPCountry": "US", "CF-Device-Type": "desktop", "Accept-Language": "zh-CN"},
                },
                {
                    url: "http://www.example.com/dog_picture.jpg",
                    headers: {"CF-IPCountry": "EU", "CF-Device-Type": "mobile", "Accept-Language": "en-US"},
                },
            ]
        }
        ```

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix.

        Flex purge with tags:

        ```
        {"tags": ["a-cache-tag", "another-cache-tag"]}
        ```

        Flex purge with hosts:

        ```
        {"hosts": ["www.example.com", "images.example.com"]}
        ```

        Flex purge with prefixes:

        ```
        {"prefixes": ["www.example.com/foo", "images.example.com/bar/baz"]}
        ```

        ### Availability and limits

        please refer to
        [purge cache availability and limits documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          tags: For more information on cache tags and purging by tags, please refer to
              [purge by cache-tags documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/).

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
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ```
        {"purge_everything": true}
        ```

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

        Single file purge example with files:

        ```
        {"files": ["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"]}
        ```

        Single file purge example with url and header pairs:

        ```
        {
            "files": [
                {
                    url: "http://www.example.com/cat_picture.jpg",
                    headers: {"CF-IPCountry": "US", "CF-Device-Type": "desktop", "Accept-Language": "zh-CN"},
                },
                {
                    url: "http://www.example.com/dog_picture.jpg",
                    headers: {"CF-IPCountry": "EU", "CF-Device-Type": "mobile", "Accept-Language": "en-US"},
                },
            ]
        }
        ```

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix.

        Flex purge with tags:

        ```
        {"tags": ["a-cache-tag", "another-cache-tag"]}
        ```

        Flex purge with hosts:

        ```
        {"hosts": ["www.example.com", "images.example.com"]}
        ```

        Flex purge with prefixes:

        ```
        {"prefixes": ["www.example.com/foo", "images.example.com/bar/baz"]}
        ```

        ### Availability and limits

        please refer to
        [purge cache availability and limits documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          hosts: For more information purging by hostnames, please refer to
              [purge by hostname documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/).

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
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ```
        {"purge_everything": true}
        ```

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

        Single file purge example with files:

        ```
        {"files": ["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"]}
        ```

        Single file purge example with url and header pairs:

        ```
        {
            "files": [
                {
                    url: "http://www.example.com/cat_picture.jpg",
                    headers: {"CF-IPCountry": "US", "CF-Device-Type": "desktop", "Accept-Language": "zh-CN"},
                },
                {
                    url: "http://www.example.com/dog_picture.jpg",
                    headers: {"CF-IPCountry": "EU", "CF-Device-Type": "mobile", "Accept-Language": "en-US"},
                },
            ]
        }
        ```

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix.

        Flex purge with tags:

        ```
        {"tags": ["a-cache-tag", "another-cache-tag"]}
        ```

        Flex purge with hosts:

        ```
        {"hosts": ["www.example.com", "images.example.com"]}
        ```

        Flex purge with prefixes:

        ```
        {"prefixes": ["www.example.com/foo", "images.example.com/bar/baz"]}
        ```

        ### Availability and limits

        please refer to
        [purge cache availability and limits documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          prefixes: For more information on purging by prefixes, please refer to
              [purge by prefix documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/).

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
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ```
        {"purge_everything": true}
        ```

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

        Single file purge example with files:

        ```
        {"files": ["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"]}
        ```

        Single file purge example with url and header pairs:

        ```
        {
            "files": [
                {
                    url: "http://www.example.com/cat_picture.jpg",
                    headers: {"CF-IPCountry": "US", "CF-Device-Type": "desktop", "Accept-Language": "zh-CN"},
                },
                {
                    url: "http://www.example.com/dog_picture.jpg",
                    headers: {"CF-IPCountry": "EU", "CF-Device-Type": "mobile", "Accept-Language": "en-US"},
                },
            ]
        }
        ```

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix.

        Flex purge with tags:

        ```
        {"tags": ["a-cache-tag", "another-cache-tag"]}
        ```

        Flex purge with hosts:

        ```
        {"hosts": ["www.example.com", "images.example.com"]}
        ```

        Flex purge with prefixes:

        ```
        {"prefixes": ["www.example.com/foo", "images.example.com/bar/baz"]}
        ```

        ### Availability and limits

        please refer to
        [purge cache availability and limits documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          purge_everything: For more information, please refer to
              [purge everything documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/).

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
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ```
        {"purge_everything": true}
        ```

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

        Single file purge example with files:

        ```
        {"files": ["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"]}
        ```

        Single file purge example with url and header pairs:

        ```
        {
            "files": [
                {
                    url: "http://www.example.com/cat_picture.jpg",
                    headers: {"CF-IPCountry": "US", "CF-Device-Type": "desktop", "Accept-Language": "zh-CN"},
                },
                {
                    url: "http://www.example.com/dog_picture.jpg",
                    headers: {"CF-IPCountry": "EU", "CF-Device-Type": "mobile", "Accept-Language": "en-US"},
                },
            ]
        }
        ```

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix.

        Flex purge with tags:

        ```
        {"tags": ["a-cache-tag", "another-cache-tag"]}
        ```

        Flex purge with hosts:

        ```
        {"hosts": ["www.example.com", "images.example.com"]}
        ```

        Flex purge with prefixes:

        ```
        {"prefixes": ["www.example.com/foo", "images.example.com/bar/baz"]}
        ```

        ### Availability and limits

        please refer to
        [purge cache availability and limits documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: For more information on purging files, please refer to
              [purge by single-file documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

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
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ```
        {"purge_everything": true}
        ```

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

        Single file purge example with files:

        ```
        {"files": ["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"]}
        ```

        Single file purge example with url and header pairs:

        ```
        {
            "files": [
                {
                    url: "http://www.example.com/cat_picture.jpg",
                    headers: {"CF-IPCountry": "US", "CF-Device-Type": "desktop", "Accept-Language": "zh-CN"},
                },
                {
                    url: "http://www.example.com/dog_picture.jpg",
                    headers: {"CF-IPCountry": "EU", "CF-Device-Type": "mobile", "Accept-Language": "en-US"},
                },
            ]
        }
        ```

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix.

        Flex purge with tags:

        ```
        {"tags": ["a-cache-tag", "another-cache-tag"]}
        ```

        Flex purge with hosts:

        ```
        {"hosts": ["www.example.com", "images.example.com"]}
        ```

        Flex purge with prefixes:

        ```
        {"prefixes": ["www.example.com/foo", "images.example.com/bar/baz"]}
        ```

        ### Availability and limits

        please refer to
        [purge cache availability and limits documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: For more information on purging files with URL and headers, please refer to
              [purge by single-file documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

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
                post_parser=ResultWrapper[Optional[CachePurgeResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CachePurgeResponse]], ResultWrapper[CachePurgeResponse]),
        )


class AsyncCacheResource(AsyncAPIResource):
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
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ```
        {"purge_everything": true}
        ```

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

        Single file purge example with files:

        ```
        {"files": ["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"]}
        ```

        Single file purge example with url and header pairs:

        ```
        {
            "files": [
                {
                    url: "http://www.example.com/cat_picture.jpg",
                    headers: {"CF-IPCountry": "US", "CF-Device-Type": "desktop", "Accept-Language": "zh-CN"},
                },
                {
                    url: "http://www.example.com/dog_picture.jpg",
                    headers: {"CF-IPCountry": "EU", "CF-Device-Type": "mobile", "Accept-Language": "en-US"},
                },
            ]
        }
        ```

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix.

        Flex purge with tags:

        ```
        {"tags": ["a-cache-tag", "another-cache-tag"]}
        ```

        Flex purge with hosts:

        ```
        {"hosts": ["www.example.com", "images.example.com"]}
        ```

        Flex purge with prefixes:

        ```
        {"prefixes": ["www.example.com/foo", "images.example.com/bar/baz"]}
        ```

        ### Availability and limits

        please refer to
        [purge cache availability and limits documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          tags: For more information on cache tags and purging by tags, please refer to
              [purge by cache-tags documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/).

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
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ```
        {"purge_everything": true}
        ```

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

        Single file purge example with files:

        ```
        {"files": ["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"]}
        ```

        Single file purge example with url and header pairs:

        ```
        {
            "files": [
                {
                    url: "http://www.example.com/cat_picture.jpg",
                    headers: {"CF-IPCountry": "US", "CF-Device-Type": "desktop", "Accept-Language": "zh-CN"},
                },
                {
                    url: "http://www.example.com/dog_picture.jpg",
                    headers: {"CF-IPCountry": "EU", "CF-Device-Type": "mobile", "Accept-Language": "en-US"},
                },
            ]
        }
        ```

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix.

        Flex purge with tags:

        ```
        {"tags": ["a-cache-tag", "another-cache-tag"]}
        ```

        Flex purge with hosts:

        ```
        {"hosts": ["www.example.com", "images.example.com"]}
        ```

        Flex purge with prefixes:

        ```
        {"prefixes": ["www.example.com/foo", "images.example.com/bar/baz"]}
        ```

        ### Availability and limits

        please refer to
        [purge cache availability and limits documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          hosts: For more information purging by hostnames, please refer to
              [purge by hostname documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/).

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
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ```
        {"purge_everything": true}
        ```

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

        Single file purge example with files:

        ```
        {"files": ["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"]}
        ```

        Single file purge example with url and header pairs:

        ```
        {
            "files": [
                {
                    url: "http://www.example.com/cat_picture.jpg",
                    headers: {"CF-IPCountry": "US", "CF-Device-Type": "desktop", "Accept-Language": "zh-CN"},
                },
                {
                    url: "http://www.example.com/dog_picture.jpg",
                    headers: {"CF-IPCountry": "EU", "CF-Device-Type": "mobile", "Accept-Language": "en-US"},
                },
            ]
        }
        ```

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix.

        Flex purge with tags:

        ```
        {"tags": ["a-cache-tag", "another-cache-tag"]}
        ```

        Flex purge with hosts:

        ```
        {"hosts": ["www.example.com", "images.example.com"]}
        ```

        Flex purge with prefixes:

        ```
        {"prefixes": ["www.example.com/foo", "images.example.com/bar/baz"]}
        ```

        ### Availability and limits

        please refer to
        [purge cache availability and limits documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          prefixes: For more information on purging by prefixes, please refer to
              [purge by prefix documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/).

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
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ```
        {"purge_everything": true}
        ```

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

        Single file purge example with files:

        ```
        {"files": ["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"]}
        ```

        Single file purge example with url and header pairs:

        ```
        {
            "files": [
                {
                    url: "http://www.example.com/cat_picture.jpg",
                    headers: {"CF-IPCountry": "US", "CF-Device-Type": "desktop", "Accept-Language": "zh-CN"},
                },
                {
                    url: "http://www.example.com/dog_picture.jpg",
                    headers: {"CF-IPCountry": "EU", "CF-Device-Type": "mobile", "Accept-Language": "en-US"},
                },
            ]
        }
        ```

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix.

        Flex purge with tags:

        ```
        {"tags": ["a-cache-tag", "another-cache-tag"]}
        ```

        Flex purge with hosts:

        ```
        {"hosts": ["www.example.com", "images.example.com"]}
        ```

        Flex purge with prefixes:

        ```
        {"prefixes": ["www.example.com/foo", "images.example.com/bar/baz"]}
        ```

        ### Availability and limits

        please refer to
        [purge cache availability and limits documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          purge_everything: For more information, please refer to
              [purge everything documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/).

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
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ```
        {"purge_everything": true}
        ```

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

        Single file purge example with files:

        ```
        {"files": ["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"]}
        ```

        Single file purge example with url and header pairs:

        ```
        {
            "files": [
                {
                    url: "http://www.example.com/cat_picture.jpg",
                    headers: {"CF-IPCountry": "US", "CF-Device-Type": "desktop", "Accept-Language": "zh-CN"},
                },
                {
                    url: "http://www.example.com/dog_picture.jpg",
                    headers: {"CF-IPCountry": "EU", "CF-Device-Type": "mobile", "Accept-Language": "en-US"},
                },
            ]
        }
        ```

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix.

        Flex purge with tags:

        ```
        {"tags": ["a-cache-tag", "another-cache-tag"]}
        ```

        Flex purge with hosts:

        ```
        {"hosts": ["www.example.com", "images.example.com"]}
        ```

        Flex purge with prefixes:

        ```
        {"prefixes": ["www.example.com/foo", "images.example.com/bar/baz"]}
        ```

        ### Availability and limits

        please refer to
        [purge cache availability and limits documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: For more information on purging files, please refer to
              [purge by single-file documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

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
        """### Purge All Cached Content

        Removes ALL files from Cloudflare's cache.

        All tiers can purge everything.

        ```
        {"purge_everything": true}
        ```

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

        Single file purge example with files:

        ```
        {"files": ["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"]}
        ```

        Single file purge example with url and header pairs:

        ```
        {
            "files": [
                {
                    url: "http://www.example.com/cat_picture.jpg",
                    headers: {"CF-IPCountry": "US", "CF-Device-Type": "desktop", "Accept-Language": "zh-CN"},
                },
                {
                    url: "http://www.example.com/dog_picture.jpg",
                    headers: {"CF-IPCountry": "EU", "CF-Device-Type": "mobile", "Accept-Language": "en-US"},
                },
            ]
        }
        ```

        ### Purge Cached Content by Tag, Host or Prefix

        Granularly removes one or more files from Cloudflare's cache either by
        specifying the host, the associated Cache-Tag, or a Prefix.

        Flex purge with tags:

        ```
        {"tags": ["a-cache-tag", "another-cache-tag"]}
        ```

        Flex purge with hosts:

        ```
        {"hosts": ["www.example.com", "images.example.com"]}
        ```

        Flex purge with prefixes:

        ```
        {"prefixes": ["www.example.com/foo", "images.example.com/bar/baz"]}
        ```

        ### Availability and limits

        please refer to
        [purge cache availability and limits documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

        Args:
          files: For more information on purging files with URL and headers, please refer to
              [purge by single-file documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

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
                post_parser=ResultWrapper[Optional[CachePurgeResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CachePurgeResponse]], ResultWrapper[CachePurgeResponse]),
        )


class CacheResourceWithRawResponse:
    def __init__(self, cache: CacheResource) -> None:
        self._cache = cache

        self.purge = to_raw_response_wrapper(
            cache.purge,
        )


class AsyncCacheResourceWithRawResponse:
    def __init__(self, cache: AsyncCacheResource) -> None:
        self._cache = cache

        self.purge = async_to_raw_response_wrapper(
            cache.purge,
        )


class CacheResourceWithStreamingResponse:
    def __init__(self, cache: CacheResource) -> None:
        self._cache = cache

        self.purge = to_streamed_response_wrapper(
            cache.purge,
        )


class AsyncCacheResourceWithStreamingResponse:
    def __init__(self, cache: AsyncCacheResource) -> None:
        self._cache = cache

        self.purge = async_to_streamed_response_wrapper(
            cache.purge,
        )
