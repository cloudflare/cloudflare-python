# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from typing import List, Optional, Type

from ..types import PurgeCachZonePurgeResponse, purge_cach_zone_purge_params

from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import SyncAPIClient, AsyncAPIClient, _merge_mappings, AsyncPaginator, make_request_options, HttpxBinaryResponseContent
from ..types import shared_params
from ..types import purge_cach_zone_purge_params
from .._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["PurgeCaches", "AsyncPurgeCaches"]

class PurgeCaches(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PurgeCachesWithRawResponse:
        return PurgeCachesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PurgeCachesWithStreamingResponse:
        return PurgeCachesWithStreamingResponse(self)

    @overload
    def zone_purge(self,
    identifier: str,
    *,
    hosts: List[str] | NotGiven = NOT_GIVEN,
    prefixes: List[str] | NotGiven = NOT_GIVEN,
    tags: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[PurgeCachZonePurgeResponse]:
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
    def zone_purge(self,
    identifier: str,
    *,
    purge_everything: bool | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[PurgeCachZonePurgeResponse]:
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
    def zone_purge(self,
    identifier: str,
    *,
    files: List[purge_cach_zone_purge_params.9HseNYt2FilesFile] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[PurgeCachZonePurgeResponse]:
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
    def zone_purge(self,
    identifier: str,
    *,
    hosts: List[str] | NotGiven = NOT_GIVEN,
    prefixes: List[str] | NotGiven = NOT_GIVEN,
    tags: List[str] | NotGiven = NOT_GIVEN,
    purge_everything: bool | NotGiven = NOT_GIVEN,
    files: List[purge_cach_zone_purge_params.9HseNYt2FilesFile] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[PurgeCachZonePurgeResponse]:
        if not identifier:
          raise ValueError(
            f'Expected a non-empty value for `identifier` but received {identifier!r}'
          )
        return self._post(
            f"/zones/{identifier}/purge_cache",
            body=maybe_transform({
                "hosts": hosts,
                "prefixes": prefixes,
                "tags": tags,
                "purge_everything": purge_everything,
                "files": files,
            }, purge_cach_zone_purge_params.PurgeCachZonePurgeParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper._unwrapper),
            cast_to=cast(Type[Optional[PurgeCachZonePurgeResponse]], ResultWrapper[PurgeCachZonePurgeResponse]),
        )

class AsyncPurgeCaches(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPurgeCachesWithRawResponse:
        return AsyncPurgeCachesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPurgeCachesWithStreamingResponse:
        return AsyncPurgeCachesWithStreamingResponse(self)

    @overload
    async def zone_purge(self,
    identifier: str,
    *,
    hosts: List[str] | NotGiven = NOT_GIVEN,
    prefixes: List[str] | NotGiven = NOT_GIVEN,
    tags: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[PurgeCachZonePurgeResponse]:
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
    async def zone_purge(self,
    identifier: str,
    *,
    purge_everything: bool | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[PurgeCachZonePurgeResponse]:
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
    async def zone_purge(self,
    identifier: str,
    *,
    files: List[purge_cach_zone_purge_params.9HseNYt2FilesFile] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[PurgeCachZonePurgeResponse]:
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
    async def zone_purge(self,
    identifier: str,
    *,
    hosts: List[str] | NotGiven = NOT_GIVEN,
    prefixes: List[str] | NotGiven = NOT_GIVEN,
    tags: List[str] | NotGiven = NOT_GIVEN,
    purge_everything: bool | NotGiven = NOT_GIVEN,
    files: List[purge_cach_zone_purge_params.9HseNYt2FilesFile] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[PurgeCachZonePurgeResponse]:
        if not identifier:
          raise ValueError(
            f'Expected a non-empty value for `identifier` but received {identifier!r}'
          )
        return await self._post(
            f"/zones/{identifier}/purge_cache",
            body=maybe_transform({
                "hosts": hosts,
                "prefixes": prefixes,
                "tags": tags,
                "purge_everything": purge_everything,
                "files": files,
            }, purge_cach_zone_purge_params.PurgeCachZonePurgeParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper._unwrapper),
            cast_to=cast(Type[Optional[PurgeCachZonePurgeResponse]], ResultWrapper[PurgeCachZonePurgeResponse]),
        )

class PurgeCachesWithRawResponse:
    def __init__(self, purge_caches: PurgeCaches) -> None:
        self._purge_caches = purge_caches

        self.zone_purge = to_raw_response_wrapper(
            purge_caches.zone_purge,
        )

class AsyncPurgeCachesWithRawResponse:
    def __init__(self, purge_caches: AsyncPurgeCaches) -> None:
        self._purge_caches = purge_caches

        self.zone_purge = async_to_raw_response_wrapper(
            purge_caches.zone_purge,
        )

class PurgeCachesWithStreamingResponse:
    def __init__(self, purge_caches: PurgeCaches) -> None:
        self._purge_caches = purge_caches

        self.zone_purge = to_streamed_response_wrapper(
            purge_caches.zone_purge,
        )

class AsyncPurgeCachesWithStreamingResponse:
    def __init__(self, purge_caches: AsyncPurgeCaches) -> None:
        self._purge_caches = purge_caches

        self.zone_purge = async_to_streamed_response_wrapper(
            purge_caches.zone_purge,
        )