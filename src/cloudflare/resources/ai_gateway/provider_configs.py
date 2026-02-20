# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
from ...types.ai_gateway import provider_config_list_params, provider_config_create_params
from ...types.ai_gateway.provider_config_list_response import ProviderConfigListResponse
from ...types.ai_gateway.provider_config_create_response import ProviderConfigCreateResponse

__all__ = ["ProviderConfigsResource", "AsyncProviderConfigsResource"]


class ProviderConfigsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProviderConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ProviderConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProviderConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ProviderConfigsResourceWithStreamingResponse(self)

    def create(
        self,
        gateway_id: str,
        *,
        account_id: str,
        alias: str,
        default_config: bool,
        provider_slug: str,
        secret: str,
        secret_id: str,
        rate_limit: float | Omit = omit,
        rate_limit_period: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderConfigCreateResponse:
        """
        Create a new Provider Configs

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
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/provider_configs",
            body=maybe_transform(
                {
                    "alias": alias,
                    "default_config": default_config,
                    "provider_slug": provider_slug,
                    "secret": secret,
                    "secret_id": secret_id,
                    "rate_limit": rate_limit,
                    "rate_limit_period": rate_limit_period,
                },
                provider_config_create_params.ProviderConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ProviderConfigCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ProviderConfigCreateResponse], ResultWrapper[ProviderConfigCreateResponse]),
        )

    def list(
        self,
        gateway_id: str,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[ProviderConfigListResponse]:
        """
        List Provider Configs

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
        return self._get_api_list(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/provider_configs",
            page=SyncV4PagePaginationArray[ProviderConfigListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    provider_config_list_params.ProviderConfigListParams,
                ),
            ),
            model=ProviderConfigListResponse,
        )


class AsyncProviderConfigsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProviderConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProviderConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProviderConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncProviderConfigsResourceWithStreamingResponse(self)

    async def create(
        self,
        gateway_id: str,
        *,
        account_id: str,
        alias: str,
        default_config: bool,
        provider_slug: str,
        secret: str,
        secret_id: str,
        rate_limit: float | Omit = omit,
        rate_limit_period: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderConfigCreateResponse:
        """
        Create a new Provider Configs

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
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/provider_configs",
            body=await async_maybe_transform(
                {
                    "alias": alias,
                    "default_config": default_config,
                    "provider_slug": provider_slug,
                    "secret": secret,
                    "secret_id": secret_id,
                    "rate_limit": rate_limit,
                    "rate_limit_period": rate_limit_period,
                },
                provider_config_create_params.ProviderConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ProviderConfigCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ProviderConfigCreateResponse], ResultWrapper[ProviderConfigCreateResponse]),
        )

    def list(
        self,
        gateway_id: str,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ProviderConfigListResponse, AsyncV4PagePaginationArray[ProviderConfigListResponse]]:
        """
        List Provider Configs

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
        return self._get_api_list(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/provider_configs",
            page=AsyncV4PagePaginationArray[ProviderConfigListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    provider_config_list_params.ProviderConfigListParams,
                ),
            ),
            model=ProviderConfigListResponse,
        )


class ProviderConfigsResourceWithRawResponse:
    def __init__(self, provider_configs: ProviderConfigsResource) -> None:
        self._provider_configs = provider_configs

        self.create = to_raw_response_wrapper(
            provider_configs.create,
        )
        self.list = to_raw_response_wrapper(
            provider_configs.list,
        )


class AsyncProviderConfigsResourceWithRawResponse:
    def __init__(self, provider_configs: AsyncProviderConfigsResource) -> None:
        self._provider_configs = provider_configs

        self.create = async_to_raw_response_wrapper(
            provider_configs.create,
        )
        self.list = async_to_raw_response_wrapper(
            provider_configs.list,
        )


class ProviderConfigsResourceWithStreamingResponse:
    def __init__(self, provider_configs: ProviderConfigsResource) -> None:
        self._provider_configs = provider_configs

        self.create = to_streamed_response_wrapper(
            provider_configs.create,
        )
        self.list = to_streamed_response_wrapper(
            provider_configs.list,
        )


class AsyncProviderConfigsResourceWithStreamingResponse:
    def __init__(self, provider_configs: AsyncProviderConfigsResource) -> None:
        self._provider_configs = provider_configs

        self.create = async_to_streamed_response_wrapper(
            provider_configs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            provider_configs.list,
        )
