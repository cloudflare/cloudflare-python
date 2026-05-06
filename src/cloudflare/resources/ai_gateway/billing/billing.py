# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .topup.topup import (
    TopupResource,
    AsyncTopupResource,
    TopupResourceWithRawResponse,
    AsyncTopupResourceWithRawResponse,
    TopupResourceWithStreamingResponse,
    AsyncTopupResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from .spending_limit import (
    SpendingLimitResource,
    AsyncSpendingLimitResource,
    SpendingLimitResourceWithRawResponse,
    AsyncSpendingLimitResourceWithRawResponse,
    SpendingLimitResourceWithStreamingResponse,
    AsyncSpendingLimitResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.ai_gateway import billing_usage_history_params, billing_invoice_history_params
from ....types.ai_gateway.billing_usage_history_response import BillingUsageHistoryResponse
from ....types.ai_gateway.billing_credit_balance_response import BillingCreditBalanceResponse
from ....types.ai_gateway.billing_invoice_history_response import BillingInvoiceHistoryResponse
from ....types.ai_gateway.billing_invoice_preview_response import BillingInvoicePreviewResponse

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def topup(self) -> TopupResource:
        return TopupResource(self._client)

    @cached_property
    def spending_limit(self) -> SpendingLimitResource:
        return SpendingLimitResource(self._client)

    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BillingResourceWithStreamingResponse(self)

    def credit_balance(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingCreditBalanceResponse:
        """
        Retrieve the current credit balance, payment method info, and top-up
        configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/ai-gateway/billing/credit-balance", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BillingCreditBalanceResponse]._unwrapper,
            ),
            cast_to=cast(Type[BillingCreditBalanceResponse], ResultWrapper[BillingCreditBalanceResponse]),
        )

    def invoice_history(
        self,
        *,
        account_id: str,
        type: Literal["auto", "all", "manual"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingInvoiceHistoryResponse:
        """
        Retrieve a list of past invoices with pagination, optionally filtered by type.

        Args:
          type: Filter invoice type: auto, manual, or all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/ai-gateway/billing/invoice-history", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, billing_invoice_history_params.BillingInvoiceHistoryParams),
                post_parser=ResultWrapper[BillingInvoiceHistoryResponse]._unwrapper,
            ),
            cast_to=cast(Type[BillingInvoiceHistoryResponse], ResultWrapper[BillingInvoiceHistoryResponse]),
        )

    def invoice_preview(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingInvoicePreviewResponse:
        """
        Retrieve a preview of the upcoming invoice including line items and tax.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/ai-gateway/billing/invoice-preview", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BillingInvoicePreviewResponse]._unwrapper,
            ),
            cast_to=cast(Type[BillingInvoicePreviewResponse], ResultWrapper[BillingInvoicePreviewResponse]),
        )

    def usage_history(
        self,
        *,
        account_id: str,
        value_grouping_window: Literal["day", "hour"],
        end_time: Optional[float] | Omit = omit,
        start_time: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingUsageHistoryResponse:
        """
        Retrieve aggregated usage meter event summaries for the given time range.

        Args:
          value_grouping_window: Grouping window for usage data.

          end_time: End time (Unix timestamp).

          start_time: Start time (Unix timestamp).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/ai-gateway/billing/usage-history", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "value_grouping_window": value_grouping_window,
                        "end_time": end_time,
                        "start_time": start_time,
                    },
                    billing_usage_history_params.BillingUsageHistoryParams,
                ),
                post_parser=ResultWrapper[BillingUsageHistoryResponse]._unwrapper,
            ),
            cast_to=cast(Type[BillingUsageHistoryResponse], ResultWrapper[BillingUsageHistoryResponse]),
        )


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def topup(self) -> AsyncTopupResource:
        return AsyncTopupResource(self._client)

    @cached_property
    def spending_limit(self) -> AsyncSpendingLimitResource:
        return AsyncSpendingLimitResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBillingResourceWithStreamingResponse(self)

    async def credit_balance(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingCreditBalanceResponse:
        """
        Retrieve the current credit balance, payment method info, and top-up
        configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/ai-gateway/billing/credit-balance", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BillingCreditBalanceResponse]._unwrapper,
            ),
            cast_to=cast(Type[BillingCreditBalanceResponse], ResultWrapper[BillingCreditBalanceResponse]),
        )

    async def invoice_history(
        self,
        *,
        account_id: str,
        type: Literal["auto", "all", "manual"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingInvoiceHistoryResponse:
        """
        Retrieve a list of past invoices with pagination, optionally filtered by type.

        Args:
          type: Filter invoice type: auto, manual, or all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/ai-gateway/billing/invoice-history", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"type": type}, billing_invoice_history_params.BillingInvoiceHistoryParams
                ),
                post_parser=ResultWrapper[BillingInvoiceHistoryResponse]._unwrapper,
            ),
            cast_to=cast(Type[BillingInvoiceHistoryResponse], ResultWrapper[BillingInvoiceHistoryResponse]),
        )

    async def invoice_preview(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingInvoicePreviewResponse:
        """
        Retrieve a preview of the upcoming invoice including line items and tax.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/ai-gateway/billing/invoice-preview", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BillingInvoicePreviewResponse]._unwrapper,
            ),
            cast_to=cast(Type[BillingInvoicePreviewResponse], ResultWrapper[BillingInvoicePreviewResponse]),
        )

    async def usage_history(
        self,
        *,
        account_id: str,
        value_grouping_window: Literal["day", "hour"],
        end_time: Optional[float] | Omit = omit,
        start_time: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingUsageHistoryResponse:
        """
        Retrieve aggregated usage meter event summaries for the given time range.

        Args:
          value_grouping_window: Grouping window for usage data.

          end_time: End time (Unix timestamp).

          start_time: Start time (Unix timestamp).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/ai-gateway/billing/usage-history", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "value_grouping_window": value_grouping_window,
                        "end_time": end_time,
                        "start_time": start_time,
                    },
                    billing_usage_history_params.BillingUsageHistoryParams,
                ),
                post_parser=ResultWrapper[BillingUsageHistoryResponse]._unwrapper,
            ),
            cast_to=cast(Type[BillingUsageHistoryResponse], ResultWrapper[BillingUsageHistoryResponse]),
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.credit_balance = to_raw_response_wrapper(
            billing.credit_balance,
        )
        self.invoice_history = to_raw_response_wrapper(
            billing.invoice_history,
        )
        self.invoice_preview = to_raw_response_wrapper(
            billing.invoice_preview,
        )
        self.usage_history = to_raw_response_wrapper(
            billing.usage_history,
        )

    @cached_property
    def topup(self) -> TopupResourceWithRawResponse:
        return TopupResourceWithRawResponse(self._billing.topup)

    @cached_property
    def spending_limit(self) -> SpendingLimitResourceWithRawResponse:
        return SpendingLimitResourceWithRawResponse(self._billing.spending_limit)


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.credit_balance = async_to_raw_response_wrapper(
            billing.credit_balance,
        )
        self.invoice_history = async_to_raw_response_wrapper(
            billing.invoice_history,
        )
        self.invoice_preview = async_to_raw_response_wrapper(
            billing.invoice_preview,
        )
        self.usage_history = async_to_raw_response_wrapper(
            billing.usage_history,
        )

    @cached_property
    def topup(self) -> AsyncTopupResourceWithRawResponse:
        return AsyncTopupResourceWithRawResponse(self._billing.topup)

    @cached_property
    def spending_limit(self) -> AsyncSpendingLimitResourceWithRawResponse:
        return AsyncSpendingLimitResourceWithRawResponse(self._billing.spending_limit)


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.credit_balance = to_streamed_response_wrapper(
            billing.credit_balance,
        )
        self.invoice_history = to_streamed_response_wrapper(
            billing.invoice_history,
        )
        self.invoice_preview = to_streamed_response_wrapper(
            billing.invoice_preview,
        )
        self.usage_history = to_streamed_response_wrapper(
            billing.usage_history,
        )

    @cached_property
    def topup(self) -> TopupResourceWithStreamingResponse:
        return TopupResourceWithStreamingResponse(self._billing.topup)

    @cached_property
    def spending_limit(self) -> SpendingLimitResourceWithStreamingResponse:
        return SpendingLimitResourceWithStreamingResponse(self._billing.spending_limit)


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.credit_balance = async_to_streamed_response_wrapper(
            billing.credit_balance,
        )
        self.invoice_history = async_to_streamed_response_wrapper(
            billing.invoice_history,
        )
        self.invoice_preview = async_to_streamed_response_wrapper(
            billing.invoice_preview,
        )
        self.usage_history = async_to_streamed_response_wrapper(
            billing.usage_history,
        )

    @cached_property
    def topup(self) -> AsyncTopupResourceWithStreamingResponse:
        return AsyncTopupResourceWithStreamingResponse(self._billing.topup)

    @cached_property
    def spending_limit(self) -> AsyncSpendingLimitResourceWithStreamingResponse:
        return AsyncSpendingLimitResourceWithStreamingResponse(self._billing.spending_limit)
