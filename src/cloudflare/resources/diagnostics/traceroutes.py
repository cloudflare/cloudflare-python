# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.diagnostics import TracerouteCreateResponse, traceroute_create_params

__all__ = ["Traceroutes", "AsyncTraceroutes"]


class Traceroutes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TraceroutesWithRawResponse:
        return TraceroutesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TraceroutesWithStreamingResponse:
        return TraceroutesWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        targets: List[str],
        colos: List[str] | NotGiven = NOT_GIVEN,
        options: traceroute_create_params.Options | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TracerouteCreateResponse]:
        """
        Run traceroutes from Cloudflare colos.

        Args:
          account_id: Identifier

          colos: If no source colo names specified, all colos will be used. China colos are
              unavailable for traceroutes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/diagnostics/traceroute",
            body=maybe_transform(
                {
                    "targets": targets,
                    "colos": colos,
                    "options": options,
                },
                traceroute_create_params.TracerouteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TracerouteCreateResponse]], ResultWrapper[TracerouteCreateResponse]),
        )


class AsyncTraceroutes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTraceroutesWithRawResponse:
        return AsyncTraceroutesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTraceroutesWithStreamingResponse:
        return AsyncTraceroutesWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        targets: List[str],
        colos: List[str] | NotGiven = NOT_GIVEN,
        options: traceroute_create_params.Options | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TracerouteCreateResponse]:
        """
        Run traceroutes from Cloudflare colos.

        Args:
          account_id: Identifier

          colos: If no source colo names specified, all colos will be used. China colos are
              unavailable for traceroutes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/diagnostics/traceroute",
            body=await async_maybe_transform(
                {
                    "targets": targets,
                    "colos": colos,
                    "options": options,
                },
                traceroute_create_params.TracerouteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TracerouteCreateResponse]], ResultWrapper[TracerouteCreateResponse]),
        )


class TraceroutesWithRawResponse:
    def __init__(self, traceroutes: Traceroutes) -> None:
        self._traceroutes = traceroutes

        self.create = to_raw_response_wrapper(
            traceroutes.create,
        )


class AsyncTraceroutesWithRawResponse:
    def __init__(self, traceroutes: AsyncTraceroutes) -> None:
        self._traceroutes = traceroutes

        self.create = async_to_raw_response_wrapper(
            traceroutes.create,
        )


class TraceroutesWithStreamingResponse:
    def __init__(self, traceroutes: Traceroutes) -> None:
        self._traceroutes = traceroutes

        self.create = to_streamed_response_wrapper(
            traceroutes.create,
        )


class AsyncTraceroutesWithStreamingResponse:
    def __init__(self, traceroutes: AsyncTraceroutes) -> None:
        self._traceroutes = traceroutes

        self.create = async_to_streamed_response_wrapper(
            traceroutes.create,
        )
