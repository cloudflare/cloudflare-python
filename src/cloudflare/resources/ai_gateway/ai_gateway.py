# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast
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
from .urls import (
    URLsResource,
    AsyncURLsResource,
    URLsResourceWithRawResponse,
    AsyncURLsResourceWithRawResponse,
    URLsResourceWithStreamingResponse,
    AsyncURLsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from .dynamic_routing import (
    DynamicRoutingResource,
    AsyncDynamicRoutingResource,
    DynamicRoutingResourceWithRawResponse,
    AsyncDynamicRoutingResourceWithRawResponse,
    DynamicRoutingResourceWithStreamingResponse,
    AsyncDynamicRoutingResourceWithStreamingResponse,
)
from .evaluation_types import (
    EvaluationTypesResource,
    AsyncEvaluationTypesResource,
    EvaluationTypesResourceWithRawResponse,
    AsyncEvaluationTypesResourceWithRawResponse,
    EvaluationTypesResourceWithStreamingResponse,
    AsyncEvaluationTypesResourceWithStreamingResponse,
)
from .provider_configs import (
    ProviderConfigsResource,
    AsyncProviderConfigsResource,
    ProviderConfigsResourceWithRawResponse,
    AsyncProviderConfigsResourceWithRawResponse,
    ProviderConfigsResourceWithStreamingResponse,
    AsyncProviderConfigsResourceWithStreamingResponse,
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
    def dynamic_routing(self) -> DynamicRoutingResource:
        return DynamicRoutingResource(self._client)

    @cached_property
    def provider_configs(self) -> ProviderConfigsResource:
        return ProviderConfigsResource(self._client)

    @cached_property
    def urls(self) -> URLsResource:
        return URLsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AIGatewayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        account_id: str | None = None,
        id: str,
        cache_invalidate_on_update: bool,
        cache_ttl: Optional[int],
        collect_logs: bool,
        rate_limiting_interval: Optional[int],
        rate_limiting_limit: Optional[int],
        authentication: bool | Omit = omit,
        log_management: Optional[int] | Omit = omit,
        log_management_strategy: Optional[Literal["STOP_INSERTING", "DELETE_OLDEST"]] | Omit = omit,
        logpush: bool | Omit = omit,
        logpush_public_key: Optional[str] | Omit = omit,
        rate_limiting_technique: Optional[Literal["fixed", "sliding"]] | Omit = omit,
        retry_backoff: Optional[Literal["constant", "linear", "exponential"]] | Omit = omit,
        retry_delay: Optional[int] | Omit = omit,
        retry_max_attempts: Optional[int] | Omit = omit,
        workers_ai_billing_mode: Literal["postpaid"] | Omit = omit,
        zdr: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIGatewayCreateResponse:
        """
        Creates a new AI Gateway.

        Args:
          id: gateway id

          retry_backoff: Backoff strategy for retry delays

          retry_delay: Delay between retry attempts in milliseconds (0-5000)

          retry_max_attempts: Maximum number of retry attempts for failed requests (1-5)

          workers_ai_billing_mode: Controls how Workers AI inference calls routed through this gateway are billed.
              Only 'postpaid' is currently supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/ai-gateway/gateways", account_id=account_id),
            body=maybe_transform(
                {
                    "id": id,
                    "cache_invalidate_on_update": cache_invalidate_on_update,
                    "cache_ttl": cache_ttl,
                    "collect_logs": collect_logs,
                    "rate_limiting_interval": rate_limiting_interval,
                    "rate_limiting_limit": rate_limiting_limit,
                    "authentication": authentication,
                    "log_management": log_management,
                    "log_management_strategy": log_management_strategy,
                    "logpush": logpush,
                    "logpush_public_key": logpush_public_key,
                    "rate_limiting_technique": rate_limiting_technique,
                    "retry_backoff": retry_backoff,
                    "retry_delay": retry_delay,
                    "retry_max_attempts": retry_max_attempts,
                    "workers_ai_billing_mode": workers_ai_billing_mode,
                    "zdr": zdr,
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
        account_id: str | None = None,
        cache_invalidate_on_update: bool,
        cache_ttl: Optional[int],
        collect_logs: bool,
        rate_limiting_interval: Optional[int],
        rate_limiting_limit: Optional[int],
        authentication: bool | Omit = omit,
        dlp: ai_gateway_update_params.DLP | Omit = omit,
        log_management: Optional[int] | Omit = omit,
        log_management_strategy: Optional[Literal["STOP_INSERTING", "DELETE_OLDEST"]] | Omit = omit,
        logpush: bool | Omit = omit,
        logpush_public_key: Optional[str] | Omit = omit,
        otel: Optional[Iterable[ai_gateway_update_params.Otel]] | Omit = omit,
        rate_limiting_technique: Optional[Literal["fixed", "sliding"]] | Omit = omit,
        retry_backoff: Optional[Literal["constant", "linear", "exponential"]] | Omit = omit,
        retry_delay: Optional[int] | Omit = omit,
        retry_max_attempts: Optional[int] | Omit = omit,
        store_id: Optional[str] | Omit = omit,
        stripe: Optional[ai_gateway_update_params.Stripe] | Omit = omit,
        workers_ai_billing_mode: Literal["postpaid"] | Omit = omit,
        zdr: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIGatewayUpdateResponse:
        """
        Updates an existing AI Gateway dataset.

        Args:
          id: gateway id

          retry_backoff: Backoff strategy for retry delays

          retry_delay: Delay between retry attempts in milliseconds (0-5000)

          retry_max_attempts: Maximum number of retry attempts for failed requests (1-5)

          workers_ai_billing_mode: Controls how Workers AI inference calls routed through this gateway are billed.
              Only 'postpaid' is currently supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/accounts/{account_id}/ai-gateway/gateways/{id}", account_id=account_id, id=id),
            body=maybe_transform(
                {
                    "cache_invalidate_on_update": cache_invalidate_on_update,
                    "cache_ttl": cache_ttl,
                    "collect_logs": collect_logs,
                    "rate_limiting_interval": rate_limiting_interval,
                    "rate_limiting_limit": rate_limiting_limit,
                    "authentication": authentication,
                    "dlp": dlp,
                    "log_management": log_management,
                    "log_management_strategy": log_management_strategy,
                    "logpush": logpush,
                    "logpush_public_key": logpush_public_key,
                    "otel": otel,
                    "rate_limiting_technique": rate_limiting_technique,
                    "retry_backoff": retry_backoff,
                    "retry_delay": retry_delay,
                    "retry_max_attempts": retry_max_attempts,
                    "store_id": store_id,
                    "stripe": stripe,
                    "workers_ai_billing_mode": workers_ai_billing_mode,
                    "zdr": zdr,
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
        account_id: str | None = None,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[AIGatewayListResponse]:
        """
        Lists all AI Gateway evaluator types configured for the account.

        Args:
          search: Search by id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/ai-gateway/gateways", account_id=account_id),
            page=SyncV4PagePaginationArray[AIGatewayListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search": search,
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
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIGatewayDeleteResponse:
        """
        Deletes an AI Gateway dataset.

        Args:
          id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/accounts/{account_id}/ai-gateway/gateways/{id}", account_id=account_id, id=id),
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
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIGatewayGetResponse:
        """
        Retrieves details for a specific AI Gateway dataset.

        Args:
          id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/accounts/{account_id}/ai-gateway/gateways/{id}", account_id=account_id, id=id),
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
    def dynamic_routing(self) -> AsyncDynamicRoutingResource:
        return AsyncDynamicRoutingResource(self._client)

    @cached_property
    def provider_configs(self) -> AsyncProviderConfigsResource:
        return AsyncProviderConfigsResource(self._client)

    @cached_property
    def urls(self) -> AsyncURLsResource:
        return AsyncURLsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAIGatewayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        account_id: str | None = None,
        id: str,
        cache_invalidate_on_update: bool,
        cache_ttl: Optional[int],
        collect_logs: bool,
        rate_limiting_interval: Optional[int],
        rate_limiting_limit: Optional[int],
        authentication: bool | Omit = omit,
        log_management: Optional[int] | Omit = omit,
        log_management_strategy: Optional[Literal["STOP_INSERTING", "DELETE_OLDEST"]] | Omit = omit,
        logpush: bool | Omit = omit,
        logpush_public_key: Optional[str] | Omit = omit,
        rate_limiting_technique: Optional[Literal["fixed", "sliding"]] | Omit = omit,
        retry_backoff: Optional[Literal["constant", "linear", "exponential"]] | Omit = omit,
        retry_delay: Optional[int] | Omit = omit,
        retry_max_attempts: Optional[int] | Omit = omit,
        workers_ai_billing_mode: Literal["postpaid"] | Omit = omit,
        zdr: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIGatewayCreateResponse:
        """
        Creates a new AI Gateway.

        Args:
          id: gateway id

          retry_backoff: Backoff strategy for retry delays

          retry_delay: Delay between retry attempts in milliseconds (0-5000)

          retry_max_attempts: Maximum number of retry attempts for failed requests (1-5)

          workers_ai_billing_mode: Controls how Workers AI inference calls routed through this gateway are billed.
              Only 'postpaid' is currently supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/ai-gateway/gateways", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "cache_invalidate_on_update": cache_invalidate_on_update,
                    "cache_ttl": cache_ttl,
                    "collect_logs": collect_logs,
                    "rate_limiting_interval": rate_limiting_interval,
                    "rate_limiting_limit": rate_limiting_limit,
                    "authentication": authentication,
                    "log_management": log_management,
                    "log_management_strategy": log_management_strategy,
                    "logpush": logpush,
                    "logpush_public_key": logpush_public_key,
                    "rate_limiting_technique": rate_limiting_technique,
                    "retry_backoff": retry_backoff,
                    "retry_delay": retry_delay,
                    "retry_max_attempts": retry_max_attempts,
                    "workers_ai_billing_mode": workers_ai_billing_mode,
                    "zdr": zdr,
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
        account_id: str | None = None,
        cache_invalidate_on_update: bool,
        cache_ttl: Optional[int],
        collect_logs: bool,
        rate_limiting_interval: Optional[int],
        rate_limiting_limit: Optional[int],
        authentication: bool | Omit = omit,
        dlp: ai_gateway_update_params.DLP | Omit = omit,
        log_management: Optional[int] | Omit = omit,
        log_management_strategy: Optional[Literal["STOP_INSERTING", "DELETE_OLDEST"]] | Omit = omit,
        logpush: bool | Omit = omit,
        logpush_public_key: Optional[str] | Omit = omit,
        otel: Optional[Iterable[ai_gateway_update_params.Otel]] | Omit = omit,
        rate_limiting_technique: Optional[Literal["fixed", "sliding"]] | Omit = omit,
        retry_backoff: Optional[Literal["constant", "linear", "exponential"]] | Omit = omit,
        retry_delay: Optional[int] | Omit = omit,
        retry_max_attempts: Optional[int] | Omit = omit,
        store_id: Optional[str] | Omit = omit,
        stripe: Optional[ai_gateway_update_params.Stripe] | Omit = omit,
        workers_ai_billing_mode: Literal["postpaid"] | Omit = omit,
        zdr: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIGatewayUpdateResponse:
        """
        Updates an existing AI Gateway dataset.

        Args:
          id: gateway id

          retry_backoff: Backoff strategy for retry delays

          retry_delay: Delay between retry attempts in milliseconds (0-5000)

          retry_max_attempts: Maximum number of retry attempts for failed requests (1-5)

          workers_ai_billing_mode: Controls how Workers AI inference calls routed through this gateway are billed.
              Only 'postpaid' is currently supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/accounts/{account_id}/ai-gateway/gateways/{id}", account_id=account_id, id=id),
            body=await async_maybe_transform(
                {
                    "cache_invalidate_on_update": cache_invalidate_on_update,
                    "cache_ttl": cache_ttl,
                    "collect_logs": collect_logs,
                    "rate_limiting_interval": rate_limiting_interval,
                    "rate_limiting_limit": rate_limiting_limit,
                    "authentication": authentication,
                    "dlp": dlp,
                    "log_management": log_management,
                    "log_management_strategy": log_management_strategy,
                    "logpush": logpush,
                    "logpush_public_key": logpush_public_key,
                    "otel": otel,
                    "rate_limiting_technique": rate_limiting_technique,
                    "retry_backoff": retry_backoff,
                    "retry_delay": retry_delay,
                    "retry_max_attempts": retry_max_attempts,
                    "store_id": store_id,
                    "stripe": stripe,
                    "workers_ai_billing_mode": workers_ai_billing_mode,
                    "zdr": zdr,
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
        account_id: str | None = None,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AIGatewayListResponse, AsyncV4PagePaginationArray[AIGatewayListResponse]]:
        """
        Lists all AI Gateway evaluator types configured for the account.

        Args:
          search: Search by id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/ai-gateway/gateways", account_id=account_id),
            page=AsyncV4PagePaginationArray[AIGatewayListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search": search,
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
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIGatewayDeleteResponse:
        """
        Deletes an AI Gateway dataset.

        Args:
          id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/accounts/{account_id}/ai-gateway/gateways/{id}", account_id=account_id, id=id),
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
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIGatewayGetResponse:
        """
        Retrieves details for a specific AI Gateway dataset.

        Args:
          id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/ai-gateway/gateways/{id}", account_id=account_id, id=id),
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

    @cached_property
    def dynamic_routing(self) -> DynamicRoutingResourceWithRawResponse:
        return DynamicRoutingResourceWithRawResponse(self._ai_gateway.dynamic_routing)

    @cached_property
    def provider_configs(self) -> ProviderConfigsResourceWithRawResponse:
        return ProviderConfigsResourceWithRawResponse(self._ai_gateway.provider_configs)

    @cached_property
    def urls(self) -> URLsResourceWithRawResponse:
        return URLsResourceWithRawResponse(self._ai_gateway.urls)


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

    @cached_property
    def dynamic_routing(self) -> AsyncDynamicRoutingResourceWithRawResponse:
        return AsyncDynamicRoutingResourceWithRawResponse(self._ai_gateway.dynamic_routing)

    @cached_property
    def provider_configs(self) -> AsyncProviderConfigsResourceWithRawResponse:
        return AsyncProviderConfigsResourceWithRawResponse(self._ai_gateway.provider_configs)

    @cached_property
    def urls(self) -> AsyncURLsResourceWithRawResponse:
        return AsyncURLsResourceWithRawResponse(self._ai_gateway.urls)


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

    @cached_property
    def dynamic_routing(self) -> DynamicRoutingResourceWithStreamingResponse:
        return DynamicRoutingResourceWithStreamingResponse(self._ai_gateway.dynamic_routing)

    @cached_property
    def provider_configs(self) -> ProviderConfigsResourceWithStreamingResponse:
        return ProviderConfigsResourceWithStreamingResponse(self._ai_gateway.provider_configs)

    @cached_property
    def urls(self) -> URLsResourceWithStreamingResponse:
        return URLsResourceWithStreamingResponse(self._ai_gateway.urls)


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

    @cached_property
    def dynamic_routing(self) -> AsyncDynamicRoutingResourceWithStreamingResponse:
        return AsyncDynamicRoutingResourceWithStreamingResponse(self._ai_gateway.dynamic_routing)

    @cached_property
    def provider_configs(self) -> AsyncProviderConfigsResourceWithStreamingResponse:
        return AsyncProviderConfigsResourceWithStreamingResponse(self._ai_gateway.provider_configs)

    @cached_property
    def urls(self) -> AsyncURLsResourceWithStreamingResponse:
        return AsyncURLsResourceWithStreamingResponse(self._ai_gateway.urls)
