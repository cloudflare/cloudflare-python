# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.url_scanner.scan_create_response import ScanCreateResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from typing import Type, Dict, List

from typing_extensions import Literal

from ...types.url_scanner.scan_get_response import ScanGetResponse

from ...types.url_scanner.scan_har_response import ScanHarResponse

from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_custom_raw_response_wrapper,
    to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    StreamedBinaryAPIResponse,
    async_to_streamed_response_wrapper,
    async_to_custom_streamed_response_wrapper,
    AsyncStreamedBinaryAPIResponse,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.url_scanner import scan_create_params
from ...types.url_scanner import scan_get_params
from ...types.url_scanner import scan_screenshot_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ScansResource", "AsyncScansResource"]


class ScansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScansResourceWithRawResponse:
        return ScansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScansResourceWithStreamingResponse:
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
          account_id: Account Id

          custom_headers: Set custom headers

          screenshots_resolutions: Take multiple screenshots targeting different device types

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
          account_id: Account Id

          scan_id: Scan uuid

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
    ) -> ScanHarResponse:
        """Get a URL scan's HAR file.

        See HAR spec at
        http://www.softwareishard.com/blog/har-12-spec/.

        Args:
          account_id: Account Id

          scan_id: Scan uuid

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
                post_parser=ResultWrapper[ScanHarResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScanHarResponse], ResultWrapper[ScanHarResponse]),
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
          account_id: Account Id

          scan_id: Scan uuid

          resolution: Target device type

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
        return AsyncScansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScansResourceWithStreamingResponse:
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
          account_id: Account Id

          custom_headers: Set custom headers

          screenshots_resolutions: Take multiple screenshots targeting different device types

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
          account_id: Account Id

          scan_id: Scan uuid

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
    ) -> ScanHarResponse:
        """Get a URL scan's HAR file.

        See HAR spec at
        http://www.softwareishard.com/blog/har-12-spec/.

        Args:
          account_id: Account Id

          scan_id: Scan uuid

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
                post_parser=ResultWrapper[ScanHarResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScanHarResponse], ResultWrapper[ScanHarResponse]),
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
          account_id: Account Id

          scan_id: Scan uuid

          resolution: Target device type

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
