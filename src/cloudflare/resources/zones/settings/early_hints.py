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
from ....types.zones.settings import ZonesEarlyHints, early_hint_edit_params

__all__ = ["EarlyHints", "AsyncEarlyHints"]


class EarlyHints(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EarlyHintsWithRawResponse:
        return EarlyHintsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EarlyHintsWithStreamingResponse:
        return EarlyHintsWithStreamingResponse(self)

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
    ) -> Optional[ZonesEarlyHints]:
        """
        When enabled, Cloudflare will attempt to speed up overall page loads by serving
        `103` responses with `Link` headers from the final response. Refer to
        [Early Hints](https://developers.cloudflare.com/cache/about/early-hints) for
        more information.

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
            f"/zones/{zone_id}/settings/early_hints",
            body=maybe_transform({"value": value}, early_hint_edit_params.EarlyHintEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesEarlyHints]], ResultWrapper[ZonesEarlyHints]),
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
    ) -> Optional[ZonesEarlyHints]:
        """
        When enabled, Cloudflare will attempt to speed up overall page loads by serving
        `103` responses with `Link` headers from the final response. Refer to
        [Early Hints](https://developers.cloudflare.com/cache/about/early-hints) for
        more information.

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
            f"/zones/{zone_id}/settings/early_hints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesEarlyHints]], ResultWrapper[ZonesEarlyHints]),
        )


class AsyncEarlyHints(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEarlyHintsWithRawResponse:
        return AsyncEarlyHintsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEarlyHintsWithStreamingResponse:
        return AsyncEarlyHintsWithStreamingResponse(self)

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
    ) -> Optional[ZonesEarlyHints]:
        """
        When enabled, Cloudflare will attempt to speed up overall page loads by serving
        `103` responses with `Link` headers from the final response. Refer to
        [Early Hints](https://developers.cloudflare.com/cache/about/early-hints) for
        more information.

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
            f"/zones/{zone_id}/settings/early_hints",
            body=await async_maybe_transform({"value": value}, early_hint_edit_params.EarlyHintEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesEarlyHints]], ResultWrapper[ZonesEarlyHints]),
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
    ) -> Optional[ZonesEarlyHints]:
        """
        When enabled, Cloudflare will attempt to speed up overall page loads by serving
        `103` responses with `Link` headers from the final response. Refer to
        [Early Hints](https://developers.cloudflare.com/cache/about/early-hints) for
        more information.

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
            f"/zones/{zone_id}/settings/early_hints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesEarlyHints]], ResultWrapper[ZonesEarlyHints]),
        )


class EarlyHintsWithRawResponse:
    def __init__(self, early_hints: EarlyHints) -> None:
        self._early_hints = early_hints

        self.edit = to_raw_response_wrapper(
            early_hints.edit,
        )
        self.get = to_raw_response_wrapper(
            early_hints.get,
        )


class AsyncEarlyHintsWithRawResponse:
    def __init__(self, early_hints: AsyncEarlyHints) -> None:
        self._early_hints = early_hints

        self.edit = async_to_raw_response_wrapper(
            early_hints.edit,
        )
        self.get = async_to_raw_response_wrapper(
            early_hints.get,
        )


class EarlyHintsWithStreamingResponse:
    def __init__(self, early_hints: EarlyHints) -> None:
        self._early_hints = early_hints

        self.edit = to_streamed_response_wrapper(
            early_hints.edit,
        )
        self.get = to_streamed_response_wrapper(
            early_hints.get,
        )


class AsyncEarlyHintsWithStreamingResponse:
    def __init__(self, early_hints: AsyncEarlyHints) -> None:
        self._early_hints = early_hints

        self.edit = async_to_streamed_response_wrapper(
            early_hints.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            early_hints.get,
        )
