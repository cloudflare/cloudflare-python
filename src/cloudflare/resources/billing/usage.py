# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import date

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.billing import usage_paygo_params
from ...types.billing.usage_paygo_response import UsagePaygoResponse

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UsageResourceWithStreamingResponse(self)

    def paygo(
        self,
        *,
        account_id: str,
        from_: Union[str, date] | Omit = omit,
        last_month_period_start: int | Omit = omit,
        last_year_period_start: int | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsagePaygoResponse:
        """Returns billable usage data for PayGo (self-serve) accounts.

        When no query
        parameters are provided, returns usage for the current billing period.

        Supports two mutually exclusive query modes:

        **Billing period mode:** Use `last_year_period_start` and
        `last_month_period_start` to query a specific billing period.

        **Date range mode:** Use `from` and `to` to query a custom date range (maximum
        62 days).

        This endpoint is currently in beta and access is restricted to select accounts.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          from_: Defines the start date for the usage query (e.g., 2025-02-01).

          last_month_period_start: Specifies the month of the billing period to query (1-12). Must be provided
              together with last_year_period_start. Mutually exclusive with from/to.

          last_year_period_start: Specifies the year of the billing period to query (e.g., 2025). Must be provided
              together with last_month_period_start. Mutually exclusive with from/to.

          to: Defines the end date for the usage query (e.g., 2025-03-01).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/billing/usage/paygo",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "last_month_period_start": last_month_period_start,
                        "last_year_period_start": last_year_period_start,
                        "to": to,
                    },
                    usage_paygo_params.UsagePaygoParams,
                ),
                post_parser=ResultWrapper[UsagePaygoResponse]._unwrapper,
            ),
            cast_to=cast(Type[UsagePaygoResponse], ResultWrapper[UsagePaygoResponse]),
        )


class AsyncUsageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUsageResourceWithStreamingResponse(self)

    async def paygo(
        self,
        *,
        account_id: str,
        from_: Union[str, date] | Omit = omit,
        last_month_period_start: int | Omit = omit,
        last_year_period_start: int | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsagePaygoResponse:
        """Returns billable usage data for PayGo (self-serve) accounts.

        When no query
        parameters are provided, returns usage for the current billing period.

        Supports two mutually exclusive query modes:

        **Billing period mode:** Use `last_year_period_start` and
        `last_month_period_start` to query a specific billing period.

        **Date range mode:** Use `from` and `to` to query a custom date range (maximum
        62 days).

        This endpoint is currently in beta and access is restricted to select accounts.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          from_: Defines the start date for the usage query (e.g., 2025-02-01).

          last_month_period_start: Specifies the month of the billing period to query (1-12). Must be provided
              together with last_year_period_start. Mutually exclusive with from/to.

          last_year_period_start: Specifies the year of the billing period to query (e.g., 2025). Must be provided
              together with last_month_period_start. Mutually exclusive with from/to.

          to: Defines the end date for the usage query (e.g., 2025-03-01).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/billing/usage/paygo",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "last_month_period_start": last_month_period_start,
                        "last_year_period_start": last_year_period_start,
                        "to": to,
                    },
                    usage_paygo_params.UsagePaygoParams,
                ),
                post_parser=ResultWrapper[UsagePaygoResponse]._unwrapper,
            ),
            cast_to=cast(Type[UsagePaygoResponse], ResultWrapper[UsagePaygoResponse]),
        )


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.paygo = to_raw_response_wrapper(
            usage.paygo,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.paygo = async_to_raw_response_wrapper(
            usage.paygo,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.paygo = to_streamed_response_wrapper(
            usage.paygo,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.paygo = async_to_streamed_response_wrapper(
            usage.paygo,
        )
