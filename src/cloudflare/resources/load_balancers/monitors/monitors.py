# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .previews import Previews, AsyncPreviews

from ...._compat import cached_property

from .references import References, AsyncReferences

from ....types.load_balancers import (
    MonitorUpdateResponse,
    MonitorDeleteResponse,
    MonitorAccountLoadBalancerMonitorsCreateMonitorResponse,
    MonitorAccountLoadBalancerMonitorsListMonitorsResponse,
    MonitorGetResponse,
)

from typing import Type, Optional

from typing_extensions import Literal

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.load_balancers import monitor_update_params
from ....types.load_balancers import monitor_account_load_balancer_monitors_create_monitor_params
from .previews import (
    Previews,
    AsyncPreviews,
    PreviewsWithRawResponse,
    AsyncPreviewsWithRawResponse,
    PreviewsWithStreamingResponse,
    AsyncPreviewsWithStreamingResponse,
)
from .references import (
    References,
    AsyncReferences,
    ReferencesWithRawResponse,
    AsyncReferencesWithRawResponse,
    ReferencesWithStreamingResponse,
    AsyncReferencesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
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

__all__ = ["Monitors", "AsyncMonitors"]


class Monitors(SyncAPIResource):
    @cached_property
    def previews(self) -> Previews:
        return Previews(self._client)

    @cached_property
    def references(self) -> References:
        return References(self._client)

    @cached_property
    def with_raw_response(self) -> MonitorsWithRawResponse:
        return MonitorsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MonitorsWithStreamingResponse:
        return MonitorsWithStreamingResponse(self)

    def update(
        self,
        identifier: str,
        *,
        account_identifier: str,
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
    ) -> MonitorUpdateResponse:
        """
        Modify a configured monitor.

        Args:
          account_identifier: Identifier

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
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._put(
            f"/accounts/{account_identifier}/load_balancers/monitors/{identifier}",
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
                monitor_update_params.MonitorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[MonitorUpdateResponse], ResultWrapper[MonitorUpdateResponse]),
        )

    def delete(
        self,
        identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MonitorDeleteResponse:
        """
        Delete a configured monitor.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._delete(
            f"/accounts/{account_identifier}/load_balancers/monitors/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[MonitorDeleteResponse], ResultWrapper[MonitorDeleteResponse]),
        )

    def account_load_balancer_monitors_create_monitor(
        self,
        account_identifier: str,
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
    ) -> MonitorAccountLoadBalancerMonitorsCreateMonitorResponse:
        """
        Create a configured monitor.

        Args:
          account_identifier: Identifier

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
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/load_balancers/monitors",
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
                monitor_account_load_balancer_monitors_create_monitor_params.MonitorAccountLoadBalancerMonitorsCreateMonitorParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[MonitorAccountLoadBalancerMonitorsCreateMonitorResponse],
                ResultWrapper[MonitorAccountLoadBalancerMonitorsCreateMonitorResponse],
            ),
        )

    def account_load_balancer_monitors_list_monitors(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MonitorAccountLoadBalancerMonitorsListMonitorsResponse]:
        """
        List configured monitors for an account.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/load_balancers/monitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[MonitorAccountLoadBalancerMonitorsListMonitorsResponse]],
                ResultWrapper[MonitorAccountLoadBalancerMonitorsListMonitorsResponse],
            ),
        )

    def get(
        self,
        identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MonitorGetResponse:
        """
        List a single configured monitor for an account.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/load_balancers/monitors/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[MonitorGetResponse], ResultWrapper[MonitorGetResponse]),
        )


class AsyncMonitors(AsyncAPIResource):
    @cached_property
    def previews(self) -> AsyncPreviews:
        return AsyncPreviews(self._client)

    @cached_property
    def references(self) -> AsyncReferences:
        return AsyncReferences(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMonitorsWithRawResponse:
        return AsyncMonitorsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMonitorsWithStreamingResponse:
        return AsyncMonitorsWithStreamingResponse(self)

    async def update(
        self,
        identifier: str,
        *,
        account_identifier: str,
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
    ) -> MonitorUpdateResponse:
        """
        Modify a configured monitor.

        Args:
          account_identifier: Identifier

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
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._put(
            f"/accounts/{account_identifier}/load_balancers/monitors/{identifier}",
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
                monitor_update_params.MonitorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[MonitorUpdateResponse], ResultWrapper[MonitorUpdateResponse]),
        )

    async def delete(
        self,
        identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MonitorDeleteResponse:
        """
        Delete a configured monitor.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._delete(
            f"/accounts/{account_identifier}/load_balancers/monitors/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[MonitorDeleteResponse], ResultWrapper[MonitorDeleteResponse]),
        )

    async def account_load_balancer_monitors_create_monitor(
        self,
        account_identifier: str,
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
    ) -> MonitorAccountLoadBalancerMonitorsCreateMonitorResponse:
        """
        Create a configured monitor.

        Args:
          account_identifier: Identifier

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
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/load_balancers/monitors",
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
                monitor_account_load_balancer_monitors_create_monitor_params.MonitorAccountLoadBalancerMonitorsCreateMonitorParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[MonitorAccountLoadBalancerMonitorsCreateMonitorResponse],
                ResultWrapper[MonitorAccountLoadBalancerMonitorsCreateMonitorResponse],
            ),
        )

    async def account_load_balancer_monitors_list_monitors(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MonitorAccountLoadBalancerMonitorsListMonitorsResponse]:
        """
        List configured monitors for an account.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/load_balancers/monitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[MonitorAccountLoadBalancerMonitorsListMonitorsResponse]],
                ResultWrapper[MonitorAccountLoadBalancerMonitorsListMonitorsResponse],
            ),
        )

    async def get(
        self,
        identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MonitorGetResponse:
        """
        List a single configured monitor for an account.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/load_balancers/monitors/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[MonitorGetResponse], ResultWrapper[MonitorGetResponse]),
        )


