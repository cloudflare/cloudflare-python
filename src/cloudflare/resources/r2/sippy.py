# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ...types.r2 import R2Sippy, SippyDeleteResponse, sippy_update_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)

__all__ = ["Sippy", "AsyncSippy"]


class Sippy(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SippyWithRawResponse:
        return SippyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SippyWithStreamingResponse:
        return SippyWithStreamingResponse(self)

    @overload
    def update(
        self,
        bucket_name: str,
        *,
        account_id: str,
        destination: sippy_update_params.R2EnableSippyAwsDestination | NotGiven = NOT_GIVEN,
        source: sippy_update_params.R2EnableSippyAwsSource | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> R2Sippy:
        """
        Sets configuration for Sippy for an existing R2 bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          destination: R2 bucket to copy objects to

          source: AWS S3 bucket to copy objects from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        bucket_name: str,
        *,
        account_id: str,
        destination: sippy_update_params.R2EnableSippyGcsDestination | NotGiven = NOT_GIVEN,
        source: sippy_update_params.R2EnableSippyGcsSource | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> R2Sippy:
        """
        Sets configuration for Sippy for an existing R2 bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          destination: R2 bucket to copy objects to

          source: GCS bucket to copy objects from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"], ["account_id"])
    def update(
        self,
        bucket_name: str,
        *,
        account_id: str,
        destination: sippy_update_params.R2EnableSippyAwsDestination | NotGiven = NOT_GIVEN,
        source: sippy_update_params.R2EnableSippyAwsSource
        | sippy_update_params.R2EnableSippyGcsSource
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> R2Sippy:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return self._put(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/sippy",
            body=maybe_transform(
                {
                    "destination": destination,
                    "source": source,
                },
                sippy_update_params.SippyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[R2Sippy], ResultWrapper[R2Sippy]),
        )

    def delete(
        self,
        bucket_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SippyDeleteResponse:
        """
        Disables Sippy on this bucket

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return self._delete(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/sippy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SippyDeleteResponse], ResultWrapper[SippyDeleteResponse]),
        )

    def get(
        self,
        bucket_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> R2Sippy:
        """
        Gets configuration for Sippy for an existing R2 bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return self._get(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/sippy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[R2Sippy], ResultWrapper[R2Sippy]),
        )


class AsyncSippy(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSippyWithRawResponse:
        return AsyncSippyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSippyWithStreamingResponse:
        return AsyncSippyWithStreamingResponse(self)

    @overload
    async def update(
        self,
        bucket_name: str,
        *,
        account_id: str,
        destination: sippy_update_params.R2EnableSippyAwsDestination | NotGiven = NOT_GIVEN,
        source: sippy_update_params.R2EnableSippyAwsSource | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> R2Sippy:
        """
        Sets configuration for Sippy for an existing R2 bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          destination: R2 bucket to copy objects to

          source: AWS S3 bucket to copy objects from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        bucket_name: str,
        *,
        account_id: str,
        destination: sippy_update_params.R2EnableSippyGcsDestination | NotGiven = NOT_GIVEN,
        source: sippy_update_params.R2EnableSippyGcsSource | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> R2Sippy:
        """
        Sets configuration for Sippy for an existing R2 bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          destination: R2 bucket to copy objects to

          source: GCS bucket to copy objects from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"], ["account_id"])
    async def update(
        self,
        bucket_name: str,
        *,
        account_id: str,
        destination: sippy_update_params.R2EnableSippyAwsDestination | NotGiven = NOT_GIVEN,
        source: sippy_update_params.R2EnableSippyAwsSource
        | sippy_update_params.R2EnableSippyGcsSource
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> R2Sippy:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return await self._put(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/sippy",
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "source": source,
                },
                sippy_update_params.SippyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[R2Sippy], ResultWrapper[R2Sippy]),
        )

    async def delete(
        self,
        bucket_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SippyDeleteResponse:
        """
        Disables Sippy on this bucket

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return await self._delete(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/sippy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SippyDeleteResponse], ResultWrapper[SippyDeleteResponse]),
        )

    async def get(
        self,
        bucket_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> R2Sippy:
        """
        Gets configuration for Sippy for an existing R2 bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return await self._get(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/sippy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[R2Sippy], ResultWrapper[R2Sippy]),
        )


class SippyWithRawResponse:
    def __init__(self, sippy: Sippy) -> None:
        self._sippy = sippy

        self.update = to_raw_response_wrapper(
            sippy.update,
        )
        self.delete = to_raw_response_wrapper(
            sippy.delete,
        )
        self.get = to_raw_response_wrapper(
            sippy.get,
        )


class AsyncSippyWithRawResponse:
    def __init__(self, sippy: AsyncSippy) -> None:
        self._sippy = sippy

        self.update = async_to_raw_response_wrapper(
            sippy.update,
        )
        self.delete = async_to_raw_response_wrapper(
            sippy.delete,
        )
        self.get = async_to_raw_response_wrapper(
            sippy.get,
        )


class SippyWithStreamingResponse:
    def __init__(self, sippy: Sippy) -> None:
        self._sippy = sippy

        self.update = to_streamed_response_wrapper(
            sippy.update,
        )
        self.delete = to_streamed_response_wrapper(
            sippy.delete,
        )
        self.get = to_streamed_response_wrapper(
            sippy.get,
        )


class AsyncSippyWithStreamingResponse:
    def __init__(self, sippy: AsyncSippy) -> None:
        self._sippy = sippy

        self.update = async_to_streamed_response_wrapper(
            sippy.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            sippy.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            sippy.get,
        )
