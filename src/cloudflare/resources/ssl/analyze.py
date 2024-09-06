# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options

from ...types.custom_hostnames.bundle_method import BundleMethod

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
from ...types import shared_params
from ...types.ssl import analyze_create_params
from ...types.custom_hostnames import BundleMethod
from typing import cast
from typing import cast

__all__ = ["AnalyzeResource", "AsyncAnalyzeResource"]


class AnalyzeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalyzeResourceWithRawResponse:
        return AnalyzeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyzeResourceWithStreamingResponse:
        return AnalyzeResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        bundle_method: BundleMethod | NotGiven = NOT_GIVEN,
        certificate: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
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
        return self._post(
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
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncAnalyzeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalyzeResourceWithRawResponse:
        return AsyncAnalyzeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyzeResourceWithStreamingResponse:
        return AsyncAnalyzeResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        bundle_method: BundleMethod | NotGiven = NOT_GIVEN,
        certificate: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
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
        return await self._post(
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
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AnalyzeResourceWithRawResponse:
    def __init__(self, analyze: AnalyzeResource) -> None:
        self._analyze = analyze

        self.create = to_raw_response_wrapper(
            analyze.create,
        )


class AsyncAnalyzeResourceWithRawResponse:
    def __init__(self, analyze: AsyncAnalyzeResource) -> None:
        self._analyze = analyze

        self.create = async_to_raw_response_wrapper(
            analyze.create,
        )


class AnalyzeResourceWithStreamingResponse:
    def __init__(self, analyze: AnalyzeResource) -> None:
        self._analyze = analyze

        self.create = to_streamed_response_wrapper(
            analyze.create,
        )


class AsyncAnalyzeResourceWithStreamingResponse:
    def __init__(self, analyze: AsyncAnalyzeResource) -> None:
        self._analyze = analyze

        self.create = async_to_streamed_response_wrapper(
            analyze.create,
        )
