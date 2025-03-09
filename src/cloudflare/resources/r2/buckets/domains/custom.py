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
from .....types.r2.buckets.domains import custom_create_params
from .....types.r2.buckets.domains.custom_list_response import CustomListResponse
from .....types.r2.buckets.domains.custom_create_response import CustomCreateResponse

__all__ = ["CustomResource", "AsyncCustomResource"]


class CustomResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CustomResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CustomResourceWithStreamingResponse(self)

    def create(
        self,
        bucket_name: str,
        *,
        account_id: str,
        domain: str,
        enabled: bool,
        zone_id: str,
        min_tls: Literal["1.0", "1.1", "1.2", "1.3"] | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomCreateResponse:
        """
        Register a new custom domain for an existing R2 bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          domain: Name of the custom domain to be added

          enabled: Whether to enable public bucket access at the custom domain. If undefined, the
              domain will be enabled.

          zone_id: Zone ID of the custom domain

          min_tls: Minimum TLS Version the custom domain will accept for incoming connections. If
              not set, defaults to 1.0.

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
        return self._post(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom",
            body=maybe_transform(
                {
                    "domain": domain,
                    "enabled": enabled,
                    "zone_id": zone_id,
                    "min_tls": min_tls,
                },
                custom_create_params.CustomCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomCreateResponse], ResultWrapper[CustomCreateResponse]),
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
    ) -> CustomListResponse:
        """
        Gets a list of all custom domains registered with an existing R2 bucket.

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
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomListResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomListResponse], ResultWrapper[CustomListResponse]),
        )


class AsyncCustomResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCustomResourceWithStreamingResponse(self)

    async def create(
        self,
        bucket_name: str,
        *,
        account_id: str,
        domain: str,
        enabled: bool,
        zone_id: str,
        min_tls: Literal["1.0", "1.1", "1.2", "1.3"] | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomCreateResponse:
        """
        Register a new custom domain for an existing R2 bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          domain: Name of the custom domain to be added

          enabled: Whether to enable public bucket access at the custom domain. If undefined, the
              domain will be enabled.

          zone_id: Zone ID of the custom domain

          min_tls: Minimum TLS Version the custom domain will accept for incoming connections. If
              not set, defaults to 1.0.

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
        return await self._post(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "enabled": enabled,
                    "zone_id": zone_id,
                    "min_tls": min_tls,
                },
                custom_create_params.CustomCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomCreateResponse], ResultWrapper[CustomCreateResponse]),
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
    ) -> CustomListResponse:
        """
        Gets a list of all custom domains registered with an existing R2 bucket.

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
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomListResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomListResponse], ResultWrapper[CustomListResponse]),
        )


class CustomResourceWithRawResponse:
    def __init__(self, custom: CustomResource) -> None:
        self._custom = custom

        self.create = to_raw_response_wrapper(
            custom.create,
        )
        self.list = to_raw_response_wrapper(
            custom.list,
        )


class AsyncCustomResourceWithRawResponse:
    def __init__(self, custom: AsyncCustomResource) -> None:
        self._custom = custom

        self.create = async_to_raw_response_wrapper(
            custom.create,
        )
        self.list = async_to_raw_response_wrapper(
            custom.list,
        )


class CustomResourceWithStreamingResponse:
    def __init__(self, custom: CustomResource) -> None:
        self._custom = custom

        self.create = to_streamed_response_wrapper(
            custom.create,
        )
        self.list = to_streamed_response_wrapper(
            custom.list,
        )


class AsyncCustomResourceWithStreamingResponse:
    def __init__(self, custom: AsyncCustomResource) -> None:
        self._custom = custom

        self.create = async_to_streamed_response_wrapper(
            custom.create,
        )
        self.list = async_to_streamed_response_wrapper(
            custom.list,
        )
