# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.cloudforce_one.threat_signals import indicator_list_params
from ....types.cloudforce_one.threat_signals.indicator_list_response import IndicatorListResponse

__all__ = ["IndicatorsResource", "AsyncIndicatorsResource"]


class IndicatorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndicatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IndicatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndicatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IndicatorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        article_id: str | Omit = omit,
        cursor: str | Omit = omit,
        feed_id: str | Omit = omit,
        include_total: bool | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndicatorListResponse:
        """
        Lists indicators of compromise extracted from the account's Threat Signals
        articles.

        Args:
          search: NFC-normalized and trimmed, case-insensitive literal substring search of
              indicator values. Requires 3–500 Unicode code points; the upper code-point bound
              is described here because OpenAPI string length cannot precisely express it
              without imposing UTF-16 semantics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/indicators", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "article_id": article_id,
                        "cursor": cursor,
                        "feed_id": feed_id,
                        "include_total": include_total,
                        "per_page": per_page,
                        "search": search,
                        "sort": sort,
                    },
                    indicator_list_params.IndicatorListParams,
                ),
                post_parser=ResultWrapper[IndicatorListResponse]._unwrapper,
            ),
            cast_to=cast(Type[IndicatorListResponse], ResultWrapper[IndicatorListResponse]),
        )


class AsyncIndicatorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndicatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndicatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndicatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIndicatorsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        article_id: str | Omit = omit,
        cursor: str | Omit = omit,
        feed_id: str | Omit = omit,
        include_total: bool | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndicatorListResponse:
        """
        Lists indicators of compromise extracted from the account's Threat Signals
        articles.

        Args:
          search: NFC-normalized and trimmed, case-insensitive literal substring search of
              indicator values. Requires 3–500 Unicode code points; the upper code-point bound
              is described here because OpenAPI string length cannot precisely express it
              without imposing UTF-16 semantics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/cloudforce-one/v2/threat-signals/indicators", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "article_id": article_id,
                        "cursor": cursor,
                        "feed_id": feed_id,
                        "include_total": include_total,
                        "per_page": per_page,
                        "search": search,
                        "sort": sort,
                    },
                    indicator_list_params.IndicatorListParams,
                ),
                post_parser=ResultWrapper[IndicatorListResponse]._unwrapper,
            ),
            cast_to=cast(Type[IndicatorListResponse], ResultWrapper[IndicatorListResponse]),
        )


class IndicatorsResourceWithRawResponse:
    def __init__(self, indicators: IndicatorsResource) -> None:
        self._indicators = indicators

        self.list = to_raw_response_wrapper(
            indicators.list,
        )


class AsyncIndicatorsResourceWithRawResponse:
    def __init__(self, indicators: AsyncIndicatorsResource) -> None:
        self._indicators = indicators

        self.list = async_to_raw_response_wrapper(
            indicators.list,
        )


class IndicatorsResourceWithStreamingResponse:
    def __init__(self, indicators: IndicatorsResource) -> None:
        self._indicators = indicators

        self.list = to_streamed_response_wrapper(
            indicators.list,
        )


class AsyncIndicatorsResourceWithStreamingResponse:
    def __init__(self, indicators: AsyncIndicatorsResource) -> None:
        self._indicators = indicators

        self.list = async_to_streamed_response_wrapper(
            indicators.list,
        )
