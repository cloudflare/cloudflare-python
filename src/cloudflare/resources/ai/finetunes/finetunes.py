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
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
        account_id: str,
        model: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        public: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuneCreateResponse:
        """
        Create a new Finetune

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/ai/finetunes",
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
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuneListResponse:
        """
        List Finetunes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/ai/finetunes",
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
        account_id: str,
        model: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        public: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuneCreateResponse:
        """
        Create a new Finetune

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/ai/finetunes",
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
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuneListResponse:
        """
        List Finetunes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai/finetunes",
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
