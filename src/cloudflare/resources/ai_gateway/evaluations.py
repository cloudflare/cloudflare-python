# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast

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
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.ai_gateway import evaluation_list_params, evaluation_create_params
from ...types.ai_gateway.evaluation_get_response import EvaluationGetResponse
from ...types.ai_gateway.evaluation_list_response import EvaluationListResponse
from ...types.ai_gateway.evaluation_create_response import EvaluationCreateResponse
from ...types.ai_gateway.evaluation_delete_response import EvaluationDeleteResponse

__all__ = ["EvaluationsResource", "AsyncEvaluationsResource"]


class EvaluationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EvaluationsResourceWithStreamingResponse(self)

    def create(
        self,
        gateway_id: str,
        *,
        account_id: str,
        dataset_ids: List[str],
        evaluation_type_ids: List[str],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationCreateResponse:
        """
        Create a new Evaluation

        Args:
          gateway_id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return self._post(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations",
            body=maybe_transform(
                {
                    "dataset_ids": dataset_ids,
                    "evaluation_type_ids": evaluation_type_ids,
                    "name": name,
                },
                evaluation_create_params.EvaluationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EvaluationCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[EvaluationCreateResponse], ResultWrapper[EvaluationCreateResponse]),
        )

    def list(
        self,
        gateway_id: str,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        processed: bool | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[EvaluationListResponse]:
        """
        List Evaluations

        Args:
          gateway_id: gateway id

          search: Search by id, name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations",
            page=SyncV4PagePaginationArray[EvaluationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "processed": processed,
                        "search": search,
                    },
                    evaluation_list_params.EvaluationListParams,
                ),
            ),
            model=EvaluationListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDeleteResponse:
        """
        Delete a Evaluation

        Args:
          gateway_id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EvaluationDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[EvaluationDeleteResponse], ResultWrapper[EvaluationDeleteResponse]),
        )

    def get(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationGetResponse:
        """
        Fetch a Evaluation

        Args:
          gateway_id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EvaluationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[EvaluationGetResponse], ResultWrapper[EvaluationGetResponse]),
        )


class AsyncEvaluationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEvaluationsResourceWithStreamingResponse(self)

    async def create(
        self,
        gateway_id: str,
        *,
        account_id: str,
        dataset_ids: List[str],
        evaluation_type_ids: List[str],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationCreateResponse:
        """
        Create a new Evaluation

        Args:
          gateway_id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return await self._post(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations",
            body=await async_maybe_transform(
                {
                    "dataset_ids": dataset_ids,
                    "evaluation_type_ids": evaluation_type_ids,
                    "name": name,
                },
                evaluation_create_params.EvaluationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EvaluationCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[EvaluationCreateResponse], ResultWrapper[EvaluationCreateResponse]),
        )

    def list(
        self,
        gateway_id: str,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        processed: bool | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EvaluationListResponse, AsyncV4PagePaginationArray[EvaluationListResponse]]:
        """
        List Evaluations

        Args:
          gateway_id: gateway id

          search: Search by id, name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations",
            page=AsyncV4PagePaginationArray[EvaluationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "processed": processed,
                        "search": search,
                    },
                    evaluation_list_params.EvaluationListParams,
                ),
            ),
            model=EvaluationListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDeleteResponse:
        """
        Delete a Evaluation

        Args:
          gateway_id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EvaluationDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[EvaluationDeleteResponse], ResultWrapper[EvaluationDeleteResponse]),
        )

    async def get(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationGetResponse:
        """
        Fetch a Evaluation

        Args:
          gateway_id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EvaluationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[EvaluationGetResponse], ResultWrapper[EvaluationGetResponse]),
        )


class EvaluationsResourceWithRawResponse:
    def __init__(self, evaluations: EvaluationsResource) -> None:
        self._evaluations = evaluations

        self.create = to_raw_response_wrapper(
            evaluations.create,
        )
        self.list = to_raw_response_wrapper(
            evaluations.list,
        )
        self.delete = to_raw_response_wrapper(
            evaluations.delete,
        )
        self.get = to_raw_response_wrapper(
            evaluations.get,
        )


class AsyncEvaluationsResourceWithRawResponse:
    def __init__(self, evaluations: AsyncEvaluationsResource) -> None:
        self._evaluations = evaluations

        self.create = async_to_raw_response_wrapper(
            evaluations.create,
        )
        self.list = async_to_raw_response_wrapper(
            evaluations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            evaluations.delete,
        )
        self.get = async_to_raw_response_wrapper(
            evaluations.get,
        )


class EvaluationsResourceWithStreamingResponse:
    def __init__(self, evaluations: EvaluationsResource) -> None:
        self._evaluations = evaluations

        self.create = to_streamed_response_wrapper(
            evaluations.create,
        )
        self.list = to_streamed_response_wrapper(
            evaluations.list,
        )
        self.delete = to_streamed_response_wrapper(
            evaluations.delete,
        )
        self.get = to_streamed_response_wrapper(
            evaluations.get,
        )


class AsyncEvaluationsResourceWithStreamingResponse:
    def __init__(self, evaluations: AsyncEvaluationsResource) -> None:
        self._evaluations = evaluations

        self.create = async_to_streamed_response_wrapper(
            evaluations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            evaluations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            evaluations.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            evaluations.get,
        )
