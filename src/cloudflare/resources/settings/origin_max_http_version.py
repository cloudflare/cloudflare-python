# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import OriginMaxHTTPVersionUpdateResponse, OriginMaxHTTPVersionGetResponse

from typing import Type

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
from ...types.settings import origin_max_http_version_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["OriginMaxHTTPVersion", "AsyncOriginMaxHTTPVersion"]


class OriginMaxHTTPVersion(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OriginMaxHTTPVersionWithRawResponse:
        return OriginMaxHTTPVersionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginMaxHTTPVersionWithStreamingResponse:
        return OriginMaxHTTPVersionWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal["2", "1"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OriginMaxHTTPVersionUpdateResponse:
        """
        Origin Max HTTP Setting Version sets the highest HTTP version Cloudflare will
        attempt to use with your origin. This setting allows Cloudflare to make HTTP/2
        requests to your origin. (Refer to
        [Enable HTTP/2 to Origin](https://developers.cloudflare.com/cache/how-to/enable-http2-to-origin/),
        for more information.). The default value is "2" for all plan types except ENT
        where it is "1"

        Args:
          zone_id: Identifier

          value: Value of the Origin Max HTTP Version Setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/origin_max_http_version",
            body=maybe_transform(
                {"value": value}, origin_max_http_version_update_params.OriginMaxHTTPVersionUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OriginMaxHTTPVersionUpdateResponse], ResultWrapper[OriginMaxHTTPVersionUpdateResponse]),
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
    ) -> OriginMaxHTTPVersionGetResponse:
        """
        Origin Max HTTP Setting Version sets the highest HTTP version Cloudflare will
        attempt to use with your origin. This setting allows Cloudflare to make HTTP/2
        requests to your origin. (Refer to
        [Enable HTTP/2 to Origin](https://developers.cloudflare.com/cache/how-to/enable-http2-to-origin/),
        for more information.). The default value is "2" for all plan types except ENT
        where it is "1"

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
            f"/zones/{zone_id}/settings/origin_max_http_version",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OriginMaxHTTPVersionGetResponse], ResultWrapper[OriginMaxHTTPVersionGetResponse]),
        )


class AsyncOriginMaxHTTPVersion(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOriginMaxHTTPVersionWithRawResponse:
        return AsyncOriginMaxHTTPVersionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginMaxHTTPVersionWithStreamingResponse:
        return AsyncOriginMaxHTTPVersionWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal["2", "1"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OriginMaxHTTPVersionUpdateResponse:
        """
        Origin Max HTTP Setting Version sets the highest HTTP version Cloudflare will
        attempt to use with your origin. This setting allows Cloudflare to make HTTP/2
        requests to your origin. (Refer to
        [Enable HTTP/2 to Origin](https://developers.cloudflare.com/cache/how-to/enable-http2-to-origin/),
        for more information.). The default value is "2" for all plan types except ENT
        where it is "1"

        Args:
          zone_id: Identifier

          value: Value of the Origin Max HTTP Version Setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/origin_max_http_version",
            body=maybe_transform(
                {"value": value}, origin_max_http_version_update_params.OriginMaxHTTPVersionUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OriginMaxHTTPVersionUpdateResponse], ResultWrapper[OriginMaxHTTPVersionUpdateResponse]),
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
    ) -> OriginMaxHTTPVersionGetResponse:
        """
        Origin Max HTTP Setting Version sets the highest HTTP version Cloudflare will
        attempt to use with your origin. This setting allows Cloudflare to make HTTP/2
        requests to your origin. (Refer to
        [Enable HTTP/2 to Origin](https://developers.cloudflare.com/cache/how-to/enable-http2-to-origin/),
        for more information.). The default value is "2" for all plan types except ENT
        where it is "1"

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
            f"/zones/{zone_id}/settings/origin_max_http_version",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OriginMaxHTTPVersionGetResponse], ResultWrapper[OriginMaxHTTPVersionGetResponse]),
        )


class OriginMaxHTTPVersionWithRawResponse:
    def __init__(self, origin_max_http_version: OriginMaxHTTPVersion) -> None:
        self._origin_max_http_version = origin_max_http_version

        self.update = to_raw_response_wrapper(
            origin_max_http_version.update,
        )
        self.get = to_raw_response_wrapper(
            origin_max_http_version.get,
        )


class AsyncOriginMaxHTTPVersionWithRawResponse:
    def __init__(self, origin_max_http_version: AsyncOriginMaxHTTPVersion) -> None:
        self._origin_max_http_version = origin_max_http_version

        self.update = async_to_raw_response_wrapper(
            origin_max_http_version.update,
        )
        self.get = async_to_raw_response_wrapper(
            origin_max_http_version.get,
        )


class OriginMaxHTTPVersionWithStreamingResponse:
    def __init__(self, origin_max_http_version: OriginMaxHTTPVersion) -> None:
        self._origin_max_http_version = origin_max_http_version

        self.update = to_streamed_response_wrapper(
            origin_max_http_version.update,
        )
        self.get = to_streamed_response_wrapper(
            origin_max_http_version.get,
        )


class AsyncOriginMaxHTTPVersionWithStreamingResponse:
    def __init__(self, origin_max_http_version: AsyncOriginMaxHTTPVersion) -> None:
        self._origin_max_http_version = origin_max_http_version

        self.update = async_to_streamed_response_wrapper(
            origin_max_http_version.update,
        )
        self.get = async_to_streamed_response_wrapper(
            origin_max_http_version.get,
        )
