# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.diagnostics import TracerouteDiagnosticsTracerouteResponse, traceroute_diagnostics_traceroute_params

from typing import Type, Optional, List

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.diagnostics import traceroute_diagnostics_traceroute_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Traceroutes", "AsyncTraceroutes"]


class Traceroutes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TraceroutesWithRawResponse:
        return TraceroutesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TraceroutesWithStreamingResponse:
        return TraceroutesWithStreamingResponse(self)

    def diagnostics_traceroute(
        self,
        account_identifier: str,
        *,
        targets: List[str],
        colos: List[str] | NotGiven = NOT_GIVEN,
        options: traceroute_diagnostics_traceroute_params.Options | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TracerouteDiagnosticsTracerouteResponse]:
        """
        Run traceroutes from Cloudflare colos.

        Args:
          account_identifier: Identifier

          colos: If no source colo names specified, all colos will be used. China colos are
              unavailable for traceroutes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/diagnostics/traceroute",
            body=maybe_transform(
                {
                    "targets": targets,
                    "colos": colos,
                    "options": options,
                },
                traceroute_diagnostics_traceroute_params.TracerouteDiagnosticsTracerouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TracerouteDiagnosticsTracerouteResponse]],
                ResultWrapper[TracerouteDiagnosticsTracerouteResponse],
            ),
        )


class AsyncTraceroutes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTraceroutesWithRawResponse:
        return AsyncTraceroutesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTraceroutesWithStreamingResponse:
        return AsyncTraceroutesWithStreamingResponse(self)

    async def diagnostics_traceroute(
        self,
        account_identifier: str,
        *,
        targets: List[str],
        colos: List[str] | NotGiven = NOT_GIVEN,
        options: traceroute_diagnostics_traceroute_params.Options | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TracerouteDiagnosticsTracerouteResponse]:
        """
        Run traceroutes from Cloudflare colos.

        Args:
          account_identifier: Identifier

          colos: If no source colo names specified, all colos will be used. China colos are
              unavailable for traceroutes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/diagnostics/traceroute",
            body=maybe_transform(
                {
                    "targets": targets,
                    "colos": colos,
                    "options": options,
                },
                traceroute_diagnostics_traceroute_params.TracerouteDiagnosticsTracerouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TracerouteDiagnosticsTracerouteResponse]],
                ResultWrapper[TracerouteDiagnosticsTracerouteResponse],
            ),
        )


class TraceroutesWithRawResponse:
    def __init__(self, traceroutes: Traceroutes) -> None:
        self._traceroutes = traceroutes

        self.diagnostics_traceroute = to_raw_response_wrapper(
            traceroutes.diagnostics_traceroute,
        )


class AsyncTraceroutesWithRawResponse:
    def __init__(self, traceroutes: AsyncTraceroutes) -> None:
        self._traceroutes = traceroutes

        self.diagnostics_traceroute = async_to_raw_response_wrapper(
            traceroutes.diagnostics_traceroute,
        )


class TraceroutesWithStreamingResponse:
    def __init__(self, traceroutes: Traceroutes) -> None:
        self._traceroutes = traceroutes

        self.diagnostics_traceroute = to_streamed_response_wrapper(
            traceroutes.diagnostics_traceroute,
        )


class AsyncTraceroutesWithStreamingResponse:
    def __init__(self, traceroutes: AsyncTraceroutes) -> None:
        self._traceroutes = traceroutes

        self.diagnostics_traceroute = async_to_streamed_response_wrapper(
            traceroutes.diagnostics_traceroute,
        )
