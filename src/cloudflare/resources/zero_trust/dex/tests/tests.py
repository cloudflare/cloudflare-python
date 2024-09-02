# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .unique_devices import UniqueDevicesResource, AsyncUniqueDevicesResource

from ....._compat import cached_property

from .....types.zero_trust.dex.test_list_response import TestListResponse

from .....pagination import SyncV4PagePagination, AsyncV4PagePagination

from ....._utils import maybe_transform

from ....._base_client import make_request_options, AsyncPaginator

from typing import List

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.zero_trust.dex import test_list_params
from .unique_devices import (
    UniqueDevicesResource,
    AsyncUniqueDevicesResource,
    UniqueDevicesResourceWithRawResponse,
    AsyncUniqueDevicesResourceWithRawResponse,
    UniqueDevicesResourceWithStreamingResponse,
    AsyncUniqueDevicesResourceWithStreamingResponse,
)

__all__ = ["TestsResource", "AsyncTestsResource"]


class TestsResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def unique_devices(self) -> UniqueDevicesResource:
        return UniqueDevicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TestsResourceWithRawResponse:
        return TestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestsResourceWithStreamingResponse:
        return TestsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        colo: str | NotGiven = NOT_GIVEN,
        device_id: List[str] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        test_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePagination[TestListResponse]:
        """
        List DEX tests

        Args:
          colo: Optionally filter result stats to a Cloudflare colo. Cannot be used in
              combination with deviceId param.

          device_id: Optionally filter result stats to a specific device(s). Cannot be used in
              combination with colo param.

          page: Page number of paginated results

          per_page: Number of items per page

          test_name: Optionally filter results by test name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dex/tests",
            page=SyncV4PagePagination[TestListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "colo": colo,
                        "device_id": device_id,
                        "page": page,
                        "per_page": per_page,
                        "test_name": test_name,
                    },
                    test_list_params.TestListParams,
                ),
            ),
            model=TestListResponse,
        )


class AsyncTestsResource(AsyncAPIResource):
    @cached_property
    def unique_devices(self) -> AsyncUniqueDevicesResource:
        return AsyncUniqueDevicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTestsResourceWithRawResponse:
        return AsyncTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestsResourceWithStreamingResponse:
        return AsyncTestsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        colo: str | NotGiven = NOT_GIVEN,
        device_id: List[str] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        test_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TestListResponse, AsyncV4PagePagination[TestListResponse]]:
        """
        List DEX tests

        Args:
          colo: Optionally filter result stats to a Cloudflare colo. Cannot be used in
              combination with deviceId param.

          device_id: Optionally filter result stats to a specific device(s). Cannot be used in
              combination with colo param.

          page: Page number of paginated results

          per_page: Number of items per page

          test_name: Optionally filter results by test name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dex/tests",
            page=AsyncV4PagePagination[TestListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "colo": colo,
                        "device_id": device_id,
                        "page": page,
                        "per_page": per_page,
                        "test_name": test_name,
                    },
                    test_list_params.TestListParams,
                ),
            ),
            model=TestListResponse,
        )


class TestsResourceWithRawResponse:
    __test__ = False

    def __init__(self, tests: TestsResource) -> None:
        self._tests = tests

        self.list = to_raw_response_wrapper(
            tests.list,
        )

    @cached_property
    def unique_devices(self) -> UniqueDevicesResourceWithRawResponse:
        return UniqueDevicesResourceWithRawResponse(self._tests.unique_devices)


class AsyncTestsResourceWithRawResponse:
    def __init__(self, tests: AsyncTestsResource) -> None:
        self._tests = tests

        self.list = async_to_raw_response_wrapper(
            tests.list,
        )

    @cached_property
    def unique_devices(self) -> AsyncUniqueDevicesResourceWithRawResponse:
        return AsyncUniqueDevicesResourceWithRawResponse(self._tests.unique_devices)


class TestsResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, tests: TestsResource) -> None:
        self._tests = tests

        self.list = to_streamed_response_wrapper(
            tests.list,
        )

    @cached_property
    def unique_devices(self) -> UniqueDevicesResourceWithStreamingResponse:
        return UniqueDevicesResourceWithStreamingResponse(self._tests.unique_devices)


class AsyncTestsResourceWithStreamingResponse:
    def __init__(self, tests: AsyncTestsResource) -> None:
        self._tests = tests

        self.list = async_to_streamed_response_wrapper(
            tests.list,
        )

    @cached_property
    def unique_devices(self) -> AsyncUniqueDevicesResourceWithStreamingResponse:
        return AsyncUniqueDevicesResourceWithStreamingResponse(self._tests.unique_devices)
