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
from ..._base_client import make_request_options
from ...types.diagnostics import traceroute_create_params
from ...types.diagnostics.traceroute_create_response import TracerouteCreateResponse

__all__ = ["TraceroutesResource", "AsyncTraceroutesResource"]


class TraceroutesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TraceroutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TraceroutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TraceroutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TraceroutesResourceWithStreamingResponse(self)

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
                post_parser=ResultWrapper[Optional[TracerouteCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TracerouteCreateResponse]], ResultWrapper[TracerouteCreateResponse]),
        )


class AsyncTraceroutesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTraceroutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTraceroutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTraceroutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTraceroutesResourceWithStreamingResponse(self)

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
                post_parser=ResultWrapper[Optional[TracerouteCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TracerouteCreateResponse]], ResultWrapper[TracerouteCreateResponse]),
        )


class TraceroutesResourceWithRawResponse:
    def __init__(self, traceroutes: TraceroutesResource) -> None:
        self._traceroutes = traceroutes

        self.create = to_raw_response_wrapper(
            traceroutes.create,
        )


class AsyncTraceroutesResourceWithRawResponse:
    def __init__(self, traceroutes: AsyncTraceroutesResource) -> None:
        self._traceroutes = traceroutes

        self.create = async_to_raw_response_wrapper(
            traceroutes.create,
        )


class TraceroutesResourceWithStreamingResponse:
    def __init__(self, traceroutes: TraceroutesResource) -> None:
        self._traceroutes = traceroutes

        self.create = to_streamed_response_wrapper(
            traceroutes.create,
        )


class AsyncTraceroutesResourceWithStreamingResponse:
    def __init__(self, traceroutes: AsyncTraceroutesResource) -> None:
        self._traceroutes = traceroutes

        self.create = async_to_streamed_response_wrapper(
            traceroutes.create,
        )
