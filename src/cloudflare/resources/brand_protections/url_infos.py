# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.brand_protections import (
    URLInfoPhishingURLInformationGetResultsForAURLScanResponse,
    url_info_phishing_url_information_get_results_for_a_url_scan_params,
)

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
from ...types.brand_protections import url_info_phishing_url_information_get_results_for_a_url_scan_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["URLInfos", "AsyncURLInfos"]


class URLInfos(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLInfosWithRawResponse:
        return URLInfosWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLInfosWithStreamingResponse:
        return URLInfosWithStreamingResponse(self)

    def phishing_url_information_get_results_for_a_url_scan(
        self,
        account_id: str,
        *,
        url: str | NotGiven = NOT_GIVEN,
        url_id_param: url_info_phishing_url_information_get_results_for_a_url_scan_params.URLIDParam
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLInfoPhishingURLInformationGetResultsForAURLScanResponse:
        """
        Get results for a URL scan

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/brand-protection/url-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "url_id_param": url_id_param,
                    },
                    url_info_phishing_url_information_get_results_for_a_url_scan_params.URLInfoPhishingURLInformationGetResultsForAURLScanParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[URLInfoPhishingURLInformationGetResultsForAURLScanResponse],
                ResultWrapper[URLInfoPhishingURLInformationGetResultsForAURLScanResponse],
            ),
        )


class AsyncURLInfos(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLInfosWithRawResponse:
        return AsyncURLInfosWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLInfosWithStreamingResponse:
        return AsyncURLInfosWithStreamingResponse(self)

    async def phishing_url_information_get_results_for_a_url_scan(
        self,
        account_id: str,
        *,
        url: str | NotGiven = NOT_GIVEN,
        url_id_param: url_info_phishing_url_information_get_results_for_a_url_scan_params.URLIDParam
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLInfoPhishingURLInformationGetResultsForAURLScanResponse:
        """
        Get results for a URL scan

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/brand-protection/url-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "url_id_param": url_id_param,
                    },
                    url_info_phishing_url_information_get_results_for_a_url_scan_params.URLInfoPhishingURLInformationGetResultsForAURLScanParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[URLInfoPhishingURLInformationGetResultsForAURLScanResponse],
                ResultWrapper[URLInfoPhishingURLInformationGetResultsForAURLScanResponse],
            ),
        )


class URLInfosWithRawResponse:
    def __init__(self, url_infos: URLInfos) -> None:
        self._url_infos = url_infos

        self.phishing_url_information_get_results_for_a_url_scan = to_raw_response_wrapper(
            url_infos.phishing_url_information_get_results_for_a_url_scan,
        )


class AsyncURLInfosWithRawResponse:
    def __init__(self, url_infos: AsyncURLInfos) -> None:
        self._url_infos = url_infos

        self.phishing_url_information_get_results_for_a_url_scan = async_to_raw_response_wrapper(
            url_infos.phishing_url_information_get_results_for_a_url_scan,
        )


class URLInfosWithStreamingResponse:
    def __init__(self, url_infos: URLInfos) -> None:
        self._url_infos = url_infos

        self.phishing_url_information_get_results_for_a_url_scan = to_streamed_response_wrapper(
            url_infos.phishing_url_information_get_results_for_a_url_scan,
        )


class AsyncURLInfosWithStreamingResponse:
    def __init__(self, url_infos: AsyncURLInfos) -> None:
        self._url_infos = url_infos

        self.phishing_url_information_get_results_for_a_url_scan = async_to_streamed_response_wrapper(
            url_infos.phishing_url_information_get_results_for_a_url_scan,
        )
