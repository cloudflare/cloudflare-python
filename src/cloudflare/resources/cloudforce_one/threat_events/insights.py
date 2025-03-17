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
from ....types.cloudforce_one.threat_events import insight_edit_params, insight_create_params
from ....types.cloudforce_one.threat_events.insight_get_response import InsightGetResponse
from ....types.cloudforce_one.threat_events.insight_edit_response import InsightEditResponse
from ....types.cloudforce_one.threat_events.insight_create_response import InsightCreateResponse
from ....types.cloudforce_one.threat_events.insight_delete_response import InsightDeleteResponse

__all__ = ["InsightsResource", "AsyncInsightsResource"]


class InsightsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return InsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return InsightsResourceWithStreamingResponse(self)

    def create(
        self,
        event_id: str,
        *,
        account_id: float,
        content: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightCreateResponse:
        """
        Adds an insight to an event

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
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}/insight/create",
            body=maybe_transform({"content": content}, insight_create_params.InsightCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InsightCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[InsightCreateResponse], ResultWrapper[InsightCreateResponse]),
        )

    def delete(
        self,
        insight_id: str,
        *,
        account_id: float,
        event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightDeleteResponse:
        """
        Deletes an event insight

        Args:
          account_id: Account ID

          event_id: Event UUID

          insight_id: Insight UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return self._delete(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}/insight/{insight_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InsightDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[InsightDeleteResponse], ResultWrapper[InsightDeleteResponse]),
        )

    def edit(
        self,
        insight_id: str,
        *,
        account_id: float,
        event_id: str,
        content: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightEditResponse:
        """
        Updates an event insight

        Args:
          account_id: Account ID

          event_id: Event UUID

          insight_id: Insight UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return self._patch(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}/insight/{insight_id}",
            body=maybe_transform({"content": content}, insight_edit_params.InsightEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InsightEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[InsightEditResponse], ResultWrapper[InsightEditResponse]),
        )

    def get(
        self,
        insight_id: str,
        *,
        account_id: float,
        event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightGetResponse:
        """
        Reads an event insight

        Args:
          account_id: Account ID

          event_id: Event UUID

          insight_id: Insight UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return self._get(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}/insight/{insight_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InsightGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[InsightGetResponse], ResultWrapper[InsightGetResponse]),
        )


class AsyncInsightsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncInsightsResourceWithStreamingResponse(self)

    async def create(
        self,
        event_id: str,
        *,
        account_id: float,
        content: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightCreateResponse:
        """
        Adds an insight to an event

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
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}/insight/create",
            body=await async_maybe_transform({"content": content}, insight_create_params.InsightCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InsightCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[InsightCreateResponse], ResultWrapper[InsightCreateResponse]),
        )

    async def delete(
        self,
        insight_id: str,
        *,
        account_id: float,
        event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightDeleteResponse:
        """
        Deletes an event insight

        Args:
          account_id: Account ID

          event_id: Event UUID

          insight_id: Insight UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}/insight/{insight_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InsightDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[InsightDeleteResponse], ResultWrapper[InsightDeleteResponse]),
        )

    async def edit(
        self,
        insight_id: str,
        *,
        account_id: float,
        event_id: str,
        content: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightEditResponse:
        """
        Updates an event insight

        Args:
          account_id: Account ID

          event_id: Event UUID

          insight_id: Insight UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}/insight/{insight_id}",
            body=await async_maybe_transform({"content": content}, insight_edit_params.InsightEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InsightEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[InsightEditResponse], ResultWrapper[InsightEditResponse]),
        )

    async def get(
        self,
        insight_id: str,
        *,
        account_id: float,
        event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsightGetResponse:
        """
        Reads an event insight

        Args:
          account_id: Account ID

          event_id: Event UUID

          insight_id: Insight UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return await self._get(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}/insight/{insight_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InsightGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[InsightGetResponse], ResultWrapper[InsightGetResponse]),
        )


class InsightsResourceWithRawResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.create = to_raw_response_wrapper(
            insights.create,
        )
        self.delete = to_raw_response_wrapper(
            insights.delete,
        )
        self.edit = to_raw_response_wrapper(
            insights.edit,
        )
        self.get = to_raw_response_wrapper(
            insights.get,
        )


class AsyncInsightsResourceWithRawResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.create = async_to_raw_response_wrapper(
            insights.create,
        )
        self.delete = async_to_raw_response_wrapper(
            insights.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            insights.edit,
        )
        self.get = async_to_raw_response_wrapper(
            insights.get,
        )


class InsightsResourceWithStreamingResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.create = to_streamed_response_wrapper(
            insights.create,
        )
        self.delete = to_streamed_response_wrapper(
            insights.delete,
        )
        self.edit = to_streamed_response_wrapper(
            insights.edit,
        )
        self.get = to_streamed_response_wrapper(
            insights.get,
        )


class AsyncInsightsResourceWithStreamingResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.create = async_to_streamed_response_wrapper(
            insights.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            insights.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            insights.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            insights.get,
        )
