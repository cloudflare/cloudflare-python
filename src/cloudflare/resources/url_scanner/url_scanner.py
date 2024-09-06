# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .scans import ScansResource, AsyncScansResource

from ..._compat import cached_property

from ...types.url_scanner.url_scanner_scan_response import URLScannerScanResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from typing import Type, Union

from datetime import datetime

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
from ...types.url_scanner import url_scanner_scan_params
from .scans import (
    ScansResource,
    AsyncScansResource,
    ScansResourceWithRawResponse,
    AsyncScansResourceWithRawResponse,
    ScansResourceWithStreamingResponse,
    AsyncScansResourceWithStreamingResponse,
)
from typing import cast
from typing import cast

__all__ = ["URLScannerResource", "AsyncURLScannerResource"]


class URLScannerResource(SyncAPIResource):
    @cached_property
    def scans(self) -> ScansResource:
        return ScansResource(self._client)

    @cached_property
    def with_raw_response(self) -> URLScannerResourceWithRawResponse:
        return URLScannerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLScannerResourceWithStreamingResponse:
        return URLScannerResourceWithStreamingResponse(self)

    def scan(
        self,
        account_id: str,
        *,
        account_scans: bool | NotGiven = NOT_GIVEN,
        asn: str | NotGiven = NOT_GIVEN,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        hash: str | NotGiven = NOT_GIVEN,
        hostname: str | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        is_malicious: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        next_cursor: str | NotGiven = NOT_GIVEN,
        page_asn: str | NotGiven = NOT_GIVEN,
        page_hostname: str | NotGiven = NOT_GIVEN,
        page_ip: str | NotGiven = NOT_GIVEN,
        page_path: str | NotGiven = NOT_GIVEN,
        page_url: str | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        scan_id: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLScannerScanResponse:
        """
        Search scans by date and webpages' requests, including full URL (after
        redirects), hostname, and path. <br/> A successful scan will appear in search
        results a few minutes after finishing but may take much longer if the system in
        under load. By default, only successfully completed scans will appear in search
        results, unless searching by `scanId`. Please take into account that older scans
        may be removed from the search index at an unspecified time.

        Args:
          account_id: Account Id

          account_scans: Return only scans created by account.

          asn: Filter scans by Autonomous System Number (ASN) of _any_ request made by the
              webpage.

          date_end: Filter scans requested before date (inclusive).

          date_start: Filter scans requested after date (inclusive).

          hash: Filter scans by hash of any html/js/css request made by the webpage.

          hostname: Filter scans by hostname of _any_ request made by the webpage.

          ip: Filter scans by IP address (IPv4 or IPv6) of _any_ request made by the webpage.

          is_malicious: Filter scans by malicious verdict.

          limit: Limit the number of objects in the response.

          next_cursor: Pagination cursor to get the next set of results.

          page_asn: Filter scans by main page Autonomous System Number (ASN).

          page_hostname: Filter scans by main page hostname (domain of effective URL).

          page_ip: Filter scans by main page IP address (IPv4 or IPv6).

          page_path: Filter scans by exact match of effective URL path (also supports suffix search).

          page_url: Filter scans by submitted or scanned URL

          path: Filter scans by url path of _any_ request made by the webpage.

          scan_id: Scan uuid

          url: Filter scans by URL of _any_ request made by the webpage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/urlscanner/scan",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_scans": account_scans,
                        "asn": asn,
                        "date_end": date_end,
                        "date_start": date_start,
                        "hash": hash,
                        "hostname": hostname,
                        "ip": ip,
                        "is_malicious": is_malicious,
                        "limit": limit,
                        "next_cursor": next_cursor,
                        "page_asn": page_asn,
                        "page_hostname": page_hostname,
                        "page_ip": page_ip,
                        "page_path": page_path,
                        "page_url": page_url,
                        "path": path,
                        "scan_id": scan_id,
                        "url": url,
                    },
                    url_scanner_scan_params.URLScannerScanParams,
                ),
                post_parser=ResultWrapper[URLScannerScanResponse]._unwrapper,
            ),
            cast_to=cast(Type[URLScannerScanResponse], ResultWrapper[URLScannerScanResponse]),
        )


class AsyncURLScannerResource(AsyncAPIResource):
    @cached_property
    def scans(self) -> AsyncScansResource:
        return AsyncScansResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncURLScannerResourceWithRawResponse:
        return AsyncURLScannerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLScannerResourceWithStreamingResponse:
        return AsyncURLScannerResourceWithStreamingResponse(self)

    async def scan(
        self,
        account_id: str,
        *,
        account_scans: bool | NotGiven = NOT_GIVEN,
        asn: str | NotGiven = NOT_GIVEN,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        hash: str | NotGiven = NOT_GIVEN,
        hostname: str | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        is_malicious: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        next_cursor: str | NotGiven = NOT_GIVEN,
        page_asn: str | NotGiven = NOT_GIVEN,
        page_hostname: str | NotGiven = NOT_GIVEN,
        page_ip: str | NotGiven = NOT_GIVEN,
        page_path: str | NotGiven = NOT_GIVEN,
        page_url: str | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        scan_id: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLScannerScanResponse:
        """
        Search scans by date and webpages' requests, including full URL (after
        redirects), hostname, and path. <br/> A successful scan will appear in search
        results a few minutes after finishing but may take much longer if the system in
        under load. By default, only successfully completed scans will appear in search
        results, unless searching by `scanId`. Please take into account that older scans
        may be removed from the search index at an unspecified time.

        Args:
          account_id: Account Id

          account_scans: Return only scans created by account.

          asn: Filter scans by Autonomous System Number (ASN) of _any_ request made by the
              webpage.

          date_end: Filter scans requested before date (inclusive).

          date_start: Filter scans requested after date (inclusive).

          hash: Filter scans by hash of any html/js/css request made by the webpage.

          hostname: Filter scans by hostname of _any_ request made by the webpage.

          ip: Filter scans by IP address (IPv4 or IPv6) of _any_ request made by the webpage.

          is_malicious: Filter scans by malicious verdict.

          limit: Limit the number of objects in the response.

          next_cursor: Pagination cursor to get the next set of results.

          page_asn: Filter scans by main page Autonomous System Number (ASN).

          page_hostname: Filter scans by main page hostname (domain of effective URL).

          page_ip: Filter scans by main page IP address (IPv4 or IPv6).

          page_path: Filter scans by exact match of effective URL path (also supports suffix search).

          page_url: Filter scans by submitted or scanned URL

          path: Filter scans by url path of _any_ request made by the webpage.

          scan_id: Scan uuid

          url: Filter scans by URL of _any_ request made by the webpage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/urlscanner/scan",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_scans": account_scans,
                        "asn": asn,
                        "date_end": date_end,
                        "date_start": date_start,
                        "hash": hash,
                        "hostname": hostname,
                        "ip": ip,
                        "is_malicious": is_malicious,
                        "limit": limit,
                        "next_cursor": next_cursor,
                        "page_asn": page_asn,
                        "page_hostname": page_hostname,
                        "page_ip": page_ip,
                        "page_path": page_path,
                        "page_url": page_url,
                        "path": path,
                        "scan_id": scan_id,
                        "url": url,
                    },
                    url_scanner_scan_params.URLScannerScanParams,
                ),
                post_parser=ResultWrapper[URLScannerScanResponse]._unwrapper,
            ),
            cast_to=cast(Type[URLScannerScanResponse], ResultWrapper[URLScannerScanResponse]),
        )


