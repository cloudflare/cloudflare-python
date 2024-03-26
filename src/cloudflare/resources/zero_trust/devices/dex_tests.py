# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.zero_trust.devices import (
    DEXTestListResponse,
    DEXTestDeleteResponse,
    TeamsDevicesDeviceDEXTestSchemasHTTP,
    dex_test_create_params,
    dex_test_update_params,
)

__all__ = ["DEXTests", "AsyncDEXTests"]


class DEXTests(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DEXTestsWithRawResponse:
        return DEXTestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DEXTestsWithStreamingResponse:
        return DEXTestsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        data: dex_test_create_params.Data,
        enabled: bool,
        interval: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDeviceDEXTestSchemasHTTP]:
        """
        Create a DEX test.

        Args:
          data: The configuration object which contains the details for the WARP client to
              conduct the test.

          enabled: Determines whether or not the test is active.

          interval: How often the test will run.

          name: The name of the DEX test. Must be unique.

          description: Additional details about the test.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/devices/dex_tests",
            body=maybe_transform(
                {
                    "data": data,
                    "enabled": enabled,
                    "interval": interval,
                    "name": name,
                    "description": description,
                },
                dex_test_create_params.DEXTestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDeviceDEXTestSchemasHTTP]],
                ResultWrapper[TeamsDevicesDeviceDEXTestSchemasHTTP],
            ),
        )

    def update(
        self,
        dex_test_id: str,
        *,
        account_id: str,
        data: dex_test_update_params.Data,
        enabled: bool,
        interval: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDeviceDEXTestSchemasHTTP]:
        """
        Update a DEX test.

        Args:
          dex_test_id: API UUID.

          data: The configuration object which contains the details for the WARP client to
              conduct the test.

          enabled: Determines whether or not the test is active.

          interval: How often the test will run.

          name: The name of the DEX test. Must be unique.

          description: Additional details about the test.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dex_test_id:
            raise ValueError(f"Expected a non-empty value for `dex_test_id` but received {dex_test_id!r}")
        return self._put(
            f"/accounts/{account_id}/devices/dex_tests/{dex_test_id}",
            body=maybe_transform(
                {
                    "data": data,
                    "enabled": enabled,
                    "interval": interval,
                    "name": name,
                    "description": description,
                },
                dex_test_update_params.DEXTestUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDeviceDEXTestSchemasHTTP]],
                ResultWrapper[TeamsDevicesDeviceDEXTestSchemasHTTP],
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DEXTestListResponse]:
        """
        Fetch all DEX tests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/dex_tests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DEXTestListResponse]], ResultWrapper[DEXTestListResponse]),
        )

    def delete(
        self,
        dex_test_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DEXTestDeleteResponse]:
        """Delete a Device DEX test.

        Returns the remaining device dex tests for the
        account.

        Args:
          dex_test_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dex_test_id:
            raise ValueError(f"Expected a non-empty value for `dex_test_id` but received {dex_test_id!r}")
        return self._delete(
            f"/accounts/{account_id}/devices/dex_tests/{dex_test_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DEXTestDeleteResponse]], ResultWrapper[DEXTestDeleteResponse]),
        )

    def get(
        self,
        dex_test_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDeviceDEXTestSchemasHTTP]:
        """
        Fetch a single DEX test.

        Args:
          dex_test_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dex_test_id:
            raise ValueError(f"Expected a non-empty value for `dex_test_id` but received {dex_test_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/dex_tests/{dex_test_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDeviceDEXTestSchemasHTTP]],
                ResultWrapper[TeamsDevicesDeviceDEXTestSchemasHTTP],
            ),
        )


class AsyncDEXTests(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDEXTestsWithRawResponse:
        return AsyncDEXTestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDEXTestsWithStreamingResponse:
        return AsyncDEXTestsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        data: dex_test_create_params.Data,
        enabled: bool,
        interval: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDeviceDEXTestSchemasHTTP]:
        """
        Create a DEX test.

        Args:
          data: The configuration object which contains the details for the WARP client to
              conduct the test.

          enabled: Determines whether or not the test is active.

          interval: How often the test will run.

          name: The name of the DEX test. Must be unique.

          description: Additional details about the test.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/devices/dex_tests",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "enabled": enabled,
                    "interval": interval,
                    "name": name,
                    "description": description,
                },
                dex_test_create_params.DEXTestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDeviceDEXTestSchemasHTTP]],
                ResultWrapper[TeamsDevicesDeviceDEXTestSchemasHTTP],
            ),
        )

    async def update(
        self,
        dex_test_id: str,
        *,
        account_id: str,
        data: dex_test_update_params.Data,
        enabled: bool,
        interval: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDeviceDEXTestSchemasHTTP]:
        """
        Update a DEX test.

        Args:
          dex_test_id: API UUID.

          data: The configuration object which contains the details for the WARP client to
              conduct the test.

          enabled: Determines whether or not the test is active.

          interval: How often the test will run.

          name: The name of the DEX test. Must be unique.

          description: Additional details about the test.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dex_test_id:
            raise ValueError(f"Expected a non-empty value for `dex_test_id` but received {dex_test_id!r}")
        return await self._put(
            f"/accounts/{account_id}/devices/dex_tests/{dex_test_id}",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "enabled": enabled,
                    "interval": interval,
                    "name": name,
                    "description": description,
                },
                dex_test_update_params.DEXTestUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDeviceDEXTestSchemasHTTP]],
                ResultWrapper[TeamsDevicesDeviceDEXTestSchemasHTTP],
            ),
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DEXTestListResponse]:
        """
        Fetch all DEX tests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/dex_tests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DEXTestListResponse]], ResultWrapper[DEXTestListResponse]),
        )

    async def delete(
        self,
        dex_test_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DEXTestDeleteResponse]:
        """Delete a Device DEX test.

        Returns the remaining device dex tests for the
        account.

        Args:
          dex_test_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dex_test_id:
            raise ValueError(f"Expected a non-empty value for `dex_test_id` but received {dex_test_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/devices/dex_tests/{dex_test_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DEXTestDeleteResponse]], ResultWrapper[DEXTestDeleteResponse]),
        )

    async def get(
        self,
        dex_test_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDeviceDEXTestSchemasHTTP]:
        """
        Fetch a single DEX test.

        Args:
          dex_test_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dex_test_id:
            raise ValueError(f"Expected a non-empty value for `dex_test_id` but received {dex_test_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/dex_tests/{dex_test_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDeviceDEXTestSchemasHTTP]],
                ResultWrapper[TeamsDevicesDeviceDEXTestSchemasHTTP],
            ),
        )


