# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.devices import (
    DEXTestUpdateResponse,
    DEXTestDeleteResponse,
    DEXTestDeviceDEXTestCreateDeviceDEXTestResponse,
    DEXTestDeviceDEXTestDetailsResponse,
    DEXTestGetResponse,
    dex_test_update_params,
    dex_test_device_dex_test_create_device_dex_test_params,
)

from typing import Type, Optional

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
from ...types.devices import dex_test_update_params
from ...types.devices import dex_test_device_dex_test_create_device_dex_test_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["DEXTests", "AsyncDEXTests"]


class DEXTests(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DEXTestsWithRawResponse:
        return DEXTestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DEXTestsWithStreamingResponse:
        return DEXTestsWithStreamingResponse(self)

    def update(
        self,
        uuid: str,
        *,
        identifier: object,
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
    ) -> Optional[DEXTestUpdateResponse]:
        """
        Update a DEX test.

        Args:
          uuid: API UUID.

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
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._put(
            f"/accounts/{identifier}/devices/dex_tests/{uuid}",
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
            cast_to=cast(Type[Optional[DEXTestUpdateResponse]], ResultWrapper[DEXTestUpdateResponse]),
        )

    def delete(
        self,
        uuid: str,
        *,
        identifier: object,
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
          uuid: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._delete(
            f"/accounts/{identifier}/devices/dex_tests/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DEXTestDeleteResponse]], ResultWrapper[DEXTestDeleteResponse]),
        )

    def device_dex_test_create_device_dex_test(
        self,
        identifier: object,
        *,
        data: dex_test_device_dex_test_create_device_dex_test_params.Data,
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
    ) -> Optional[DEXTestDeviceDEXTestCreateDeviceDEXTestResponse]:
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
        return self._post(
            f"/accounts/{identifier}/devices/dex_tests",
            body=maybe_transform(
                {
                    "data": data,
                    "enabled": enabled,
                    "interval": interval,
                    "name": name,
                    "description": description,
                },
                dex_test_device_dex_test_create_device_dex_test_params.DEXTestDeviceDEXTestCreateDeviceDEXTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[DEXTestDeviceDEXTestCreateDeviceDEXTestResponse]],
                ResultWrapper[DEXTestDeviceDEXTestCreateDeviceDEXTestResponse],
            ),
        )

    def device_dex_test_details(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DEXTestDeviceDEXTestDetailsResponse]:
        """
        Fetch all DEX tests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{identifier}/devices/dex_tests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[DEXTestDeviceDEXTestDetailsResponse]], ResultWrapper[DEXTestDeviceDEXTestDetailsResponse]
            ),
        )

    def get(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DEXTestGetResponse]:
        """
        Fetch a single DEX test.

        Args:
          uuid: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/accounts/{identifier}/devices/dex_tests/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DEXTestGetResponse]], ResultWrapper[DEXTestGetResponse]),
        )


class AsyncDEXTests(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDEXTestsWithRawResponse:
        return AsyncDEXTestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDEXTestsWithStreamingResponse:
        return AsyncDEXTestsWithStreamingResponse(self)

    async def update(
        self,
        uuid: str,
        *,
        identifier: object,
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
    ) -> Optional[DEXTestUpdateResponse]:
        """
        Update a DEX test.

        Args:
          uuid: API UUID.

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
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._put(
            f"/accounts/{identifier}/devices/dex_tests/{uuid}",
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
            cast_to=cast(Type[Optional[DEXTestUpdateResponse]], ResultWrapper[DEXTestUpdateResponse]),
        )

    async def delete(
        self,
        uuid: str,
        *,
        identifier: object,
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
          uuid: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._delete(
            f"/accounts/{identifier}/devices/dex_tests/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DEXTestDeleteResponse]], ResultWrapper[DEXTestDeleteResponse]),
        )

    async def device_dex_test_create_device_dex_test(
        self,
        identifier: object,
        *,
        data: dex_test_device_dex_test_create_device_dex_test_params.Data,
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
    ) -> Optional[DEXTestDeviceDEXTestCreateDeviceDEXTestResponse]:
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
        return await self._post(
            f"/accounts/{identifier}/devices/dex_tests",
            body=maybe_transform(
                {
                    "data": data,
                    "enabled": enabled,
                    "interval": interval,
                    "name": name,
                    "description": description,
                },
                dex_test_device_dex_test_create_device_dex_test_params.DEXTestDeviceDEXTestCreateDeviceDEXTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[DEXTestDeviceDEXTestCreateDeviceDEXTestResponse]],
                ResultWrapper[DEXTestDeviceDEXTestCreateDeviceDEXTestResponse],
            ),
        )

    async def device_dex_test_details(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DEXTestDeviceDEXTestDetailsResponse]:
        """
        Fetch all DEX tests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{identifier}/devices/dex_tests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[DEXTestDeviceDEXTestDetailsResponse]], ResultWrapper[DEXTestDeviceDEXTestDetailsResponse]
            ),
        )

    async def get(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DEXTestGetResponse]:
        """
        Fetch a single DEX test.

        Args:
          uuid: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/accounts/{identifier}/devices/dex_tests/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DEXTestGetResponse]], ResultWrapper[DEXTestGetResponse]),
        )


