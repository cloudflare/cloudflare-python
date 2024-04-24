# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ......_wrappers import ResultWrapper
from ......_base_client import (
    make_request_options,
)
from ......types.workers_for_platforms.dispatch.namespaces.scripts.binding_get_response import BindingGetResponse

__all__ = ["BindingsResource", "AsyncBindingsResource"]


class BindingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BindingsResourceWithRawResponse:
        return BindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BindingsResourceWithStreamingResponse:
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
    ) -> Optional[BindingGetResponse]:
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
        return self._get(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/bindings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BindingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BindingGetResponse]], ResultWrapper[BindingGetResponse]),
        )


class AsyncBindingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBindingsResourceWithRawResponse:
        return AsyncBindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBindingsResourceWithStreamingResponse:
        return AsyncBindingsResourceWithStreamingResponse(self)

    async def get(
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
    ) -> Optional[BindingGetResponse]:
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
        return await self._get(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/bindings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BindingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BindingGetResponse]], ResultWrapper[BindingGetResponse]),
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
