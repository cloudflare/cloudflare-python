# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.ai_gateway import evaluation_type_list_params
from ...types.ai_gateway.evaluation_type_list_response import EvaluationTypeListResponse

__all__ = ["EvaluationTypesResource", "AsyncEvaluationTypesResource"]


class EvaluationTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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

    def list(
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
    ) -> SyncV4PagePaginationArray[EvaluationTypeListResponse]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/ai-gateway/evaluation-types",
            page=SyncV4PagePaginationArray[EvaluationTypeListResponse],
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
                    evaluation_type_list_params.EvaluationTypeListParams,
                ),
            ),
            model=EvaluationTypeListResponse,
        )


class AsyncEvaluationTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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

    def list(
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
    ) -> AsyncPaginator[EvaluationTypeListResponse, AsyncV4PagePaginationArray[EvaluationTypeListResponse]]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/ai-gateway/evaluation-types",
            page=AsyncV4PagePaginationArray[EvaluationTypeListResponse],
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
                    evaluation_type_list_params.EvaluationTypeListParams,
                ),
            ),
            model=EvaluationTypeListResponse,
        )


class EvaluationTypesResourceWithRawResponse:
    def __init__(self, evaluation_types: EvaluationTypesResource) -> None:
        self._evaluation_types = evaluation_types

        self.list = to_raw_response_wrapper(
            evaluation_types.list,
        )


class AsyncEvaluationTypesResourceWithRawResponse:
    def __init__(self, evaluation_types: AsyncEvaluationTypesResource) -> None:
        self._evaluation_types = evaluation_types

        self.list = async_to_raw_response_wrapper(
            evaluation_types.list,
        )


class EvaluationTypesResourceWithStreamingResponse:
    def __init__(self, evaluation_types: EvaluationTypesResource) -> None:
        self._evaluation_types = evaluation_types

        self.list = to_streamed_response_wrapper(
            evaluation_types.list,
        )


class AsyncEvaluationTypesResourceWithStreamingResponse:
    def __init__(self, evaluation_types: AsyncEvaluationTypesResource) -> None:
        self._evaluation_types = evaluation_types

        self.list = async_to_streamed_response_wrapper(
            evaluation_types.list,
        )
