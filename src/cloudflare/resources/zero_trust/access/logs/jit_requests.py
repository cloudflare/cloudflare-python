# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.access.logs import jit_request_list_params
from .....types.zero_trust.access.logs.jit_request_get_response import JitRequestGetResponse
from .....types.zero_trust.access.logs.jit_request_list_response import JitRequestListResponse

__all__ = ["JitRequestsResource", "AsyncJitRequestsResource"]


class JitRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JitRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return JitRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JitRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return JitRequestsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        status: Literal["PENDING", "APPROVED", "DENIED", "CANCELED", "SPENT"] | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[JitRequestListResponse]:
        """
        Lists account-wide Access JIT request logs reconstructed from request lifecycle
        events.

        Args:
          account_id: Identifier.

          page: Page number of results.

          per_page: Number of results per page.

          search: Case-insensitive search over request ID, requester email, application audience,
              and application hostname.

          since: The earliest request timestamp to query. Defaults to 366 days before the current
              time.

          status: JIT request status. `SPENT` is deprecated and interpreted as `APPROVED`.

          until: The latest request timestamp to query. Defaults to the current time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/access/logs/jit_requests", account_id=account_id),
            page=SyncV4PagePaginationArray[JitRequestListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "since": since,
                        "status": status,
                        "until": until,
                    },
                    jit_request_list_params.JitRequestListParams,
                ),
            ),
            model=JitRequestListResponse,
        )

    def get(
        self,
        knock_request_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[JitRequestGetResponse]:
        """
        Gets an account-scoped Access JIT request summary and its lifecycle events in
        chronological order.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not knock_request_id:
            raise ValueError(f"Expected a non-empty value for `knock_request_id` but received {knock_request_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/access/logs/jit_requests/{knock_request_id}",
                account_id=account_id,
                knock_request_id=knock_request_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JitRequestGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[JitRequestGetResponse]], ResultWrapper[JitRequestGetResponse]),
        )


class AsyncJitRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJitRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJitRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJitRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncJitRequestsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        status: Literal["PENDING", "APPROVED", "DENIED", "CANCELED", "SPENT"] | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[JitRequestListResponse, AsyncV4PagePaginationArray[JitRequestListResponse]]:
        """
        Lists account-wide Access JIT request logs reconstructed from request lifecycle
        events.

        Args:
          account_id: Identifier.

          page: Page number of results.

          per_page: Number of results per page.

          search: Case-insensitive search over request ID, requester email, application audience,
              and application hostname.

          since: The earliest request timestamp to query. Defaults to 366 days before the current
              time.

          status: JIT request status. `SPENT` is deprecated and interpreted as `APPROVED`.

          until: The latest request timestamp to query. Defaults to the current time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/access/logs/jit_requests", account_id=account_id),
            page=AsyncV4PagePaginationArray[JitRequestListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "since": since,
                        "status": status,
                        "until": until,
                    },
                    jit_request_list_params.JitRequestListParams,
                ),
            ),
            model=JitRequestListResponse,
        )

    async def get(
        self,
        knock_request_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[JitRequestGetResponse]:
        """
        Gets an account-scoped Access JIT request summary and its lifecycle events in
        chronological order.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not knock_request_id:
            raise ValueError(f"Expected a non-empty value for `knock_request_id` but received {knock_request_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/access/logs/jit_requests/{knock_request_id}",
                account_id=account_id,
                knock_request_id=knock_request_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JitRequestGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[JitRequestGetResponse]], ResultWrapper[JitRequestGetResponse]),
        )


class JitRequestsResourceWithRawResponse:
    def __init__(self, jit_requests: JitRequestsResource) -> None:
        self._jit_requests = jit_requests

        self.list = to_raw_response_wrapper(
            jit_requests.list,
        )
        self.get = to_raw_response_wrapper(
            jit_requests.get,
        )


class AsyncJitRequestsResourceWithRawResponse:
    def __init__(self, jit_requests: AsyncJitRequestsResource) -> None:
        self._jit_requests = jit_requests

        self.list = async_to_raw_response_wrapper(
            jit_requests.list,
        )
        self.get = async_to_raw_response_wrapper(
            jit_requests.get,
        )


class JitRequestsResourceWithStreamingResponse:
    def __init__(self, jit_requests: JitRequestsResource) -> None:
        self._jit_requests = jit_requests

        self.list = to_streamed_response_wrapper(
            jit_requests.list,
        )
        self.get = to_streamed_response_wrapper(
            jit_requests.get,
        )


class AsyncJitRequestsResourceWithStreamingResponse:
    def __init__(self, jit_requests: AsyncJitRequestsResource) -> None:
        self._jit_requests = jit_requests

        self.list = async_to_streamed_response_wrapper(
            jit_requests.list,
        )
        self.get = async_to_streamed_response_wrapper(
            jit_requests.get,
        )
