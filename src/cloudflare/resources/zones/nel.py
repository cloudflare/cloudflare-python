# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.zones import nel_edit_params
from ..._base_client import make_request_options
from ...types.zones.setting import Setting

__all__ = ["NELResource", "AsyncNELResource"]


class NELResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NELResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return NELResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NELResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return NELResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: nel_edit_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Setting:
        """Updates the Network Error Logging (NEL) setting for a zone.

        Requires the NEL
        product feature to be enabled for the zone. The setting controls whether
        browsers report network errors to Cloudflare's NEL endpoint.

        Args:
          zone_id: Identifier of the zone.

          value: The NEL configuration value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            path_template("/zones/{zone_id}/settings/nel", zone_id=zone_id),
            body=maybe_transform({"value": value}, nel_edit_params.NELEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Setting]._unwrapper,
            ),
            cast_to=cast(Type[Setting], ResultWrapper[Setting]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Setting:
        """Fetches the Network Error Logging (NEL) setting for a zone.

        NEL allows browsers
        to report network errors to a configured endpoint. The setting is enabled by
        default for free and pro zones, and disabled by default for business and
        enterprise zones unless the NEL product feature is enabled.

        Args:
          zone_id: Identifier of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/settings/nel", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Setting]._unwrapper,
            ),
            cast_to=cast(Type[Setting], ResultWrapper[Setting]),
        )


class AsyncNELResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNELResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNELResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNELResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncNELResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: nel_edit_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Setting:
        """Updates the Network Error Logging (NEL) setting for a zone.

        Requires the NEL
        product feature to be enabled for the zone. The setting controls whether
        browsers report network errors to Cloudflare's NEL endpoint.

        Args:
          zone_id: Identifier of the zone.

          value: The NEL configuration value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            path_template("/zones/{zone_id}/settings/nel", zone_id=zone_id),
            body=await async_maybe_transform({"value": value}, nel_edit_params.NELEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Setting]._unwrapper,
            ),
            cast_to=cast(Type[Setting], ResultWrapper[Setting]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Setting:
        """Fetches the Network Error Logging (NEL) setting for a zone.

        NEL allows browsers
        to report network errors to a configured endpoint. The setting is enabled by
        default for free and pro zones, and disabled by default for business and
        enterprise zones unless the NEL product feature is enabled.

        Args:
          zone_id: Identifier of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/settings/nel", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Setting]._unwrapper,
            ),
            cast_to=cast(Type[Setting], ResultWrapper[Setting]),
        )


class NELResourceWithRawResponse:
    def __init__(self, nel: NELResource) -> None:
        self._nel = nel

        self.edit = to_raw_response_wrapper(
            nel.edit,
        )
        self.get = to_raw_response_wrapper(
            nel.get,
        )


class AsyncNELResourceWithRawResponse:
    def __init__(self, nel: AsyncNELResource) -> None:
        self._nel = nel

        self.edit = async_to_raw_response_wrapper(
            nel.edit,
        )
        self.get = async_to_raw_response_wrapper(
            nel.get,
        )


class NELResourceWithStreamingResponse:
    def __init__(self, nel: NELResource) -> None:
        self._nel = nel

        self.edit = to_streamed_response_wrapper(
            nel.edit,
        )
        self.get = to_streamed_response_wrapper(
            nel.get,
        )


class AsyncNELResourceWithStreamingResponse:
    def __init__(self, nel: AsyncNELResource) -> None:
        self._nel = nel

        self.edit = async_to_streamed_response_wrapper(
            nel.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            nel.get,
        )
