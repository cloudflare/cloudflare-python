# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.r2.buckets.domains import managed_update_params
from .....types.r2.buckets.domains.managed_list_response import ManagedListResponse
from .....types.r2.buckets.domains.managed_update_response import ManagedUpdateResponse

__all__ = ["ManagedResource", "AsyncManagedResource"]


class ManagedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ManagedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ManagedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManagedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ManagedResourceWithStreamingResponse(self)

    def update(
        self,
        bucket_name: str,
        *,
        account_id: str,
        enabled: bool,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagedUpdateResponse:
        """
        Updates state of public access over the bucket's R2-managed (r2.dev) domain.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          enabled: Whether to enable public bucket access at the r2.dev domain

          jurisdiction: The bucket jurisdiction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {
            **strip_not_given({"cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return self._put(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/managed",
            body=maybe_transform({"enabled": enabled}, managed_update_params.ManagedUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ManagedUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ManagedUpdateResponse], ResultWrapper[ManagedUpdateResponse]),
        )

    def list(
        self,
        bucket_name: str,
        *,
        account_id: str,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagedListResponse:
        """
        Gets state of public access over the bucket's R2-managed (r2.dev) domain.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          jurisdiction: The bucket jurisdiction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {
            **strip_not_given({"cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return self._get(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/managed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ManagedListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ManagedListResponse], ResultWrapper[ManagedListResponse]),
        )


class AsyncManagedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncManagedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncManagedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManagedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncManagedResourceWithStreamingResponse(self)

    async def update(
        self,
        bucket_name: str,
        *,
        account_id: str,
        enabled: bool,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagedUpdateResponse:
        """
        Updates state of public access over the bucket's R2-managed (r2.dev) domain.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          enabled: Whether to enable public bucket access at the r2.dev domain

          jurisdiction: The bucket jurisdiction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {
            **strip_not_given({"cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return await self._put(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/managed",
            body=await async_maybe_transform({"enabled": enabled}, managed_update_params.ManagedUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ManagedUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ManagedUpdateResponse], ResultWrapper[ManagedUpdateResponse]),
        )

    async def list(
        self,
        bucket_name: str,
        *,
        account_id: str,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagedListResponse:
        """
        Gets state of public access over the bucket's R2-managed (r2.dev) domain.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          jurisdiction: The bucket jurisdiction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {
            **strip_not_given({"cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return await self._get(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/managed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ManagedListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ManagedListResponse], ResultWrapper[ManagedListResponse]),
        )


class ManagedResourceWithRawResponse:
    def __init__(self, managed: ManagedResource) -> None:
        self._managed = managed

        self.update = to_raw_response_wrapper(
            managed.update,
        )
        self.list = to_raw_response_wrapper(
            managed.list,
        )


class AsyncManagedResourceWithRawResponse:
    def __init__(self, managed: AsyncManagedResource) -> None:
        self._managed = managed

        self.update = async_to_raw_response_wrapper(
            managed.update,
        )
        self.list = async_to_raw_response_wrapper(
            managed.list,
        )


class ManagedResourceWithStreamingResponse:
    def __init__(self, managed: ManagedResource) -> None:
        self._managed = managed

        self.update = to_streamed_response_wrapper(
            managed.update,
        )
        self.list = to_streamed_response_wrapper(
            managed.list,
        )


class AsyncManagedResourceWithStreamingResponse:
    def __init__(self, managed: AsyncManagedResource) -> None:
        self._managed = managed

        self.update = async_to_streamed_response_wrapper(
            managed.update,
        )
        self.list = async_to_streamed_response_wrapper(
            managed.list,
        )
