# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.workers.scripts import UsageModelGetResponse, UsageModelUpdateResponse, usage_model_update_params

__all__ = ["UsageModel", "AsyncUsageModel"]


class UsageModel(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageModelWithRawResponse:
        return UsageModelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageModelWithStreamingResponse:
        return UsageModelWithStreamingResponse(self)

    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageModelUpdateResponse:
        """Updates the Usage Model for a given Worker.

        Requires a Workers Paid
        subscription.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._put(
            f"/accounts/{account_id}/workers/scripts/{script_name}/usage-model",
            body=maybe_transform(body, usage_model_update_params.UsageModelUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[UsageModelUpdateResponse], ResultWrapper[UsageModelUpdateResponse]),
        )

    def get(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageModelGetResponse:
        """
        Fetches the Usage Model for a given Worker.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/usage-model",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[UsageModelGetResponse], ResultWrapper[UsageModelGetResponse]),
        )


class AsyncUsageModel(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageModelWithRawResponse:
        return AsyncUsageModelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageModelWithStreamingResponse:
        return AsyncUsageModelWithStreamingResponse(self)

    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageModelUpdateResponse:
        """Updates the Usage Model for a given Worker.

        Requires a Workers Paid
        subscription.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._put(
            f"/accounts/{account_id}/workers/scripts/{script_name}/usage-model",
            body=await async_maybe_transform(body, usage_model_update_params.UsageModelUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[UsageModelUpdateResponse], ResultWrapper[UsageModelUpdateResponse]),
        )

    async def get(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageModelGetResponse:
        """
        Fetches the Usage Model for a given Worker.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/usage-model",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[UsageModelGetResponse], ResultWrapper[UsageModelGetResponse]),
        )


class UsageModelWithRawResponse:
    def __init__(self, usage_model: UsageModel) -> None:
        self._usage_model = usage_model

        self.update = to_raw_response_wrapper(
            usage_model.update,
        )
        self.get = to_raw_response_wrapper(
            usage_model.get,
        )


class AsyncUsageModelWithRawResponse:
    def __init__(self, usage_model: AsyncUsageModel) -> None:
        self._usage_model = usage_model

        self.update = async_to_raw_response_wrapper(
            usage_model.update,
        )
        self.get = async_to_raw_response_wrapper(
            usage_model.get,
        )


class UsageModelWithStreamingResponse:
    def __init__(self, usage_model: UsageModel) -> None:
        self._usage_model = usage_model

        self.update = to_streamed_response_wrapper(
            usage_model.update,
        )
        self.get = to_streamed_response_wrapper(
            usage_model.get,
        )


class AsyncUsageModelWithStreamingResponse:
    def __init__(self, usage_model: AsyncUsageModel) -> None:
        self._usage_model = usage_model

        self.update = async_to_streamed_response_wrapper(
            usage_model.update,
        )
        self.get = async_to_streamed_response_wrapper(
            usage_model.get,
        )