class DEXTestsWithRawResponse:
    def __init__(self, dex_tests: DEXTests) -> None:
        self._dex_tests = dex_tests

        self.update = to_raw_response_wrapper(
            dex_tests.update,
        )
        self.delete = to_raw_response_wrapper(
            dex_tests.delete,
        )
        self.device_dex_test_create_device_dex_test = to_raw_response_wrapper(
            dex_tests.device_dex_test_create_device_dex_test,
        )
        self.device_dex_test_details = to_raw_response_wrapper(
            dex_tests.device_dex_test_details,
        )
        self.get = to_raw_response_wrapper(
            dex_tests.get,
        )


class AsyncDEXTestsWithRawResponse:
    def __init__(self, dex_tests: AsyncDEXTests) -> None:
        self._dex_tests = dex_tests

        self.update = async_to_raw_response_wrapper(
            dex_tests.update,
        )
        self.delete = async_to_raw_response_wrapper(
            dex_tests.delete,
        )
        self.device_dex_test_create_device_dex_test = async_to_raw_response_wrapper(
            dex_tests.device_dex_test_create_device_dex_test,
        )
        self.device_dex_test_details = async_to_raw_response_wrapper(
            dex_tests.device_dex_test_details,
        )
        self.get = async_to_raw_response_wrapper(
            dex_tests.get,
        )


class DEXTestsWithStreamingResponse:
    def __init__(self, dex_tests: DEXTests) -> None:
        self._dex_tests = dex_tests

        self.update = to_streamed_response_wrapper(
            dex_tests.update,
        )
        self.delete = to_streamed_response_wrapper(
            dex_tests.delete,
        )
        self.device_dex_test_create_device_dex_test = to_streamed_response_wrapper(
            dex_tests.device_dex_test_create_device_dex_test,
        )
        self.device_dex_test_details = to_streamed_response_wrapper(
            dex_tests.device_dex_test_details,
        )
        self.get = to_streamed_response_wrapper(
            dex_tests.get,
        )


class AsyncDEXTestsWithStreamingResponse:
    def __init__(self, dex_tests: AsyncDEXTests) -> None:
        self._dex_tests = dex_tests

        self.update = async_to_streamed_response_wrapper(
            dex_tests.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            dex_tests.delete,
        )
        self.device_dex_test_create_device_dex_test = async_to_streamed_response_wrapper(
            dex_tests.device_dex_test_create_device_dex_test,
        )
        self.device_dex_test_details = async_to_streamed_response_wrapper(
            dex_tests.device_dex_test_details,
        )
        self.get = async_to_streamed_response_wrapper(
            dex_tests.get,
        )
