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
from ....types.zones.settings import font_setting_edit_params
from ....types.zones.settings.font_settings import FontSettings

__all__ = ["FontSettingsResource", "AsyncFontSettingsResource"]


class FontSettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FontSettingsResourceWithRawResponse:
        return FontSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FontSettingsResourceWithStreamingResponse:
        return FontSettingsResourceWithStreamingResponse(self)

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
    ) -> Optional[FontSettings]:
        """Enhance your website's font delivery with Cloudflare Fonts.

        Deliver Google
        Hosted fonts from your own domain, boost performance, and enhance user privacy.
        Refer to the Cloudflare Fonts documentation for more information.

        Args:
          zone_id: Identifier

          value: Whether the feature is enabled or disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/fonts",
            body=maybe_transform({"value": value}, font_setting_edit_params.FontSettingEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FontSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FontSettings]], ResultWrapper[FontSettings]),
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
    ) -> Optional[FontSettings]:
        """Enhance your website's font delivery with Cloudflare Fonts.

        Deliver Google
        Hosted fonts from your own domain, boost performance, and enhance user privacy.
        Refer to the Cloudflare Fonts documentation for more information.

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
            f"/zones/{zone_id}/settings/fonts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FontSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FontSettings]], ResultWrapper[FontSettings]),
        )


class AsyncFontSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFontSettingsResourceWithRawResponse:
        return AsyncFontSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFontSettingsResourceWithStreamingResponse:
        return AsyncFontSettingsResourceWithStreamingResponse(self)

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
    ) -> Optional[FontSettings]:
        """Enhance your website's font delivery with Cloudflare Fonts.

        Deliver Google
        Hosted fonts from your own domain, boost performance, and enhance user privacy.
        Refer to the Cloudflare Fonts documentation for more information.

        Args:
          zone_id: Identifier

          value: Whether the feature is enabled or disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/fonts",
            body=await async_maybe_transform({"value": value}, font_setting_edit_params.FontSettingEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FontSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FontSettings]], ResultWrapper[FontSettings]),
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
    ) -> Optional[FontSettings]:
        """Enhance your website's font delivery with Cloudflare Fonts.

        Deliver Google
        Hosted fonts from your own domain, boost performance, and enhance user privacy.
        Refer to the Cloudflare Fonts documentation for more information.

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
            f"/zones/{zone_id}/settings/fonts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FontSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FontSettings]], ResultWrapper[FontSettings]),
        )


class FontSettingsResourceWithRawResponse:
    def __init__(self, font_settings: FontSettingsResource) -> None:
        self._font_settings = font_settings

        self.edit = to_raw_response_wrapper(
            font_settings.edit,
        )
        self.get = to_raw_response_wrapper(
            font_settings.get,
        )


class AsyncFontSettingsResourceWithRawResponse:
    def __init__(self, font_settings: AsyncFontSettingsResource) -> None:
        self._font_settings = font_settings

        self.edit = async_to_raw_response_wrapper(
            font_settings.edit,
        )
        self.get = async_to_raw_response_wrapper(
            font_settings.get,
        )


class FontSettingsResourceWithStreamingResponse:
    def __init__(self, font_settings: FontSettingsResource) -> None:
        self._font_settings = font_settings

        self.edit = to_streamed_response_wrapper(
            font_settings.edit,
        )
        self.get = to_streamed_response_wrapper(
            font_settings.get,
        )


class AsyncFontSettingsResourceWithStreamingResponse:
    def __init__(self, font_settings: AsyncFontSettingsResource) -> None:
        self._font_settings = font_settings

        self.edit = async_to_streamed_response_wrapper(
            font_settings.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            font_settings.get,
        )
