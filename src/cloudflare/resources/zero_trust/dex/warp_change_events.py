# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
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
from ....types.zero_trust.dex import warp_change_event_get_params
from ....types.zero_trust.dex.warp_change_event_get_response import WARPChangeEventGetResponse

__all__ = ["WARPChangeEventsResource", "AsyncWARPChangeEventsResource"]


class WARPChangeEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WARPChangeEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return WARPChangeEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WARPChangeEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return WARPChangeEventsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        from_: str,
        page: float,
        per_page: float,
        to: str,
        account_name: str | NotGiven = NOT_GIVEN,
        config_name: str | NotGiven = NOT_GIVEN,
        sort_order: Literal["ASC", "DESC"] | NotGiven = NOT_GIVEN,
        toggle: Literal["on", "off"] | NotGiven = NOT_GIVEN,
        type: Literal["config", "toggle"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WARPChangeEventGetResponse]:
        """
        List WARP configuration and enablement toggle change events by device.

        Args:
          from_: Start time for the query in ISO (RFC3339 - ISO 8601) format

          page: Page number of paginated results

          per_page: Number of items per page

          to: End time for the query in ISO (RFC3339 - ISO 8601) format

          account_name: Filter events by account name.

          config_name: Filter events by WARP configuration name changed from or to. Applicable to
              type='config' events only.

          sort_order: Sort response by event timestamp.

          toggle: Filter events by type toggle value. Applicable to type='toggle' events only.

          type: Filter events by type 'config' or 'toggle'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/dex/warp-change-events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "page": page,
                        "per_page": per_page,
                        "to": to,
                        "account_name": account_name,
                        "config_name": config_name,
                        "sort_order": sort_order,
                        "toggle": toggle,
                        "type": type,
                    },
                    warp_change_event_get_params.WARPChangeEventGetParams,
                ),
                post_parser=ResultWrapper[Optional[WARPChangeEventGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[WARPChangeEventGetResponse]], ResultWrapper[WARPChangeEventGetResponse]),
        )


class AsyncWARPChangeEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWARPChangeEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWARPChangeEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWARPChangeEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncWARPChangeEventsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        from_: str,
        page: float,
        per_page: float,
        to: str,
        account_name: str | NotGiven = NOT_GIVEN,
        config_name: str | NotGiven = NOT_GIVEN,
        sort_order: Literal["ASC", "DESC"] | NotGiven = NOT_GIVEN,
        toggle: Literal["on", "off"] | NotGiven = NOT_GIVEN,
        type: Literal["config", "toggle"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WARPChangeEventGetResponse]:
        """
        List WARP configuration and enablement toggle change events by device.

        Args:
          from_: Start time for the query in ISO (RFC3339 - ISO 8601) format

          page: Page number of paginated results

          per_page: Number of items per page

          to: End time for the query in ISO (RFC3339 - ISO 8601) format

          account_name: Filter events by account name.

          config_name: Filter events by WARP configuration name changed from or to. Applicable to
              type='config' events only.

          sort_order: Sort response by event timestamp.

          toggle: Filter events by type toggle value. Applicable to type='toggle' events only.

          type: Filter events by type 'config' or 'toggle'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dex/warp-change-events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "page": page,
                        "per_page": per_page,
                        "to": to,
                        "account_name": account_name,
                        "config_name": config_name,
                        "sort_order": sort_order,
                        "toggle": toggle,
                        "type": type,
                    },
                    warp_change_event_get_params.WARPChangeEventGetParams,
                ),
                post_parser=ResultWrapper[Optional[WARPChangeEventGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[WARPChangeEventGetResponse]], ResultWrapper[WARPChangeEventGetResponse]),
        )


class WARPChangeEventsResourceWithRawResponse:
    def __init__(self, warp_change_events: WARPChangeEventsResource) -> None:
        self._warp_change_events = warp_change_events

        self.get = to_raw_response_wrapper(
            warp_change_events.get,
        )


class AsyncWARPChangeEventsResourceWithRawResponse:
    def __init__(self, warp_change_events: AsyncWARPChangeEventsResource) -> None:
        self._warp_change_events = warp_change_events

        self.get = async_to_raw_response_wrapper(
            warp_change_events.get,
        )


class WARPChangeEventsResourceWithStreamingResponse:
    def __init__(self, warp_change_events: WARPChangeEventsResource) -> None:
        self._warp_change_events = warp_change_events

        self.get = to_streamed_response_wrapper(
            warp_change_events.get,
        )


class AsyncWARPChangeEventsResourceWithStreamingResponse:
    def __init__(self, warp_change_events: AsyncWARPChangeEventsResource) -> None:
        self._warp_change_events = warp_change_events

        self.get = async_to_streamed_response_wrapper(
            warp_change_events.get,
        )
