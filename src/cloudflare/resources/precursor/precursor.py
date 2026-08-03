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
from ...types.precursor.enforcement_rule_param import EnforcementRuleParam

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
        default_mode: Literal["off", "min-friction", "max-security"] | Omit = omit,
        enforcement_rules: Iterable[EnforcementRuleParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PrecursorConfig]:
        """
        Updates the Precursor configuration for a zone.

        `default_mode` sets the zone-level enforcement mode. `enforcement_rules` is the
        ordered list of rules that override enforcement for matching requests.

        This is a partial update: only the fields present in the request body are
        changed.

        - Sending an empty array (`[]`) clears all enforcement rules.
        - At least one of `default_mode` or `enforcement_rules` must be present; an
          empty body (`{}`) is rejected with `400`.
        - Rule `id` is read-only (assigned by Cloudflare) and ignored on input.
        - Rule `mode` must be `min-friction` or `max-security` (`off` is not a valid
          rule mode; use `default_mode` to disable enforcement).

        Args:
          zone_id: Identifier.

          default_mode: The zone-level Precursor enforcement mode applied to requests that do not match
              a more specific enforcement rule.

          enforcement_rules: The ordered list of enforcement rules for the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            path_template("/zones/{zone_id}/precursor", zone_id=zone_id),
            body=maybe_transform(
                {
                    "default_mode": default_mode,
                    "enforcement_rules": enforcement_rules,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PrecursorConfig]:
        """
        Retrieve a zone's Precursor configuration: the zone-level `default_mode` and the
        ordered list of `enforcement_rules`.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
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
        default_mode: Literal["off", "min-friction", "max-security"] | Omit = omit,
        enforcement_rules: Iterable[EnforcementRuleParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PrecursorConfig]:
        """
        Updates the Precursor configuration for a zone.

        `default_mode` sets the zone-level enforcement mode. `enforcement_rules` is the
        ordered list of rules that override enforcement for matching requests.

        This is a partial update: only the fields present in the request body are
        changed.

        - Sending an empty array (`[]`) clears all enforcement rules.
        - At least one of `default_mode` or `enforcement_rules` must be present; an
          empty body (`{}`) is rejected with `400`.
        - Rule `id` is read-only (assigned by Cloudflare) and ignored on input.
        - Rule `mode` must be `min-friction` or `max-security` (`off` is not a valid
          rule mode; use `default_mode` to disable enforcement).

        Args:
          zone_id: Identifier.

          default_mode: The zone-level Precursor enforcement mode applied to requests that do not match
              a more specific enforcement rule.

          enforcement_rules: The ordered list of enforcement rules for the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            path_template("/zones/{zone_id}/precursor", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "default_mode": default_mode,
                    "enforcement_rules": enforcement_rules,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PrecursorConfig]:
        """
        Retrieve a zone's Precursor configuration: the zone-level `default_mode` and the
        ordered list of `enforcement_rules`.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
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
