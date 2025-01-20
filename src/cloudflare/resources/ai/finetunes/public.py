# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.ai.finetunes import public_list_params
from ....types.ai.finetunes.public_list_response import PublicListResponse

__all__ = ["PublicResource", "AsyncPublicResource"]


class PublicResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PublicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PublicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PublicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PublicResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[PublicListResponse]:
        """
        List Public Finetunes

        Args:
          limit: Pagination Limit

          offset: Pagination Offset

          order_by: Order By Column Name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/ai/finetunes/public",
            page=SyncSinglePage[PublicListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                    },
                    public_list_params.PublicListParams,
                ),
            ),
            model=PublicListResponse,
        )


class AsyncPublicResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPublicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPublicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPublicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPublicResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PublicListResponse, AsyncSinglePage[PublicListResponse]]:
        """
        List Public Finetunes

        Args:
          limit: Pagination Limit

          offset: Pagination Offset

          order_by: Order By Column Name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/ai/finetunes/public",
            page=AsyncSinglePage[PublicListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                    },
                    public_list_params.PublicListParams,
                ),
            ),
            model=PublicListResponse,
        )


class PublicResourceWithRawResponse:
    def __init__(self, public: PublicResource) -> None:
        self._public = public

        self.list = to_raw_response_wrapper(
            public.list,
        )


class AsyncPublicResourceWithRawResponse:
    def __init__(self, public: AsyncPublicResource) -> None:
        self._public = public

        self.list = async_to_raw_response_wrapper(
            public.list,
        )


class PublicResourceWithStreamingResponse:
    def __init__(self, public: PublicResource) -> None:
        self._public = public

        self.list = to_streamed_response_wrapper(
            public.list,
        )


class AsyncPublicResourceWithStreamingResponse:
    def __init__(self, public: AsyncPublicResource) -> None:
        self._public = public

        self.list = async_to_streamed_response_wrapper(
            public.list,
        )
