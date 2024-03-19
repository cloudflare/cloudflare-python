# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncV4PagePagination, AsyncV4PagePagination
from .unique_devices import (
    UniqueDevices,
    AsyncUniqueDevices,
    UniqueDevicesWithRawResponse,
    AsyncUniqueDevicesWithRawResponse,
    UniqueDevicesWithStreamingResponse,
    AsyncUniqueDevicesWithStreamingResponse,
)
from ....._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .....types.zero_trust.dex import TestListResponse, test_list_params

__all__ = ["Tests", "AsyncTests"]


class Tests(SyncAPIResource):
    __test__ = False

    @cached_property
    def unique_devices(self) -> UniqueDevices:
        return UniqueDevices(self._client)

    @cached_property
    def with_raw_response(self) -> TestsWithRawResponse:
        return TestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestsWithStreamingResponse:
        return TestsWithStreamingResponse(self)

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


class AsyncTests(AsyncAPIResource):
    @cached_property
    def unique_devices(self) -> AsyncUniqueDevices:
        return AsyncUniqueDevices(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTestsWithRawResponse:
        return AsyncTestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestsWithStreamingResponse:
        return AsyncTestsWithStreamingResponse(self)

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


class TestsWithRawResponse:
    __test__ = False

    def __init__(self, tests: Tests) -> None:
        self._tests = tests

        self.list = to_raw_response_wrapper(
            tests.list,
        )

    @cached_property
    def unique_devices(self) -> UniqueDevicesWithRawResponse:
        return UniqueDevicesWithRawResponse(self._tests.unique_devices)


class AsyncTestsWithRawResponse:
    def __init__(self, tests: AsyncTests) -> None:
        self._tests = tests

        self.list = async_to_raw_response_wrapper(
            tests.list,
        )

    @cached_property
    def unique_devices(self) -> AsyncUniqueDevicesWithRawResponse:
        return AsyncUniqueDevicesWithRawResponse(self._tests.unique_devices)


class TestsWithStreamingResponse:
    __test__ = False

    def __init__(self, tests: Tests) -> None:
        self._tests = tests

        self.list = to_streamed_response_wrapper(
            tests.list,
        )

    @cached_property
    def unique_devices(self) -> UniqueDevicesWithStreamingResponse:
        return UniqueDevicesWithStreamingResponse(self._tests.unique_devices)


class AsyncTestsWithStreamingResponse:
    def __init__(self, tests: AsyncTests) -> None:
        self._tests = tests

        self.list = async_to_streamed_response_wrapper(
            tests.list,
        )

    @cached_property
    def unique_devices(self) -> AsyncUniqueDevicesWithStreamingResponse:
        return AsyncUniqueDevicesWithStreamingResponse(self._tests.unique_devices)
