# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import WebpUpdateResponse, WebpGetResponse

from typing import Type, Optional

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.settings import webp_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Webp", "AsyncWebp"]


class Webp(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebpWithRawResponse:
        return WebpWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebpWithStreamingResponse:
        return WebpWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WebpUpdateResponse]:
        """
        When the client requesting the image supports the WebP image codec, and WebP
        offers a performance advantage over the original image format, Cloudflare will
        serve a WebP version of the original image.

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
            f"/zones/{zone_id}/settings/webp",
            body=maybe_transform({"value": value}, webp_update_params.WebpUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WebpUpdateResponse]], ResultWrapper[WebpUpdateResponse]),
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
    ) -> Optional[WebpGetResponse]:
        """
        When the client requesting the image supports the WebP image codec, and WebP
        offers a performance advantage over the original image format, Cloudflare will
        serve a WebP version of the original image.

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
            f"/zones/{zone_id}/settings/webp",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WebpGetResponse]], ResultWrapper[WebpGetResponse]),
        )


class AsyncWebp(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebpWithRawResponse:
        return AsyncWebpWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebpWithStreamingResponse:
        return AsyncWebpWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WebpUpdateResponse]:
        """
        When the client requesting the image supports the WebP image codec, and WebP
        offers a performance advantage over the original image format, Cloudflare will
        serve a WebP version of the original image.

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
            f"/zones/{zone_id}/settings/webp",
            body=maybe_transform({"value": value}, webp_update_params.WebpUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WebpUpdateResponse]], ResultWrapper[WebpUpdateResponse]),
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
    ) -> Optional[WebpGetResponse]:
        """
        When the client requesting the image supports the WebP image codec, and WebP
        offers a performance advantage over the original image format, Cloudflare will
        serve a WebP version of the original image.

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
            f"/zones/{zone_id}/settings/webp",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WebpGetResponse]], ResultWrapper[WebpGetResponse]),
        )


class WebpWithRawResponse:
    def __init__(self, webp: Webp) -> None:
        self._webp = webp

        self.update = to_raw_response_wrapper(
            webp.update,
        )
        self.get = to_raw_response_wrapper(
            webp.get,
        )


class AsyncWebpWithRawResponse:
    def __init__(self, webp: AsyncWebp) -> None:
        self._webp = webp

        self.update = async_to_raw_response_wrapper(
            webp.update,
        )
        self.get = async_to_raw_response_wrapper(
            webp.get,
        )


class WebpWithStreamingResponse:
    def __init__(self, webp: Webp) -> None:
        self._webp = webp

        self.update = to_streamed_response_wrapper(
            webp.update,
        )
        self.get = to_streamed_response_wrapper(
            webp.get,
        )


class AsyncWebpWithStreamingResponse:
    def __init__(self, webp: AsyncWebp) -> None:
        self._webp = webp

        self.update = async_to_streamed_response_wrapper(
            webp.update,
        )
        self.get = async_to_streamed_response_wrapper(
            webp.get,
        )
