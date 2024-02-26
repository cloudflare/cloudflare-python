# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.emails.routing import DisableCreateResponse

__all__ = ["Disables", "AsyncDisables"]


class Disables(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DisablesWithRawResponse:
        return DisablesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DisablesWithStreamingResponse:
        return DisablesWithStreamingResponse(self)

    def create(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DisableCreateResponse:
        """Disable your Email Routing zone.

        Also removes additional MX records previously
        required for Email Routing to work.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/email/routing/disable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DisableCreateResponse], ResultWrapper[DisableCreateResponse]),
        )


class AsyncDisables(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDisablesWithRawResponse:
        return AsyncDisablesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDisablesWithStreamingResponse:
        return AsyncDisablesWithStreamingResponse(self)

    async def create(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DisableCreateResponse:
        """Disable your Email Routing zone.

        Also removes additional MX records previously
        required for Email Routing to work.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/email/routing/disable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DisableCreateResponse], ResultWrapper[DisableCreateResponse]),
        )


class DisablesWithRawResponse:
    def __init__(self, disables: Disables) -> None:
        self._disables = disables

        self.create = to_raw_response_wrapper(
            disables.create,
        )


class AsyncDisablesWithRawResponse:
    def __init__(self, disables: AsyncDisables) -> None:
        self._disables = disables

        self.create = async_to_raw_response_wrapper(
            disables.create,
        )


class DisablesWithStreamingResponse:
    def __init__(self, disables: Disables) -> None:
        self._disables = disables

        self.create = to_streamed_response_wrapper(
            disables.create,
        )


class AsyncDisablesWithStreamingResponse:
    def __init__(self, disables: AsyncDisables) -> None:
        self._disables = disables

        self.create = async_to_streamed_response_wrapper(
            disables.create,
        )
