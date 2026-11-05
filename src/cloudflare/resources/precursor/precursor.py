# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..._base_client import make_request_options
from ...types.precursor import precursor_update_params
from ...types.precursor.precursor_config import PrecursorConfig

__all__ = ["PrecursorResource", "AsyncPrecursorResource"]


class PrecursorResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrecursorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PrecursorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrecursorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PrecursorResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        cloudflare_version: Literal["1.0"] = "1.0",
        mode: Literal["off", "monitor", "arm"] | Omit = omit,
        rules: Iterable[precursor_update_params.Rule] | Omit = omit,
        show_interstitial: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PrecursorConfig]:
        """
        Updates the Precursor configuration for a zone.

        `mode` controls whether Precursor detection is off, monitoring, or armed.
        `show_interstitial` controls the zone-level response when armed. `rules` is the
        ordered list of overrides for matching requests.

        This is a partial update: only the fields present in the request body are
        changed.

        - Sending an empty array (`[]`) clears all rules.
        - At least one of `mode`, `show_interstitial`, or `rules` must be present; an
          empty body (`{}`) is rejected with `400`.
        - Rule `id` is read-only (assigned by Cloudflare) and ignored on input.
        - Rule `show_interstitial` is required and controls the response for requests
          that match that rule.
        - Rule `expression` is limited to 4000 characters. The limit applies to each
          rule individually, not to the combined size of all rules.

        Args:
          zone_id: Identifier.

          mode: Controls Precursor detection for the zone. `off` disables detection, `monitor`
              records detections without affecting bot scores, and `arm` allows detections to
              affect bot scores.

          rules: The ordered list of Precursor rules for the zone.

          show_interstitial: Whether Precursor shows an interstitial when it takes action on a request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Cloudflare-Version": str(cloudflare_version), **(extra_headers or {})}
        extra_headers.update({"Cloudflare-Version": "1.0"})
        return self._put(
            path_template("/zones/{zone_id}/precursor", zone_id=zone_id),
            body=maybe_transform(
                {
                    "mode": mode,
                    "rules": rules,
                    "show_interstitial": show_interstitial,
                },
                precursor_update_params.PrecursorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PrecursorConfig]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrecursorConfig]], ResultWrapper[PrecursorConfig]),
        )

    def get(
        self,
        *,
        zone_id: str,
        cloudflare_version: Literal["1.0"] = "1.0",
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PrecursorConfig]:
        """
        Retrieve a zone's Precursor configuration: the detection `mode`, whether to
        `show_interstitial`, and the ordered list of `rules`.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Cloudflare-Version": str(cloudflare_version), **(extra_headers or {})}
        extra_headers.update({"Cloudflare-Version": "1.0"})
        return self._get(
            path_template("/zones/{zone_id}/precursor", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PrecursorConfig]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrecursorConfig]], ResultWrapper[PrecursorConfig]),
        )


class AsyncPrecursorResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrecursorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrecursorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrecursorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPrecursorResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        cloudflare_version: Literal["1.0"] = "1.0",
        mode: Literal["off", "monitor", "arm"] | Omit = omit,
        rules: Iterable[precursor_update_params.Rule] | Omit = omit,
        show_interstitial: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PrecursorConfig]:
        """
        Updates the Precursor configuration for a zone.

        `mode` controls whether Precursor detection is off, monitoring, or armed.
        `show_interstitial` controls the zone-level response when armed. `rules` is the
        ordered list of overrides for matching requests.

        This is a partial update: only the fields present in the request body are
        changed.

        - Sending an empty array (`[]`) clears all rules.
        - At least one of `mode`, `show_interstitial`, or `rules` must be present; an
          empty body (`{}`) is rejected with `400`.
        - Rule `id` is read-only (assigned by Cloudflare) and ignored on input.
        - Rule `show_interstitial` is required and controls the response for requests
          that match that rule.
        - Rule `expression` is limited to 4000 characters. The limit applies to each
          rule individually, not to the combined size of all rules.

        Args:
          zone_id: Identifier.

          mode: Controls Precursor detection for the zone. `off` disables detection, `monitor`
              records detections without affecting bot scores, and `arm` allows detections to
              affect bot scores.

          rules: The ordered list of Precursor rules for the zone.

          show_interstitial: Whether Precursor shows an interstitial when it takes action on a request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Cloudflare-Version": str(cloudflare_version), **(extra_headers or {})}
        extra_headers.update({"Cloudflare-Version": "1.0"})
        return await self._put(
            path_template("/zones/{zone_id}/precursor", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "mode": mode,
                    "rules": rules,
                    "show_interstitial": show_interstitial,
                },
                precursor_update_params.PrecursorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PrecursorConfig]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrecursorConfig]], ResultWrapper[PrecursorConfig]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        cloudflare_version: Literal["1.0"] = "1.0",
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PrecursorConfig]:
        """
        Retrieve a zone's Precursor configuration: the detection `mode`, whether to
        `show_interstitial`, and the ordered list of `rules`.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Cloudflare-Version": str(cloudflare_version), **(extra_headers or {})}
        extra_headers.update({"Cloudflare-Version": "1.0"})
        return await self._get(
            path_template("/zones/{zone_id}/precursor", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PrecursorConfig]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrecursorConfig]], ResultWrapper[PrecursorConfig]),
        )


class PrecursorResourceWithRawResponse:
    def __init__(self, precursor: PrecursorResource) -> None:
        self._precursor = precursor

        self.update = to_raw_response_wrapper(
            precursor.update,
        )
        self.get = to_raw_response_wrapper(
            precursor.get,
        )


class AsyncPrecursorResourceWithRawResponse:
    def __init__(self, precursor: AsyncPrecursorResource) -> None:
        self._precursor = precursor

        self.update = async_to_raw_response_wrapper(
            precursor.update,
        )
        self.get = async_to_raw_response_wrapper(
            precursor.get,
        )


class PrecursorResourceWithStreamingResponse:
    def __init__(self, precursor: PrecursorResource) -> None:
        self._precursor = precursor

        self.update = to_streamed_response_wrapper(
            precursor.update,
        )
        self.get = to_streamed_response_wrapper(
            precursor.get,
        )


class AsyncPrecursorResourceWithStreamingResponse:
    def __init__(self, precursor: AsyncPrecursorResource) -> None:
        self._precursor = precursor

        self.update = async_to_streamed_response_wrapper(
            precursor.update,
        )
        self.get = async_to_streamed_response_wrapper(
            precursor.get,
        )
