# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import required_args, maybe_transform, async_maybe_transform
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
from ....types.r2.buckets import Provider
from ....types.r2.super_slurper import connectivity_precheck_source_params, connectivity_precheck_target_params
from ....types.r2.buckets.provider import Provider
from ....types.r2.super_slurper.connectivity_precheck_source_response import ConnectivityPrecheckSourceResponse
from ....types.r2.super_slurper.connectivity_precheck_target_response import ConnectivityPrecheckTargetResponse

__all__ = ["ConnectivityPrecheckResource", "AsyncConnectivityPrecheckResource"]


class ConnectivityPrecheckResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectivityPrecheckResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ConnectivityPrecheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectivityPrecheckResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ConnectivityPrecheckResourceWithStreamingResponse(self)

    @overload
    def source(
        self,
        *,
        account_id: str,
        bucket: str | NotGiven = NOT_GIVEN,
        endpoint: Optional[str] | NotGiven = NOT_GIVEN,
        secret: connectivity_precheck_source_params.R2SlurperS3SourceSchemaSecret | NotGiven = NOT_GIVEN,
        vendor: Literal["s3"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConnectivityPrecheckSourceResponse]:
        """
        Check whether tokens are valid against the source bucket

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def source(
        self,
        *,
        account_id: str,
        bucket: str | NotGiven = NOT_GIVEN,
        secret: connectivity_precheck_source_params.R2SlurperGcsSourceSchemaSecret | NotGiven = NOT_GIVEN,
        vendor: Literal["gcs"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConnectivityPrecheckSourceResponse]:
        """
        Check whether tokens are valid against the source bucket

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def source(
        self,
        *,
        account_id: str,
        bucket: str | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        secret: connectivity_precheck_source_params.R2SlurperR2SourceSchemaSecret | NotGiven = NOT_GIVEN,
        vendor: Provider | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConnectivityPrecheckSourceResponse]:
        """
        Check whether tokens are valid against the source bucket

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"])
    def source(
        self,
        *,
        account_id: str,
        bucket: str | NotGiven = NOT_GIVEN,
        endpoint: Optional[str] | NotGiven = NOT_GIVEN,
        secret: connectivity_precheck_source_params.R2SlurperS3SourceSchemaSecret
        | connectivity_precheck_source_params.R2SlurperGcsSourceSchemaSecret
        | NotGiven = NOT_GIVEN,
        vendor: Literal["s3"] | Literal["gcs"] | Provider | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConnectivityPrecheckSourceResponse]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/slurper/source/connectivity-precheck",
            body=maybe_transform(
                {
                    "bucket": bucket,
                    "endpoint": endpoint,
                    "secret": secret,
                    "vendor": vendor,
                    "jurisdiction": jurisdiction,
                },
                connectivity_precheck_source_params.ConnectivityPrecheckSourceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ConnectivityPrecheckSourceResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ConnectivityPrecheckSourceResponse]], ResultWrapper[ConnectivityPrecheckSourceResponse]
            ),
        )

    def target(
        self,
        *,
        account_id: str,
        bucket: str | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        secret: connectivity_precheck_target_params.Secret | NotGiven = NOT_GIVEN,
        vendor: Provider | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConnectivityPrecheckTargetResponse]:
        """
        Check whether tokens are valid against the target bucket

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/slurper/target/connectivity-precheck",
            body=maybe_transform(
                {
                    "bucket": bucket,
                    "jurisdiction": jurisdiction,
                    "secret": secret,
                    "vendor": vendor,
                },
                connectivity_precheck_target_params.ConnectivityPrecheckTargetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ConnectivityPrecheckTargetResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ConnectivityPrecheckTargetResponse]], ResultWrapper[ConnectivityPrecheckTargetResponse]
            ),
        )


class AsyncConnectivityPrecheckResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectivityPrecheckResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectivityPrecheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectivityPrecheckResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncConnectivityPrecheckResourceWithStreamingResponse(self)

    @overload
    async def source(
        self,
        *,
        account_id: str,
        bucket: str | NotGiven = NOT_GIVEN,
        endpoint: Optional[str] | NotGiven = NOT_GIVEN,
        secret: connectivity_precheck_source_params.R2SlurperS3SourceSchemaSecret | NotGiven = NOT_GIVEN,
        vendor: Literal["s3"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConnectivityPrecheckSourceResponse]:
        """
        Check whether tokens are valid against the source bucket

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def source(
        self,
        *,
        account_id: str,
        bucket: str | NotGiven = NOT_GIVEN,
        secret: connectivity_precheck_source_params.R2SlurperGcsSourceSchemaSecret | NotGiven = NOT_GIVEN,
        vendor: Literal["gcs"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConnectivityPrecheckSourceResponse]:
        """
        Check whether tokens are valid against the source bucket

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def source(
        self,
        *,
        account_id: str,
        bucket: str | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        secret: connectivity_precheck_source_params.R2SlurperR2SourceSchemaSecret | NotGiven = NOT_GIVEN,
        vendor: Provider | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConnectivityPrecheckSourceResponse]:
        """
        Check whether tokens are valid against the source bucket

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"])
    async def source(
        self,
        *,
        account_id: str,
        bucket: str | NotGiven = NOT_GIVEN,
        endpoint: Optional[str] | NotGiven = NOT_GIVEN,
        secret: connectivity_precheck_source_params.R2SlurperS3SourceSchemaSecret
        | connectivity_precheck_source_params.R2SlurperGcsSourceSchemaSecret
        | NotGiven = NOT_GIVEN,
        vendor: Literal["s3"] | Literal["gcs"] | Provider | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConnectivityPrecheckSourceResponse]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/slurper/source/connectivity-precheck",
            body=await async_maybe_transform(
                {
                    "bucket": bucket,
                    "endpoint": endpoint,
                    "secret": secret,
                    "vendor": vendor,
                    "jurisdiction": jurisdiction,
                },
                connectivity_precheck_source_params.ConnectivityPrecheckSourceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ConnectivityPrecheckSourceResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ConnectivityPrecheckSourceResponse]], ResultWrapper[ConnectivityPrecheckSourceResponse]
            ),
        )

    async def target(
        self,
        *,
        account_id: str,
        bucket: str | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        secret: connectivity_precheck_target_params.Secret | NotGiven = NOT_GIVEN,
        vendor: Provider | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConnectivityPrecheckTargetResponse]:
        """
        Check whether tokens are valid against the target bucket

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/slurper/target/connectivity-precheck",
            body=await async_maybe_transform(
                {
                    "bucket": bucket,
                    "jurisdiction": jurisdiction,
                    "secret": secret,
                    "vendor": vendor,
                },
                connectivity_precheck_target_params.ConnectivityPrecheckTargetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ConnectivityPrecheckTargetResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ConnectivityPrecheckTargetResponse]], ResultWrapper[ConnectivityPrecheckTargetResponse]
            ),
        )


class ConnectivityPrecheckResourceWithRawResponse:
    def __init__(self, connectivity_precheck: ConnectivityPrecheckResource) -> None:
        self._connectivity_precheck = connectivity_precheck

        self.source = to_raw_response_wrapper(
            connectivity_precheck.source,
        )
        self.target = to_raw_response_wrapper(
            connectivity_precheck.target,
        )


class AsyncConnectivityPrecheckResourceWithRawResponse:
    def __init__(self, connectivity_precheck: AsyncConnectivityPrecheckResource) -> None:
        self._connectivity_precheck = connectivity_precheck

        self.source = async_to_raw_response_wrapper(
            connectivity_precheck.source,
        )
        self.target = async_to_raw_response_wrapper(
            connectivity_precheck.target,
        )


class ConnectivityPrecheckResourceWithStreamingResponse:
    def __init__(self, connectivity_precheck: ConnectivityPrecheckResource) -> None:
        self._connectivity_precheck = connectivity_precheck

        self.source = to_streamed_response_wrapper(
            connectivity_precheck.source,
        )
        self.target = to_streamed_response_wrapper(
            connectivity_precheck.target,
        )


class AsyncConnectivityPrecheckResourceWithStreamingResponse:
    def __init__(self, connectivity_precheck: AsyncConnectivityPrecheckResource) -> None:
        self._connectivity_precheck = connectivity_precheck

        self.source = async_to_streamed_response_wrapper(
            connectivity_precheck.source,
        )
        self.target = async_to_streamed_response_wrapper(
            connectivity_precheck.target,
        )
