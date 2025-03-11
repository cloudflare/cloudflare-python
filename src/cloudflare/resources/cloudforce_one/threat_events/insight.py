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
from ....types.cloudforce_one.threat_events import insight_creat_params, insight_update_params
from ....types.cloudforce_one.threat_events.insight_get_response import InsightGetResponse
from ....types.cloudforce_one.threat_events.insight_creat_response import InsightCreatResponse
from ....types.cloudforce_one.threat_events.insight_delete_response import InsightDeleteResponse
from ....types.cloudforce_one.threat_events.insight_update_response import InsightUpdateResponse

__all__ = ["InsightResource", "AsyncInsightResource"]


class InsightResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InsightResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return InsightResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsightResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return InsightResourceWithStreamingResponse(self)

    def update(
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
    ) -> InsightUpdateResponse:
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
        return self._post(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}/insight/{insight_id}",
            body=maybe_transform({"content": content}, insight_update_params.InsightUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InsightUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[InsightUpdateResponse], ResultWrapper[InsightUpdateResponse]),
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

    def creat(
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
    ) -> InsightCreatResponse:
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
            body=maybe_transform({"content": content}, insight_creat_params.InsightCreatParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InsightCreatResponse]._unwrapper,
            ),
            cast_to=cast(Type[InsightCreatResponse], ResultWrapper[InsightCreatResponse]),
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


class AsyncInsightResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInsightResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsightResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsightResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncInsightResourceWithStreamingResponse(self)

    async def update(
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
    ) -> InsightUpdateResponse:
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
        return await self._post(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}/insight/{insight_id}",
            body=await async_maybe_transform({"content": content}, insight_update_params.InsightUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InsightUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[InsightUpdateResponse], ResultWrapper[InsightUpdateResponse]),
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

    async def creat(
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
    ) -> InsightCreatResponse:
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
            body=await async_maybe_transform({"content": content}, insight_creat_params.InsightCreatParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InsightCreatResponse]._unwrapper,
            ),
            cast_to=cast(Type[InsightCreatResponse], ResultWrapper[InsightCreatResponse]),
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


class InsightResourceWithRawResponse:
    def __init__(self, insight: InsightResource) -> None:
        self._insight = insight

        self.update = to_raw_response_wrapper(
            insight.update,
        )
        self.delete = to_raw_response_wrapper(
            insight.delete,
        )
        self.creat = to_raw_response_wrapper(
            insight.creat,
        )
        self.get = to_raw_response_wrapper(
            insight.get,
        )


class AsyncInsightResourceWithRawResponse:
    def __init__(self, insight: AsyncInsightResource) -> None:
        self._insight = insight

        self.update = async_to_raw_response_wrapper(
            insight.update,
        )
        self.delete = async_to_raw_response_wrapper(
            insight.delete,
        )
        self.creat = async_to_raw_response_wrapper(
            insight.creat,
        )
        self.get = async_to_raw_response_wrapper(
            insight.get,
        )


class InsightResourceWithStreamingResponse:
    def __init__(self, insight: InsightResource) -> None:
        self._insight = insight

        self.update = to_streamed_response_wrapper(
            insight.update,
        )
        self.delete = to_streamed_response_wrapper(
            insight.delete,
        )
        self.creat = to_streamed_response_wrapper(
            insight.creat,
        )
        self.get = to_streamed_response_wrapper(
            insight.get,
        )


class AsyncInsightResourceWithStreamingResponse:
    def __init__(self, insight: AsyncInsightResource) -> None:
        self._insight = insight

        self.update = async_to_streamed_response_wrapper(
            insight.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            insight.delete,
        )
        self.creat = async_to_streamed_response_wrapper(
            insight.creat,
        )
        self.get = async_to_streamed_response_wrapper(
            insight.get,
        )
