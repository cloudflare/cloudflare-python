# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ...._base_client import (
    make_request_options,
)
from ....types.zones.settings import OrangeToOrange, orange_to_orange_edit_params
from ....types.zones.settings.orange_to_orange import OrangeToOrange
from ....types.zones.settings.orange_to_orange_param import OrangeToOrangeParam

__all__ = ["OrangeToOrangeResource", "AsyncOrangeToOrangeResource"]


class OrangeToOrangeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrangeToOrangeResourceWithRawResponse:
        return OrangeToOrangeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrangeToOrangeResourceWithStreamingResponse:
        return OrangeToOrangeResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: OrangeToOrangeParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OrangeToOrange]:
        """
        Orange to Orange (O2O) allows zones on Cloudflare to CNAME to other zones also
        on Cloudflare.

        Args:
          zone_id: Identifier

          value: Orange to Orange (O2O) allows zones on Cloudflare to CNAME to other zones also
              on Cloudflare.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/orange_to_orange",
            body=maybe_transform({"value": value}, orange_to_orange_edit_params.OrangeToOrangeEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OrangeToOrange]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OrangeToOrange]], ResultWrapper[OrangeToOrange]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OrangeToOrange]:
        """
        Orange to Orange (O2O) allows zones on Cloudflare to CNAME to other zones also
        on Cloudflare.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/orange_to_orange",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OrangeToOrange]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OrangeToOrange]], ResultWrapper[OrangeToOrange]),
        )


class AsyncOrangeToOrangeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrangeToOrangeResourceWithRawResponse:
        return AsyncOrangeToOrangeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrangeToOrangeResourceWithStreamingResponse:
        return AsyncOrangeToOrangeResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: OrangeToOrangeParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OrangeToOrange]:
        """
        Orange to Orange (O2O) allows zones on Cloudflare to CNAME to other zones also
        on Cloudflare.

        Args:
          zone_id: Identifier

          value: Orange to Orange (O2O) allows zones on Cloudflare to CNAME to other zones also
              on Cloudflare.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/orange_to_orange",
            body=await async_maybe_transform({"value": value}, orange_to_orange_edit_params.OrangeToOrangeEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OrangeToOrange]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OrangeToOrange]], ResultWrapper[OrangeToOrange]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OrangeToOrange]:
        """
        Orange to Orange (O2O) allows zones on Cloudflare to CNAME to other zones also
        on Cloudflare.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/orange_to_orange",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OrangeToOrange]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OrangeToOrange]], ResultWrapper[OrangeToOrange]),
        )


class OrangeToOrangeResourceWithRawResponse:
    def __init__(self, orange_to_orange: OrangeToOrangeResource) -> None:
        self._orange_to_orange = orange_to_orange

        self.edit = to_raw_response_wrapper(
            orange_to_orange.edit,
        )
        self.get = to_raw_response_wrapper(
            orange_to_orange.get,
        )


class AsyncOrangeToOrangeResourceWithRawResponse:
    def __init__(self, orange_to_orange: AsyncOrangeToOrangeResource) -> None:
        self._orange_to_orange = orange_to_orange

        self.edit = async_to_raw_response_wrapper(
            orange_to_orange.edit,
        )
        self.get = async_to_raw_response_wrapper(
            orange_to_orange.get,
        )


class OrangeToOrangeResourceWithStreamingResponse:
    def __init__(self, orange_to_orange: OrangeToOrangeResource) -> None:
        self._orange_to_orange = orange_to_orange

        self.edit = to_streamed_response_wrapper(
            orange_to_orange.edit,
        )
        self.get = to_streamed_response_wrapper(
            orange_to_orange.get,
        )


class AsyncOrangeToOrangeResourceWithStreamingResponse:
    def __init__(self, orange_to_orange: AsyncOrangeToOrangeResource) -> None:
        self._orange_to_orange = orange_to_orange

        self.edit = async_to_streamed_response_wrapper(
            orange_to_orange.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            orange_to_orange.get,
        )
