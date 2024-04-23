# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

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
from ....types.zones.settings import mirage_edit_params
from ....types.zones.settings.mirage import Mirage

__all__ = ["MirageResource", "AsyncMirageResource"]


class MirageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MirageResourceWithRawResponse:
        return MirageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MirageResourceWithStreamingResponse:
        return MirageResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Mirage]:
        """
        Automatically optimize image loading for website visitors on mobile devices.
        Refer to our
        [blog post](http://blog.cloudflare.com/mirage2-solving-mobile-speed) for more
        information.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/mirage",
            body=maybe_transform({"value": value}, mirage_edit_params.MirageEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Mirage]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Mirage]], ResultWrapper[Mirage]),
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
    ) -> Optional[Mirage]:
        """
        Automatically optimize image loading for website visitors on mobile devices.
        Refer to our
        [blog post](http://blog.cloudflare.com/mirage2-solving-mobile-speed) for more
        information.

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
            f"/zones/{zone_id}/settings/mirage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Mirage]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Mirage]], ResultWrapper[Mirage]),
        )


class AsyncMirageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMirageResourceWithRawResponse:
        return AsyncMirageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMirageResourceWithStreamingResponse:
        return AsyncMirageResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Mirage]:
        """
        Automatically optimize image loading for website visitors on mobile devices.
        Refer to our
        [blog post](http://blog.cloudflare.com/mirage2-solving-mobile-speed) for more
        information.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/mirage",
            body=await async_maybe_transform({"value": value}, mirage_edit_params.MirageEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Mirage]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Mirage]], ResultWrapper[Mirage]),
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
    ) -> Optional[Mirage]:
        """
        Automatically optimize image loading for website visitors on mobile devices.
        Refer to our
        [blog post](http://blog.cloudflare.com/mirage2-solving-mobile-speed) for more
        information.

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
            f"/zones/{zone_id}/settings/mirage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Mirage]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Mirage]], ResultWrapper[Mirage]),
        )


class MirageResourceWithRawResponse:
    def __init__(self, mirage: MirageResource) -> None:
        self._mirage = mirage

        self.edit = to_raw_response_wrapper(
            mirage.edit,
        )
        self.get = to_raw_response_wrapper(
            mirage.get,
        )


class AsyncMirageResourceWithRawResponse:
    def __init__(self, mirage: AsyncMirageResource) -> None:
        self._mirage = mirage

        self.edit = async_to_raw_response_wrapper(
            mirage.edit,
        )
        self.get = async_to_raw_response_wrapper(
            mirage.get,
        )


class MirageResourceWithStreamingResponse:
    def __init__(self, mirage: MirageResource) -> None:
        self._mirage = mirage

        self.edit = to_streamed_response_wrapper(
            mirage.edit,
        )
        self.get = to_streamed_response_wrapper(
            mirage.get,
        )


class AsyncMirageResourceWithStreamingResponse:
    def __init__(self, mirage: AsyncMirageResource) -> None:
        self._mirage = mirage

        self.edit = async_to_streamed_response_wrapper(
            mirage.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            mirage.get,
        )
