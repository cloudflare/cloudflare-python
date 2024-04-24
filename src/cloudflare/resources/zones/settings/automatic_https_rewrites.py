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
from ....types.zones.settings import automatic_https_rewrite_edit_params
from ....types.zones.settings.automatic_https_rewrites import AutomaticHTTPSRewrites

__all__ = ["AutomaticHTTPSRewritesResource", "AsyncAutomaticHTTPSRewritesResource"]


class AutomaticHTTPSRewritesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutomaticHTTPSRewritesResourceWithRawResponse:
        return AutomaticHTTPSRewritesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutomaticHTTPSRewritesResourceWithStreamingResponse:
        return AutomaticHTTPSRewritesResourceWithStreamingResponse(self)

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
    ) -> Optional[AutomaticHTTPSRewrites]:
        """
        Enable the Automatic HTTPS Rewrites feature for this zone.

        Args:
          zone_id: Identifier

          value: Value of the zone setting. Notes: Default value depends on the zone's plan
              level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/automatic_https_rewrites",
            body=maybe_transform({"value": value}, automatic_https_rewrite_edit_params.AutomaticHTTPSRewriteEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AutomaticHTTPSRewrites]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AutomaticHTTPSRewrites]], ResultWrapper[AutomaticHTTPSRewrites]),
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
    ) -> Optional[AutomaticHTTPSRewrites]:
        """
        Enable the Automatic HTTPS Rewrites feature for this zone.

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
            f"/zones/{zone_id}/settings/automatic_https_rewrites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AutomaticHTTPSRewrites]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AutomaticHTTPSRewrites]], ResultWrapper[AutomaticHTTPSRewrites]),
        )


class AsyncAutomaticHTTPSRewritesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutomaticHTTPSRewritesResourceWithRawResponse:
        return AsyncAutomaticHTTPSRewritesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutomaticHTTPSRewritesResourceWithStreamingResponse:
        return AsyncAutomaticHTTPSRewritesResourceWithStreamingResponse(self)

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
    ) -> Optional[AutomaticHTTPSRewrites]:
        """
        Enable the Automatic HTTPS Rewrites feature for this zone.

        Args:
          zone_id: Identifier

          value: Value of the zone setting. Notes: Default value depends on the zone's plan
              level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/automatic_https_rewrites",
            body=await async_maybe_transform(
                {"value": value}, automatic_https_rewrite_edit_params.AutomaticHTTPSRewriteEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AutomaticHTTPSRewrites]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AutomaticHTTPSRewrites]], ResultWrapper[AutomaticHTTPSRewrites]),
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
    ) -> Optional[AutomaticHTTPSRewrites]:
        """
        Enable the Automatic HTTPS Rewrites feature for this zone.

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
            f"/zones/{zone_id}/settings/automatic_https_rewrites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AutomaticHTTPSRewrites]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AutomaticHTTPSRewrites]], ResultWrapper[AutomaticHTTPSRewrites]),
        )


class AutomaticHTTPSRewritesResourceWithRawResponse:
    def __init__(self, automatic_https_rewrites: AutomaticHTTPSRewritesResource) -> None:
        self._automatic_https_rewrites = automatic_https_rewrites

        self.edit = to_raw_response_wrapper(
            automatic_https_rewrites.edit,
        )
        self.get = to_raw_response_wrapper(
            automatic_https_rewrites.get,
        )


class AsyncAutomaticHTTPSRewritesResourceWithRawResponse:
    def __init__(self, automatic_https_rewrites: AsyncAutomaticHTTPSRewritesResource) -> None:
        self._automatic_https_rewrites = automatic_https_rewrites

        self.edit = async_to_raw_response_wrapper(
            automatic_https_rewrites.edit,
        )
        self.get = async_to_raw_response_wrapper(
            automatic_https_rewrites.get,
        )


class AutomaticHTTPSRewritesResourceWithStreamingResponse:
    def __init__(self, automatic_https_rewrites: AutomaticHTTPSRewritesResource) -> None:
        self._automatic_https_rewrites = automatic_https_rewrites

        self.edit = to_streamed_response_wrapper(
            automatic_https_rewrites.edit,
        )
        self.get = to_streamed_response_wrapper(
            automatic_https_rewrites.get,
        )


class AsyncAutomaticHTTPSRewritesResourceWithStreamingResponse:
    def __init__(self, automatic_https_rewrites: AsyncAutomaticHTTPSRewritesResource) -> None:
        self._automatic_https_rewrites = automatic_https_rewrites

        self.edit = async_to_streamed_response_wrapper(
            automatic_https_rewrites.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            automatic_https_rewrites.get,
        )
