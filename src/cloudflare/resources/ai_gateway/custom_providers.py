# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.ai_gateway import custom_provider_list_params, custom_provider_create_params
from ...types.ai_gateway.custom_provider_get_response import CustomProviderGetResponse
from ...types.ai_gateway.custom_provider_list_response import CustomProviderListResponse
from ...types.ai_gateway.custom_provider_create_response import CustomProviderCreateResponse
from ...types.ai_gateway.custom_provider_delete_response import CustomProviderDeleteResponse

__all__ = ["CustomProvidersResource", "AsyncCustomProvidersResource"]


class CustomProvidersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CustomProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CustomProvidersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        base_url: str,
        name: str,
        slug: str,
        beta: bool | Omit = omit,
        curl_example: str | Omit = omit,
        description: str | Omit = omit,
        enable: bool | Omit = omit,
        headers: str | Omit = omit,
        js_example: str | Omit = omit,
        link: str | Omit = omit,
        position: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomProviderCreateResponse:
        """
        Creates a new AI Gateway.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/ai-gateway/custom-providers", account_id=account_id),
            body=maybe_transform(
                {
                    "base_url": base_url,
                    "name": name,
                    "slug": slug,
                    "beta": beta,
                    "curl_example": curl_example,
                    "description": description,
                    "enable": enable,
                    "headers": headers,
                    "js_example": js_example,
                    "link": link,
                    "position": position,
                },
                custom_provider_create_params.CustomProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomProviderCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomProviderCreateResponse], ResultWrapper[CustomProviderCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        beta: bool | Omit = omit,
        enable: bool | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[CustomProviderListResponse]:
        """
        Lists all AI Gateway evaluator types configured for the account.

        Args:
          search: Search by id, name, slug

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/ai-gateway/custom-providers", account_id=account_id),
            page=SyncV4PagePaginationArray[CustomProviderListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "beta": beta,
                        "enable": enable,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    custom_provider_list_params.CustomProviderListParams,
                ),
            ),
            model=CustomProviderListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomProviderDeleteResponse:
        """
        Deletes an AI Gateway dataset.

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
            path_template("/accounts/{account_id}/ai-gateway/custom-providers/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomProviderDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomProviderDeleteResponse], ResultWrapper[CustomProviderDeleteResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomProviderGetResponse:
        """
        Retrieves details for a specific AI Gateway dataset.

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
        return self._get(
            path_template("/accounts/{account_id}/ai-gateway/custom-providers/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomProviderGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomProviderGetResponse], ResultWrapper[CustomProviderGetResponse]),
        )


class AsyncCustomProvidersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCustomProvidersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        base_url: str,
        name: str,
        slug: str,
        beta: bool | Omit = omit,
        curl_example: str | Omit = omit,
        description: str | Omit = omit,
        enable: bool | Omit = omit,
        headers: str | Omit = omit,
        js_example: str | Omit = omit,
        link: str | Omit = omit,
        position: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomProviderCreateResponse:
        """
        Creates a new AI Gateway.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/ai-gateway/custom-providers", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "base_url": base_url,
                    "name": name,
                    "slug": slug,
                    "beta": beta,
                    "curl_example": curl_example,
                    "description": description,
                    "enable": enable,
                    "headers": headers,
                    "js_example": js_example,
                    "link": link,
                    "position": position,
                },
                custom_provider_create_params.CustomProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomProviderCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomProviderCreateResponse], ResultWrapper[CustomProviderCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        beta: bool | Omit = omit,
        enable: bool | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CustomProviderListResponse, AsyncV4PagePaginationArray[CustomProviderListResponse]]:
        """
        Lists all AI Gateway evaluator types configured for the account.

        Args:
          search: Search by id, name, slug

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/ai-gateway/custom-providers", account_id=account_id),
            page=AsyncV4PagePaginationArray[CustomProviderListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "beta": beta,
                        "enable": enable,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    custom_provider_list_params.CustomProviderListParams,
                ),
            ),
            model=CustomProviderListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomProviderDeleteResponse:
        """
        Deletes an AI Gateway dataset.

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
            path_template("/accounts/{account_id}/ai-gateway/custom-providers/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomProviderDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomProviderDeleteResponse], ResultWrapper[CustomProviderDeleteResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomProviderGetResponse:
        """
        Retrieves details for a specific AI Gateway dataset.

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
        return await self._get(
            path_template("/accounts/{account_id}/ai-gateway/custom-providers/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomProviderGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomProviderGetResponse], ResultWrapper[CustomProviderGetResponse]),
        )


class CustomProvidersResourceWithRawResponse:
    def __init__(self, custom_providers: CustomProvidersResource) -> None:
        self._custom_providers = custom_providers

        self.create = to_raw_response_wrapper(
            custom_providers.create,
        )
        self.list = to_raw_response_wrapper(
            custom_providers.list,
        )
        self.delete = to_raw_response_wrapper(
            custom_providers.delete,
        )
        self.get = to_raw_response_wrapper(
            custom_providers.get,
        )


class AsyncCustomProvidersResourceWithRawResponse:
    def __init__(self, custom_providers: AsyncCustomProvidersResource) -> None:
        self._custom_providers = custom_providers

        self.create = async_to_raw_response_wrapper(
            custom_providers.create,
        )
        self.list = async_to_raw_response_wrapper(
            custom_providers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_providers.delete,
        )
        self.get = async_to_raw_response_wrapper(
            custom_providers.get,
        )


class CustomProvidersResourceWithStreamingResponse:
    def __init__(self, custom_providers: CustomProvidersResource) -> None:
        self._custom_providers = custom_providers

        self.create = to_streamed_response_wrapper(
            custom_providers.create,
        )
        self.list = to_streamed_response_wrapper(
            custom_providers.list,
        )
        self.delete = to_streamed_response_wrapper(
            custom_providers.delete,
        )
        self.get = to_streamed_response_wrapper(
            custom_providers.get,
        )


class AsyncCustomProvidersResourceWithStreamingResponse:
    def __init__(self, custom_providers: AsyncCustomProvidersResource) -> None:
        self._custom_providers = custom_providers

        self.create = async_to_streamed_response_wrapper(
            custom_providers.create,
        )
        self.list = async_to_streamed_response_wrapper(
            custom_providers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_providers.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            custom_providers.get,
        )
