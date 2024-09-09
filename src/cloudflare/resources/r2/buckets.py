# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ...types.r2 import bucket_list_params, bucket_create_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.r2.bucket import Bucket
from ...types.r2.bucket_list_response import BucketListResponse

__all__ = ["BucketsResource", "AsyncBucketsResource"]


class BucketsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BucketsResourceWithRawResponse:
        return BucketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BucketsResourceWithStreamingResponse:
        return BucketsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        location_hint: Literal["apac", "eeur", "enam", "weur", "wnam"] | NotGiven = NOT_GIVEN,
        storage_class: Literal["Standard", "InfrequentAccess"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Bucket:
        """
        Creates a new R2 bucket.

        Args:
          account_id: Account ID

          name: Name of the bucket

          location_hint: Location of the bucket

          storage_class: Storage class for newly uploaded objects, unless specified otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/r2/buckets",
            body=maybe_transform(
                {
                    "name": name,
                    "location_hint": location_hint,
                    "storage_class": storage_class,
                },
                bucket_create_params.BucketCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Bucket]._unwrapper,
            ),
            cast_to=cast(Type[Bucket], ResultWrapper[Bucket]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        order: Literal["name"] | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        start_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BucketListResponse:
        """
        Lists all R2 buckets on your account

        Args:
          account_id: Account ID

          cursor: Pagination cursor received during the last List Buckets call. R2 buckets are
              paginated using cursors instead of page numbers.

          direction: Direction to order buckets

          name_contains: Bucket names to filter by. Only buckets with this phrase in their name will be
              returned.

          order: Field to order buckets by

          per_page: Maximum number of buckets to return in a single call

          start_after: Bucket name to start searching after. Buckets are ordered lexicographically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/r2/buckets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "name_contains": name_contains,
                        "order": order,
                        "per_page": per_page,
                        "start_after": start_after,
                    },
                    bucket_list_params.BucketListParams,
                ),
                post_parser=ResultWrapper[BucketListResponse]._unwrapper,
            ),
            cast_to=cast(Type[BucketListResponse], ResultWrapper[BucketListResponse]),
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
    ) -> object:
        """
        Deletes an existing R2 bucket.

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
            f"/accounts/{account_id}/r2/buckets/{bucket_name}",
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Bucket:
        """
        Gets metadata for an existing R2 bucket.

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
            f"/accounts/{account_id}/r2/buckets/{bucket_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Bucket]._unwrapper,
            ),
            cast_to=cast(Type[Bucket], ResultWrapper[Bucket]),
        )


class AsyncBucketsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBucketsResourceWithRawResponse:
        return AsyncBucketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBucketsResourceWithStreamingResponse:
        return AsyncBucketsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        location_hint: Literal["apac", "eeur", "enam", "weur", "wnam"] | NotGiven = NOT_GIVEN,
        storage_class: Literal["Standard", "InfrequentAccess"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Bucket:
        """
        Creates a new R2 bucket.

        Args:
          account_id: Account ID

          name: Name of the bucket

          location_hint: Location of the bucket

          storage_class: Storage class for newly uploaded objects, unless specified otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/r2/buckets",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "location_hint": location_hint,
                    "storage_class": storage_class,
                },
                bucket_create_params.BucketCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Bucket]._unwrapper,
            ),
            cast_to=cast(Type[Bucket], ResultWrapper[Bucket]),
        )

    async def list(
        self,
        *,
        account_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        name_contains: str | NotGiven = NOT_GIVEN,
        order: Literal["name"] | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        start_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BucketListResponse:
        """
        Lists all R2 buckets on your account

        Args:
          account_id: Account ID

          cursor: Pagination cursor received during the last List Buckets call. R2 buckets are
              paginated using cursors instead of page numbers.

          direction: Direction to order buckets

          name_contains: Bucket names to filter by. Only buckets with this phrase in their name will be
              returned.

          order: Field to order buckets by

          per_page: Maximum number of buckets to return in a single call

          start_after: Bucket name to start searching after. Buckets are ordered lexicographically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/r2/buckets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "name_contains": name_contains,
                        "order": order,
                        "per_page": per_page,
                        "start_after": start_after,
                    },
                    bucket_list_params.BucketListParams,
                ),
                post_parser=ResultWrapper[BucketListResponse]._unwrapper,
            ),
            cast_to=cast(Type[BucketListResponse], ResultWrapper[BucketListResponse]),
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
    ) -> object:
        """
        Deletes an existing R2 bucket.

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
            f"/accounts/{account_id}/r2/buckets/{bucket_name}",
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Bucket:
        """
        Gets metadata for an existing R2 bucket.

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
            f"/accounts/{account_id}/r2/buckets/{bucket_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Bucket]._unwrapper,
            ),
            cast_to=cast(Type[Bucket], ResultWrapper[Bucket]),
        )


class BucketsResourceWithRawResponse:
    def __init__(self, buckets: BucketsResource) -> None:
        self._buckets = buckets

        self.create = to_raw_response_wrapper(
            buckets.create,
        )
        self.list = to_raw_response_wrapper(
            buckets.list,
        )
        self.delete = to_raw_response_wrapper(
            buckets.delete,
        )
        self.get = to_raw_response_wrapper(
            buckets.get,
        )


class AsyncBucketsResourceWithRawResponse:
    def __init__(self, buckets: AsyncBucketsResource) -> None:
        self._buckets = buckets

        self.create = async_to_raw_response_wrapper(
            buckets.create,
        )
        self.list = async_to_raw_response_wrapper(
            buckets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            buckets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            buckets.get,
        )


class BucketsResourceWithStreamingResponse:
    def __init__(self, buckets: BucketsResource) -> None:
        self._buckets = buckets

        self.create = to_streamed_response_wrapper(
            buckets.create,
        )
        self.list = to_streamed_response_wrapper(
            buckets.list,
        )
        self.delete = to_streamed_response_wrapper(
            buckets.delete,
        )
        self.get = to_streamed_response_wrapper(
            buckets.get,
        )


class AsyncBucketsResourceWithStreamingResponse:
    def __init__(self, buckets: AsyncBucketsResource) -> None:
        self._buckets = buckets

        self.create = async_to_streamed_response_wrapper(
            buckets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            buckets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            buckets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            buckets.get,
        )
