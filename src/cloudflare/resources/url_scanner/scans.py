# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Type, Union, cast
from datetime import datetime
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
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.url_scanner import scan_get_params, scan_list_params, scan_create_params, scan_screenshot_params
from ...types.url_scanner.scan_get_response import ScanGetResponse
from ...types.url_scanner.scan_har_response import ScanHARResponse
from ...types.url_scanner.scan_list_response import ScanListResponse
from ...types.url_scanner.scan_create_response import ScanCreateResponse

__all__ = ["ScansResource", "AsyncScansResource"]


class ScansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ScansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ScansResourceWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        url: str,
        custom_headers: Dict[str, str] | NotGiven = NOT_GIVEN,
        screenshots_resolutions: List[Literal["desktop", "mobile", "tablet"]] | NotGiven = NOT_GIVEN,
        visibility: Literal["Public", "Unlisted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanCreateResponse:
        """Submit a URL to scan.

        You can also set some options, like the visibility level
        and custom headers. Check limits at
        https://developers.cloudflare.com/security-center/investigate/scan-limits/.

        Args:
          account_id: Account Id.

          custom_headers: Set custom headers.

          screenshots_resolutions: Take multiple screenshots targeting different device types.

          visibility: The option `Public` means it will be included in listings like recent scans and
              search results. `Unlisted` means it will not be included in the aforementioned
              listings, users will need to have the scan's ID to access it. A a scan will be
              automatically marked as unlisted if it fails, if it contains potential PII or
              other sensitive material.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/urlscanner/scan",
            body=maybe_transform(
                {
                    "url": url,
                    "custom_headers": custom_headers,
                    "screenshots_resolutions": screenshots_resolutions,
                    "visibility": visibility,
                },
                scan_create_params.ScanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ScanCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScanCreateResponse], ResultWrapper[ScanCreateResponse]),
        )

    def list(
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
    ) -> ScanListResponse:
        """
        Search scans by date and webpages' requests, including full URL (after
        redirects), hostname, and path. <br/> A successful scan will appear in search
        results a few minutes after finishing but may take much longer if the system in
        under load. By default, only successfully completed scans will appear in search
        results, unless searching by `scanId`. Please take into account that older scans
        may be removed from the search index at an unspecified time.

        Args:
          account_id: Account Id.

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
                    scan_list_params.ScanListParams,
                ),
                post_parser=ResultWrapper[ScanListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScanListResponse], ResultWrapper[ScanListResponse]),
        )

    def get(
        self,
        scan_id: str,
        *,
        account_id: str,
        full: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanGetResponse:
        """
        Get URL scan by uuid

        Args:
          account_id: Account Id.

          scan_id: Scan uuid.

          full: Whether to return full report (scan summary and network log).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return self._get(
            f"/accounts/{account_id}/urlscanner/scan/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"full": full}, scan_get_params.ScanGetParams),
                post_parser=ResultWrapper[ScanGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScanGetResponse], ResultWrapper[ScanGetResponse]),
        )

    def har(
        self,
        scan_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanHARResponse:
        """Get a URL scan's HAR file.

        See HAR spec at
        http://www.softwareishard.com/blog/har-12-spec/.

        Args:
          account_id: Account Id.

          scan_id: Scan uuid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return self._get(
            f"/accounts/{account_id}/urlscanner/scan/{scan_id}/har",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ScanHARResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScanHARResponse], ResultWrapper[ScanHARResponse]),
        )

    def screenshot(
        self,
        scan_id: str,
        *,
        account_id: str,
        resolution: Literal["desktop", "mobile", "tablet"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Get scan's screenshot by resolution (desktop/mobile/tablet).

        Args:
          account_id: Account Id.

          scan_id: Scan uuid.

          resolution: Target device type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/urlscanner/scan/{scan_id}/screenshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"resolution": resolution}, scan_screenshot_params.ScanScreenshotParams),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncScansResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncScansResourceWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        url: str,
        custom_headers: Dict[str, str] | NotGiven = NOT_GIVEN,
        screenshots_resolutions: List[Literal["desktop", "mobile", "tablet"]] | NotGiven = NOT_GIVEN,
        visibility: Literal["Public", "Unlisted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanCreateResponse:
        """Submit a URL to scan.

        You can also set some options, like the visibility level
        and custom headers. Check limits at
        https://developers.cloudflare.com/security-center/investigate/scan-limits/.

        Args:
          account_id: Account Id.

          custom_headers: Set custom headers.

          screenshots_resolutions: Take multiple screenshots targeting different device types.

          visibility: The option `Public` means it will be included in listings like recent scans and
              search results. `Unlisted` means it will not be included in the aforementioned
              listings, users will need to have the scan's ID to access it. A a scan will be
              automatically marked as unlisted if it fails, if it contains potential PII or
              other sensitive material.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/urlscanner/scan",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "custom_headers": custom_headers,
                    "screenshots_resolutions": screenshots_resolutions,
                    "visibility": visibility,
                },
                scan_create_params.ScanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ScanCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScanCreateResponse], ResultWrapper[ScanCreateResponse]),
        )

    async def list(
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
    ) -> ScanListResponse:
        """
        Search scans by date and webpages' requests, including full URL (after
        redirects), hostname, and path. <br/> A successful scan will appear in search
        results a few minutes after finishing but may take much longer if the system in
        under load. By default, only successfully completed scans will appear in search
        results, unless searching by `scanId`. Please take into account that older scans
        may be removed from the search index at an unspecified time.

        Args:
          account_id: Account Id.

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
                    scan_list_params.ScanListParams,
                ),
                post_parser=ResultWrapper[ScanListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScanListResponse], ResultWrapper[ScanListResponse]),
        )

    async def get(
        self,
        scan_id: str,
        *,
        account_id: str,
        full: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanGetResponse:
        """
        Get URL scan by uuid

        Args:
          account_id: Account Id.

          scan_id: Scan uuid.

          full: Whether to return full report (scan summary and network log).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return await self._get(
            f"/accounts/{account_id}/urlscanner/scan/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"full": full}, scan_get_params.ScanGetParams),
                post_parser=ResultWrapper[ScanGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScanGetResponse], ResultWrapper[ScanGetResponse]),
        )

    async def har(
        self,
        scan_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanHARResponse:
        """Get a URL scan's HAR file.

        See HAR spec at
        http://www.softwareishard.com/blog/har-12-spec/.

        Args:
          account_id: Account Id.

          scan_id: Scan uuid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return await self._get(
            f"/accounts/{account_id}/urlscanner/scan/{scan_id}/har",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ScanHARResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScanHARResponse], ResultWrapper[ScanHARResponse]),
        )

    async def screenshot(
        self,
        scan_id: str,
        *,
        account_id: str,
        resolution: Literal["desktop", "mobile", "tablet"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Get scan's screenshot by resolution (desktop/mobile/tablet).

        Args:
          account_id: Account Id.

          scan_id: Scan uuid.

          resolution: Target device type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/urlscanner/scan/{scan_id}/screenshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"resolution": resolution}, scan_screenshot_params.ScanScreenshotParams
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ScansResourceWithRawResponse:
    def __init__(self, scans: ScansResource) -> None:
        self._scans = scans

        self.create = to_raw_response_wrapper(
            scans.create,
        )
        self.list = to_raw_response_wrapper(
            scans.list,
        )
        self.get = to_raw_response_wrapper(
            scans.get,
        )
        self.har = to_raw_response_wrapper(
            scans.har,
        )
        self.screenshot = to_custom_raw_response_wrapper(
            scans.screenshot,
            BinaryAPIResponse,
        )


class AsyncScansResourceWithRawResponse:
    def __init__(self, scans: AsyncScansResource) -> None:
        self._scans = scans

        self.create = async_to_raw_response_wrapper(
            scans.create,
        )
        self.list = async_to_raw_response_wrapper(
            scans.list,
        )
        self.get = async_to_raw_response_wrapper(
            scans.get,
        )
        self.har = async_to_raw_response_wrapper(
            scans.har,
        )
        self.screenshot = async_to_custom_raw_response_wrapper(
            scans.screenshot,
            AsyncBinaryAPIResponse,
        )


class ScansResourceWithStreamingResponse:
    def __init__(self, scans: ScansResource) -> None:
        self._scans = scans

        self.create = to_streamed_response_wrapper(
            scans.create,
        )
        self.list = to_streamed_response_wrapper(
            scans.list,
        )
        self.get = to_streamed_response_wrapper(
            scans.get,
        )
        self.har = to_streamed_response_wrapper(
            scans.har,
        )
        self.screenshot = to_custom_streamed_response_wrapper(
            scans.screenshot,
            StreamedBinaryAPIResponse,
        )


class AsyncScansResourceWithStreamingResponse:
    def __init__(self, scans: AsyncScansResource) -> None:
        self._scans = scans

        self.create = async_to_streamed_response_wrapper(
            scans.create,
        )
        self.list = async_to_streamed_response_wrapper(
            scans.list,
        )
        self.get = async_to_streamed_response_wrapper(
            scans.get,
        )
        self.har = async_to_streamed_response_wrapper(
            scans.har,
        )
        self.screenshot = async_to_custom_streamed_response_wrapper(
            scans.screenshot,
            AsyncStreamedBinaryAPIResponse,
        )
