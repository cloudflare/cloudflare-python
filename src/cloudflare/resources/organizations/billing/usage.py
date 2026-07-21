# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import date

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
from ....types.organizations.billing import usage_get_params
from ....types.organizations.billing.usage_get_response import UsageGetResponse

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

    def get(
        self,
        organization_id: str,
        *,
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
        Returns cost and usage data for all accounts within an organization, aligned
        with the [FinOps FOCUS v1.3](https://focus.finops.org/focus-specification/v1-3/)
        Cost and Usage dataset specification.

        Each record represents one billable metric for one account on one day. This
        includes all metered usage, including usage that falls within free-tier
        allowances and may result in zero cost. The response includes usage for every
        account belonging to the specified organization.

        **Note:** Cost and pricing fields are not yet populated and will be absent from
        responses until billing integration is complete.

        When `from` and `to` are omitted, defaults to the start of the current month
        through today. The maximum date range is 31 days.

        Args:
          organization_id: Represents a Cloudflare resource identifier tag.

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
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            path_template("/organizations/{organization_id}/billable/usage", organization_id=organization_id),
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

    async def get(
        self,
        organization_id: str,
        *,
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
        Returns cost and usage data for all accounts within an organization, aligned
        with the [FinOps FOCUS v1.3](https://focus.finops.org/focus-specification/v1-3/)
        Cost and Usage dataset specification.

        Each record represents one billable metric for one account on one day. This
        includes all metered usage, including usage that falls within free-tier
        allowances and may result in zero cost. The response includes usage for every
        account belonging to the specified organization.

        **Note:** Cost and pricing fields are not yet populated and will be absent from
        responses until billing integration is complete.

        When `from` and `to` are omitted, defaults to the start of the current month
        through today. The maximum date range is 31 days.

        Args:
          organization_id: Represents a Cloudflare resource identifier tag.

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
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            path_template("/organizations/{organization_id}/billable/usage", organization_id=organization_id),
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


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.get = to_raw_response_wrapper(
            usage.get,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.get = async_to_raw_response_wrapper(
            usage.get,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.get = to_streamed_response_wrapper(
            usage.get,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.get = async_to_streamed_response_wrapper(
            usage.get,
        )
