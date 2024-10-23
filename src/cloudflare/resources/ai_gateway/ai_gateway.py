# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
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
from .evaluations import (
    EvaluationsResource,
    AsyncEvaluationsResource,
    EvaluationsResourceWithRawResponse,
    AsyncEvaluationsResourceWithRawResponse,
    EvaluationsResourceWithStreamingResponse,
    AsyncEvaluationsResourceWithStreamingResponse,
)
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from .evaluation_types import (
    EvaluationTypesResource,
    AsyncEvaluationTypesResource,
    EvaluationTypesResourceWithRawResponse,
    AsyncEvaluationTypesResourceWithRawResponse,
    EvaluationTypesResourceWithStreamingResponse,
    AsyncEvaluationTypesResourceWithStreamingResponse,
)
from ...types.ai_gateway import ai_gateway_list_params, ai_gateway_create_params, ai_gateway_update_params
from ...types.ai_gateway.ai_gateway_get_response import AIGatewayGetResponse
from ...types.ai_gateway.ai_gateway_list_response import AIGatewayListResponse
from ...types.ai_gateway.ai_gateway_create_response import AIGatewayCreateResponse
from ...types.ai_gateway.ai_gateway_delete_response import AIGatewayDeleteResponse
from ...types.ai_gateway.ai_gateway_update_response import AIGatewayUpdateResponse

__all__ = ["AIGatewayResource", "AsyncAIGatewayResource"]