class DEXTestsWithRawResponse:
    def __init__(self, dex_tests: DEXTests) -> None:
        self._dex_tests = dex_tests

        self.create = to_raw_response_wrapper(
            dex_tests.create,
        )
        self.update = to_raw_response_wrapper(
            dex_tests.update,
        )
        self.list = to_raw_response_wrapper(
            dex_tests.list,
        )
        self.delete = to_raw_response_wrapper(
            dex_tests.delete,
        )
        self.get = to_raw_response_wrapper(
            dex_tests.get,
        )


class AsyncDEXTestsWithRawResponse:
    def __init__(self, dex_tests: AsyncDEXTests) -> None:
        self._dex_tests = dex_tests

        self.create = async_to_raw_response_wrapper(
            dex_tests.create,
        )
        self.update = async_to_raw_response_wrapper(
            dex_tests.update,
        )
        self.list = async_to_raw_response_wrapper(
            dex_tests.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dex_tests.delete,
        )
        self.get = async_to_raw_response_wrapper(
            dex_tests.get,
        )


class DEXTestsWithStreamingResponse:
    def __init__(self, dex_tests: DEXTests) -> None:
        self._dex_tests = dex_tests

        self.create = to_streamed_response_wrapper(
            dex_tests.create,
        )
        self.update = to_streamed_response_wrapper(
            dex_tests.update,
        )
        self.list = to_streamed_response_wrapper(
            dex_tests.list,
        )
        self.delete = to_streamed_response_wrapper(
            dex_tests.delete,
        )
        self.get = to_streamed_response_wrapper(
            dex_tests.get,
        )


class AsyncDEXTestsWithStreamingResponse:
    def __init__(self, dex_tests: AsyncDEXTests) -> None:
        self._dex_tests = dex_tests

        self.create = async_to_streamed_response_wrapper(
            dex_tests.create,
        )
        self.update = async_to_streamed_response_wrapper(
            dex_tests.update,
        )
        self.list = async_to_streamed_response_wrapper(
            dex_tests.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dex_tests.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            dex_tests.get,
        )
