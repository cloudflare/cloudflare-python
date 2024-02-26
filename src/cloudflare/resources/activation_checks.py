# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..types import ActivationCheckUpdateResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["ActivationChecks", "AsyncActivationChecks"]


class ActivationChecks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActivationChecksWithRawResponse:
        return ActivationChecksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActivationChecksWithStreamingResponse:
        return ActivationChecksWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivationCheckUpdateResponse:
        """Triggeres a new activation check for a PENDING Zone.

        This can be triggered every
        5 min for paygo/ent customers, every hour for FREE Zones.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/activation_check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ActivationCheckUpdateResponse], ResultWrapper[ActivationCheckUpdateResponse]),
        )


class AsyncActivationChecks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActivationChecksWithRawResponse:
        return AsyncActivationChecksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActivationChecksWithStreamingResponse:
        return AsyncActivationChecksWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivationCheckUpdateResponse:
        """Triggeres a new activation check for a PENDING Zone.

        This can be triggered every
        5 min for paygo/ent customers, every hour for FREE Zones.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/activation_check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ActivationCheckUpdateResponse], ResultWrapper[ActivationCheckUpdateResponse]),
        )


class ActivationChecksWithRawResponse:
    def __init__(self, activation_checks: ActivationChecks) -> None:
        self._activation_checks = activation_checks

        self.update = to_raw_response_wrapper(
            activation_checks.update,
        )


class AsyncActivationChecksWithRawResponse:
    def __init__(self, activation_checks: AsyncActivationChecks) -> None:
        self._activation_checks = activation_checks

        self.update = async_to_raw_response_wrapper(
            activation_checks.update,
        )


class ActivationChecksWithStreamingResponse:
    def __init__(self, activation_checks: ActivationChecks) -> None:
        self._activation_checks = activation_checks

        self.update = to_streamed_response_wrapper(
            activation_checks.update,
        )


class AsyncActivationChecksWithStreamingResponse:
    def __init__(self, activation_checks: AsyncActivationChecks) -> None:
        self._activation_checks = activation_checks

        self.update = async_to_streamed_response_wrapper(
            activation_checks.update,
        )
