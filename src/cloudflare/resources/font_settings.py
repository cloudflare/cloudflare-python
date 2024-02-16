# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types import FontSettingUpdateResponse, FontSettingGetResponse

from typing import Type, Optional

from typing_extensions import Literal

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import font_setting_update_params
from .._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["FontSettings", "AsyncFontSettings"]


class FontSettings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FontSettingsWithRawResponse:
        return FontSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FontSettingsWithStreamingResponse:
        return FontSettingsWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FontSettingUpdateResponse]:
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
            body=maybe_transform({"value": value}, font_setting_update_params.FontSettingUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FontSettingUpdateResponse]], ResultWrapper[FontSettingUpdateResponse]),
        )

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FontSettingGetResponse]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FontSettingGetResponse]], ResultWrapper[FontSettingGetResponse]),
        )


class AsyncFontSettings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFontSettingsWithRawResponse:
        return AsyncFontSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFontSettingsWithStreamingResponse:
        return AsyncFontSettingsWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FontSettingUpdateResponse]:
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
            body=maybe_transform({"value": value}, font_setting_update_params.FontSettingUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FontSettingUpdateResponse]], ResultWrapper[FontSettingUpdateResponse]),
        )

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FontSettingGetResponse]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[FontSettingGetResponse]], ResultWrapper[FontSettingGetResponse]),
        )


class FontSettingsWithRawResponse:
    def __init__(self, font_settings: FontSettings) -> None:
        self._font_settings = font_settings

        self.update = to_raw_response_wrapper(
            font_settings.update,
        )
        self.get = to_raw_response_wrapper(
            font_settings.get,
        )


class AsyncFontSettingsWithRawResponse:
    def __init__(self, font_settings: AsyncFontSettings) -> None:
        self._font_settings = font_settings

        self.update = async_to_raw_response_wrapper(
            font_settings.update,
        )
        self.get = async_to_raw_response_wrapper(
            font_settings.get,
        )


class FontSettingsWithStreamingResponse:
    def __init__(self, font_settings: FontSettings) -> None:
        self._font_settings = font_settings

        self.update = to_streamed_response_wrapper(
            font_settings.update,
        )
        self.get = to_streamed_response_wrapper(
            font_settings.get,
        )


class AsyncFontSettingsWithStreamingResponse:
    def __init__(self, font_settings: AsyncFontSettings) -> None:
        self._font_settings = font_settings

        self.update = async_to_streamed_response_wrapper(
            font_settings.update,
        )
        self.get = async_to_streamed_response_wrapper(
            font_settings.get,
        )
