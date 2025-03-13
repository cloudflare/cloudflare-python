# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast

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
from ....types.cloudforce_one.threat_events import event_tag_create_params
from ....types.cloudforce_one.threat_events.event_tag_create_response import EventTagCreateResponse
from ....types.cloudforce_one.threat_events.event_tag_delete_response import EventTagDeleteResponse

__all__ = ["EventTagsResource", "AsyncEventTagsResource"]


class EventTagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EventTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EventTagsResourceWithStreamingResponse(self)

    def create(
        self,
        event_id: str,
        *,
        account_id: float,
        tags: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventTagCreateResponse:
        """
        Adds a tag to an event

        Args:
          account_id: Account ID

          event_id: Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._post(
            f"/accounts/{account_id}/cloudforce-one/events/event_tag/{event_id}/create",
            body=maybe_transform({"tags": tags}, event_tag_create_params.EventTagCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EventTagCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[EventTagCreateResponse], ResultWrapper[EventTagCreateResponse]),
        )

    def delete(
        self,
        event_id: str,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventTagDeleteResponse:
        """
        Removes a tag from an event

        Args:
          account_id: Account ID

          event_id: Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._delete(
            f"/accounts/{account_id}/cloudforce-one/events/event_tag/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EventTagDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[EventTagDeleteResponse], ResultWrapper[EventTagDeleteResponse]),
        )


class AsyncEventTagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEventTagsResourceWithStreamingResponse(self)

    async def create(
        self,
        event_id: str,
        *,
        account_id: float,
        tags: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventTagCreateResponse:
        """
        Adds a tag to an event

        Args:
          account_id: Account ID

          event_id: Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._post(
            f"/accounts/{account_id}/cloudforce-one/events/event_tag/{event_id}/create",
            body=await async_maybe_transform({"tags": tags}, event_tag_create_params.EventTagCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EventTagCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[EventTagCreateResponse], ResultWrapper[EventTagCreateResponse]),
        )

    async def delete(
        self,
        event_id: str,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventTagDeleteResponse:
        """
        Removes a tag from an event

        Args:
          account_id: Account ID

          event_id: Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/cloudforce-one/events/event_tag/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EventTagDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[EventTagDeleteResponse], ResultWrapper[EventTagDeleteResponse]),
        )


class EventTagsResourceWithRawResponse:
    def __init__(self, event_tags: EventTagsResource) -> None:
        self._event_tags = event_tags

        self.create = to_raw_response_wrapper(
            event_tags.create,
        )
        self.delete = to_raw_response_wrapper(
            event_tags.delete,
        )


class AsyncEventTagsResourceWithRawResponse:
    def __init__(self, event_tags: AsyncEventTagsResource) -> None:
        self._event_tags = event_tags

        self.create = async_to_raw_response_wrapper(
            event_tags.create,
        )
        self.delete = async_to_raw_response_wrapper(
            event_tags.delete,
        )


class EventTagsResourceWithStreamingResponse:
    def __init__(self, event_tags: EventTagsResource) -> None:
        self._event_tags = event_tags

        self.create = to_streamed_response_wrapper(
            event_tags.create,
        )
        self.delete = to_streamed_response_wrapper(
            event_tags.delete,
        )


class AsyncEventTagsResourceWithStreamingResponse:
    def __init__(self, event_tags: AsyncEventTagsResource) -> None:
        self._event_tags = event_tags

        self.create = async_to_streamed_response_wrapper(
            event_tags.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            event_tags.delete,
        )
