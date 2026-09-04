# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Type, Union, cast
from datetime import date

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.billing import (
    usage_get_params,
    usage_paygo_params,
    usage_get_account_usage_v1_params,
    usage_get_account_usage_v2_params,
)
from ...types.billing.usage_get_response import UsageGetResponse
from ...types.billing.usage_paygo_response import UsagePaygoResponse
from ...types.billing.usage_paygo_info_response import UsagePaygoInfoResponse
from ...types.billing.usage_get_account_usage_v1_response import UsageGetAccountUsageV1Response
from ...types.billing.usage_get_account_usage_v2_response import UsageGetAccountUsageV2Response
from ...types.billing.usage_get_account_usage_info_v1_response import UsageGetAccountUsageInfoV1Response

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

    @typing_extensions.deprecated("Use `get_account_usage_v2` instead.")
    def get(
        self,
        *,
        account_id: str,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetResponse:
        """
        Returns cost and usage data for a single Cloudflare account, aligned with the
        [FinOps FOCUS v1.3](https://focus.finops.org/focus-specification/v1-3/) Cost and
        Usage dataset specification.

        Each record represents one billable metric for one account on one day. This
        includes all metered usage, including usage that falls within free-tier
        allowances and may result in zero cost.

        **Note:** Cost and pricing fields are not yet populated and will be absent from
        responses until billing integration is complete.

        When `from` and `to` are omitted, defaults to the start of the current month
        through today. The maximum date range is 31 days.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          from_: Start date for the usage query (ISO 8601). Required if `to` is set. When omitted
              along with `to`, defaults to the start of the current month. Filters by charge
              period (when consumption happened), not billing period. The maximum date range
              is 31 days.

          to: End date for the usage query (ISO 8601). Required if `from` is set. When omitted
              along with `from`, defaults to today. Filters by charge period (when consumption
              happened), not billing period. The maximum date range is 31 days.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/billable/usage", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    usage_get_params.UsageGetParams,
                ),
                post_parser=ResultWrapper[UsageGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[UsageGetResponse], ResultWrapper[UsageGetResponse]),
        )

    def get_account_usage_info_v1(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetAccountUsageInfoV1Response:
        """
        Returns high-level usage information for the account, including coverage, and
        subscription metadata.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/billable-usage/info", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UsageGetAccountUsageInfoV1Response]._unwrapper,
            ),
            cast_to=cast(Type[UsageGetAccountUsageInfoV1Response], ResultWrapper[UsageGetAccountUsageInfoV1Response]),
        )

    def get_account_usage_v1(
        self,
        *,
        account_id: str,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetAccountUsageV1Response:
        """Returns billable usage data for the account.

        When no query parameters are
        provided, returns usage for the current billing period.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          from_: Start date for the usage query (ISO 8601). The provided time range must include
              the subscription billing cycle anchor day, otherwise no usage data is returned.
              Use the info endpoint to retrieve the subscription anchor day.

          to: End date for the usage query (ISO 8601).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/billable-usage", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    usage_get_account_usage_v1_params.UsageGetAccountUsageV1Params,
                ),
                post_parser=ResultWrapper[UsageGetAccountUsageV1Response]._unwrapper,
            ),
            cast_to=cast(Type[UsageGetAccountUsageV1Response], ResultWrapper[UsageGetAccountUsageV1Response]),
        )

    def get_account_usage_v2(
        self,
        *,
        account_id: str,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetAccountUsageV2Response:
        """
        Returns cost and usage data for a single Cloudflare account, aligned with the
        [FinOps FOCUS v1.3](https://focus.finops.org/focus-specification/v1-3/) Cost and
        Usage dataset specification.

        Each record represents one billable metric for one account on one day. This
        includes all metered usage, including usage that falls within free-tier
        allowances and may result in zero cost.

        **Note:** Cost and pricing fields are not yet populated and will be absent from
        responses until billing integration is complete.

        When `from` and `to` are omitted, defaults to the start of the current month
        through today. The maximum date range is 31 days.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          from_: Start date for the usage query (ISO 8601). Required if `to` is set. When omitted
              along with `to`, defaults to the start of the current month. Filters by charge
              period (when consumption happened), not billing period. The maximum date range
              is 31 days.

          to: End date for the usage query (ISO 8601). Required if `from` is set. When omitted
              along with `from`, defaults to today. Filters by charge period (when consumption
              happened), not billing period. The maximum date range is 31 days.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/billable/usage", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    usage_get_account_usage_v2_params.UsageGetAccountUsageV2Params,
                ),
                post_parser=ResultWrapper[UsageGetAccountUsageV2Response]._unwrapper,
            ),
            cast_to=cast(Type[UsageGetAccountUsageV2Response], ResultWrapper[UsageGetAccountUsageV2Response]),
        )

    @typing_extensions.deprecated("Use `get_account_usage_v1` instead.")
    def paygo(
        self,
        *,
        account_id: str,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsagePaygoResponse:
        """Returns billable usage data for the account.

        When no query parameters are
        provided, returns usage for the current billing period.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          from_: Start date for the usage query (ISO 8601). The provided time range must include
              the subscription billing cycle anchor day, otherwise no usage data is returned.
              Use the info endpoint to retrieve the subscription anchor day.

          to: End date for the usage query (ISO 8601).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/billable-usage", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    usage_paygo_params.UsagePaygoParams,
                ),
                post_parser=ResultWrapper[UsagePaygoResponse]._unwrapper,
            ),
            cast_to=cast(Type[UsagePaygoResponse], ResultWrapper[UsagePaygoResponse]),
        )

    @typing_extensions.deprecated("Use `get_account_usage_info_v1` instead.")
    def paygo_info(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsagePaygoInfoResponse:
        """
        Returns high-level usage information for the account, including coverage, and
        subscription metadata.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/billable-usage/info", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UsagePaygoInfoResponse]._unwrapper,
            ),
            cast_to=cast(Type[UsagePaygoInfoResponse], ResultWrapper[UsagePaygoInfoResponse]),
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

    @typing_extensions.deprecated("Use `get_account_usage_v2` instead.")
    async def get(
        self,
        *,
        account_id: str,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetResponse:
        """
        Returns cost and usage data for a single Cloudflare account, aligned with the
        [FinOps FOCUS v1.3](https://focus.finops.org/focus-specification/v1-3/) Cost and
        Usage dataset specification.

        Each record represents one billable metric for one account on one day. This
        includes all metered usage, including usage that falls within free-tier
        allowances and may result in zero cost.

        **Note:** Cost and pricing fields are not yet populated and will be absent from
        responses until billing integration is complete.

        When `from` and `to` are omitted, defaults to the start of the current month
        through today. The maximum date range is 31 days.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          from_: Start date for the usage query (ISO 8601). Required if `to` is set. When omitted
              along with `to`, defaults to the start of the current month. Filters by charge
              period (when consumption happened), not billing period. The maximum date range
              is 31 days.

          to: End date for the usage query (ISO 8601). Required if `from` is set. When omitted
              along with `from`, defaults to today. Filters by charge period (when consumption
              happened), not billing period. The maximum date range is 31 days.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/billable/usage", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    usage_get_params.UsageGetParams,
                ),
                post_parser=ResultWrapper[UsageGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[UsageGetResponse], ResultWrapper[UsageGetResponse]),
        )

    async def get_account_usage_info_v1(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetAccountUsageInfoV1Response:
        """
        Returns high-level usage information for the account, including coverage, and
        subscription metadata.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/billable-usage/info", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UsageGetAccountUsageInfoV1Response]._unwrapper,
            ),
            cast_to=cast(Type[UsageGetAccountUsageInfoV1Response], ResultWrapper[UsageGetAccountUsageInfoV1Response]),
        )

    async def get_account_usage_v1(
        self,
        *,
        account_id: str,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetAccountUsageV1Response:
        """Returns billable usage data for the account.

        When no query parameters are
        provided, returns usage for the current billing period.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          from_: Start date for the usage query (ISO 8601). The provided time range must include
              the subscription billing cycle anchor day, otherwise no usage data is returned.
              Use the info endpoint to retrieve the subscription anchor day.

          to: End date for the usage query (ISO 8601).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/billable-usage", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    usage_get_account_usage_v1_params.UsageGetAccountUsageV1Params,
                ),
                post_parser=ResultWrapper[UsageGetAccountUsageV1Response]._unwrapper,
            ),
            cast_to=cast(Type[UsageGetAccountUsageV1Response], ResultWrapper[UsageGetAccountUsageV1Response]),
        )

    async def get_account_usage_v2(
        self,
        *,
        account_id: str,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetAccountUsageV2Response:
        """
        Returns cost and usage data for a single Cloudflare account, aligned with the
        [FinOps FOCUS v1.3](https://focus.finops.org/focus-specification/v1-3/) Cost and
        Usage dataset specification.

        Each record represents one billable metric for one account on one day. This
        includes all metered usage, including usage that falls within free-tier
        allowances and may result in zero cost.

        **Note:** Cost and pricing fields are not yet populated and will be absent from
        responses until billing integration is complete.

        When `from` and `to` are omitted, defaults to the start of the current month
        through today. The maximum date range is 31 days.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          from_: Start date for the usage query (ISO 8601). Required if `to` is set. When omitted
              along with `to`, defaults to the start of the current month. Filters by charge
              period (when consumption happened), not billing period. The maximum date range
              is 31 days.

          to: End date for the usage query (ISO 8601). Required if `from` is set. When omitted
              along with `from`, defaults to today. Filters by charge period (when consumption
              happened), not billing period. The maximum date range is 31 days.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/billable/usage", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    usage_get_account_usage_v2_params.UsageGetAccountUsageV2Params,
                ),
                post_parser=ResultWrapper[UsageGetAccountUsageV2Response]._unwrapper,
            ),
            cast_to=cast(Type[UsageGetAccountUsageV2Response], ResultWrapper[UsageGetAccountUsageV2Response]),
        )

    @typing_extensions.deprecated("Use `get_account_usage_v1` instead.")
    async def paygo(
        self,
        *,
        account_id: str,
        from_: Union[str, date] | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsagePaygoResponse:
        """Returns billable usage data for the account.

        When no query parameters are
        provided, returns usage for the current billing period.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          from_: Start date for the usage query (ISO 8601). The provided time range must include
              the subscription billing cycle anchor day, otherwise no usage data is returned.
              Use the info endpoint to retrieve the subscription anchor day.

          to: End date for the usage query (ISO 8601).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/billable-usage", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    usage_paygo_params.UsagePaygoParams,
                ),
                post_parser=ResultWrapper[UsagePaygoResponse]._unwrapper,
            ),
            cast_to=cast(Type[UsagePaygoResponse], ResultWrapper[UsagePaygoResponse]),
        )

    @typing_extensions.deprecated("Use `get_account_usage_info_v1` instead.")
    async def paygo_info(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsagePaygoInfoResponse:
        """
        Returns high-level usage information for the account, including coverage, and
        subscription metadata.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/billable-usage/info", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UsagePaygoInfoResponse]._unwrapper,
            ),
            cast_to=cast(Type[UsagePaygoInfoResponse], ResultWrapper[UsagePaygoInfoResponse]),
        )


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                usage.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_account_usage_info_v1 = to_raw_response_wrapper(
            usage.get_account_usage_info_v1,
        )
        self.get_account_usage_v1 = to_raw_response_wrapper(
            usage.get_account_usage_v1,
        )
        self.get_account_usage_v2 = to_raw_response_wrapper(
            usage.get_account_usage_v2,
        )
        self.paygo = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                usage.paygo,  # pyright: ignore[reportDeprecated],
            )
        )
        self.paygo_info = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                usage.paygo_info,  # pyright: ignore[reportDeprecated],
            )
        )
        self.paygo_info = to_raw_response_wrapper(
            usage.paygo_info,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                usage.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_account_usage_info_v1 = async_to_raw_response_wrapper(
            usage.get_account_usage_info_v1,
        )
        self.get_account_usage_v1 = async_to_raw_response_wrapper(
            usage.get_account_usage_v1,
        )
        self.get_account_usage_v2 = async_to_raw_response_wrapper(
            usage.get_account_usage_v2,
        )
        self.paygo = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                usage.paygo,  # pyright: ignore[reportDeprecated],
            )
        )
        self.paygo_info = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                usage.paygo_info,  # pyright: ignore[reportDeprecated],
            )
        )
        self.paygo_info = async_to_raw_response_wrapper(
            usage.paygo_info,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                usage.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_account_usage_info_v1 = to_streamed_response_wrapper(
            usage.get_account_usage_info_v1,
        )
        self.get_account_usage_v1 = to_streamed_response_wrapper(
            usage.get_account_usage_v1,
        )
        self.get_account_usage_v2 = to_streamed_response_wrapper(
            usage.get_account_usage_v2,
        )
        self.paygo = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                usage.paygo,  # pyright: ignore[reportDeprecated],
            )
        )
        self.paygo_info = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                usage.paygo_info,  # pyright: ignore[reportDeprecated],
            )
        )
        self.paygo_info = to_streamed_response_wrapper(
            usage.paygo_info,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                usage.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_account_usage_info_v1 = async_to_streamed_response_wrapper(
            usage.get_account_usage_info_v1,
        )
        self.get_account_usage_v1 = async_to_streamed_response_wrapper(
            usage.get_account_usage_v1,
        )
        self.get_account_usage_v2 = async_to_streamed_response_wrapper(
            usage.get_account_usage_v2,
        )
        self.paygo = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                usage.paygo,  # pyright: ignore[reportDeprecated],
            )
        )
        self.paygo_info = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                usage.paygo_info,  # pyright: ignore[reportDeprecated],
            )
        )
        self.paygo_info = async_to_streamed_response_wrapper(
            usage.paygo_info,
        )
