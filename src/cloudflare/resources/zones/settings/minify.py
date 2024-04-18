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
from ....types.zones.settings import Minify, minify_edit_params

__all__ = ["MinifyResource", "AsyncMinifyResource"]


class MinifyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MinifyResourceWithRawResponse:
        return MinifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MinifyResourceWithStreamingResponse:
        return MinifyResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: minify_edit_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Minify]:
        """Automatically minify certain assets for your website.

        Refer to
        [Using Cloudflare Auto Minify](https://support.cloudflare.com/hc/en-us/articles/200168196)
        for more information.

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
            f"/zones/{zone_id}/settings/minify",
            body=maybe_transform({"value": value}, minify_edit_params.MinifyEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Minify]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Minify]], ResultWrapper[Minify]),
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
    ) -> Optional[Minify]:
        """Automatically minify certain assets for your website.

        Refer to
        [Using Cloudflare Auto Minify](https://support.cloudflare.com/hc/en-us/articles/200168196)
        for more information.

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
            f"/zones/{zone_id}/settings/minify",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Minify]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Minify]], ResultWrapper[Minify]),
        )


class AsyncMinifyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMinifyResourceWithRawResponse:
        return AsyncMinifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMinifyResourceWithStreamingResponse:
        return AsyncMinifyResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: minify_edit_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Minify]:
        """Automatically minify certain assets for your website.

        Refer to
        [Using Cloudflare Auto Minify](https://support.cloudflare.com/hc/en-us/articles/200168196)
        for more information.

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
            f"/zones/{zone_id}/settings/minify",
            body=await async_maybe_transform({"value": value}, minify_edit_params.MinifyEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Minify]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Minify]], ResultWrapper[Minify]),
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
    ) -> Optional[Minify]:
        """Automatically minify certain assets for your website.

        Refer to
        [Using Cloudflare Auto Minify](https://support.cloudflare.com/hc/en-us/articles/200168196)
        for more information.

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
            f"/zones/{zone_id}/settings/minify",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Minify]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Minify]], ResultWrapper[Minify]),
        )


class MinifyResourceWithRawResponse:
    def __init__(self, minify: MinifyResource) -> None:
        self._minify = minify

        self.edit = to_raw_response_wrapper(
            minify.edit,
        )
        self.get = to_raw_response_wrapper(
            minify.get,
        )


class AsyncMinifyResourceWithRawResponse:
    def __init__(self, minify: AsyncMinifyResource) -> None:
        self._minify = minify

        self.edit = async_to_raw_response_wrapper(
            minify.edit,
        )
        self.get = async_to_raw_response_wrapper(
            minify.get,
        )


class MinifyResourceWithStreamingResponse:
    def __init__(self, minify: MinifyResource) -> None:
        self._minify = minify

        self.edit = to_streamed_response_wrapper(
            minify.edit,
        )
        self.get = to_streamed_response_wrapper(
            minify.get,
        )


class AsyncMinifyResourceWithStreamingResponse:
    def __init__(self, minify: AsyncMinifyResource) -> None:
        self._minify = minify

        self.edit = async_to_streamed_response_wrapper(
            minify.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            minify.get,
        )