class AIGatewayResource(SyncAPIResource):
    @cached_property
    def evaluation_types(self) -> EvaluationTypesResource:
        return EvaluationTypesResource(self._client)

    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def datasets(self) -> DatasetsResource:
        return DatasetsResource(self._client)

    @cached_property
    def evaluations(self) -> EvaluationsResource:
        return EvaluationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AIGatewayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AIGatewayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIGatewayResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AIGatewayResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        id: str,
        cache_invalidate_on_update: bool,
        cache_ttl: Optional[int],
        collect_logs: bool,
        rate_limiting_interval: Optional[int],
        rate_limiting_limit: Optional[int],
        rate_limiting_technique: Literal["fixed", "sliding"],
        logpush: bool | NotGiven = NOT_GIVEN,
        logpush_public_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIGatewayCreateResponse:
        """
        Create a new Gateway

        Args:
          id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/ai-gateway/gateways",
            body=maybe_transform(
                {
                    "id": id,
                    "cache_invalidate_on_update": cache_invalidate_on_update,
                    "cache_ttl": cache_ttl,
                    "collect_logs": collect_logs,
                    "rate_limiting_interval": rate_limiting_interval,
                    "rate_limiting_limit": rate_limiting_limit,
                    "rate_limiting_technique": rate_limiting_technique,
                    "logpush": logpush,
                    "logpush_public_key": logpush_public_key,
                },
                ai_gateway_create_params.AIGatewayCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AIGatewayCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[AIGatewayCreateResponse], ResultWrapper[AIGatewayCreateResponse]),
        )

    def update(
        self,
        id: str,
        *,
        account_id: str,
        cache_invalidate_on_update: bool,
        cache_ttl: Optional[int],
        collect_logs: bool,
        rate_limiting_interval: Optional[int],
        rate_limiting_limit: Optional[int],
        rate_limiting_technique: Literal["fixed", "sliding"],
        logpush: bool | NotGiven = NOT_GIVEN,
        logpush_public_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIGatewayUpdateResponse:
        """
        Update a Gateway

        Args:
          id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/accounts/{account_id}/ai-gateway/gateways/{id}",
            body=maybe_transform(
                {
                    "cache_invalidate_on_update": cache_invalidate_on_update,
                    "cache_ttl": cache_ttl,
                    "collect_logs": collect_logs,
                    "rate_limiting_interval": rate_limiting_interval,
                    "rate_limiting_limit": rate_limiting_limit,
                    "rate_limiting_technique": rate_limiting_technique,
                    "logpush": logpush,
                    "logpush_public_key": logpush_public_key,
                },
                ai_gateway_update_params.AIGatewayUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AIGatewayUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[AIGatewayUpdateResponse], ResultWrapper[AIGatewayUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncV4PagePaginationArray[AIGatewayListResponse]:
        """
        List Gateways

        Args:
          id: gateway id

          order_by: Order By Column Name

          order_by_direction: Order By Direction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/ai-gateway/gateways",
            page=SyncV4PagePaginationArray[AIGatewayListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "per_page": per_page,
                    },
                    ai_gateway_list_params.AIGatewayListParams,
                ),
            ),
            model=AIGatewayListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIGatewayDeleteResponse:
        """
        Delete a Gateway

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/accounts/{account_id}/ai-gateway/gateways/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AIGatewayDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[AIGatewayDeleteResponse], ResultWrapper[AIGatewayDeleteResponse]),
        )

    def get(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIGatewayGetResponse:
        """
        Fetch a Gateway

        Args:
          id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AIGatewayGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AIGatewayGetResponse], ResultWrapper[AIGatewayGetResponse]),
        )


class AsyncAIGatewayResource(AsyncAPIResource):
    @cached_property
    def evaluation_types(self) -> AsyncEvaluationTypesResource:
        return AsyncEvaluationTypesResource(self._client)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        return AsyncDatasetsResource(self._client)

    @cached_property
    def evaluations(self) -> AsyncEvaluationsResource:
        return AsyncEvaluationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAIGatewayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAIGatewayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIGatewayResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAIGatewayResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        id: str,
        cache_invalidate_on_update: bool,
        cache_ttl: Optional[int],
        collect_logs: bool,
        rate_limiting_interval: Optional[int],
        rate_limiting_limit: Optional[int],
        rate_limiting_technique: Literal["fixed", "sliding"],
        logpush: bool | NotGiven = NOT_GIVEN,
        logpush_public_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIGatewayCreateResponse:
        """
        Create a new Gateway

        Args:
          id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/ai-gateway/gateways",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "cache_invalidate_on_update": cache_invalidate_on_update,
                    "cache_ttl": cache_ttl,
                    "collect_logs": collect_logs,
                    "rate_limiting_interval": rate_limiting_interval,
                    "rate_limiting_limit": rate_limiting_limit,
                    "rate_limiting_technique": rate_limiting_technique,
                    "logpush": logpush,
                    "logpush_public_key": logpush_public_key,
                },
                ai_gateway_create_params.AIGatewayCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AIGatewayCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[AIGatewayCreateResponse], ResultWrapper[AIGatewayCreateResponse]),
        )

    async def update(
        self,
        id: str,
        *,
        account_id: str,
        cache_invalidate_on_update: bool,
        cache_ttl: Optional[int],
        collect_logs: bool,
        rate_limiting_interval: Optional[int],
        rate_limiting_limit: Optional[int],
        rate_limiting_technique: Literal["fixed", "sliding"],
        logpush: bool | NotGiven = NOT_GIVEN,
        logpush_public_key: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIGatewayUpdateResponse:
        """
        Update a Gateway

        Args:
          id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/accounts/{account_id}/ai-gateway/gateways/{id}",
            body=await async_maybe_transform(
                {
                    "cache_invalidate_on_update": cache_invalidate_on_update,
                    "cache_ttl": cache_ttl,
                    "collect_logs": collect_logs,
                    "rate_limiting_interval": rate_limiting_interval,
                    "rate_limiting_limit": rate_limiting_limit,
                    "rate_limiting_technique": rate_limiting_technique,
                    "logpush": logpush,
                    "logpush_public_key": logpush_public_key,
                },
                ai_gateway_update_params.AIGatewayUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AIGatewayUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[AIGatewayUpdateResponse], ResultWrapper[AIGatewayUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[AIGatewayListResponse, AsyncV4PagePaginationArray[AIGatewayListResponse]]:
        """
        List Gateways

        Args:
          id: gateway id

          order_by: Order By Column Name

          order_by_direction: Order By Direction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/ai-gateway/gateways",
            page=AsyncV4PagePaginationArray[AIGatewayListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "order_by": order_by,
                        "order_by_direction": order_by_direction,
                        "page": page,
                        "per_page": per_page,
                    },
                    ai_gateway_list_params.AIGatewayListParams,
                ),
            ),
            model=AIGatewayListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIGatewayDeleteResponse:
        """
        Delete a Gateway

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/accounts/{account_id}/ai-gateway/gateways/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AIGatewayDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[AIGatewayDeleteResponse], ResultWrapper[AIGatewayDeleteResponse]),
        )

    async def get(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIGatewayGetResponse:
        """
        Fetch a Gateway

        Args:
          id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AIGatewayGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AIGatewayGetResponse], ResultWrapper[AIGatewayGetResponse]),
        )