class MonitorsWithRawResponse:
    def __init__(self, monitors: Monitors) -> None:
        self._monitors = monitors

        self.update = to_raw_response_wrapper(
            monitors.update,
        )
        self.delete = to_raw_response_wrapper(
            monitors.delete,
        )
        self.account_load_balancer_monitors_create_monitor = to_raw_response_wrapper(
            monitors.account_load_balancer_monitors_create_monitor,
        )
        self.account_load_balancer_monitors_list_monitors = to_raw_response_wrapper(
            monitors.account_load_balancer_monitors_list_monitors,
        )
        self.get = to_raw_response_wrapper(
            monitors.get,
        )

    @cached_property
    def previews(self) -> PreviewsWithRawResponse:
        return PreviewsWithRawResponse(self._monitors.previews)

    @cached_property
    def references(self) -> ReferencesWithRawResponse:
        return ReferencesWithRawResponse(self._monitors.references)


class AsyncMonitorsWithRawResponse:
    def __init__(self, monitors: AsyncMonitors) -> None:
        self._monitors = monitors

        self.update = async_to_raw_response_wrapper(
            monitors.update,
        )
        self.delete = async_to_raw_response_wrapper(
            monitors.delete,
        )
        self.account_load_balancer_monitors_create_monitor = async_to_raw_response_wrapper(
            monitors.account_load_balancer_monitors_create_monitor,
        )
        self.account_load_balancer_monitors_list_monitors = async_to_raw_response_wrapper(
            monitors.account_load_balancer_monitors_list_monitors,
        )
        self.get = async_to_raw_response_wrapper(
            monitors.get,
        )

    @cached_property
    def previews(self) -> AsyncPreviewsWithRawResponse:
        return AsyncPreviewsWithRawResponse(self._monitors.previews)

    @cached_property
    def references(self) -> AsyncReferencesWithRawResponse:
        return AsyncReferencesWithRawResponse(self._monitors.references)


class MonitorsWithStreamingResponse:
    def __init__(self, monitors: Monitors) -> None:
        self._monitors = monitors

        self.update = to_streamed_response_wrapper(
            monitors.update,
        )
        self.delete = to_streamed_response_wrapper(
            monitors.delete,
        )
        self.account_load_balancer_monitors_create_monitor = to_streamed_response_wrapper(
            monitors.account_load_balancer_monitors_create_monitor,
        )
        self.account_load_balancer_monitors_list_monitors = to_streamed_response_wrapper(
            monitors.account_load_balancer_monitors_list_monitors,
        )
        self.get = to_streamed_response_wrapper(
            monitors.get,
        )

    @cached_property
    def previews(self) -> PreviewsWithStreamingResponse:
        return PreviewsWithStreamingResponse(self._monitors.previews)

    @cached_property
    def references(self) -> ReferencesWithStreamingResponse:
        return ReferencesWithStreamingResponse(self._monitors.references)


class AsyncMonitorsWithStreamingResponse:
    def __init__(self, monitors: AsyncMonitors) -> None:
        self._monitors = monitors

        self.update = async_to_streamed_response_wrapper(
            monitors.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            monitors.delete,
        )
        self.account_load_balancer_monitors_create_monitor = async_to_streamed_response_wrapper(
            monitors.account_load_balancer_monitors_create_monitor,
        )
        self.account_load_balancer_monitors_list_monitors = async_to_streamed_response_wrapper(
            monitors.account_load_balancer_monitors_list_monitors,
        )
        self.get = async_to_streamed_response_wrapper(
            monitors.get,
        )

    @cached_property
    def previews(self) -> AsyncPreviewsWithStreamingResponse:
        return AsyncPreviewsWithStreamingResponse(self._monitors.previews)

    @cached_property
    def references(self) -> AsyncReferencesWithStreamingResponse:
        return AsyncReferencesWithStreamingResponse(self._monitors.references)
