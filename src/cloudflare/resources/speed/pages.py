# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.speed import PageListResponse
from ..._base_client import (
    make_request_options,
)

__all__ = ["Pages", "AsyncPages"]


class Pages(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PagesWithRawResponse:
        return PagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PagesWithStreamingResponse:
        return PagesWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PageListResponse]:
        """
        Lists all webpages which have been tested.

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
            f"/zones/{zone_id}/speed_api/pages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageListResponse]], ResultWrapper[PageListResponse]),
        )


class AsyncPages(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPagesWithRawResponse:
        return AsyncPagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPagesWithStreamingResponse:
        return AsyncPagesWithStreamingResponse(self)

    async def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PageListResponse]:
        """
        Lists all webpages which have been tested.

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
            f"/zones/{zone_id}/speed_api/pages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PageListResponse]], ResultWrapper[PageListResponse]),
        )


class PagesWithRawResponse:
    def __init__(self, pages: Pages) -> None:
        self._pages = pages

        self.list = to_raw_response_wrapper(
            pages.list,
        )


class AsyncPagesWithRawResponse:
    def __init__(self, pages: AsyncPages) -> None:
        self._pages = pages

        self.list = async_to_raw_response_wrapper(
            pages.list,
        )


class PagesWithStreamingResponse:
    def __init__(self, pages: Pages) -> None:
        self._pages = pages

        self.list = to_streamed_response_wrapper(
            pages.list,
        )


class AsyncPagesWithStreamingResponse:
    def __init__(self, pages: AsyncPages) -> None:
        self._pages = pages

        self.list = async_to_streamed_response_wrapper(
            pages.list,
        )
