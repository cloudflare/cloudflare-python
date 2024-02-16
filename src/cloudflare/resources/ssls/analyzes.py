# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.ssls import (
    AnalyzeAnalyzeCertificateAnalyzeCertificateResponse,
    analyze_analyze_certificate_analyze_certificate_params,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["Analyzes", "AsyncAnalyzes"]


class Analyzes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalyzesWithRawResponse:
        return AnalyzesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyzesWithStreamingResponse:
        return AnalyzesWithStreamingResponse(self)

    def analyze_certificate_analyze_certificate(
        self,
        zone_id: str,
        *,
        bundle_method: Literal["ubiquitous", "optimal", "force"] | NotGiven = NOT_GIVEN,
        certificate: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyzeAnalyzeCertificateAnalyzeCertificateResponse:
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
            AnalyzeAnalyzeCertificateAnalyzeCertificateResponse,
            self._post(
                f"/zones/{zone_id}/ssl/analyze",
                body=maybe_transform(
                    {
                        "bundle_method": bundle_method,
                        "certificate": certificate,
                    },
                    analyze_analyze_certificate_analyze_certificate_params.AnalyzeAnalyzeCertificateAnalyzeCertificateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AnalyzeAnalyzeCertificateAnalyzeCertificateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncAnalyzes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalyzesWithRawResponse:
        return AsyncAnalyzesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyzesWithStreamingResponse:
        return AsyncAnalyzesWithStreamingResponse(self)

    async def analyze_certificate_analyze_certificate(
        self,
        zone_id: str,
        *,
        bundle_method: Literal["ubiquitous", "optimal", "force"] | NotGiven = NOT_GIVEN,
        certificate: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnalyzeAnalyzeCertificateAnalyzeCertificateResponse:
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
            AnalyzeAnalyzeCertificateAnalyzeCertificateResponse,
            await self._post(
                f"/zones/{zone_id}/ssl/analyze",
                body=maybe_transform(
                    {
                        "bundle_method": bundle_method,
                        "certificate": certificate,
                    },
                    analyze_analyze_certificate_analyze_certificate_params.AnalyzeAnalyzeCertificateAnalyzeCertificateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AnalyzeAnalyzeCertificateAnalyzeCertificateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AnalyzesWithRawResponse:
    def __init__(self, analyzes: Analyzes) -> None:
        self._analyzes = analyzes

        self.analyze_certificate_analyze_certificate = to_raw_response_wrapper(
            analyzes.analyze_certificate_analyze_certificate,
        )


class AsyncAnalyzesWithRawResponse:
    def __init__(self, analyzes: AsyncAnalyzes) -> None:
        self._analyzes = analyzes

        self.analyze_certificate_analyze_certificate = async_to_raw_response_wrapper(
            analyzes.analyze_certificate_analyze_certificate,
        )


class AnalyzesWithStreamingResponse:
    def __init__(self, analyzes: Analyzes) -> None:
        self._analyzes = analyzes

        self.analyze_certificate_analyze_certificate = to_streamed_response_wrapper(
            analyzes.analyze_certificate_analyze_certificate,
        )


class AsyncAnalyzesWithStreamingResponse:
    def __init__(self, analyzes: AsyncAnalyzes) -> None:
        self._analyzes = analyzes

        self.analyze_certificate_analyze_certificate = async_to_streamed_response_wrapper(
            analyzes.analyze_certificate_analyze_certificate,
        )
