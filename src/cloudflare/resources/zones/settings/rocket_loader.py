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
from ....types.zones.settings import ZonesRocketLoader, ZonesRocketLoaderParam, rocket_loader_edit_params

__all__ = ["RocketLoader", "AsyncRocketLoader"]


class RocketLoader(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RocketLoaderWithRawResponse:
        return RocketLoaderWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RocketLoaderWithStreamingResponse:
        return RocketLoaderWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: ZonesRocketLoaderParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesRocketLoader]:
        """
        Rocket Loader is a general-purpose asynchronous JavaScript optimisation that
        prioritises rendering your content while loading your site's Javascript
        asynchronously. Turning on Rocket Loader will immediately improve a web page's
        rendering time sometimes measured as Time to First Paint (TTFP), and also the
        `window.onload` time (assuming there is JavaScript on the page). This can have a
        positive impact on your Google search ranking. When turned on, Rocket Loader
        will automatically defer the loading of all Javascript referenced in your HTML,
        with no configuration required. Refer to
        [Understanding Rocket Loader](https://support.cloudflare.com/hc/articles/200168056)
        for more information.

        Args:
          zone_id: Identifier

          value: Rocket Loader is a general-purpose asynchronous JavaScript optimisation that
              prioritises rendering your content while loading your site's Javascript
              asynchronously. Turning on Rocket Loader will immediately improve a web page's
              rendering time sometimes measured as Time to First Paint (TTFP), and also the
              `window.onload` time (assuming there is JavaScript on the page). This can have a
              positive impact on your Google search ranking. When turned on, Rocket Loader
              will automatically defer the loading of all Javascript referenced in your HTML,
              with no configuration required. Refer to
              [Understanding Rocket Loader](https://support.cloudflare.com/hc/articles/200168056)
              for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/rocket_loader",
            body=maybe_transform({"value": value}, rocket_loader_edit_params.RocketLoaderEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesRocketLoader]], ResultWrapper[ZonesRocketLoader]),
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
    ) -> Optional[ZonesRocketLoader]:
        """
        Rocket Loader is a general-purpose asynchronous JavaScript optimisation that
        prioritises rendering your content while loading your site's Javascript
        asynchronously. Turning on Rocket Loader will immediately improve a web page's
        rendering time sometimes measured as Time to First Paint (TTFP), and also the
        `window.onload` time (assuming there is JavaScript on the page). This can have a
        positive impact on your Google search ranking. When turned on, Rocket Loader
        will automatically defer the loading of all Javascript referenced in your HTML,
        with no configuration required. Refer to
        [Understanding Rocket Loader](https://support.cloudflare.com/hc/articles/200168056)
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
            f"/zones/{zone_id}/settings/rocket_loader",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesRocketLoader]], ResultWrapper[ZonesRocketLoader]),
        )


class AsyncRocketLoader(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRocketLoaderWithRawResponse:
        return AsyncRocketLoaderWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRocketLoaderWithStreamingResponse:
        return AsyncRocketLoaderWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: ZonesRocketLoaderParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesRocketLoader]:
        """
        Rocket Loader is a general-purpose asynchronous JavaScript optimisation that
        prioritises rendering your content while loading your site's Javascript
        asynchronously. Turning on Rocket Loader will immediately improve a web page's
        rendering time sometimes measured as Time to First Paint (TTFP), and also the
        `window.onload` time (assuming there is JavaScript on the page). This can have a
        positive impact on your Google search ranking. When turned on, Rocket Loader
        will automatically defer the loading of all Javascript referenced in your HTML,
        with no configuration required. Refer to
        [Understanding Rocket Loader](https://support.cloudflare.com/hc/articles/200168056)
        for more information.

        Args:
          zone_id: Identifier

          value: Rocket Loader is a general-purpose asynchronous JavaScript optimisation that
              prioritises rendering your content while loading your site's Javascript
              asynchronously. Turning on Rocket Loader will immediately improve a web page's
              rendering time sometimes measured as Time to First Paint (TTFP), and also the
              `window.onload` time (assuming there is JavaScript on the page). This can have a
              positive impact on your Google search ranking. When turned on, Rocket Loader
              will automatically defer the loading of all Javascript referenced in your HTML,
              with no configuration required. Refer to
              [Understanding Rocket Loader](https://support.cloudflare.com/hc/articles/200168056)
              for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/rocket_loader",
            body=await async_maybe_transform({"value": value}, rocket_loader_edit_params.RocketLoaderEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesRocketLoader]], ResultWrapper[ZonesRocketLoader]),
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
    ) -> Optional[ZonesRocketLoader]:
        """
        Rocket Loader is a general-purpose asynchronous JavaScript optimisation that
        prioritises rendering your content while loading your site's Javascript
        asynchronously. Turning on Rocket Loader will immediately improve a web page's
        rendering time sometimes measured as Time to First Paint (TTFP), and also the
        `window.onload` time (assuming there is JavaScript on the page). This can have a
        positive impact on your Google search ranking. When turned on, Rocket Loader
        will automatically defer the loading of all Javascript referenced in your HTML,
        with no configuration required. Refer to
        [Understanding Rocket Loader](https://support.cloudflare.com/hc/articles/200168056)
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
            f"/zones/{zone_id}/settings/rocket_loader",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesRocketLoader]], ResultWrapper[ZonesRocketLoader]),
        )


class RocketLoaderWithRawResponse:
    def __init__(self, rocket_loader: RocketLoader) -> None:
        self._rocket_loader = rocket_loader

        self.edit = to_raw_response_wrapper(
            rocket_loader.edit,
        )
        self.get = to_raw_response_wrapper(
            rocket_loader.get,
        )


class AsyncRocketLoaderWithRawResponse:
    def __init__(self, rocket_loader: AsyncRocketLoader) -> None:
        self._rocket_loader = rocket_loader

        self.edit = async_to_raw_response_wrapper(
            rocket_loader.edit,
        )
        self.get = async_to_raw_response_wrapper(
            rocket_loader.get,
        )


class RocketLoaderWithStreamingResponse:
    def __init__(self, rocket_loader: RocketLoader) -> None:
        self._rocket_loader = rocket_loader

        self.edit = to_streamed_response_wrapper(
            rocket_loader.edit,
        )
        self.get = to_streamed_response_wrapper(
            rocket_loader.get,
        )


class AsyncRocketLoaderWithStreamingResponse:
    def __init__(self, rocket_loader: AsyncRocketLoader) -> None:
        self._rocket_loader = rocket_loader

        self.edit = async_to_streamed_response_wrapper(
            rocket_loader.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            rocket_loader.get,
        )
