# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cloudforce_one.threat_events.indicators import type_list_params
from .....types.cloudforce_one.threat_events.indicators.type_list_response import TypeListResponse

__all__ = ["TypesResource", "AsyncTypesResource"]


class TypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TypesResourceWithStreamingResponse(self)

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
    ) -> TypeListResponse:
        """
        List indicator types across one or more datasets for the account.

        Args:
          account_id: Account ID.

          dataset_ids: Array of dataset IDs to query indicator types from. If not provided, queries all
              datasets for the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/indicator-types", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dataset_ids": dataset_ids}, type_list_params.TypeListParams),
            ),
            cast_to=TypeListResponse,
        )


class AsyncTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTypesResourceWithStreamingResponse(self)

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
    ) -> TypeListResponse:
        """
        List indicator types across one or more datasets for the account.

        Args:
          account_id: Account ID.

          dataset_ids: Array of dataset IDs to query indicator types from. If not provided, queries all
              datasets for the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/indicator-types", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"dataset_ids": dataset_ids}, type_list_params.TypeListParams),
            ),
            cast_to=TypeListResponse,
        )


class TypesResourceWithRawResponse:
    def __init__(self, types: TypesResource) -> None:
        self._types = types

        self.list = to_raw_response_wrapper(
            types.list,
        )


class AsyncTypesResourceWithRawResponse:
    def __init__(self, types: AsyncTypesResource) -> None:
        self._types = types

        self.list = async_to_raw_response_wrapper(
            types.list,
        )


class TypesResourceWithStreamingResponse:
    def __init__(self, types: TypesResource) -> None:
        self._types = types

        self.list = to_streamed_response_wrapper(
            types.list,
        )


class AsyncTypesResourceWithStreamingResponse:
    def __init__(self, types: AsyncTypesResource) -> None:
        self._types = types

        self.list = async_to_streamed_response_wrapper(
            types.list,
        )
