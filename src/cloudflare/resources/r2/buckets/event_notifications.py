# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import is_given, path_template, maybe_transform, strip_not_given, async_maybe_transform
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
from ....types.r2.buckets import event_notification_update_params
from ....types.r2.buckets.event_notification_get_response import EventNotificationGetResponse
from ....types.r2.buckets.event_notification_list_response import EventNotificationListResponse

__all__ = ["EventNotificationsResource", "AsyncEventNotificationsResource"]


class EventNotificationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EventNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EventNotificationsResourceWithStreamingResponse(self)

    def update(
        self,
        queue_id: str,
        *,
        account_id: str,
        bucket_name: str,
        rules: Iterable[event_notification_update_params.Rule],
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Creates rules that send notifications for matching R2 object events to the
        specified Cloudflare Queue. Rules can filter objects by key prefix and suffix.
        New rules are added to any existing rules for the queue; a rule that overlaps an
        existing rule is rejected.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

          queue_id: ID of the Cloudflare Queue that receives notifications for matching R2 object
              events.

          rules: Array of rules to drive notifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else not_given}
            ),
            **(extra_headers or {}),
        }
        return self._put(
            path_template(
                "/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}",
                account_id=account_id,
                bucket_name=bucket_name,
                queue_id=queue_id,
            ),
            body=maybe_transform({"rules": rules}, event_notification_update_params.EventNotificationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def list(
        self,
        bucket_name: str,
        *,
        account_id: str,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventNotificationListResponse:
        """
        Lists event notification rules for an R2 bucket, grouped by the Cloudflare Queue
        that receives matching object events.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

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
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else not_given}
            ),
            **(extra_headers or {}),
        }
        return self._get(
            path_template(
                "/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration",
                account_id=account_id,
                bucket_name=bucket_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EventNotificationListResponse]._unwrapper,
            ),
            cast_to=cast(Type[EventNotificationListResponse], ResultWrapper[EventNotificationListResponse]),
        )

    def delete(
        self,
        queue_id: str,
        *,
        account_id: str,
        bucket_name: str,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes the specified event notification rules for an R2 bucket and Cloudflare
        Queue. Provide ruleIds in the request body to select rules. If no body is
        provided, all rules for that bucket and queue are deleted.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

          queue_id: ID of the Cloudflare Queue that receives notifications for matching R2 object
              events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else not_given}
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            path_template(
                "/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}",
                account_id=account_id,
                bucket_name=bucket_name,
                queue_id=queue_id,
            ),
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
        queue_id: str,
        *,
        account_id: str,
        bucket_name: str,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventNotificationGetResponse:
        """
        Gets the event notification rules for the specified R2 bucket and Cloudflare
        Queue. The response includes the queue's configuration and its array of rules.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

          queue_id: ID of the Cloudflare Queue that receives notifications for matching R2 object
              events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else not_given}
            ),
            **(extra_headers or {}),
        }
        return self._get(
            path_template(
                "/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}",
                account_id=account_id,
                bucket_name=bucket_name,
                queue_id=queue_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EventNotificationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[EventNotificationGetResponse], ResultWrapper[EventNotificationGetResponse]),
        )


class AsyncEventNotificationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEventNotificationsResourceWithStreamingResponse(self)

    async def update(
        self,
        queue_id: str,
        *,
        account_id: str,
        bucket_name: str,
        rules: Iterable[event_notification_update_params.Rule],
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Creates rules that send notifications for matching R2 object events to the
        specified Cloudflare Queue. Rules can filter objects by key prefix and suffix.
        New rules are added to any existing rules for the queue; a rule that overlaps an
        existing rule is rejected.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

          queue_id: ID of the Cloudflare Queue that receives notifications for matching R2 object
              events.

          rules: Array of rules to drive notifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else not_given}
            ),
            **(extra_headers or {}),
        }
        return await self._put(
            path_template(
                "/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}",
                account_id=account_id,
                bucket_name=bucket_name,
                queue_id=queue_id,
            ),
            body=await async_maybe_transform(
                {"rules": rules}, event_notification_update_params.EventNotificationUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def list(
        self,
        bucket_name: str,
        *,
        account_id: str,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventNotificationListResponse:
        """
        Lists event notification rules for an R2 bucket, grouped by the Cloudflare Queue
        that receives matching object events.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

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
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else not_given}
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template(
                "/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration",
                account_id=account_id,
                bucket_name=bucket_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EventNotificationListResponse]._unwrapper,
            ),
            cast_to=cast(Type[EventNotificationListResponse], ResultWrapper[EventNotificationListResponse]),
        )

    async def delete(
        self,
        queue_id: str,
        *,
        account_id: str,
        bucket_name: str,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes the specified event notification rules for an R2 bucket and Cloudflare
        Queue. Provide ruleIds in the request body to select rules. If no body is
        provided, all rules for that bucket and queue are deleted.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

          queue_id: ID of the Cloudflare Queue that receives notifications for matching R2 object
              events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else not_given}
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            path_template(
                "/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}",
                account_id=account_id,
                bucket_name=bucket_name,
                queue_id=queue_id,
            ),
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
        queue_id: str,
        *,
        account_id: str,
        bucket_name: str,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventNotificationGetResponse:
        """
        Gets the event notification rules for the specified R2 bucket and Cloudflare
        Queue. The response includes the queue's configuration and its array of rules.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

          queue_id: ID of the Cloudflare Queue that receives notifications for matching R2 object
              events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else not_given}
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template(
                "/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}",
                account_id=account_id,
                bucket_name=bucket_name,
                queue_id=queue_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EventNotificationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[EventNotificationGetResponse], ResultWrapper[EventNotificationGetResponse]),
        )


class EventNotificationsResourceWithRawResponse:
    def __init__(self, event_notifications: EventNotificationsResource) -> None:
        self._event_notifications = event_notifications

        self.update = to_raw_response_wrapper(
            event_notifications.update,
        )
        self.list = to_raw_response_wrapper(
            event_notifications.list,
        )
        self.delete = to_raw_response_wrapper(
            event_notifications.delete,
        )
        self.get = to_raw_response_wrapper(
            event_notifications.get,
        )


class AsyncEventNotificationsResourceWithRawResponse:
    def __init__(self, event_notifications: AsyncEventNotificationsResource) -> None:
        self._event_notifications = event_notifications

        self.update = async_to_raw_response_wrapper(
            event_notifications.update,
        )
        self.list = async_to_raw_response_wrapper(
            event_notifications.list,
        )
        self.delete = async_to_raw_response_wrapper(
            event_notifications.delete,
        )
        self.get = async_to_raw_response_wrapper(
            event_notifications.get,
        )


class EventNotificationsResourceWithStreamingResponse:
    def __init__(self, event_notifications: EventNotificationsResource) -> None:
        self._event_notifications = event_notifications

        self.update = to_streamed_response_wrapper(
            event_notifications.update,
        )
        self.list = to_streamed_response_wrapper(
            event_notifications.list,
        )
        self.delete = to_streamed_response_wrapper(
            event_notifications.delete,
        )
        self.get = to_streamed_response_wrapper(
            event_notifications.get,
        )


class AsyncEventNotificationsResourceWithStreamingResponse:
    def __init__(self, event_notifications: AsyncEventNotificationsResource) -> None:
        self._event_notifications = event_notifications

        self.update = async_to_streamed_response_wrapper(
            event_notifications.update,
        )
        self.list = async_to_streamed_response_wrapper(
            event_notifications.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            event_notifications.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            event_notifications.get,
        )
