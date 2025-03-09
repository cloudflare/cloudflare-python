# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from .cors import (
    CORSResource,
    AsyncCORSResource,
    CORSResourceWithRawResponse,
    AsyncCORSResourceWithRawResponse,
    CORSResourceWithStreamingResponse,
    AsyncCORSResourceWithStreamingResponse,
)
from .locks import (
    LocksResource,
    AsyncLocksResource,
    LocksResourceWithRawResponse,
    AsyncLocksResourceWithRawResponse,
    LocksResourceWithStreamingResponse,
    AsyncLocksResourceWithStreamingResponse,
)
from .sippy import (
    SippyResource,
    AsyncSippyResource,
    SippyResourceWithRawResponse,
    AsyncSippyResourceWithRawResponse,
    SippyResourceWithStreamingResponse,
    AsyncSippyResourceWithStreamingResponse,
)
from .metrics import (
    MetricsResource,
    AsyncMetricsResource,
    MetricsResourceWithRawResponse,
    AsyncMetricsResourceWithRawResponse,
    MetricsResourceWithStreamingResponse,
    AsyncMetricsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .lifecycle import (
    LifecycleResource,
    AsyncLifecycleResource,
    LifecycleResourceWithRawResponse,
    AsyncLifecycleResourceWithRawResponse,
    LifecycleResourceWithStreamingResponse,
    AsyncLifecycleResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ....types.r2 import bucket_list_params, bucket_create_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from .domains.domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
from ....types.r2.bucket import Bucket
from .event_notifications import (
    EventNotificationsResource,
    AsyncEventNotificationsResource,
    EventNotificationsResourceWithRawResponse,
    AsyncEventNotificationsResourceWithRawResponse,
    EventNotificationsResourceWithStreamingResponse,
    AsyncEventNotificationsResourceWithStreamingResponse,
)
from ....types.r2.bucket_list_response import BucketListResponse

__all__ = ["BucketsResource", "AsyncBucketsResource"]


class BucketsResource(SyncAPIResource):
    @cached_property
    def lifecycle(self) -> LifecycleResource:
        return LifecycleResource(self._client)

    @cached_property
    def cors(self) -> CORSResource:
        return CORSResource(self._client)

    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def event_notifications(self) -> EventNotificationsResource:
        return EventNotificationsResource(self._client)

    @cached_property
    def locks(self) -> LocksResource:
        return LocksResource(self._client)

    @cached_property
    def metrics(self) -> MetricsResource:
        return MetricsResource(self._client)

    @cached_property
    def sippy(self) -> SippyResource:
        return SippyResource(self._client)

    @cached_property
    def with_raw_response(self) -> BucketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BucketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BucketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BucketsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        location_hint: Literal["apac", "eeur", "enam", "weur", "wnam", "oc"] | NotGiven = NOT_GIVEN,
        storage_class: Literal["Standard", "InfrequentAccess"] | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
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

          jurisdiction: Creates the bucket in the provided jurisdiction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given({"cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
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
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
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

          jurisdiction: Lists buckets in the provided jurisdiction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given({"cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
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
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
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
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
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
    def lifecycle(self) -> AsyncLifecycleResource:
        return AsyncLifecycleResource(self._client)

    @cached_property
    def cors(self) -> AsyncCORSResource:
        return AsyncCORSResource(self._client)

    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def event_notifications(self) -> AsyncEventNotificationsResource:
        return AsyncEventNotificationsResource(self._client)

    @cached_property
    def locks(self) -> AsyncLocksResource:
        return AsyncLocksResource(self._client)

    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        return AsyncMetricsResource(self._client)

    @cached_property
    def sippy(self) -> AsyncSippyResource:
        return AsyncSippyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBucketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBucketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBucketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBucketsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        location_hint: Literal["apac", "eeur", "enam", "weur", "wnam", "oc"] | NotGiven = NOT_GIVEN,
        storage_class: Literal["Standard", "InfrequentAccess"] | NotGiven = NOT_GIVEN,
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
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

          jurisdiction: Creates the bucket in the provided jurisdiction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given({"cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
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
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
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

          jurisdiction: Lists buckets in the provided jurisdiction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given({"cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
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
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
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
        jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
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

    @cached_property
    def lifecycle(self) -> LifecycleResourceWithRawResponse:
        return LifecycleResourceWithRawResponse(self._buckets.lifecycle)

    @cached_property
    def cors(self) -> CORSResourceWithRawResponse:
        return CORSResourceWithRawResponse(self._buckets.cors)

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._buckets.domains)

    @cached_property
    def event_notifications(self) -> EventNotificationsResourceWithRawResponse:
        return EventNotificationsResourceWithRawResponse(self._buckets.event_notifications)

    @cached_property
    def locks(self) -> LocksResourceWithRawResponse:
        return LocksResourceWithRawResponse(self._buckets.locks)

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        return MetricsResourceWithRawResponse(self._buckets.metrics)

    @cached_property
    def sippy(self) -> SippyResourceWithRawResponse:
        return SippyResourceWithRawResponse(self._buckets.sippy)


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

    @cached_property
    def lifecycle(self) -> AsyncLifecycleResourceWithRawResponse:
        return AsyncLifecycleResourceWithRawResponse(self._buckets.lifecycle)

    @cached_property
    def cors(self) -> AsyncCORSResourceWithRawResponse:
        return AsyncCORSResourceWithRawResponse(self._buckets.cors)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._buckets.domains)

    @cached_property
    def event_notifications(self) -> AsyncEventNotificationsResourceWithRawResponse:
        return AsyncEventNotificationsResourceWithRawResponse(self._buckets.event_notifications)

    @cached_property
    def locks(self) -> AsyncLocksResourceWithRawResponse:
        return AsyncLocksResourceWithRawResponse(self._buckets.locks)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        return AsyncMetricsResourceWithRawResponse(self._buckets.metrics)

    @cached_property
    def sippy(self) -> AsyncSippyResourceWithRawResponse:
        return AsyncSippyResourceWithRawResponse(self._buckets.sippy)


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

    @cached_property
    def lifecycle(self) -> LifecycleResourceWithStreamingResponse:
        return LifecycleResourceWithStreamingResponse(self._buckets.lifecycle)

    @cached_property
    def cors(self) -> CORSResourceWithStreamingResponse:
        return CORSResourceWithStreamingResponse(self._buckets.cors)

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._buckets.domains)

    @cached_property
    def event_notifications(self) -> EventNotificationsResourceWithStreamingResponse:
        return EventNotificationsResourceWithStreamingResponse(self._buckets.event_notifications)

    @cached_property
    def locks(self) -> LocksResourceWithStreamingResponse:
        return LocksResourceWithStreamingResponse(self._buckets.locks)

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        return MetricsResourceWithStreamingResponse(self._buckets.metrics)

    @cached_property
    def sippy(self) -> SippyResourceWithStreamingResponse:
        return SippyResourceWithStreamingResponse(self._buckets.sippy)


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

    @cached_property
    def lifecycle(self) -> AsyncLifecycleResourceWithStreamingResponse:
        return AsyncLifecycleResourceWithStreamingResponse(self._buckets.lifecycle)

    @cached_property
    def cors(self) -> AsyncCORSResourceWithStreamingResponse:
        return AsyncCORSResourceWithStreamingResponse(self._buckets.cors)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._buckets.domains)

    @cached_property
    def event_notifications(self) -> AsyncEventNotificationsResourceWithStreamingResponse:
        return AsyncEventNotificationsResourceWithStreamingResponse(self._buckets.event_notifications)

    @cached_property
    def locks(self) -> AsyncLocksResourceWithStreamingResponse:
        return AsyncLocksResourceWithStreamingResponse(self._buckets.locks)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._buckets.metrics)

    @cached_property
    def sippy(self) -> AsyncSippyResourceWithStreamingResponse:
        return AsyncSippyResourceWithStreamingResponse(self._buckets.sippy)
