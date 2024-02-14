# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.brand_protections import SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse

from typing import Type

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
from ...types.brand_protections import submit_phishing_url_scanner_submit_suspicious_url_for_scanning_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Submits", "AsyncSubmits"]


class Submits(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubmitsWithRawResponse:
        return SubmitsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubmitsWithStreamingResponse:
        return SubmitsWithStreamingResponse(self)

    def phishing_url_scanner_submit_suspicious_url_for_scanning(
        self,
        account_id: str,
        *,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse:
        """
        Submit suspicious URL for scanning

        Args:
          account_id: Identifier

          url: URL(s) to filter submissions results by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/brand-protection/submit",
            body=maybe_transform(
                {"url": url},
                submit_phishing_url_scanner_submit_suspicious_url_for_scanning_params.SubmitPhishingURLScannerSubmitSuspiciousURLForScanningParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse],
                ResultWrapper[SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse],
            ),
        )


class AsyncSubmits(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubmitsWithRawResponse:
        return AsyncSubmitsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubmitsWithStreamingResponse:
        return AsyncSubmitsWithStreamingResponse(self)

    async def phishing_url_scanner_submit_suspicious_url_for_scanning(
        self,
        account_id: str,
        *,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse:
        """
        Submit suspicious URL for scanning

        Args:
          account_id: Identifier

          url: URL(s) to filter submissions results by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/brand-protection/submit",
            body=maybe_transform(
                {"url": url},
                submit_phishing_url_scanner_submit_suspicious_url_for_scanning_params.SubmitPhishingURLScannerSubmitSuspiciousURLForScanningParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse],
                ResultWrapper[SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse],
            ),
        )


class SubmitsWithRawResponse:
    def __init__(self, submits: Submits) -> None:
        self._submits = submits

        self.phishing_url_scanner_submit_suspicious_url_for_scanning = to_raw_response_wrapper(
            submits.phishing_url_scanner_submit_suspicious_url_for_scanning,
        )


class AsyncSubmitsWithRawResponse:
    def __init__(self, submits: AsyncSubmits) -> None:
        self._submits = submits

        self.phishing_url_scanner_submit_suspicious_url_for_scanning = async_to_raw_response_wrapper(
            submits.phishing_url_scanner_submit_suspicious_url_for_scanning,
        )


class SubmitsWithStreamingResponse:
    def __init__(self, submits: Submits) -> None:
        self._submits = submits

        self.phishing_url_scanner_submit_suspicious_url_for_scanning = to_streamed_response_wrapper(
            submits.phishing_url_scanner_submit_suspicious_url_for_scanning,
        )


class AsyncSubmitsWithStreamingResponse:
    def __init__(self, submits: AsyncSubmits) -> None:
        self._submits = submits

        self.phishing_url_scanner_submit_suspicious_url_for_scanning = async_to_streamed_response_wrapper(
            submits.phishing_url_scanner_submit_suspicious_url_for_scanning,
        )
