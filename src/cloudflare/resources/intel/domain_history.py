# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
from ...types.intel import domain_history_get_params
from ..._base_client import make_request_options
from ...types.intel.domain_history_get_response import DomainHistoryGetResponse

__all__ = ["DomainHistoryResource", "AsyncDomainHistoryResource"]


class DomainHistoryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainHistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DomainHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainHistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DomainHistoryResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        domain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainHistoryGetResponse]:
        """
        Gets historical security threat and content categories currently and previously
        assigned to a domain.

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
                post_parser=ResultWrapper[Optional[DomainHistoryGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainHistoryGetResponse]], ResultWrapper[DomainHistoryGetResponse]),
        )


class AsyncDomainHistoryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainHistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDomainHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainHistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDomainHistoryResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        domain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainHistoryGetResponse]:
        """
        Gets historical security threat and content categories currently and previously
        assigned to a domain.

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
                post_parser=ResultWrapper[Optional[DomainHistoryGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainHistoryGetResponse]], ResultWrapper[DomainHistoryGetResponse]),
        )


class DomainHistoryResourceWithRawResponse:
    def __init__(self, domain_history: DomainHistoryResource) -> None:
        self._domain_history = domain_history

        self.get = to_raw_response_wrapper(
            domain_history.get,
        )


class AsyncDomainHistoryResourceWithRawResponse:
    def __init__(self, domain_history: AsyncDomainHistoryResource) -> None:
        self._domain_history = domain_history

        self.get = async_to_raw_response_wrapper(
            domain_history.get,
        )


class DomainHistoryResourceWithStreamingResponse:
    def __init__(self, domain_history: DomainHistoryResource) -> None:
        self._domain_history = domain_history

        self.get = to_streamed_response_wrapper(
            domain_history.get,
        )


class AsyncDomainHistoryResourceWithStreamingResponse:
    def __init__(self, domain_history: AsyncDomainHistoryResource) -> None:
        self._domain_history = domain_history

        self.get = async_to_streamed_response_wrapper(
            domain_history.get,
        )
