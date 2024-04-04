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
from ....types.zones.settings import RocketLoader, RocketLoaderParam, rocket_loader_edit_params

__all__ = ["RocketLoaderResource", "AsyncRocketLoaderResource"]


class RocketLoaderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RocketLoaderResourceWithRawResponse:
        return RocketLoaderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RocketLoaderResourceWithStreamingResponse:
        return RocketLoaderResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: RocketLoaderParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RocketLoader]:
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
            cast_to=cast(Type[Optional[RocketLoader]], ResultWrapper[RocketLoader]),
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
    ) -> Optional[RocketLoader]:
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
            cast_to=cast(Type[Optional[RocketLoader]], ResultWrapper[RocketLoader]),
        )


class AsyncRocketLoaderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRocketLoaderResourceWithRawResponse:
        return AsyncRocketLoaderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRocketLoaderResourceWithStreamingResponse:
        return AsyncRocketLoaderResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: RocketLoaderParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RocketLoader]:
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
            cast_to=cast(Type[Optional[RocketLoader]], ResultWrapper[RocketLoader]),
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
    ) -> Optional[RocketLoader]:
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
            cast_to=cast(Type[Optional[RocketLoader]], ResultWrapper[RocketLoader]),
        )


class RocketLoaderResourceWithRawResponse:
    def __init__(self, rocket_loader: RocketLoaderResource) -> None:
        self._rocket_loader = rocket_loader

        self.edit = to_raw_response_wrapper(
            rocket_loader.edit,
        )
        self.get = to_raw_response_wrapper(
            rocket_loader.get,
        )


class AsyncRocketLoaderResourceWithRawResponse:
    def __init__(self, rocket_loader: AsyncRocketLoaderResource) -> None:
        self._rocket_loader = rocket_loader

        self.edit = async_to_raw_response_wrapper(
            rocket_loader.edit,
        )
        self.get = async_to_raw_response_wrapper(
            rocket_loader.get,
        )


class RocketLoaderResourceWithStreamingResponse:
    def __init__(self, rocket_loader: RocketLoaderResource) -> None:
        self._rocket_loader = rocket_loader

        self.edit = to_streamed_response_wrapper(
            rocket_loader.edit,
        )
        self.get = to_streamed_response_wrapper(
            rocket_loader.get,
        )


class AsyncRocketLoaderResourceWithStreamingResponse:
    def __init__(self, rocket_loader: AsyncRocketLoaderResource) -> None:
        self._rocket_loader = rocket_loader

        self.edit = async_to_streamed_response_wrapper(
            rocket_loader.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            rocket_loader.get,
        )
