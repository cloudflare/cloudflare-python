# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Type, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.spectrum import app_list_params, app_create_params, app_update_params
from ...types.spectrum.dns_param import DNSParam
from ...types.spectrum.edge_ips_param import EdgeIPsParam
from ...types.spectrum.app_get_response import AppGetResponse
from ...types.spectrum.origin_dns_param import OriginDNSParam
from ...types.spectrum.app_list_response import AppListResponse
from ...types.spectrum.origin_port_param import OriginPortParam
from ...types.spectrum.app_create_response import AppCreateResponse
from ...types.spectrum.app_delete_response import AppDeleteResponse
from ...types.spectrum.app_update_response import AppUpdateResponse

__all__ = ["AppsResource", "AsyncAppsResource"]


class AppsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AppsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        zone_id: str,
        dns: DNSParam,
        ip_firewall: bool,
        protocol: str,
        proxy_protocol: Literal["off", "v1", "v2", "simple"],
        tls: Literal["off", "flexible", "full", "strict"],
        traffic_type: Literal["direct", "http", "https"],
        argo_smart_routing: bool | NotGiven = NOT_GIVEN,
        edge_ips: EdgeIPsParam | NotGiven = NOT_GIVEN,
        origin_direct: List[str] | NotGiven = NOT_GIVEN,
        origin_dns: OriginDNSParam | NotGiven = NOT_GIVEN,
        origin_port: OriginPortParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppCreateResponse]:
        """
        Creates a new Spectrum application from a configuration using a name for the
        origin.

        Args:
          zone_id: Zone identifier.

          dns: The name and type of DNS record for the Spectrum application.

          ip_firewall: Enables IP Access Rules for this application. Notes: Only available for TCP
              applications.

          protocol: The port configuration at Cloudflare's edge. May specify a single port, for
              example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

          proxy_protocol: Enables Proxy Protocol to the origin. Refer to
              [Enable Proxy protocol](https://developers.cloudflare.com/spectrum/getting-started/proxy-protocol/)
              for implementation details on PROXY Protocol V1, PROXY Protocol V2, and Simple
              Proxy Protocol.

          tls: The type of TLS termination associated with the application.

          traffic_type: Determines how data travels from the edge to your origin. When set to "direct",
              Spectrum will send traffic directly to your origin, and the application's type
              is derived from the `protocol`. When set to "http" or "https", Spectrum will
              apply Cloudflare's HTTP/HTTPS features as it sends traffic to your origin, and
              the application type matches this property exactly.

          argo_smart_routing: Enables Argo Smart Routing for this application. Notes: Only available for TCP
              applications with traffic_type set to "direct".

          edge_ips: The anycast edge IP configuration for the hostname of this application.

          origin_direct: List of origin IP addresses. Array may contain multiple IP addresses for load
              balancing.

          origin_dns: The name and type of DNS record for the Spectrum application.

          origin_port: The destination port at the origin. Only specified in conjunction with
              origin_dns. May use an integer to specify a single origin port, for example
              `1000`, or a string to specify a range of origin ports, for example
              `"1000-2000"`. Notes: If specifying a port range, the number of ports in the
              range must match the number of ports specified in the "protocol" field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        zone_id: str,
        dns: DNSParam,
        protocol: str,
        origin_direct: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppCreateResponse]:
        """
        Creates a new Spectrum application from a configuration using a name for the
        origin.

        Args:
          zone_id: Zone identifier.

          dns: The name and type of DNS record for the Spectrum application.

          protocol: The port configuration at Cloudflare's edge. May specify a single port, for
              example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

          origin_direct: List of origin IP addresses. Array may contain multiple IP addresses for load
              balancing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["zone_id", "dns", "ip_firewall", "protocol", "proxy_protocol", "tls", "traffic_type"],
        ["zone_id", "dns", "protocol"],
    )
    def create(
        self,
        *,
        zone_id: str,
        dns: DNSParam,
        ip_firewall: bool | NotGiven = NOT_GIVEN,
        protocol: str,
        proxy_protocol: Literal["off", "v1", "v2", "simple"] | NotGiven = NOT_GIVEN,
        tls: Literal["off", "flexible", "full", "strict"] | NotGiven = NOT_GIVEN,
        traffic_type: Literal["direct", "http", "https"] | NotGiven = NOT_GIVEN,
        argo_smart_routing: bool | NotGiven = NOT_GIVEN,
        edge_ips: EdgeIPsParam | NotGiven = NOT_GIVEN,
        origin_direct: List[str] | NotGiven = NOT_GIVEN,
        origin_dns: OriginDNSParam | NotGiven = NOT_GIVEN,
        origin_port: OriginPortParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppCreateResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[AppCreateResponse],
            self._post(
                f"/zones/{zone_id}/spectrum/apps",
                body=maybe_transform(
                    {
                        "dns": dns,
                        "ip_firewall": ip_firewall,
                        "protocol": protocol,
                        "proxy_protocol": proxy_protocol,
                        "tls": tls,
                        "traffic_type": traffic_type,
                        "argo_smart_routing": argo_smart_routing,
                        "edge_ips": edge_ips,
                        "origin_direct": origin_direct,
                        "origin_dns": origin_dns,
                        "origin_port": origin_port,
                    },
                    app_create_params.AppCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[AppCreateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AppCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        app_id: str,
        *,
        zone_id: str,
        dns: DNSParam,
        ip_firewall: bool,
        protocol: str,
        proxy_protocol: Literal["off", "v1", "v2", "simple"],
        tls: Literal["off", "flexible", "full", "strict"],
        traffic_type: Literal["direct", "http", "https"],
        argo_smart_routing: bool | NotGiven = NOT_GIVEN,
        edge_ips: EdgeIPsParam | NotGiven = NOT_GIVEN,
        origin_direct: List[str] | NotGiven = NOT_GIVEN,
        origin_dns: OriginDNSParam | NotGiven = NOT_GIVEN,
        origin_port: OriginPortParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppUpdateResponse]:
        """
        Updates a previously existing application's configuration that uses a name for
        the origin.

        Args:
          zone_id: Zone identifier.

          app_id: App identifier.

          dns: The name and type of DNS record for the Spectrum application.

          ip_firewall: Enables IP Access Rules for this application. Notes: Only available for TCP
              applications.

          protocol: The port configuration at Cloudflare's edge. May specify a single port, for
              example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

          proxy_protocol: Enables Proxy Protocol to the origin. Refer to
              [Enable Proxy protocol](https://developers.cloudflare.com/spectrum/getting-started/proxy-protocol/)
              for implementation details on PROXY Protocol V1, PROXY Protocol V2, and Simple
              Proxy Protocol.

          tls: The type of TLS termination associated with the application.

          traffic_type: Determines how data travels from the edge to your origin. When set to "direct",
              Spectrum will send traffic directly to your origin, and the application's type
              is derived from the `protocol`. When set to "http" or "https", Spectrum will
              apply Cloudflare's HTTP/HTTPS features as it sends traffic to your origin, and
              the application type matches this property exactly.

          argo_smart_routing: Enables Argo Smart Routing for this application. Notes: Only available for TCP
              applications with traffic_type set to "direct".

          edge_ips: The anycast edge IP configuration for the hostname of this application.

          origin_direct: List of origin IP addresses. Array may contain multiple IP addresses for load
              balancing.

          origin_dns: The name and type of DNS record for the Spectrum application.

          origin_port: The destination port at the origin. Only specified in conjunction with
              origin_dns. May use an integer to specify a single origin port, for example
              `1000`, or a string to specify a range of origin ports, for example
              `"1000-2000"`. Notes: If specifying a port range, the number of ports in the
              range must match the number of ports specified in the "protocol" field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_id: str,
        *,
        zone_id: str,
        dns: DNSParam,
        protocol: str,
        origin_direct: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppUpdateResponse]:
        """
        Updates a previously existing application's configuration that uses a name for
        the origin.

        Args:
          zone_id: Zone identifier.

          app_id: App identifier.

          dns: The name and type of DNS record for the Spectrum application.

          protocol: The port configuration at Cloudflare's edge. May specify a single port, for
              example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

          origin_direct: List of origin IP addresses. Array may contain multiple IP addresses for load
              balancing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["zone_id", "dns", "ip_firewall", "protocol", "proxy_protocol", "tls", "traffic_type"],
        ["zone_id", "dns", "protocol"],
    )
    def update(
        self,
        app_id: str,
        *,
        zone_id: str,
        dns: DNSParam,
        ip_firewall: bool | NotGiven = NOT_GIVEN,
        protocol: str,
        proxy_protocol: Literal["off", "v1", "v2", "simple"] | NotGiven = NOT_GIVEN,
        tls: Literal["off", "flexible", "full", "strict"] | NotGiven = NOT_GIVEN,
        traffic_type: Literal["direct", "http", "https"] | NotGiven = NOT_GIVEN,
        argo_smart_routing: bool | NotGiven = NOT_GIVEN,
        edge_ips: EdgeIPsParam | NotGiven = NOT_GIVEN,
        origin_direct: List[str] | NotGiven = NOT_GIVEN,
        origin_dns: OriginDNSParam | NotGiven = NOT_GIVEN,
        origin_port: OriginPortParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppUpdateResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return cast(
            Optional[AppUpdateResponse],
            self._put(
                f"/zones/{zone_id}/spectrum/apps/{app_id}",
                body=maybe_transform(
                    {
                        "dns": dns,
                        "ip_firewall": ip_firewall,
                        "protocol": protocol,
                        "proxy_protocol": proxy_protocol,
                        "tls": tls,
                        "traffic_type": traffic_type,
                        "argo_smart_routing": argo_smart_routing,
                        "edge_ips": edge_ips,
                        "origin_direct": origin_direct,
                        "origin_dns": origin_dns,
                        "origin_port": origin_port,
                    },
                    app_update_params.AppUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[AppUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AppUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["protocol", "app_id", "created_on", "modified_on", "dns"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[Optional[AppListResponse]]:
        """
        Retrieves a list of currently existing Spectrum applications inside a zone.

        Args:
          zone_id: Zone identifier.

          direction: Sets the direction by which results are ordered.

          order: Application field by which results are ordered.

          page: Page number of paginated results. This parameter is required in order to use
              other pagination parameters. If included in the query, `result_info` will be
              present in the response.

          per_page: Sets the maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/spectrum/apps",
            page=SyncV4PagePaginationArray[Optional[AppListResponse]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    app_list_params.AppListParams,
                ),
            ),
            model=cast(Any, AppListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    def delete(
        self,
        app_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppDeleteResponse]:
        """
        Deletes a previously existing application.

        Args:
          zone_id: Zone identifier.

          app_id: App identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._delete(
            f"/zones/{zone_id}/spectrum/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AppDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppDeleteResponse]], ResultWrapper[AppDeleteResponse]),
        )

    def get(
        self,
        app_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppGetResponse]:
        """
        Gets the application configuration of a specific application inside a zone.

        Args:
          zone_id: Zone identifier.

          app_id: App identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return cast(
            Optional[AppGetResponse],
            self._get(
                f"/zones/{zone_id}/spectrum/apps/{app_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[AppGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AppGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncAppsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAppsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        zone_id: str,
        dns: DNSParam,
        ip_firewall: bool,
        protocol: str,
        proxy_protocol: Literal["off", "v1", "v2", "simple"],
        tls: Literal["off", "flexible", "full", "strict"],
        traffic_type: Literal["direct", "http", "https"],
        argo_smart_routing: bool | NotGiven = NOT_GIVEN,
        edge_ips: EdgeIPsParam | NotGiven = NOT_GIVEN,
        origin_direct: List[str] | NotGiven = NOT_GIVEN,
        origin_dns: OriginDNSParam | NotGiven = NOT_GIVEN,
        origin_port: OriginPortParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppCreateResponse]:
        """
        Creates a new Spectrum application from a configuration using a name for the
        origin.

        Args:
          zone_id: Zone identifier.

          dns: The name and type of DNS record for the Spectrum application.

          ip_firewall: Enables IP Access Rules for this application. Notes: Only available for TCP
              applications.

          protocol: The port configuration at Cloudflare's edge. May specify a single port, for
              example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

          proxy_protocol: Enables Proxy Protocol to the origin. Refer to
              [Enable Proxy protocol](https://developers.cloudflare.com/spectrum/getting-started/proxy-protocol/)
              for implementation details on PROXY Protocol V1, PROXY Protocol V2, and Simple
              Proxy Protocol.

          tls: The type of TLS termination associated with the application.

          traffic_type: Determines how data travels from the edge to your origin. When set to "direct",
              Spectrum will send traffic directly to your origin, and the application's type
              is derived from the `protocol`. When set to "http" or "https", Spectrum will
              apply Cloudflare's HTTP/HTTPS features as it sends traffic to your origin, and
              the application type matches this property exactly.

          argo_smart_routing: Enables Argo Smart Routing for this application. Notes: Only available for TCP
              applications with traffic_type set to "direct".

          edge_ips: The anycast edge IP configuration for the hostname of this application.

          origin_direct: List of origin IP addresses. Array may contain multiple IP addresses for load
              balancing.

          origin_dns: The name and type of DNS record for the Spectrum application.

          origin_port: The destination port at the origin. Only specified in conjunction with
              origin_dns. May use an integer to specify a single origin port, for example
              `1000`, or a string to specify a range of origin ports, for example
              `"1000-2000"`. Notes: If specifying a port range, the number of ports in the
              range must match the number of ports specified in the "protocol" field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        zone_id: str,
        dns: DNSParam,
        protocol: str,
        origin_direct: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppCreateResponse]:
        """
        Creates a new Spectrum application from a configuration using a name for the
        origin.

        Args:
          zone_id: Zone identifier.

          dns: The name and type of DNS record for the Spectrum application.

          protocol: The port configuration at Cloudflare's edge. May specify a single port, for
              example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

          origin_direct: List of origin IP addresses. Array may contain multiple IP addresses for load
              balancing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["zone_id", "dns", "ip_firewall", "protocol", "proxy_protocol", "tls", "traffic_type"],
        ["zone_id", "dns", "protocol"],
    )
    async def create(
        self,
        *,
        zone_id: str,
        dns: DNSParam,
        ip_firewall: bool | NotGiven = NOT_GIVEN,
        protocol: str,
        proxy_protocol: Literal["off", "v1", "v2", "simple"] | NotGiven = NOT_GIVEN,
        tls: Literal["off", "flexible", "full", "strict"] | NotGiven = NOT_GIVEN,
        traffic_type: Literal["direct", "http", "https"] | NotGiven = NOT_GIVEN,
        argo_smart_routing: bool | NotGiven = NOT_GIVEN,
        edge_ips: EdgeIPsParam | NotGiven = NOT_GIVEN,
        origin_direct: List[str] | NotGiven = NOT_GIVEN,
        origin_dns: OriginDNSParam | NotGiven = NOT_GIVEN,
        origin_port: OriginPortParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppCreateResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[AppCreateResponse],
            await self._post(
                f"/zones/{zone_id}/spectrum/apps",
                body=await async_maybe_transform(
                    {
                        "dns": dns,
                        "ip_firewall": ip_firewall,
                        "protocol": protocol,
                        "proxy_protocol": proxy_protocol,
                        "tls": tls,
                        "traffic_type": traffic_type,
                        "argo_smart_routing": argo_smart_routing,
                        "edge_ips": edge_ips,
                        "origin_direct": origin_direct,
                        "origin_dns": origin_dns,
                        "origin_port": origin_port,
                    },
                    app_create_params.AppCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[AppCreateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AppCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        app_id: str,
        *,
        zone_id: str,
        dns: DNSParam,
        ip_firewall: bool,
        protocol: str,
        proxy_protocol: Literal["off", "v1", "v2", "simple"],
        tls: Literal["off", "flexible", "full", "strict"],
        traffic_type: Literal["direct", "http", "https"],
        argo_smart_routing: bool | NotGiven = NOT_GIVEN,
        edge_ips: EdgeIPsParam | NotGiven = NOT_GIVEN,
        origin_direct: List[str] | NotGiven = NOT_GIVEN,
        origin_dns: OriginDNSParam | NotGiven = NOT_GIVEN,
        origin_port: OriginPortParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppUpdateResponse]:
        """
        Updates a previously existing application's configuration that uses a name for
        the origin.

        Args:
          zone_id: Zone identifier.

          app_id: App identifier.

          dns: The name and type of DNS record for the Spectrum application.

          ip_firewall: Enables IP Access Rules for this application. Notes: Only available for TCP
              applications.

          protocol: The port configuration at Cloudflare's edge. May specify a single port, for
              example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

          proxy_protocol: Enables Proxy Protocol to the origin. Refer to
              [Enable Proxy protocol](https://developers.cloudflare.com/spectrum/getting-started/proxy-protocol/)
              for implementation details on PROXY Protocol V1, PROXY Protocol V2, and Simple
              Proxy Protocol.

          tls: The type of TLS termination associated with the application.

          traffic_type: Determines how data travels from the edge to your origin. When set to "direct",
              Spectrum will send traffic directly to your origin, and the application's type
              is derived from the `protocol`. When set to "http" or "https", Spectrum will
              apply Cloudflare's HTTP/HTTPS features as it sends traffic to your origin, and
              the application type matches this property exactly.

          argo_smart_routing: Enables Argo Smart Routing for this application. Notes: Only available for TCP
              applications with traffic_type set to "direct".

          edge_ips: The anycast edge IP configuration for the hostname of this application.

          origin_direct: List of origin IP addresses. Array may contain multiple IP addresses for load
              balancing.

          origin_dns: The name and type of DNS record for the Spectrum application.

          origin_port: The destination port at the origin. Only specified in conjunction with
              origin_dns. May use an integer to specify a single origin port, for example
              `1000`, or a string to specify a range of origin ports, for example
              `"1000-2000"`. Notes: If specifying a port range, the number of ports in the
              range must match the number of ports specified in the "protocol" field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_id: str,
        *,
        zone_id: str,
        dns: DNSParam,
        protocol: str,
        origin_direct: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppUpdateResponse]:
        """
        Updates a previously existing application's configuration that uses a name for
        the origin.

        Args:
          zone_id: Zone identifier.

          app_id: App identifier.

          dns: The name and type of DNS record for the Spectrum application.

          protocol: The port configuration at Cloudflare's edge. May specify a single port, for
              example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

          origin_direct: List of origin IP addresses. Array may contain multiple IP addresses for load
              balancing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["zone_id", "dns", "ip_firewall", "protocol", "proxy_protocol", "tls", "traffic_type"],
        ["zone_id", "dns", "protocol"],
    )
    async def update(
        self,
        app_id: str,
        *,
        zone_id: str,
        dns: DNSParam,
        ip_firewall: bool | NotGiven = NOT_GIVEN,
        protocol: str,
        proxy_protocol: Literal["off", "v1", "v2", "simple"] | NotGiven = NOT_GIVEN,
        tls: Literal["off", "flexible", "full", "strict"] | NotGiven = NOT_GIVEN,
        traffic_type: Literal["direct", "http", "https"] | NotGiven = NOT_GIVEN,
        argo_smart_routing: bool | NotGiven = NOT_GIVEN,
        edge_ips: EdgeIPsParam | NotGiven = NOT_GIVEN,
        origin_direct: List[str] | NotGiven = NOT_GIVEN,
        origin_dns: OriginDNSParam | NotGiven = NOT_GIVEN,
        origin_port: OriginPortParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppUpdateResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return cast(
            Optional[AppUpdateResponse],
            await self._put(
                f"/zones/{zone_id}/spectrum/apps/{app_id}",
                body=await async_maybe_transform(
                    {
                        "dns": dns,
                        "ip_firewall": ip_firewall,
                        "protocol": protocol,
                        "proxy_protocol": proxy_protocol,
                        "tls": tls,
                        "traffic_type": traffic_type,
                        "argo_smart_routing": argo_smart_routing,
                        "edge_ips": edge_ips,
                        "origin_direct": origin_direct,
                        "origin_dns": origin_dns,
                        "origin_port": origin_port,
                    },
                    app_update_params.AppUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[AppUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AppUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["protocol", "app_id", "created_on", "modified_on", "dns"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Optional[AppListResponse], AsyncV4PagePaginationArray[Optional[AppListResponse]]]:
        """
        Retrieves a list of currently existing Spectrum applications inside a zone.

        Args:
          zone_id: Zone identifier.

          direction: Sets the direction by which results are ordered.

          order: Application field by which results are ordered.

          page: Page number of paginated results. This parameter is required in order to use
              other pagination parameters. If included in the query, `result_info` will be
              present in the response.

          per_page: Sets the maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/spectrum/apps",
            page=AsyncV4PagePaginationArray[Optional[AppListResponse]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    app_list_params.AppListParams,
                ),
            ),
            model=cast(Any, AppListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    async def delete(
        self,
        app_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppDeleteResponse]:
        """
        Deletes a previously existing application.

        Args:
          zone_id: Zone identifier.

          app_id: App identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/spectrum/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AppDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppDeleteResponse]], ResultWrapper[AppDeleteResponse]),
        )

    async def get(
        self,
        app_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppGetResponse]:
        """
        Gets the application configuration of a specific application inside a zone.

        Args:
          zone_id: Zone identifier.

          app_id: App identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return cast(
            Optional[AppGetResponse],
            await self._get(
                f"/zones/{zone_id}/spectrum/apps/{app_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[AppGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AppGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AppsResourceWithRawResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.create = to_raw_response_wrapper(
            apps.create,
        )
        self.update = to_raw_response_wrapper(
            apps.update,
        )
        self.list = to_raw_response_wrapper(
            apps.list,
        )
        self.delete = to_raw_response_wrapper(
            apps.delete,
        )
        self.get = to_raw_response_wrapper(
            apps.get,
        )


class AsyncAppsResourceWithRawResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.create = async_to_raw_response_wrapper(
            apps.create,
        )
        self.update = async_to_raw_response_wrapper(
            apps.update,
        )
        self.list = async_to_raw_response_wrapper(
            apps.list,
        )
        self.delete = async_to_raw_response_wrapper(
            apps.delete,
        )
        self.get = async_to_raw_response_wrapper(
            apps.get,
        )


class AppsResourceWithStreamingResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.create = to_streamed_response_wrapper(
            apps.create,
        )
        self.update = to_streamed_response_wrapper(
            apps.update,
        )
        self.list = to_streamed_response_wrapper(
            apps.list,
        )
        self.delete = to_streamed_response_wrapper(
            apps.delete,
        )
        self.get = to_streamed_response_wrapper(
            apps.get,
        )


class AsyncAppsResourceWithStreamingResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.create = async_to_streamed_response_wrapper(
            apps.create,
        )
        self.update = async_to_streamed_response_wrapper(
            apps.update,
        )
        self.list = async_to_streamed_response_wrapper(
            apps.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            apps.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            apps.get,
        )
