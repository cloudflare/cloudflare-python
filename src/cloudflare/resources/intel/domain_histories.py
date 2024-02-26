# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.intel import DomainHistoryListResponse, domain_history_list_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["DomainHistories", "AsyncDomainHistories"]


class DomainHistories(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainHistoriesWithRawResponse:
        return DomainHistoriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainHistoriesWithStreamingResponse:
        return DomainHistoriesWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        domain: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainHistoryListResponse]:
        """
        Get Domain History

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/domain-history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"domain": domain}, domain_history_list_params.DomainHistoryListParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainHistoryListResponse]], ResultWrapper[DomainHistoryListResponse]),
        )


class AsyncDomainHistories(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainHistoriesWithRawResponse:
        return AsyncDomainHistoriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainHistoriesWithStreamingResponse:
        return AsyncDomainHistoriesWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        domain: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainHistoryListResponse]:
        """
        Get Domain History

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/domain-history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"domain": domain}, domain_history_list_params.DomainHistoryListParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainHistoryListResponse]], ResultWrapper[DomainHistoryListResponse]),
        )


class DomainHistoriesWithRawResponse:
    def __init__(self, domain_histories: DomainHistories) -> None:
        self._domain_histories = domain_histories

        self.list = to_raw_response_wrapper(
            domain_histories.list,
        )


class AsyncDomainHistoriesWithRawResponse:
    def __init__(self, domain_histories: AsyncDomainHistories) -> None:
        self._domain_histories = domain_histories

        self.list = async_to_raw_response_wrapper(
            domain_histories.list,
        )


class DomainHistoriesWithStreamingResponse:
    def __init__(self, domain_histories: DomainHistories) -> None:
        self._domain_histories = domain_histories

        self.list = to_streamed_response_wrapper(
            domain_histories.list,
        )


class AsyncDomainHistoriesWithStreamingResponse:
    def __init__(self, domain_histories: AsyncDomainHistories) -> None:
        self._domain_histories = domain_histories

        self.list = async_to_streamed_response_wrapper(
            domain_histories.list,
        )