class URLScannerResourceWithRawResponse:
    def __init__(self, url_scanner: URLScannerResource) -> None:
        self._url_scanner = url_scanner

        self.scan = to_raw_response_wrapper(
            url_scanner.scan,
        )

    @cached_property
    def scans(self) -> ScansResourceWithRawResponse:
        return ScansResourceWithRawResponse(self._url_scanner.scans)


class AsyncURLScannerResourceWithRawResponse:
    def __init__(self, url_scanner: AsyncURLScannerResource) -> None:
        self._url_scanner = url_scanner

        self.scan = async_to_raw_response_wrapper(
            url_scanner.scan,
        )

    @cached_property
    def scans(self) -> AsyncScansResourceWithRawResponse:
        return AsyncScansResourceWithRawResponse(self._url_scanner.scans)


class URLScannerResourceWithStreamingResponse:
    def __init__(self, url_scanner: URLScannerResource) -> None:
        self._url_scanner = url_scanner

        self.scan = to_streamed_response_wrapper(
            url_scanner.scan,
        )

    @cached_property
    def scans(self) -> ScansResourceWithStreamingResponse:
        return ScansResourceWithStreamingResponse(self._url_scanner.scans)


class AsyncURLScannerResourceWithStreamingResponse:
    def __init__(self, url_scanner: AsyncURLScannerResource) -> None:
        self._url_scanner = url_scanner

        self.scan = async_to_streamed_response_wrapper(
            url_scanner.scan,
        )

    @cached_property
    def scans(self) -> AsyncScansResourceWithStreamingResponse:
        return AsyncScansResourceWithStreamingResponse(self._url_scanner.scans)
