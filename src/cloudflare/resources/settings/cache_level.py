# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import CacheLevelUpdateResponse, CacheLevelGetResponse

from typing import Type, Optional

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.settings import cache_level_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["CacheLevel", "AsyncCacheLevel"]


class CacheLevel(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CacheLevelWithRawResponse:
        return CacheLevelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CacheLevelWithStreamingResponse:
        return CacheLevelWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal["aggressive", "basic", "simplified"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CacheLevelUpdateResponse]:
        """Cache Level functions based off the setting level.

        The basic setting will cache
        most static resources (i.e., css, images, and JavaScript). The simplified
        setting will ignore the query string when delivering a cached resource. The
        aggressive setting will cache all static resources, including ones with a query
        string. (https://support.cloudflare.com/hc/en-us/articles/200168256).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/cache_level",
            body=maybe_transform({"value": value}, cache_level_update_params.CacheLevelUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CacheLevelUpdateResponse]], ResultWrapper[CacheLevelUpdateResponse]),
        )

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CacheLevelGetResponse]:
        """Cache Level functions based off the setting level.

        The basic setting will cache
        most static resources (i.e., css, images, and JavaScript). The simplified
        setting will ignore the query string when delivering a cached resource. The
        aggressive setting will cache all static resources, including ones with a query
        string. (https://support.cloudflare.com/hc/en-us/articles/200168256).

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/cache_level",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CacheLevelGetResponse]], ResultWrapper[CacheLevelGetResponse]),
        )


class AsyncCacheLevel(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCacheLevelWithRawResponse:
        return AsyncCacheLevelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCacheLevelWithStreamingResponse:
        return AsyncCacheLevelWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal["aggressive", "basic", "simplified"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CacheLevelUpdateResponse]:
        """Cache Level functions based off the setting level.

        The basic setting will cache
        most static resources (i.e., css, images, and JavaScript). The simplified
        setting will ignore the query string when delivering a cached resource. The
        aggressive setting will cache all static resources, including ones with a query
        string. (https://support.cloudflare.com/hc/en-us/articles/200168256).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/cache_level",
            body=maybe_transform({"value": value}, cache_level_update_params.CacheLevelUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CacheLevelUpdateResponse]], ResultWrapper[CacheLevelUpdateResponse]),
        )

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CacheLevelGetResponse]:
        """Cache Level functions based off the setting level.

        The basic setting will cache
        most static resources (i.e., css, images, and JavaScript). The simplified
        setting will ignore the query string when delivering a cached resource. The
        aggressive setting will cache all static resources, including ones with a query
        string. (https://support.cloudflare.com/hc/en-us/articles/200168256).

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/cache_level",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CacheLevelGetResponse]], ResultWrapper[CacheLevelGetResponse]),
        )


class CacheLevelWithRawResponse:
    def __init__(self, cache_level: CacheLevel) -> None:
        self._cache_level = cache_level

        self.update = to_raw_response_wrapper(
            cache_level.update,
        )
        self.get = to_raw_response_wrapper(
            cache_level.get,
        )


class AsyncCacheLevelWithRawResponse:
    def __init__(self, cache_level: AsyncCacheLevel) -> None:
        self._cache_level = cache_level

        self.update = async_to_raw_response_wrapper(
            cache_level.update,
        )
        self.get = async_to_raw_response_wrapper(
            cache_level.get,
        )


class CacheLevelWithStreamingResponse:
    def __init__(self, cache_level: CacheLevel) -> None:
        self._cache_level = cache_level

        self.update = to_streamed_response_wrapper(
            cache_level.update,
        )
        self.get = to_streamed_response_wrapper(
            cache_level.get,
        )


class AsyncCacheLevelWithStreamingResponse:
    def __init__(self, cache_level: AsyncCacheLevel) -> None:
        self._cache_level = cache_level

        self.update = async_to_streamed_response_wrapper(
            cache_level.update,
        )
        self.get = async_to_streamed_response_wrapper(
            cache_level.get,
        )
