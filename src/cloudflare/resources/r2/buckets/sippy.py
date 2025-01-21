# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal, overload

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    is_given,
    required_args,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.r2.buckets import sippy_update_params
from ....types.r2.buckets.sippy import Sippy
from ....types.r2.buckets.sippy_delete_response import SippyDeleteResponse

__all__ = ["SippyResource", "AsyncSippyResource"]


class SippyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SippyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SippyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SippyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SippyResourceWithStreamingResponse(self)

    @overload
    def update(
        self,
        bucket_name: str,
        *,
        account_id: str,
        destination: sippy_update_params.R2EnableSippyAwsDestination | NotGiven = NOT_GIVEN,
        source: sippy_update_params.R2EnableSippyAwsSource | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sippy:
        """
        Sets configuration for Sippy for an existing R2 bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          destination: R2 bucket to copy objects to

          source: AWS S3 bucket to copy objects from

          jurisdiction: The bucket jurisdiction

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
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sippy:
        """
        Sets configuration for Sippy for an existing R2 bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          destination: R2 bucket to copy objects to

          source: GCS bucket to copy objects from

          jurisdiction: The bucket jurisdiction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"])
    def update(
        self,
        bucket_name: str,
        *,
        account_id: str,
        destination: sippy_update_params.R2EnableSippyAwsDestination | NotGiven = NOT_GIVEN,
        source: sippy_update_params.R2EnableSippyAwsSource
        | sippy_update_params.R2EnableSippyGcsSource
        | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sippy:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {
            **strip_not_given({"cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
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
                post_parser=ResultWrapper[Sippy]._unwrapper,
            ),
            cast_to=cast(Type[Sippy], ResultWrapper[Sippy]),
        )

    def delete(
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
    ) -> SippyDeleteResponse:
        """
        Disables Sippy on this bucket

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
        return self._delete(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/sippy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SippyDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[SippyDeleteResponse], ResultWrapper[SippyDeleteResponse]),
        )

    def get(
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
    ) -> Sippy:
        """
        Gets configuration for Sippy for an existing R2 bucket.

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
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/sippy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Sippy]._unwrapper,
            ),
            cast_to=cast(Type[Sippy], ResultWrapper[Sippy]),
        )


class AsyncSippyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSippyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSippyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSippyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSippyResourceWithStreamingResponse(self)

    @overload
    async def update(
        self,
        bucket_name: str,
        *,
        account_id: str,
        destination: sippy_update_params.R2EnableSippyAwsDestination | NotGiven = NOT_GIVEN,
        source: sippy_update_params.R2EnableSippyAwsSource | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sippy:
        """
        Sets configuration for Sippy for an existing R2 bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          destination: R2 bucket to copy objects to

          source: AWS S3 bucket to copy objects from

          jurisdiction: The bucket jurisdiction

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
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sippy:
        """
        Sets configuration for Sippy for an existing R2 bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          destination: R2 bucket to copy objects to

          source: GCS bucket to copy objects from

          jurisdiction: The bucket jurisdiction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"])
    async def update(
        self,
        bucket_name: str,
        *,
        account_id: str,
        destination: sippy_update_params.R2EnableSippyAwsDestination | NotGiven = NOT_GIVEN,
        source: sippy_update_params.R2EnableSippyAwsSource
        | sippy_update_params.R2EnableSippyGcsSource
        | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sippy:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {
            **strip_not_given({"cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
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
                post_parser=ResultWrapper[Sippy]._unwrapper,
            ),
            cast_to=cast(Type[Sippy], ResultWrapper[Sippy]),
        )

    async def delete(
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
    ) -> SippyDeleteResponse:
        """
        Disables Sippy on this bucket

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
        return await self._delete(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/sippy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SippyDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[SippyDeleteResponse], ResultWrapper[SippyDeleteResponse]),
        )

    async def get(
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
    ) -> Sippy:
        """
        Gets configuration for Sippy for an existing R2 bucket.

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
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/sippy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Sippy]._unwrapper,
            ),
            cast_to=cast(Type[Sippy], ResultWrapper[Sippy]),
        )


class SippyResourceWithRawResponse:
    def __init__(self, sippy: SippyResource) -> None:
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


class AsyncSippyResourceWithRawResponse:
    def __init__(self, sippy: AsyncSippyResource) -> None:
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


class SippyResourceWithStreamingResponse:
    def __init__(self, sippy: SippyResource) -> None:
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


class AsyncSippyResourceWithStreamingResponse:
    def __init__(self, sippy: AsyncSippyResource) -> None:
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
