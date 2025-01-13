# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

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
from ..._base_client import make_request_options
from ...types.ai_gateway import evaluation_type_get_params
from ...types.ai_gateway.evaluation_type_get_response import EvaluationTypeGetResponse

__all__ = ["EvaluationTypesResource", "AsyncEvaluationTypesResource"]


class EvaluationTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EvaluationTypesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        order_by: str | NotGiven = NOT_GIVEN,
        order_by_direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationTypeGetResponse:
        """
        List Evaluators

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/ai-gateway/evaluation-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "per_page": per_page,
                    },
                    evaluation_type_get_params.EvaluationTypeGetParams,
                ),
                post_parser=ResultWrapper[EvaluationTypeGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[EvaluationTypeGetResponse], ResultWrapper[EvaluationTypeGetResponse]),
        )


class AsyncEvaluationTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEvaluationTypesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        order_by: str | NotGiven = NOT_GIVEN,
        order_by_direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationTypeGetResponse:
        """
        List Evaluators

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-gateway/evaluation-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "per_page": per_page,
                    },
                    evaluation_type_get_params.EvaluationTypeGetParams,
                ),
                post_parser=ResultWrapper[EvaluationTypeGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[EvaluationTypeGetResponse], ResultWrapper[EvaluationTypeGetResponse]),
        )


class EvaluationTypesResourceWithRawResponse:
    def __init__(self, evaluation_types: EvaluationTypesResource) -> None:
        self._evaluation_types = evaluation_types

        self.get = to_raw_response_wrapper(
            evaluation_types.get,
        )


class AsyncEvaluationTypesResourceWithRawResponse:
    def __init__(self, evaluation_types: AsyncEvaluationTypesResource) -> None:
        self._evaluation_types = evaluation_types

        self.get = async_to_raw_response_wrapper(
            evaluation_types.get,
        )


class EvaluationTypesResourceWithStreamingResponse:
    def __init__(self, evaluation_types: EvaluationTypesResource) -> None:
        self._evaluation_types = evaluation_types

        self.get = to_streamed_response_wrapper(
            evaluation_types.get,
        )


class AsyncEvaluationTypesResourceWithStreamingResponse:
    def __init__(self, evaluation_types: AsyncEvaluationTypesResource) -> None:
        self._evaluation_types = evaluation_types

        self.get = async_to_streamed_response_wrapper(
            evaluation_types.get,
        )
