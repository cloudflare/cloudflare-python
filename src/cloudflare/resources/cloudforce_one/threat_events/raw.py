# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...._base_client import make_request_options
from ....types.cloudforce_one.threat_events import raw_edit_params
from ....types.cloudforce_one.threat_events.raw_get_response import RawGetResponse
from ....types.cloudforce_one.threat_events.raw_edit_response import RawEditResponse

__all__ = ["RawResource", "AsyncRawResource"]


class RawResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RawResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RawResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RawResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RawResourceWithStreamingResponse(self)

    def edit(
        self,
        raw_id: str,
        *,
        account_id: float,
        event_id: str,
        data: object | NotGiven = NOT_GIVEN,
        source: str | NotGiven = NOT_GIVEN,
        tlp: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RawEditResponse:
        """
        Updates a raw event

        Args:
          account_id: Account ID

          event_id: Event UUID

          raw_id: Raw Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        if not raw_id:
            raise ValueError(f"Expected a non-empty value for `raw_id` but received {raw_id!r}")
        return self._patch(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}/raw/{raw_id}",
            body=maybe_transform(
                {
                    "data": data,
                    "source": source,
                    "tlp": tlp,
                },
                raw_edit_params.RawEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RawEditResponse,
        )

    def get(
        self,
        raw_id: str,
        *,
        account_id: float,
        event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RawGetResponse:
        """
        Reads data for a raw event

        Args:
          account_id: Account ID

          event_id: Event UUID

          raw_id: Raw Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        if not raw_id:
            raise ValueError(f"Expected a non-empty value for `raw_id` but received {raw_id!r}")
        return self._get(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}/raw/{raw_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RawGetResponse,
        )


class AsyncRawResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRawResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRawResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRawResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRawResourceWithStreamingResponse(self)

    async def edit(
        self,
        raw_id: str,
        *,
        account_id: float,
        event_id: str,
        data: object | NotGiven = NOT_GIVEN,
        source: str | NotGiven = NOT_GIVEN,
        tlp: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RawEditResponse:
        """
        Updates a raw event

        Args:
          account_id: Account ID

          event_id: Event UUID

          raw_id: Raw Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        if not raw_id:
            raise ValueError(f"Expected a non-empty value for `raw_id` but received {raw_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}/raw/{raw_id}",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "source": source,
                    "tlp": tlp,
                },
                raw_edit_params.RawEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RawEditResponse,
        )

    async def get(
        self,
        raw_id: str,
        *,
        account_id: float,
        event_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RawGetResponse:
        """
        Reads data for a raw event

        Args:
          account_id: Account ID

          event_id: Event UUID

          raw_id: Raw Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        if not raw_id:
            raise ValueError(f"Expected a non-empty value for `raw_id` but received {raw_id!r}")
        return await self._get(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}/raw/{raw_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RawGetResponse,
        )


class RawResourceWithRawResponse:
    def __init__(self, raw: RawResource) -> None:
        self._raw = raw

        self.edit = to_raw_response_wrapper(
            raw.edit,
        )
        self.get = to_raw_response_wrapper(
            raw.get,
        )


class AsyncRawResourceWithRawResponse:
    def __init__(self, raw: AsyncRawResource) -> None:
        self._raw = raw

        self.edit = async_to_raw_response_wrapper(
            raw.edit,
        )
        self.get = async_to_raw_response_wrapper(
            raw.get,
        )


class RawResourceWithStreamingResponse:
    def __init__(self, raw: RawResource) -> None:
        self._raw = raw

        self.edit = to_streamed_response_wrapper(
            raw.edit,
        )
        self.get = to_streamed_response_wrapper(
            raw.get,
        )


class AsyncRawResourceWithStreamingResponse:
    def __init__(self, raw: AsyncRawResource) -> None:
        self._raw = raw

        self.edit = async_to_streamed_response_wrapper(
            raw.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            raw.get,
        )
