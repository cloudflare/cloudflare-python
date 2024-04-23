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
from ....types.zones.settings import development_mode_edit_params
from ....types.zones.settings.development_mode import DevelopmentMode

__all__ = ["DevelopmentModeResource", "AsyncDevelopmentModeResource"]


class DevelopmentModeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DevelopmentModeResourceWithRawResponse:
        return DevelopmentModeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DevelopmentModeResourceWithStreamingResponse:
        return DevelopmentModeResourceWithStreamingResponse(self)

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
    ) -> Optional[DevelopmentMode]:
        """
        Development Mode temporarily allows you to enter development mode for your
        websites if you need to make changes to your site. This will bypass Cloudflare's
        accelerated cache and slow down your site, but is useful if you are making
        changes to cacheable content (like images, css, or JavaScript) and would like to
        see those changes right away. Once entered, development mode will last for 3
        hours and then automatically toggle off.

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
            f"/zones/{zone_id}/settings/development_mode",
            body=maybe_transform({"value": value}, development_mode_edit_params.DevelopmentModeEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DevelopmentMode]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DevelopmentMode]], ResultWrapper[DevelopmentMode]),
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
    ) -> Optional[DevelopmentMode]:
        """
        Development Mode temporarily allows you to enter development mode for your
        websites if you need to make changes to your site. This will bypass Cloudflare's
        accelerated cache and slow down your site, but is useful if you are making
        changes to cacheable content (like images, css, or JavaScript) and would like to
        see those changes right away. Once entered, development mode will last for 3
        hours and then automatically toggle off.

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
            f"/zones/{zone_id}/settings/development_mode",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DevelopmentMode]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DevelopmentMode]], ResultWrapper[DevelopmentMode]),
        )


class AsyncDevelopmentModeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDevelopmentModeResourceWithRawResponse:
        return AsyncDevelopmentModeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDevelopmentModeResourceWithStreamingResponse:
        return AsyncDevelopmentModeResourceWithStreamingResponse(self)

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
    ) -> Optional[DevelopmentMode]:
        """
        Development Mode temporarily allows you to enter development mode for your
        websites if you need to make changes to your site. This will bypass Cloudflare's
        accelerated cache and slow down your site, but is useful if you are making
        changes to cacheable content (like images, css, or JavaScript) and would like to
        see those changes right away. Once entered, development mode will last for 3
        hours and then automatically toggle off.

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
            f"/zones/{zone_id}/settings/development_mode",
            body=await async_maybe_transform({"value": value}, development_mode_edit_params.DevelopmentModeEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DevelopmentMode]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DevelopmentMode]], ResultWrapper[DevelopmentMode]),
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
    ) -> Optional[DevelopmentMode]:
        """
        Development Mode temporarily allows you to enter development mode for your
        websites if you need to make changes to your site. This will bypass Cloudflare's
        accelerated cache and slow down your site, but is useful if you are making
        changes to cacheable content (like images, css, or JavaScript) and would like to
        see those changes right away. Once entered, development mode will last for 3
        hours and then automatically toggle off.

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
            f"/zones/{zone_id}/settings/development_mode",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DevelopmentMode]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DevelopmentMode]], ResultWrapper[DevelopmentMode]),
        )


class DevelopmentModeResourceWithRawResponse:
    def __init__(self, development_mode: DevelopmentModeResource) -> None:
        self._development_mode = development_mode

        self.edit = to_raw_response_wrapper(
            development_mode.edit,
        )
        self.get = to_raw_response_wrapper(
            development_mode.get,
        )


class AsyncDevelopmentModeResourceWithRawResponse:
    def __init__(self, development_mode: AsyncDevelopmentModeResource) -> None:
        self._development_mode = development_mode

        self.edit = async_to_raw_response_wrapper(
            development_mode.edit,
        )
        self.get = async_to_raw_response_wrapper(
            development_mode.get,
        )


class DevelopmentModeResourceWithStreamingResponse:
    def __init__(self, development_mode: DevelopmentModeResource) -> None:
        self._development_mode = development_mode

        self.edit = to_streamed_response_wrapper(
            development_mode.edit,
        )
        self.get = to_streamed_response_wrapper(
            development_mode.get,
        )


class AsyncDevelopmentModeResourceWithStreamingResponse:
    def __init__(self, development_mode: AsyncDevelopmentModeResource) -> None:
        self._development_mode = development_mode

        self.edit = async_to_streamed_response_wrapper(
            development_mode.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            development_mode.get,
        )
