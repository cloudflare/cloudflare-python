# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloudforce_one.threat_events import target_industry_list_params
from ....types.cloudforce_one.threat_events.target_industry_list_response import TargetIndustryListResponse

__all__ = ["TargetIndustriesResource", "AsyncTargetIndustriesResource"]


class TargetIndustriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TargetIndustriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TargetIndustriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TargetIndustriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TargetIndustriesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        dataset_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TargetIndustryListResponse:
        """
        Lists target industries across multiple datasets

        Args:
          account_id: Account ID.

          dataset_ids: Array of dataset IDs to query target industries from. If not provided, uses the
              default dataset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/cloudforce-one/events/targetIndustries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"dataset_ids": dataset_ids}, target_industry_list_params.TargetIndustryListParams
                ),
            ),
            cast_to=TargetIndustryListResponse,
        )


class AsyncTargetIndustriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTargetIndustriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTargetIndustriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTargetIndustriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTargetIndustriesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        dataset_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TargetIndustryListResponse:
        """
        Lists target industries across multiple datasets

        Args:
          account_id: Account ID.

          dataset_ids: Array of dataset IDs to query target industries from. If not provided, uses the
              default dataset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/cloudforce-one/events/targetIndustries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dataset_ids": dataset_ids}, target_industry_list_params.TargetIndustryListParams
                ),
            ),
            cast_to=TargetIndustryListResponse,
        )


class TargetIndustriesResourceWithRawResponse:
    def __init__(self, target_industries: TargetIndustriesResource) -> None:
        self._target_industries = target_industries

        self.list = to_raw_response_wrapper(
            target_industries.list,
        )


class AsyncTargetIndustriesResourceWithRawResponse:
    def __init__(self, target_industries: AsyncTargetIndustriesResource) -> None:
        self._target_industries = target_industries

        self.list = async_to_raw_response_wrapper(
            target_industries.list,
        )


class TargetIndustriesResourceWithStreamingResponse:
    def __init__(self, target_industries: TargetIndustriesResource) -> None:
        self._target_industries = target_industries

        self.list = to_streamed_response_wrapper(
            target_industries.list,
        )


class AsyncTargetIndustriesResourceWithStreamingResponse:
    def __init__(self, target_industries: AsyncTargetIndustriesResource) -> None:
        self._target_industries = target_industries

        self.list = async_to_streamed_response_wrapper(
            target_industries.list,
        )
