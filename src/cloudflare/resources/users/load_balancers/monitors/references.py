# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.users.load_balancers.monitors import ReferenceLoadBalancerMonitorsListMonitorReferencesResponse

__all__ = ["References", "AsyncReferences"]


class References(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReferencesWithRawResponse:
        return ReferencesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReferencesWithStreamingResponse:
        return ReferencesWithStreamingResponse(self)

    def load_balancer_monitors_list_monitor_references(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ReferenceLoadBalancerMonitorsListMonitorReferencesResponse]:
        """
        Get the list of resources that reference the provided monitor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/user/load_balancers/monitors/{identifier}/references",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ReferenceLoadBalancerMonitorsListMonitorReferencesResponse]],
                ResultWrapper[ReferenceLoadBalancerMonitorsListMonitorReferencesResponse],
            ),
        )


class AsyncReferences(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReferencesWithRawResponse:
        return AsyncReferencesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReferencesWithStreamingResponse:
        return AsyncReferencesWithStreamingResponse(self)

    async def load_balancer_monitors_list_monitor_references(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ReferenceLoadBalancerMonitorsListMonitorReferencesResponse]:
        """
        Get the list of resources that reference the provided monitor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/user/load_balancers/monitors/{identifier}/references",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ReferenceLoadBalancerMonitorsListMonitorReferencesResponse]],
                ResultWrapper[ReferenceLoadBalancerMonitorsListMonitorReferencesResponse],
            ),
        )


class ReferencesWithRawResponse:
    def __init__(self, references: References) -> None:
        self._references = references

        self.load_balancer_monitors_list_monitor_references = to_raw_response_wrapper(
            references.load_balancer_monitors_list_monitor_references,
        )


class AsyncReferencesWithRawResponse:
    def __init__(self, references: AsyncReferences) -> None:
        self._references = references

        self.load_balancer_monitors_list_monitor_references = async_to_raw_response_wrapper(
            references.load_balancer_monitors_list_monitor_references,
        )


class ReferencesWithStreamingResponse:
    def __init__(self, references: References) -> None:
        self._references = references

        self.load_balancer_monitors_list_monitor_references = to_streamed_response_wrapper(
            references.load_balancer_monitors_list_monitor_references,
        )


class AsyncReferencesWithStreamingResponse:
    def __init__(self, references: AsyncReferences) -> None:
        self._references = references

        self.load_balancer_monitors_list_monitor_references = async_to_streamed_response_wrapper(
            references.load_balancer_monitors_list_monitor_references,
        )
