# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

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
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.users.load_balancers import (
    MonitorLoadBalancerMonitorsListMonitorsResponse,
    MonitorLoadBalancerMonitorsCreateMonitorResponse,
    monitor_load_balancer_monitors_create_monitor_params,
)

__all__ = ["Monitors", "AsyncMonitors"]


class Monitors(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MonitorsWithRawResponse:
        return MonitorsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MonitorsWithStreamingResponse:
        return MonitorsWithStreamingResponse(self)

    def load_balancer_monitors_create_monitor(
        self,
        *,
        expected_codes: str,
        allow_insecure: bool | NotGiven = NOT_GIVEN,
        consecutive_down: int | NotGiven = NOT_GIVEN,
        consecutive_up: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        expected_body: str | NotGiven = NOT_GIVEN,
        follow_redirects: bool | NotGiven = NOT_GIVEN,
        header: object | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        method: str | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        port: int | NotGiven = NOT_GIVEN,
        probe_zone: str | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        api_timeout: int | NotGiven = NOT_GIVEN,
        type: Literal["http", "https", "tcp", "udp_icmp", "icmp_ping", "smtp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MonitorLoadBalancerMonitorsCreateMonitorResponse:
        """
        Create a configured monitor.

        Args:
          expected_codes: The expected HTTP response code or code range of the health check. This
              parameter is only valid for HTTP and HTTPS monitors.

          allow_insecure: Do not validate the certificate when monitor use HTTPS. This parameter is
              currently only valid for HTTP and HTTPS monitors.

          consecutive_down: To be marked unhealthy the monitored origin must fail this healthcheck N
              consecutive times.

          consecutive_up: To be marked healthy the monitored origin must pass this healthcheck N
              consecutive times.

          description: Object description.

          expected_body: A case-insensitive sub-string to look for in the response body. If this string
              is not found, the origin will be marked as unhealthy. This parameter is only
              valid for HTTP and HTTPS monitors.

          follow_redirects: Follow redirects if returned by the origin. This parameter is only valid for
              HTTP and HTTPS monitors.

          header: The HTTP request headers to send in the health check. It is recommended you set
              a Host header by default. The User-Agent header cannot be overridden. This
              parameter is only valid for HTTP and HTTPS monitors.

          interval: The interval between each health check. Shorter intervals may improve failover
              time, but will increase load on the origins as we check from multiple locations.

          method: The method to use for the health check. This defaults to 'GET' for HTTP/HTTPS
              based checks and 'connection_established' for TCP based health checks.

          path: The endpoint path you want to conduct a health check against. This parameter is
              only valid for HTTP and HTTPS monitors.

          port: The port number to connect to for the health check. Required for TCP, UDP, and
              SMTP checks. HTTP and HTTPS checks should only define the port when using a
              non-standard port (HTTP: default 80, HTTPS: default 443).

          probe_zone: Assign this monitor to emulate the specified zone while probing. This parameter
              is only valid for HTTP and HTTPS monitors.

          retries: The number of retries to attempt in case of a timeout before marking the origin
              as unhealthy. Retries are attempted immediately.

          api_timeout: The timeout (in seconds) before marking the health check as failed.

          type: The protocol to use for the health check. Currently supported protocols are
              'HTTP','HTTPS', 'TCP', 'ICMP-PING', 'UDP-ICMP', and 'SMTP'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user/load_balancers/monitors",
            body=maybe_transform(
                {
                    "expected_codes": expected_codes,
                    "allow_insecure": allow_insecure,
                    "consecutive_down": consecutive_down,
                    "consecutive_up": consecutive_up,
                    "description": description,
                    "expected_body": expected_body,
                    "follow_redirects": follow_redirects,
                    "header": header,
                    "interval": interval,
                    "method": method,
                    "path": path,
                    "port": port,
                    "probe_zone": probe_zone,
                    "retries": retries,
                    "timeout": api_timeout,
                    "type": type,
                },
                monitor_load_balancer_monitors_create_monitor_params.MonitorLoadBalancerMonitorsCreateMonitorParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[MonitorLoadBalancerMonitorsCreateMonitorResponse],
                ResultWrapper[MonitorLoadBalancerMonitorsCreateMonitorResponse],
            ),
        )

    def load_balancer_monitors_list_monitors(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MonitorLoadBalancerMonitorsListMonitorsResponse]:
        """List configured monitors for a user."""
        return self._get(
            "/user/load_balancers/monitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[MonitorLoadBalancerMonitorsListMonitorsResponse]],
                ResultWrapper[MonitorLoadBalancerMonitorsListMonitorsResponse],
            ),
        )


class AsyncMonitors(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMonitorsWithRawResponse:
        return AsyncMonitorsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMonitorsWithStreamingResponse:
        return AsyncMonitorsWithStreamingResponse(self)

    async def load_balancer_monitors_create_monitor(
        self,
        *,
        expected_codes: str,
        allow_insecure: bool | NotGiven = NOT_GIVEN,
        consecutive_down: int | NotGiven = NOT_GIVEN,
        consecutive_up: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        expected_body: str | NotGiven = NOT_GIVEN,
        follow_redirects: bool | NotGiven = NOT_GIVEN,
        header: object | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        method: str | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        port: int | NotGiven = NOT_GIVEN,
        probe_zone: str | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        api_timeout: int | NotGiven = NOT_GIVEN,
        type: Literal["http", "https", "tcp", "udp_icmp", "icmp_ping", "smtp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MonitorLoadBalancerMonitorsCreateMonitorResponse:
        """
        Create a configured monitor.

        Args:
          expected_codes: The expected HTTP response code or code range of the health check. This
              parameter is only valid for HTTP and HTTPS monitors.

          allow_insecure: Do not validate the certificate when monitor use HTTPS. This parameter is
              currently only valid for HTTP and HTTPS monitors.

          consecutive_down: To be marked unhealthy the monitored origin must fail this healthcheck N
              consecutive times.

          consecutive_up: To be marked healthy the monitored origin must pass this healthcheck N
              consecutive times.

          description: Object description.

          expected_body: A case-insensitive sub-string to look for in the response body. If this string
              is not found, the origin will be marked as unhealthy. This parameter is only
              valid for HTTP and HTTPS monitors.

          follow_redirects: Follow redirects if returned by the origin. This parameter is only valid for
              HTTP and HTTPS monitors.

          header: The HTTP request headers to send in the health check. It is recommended you set
              a Host header by default. The User-Agent header cannot be overridden. This
              parameter is only valid for HTTP and HTTPS monitors.

          interval: The interval between each health check. Shorter intervals may improve failover
              time, but will increase load on the origins as we check from multiple locations.

          method: The method to use for the health check. This defaults to 'GET' for HTTP/HTTPS
              based checks and 'connection_established' for TCP based health checks.

          path: The endpoint path you want to conduct a health check against. This parameter is
              only valid for HTTP and HTTPS monitors.

          port: The port number to connect to for the health check. Required for TCP, UDP, and
              SMTP checks. HTTP and HTTPS checks should only define the port when using a
              non-standard port (HTTP: default 80, HTTPS: default 443).

          probe_zone: Assign this monitor to emulate the specified zone while probing. This parameter
              is only valid for HTTP and HTTPS monitors.

          retries: The number of retries to attempt in case of a timeout before marking the origin
              as unhealthy. Retries are attempted immediately.

          api_timeout: The timeout (in seconds) before marking the health check as failed.

          type: The protocol to use for the health check. Currently supported protocols are
              'HTTP','HTTPS', 'TCP', 'ICMP-PING', 'UDP-ICMP', and 'SMTP'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user/load_balancers/monitors",
            body=maybe_transform(
                {
                    "expected_codes": expected_codes,
                    "allow_insecure": allow_insecure,
                    "consecutive_down": consecutive_down,
                    "consecutive_up": consecutive_up,
                    "description": description,
                    "expected_body": expected_body,
                    "follow_redirects": follow_redirects,
                    "header": header,
                    "interval": interval,
                    "method": method,
                    "path": path,
                    "port": port,
                    "probe_zone": probe_zone,
                    "retries": retries,
                    "timeout": api_timeout,
                    "type": type,
                },
                monitor_load_balancer_monitors_create_monitor_params.MonitorLoadBalancerMonitorsCreateMonitorParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[MonitorLoadBalancerMonitorsCreateMonitorResponse],
                ResultWrapper[MonitorLoadBalancerMonitorsCreateMonitorResponse],
            ),
        )

    async def load_balancer_monitors_list_monitors(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MonitorLoadBalancerMonitorsListMonitorsResponse]:
        """List configured monitors for a user."""
        return await self._get(
            "/user/load_balancers/monitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[MonitorLoadBalancerMonitorsListMonitorsResponse]],
                ResultWrapper[MonitorLoadBalancerMonitorsListMonitorsResponse],
            ),
        )


class MonitorsWithRawResponse:
    def __init__(self, monitors: Monitors) -> None:
        self._monitors = monitors

        self.load_balancer_monitors_create_monitor = to_raw_response_wrapper(
            monitors.load_balancer_monitors_create_monitor,
        )
        self.load_balancer_monitors_list_monitors = to_raw_response_wrapper(
            monitors.load_balancer_monitors_list_monitors,
        )


class AsyncMonitorsWithRawResponse:
    def __init__(self, monitors: AsyncMonitors) -> None:
        self._monitors = monitors

        self.load_balancer_monitors_create_monitor = async_to_raw_response_wrapper(
            monitors.load_balancer_monitors_create_monitor,
        )
        self.load_balancer_monitors_list_monitors = async_to_raw_response_wrapper(
            monitors.load_balancer_monitors_list_monitors,
        )


class MonitorsWithStreamingResponse:
    def __init__(self, monitors: Monitors) -> None:
        self._monitors = monitors

        self.load_balancer_monitors_create_monitor = to_streamed_response_wrapper(
            monitors.load_balancer_monitors_create_monitor,
        )
        self.load_balancer_monitors_list_monitors = to_streamed_response_wrapper(
            monitors.load_balancer_monitors_list_monitors,
        )


class AsyncMonitorsWithStreamingResponse:
    def __init__(self, monitors: AsyncMonitors) -> None:
        self._monitors = monitors

        self.load_balancer_monitors_create_monitor = async_to_streamed_response_wrapper(
            monitors.load_balancer_monitors_create_monitor,
        )
        self.load_balancer_monitors_list_monitors = async_to_streamed_response_wrapper(
            monitors.load_balancer_monitors_list_monitors,
        )
