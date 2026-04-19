# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from .assets import (
    AssetsResource,
    AsyncAssetsResource,
    AssetsResourceWithRawResponse,
    AsyncAssetsResourceWithRawResponse,
    AssetsResourceWithStreamingResponse,
    AsyncAssetsResourceWithStreamingResponse,
)
from .public import (
    PublicResource,
    AsyncPublicResource,
    PublicResourceWithRawResponse,
    AsyncPublicResourceWithRawResponse,
    PublicResourceWithStreamingResponse,
    AsyncPublicResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.ai import finetune_create_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.ai.finetune_list_response import FinetuneListResponse
from ....types.ai.finetune_create_response import FinetuneCreateResponse

__all__ = ["FinetunesResource", "AsyncFinetunesResource"]


class FinetunesResource(SyncAPIResource):
    @cached_property
    def assets(self) -> AssetsResource:
        return AssetsResource(self._client)

    @cached_property
    def public(self) -> PublicResource:
        return PublicResource(self._client)

    @cached_property
    def with_raw_response(self) -> FinetunesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FinetunesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FinetunesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FinetunesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str | None = None,
        model: str,
        name: str,
        description: str | Omit = omit,
        public: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinetuneCreateResponse:
        """
        Creates a new fine-tuning job for a Workers AI model using custom training data.

        Args:
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
            path_template("/accounts/{account_id}/ai/finetunes", account_id=account_id),
            body=maybe_transform(
                {
                    "model": model,
                    "name": name,
                    "description": description,
                    "public": public,
                },
                finetune_create_params.FinetuneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FinetuneCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[FinetuneCreateResponse], ResultWrapper[FinetuneCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinetuneListResponse:
        """
        Lists all fine-tuning jobs created by the account, including status and metrics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/ai/finetunes", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FinetuneListResponse]._unwrapper,
            ),
            cast_to=cast(Type[FinetuneListResponse], ResultWrapper[FinetuneListResponse]),
        )


class AsyncFinetunesResource(AsyncAPIResource):
    @cached_property
    def assets(self) -> AsyncAssetsResource:
        return AsyncAssetsResource(self._client)

    @cached_property
    def public(self) -> AsyncPublicResource:
        return AsyncPublicResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFinetunesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFinetunesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFinetunesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFinetunesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str | None = None,
        model: str,
        name: str,
        description: str | Omit = omit,
        public: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinetuneCreateResponse:
        """
        Creates a new fine-tuning job for a Workers AI model using custom training data.

        Args:
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
            path_template("/accounts/{account_id}/ai/finetunes", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "model": model,
                    "name": name,
                    "description": description,
                    "public": public,
                },
                finetune_create_params.FinetuneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FinetuneCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[FinetuneCreateResponse], ResultWrapper[FinetuneCreateResponse]),
        )

    async def list(
        self,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinetuneListResponse:
        """
        Lists all fine-tuning jobs created by the account, including status and metrics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/ai/finetunes", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FinetuneListResponse]._unwrapper,
            ),
            cast_to=cast(Type[FinetuneListResponse], ResultWrapper[FinetuneListResponse]),
        )


class FinetunesResourceWithRawResponse:
    def __init__(self, finetunes: FinetunesResource) -> None:
        self._finetunes = finetunes

        self.create = to_raw_response_wrapper(
            finetunes.create,
        )
        self.list = to_raw_response_wrapper(
            finetunes.list,
        )

    @cached_property
    def assets(self) -> AssetsResourceWithRawResponse:
        return AssetsResourceWithRawResponse(self._finetunes.assets)

    @cached_property
    def public(self) -> PublicResourceWithRawResponse:
        return PublicResourceWithRawResponse(self._finetunes.public)


class AsyncFinetunesResourceWithRawResponse:
    def __init__(self, finetunes: AsyncFinetunesResource) -> None:
        self._finetunes = finetunes

        self.create = async_to_raw_response_wrapper(
            finetunes.create,
        )
        self.list = async_to_raw_response_wrapper(
            finetunes.list,
        )

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithRawResponse:
        return AsyncAssetsResourceWithRawResponse(self._finetunes.assets)

    @cached_property
    def public(self) -> AsyncPublicResourceWithRawResponse:
        return AsyncPublicResourceWithRawResponse(self._finetunes.public)


class FinetunesResourceWithStreamingResponse:
    def __init__(self, finetunes: FinetunesResource) -> None:
        self._finetunes = finetunes

        self.create = to_streamed_response_wrapper(
            finetunes.create,
        )
        self.list = to_streamed_response_wrapper(
            finetunes.list,
        )

    @cached_property
    def assets(self) -> AssetsResourceWithStreamingResponse:
        return AssetsResourceWithStreamingResponse(self._finetunes.assets)

    @cached_property
    def public(self) -> PublicResourceWithStreamingResponse:
        return PublicResourceWithStreamingResponse(self._finetunes.public)


class AsyncFinetunesResourceWithStreamingResponse:
    def __init__(self, finetunes: AsyncFinetunesResource) -> None:
        self._finetunes = finetunes

        self.create = async_to_streamed_response_wrapper(
            finetunes.create,
        )
        self.list = async_to_streamed_response_wrapper(
            finetunes.list,
        )

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithStreamingResponse:
        return AsyncAssetsResourceWithStreamingResponse(self._finetunes.assets)

    @cached_property
    def public(self) -> AsyncPublicResourceWithStreamingResponse:
        return AsyncPublicResourceWithStreamingResponse(self._finetunes.public)
