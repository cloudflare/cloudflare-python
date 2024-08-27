# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
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
from ....types.r2.domains import custom_create_params, custom_update_params
from ....types.r2.domains.custom_get_response import CustomGetResponse
from ....types.r2.domains.custom_create_response import CustomCreateResponse
from ....types.r2.domains.custom_delete_response import CustomDeleteResponse
from ....types.r2.domains.custom_update_response import CustomUpdateResponse

__all__ = ["CustomResource", "AsyncCustomResource"]


class CustomResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomResourceWithRawResponse:
        return CustomResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomResourceWithStreamingResponse:
        return CustomResourceWithStreamingResponse(self)

    def create(
        self,
        bucket_name: str,
        *,
        account_id: str,
        domain: str,
        zone_name: str,
        zone_tag: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
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

          zone_name: Zone name of the custom domain. Note that `zoneName` must be a suffix of
              `domain`.

          zone_tag: Zone tag of the custom domain

          enabled: Whether to enable public bucket access at the custom domain. If undefined, the
              domain will be enabled.

          zone_id: Zone ID of the custom domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return self._post(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom",
            body=maybe_transform(
                {
                    "domain": domain,
                    "zone_name": zone_name,
                    "zone_tag": zone_tag,
                    "enabled": enabled,
                    "zone_id": zone_id,
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

    def update(
        self,
        domain_name: str,
        *,
        account_id: str,
        bucket_name: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomUpdateResponse:
        """
        Edit the configuration for a custom domain on an existing R2 bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          domain_name: Name of the custom domain

          enabled: Whether to enable public bucket access at the specified custom domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return self._put(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain_name}",
            body=maybe_transform({"enabled": enabled}, custom_update_params.CustomUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomUpdateResponse], ResultWrapper[CustomUpdateResponse]),
        )

    def delete(
        self,
        domain_name: str,
        *,
        account_id: str,
        bucket_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomDeleteResponse:
        """
        Remove custom domain registration from an existing R2 bucket

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          domain_name: Name of the custom domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return self._delete(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomDeleteResponse], ResultWrapper[CustomDeleteResponse]),
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
    ) -> CustomGetResponse:
        """
        Gets a list of all custom domains registered with an existing R2 bucket.

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
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomGetResponse], ResultWrapper[CustomGetResponse]),
        )


class AsyncCustomResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomResourceWithRawResponse:
        return AsyncCustomResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomResourceWithStreamingResponse:
        return AsyncCustomResourceWithStreamingResponse(self)

    async def create(
        self,
        bucket_name: str,
        *,
        account_id: str,
        domain: str,
        zone_name: str,
        zone_tag: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
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

          zone_name: Zone name of the custom domain. Note that `zoneName` must be a suffix of
              `domain`.

          zone_tag: Zone tag of the custom domain

          enabled: Whether to enable public bucket access at the custom domain. If undefined, the
              domain will be enabled.

          zone_id: Zone ID of the custom domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return await self._post(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "zone_name": zone_name,
                    "zone_tag": zone_tag,
                    "enabled": enabled,
                    "zone_id": zone_id,
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

    async def update(
        self,
        domain_name: str,
        *,
        account_id: str,
        bucket_name: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomUpdateResponse:
        """
        Edit the configuration for a custom domain on an existing R2 bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          domain_name: Name of the custom domain

          enabled: Whether to enable public bucket access at the specified custom domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return await self._put(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain_name}",
            body=await async_maybe_transform({"enabled": enabled}, custom_update_params.CustomUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomUpdateResponse], ResultWrapper[CustomUpdateResponse]),
        )

    async def delete(
        self,
        domain_name: str,
        *,
        account_id: str,
        bucket_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomDeleteResponse:
        """
        Remove custom domain registration from an existing R2 bucket

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          domain_name: Name of the custom domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return await self._delete(
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomDeleteResponse], ResultWrapper[CustomDeleteResponse]),
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
    ) -> CustomGetResponse:
        """
        Gets a list of all custom domains registered with an existing R2 bucket.

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
            f"/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CustomGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CustomGetResponse], ResultWrapper[CustomGetResponse]),
        )


class CustomResourceWithRawResponse:
    def __init__(self, custom: CustomResource) -> None:
        self._custom = custom

        self.create = to_raw_response_wrapper(
            custom.create,
        )
        self.update = to_raw_response_wrapper(
            custom.update,
        )
        self.delete = to_raw_response_wrapper(
            custom.delete,
        )
        self.get = to_raw_response_wrapper(
            custom.get,
        )


class AsyncCustomResourceWithRawResponse:
    def __init__(self, custom: AsyncCustomResource) -> None:
        self._custom = custom

        self.create = async_to_raw_response_wrapper(
            custom.create,
        )
        self.update = async_to_raw_response_wrapper(
            custom.update,
        )
        self.delete = async_to_raw_response_wrapper(
            custom.delete,
        )
        self.get = async_to_raw_response_wrapper(
            custom.get,
        )


class CustomResourceWithStreamingResponse:
    def __init__(self, custom: CustomResource) -> None:
        self._custom = custom

        self.create = to_streamed_response_wrapper(
            custom.create,
        )
        self.update = to_streamed_response_wrapper(
            custom.update,
        )
        self.delete = to_streamed_response_wrapper(
            custom.delete,
        )
        self.get = to_streamed_response_wrapper(
            custom.get,
        )


class AsyncCustomResourceWithStreamingResponse:
    def __init__(self, custom: AsyncCustomResource) -> None:
        self._custom = custom

        self.create = async_to_streamed_response_wrapper(
            custom.create,
        )
        self.update = async_to_streamed_response_wrapper(
            custom.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            custom.get,
        )
