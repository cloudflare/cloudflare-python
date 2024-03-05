# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
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
from ...types.intel import DomainHistoryGetResponse, domain_history_get_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["DomainHistory", "AsyncDomainHistory"]


class DomainHistory(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainHistoryWithRawResponse:
        return DomainHistoryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainHistoryWithStreamingResponse:
        return DomainHistoryWithStreamingResponse(self)

    def get(
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
    ) -> Optional[DomainHistoryGetResponse]:
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
                query=maybe_transform({"domain": domain}, domain_history_get_params.DomainHistoryGetParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainHistoryGetResponse]], ResultWrapper[DomainHistoryGetResponse]),
        )


class AsyncDomainHistory(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainHistoryWithRawResponse:
        return AsyncDomainHistoryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainHistoryWithStreamingResponse:
        return AsyncDomainHistoryWithStreamingResponse(self)

    async def get(
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
    ) -> Optional[DomainHistoryGetResponse]:
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
                query=await async_maybe_transform({"domain": domain}, domain_history_get_params.DomainHistoryGetParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainHistoryGetResponse]], ResultWrapper[DomainHistoryGetResponse]),
        )


class DomainHistoryWithRawResponse:
    def __init__(self, domain_history: DomainHistory) -> None:
        self._domain_history = domain_history

        self.get = to_raw_response_wrapper(
            domain_history.get,
        )


class AsyncDomainHistoryWithRawResponse:
    def __init__(self, domain_history: AsyncDomainHistory) -> None:
        self._domain_history = domain_history

        self.get = async_to_raw_response_wrapper(
            domain_history.get,
        )


class DomainHistoryWithStreamingResponse:
    def __init__(self, domain_history: DomainHistory) -> None:
        self._domain_history = domain_history

        self.get = to_streamed_response_wrapper(
            domain_history.get,
        )


class AsyncDomainHistoryWithStreamingResponse:
    def __init__(self, domain_history: AsyncDomainHistory) -> None:
        self._domain_history = domain_history

        self.get = async_to_streamed_response_wrapper(
            domain_history.get,
        )
