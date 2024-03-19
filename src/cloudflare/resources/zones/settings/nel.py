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
from ....types.zones.settings import ZonesNEL, ZonesNELParam, nel_edit_params

__all__ = ["NEL", "AsyncNEL"]


class NEL(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NELWithRawResponse:
        return NELWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NELWithStreamingResponse:
        return NELWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: ZonesNELParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesNEL]:
        """
        Automatically optimize image loading for website visitors on mobile devices.
        Refer to our [blog post](http://blog.cloudflare.com/nel-solving-mobile-speed)
        for more information.

        Args:
          zone_id: Identifier

          value: Enable Network Error Logging reporting on your zone. (Beta)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/nel",
            body=maybe_transform({"value": value}, nel_edit_params.NELEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesNEL]], ResultWrapper[ZonesNEL]),
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
    ) -> Optional[ZonesNEL]:
        """Enable Network Error Logging reporting on your zone.

        (Beta)

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
            f"/zones/{zone_id}/settings/nel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesNEL]], ResultWrapper[ZonesNEL]),
        )


class AsyncNEL(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNELWithRawResponse:
        return AsyncNELWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNELWithStreamingResponse:
        return AsyncNELWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: ZonesNELParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesNEL]:
        """
        Automatically optimize image loading for website visitors on mobile devices.
        Refer to our [blog post](http://blog.cloudflare.com/nel-solving-mobile-speed)
        for more information.

        Args:
          zone_id: Identifier

          value: Enable Network Error Logging reporting on your zone. (Beta)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/nel",
            body=await async_maybe_transform({"value": value}, nel_edit_params.NELEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesNEL]], ResultWrapper[ZonesNEL]),
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
    ) -> Optional[ZonesNEL]:
        """Enable Network Error Logging reporting on your zone.

        (Beta)

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
            f"/zones/{zone_id}/settings/nel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesNEL]], ResultWrapper[ZonesNEL]),
        )


class NELWithRawResponse:
    def __init__(self, nel: NEL) -> None:
        self._nel = nel

        self.edit = to_raw_response_wrapper(
            nel.edit,
        )
        self.get = to_raw_response_wrapper(
            nel.get,
        )


class AsyncNELWithRawResponse:
    def __init__(self, nel: AsyncNEL) -> None:
        self._nel = nel

        self.edit = async_to_raw_response_wrapper(
            nel.edit,
        )
        self.get = async_to_raw_response_wrapper(
            nel.get,
        )


class NELWithStreamingResponse:
    def __init__(self, nel: NEL) -> None:
        self._nel = nel

        self.edit = to_streamed_response_wrapper(
            nel.edit,
        )
        self.get = to_streamed_response_wrapper(
            nel.get,
        )


class AsyncNELWithStreamingResponse:
    def __init__(self, nel: AsyncNEL) -> None:
        self._nel = nel

        self.edit = async_to_streamed_response_wrapper(
            nel.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            nel.get,
        )
