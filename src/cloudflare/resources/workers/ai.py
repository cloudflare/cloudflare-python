# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

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
from ..._base_client import (
    make_request_options,
)
from ...types.workers import ai_run_params

__all__ = ["AI", "AsyncAI"]


class AI(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AIWithRawResponse:
        return AIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIWithStreamingResponse:
        return AIWithStreamingResponse(self)

    def run(
        self,
        model_name: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        This endpoint provides users with the capability to run specific AI models
        on-demand.

        By submitting the required input data, users can receive real-time predictions
        or results generated by the chosen AI model. The endpoint supports various AI
        model types, ensuring flexibility and adaptability for diverse use cases.

        Model specific inputs available in
        [Cloudflare Docs](https://developers.cloudflare.com/workers-ai/models/).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not model_name:
            raise ValueError(f"Expected a non-empty value for `model_name` but received {model_name!r}")
        return self._post(
            f"/accounts/{account_id}/ai/run/{model_name}",
            body=maybe_transform(body, ai_run_params.AIRunParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncAI(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAIWithRawResponse:
        return AsyncAIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIWithStreamingResponse:
        return AsyncAIWithStreamingResponse(self)

    async def run(
        self,
        model_name: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        This endpoint provides users with the capability to run specific AI models
        on-demand.

        By submitting the required input data, users can receive real-time predictions
        or results generated by the chosen AI model. The endpoint supports various AI
        model types, ensuring flexibility and adaptability for diverse use cases.

        Model specific inputs available in
        [Cloudflare Docs](https://developers.cloudflare.com/workers-ai/models/).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not model_name:
            raise ValueError(f"Expected a non-empty value for `model_name` but received {model_name!r}")
        return await self._post(
            f"/accounts/{account_id}/ai/run/{model_name}",
            body=await async_maybe_transform(body, ai_run_params.AIRunParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AIWithRawResponse:
    def __init__(self, ai: AI) -> None:
        self._ai = ai

        self.run = to_raw_response_wrapper(
            ai.run,
        )


class AsyncAIWithRawResponse:
    def __init__(self, ai: AsyncAI) -> None:
        self._ai = ai

        self.run = async_to_raw_response_wrapper(
            ai.run,
        )


class AIWithStreamingResponse:
    def __init__(self, ai: AI) -> None:
        self._ai = ai

        self.run = to_streamed_response_wrapper(
            ai.run,
        )


class AsyncAIWithStreamingResponse:
    def __init__(self, ai: AsyncAI) -> None:
        self._ai = ai

        self.run = async_to_streamed_response_wrapper(
            ai.run,
        )