class AIGatewayResourceWithRawResponse:
    def __init__(self, ai_gateway: AIGatewayResource) -> None:
        self._ai_gateway = ai_gateway

        self.create = to_raw_response_wrapper(
            ai_gateway.create,
        )
        self.update = to_raw_response_wrapper(
            ai_gateway.update,
        )
        self.list = to_raw_response_wrapper(
            ai_gateway.list,
        )
        self.delete = to_raw_response_wrapper(
            ai_gateway.delete,
        )
        self.get = to_raw_response_wrapper(
            ai_gateway.get,
        )

    @cached_property
    def evaluation_types(self) -> EvaluationTypesResourceWithRawResponse:
        return EvaluationTypesResourceWithRawResponse(self._ai_gateway.evaluation_types)

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._ai_gateway.logs)

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self._ai_gateway.datasets)

    @cached_property
    def evaluations(self) -> EvaluationsResourceWithRawResponse:
        return EvaluationsResourceWithRawResponse(self._ai_gateway.evaluations)


class AsyncAIGatewayResourceWithRawResponse:
    def __init__(self, ai_gateway: AsyncAIGatewayResource) -> None:
        self._ai_gateway = ai_gateway

        self.create = async_to_raw_response_wrapper(
            ai_gateway.create,
        )
        self.update = async_to_raw_response_wrapper(
            ai_gateway.update,
        )
        self.list = async_to_raw_response_wrapper(
            ai_gateway.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ai_gateway.delete,
        )
        self.get = async_to_raw_response_wrapper(
            ai_gateway.get,
        )

    @cached_property
    def evaluation_types(self) -> AsyncEvaluationTypesResourceWithRawResponse:
        return AsyncEvaluationTypesResourceWithRawResponse(self._ai_gateway.evaluation_types)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._ai_gateway.logs)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self._ai_gateway.datasets)

    @cached_property
    def evaluations(self) -> AsyncEvaluationsResourceWithRawResponse:
        return AsyncEvaluationsResourceWithRawResponse(self._ai_gateway.evaluations)


class AIGatewayResourceWithStreamingResponse:
    def __init__(self, ai_gateway: AIGatewayResource) -> None:
        self._ai_gateway = ai_gateway

        self.create = to_streamed_response_wrapper(
            ai_gateway.create,
        )
        self.update = to_streamed_response_wrapper(
            ai_gateway.update,
        )
        self.list = to_streamed_response_wrapper(
            ai_gateway.list,
        )
        self.delete = to_streamed_response_wrapper(
            ai_gateway.delete,
        )
        self.get = to_streamed_response_wrapper(
            ai_gateway.get,
        )

    @cached_property
    def evaluation_types(self) -> EvaluationTypesResourceWithStreamingResponse:
        return EvaluationTypesResourceWithStreamingResponse(self._ai_gateway.evaluation_types)

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._ai_gateway.logs)

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self._ai_gateway.datasets)

    @cached_property
    def evaluations(self) -> EvaluationsResourceWithStreamingResponse:
        return EvaluationsResourceWithStreamingResponse(self._ai_gateway.evaluations)


class AsyncAIGatewayResourceWithStreamingResponse:
    def __init__(self, ai_gateway: AsyncAIGatewayResource) -> None:
        self._ai_gateway = ai_gateway

        self.create = async_to_streamed_response_wrapper(
            ai_gateway.create,
        )
        self.update = async_to_streamed_response_wrapper(
            ai_gateway.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ai_gateway.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ai_gateway.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            ai_gateway.get,
        )

    @cached_property
    def evaluation_types(self) -> AsyncEvaluationTypesResourceWithStreamingResponse:
        return AsyncEvaluationTypesResourceWithStreamingResponse(self._ai_gateway.evaluation_types)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._ai_gateway.logs)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self._ai_gateway.datasets)

    @cached_property
    def evaluations(self) -> AsyncEvaluationsResourceWithStreamingResponse:
        return AsyncEvaluationsResourceWithStreamingResponse(self._ai_gateway.evaluations)
