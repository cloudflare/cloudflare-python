# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

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
from ...types.ssl import AnalyzeCreateResponse, analyze_create_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["Analyze", "AsyncAnalyze"]


class Analyze(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalyzeWithRawResponse:
        return AnalyzeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyzeWithStreamingResponse:
        return AnalyzeWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        bundle_method: Literal["ubiquitous", "optimal", "force"] | NotGiven = NOT_GIVEN,
        certificate: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyzeCreateResponse:
        """
        Returns the set of hostnames, the signature algorithm, and the expiration date
        of the certificate.

        Args:
          zone_id: Identifier

          bundle_method: A ubiquitous bundle has the highest probability of being verified everywhere,
              even by clients using outdated or unusual trust stores. An optimal bundle uses
              the shortest chain and newest intermediates. And the force bundle verifies the
              chain, but does not otherwise modify it.

          certificate: The zone's SSL certificate or certificate and the intermediate(s).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            AnalyzeCreateResponse,
            self._post(
                f"/zones/{zone_id}/ssl/analyze",
                body=maybe_transform(
                    {
                        "bundle_method": bundle_method,
                        "certificate": certificate,
                    },
                    analyze_create_params.AnalyzeCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AnalyzeCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncAnalyze(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalyzeWithRawResponse:
        return AsyncAnalyzeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyzeWithStreamingResponse:
        return AsyncAnalyzeWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        bundle_method: Literal["ubiquitous", "optimal", "force"] | NotGiven = NOT_GIVEN,
        certificate: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyzeCreateResponse:
        """
        Returns the set of hostnames, the signature algorithm, and the expiration date
        of the certificate.

        Args:
          zone_id: Identifier

          bundle_method: A ubiquitous bundle has the highest probability of being verified everywhere,
              even by clients using outdated or unusual trust stores. An optimal bundle uses
              the shortest chain and newest intermediates. And the force bundle verifies the
              chain, but does not otherwise modify it.

          certificate: The zone's SSL certificate or certificate and the intermediate(s).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            AnalyzeCreateResponse,
            await self._post(
                f"/zones/{zone_id}/ssl/analyze",
                body=await async_maybe_transform(
                    {
                        "bundle_method": bundle_method,
                        "certificate": certificate,
                    },
                    analyze_create_params.AnalyzeCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AnalyzeCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AnalyzeWithRawResponse:
    def __init__(self, analyze: Analyze) -> None:
        self._analyze = analyze

        self.create = to_raw_response_wrapper(
            analyze.create,
        )


class AsyncAnalyzeWithRawResponse:
    def __init__(self, analyze: AsyncAnalyze) -> None:
        self._analyze = analyze

        self.create = async_to_raw_response_wrapper(
            analyze.create,
        )


class AnalyzeWithStreamingResponse:
    def __init__(self, analyze: Analyze) -> None:
        self._analyze = analyze

        self.create = to_streamed_response_wrapper(
            analyze.create,
        )


class AsyncAnalyzeWithStreamingResponse:
    def __init__(self, analyze: AsyncAnalyze) -> None:
        self._analyze = analyze

        self.create = async_to_streamed_response_wrapper(
            analyze.create,
        )
