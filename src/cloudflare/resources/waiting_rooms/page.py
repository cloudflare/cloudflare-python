# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.waiting_rooms import page_preview_params
from ...types.waiting_rooms.page_preview_response import PagePreviewResponse

__all__ = ["PageResource", "AsyncPageResource"]


class PageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PageResourceWithStreamingResponse(self)

    def preview(
        self,
        *,
        zone_id: str,
        custom_html: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PagePreviewResponse:
        """Creates a waiting room page preview.

        Upload a custom waiting room page for
        preview. You will receive a preview URL in the form
        `http://waitingrooms.dev/preview/<uuid>`. You can use the following query
        parameters to change the state of the preview:

        1. `force_queue`: Boolean indicating if all users will be queued in the waiting
           room and no one will be let into the origin website (also known as queueAll).
        2. `queue_is_full`: Boolean indicating if the waiting room's queue is currently
           full and not accepting new users at the moment.
        3. `queueing_method`: The queueing method currently used by the waiting room.
           - **fifo** indicates a FIFO queue.
           - **random** indicates a Random queue.
           - **passthrough** indicates a Passthrough queue. Keep in mind that the
             waiting room page will only be displayed if `force_queue=true` or
             `event=prequeueing` — for other cases the request will pass through to the
             origin. For our preview, this will be a fake origin website returning
             "Welcome".
           - **reject** indicates a Reject queue.
        4. `event`: Used to preview a waiting room event.
           - **none** indicates no event is occurring.
           - **prequeueing** indicates that an event is prequeueing (between
             `prequeue_start_time` and `event_start_time`).
           - **started** indicates that an event has started (between `event_start_time`
             and `event_end_time`).
        5. `shuffle_at_event_start`: Boolean indicating if the event will shuffle users
           in the prequeue when it starts. This can only be set to **true** if an event
           is active (`event` is not **none**).

        For example, you can make a request to
        `http://waitingrooms.dev/preview/<uuid>?force_queue=false&queue_is_full=false&queueing_method=random&event=started&shuffle_at_event_start=true` 6.
        `waitTime`: Non-zero, positive integer indicating the estimated wait time in
        minutes. The default value is 10 minutes.

        For example, you can make a request to
        `http://waitingrooms.dev/preview/<uuid>?waitTime=50` to configure the estimated
        wait time as 50 minutes.

        Args:
          zone_id: Identifier

          custom_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/waiting_rooms/preview",
            body=maybe_transform({"custom_html": custom_html}, page_preview_params.PagePreviewParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PagePreviewResponse]._unwrapper,
            ),
            cast_to=cast(Type[PagePreviewResponse], ResultWrapper[PagePreviewResponse]),
        )


class AsyncPageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPageResourceWithStreamingResponse(self)

    async def preview(
        self,
        *,
        zone_id: str,
        custom_html: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PagePreviewResponse:
        """Creates a waiting room page preview.

        Upload a custom waiting room page for
        preview. You will receive a preview URL in the form
        `http://waitingrooms.dev/preview/<uuid>`. You can use the following query
        parameters to change the state of the preview:

        1. `force_queue`: Boolean indicating if all users will be queued in the waiting
           room and no one will be let into the origin website (also known as queueAll).
        2. `queue_is_full`: Boolean indicating if the waiting room's queue is currently
           full and not accepting new users at the moment.
        3. `queueing_method`: The queueing method currently used by the waiting room.
           - **fifo** indicates a FIFO queue.
           - **random** indicates a Random queue.
           - **passthrough** indicates a Passthrough queue. Keep in mind that the
             waiting room page will only be displayed if `force_queue=true` or
             `event=prequeueing` — for other cases the request will pass through to the
             origin. For our preview, this will be a fake origin website returning
             "Welcome".
           - **reject** indicates a Reject queue.
        4. `event`: Used to preview a waiting room event.
           - **none** indicates no event is occurring.
           - **prequeueing** indicates that an event is prequeueing (between
             `prequeue_start_time` and `event_start_time`).
           - **started** indicates that an event has started (between `event_start_time`
             and `event_end_time`).
        5. `shuffle_at_event_start`: Boolean indicating if the event will shuffle users
           in the prequeue when it starts. This can only be set to **true** if an event
           is active (`event` is not **none**).

        For example, you can make a request to
        `http://waitingrooms.dev/preview/<uuid>?force_queue=false&queue_is_full=false&queueing_method=random&event=started&shuffle_at_event_start=true` 6.
        `waitTime`: Non-zero, positive integer indicating the estimated wait time in
        minutes. The default value is 10 minutes.

        For example, you can make a request to
        `http://waitingrooms.dev/preview/<uuid>?waitTime=50` to configure the estimated
        wait time as 50 minutes.

        Args:
          zone_id: Identifier

          custom_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/waiting_rooms/preview",
            body=await async_maybe_transform({"custom_html": custom_html}, page_preview_params.PagePreviewParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PagePreviewResponse]._unwrapper,
            ),
            cast_to=cast(Type[PagePreviewResponse], ResultWrapper[PagePreviewResponse]),
        )


class PageResourceWithRawResponse:
    def __init__(self, page: PageResource) -> None:
        self._page = page

        self.preview = to_raw_response_wrapper(
            page.preview,
        )


class AsyncPageResourceWithRawResponse:
    def __init__(self, page: AsyncPageResource) -> None:
        self._page = page

        self.preview = async_to_raw_response_wrapper(
            page.preview,
        )


class PageResourceWithStreamingResponse:
    def __init__(self, page: PageResource) -> None:
        self._page = page

        self.preview = to_streamed_response_wrapper(
            page.preview,
        )


class AsyncPageResourceWithStreamingResponse:
    def __init__(self, page: AsyncPageResource) -> None:
        self._page = page

        self.preview = async_to_streamed_response_wrapper(
            page.preview,
        )
