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
from ....types.zones.settings import mobile_redirect_edit_params
from ....types.zones.settings.mobile_redirect import MobileRedirect

__all__ = ["MobileRedirectResource", "AsyncMobileRedirectResource"]


class MobileRedirectResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MobileRedirectResourceWithRawResponse:
        return MobileRedirectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MobileRedirectResourceWithStreamingResponse:
        return MobileRedirectResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: mobile_redirect_edit_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MobileRedirect]:
        """
        Automatically redirect visitors on mobile devices to a mobile-optimized
        subdomain. Refer to
        [Understanding Cloudflare Mobile Redirect](https://support.cloudflare.com/hc/articles/200168336)
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
            f"/zones/{zone_id}/settings/mobile_redirect",
            body=maybe_transform({"value": value}, mobile_redirect_edit_params.MobileRedirectEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MobileRedirect]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MobileRedirect]], ResultWrapper[MobileRedirect]),
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
    ) -> Optional[MobileRedirect]:
        """
        Automatically redirect visitors on mobile devices to a mobile-optimized
        subdomain. Refer to
        [Understanding Cloudflare Mobile Redirect](https://support.cloudflare.com/hc/articles/200168336)
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
            f"/zones/{zone_id}/settings/mobile_redirect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MobileRedirect]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MobileRedirect]], ResultWrapper[MobileRedirect]),
        )


class AsyncMobileRedirectResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMobileRedirectResourceWithRawResponse:
        return AsyncMobileRedirectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMobileRedirectResourceWithStreamingResponse:
        return AsyncMobileRedirectResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: mobile_redirect_edit_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MobileRedirect]:
        """
        Automatically redirect visitors on mobile devices to a mobile-optimized
        subdomain. Refer to
        [Understanding Cloudflare Mobile Redirect](https://support.cloudflare.com/hc/articles/200168336)
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
            f"/zones/{zone_id}/settings/mobile_redirect",
            body=await async_maybe_transform({"value": value}, mobile_redirect_edit_params.MobileRedirectEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MobileRedirect]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MobileRedirect]], ResultWrapper[MobileRedirect]),
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
    ) -> Optional[MobileRedirect]:
        """
        Automatically redirect visitors on mobile devices to a mobile-optimized
        subdomain. Refer to
        [Understanding Cloudflare Mobile Redirect](https://support.cloudflare.com/hc/articles/200168336)
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
            f"/zones/{zone_id}/settings/mobile_redirect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MobileRedirect]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MobileRedirect]], ResultWrapper[MobileRedirect]),
        )


class MobileRedirectResourceWithRawResponse:
    def __init__(self, mobile_redirect: MobileRedirectResource) -> None:
        self._mobile_redirect = mobile_redirect

        self.edit = to_raw_response_wrapper(
            mobile_redirect.edit,
        )
        self.get = to_raw_response_wrapper(
            mobile_redirect.get,
        )


class AsyncMobileRedirectResourceWithRawResponse:
    def __init__(self, mobile_redirect: AsyncMobileRedirectResource) -> None:
        self._mobile_redirect = mobile_redirect

        self.edit = async_to_raw_response_wrapper(
            mobile_redirect.edit,
        )
        self.get = async_to_raw_response_wrapper(
            mobile_redirect.get,
        )


class MobileRedirectResourceWithStreamingResponse:
    def __init__(self, mobile_redirect: MobileRedirectResource) -> None:
        self._mobile_redirect = mobile_redirect

        self.edit = to_streamed_response_wrapper(
            mobile_redirect.edit,
        )
        self.get = to_streamed_response_wrapper(
            mobile_redirect.get,
        )


class AsyncMobileRedirectResourceWithStreamingResponse:
    def __init__(self, mobile_redirect: AsyncMobileRedirectResource) -> None:
        self._mobile_redirect = mobile_redirect

        self.edit = async_to_streamed_response_wrapper(
            mobile_redirect.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            mobile_redirect.get,
        )
