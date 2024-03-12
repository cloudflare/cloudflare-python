# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime

import httpx

from .scans import (
    Scans,
    AsyncScans,
    ScansWithRawResponse,
    AsyncScansWithRawResponse,
    ScansWithStreamingResponse,
    AsyncScansWithStreamingResponse,
)
from ...types import URLScannerScanResponse, url_scanner_scan_params
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

__all__ = ["URLScanner", "AsyncURLScanner"]


class URLScanner(SyncAPIResource):
    @cached_property
    def scans(self) -> Scans:
        return Scans(self._client)

    @cached_property
    def with_raw_response(self) -> URLScannerWithRawResponse:
        return URLScannerWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLScannerWithStreamingResponse:
        return URLScannerWithStreamingResponse(self)

    def scan(
        self,
        account_id: str,
        *,
        account_scans: bool | NotGiven = NOT_GIVEN,
        asn: str | NotGiven = NOT_GIVEN,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
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

          hostname: Filter scans by hostname of _any_ request made by the webpage.

          ip: Filter scans by IP address (IPv4 or IPv6) of _any_ request made by the webpage.

          is_malicious: Filter scans by malicious verdict.

          limit: Limit the number of objects in the response.

          next_cursor: Pagination cursor to get the next set of results.

          page_asn: Filter scans by main page Autonomous System Number (ASN).

          page_hostname: Filter scans by main page hostname .

          page_ip: Filter scans by main page IP address (IPv4 or IPv6).

          page_path: Filter scans by exact match URL path (also supports suffix search).

          page_url: Filter scans by exact match to scanned URL (_after redirects_)

          path: Filter scans by url path of _any_ request made by the webpage.

          scan_id: Scan uuid

          url: Filter scans by exact match URL of _any_ request made by the webpage

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[URLScannerScanResponse], ResultWrapper[URLScannerScanResponse]),
        )


class AsyncURLScanner(AsyncAPIResource):
    @cached_property
    def scans(self) -> AsyncScans:
        return AsyncScans(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncURLScannerWithRawResponse:
        return AsyncURLScannerWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLScannerWithStreamingResponse:
        return AsyncURLScannerWithStreamingResponse(self)

    async def scan(
        self,
        account_id: str,
        *,
        account_scans: bool | NotGiven = NOT_GIVEN,
        asn: str | NotGiven = NOT_GIVEN,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
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

          hostname: Filter scans by hostname of _any_ request made by the webpage.

          ip: Filter scans by IP address (IPv4 or IPv6) of _any_ request made by the webpage.

          is_malicious: Filter scans by malicious verdict.

          limit: Limit the number of objects in the response.

          next_cursor: Pagination cursor to get the next set of results.

          page_asn: Filter scans by main page Autonomous System Number (ASN).

          page_hostname: Filter scans by main page hostname .

          page_ip: Filter scans by main page IP address (IPv4 or IPv6).

          page_path: Filter scans by exact match URL path (also supports suffix search).

          page_url: Filter scans by exact match to scanned URL (_after redirects_)

          path: Filter scans by url path of _any_ request made by the webpage.

          scan_id: Scan uuid

          url: Filter scans by exact match URL of _any_ request made by the webpage

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[URLScannerScanResponse], ResultWrapper[URLScannerScanResponse]),
        )


class URLScannerWithRawResponse:
    def __init__(self, url_scanner: URLScanner) -> None:
        self._url_scanner = url_scanner

        self.scan = to_raw_response_wrapper(
            url_scanner.scan,
        )

    @cached_property
    def scans(self) -> ScansWithRawResponse:
        return ScansWithRawResponse(self._url_scanner.scans)


class AsyncURLScannerWithRawResponse:
    def __init__(self, url_scanner: AsyncURLScanner) -> None:
        self._url_scanner = url_scanner

        self.scan = async_to_raw_response_wrapper(
            url_scanner.scan,
        )

    @cached_property
    def scans(self) -> AsyncScansWithRawResponse:
        return AsyncScansWithRawResponse(self._url_scanner.scans)


class URLScannerWithStreamingResponse:
    def __init__(self, url_scanner: URLScanner) -> None:
        self._url_scanner = url_scanner

        self.scan = to_streamed_response_wrapper(
            url_scanner.scan,
        )

    @cached_property
    def scans(self) -> ScansWithStreamingResponse:
        return ScansWithStreamingResponse(self._url_scanner.scans)


class AsyncURLScannerWithStreamingResponse:
    def __init__(self, url_scanner: AsyncURLScanner) -> None:
        self._url_scanner = url_scanner

        self.scan = async_to_streamed_response_wrapper(
            url_scanner.scan,
        )

    @cached_property
    def scans(self) -> AsyncScansWithStreamingResponse:
        return AsyncScansWithStreamingResponse(self._url_scanner.scans)
