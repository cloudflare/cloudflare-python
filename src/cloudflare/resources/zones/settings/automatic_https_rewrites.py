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
from ....types.zones.settings import ZonesAutomaticHTTPSRewrites, automatic_https_rewrite_edit_params

__all__ = ["AutomaticHTTPSRewrites", "AsyncAutomaticHTTPSRewrites"]


class AutomaticHTTPSRewrites(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutomaticHTTPSRewritesWithRawResponse:
        return AutomaticHTTPSRewritesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutomaticHTTPSRewritesWithStreamingResponse:
        return AutomaticHTTPSRewritesWithStreamingResponse(self)

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
    ) -> Optional[ZonesAutomaticHTTPSRewrites]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesAutomaticHTTPSRewrites]], ResultWrapper[ZonesAutomaticHTTPSRewrites]),
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
    ) -> Optional[ZonesAutomaticHTTPSRewrites]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesAutomaticHTTPSRewrites]], ResultWrapper[ZonesAutomaticHTTPSRewrites]),
        )


class AsyncAutomaticHTTPSRewrites(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutomaticHTTPSRewritesWithRawResponse:
        return AsyncAutomaticHTTPSRewritesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutomaticHTTPSRewritesWithStreamingResponse:
        return AsyncAutomaticHTTPSRewritesWithStreamingResponse(self)

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
    ) -> Optional[ZonesAutomaticHTTPSRewrites]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesAutomaticHTTPSRewrites]], ResultWrapper[ZonesAutomaticHTTPSRewrites]),
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
    ) -> Optional[ZonesAutomaticHTTPSRewrites]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesAutomaticHTTPSRewrites]], ResultWrapper[ZonesAutomaticHTTPSRewrites]),
        )


class AutomaticHTTPSRewritesWithRawResponse:
    def __init__(self, automatic_https_rewrites: AutomaticHTTPSRewrites) -> None:
        self._automatic_https_rewrites = automatic_https_rewrites

        self.edit = to_raw_response_wrapper(
            automatic_https_rewrites.edit,
        )
        self.get = to_raw_response_wrapper(
            automatic_https_rewrites.get,
        )


class AsyncAutomaticHTTPSRewritesWithRawResponse:
    def __init__(self, automatic_https_rewrites: AsyncAutomaticHTTPSRewrites) -> None:
        self._automatic_https_rewrites = automatic_https_rewrites

        self.edit = async_to_raw_response_wrapper(
            automatic_https_rewrites.edit,
        )
        self.get = async_to_raw_response_wrapper(
            automatic_https_rewrites.get,
        )


class AutomaticHTTPSRewritesWithStreamingResponse:
    def __init__(self, automatic_https_rewrites: AutomaticHTTPSRewrites) -> None:
        self._automatic_https_rewrites = automatic_https_rewrites

        self.edit = to_streamed_response_wrapper(
            automatic_https_rewrites.edit,
        )
        self.get = to_streamed_response_wrapper(
            automatic_https_rewrites.get,
        )


class AsyncAutomaticHTTPSRewritesWithStreamingResponse:
    def __init__(self, automatic_https_rewrites: AsyncAutomaticHTTPSRewrites) -> None:
        self._automatic_https_rewrites = automatic_https_rewrites

        self.edit = async_to_streamed_response_wrapper(
            automatic_https_rewrites.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            automatic_https_rewrites.get,
        )
