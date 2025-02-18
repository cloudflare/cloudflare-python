# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    is_given,
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
from ....types.r2.buckets import cors_update_params
from ....types.r2.buckets.cors_get_response import CORSGetResponse

__all__ = ["CORSResource", "AsyncCORSResource"]


class CORSResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CORSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CORSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CORSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CORSResourceWithStreamingResponse(self)

    def update(
        self,
        bucket_name: str,
        *,
        account_id: str,
        rules: Iterable[cors_update_params.Rule] | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Set the CORS policy for a bucket

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
        return self._put(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/cors",
            body=maybe_transform({"rules": rules}, cors_update_params.CORSUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
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
    ) -> object:
        """
        Delete the CORS policy for a bucket

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
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/cors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
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
    ) -> CORSGetResponse:
        """
        Get the CORS policy for a bucket

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
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/cors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CORSGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CORSGetResponse], ResultWrapper[CORSGetResponse]),
        )


class AsyncCORSResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCORSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCORSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCORSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCORSResourceWithStreamingResponse(self)

    async def update(
        self,
        bucket_name: str,
        *,
        account_id: str,
        rules: Iterable[cors_update_params.Rule] | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Set the CORS policy for a bucket

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
        return await self._put(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/cors",
            body=await async_maybe_transform({"rules": rules}, cors_update_params.CORSUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
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
    ) -> object:
        """
        Delete the CORS policy for a bucket

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
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/cors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
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
    ) -> CORSGetResponse:
        """
        Get the CORS policy for a bucket

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
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/cors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CORSGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CORSGetResponse], ResultWrapper[CORSGetResponse]),
        )


class CORSResourceWithRawResponse:
    def __init__(self, cors: CORSResource) -> None:
        self._cors = cors

        self.update = to_raw_response_wrapper(
            cors.update,
        )
        self.delete = to_raw_response_wrapper(
            cors.delete,
        )
        self.get = to_raw_response_wrapper(
            cors.get,
        )


class AsyncCORSResourceWithRawResponse:
    def __init__(self, cors: AsyncCORSResource) -> None:
        self._cors = cors

        self.update = async_to_raw_response_wrapper(
            cors.update,
        )
        self.delete = async_to_raw_response_wrapper(
            cors.delete,
        )
        self.get = async_to_raw_response_wrapper(
            cors.get,
        )


class CORSResourceWithStreamingResponse:
    def __init__(self, cors: CORSResource) -> None:
        self._cors = cors

        self.update = to_streamed_response_wrapper(
            cors.update,
        )
        self.delete = to_streamed_response_wrapper(
            cors.delete,
        )
        self.get = to_streamed_response_wrapper(
            cors.get,
        )


class AsyncCORSResourceWithStreamingResponse:
    def __init__(self, cors: AsyncCORSResource) -> None:
        self._cors = cors

        self.update = async_to_streamed_response_wrapper(
            cors.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            cors.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            cors.get,
        )
