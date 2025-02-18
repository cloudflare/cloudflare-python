# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Optional, cast

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
from ...types.request_tracers import trace_create_params
from ...types.request_tracers.trace_create_response import TraceCreateResponse

__all__ = ["TracesResource", "AsyncTracesResource"]


class TracesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TracesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TracesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TracesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TracesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        method: str,
        url: str,
        body: trace_create_params.Body | NotGiven = NOT_GIVEN,
        context: trace_create_params.Context | NotGiven = NOT_GIVEN,
        cookies: Dict[str, str] | NotGiven = NOT_GIVEN,
        headers: Dict[str, str] | NotGiven = NOT_GIVEN,
        protocol: str | NotGiven = NOT_GIVEN,
        skip_response: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TraceCreateResponse]:
        """
        Request Trace

        Args:
          account_id: Identifier

          method: HTTP Method of tracing request

          url: URL to which perform tracing request

          context: Additional request parameters

          cookies: Cookies added to tracing request

          headers: Headers added to tracing request

          protocol: HTTP Protocol of tracing request

          skip_response: Skip sending the request to the Origin server after all rules evaluation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/request-tracer/trace",
            body=maybe_transform(
                {
                    "method": method,
                    "url": url,
                    "body": body,
                    "context": context,
                    "cookies": cookies,
                    "headers": headers,
                    "protocol": protocol,
                    "skip_response": skip_response,
                },
                trace_create_params.TraceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TraceCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TraceCreateResponse]], ResultWrapper[TraceCreateResponse]),
        )


class AsyncTracesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTracesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTracesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTracesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTracesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        method: str,
        url: str,
        body: trace_create_params.Body | NotGiven = NOT_GIVEN,
        context: trace_create_params.Context | NotGiven = NOT_GIVEN,
        cookies: Dict[str, str] | NotGiven = NOT_GIVEN,
        headers: Dict[str, str] | NotGiven = NOT_GIVEN,
        protocol: str | NotGiven = NOT_GIVEN,
        skip_response: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TraceCreateResponse]:
        """
        Request Trace

        Args:
          account_id: Identifier

          method: HTTP Method of tracing request

          url: URL to which perform tracing request

          context: Additional request parameters

          cookies: Cookies added to tracing request

          headers: Headers added to tracing request

          protocol: HTTP Protocol of tracing request

          skip_response: Skip sending the request to the Origin server after all rules evaluation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/request-tracer/trace",
            body=await async_maybe_transform(
                {
                    "method": method,
                    "url": url,
                    "body": body,
                    "context": context,
                    "cookies": cookies,
                    "headers": headers,
                    "protocol": protocol,
                    "skip_response": skip_response,
                },
                trace_create_params.TraceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TraceCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TraceCreateResponse]], ResultWrapper[TraceCreateResponse]),
        )


class TracesResourceWithRawResponse:
    def __init__(self, traces: TracesResource) -> None:
        self._traces = traces

        self.create = to_raw_response_wrapper(
            traces.create,
        )


class AsyncTracesResourceWithRawResponse:
    def __init__(self, traces: AsyncTracesResource) -> None:
        self._traces = traces

        self.create = async_to_raw_response_wrapper(
            traces.create,
        )


class TracesResourceWithStreamingResponse:
    def __init__(self, traces: TracesResource) -> None:
        self._traces = traces

        self.create = to_streamed_response_wrapper(
            traces.create,
        )


class AsyncTracesResourceWithStreamingResponse:
    def __init__(self, traces: AsyncTracesResource) -> None:
        self._traces = traces

        self.create = async_to_streamed_response_wrapper(
            traces.create,
        )
