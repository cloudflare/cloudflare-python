# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......pagination import SyncSinglePage, AsyncSinglePage
from ......_base_client import AsyncPaginator, make_request_options
from ......types.workers_for_platforms.dispatch.namespaces.scripts.binding_get_response import BindingGetResponse

__all__ = ["BindingsResource", "AsyncBindingsResource"]


class BindingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BindingsResourceWithStreamingResponse(self)

    def get(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[BindingGetResponse]:
        """
        Fetch script bindings from a script uploaded to a Workers for Platforms
        namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/bindings",
            page=SyncSinglePage[BindingGetResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, BindingGetResponse),  # Union types cannot be passed in as arguments in the type system
        )


class AsyncBindingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBindingsResourceWithStreamingResponse(self)

    def get(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BindingGetResponse, AsyncSinglePage[BindingGetResponse]]:
        """
        Fetch script bindings from a script uploaded to a Workers for Platforms
        namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/bindings",
            page=AsyncSinglePage[BindingGetResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, BindingGetResponse),  # Union types cannot be passed in as arguments in the type system
        )


class BindingsResourceWithRawResponse:
    def __init__(self, bindings: BindingsResource) -> None:
        self._bindings = bindings

        self.get = to_raw_response_wrapper(
            bindings.get,
        )


class AsyncBindingsResourceWithRawResponse:
    def __init__(self, bindings: AsyncBindingsResource) -> None:
        self._bindings = bindings

        self.get = async_to_raw_response_wrapper(
            bindings.get,
        )


class BindingsResourceWithStreamingResponse:
    def __init__(self, bindings: BindingsResource) -> None:
        self._bindings = bindings

        self.get = to_streamed_response_wrapper(
            bindings.get,
        )


class AsyncBindingsResourceWithStreamingResponse:
    def __init__(self, bindings: AsyncBindingsResource) -> None:
        self._bindings = bindings

        self.get = async_to_streamed_response_wrapper(
            bindings.get,
        )
