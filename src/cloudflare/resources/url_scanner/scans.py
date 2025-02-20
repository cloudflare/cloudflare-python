# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Type, Iterable, cast
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
from ...types.url_scanner import scan_list_params, scan_create_params, scan_screenshot_params, scan_bulk_create_params
from ...types.url_scanner.scan_get_response import ScanGetResponse
from ...types.url_scanner.scan_har_response import ScanHARResponse
from ...types.url_scanner.scan_list_response import ScanListResponse
from ...types.url_scanner.scan_create_response import ScanCreateResponse
from ...types.url_scanner.scan_bulk_create_response import ScanBulkCreateResponse

__all__ = ["ScansResource", "AsyncScansResource"]


class ScansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        *,
        account_id: str,
        url: str,
        customagent: str | NotGiven = NOT_GIVEN,
        custom_headers: Dict[str, str] | NotGiven = NOT_GIVEN,
        referer: str | NotGiven = NOT_GIVEN,
        screenshots_resolutions: List[Literal["desktop", "mobile", "tablet"]] | NotGiven = NOT_GIVEN,
        visibility: Literal["Public", "Unlisted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Submit a URL to scan.

        Check limits at
        https://developers.cloudflare.com/security-center/investigate/scan-limits/.

        Args:
          account_id: Account ID.

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
            f"/accounts/{account_id}/urlscanner/v2/scan",
            body=maybe_transform(
                {
                    "url": url,
                    "customagent": customagent,
                    "custom_headers": custom_headers,
                    "referer": referer,
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
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def list(
        self,
        *,
        account_id: str,
        q: str | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanListResponse:
        """Use a subset of ElasticSearch Query syntax to filter scans.

        Some example
        queries:<br/> <br/>- 'path:"/bundles/jquery.js"': Searches for scans who
        requested resources with the given path.<br/>- 'page.asn:AS24940 AND hash:xxx':
        Websites hosted in AS24940 where a resource with the given hash was
        downloaded.<br/>- 'page.domain:microsoft\\** AND verdicts.malicious:true AND NOT
        page.domain:microsoft.com': malicious scans whose hostname starts with
        "microsoft".<br/>- 'apikey:me AND date:[2025-01 TO 2025-02]': my scans from 2025
        January to 2025 February.

        Args:
          account_id: Account ID.

          q: Filter scans

          size: Limit the number of objects in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/urlscanner/v2/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "size": size,
                    },
                    scan_list_params.ScanListParams,
                ),
            ),
            cast_to=ScanListResponse,
        )

    def bulk_create(
        self,
        *,
        account_id: str,
        body: Iterable[scan_bulk_create_params.Body] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanBulkCreateResponse:
        """Submit URLs to scan.

        Check limits at
        https://developers.cloudflare.com/security-center/investigate/scan-limits/ and
        take into account scans submitted in bulk have lower priority and may take
        longer to finish.

        Args:
          account_id: Account ID.

          body: List of urls to scan (up to a 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/urlscanner/v2/bulk",
            body=maybe_transform(body, Iterable[scan_bulk_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScanBulkCreateResponse,
        )

    def dom(
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
    ) -> str:
        """
        Returns a plain text response, with the scan's DOM content as rendered by
        Chrome.

        Args:
          account_id: Account ID.

          scan_id: Scan UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/urlscanner/v2/dom/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def get(
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
    ) -> ScanGetResponse:
        """
        Get URL scan by uuid

        Args:
          account_id: Account ID.

          scan_id: Scan UUID.

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
            f"/accounts/{account_id}/urlscanner/v2/result/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScanGetResponse,
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
          account_id: Account ID.

          scan_id: Scan UUID.

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
            f"/accounts/{account_id}/urlscanner/v2/har/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScanHARResponse,
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
          account_id: Account ID.

          scan_id: Scan UUID.

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
            f"/accounts/{account_id}/urlscanner/v2/screenshots/{scan_id}.png",
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
        This property can be used as a prefix for any HTTP method call to return
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
        *,
        account_id: str,
        url: str,
        customagent: str | NotGiven = NOT_GIVEN,
        custom_headers: Dict[str, str] | NotGiven = NOT_GIVEN,
        referer: str | NotGiven = NOT_GIVEN,
        screenshots_resolutions: List[Literal["desktop", "mobile", "tablet"]] | NotGiven = NOT_GIVEN,
        visibility: Literal["Public", "Unlisted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Submit a URL to scan.

        Check limits at
        https://developers.cloudflare.com/security-center/investigate/scan-limits/.

        Args:
          account_id: Account ID.

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
            f"/accounts/{account_id}/urlscanner/v2/scan",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "customagent": customagent,
                    "custom_headers": custom_headers,
                    "referer": referer,
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
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def list(
        self,
        *,
        account_id: str,
        q: str | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanListResponse:
        """Use a subset of ElasticSearch Query syntax to filter scans.

        Some example
        queries:<br/> <br/>- 'path:"/bundles/jquery.js"': Searches for scans who
        requested resources with the given path.<br/>- 'page.asn:AS24940 AND hash:xxx':
        Websites hosted in AS24940 where a resource with the given hash was
        downloaded.<br/>- 'page.domain:microsoft\\** AND verdicts.malicious:true AND NOT
        page.domain:microsoft.com': malicious scans whose hostname starts with
        "microsoft".<br/>- 'apikey:me AND date:[2025-01 TO 2025-02]': my scans from 2025
        January to 2025 February.

        Args:
          account_id: Account ID.

          q: Filter scans

          size: Limit the number of objects in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/urlscanner/v2/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "size": size,
                    },
                    scan_list_params.ScanListParams,
                ),
            ),
            cast_to=ScanListResponse,
        )

    async def bulk_create(
        self,
        *,
        account_id: str,
        body: Iterable[scan_bulk_create_params.Body] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanBulkCreateResponse:
        """Submit URLs to scan.

        Check limits at
        https://developers.cloudflare.com/security-center/investigate/scan-limits/ and
        take into account scans submitted in bulk have lower priority and may take
        longer to finish.

        Args:
          account_id: Account ID.

          body: List of urls to scan (up to a 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/urlscanner/v2/bulk",
            body=await async_maybe_transform(body, Iterable[scan_bulk_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScanBulkCreateResponse,
        )

    async def dom(
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
    ) -> str:
        """
        Returns a plain text response, with the scan's DOM content as rendered by
        Chrome.

        Args:
          account_id: Account ID.

          scan_id: Scan UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/urlscanner/v2/dom/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def get(
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
    ) -> ScanGetResponse:
        """
        Get URL scan by uuid

        Args:
          account_id: Account ID.

          scan_id: Scan UUID.

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
            f"/accounts/{account_id}/urlscanner/v2/result/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScanGetResponse,
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
          account_id: Account ID.

          scan_id: Scan UUID.

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
            f"/accounts/{account_id}/urlscanner/v2/har/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScanHARResponse,
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
          account_id: Account ID.

          scan_id: Scan UUID.

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
            f"/accounts/{account_id}/urlscanner/v2/screenshots/{scan_id}.png",
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
        self.bulk_create = to_raw_response_wrapper(
            scans.bulk_create,
        )
        self.dom = to_raw_response_wrapper(
            scans.dom,
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
        self.bulk_create = async_to_raw_response_wrapper(
            scans.bulk_create,
        )
        self.dom = async_to_raw_response_wrapper(
            scans.dom,
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
        self.bulk_create = to_streamed_response_wrapper(
            scans.bulk_create,
        )
        self.dom = to_streamed_response_wrapper(
            scans.dom,
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
        self.bulk_create = async_to_streamed_response_wrapper(
            scans.bulk_create,
        )
        self.dom = async_to_streamed_response_wrapper(
            scans.dom,
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
