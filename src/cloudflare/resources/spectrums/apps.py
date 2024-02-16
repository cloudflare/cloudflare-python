# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.spectrums import (
    AppUpdateResponse,
    AppDeleteResponse,
    AppGetResponse,
    AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse,
    AppSpectrumApplicationsListSpectrumApplicationsResponse,
    app_update_params,
    app_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin_params,
)

from typing import Type, Optional, Union

from typing_extensions import Literal

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
from ...types.spectrums import app_update_params
from ...types.spectrums import app_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin_params
from ...types.spectrums import app_spectrum_applications_list_spectrum_applications_params
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
from typing import cast
from typing import cast

__all__ = ["Apps", "AsyncApps"]


class Apps(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppsWithRawResponse:
        return AppsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppsWithStreamingResponse:
        return AppsWithStreamingResponse(self)

    def update(
        self,
        app_id: str,
        *,
        zone: str,
        dns: app_update_params.DNS,
        origin_dns: app_update_params.OriginDNS,
        origin_port: Union[int, str],
        protocol: str,
        argo_smart_routing: bool | NotGiven = NOT_GIVEN,
        edge_ips: app_update_params.EdgeIPs | NotGiven = NOT_GIVEN,
        ip_firewall: bool | NotGiven = NOT_GIVEN,
        proxy_protocol: Literal["off", "v1", "v2", "simple"] | NotGiven = NOT_GIVEN,
        tls: Literal["off", "flexible", "full", "strict"] | NotGiven = NOT_GIVEN,
        traffic_type: Literal["direct", "http", "https"] | NotGiven = NOT_GIVEN,
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
          zone: Identifier

          app_id: Application identifier.

          dns: The name and type of DNS record for the Spectrum application.

          origin_dns: The name and type of DNS record for the Spectrum application.

          origin_port: The destination port at the origin. Only specified in conjunction with
              origin_dns. May use an integer to specify a single origin port, for example
              `1000`, or a string to specify a range of origin ports, for example
              `"1000-2000"`. Notes: If specifying a port range, the number of ports in the
              range must match the number of ports specified in the "protocol" field.

          protocol: The port configuration at Cloudflare’s edge. May specify a single port, for
              example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

          argo_smart_routing: Enables Argo Smart Routing for this application. Notes: Only available for TCP
              applications with traffic_type set to "direct".

          edge_ips: The anycast edge IP configuration for the hostname of this application.

          ip_firewall: Enables IP Access Rules for this application. Notes: Only available for TCP
              applications.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._put(
            f"/zones/{zone}/spectrum/apps/{app_id}",
            body=maybe_transform(
                {
                    "dns": dns,
                    "origin_dns": origin_dns,
                    "origin_port": origin_port,
                    "protocol": protocol,
                    "argo_smart_routing": argo_smart_routing,
                    "edge_ips": edge_ips,
                    "ip_firewall": ip_firewall,
                    "proxy_protocol": proxy_protocol,
                    "tls": tls,
                    "traffic_type": traffic_type,
                },
                app_update_params.AppUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppUpdateResponse]], ResultWrapper[AppUpdateResponse]),
        )

    def delete(
        self,
        app_id: str,
        *,
        zone: str,
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
          zone: Identifier

          app_id: Application identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._delete(
            f"/zones/{zone}/spectrum/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppDeleteResponse]], ResultWrapper[AppDeleteResponse]),
        )

    def get(
        self,
        app_id: str,
        *,
        zone: str,
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
          zone: Identifier

          app_id: Application identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return cast(
            Optional[AppGetResponse],
            self._get(
                f"/zones/{zone}/spectrum/apps/{app_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AppGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
        self,
        zone: str,
        *,
        dns: app_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin_params.DNS,
        origin_dns: app_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin_params.OriginDNS,
        origin_port: Union[int, str],
        protocol: str,
        argo_smart_routing: bool | NotGiven = NOT_GIVEN,
        edge_ips: app_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin_params.EdgeIPs
        | NotGiven = NOT_GIVEN,
        ip_firewall: bool | NotGiven = NOT_GIVEN,
        proxy_protocol: Literal["off", "v1", "v2", "simple"] | NotGiven = NOT_GIVEN,
        tls: Literal["off", "flexible", "full", "strict"] | NotGiven = NOT_GIVEN,
        traffic_type: Literal["direct", "http", "https"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse]:
        """
        Creates a new Spectrum application from a configuration using a name for the
        origin.

        Args:
          zone: Identifier

          dns: The name and type of DNS record for the Spectrum application.

          origin_dns: The name and type of DNS record for the Spectrum application.

          origin_port: The destination port at the origin. Only specified in conjunction with
              origin_dns. May use an integer to specify a single origin port, for example
              `1000`, or a string to specify a range of origin ports, for example
              `"1000-2000"`. Notes: If specifying a port range, the number of ports in the
              range must match the number of ports specified in the "protocol" field.

          protocol: The port configuration at Cloudflare’s edge. May specify a single port, for
              example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

          argo_smart_routing: Enables Argo Smart Routing for this application. Notes: Only available for TCP
              applications with traffic_type set to "direct".

          edge_ips: The anycast edge IP configuration for the hostname of this application.

          ip_firewall: Enables IP Access Rules for this application. Notes: Only available for TCP
              applications.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        return self._post(
            f"/zones/{zone}/spectrum/apps",
            body=maybe_transform(
                {
                    "dns": dns,
                    "origin_dns": origin_dns,
                    "origin_port": origin_port,
                    "protocol": protocol,
                    "argo_smart_routing": argo_smart_routing,
                    "edge_ips": edge_ips,
                    "ip_firewall": ip_firewall,
                    "proxy_protocol": proxy_protocol,
                    "tls": tls,
                    "traffic_type": traffic_type,
                },
                app_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin_params.AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse]],
                ResultWrapper[AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse],
            ),
        )

    def spectrum_applications_list_spectrum_applications(
        self,
        zone: str,
        *,
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
    ) -> Optional[AppSpectrumApplicationsListSpectrumApplicationsResponse]:
        """
        Retrieves a list of currently existing Spectrum applications inside a zone.

        Args:
          zone: Identifier

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
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        return self._get(
            f"/zones/{zone}/spectrum/apps",
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
                    app_spectrum_applications_list_spectrum_applications_params.AppSpectrumApplicationsListSpectrumApplicationsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AppSpectrumApplicationsListSpectrumApplicationsResponse]],
                ResultWrapper[AppSpectrumApplicationsListSpectrumApplicationsResponse],
            ),
        )


class AsyncApps(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppsWithRawResponse:
        return AsyncAppsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppsWithStreamingResponse:
        return AsyncAppsWithStreamingResponse(self)

    async def update(
        self,
        app_id: str,
        *,
        zone: str,
        dns: app_update_params.DNS,
        origin_dns: app_update_params.OriginDNS,
        origin_port: Union[int, str],
        protocol: str,
        argo_smart_routing: bool | NotGiven = NOT_GIVEN,
        edge_ips: app_update_params.EdgeIPs | NotGiven = NOT_GIVEN,
        ip_firewall: bool | NotGiven = NOT_GIVEN,
        proxy_protocol: Literal["off", "v1", "v2", "simple"] | NotGiven = NOT_GIVEN,
        tls: Literal["off", "flexible", "full", "strict"] | NotGiven = NOT_GIVEN,
        traffic_type: Literal["direct", "http", "https"] | NotGiven = NOT_GIVEN,
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
          zone: Identifier

          app_id: Application identifier.

          dns: The name and type of DNS record for the Spectrum application.

          origin_dns: The name and type of DNS record for the Spectrum application.

          origin_port: The destination port at the origin. Only specified in conjunction with
              origin_dns. May use an integer to specify a single origin port, for example
              `1000`, or a string to specify a range of origin ports, for example
              `"1000-2000"`. Notes: If specifying a port range, the number of ports in the
              range must match the number of ports specified in the "protocol" field.

          protocol: The port configuration at Cloudflare’s edge. May specify a single port, for
              example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

          argo_smart_routing: Enables Argo Smart Routing for this application. Notes: Only available for TCP
              applications with traffic_type set to "direct".

          edge_ips: The anycast edge IP configuration for the hostname of this application.

          ip_firewall: Enables IP Access Rules for this application. Notes: Only available for TCP
              applications.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._put(
            f"/zones/{zone}/spectrum/apps/{app_id}",
            body=maybe_transform(
                {
                    "dns": dns,
                    "origin_dns": origin_dns,
                    "origin_port": origin_port,
                    "protocol": protocol,
                    "argo_smart_routing": argo_smart_routing,
                    "edge_ips": edge_ips,
                    "ip_firewall": ip_firewall,
                    "proxy_protocol": proxy_protocol,
                    "tls": tls,
                    "traffic_type": traffic_type,
                },
                app_update_params.AppUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppUpdateResponse]], ResultWrapper[AppUpdateResponse]),
        )

    async def delete(
        self,
        app_id: str,
        *,
        zone: str,
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
          zone: Identifier

          app_id: Application identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._delete(
            f"/zones/{zone}/spectrum/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppDeleteResponse]], ResultWrapper[AppDeleteResponse]),
        )

    async def get(
        self,
        app_id: str,
        *,
        zone: str,
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
          zone: Identifier

          app_id: Application identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return cast(
            Optional[AppGetResponse],
            await self._get(
                f"/zones/{zone}/spectrum/apps/{app_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AppGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
        self,
        zone: str,
        *,
        dns: app_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin_params.DNS,
        origin_dns: app_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin_params.OriginDNS,
        origin_port: Union[int, str],
        protocol: str,
        argo_smart_routing: bool | NotGiven = NOT_GIVEN,
        edge_ips: app_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin_params.EdgeIPs
        | NotGiven = NOT_GIVEN,
        ip_firewall: bool | NotGiven = NOT_GIVEN,
        proxy_protocol: Literal["off", "v1", "v2", "simple"] | NotGiven = NOT_GIVEN,
        tls: Literal["off", "flexible", "full", "strict"] | NotGiven = NOT_GIVEN,
        traffic_type: Literal["direct", "http", "https"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse]:
        """
        Creates a new Spectrum application from a configuration using a name for the
        origin.

        Args:
          zone: Identifier

          dns: The name and type of DNS record for the Spectrum application.

          origin_dns: The name and type of DNS record for the Spectrum application.

          origin_port: The destination port at the origin. Only specified in conjunction with
              origin_dns. May use an integer to specify a single origin port, for example
              `1000`, or a string to specify a range of origin ports, for example
              `"1000-2000"`. Notes: If specifying a port range, the number of ports in the
              range must match the number of ports specified in the "protocol" field.

          protocol: The port configuration at Cloudflare’s edge. May specify a single port, for
              example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

          argo_smart_routing: Enables Argo Smart Routing for this application. Notes: Only available for TCP
              applications with traffic_type set to "direct".

          edge_ips: The anycast edge IP configuration for the hostname of this application.

          ip_firewall: Enables IP Access Rules for this application. Notes: Only available for TCP
              applications.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        return await self._post(
            f"/zones/{zone}/spectrum/apps",
            body=maybe_transform(
                {
                    "dns": dns,
                    "origin_dns": origin_dns,
                    "origin_port": origin_port,
                    "protocol": protocol,
                    "argo_smart_routing": argo_smart_routing,
                    "edge_ips": edge_ips,
                    "ip_firewall": ip_firewall,
                    "proxy_protocol": proxy_protocol,
                    "tls": tls,
                    "traffic_type": traffic_type,
                },
                app_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin_params.AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse]],
                ResultWrapper[AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse],
            ),
        )

    async def spectrum_applications_list_spectrum_applications(
        self,
        zone: str,
        *,
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
    ) -> Optional[AppSpectrumApplicationsListSpectrumApplicationsResponse]:
        """
        Retrieves a list of currently existing Spectrum applications inside a zone.

        Args:
          zone: Identifier

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
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        return await self._get(
            f"/zones/{zone}/spectrum/apps",
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
                    app_spectrum_applications_list_spectrum_applications_params.AppSpectrumApplicationsListSpectrumApplicationsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AppSpectrumApplicationsListSpectrumApplicationsResponse]],
                ResultWrapper[AppSpectrumApplicationsListSpectrumApplicationsResponse],
            ),
        )


class AppsWithRawResponse:
    def __init__(self, apps: Apps) -> None:
        self._apps = apps

        self.update = to_raw_response_wrapper(
            apps.update,
        )
        self.delete = to_raw_response_wrapper(
            apps.delete,
        )
        self.get = to_raw_response_wrapper(
            apps.get,
        )
        self.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin = to_raw_response_wrapper(
            apps.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin,
        )
        self.spectrum_applications_list_spectrum_applications = to_raw_response_wrapper(
            apps.spectrum_applications_list_spectrum_applications,
        )


class AsyncAppsWithRawResponse:
    def __init__(self, apps: AsyncApps) -> None:
        self._apps = apps

        self.update = async_to_raw_response_wrapper(
            apps.update,
        )
        self.delete = async_to_raw_response_wrapper(
            apps.delete,
        )
        self.get = async_to_raw_response_wrapper(
            apps.get,
        )
        self.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin = (
            async_to_raw_response_wrapper(
                apps.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin,
            )
        )
        self.spectrum_applications_list_spectrum_applications = async_to_raw_response_wrapper(
            apps.spectrum_applications_list_spectrum_applications,
        )


class AppsWithStreamingResponse:
    def __init__(self, apps: Apps) -> None:
        self._apps = apps

        self.update = to_streamed_response_wrapper(
            apps.update,
        )
        self.delete = to_streamed_response_wrapper(
            apps.delete,
        )
        self.get = to_streamed_response_wrapper(
            apps.get,
        )
        self.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin = (
            to_streamed_response_wrapper(
                apps.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin,
            )
        )
        self.spectrum_applications_list_spectrum_applications = to_streamed_response_wrapper(
            apps.spectrum_applications_list_spectrum_applications,
        )


class AsyncAppsWithStreamingResponse:
    def __init__(self, apps: AsyncApps) -> None:
        self._apps = apps

        self.update = async_to_streamed_response_wrapper(
            apps.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            apps.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            apps.get,
        )
        self.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin = (
            async_to_streamed_response_wrapper(
                apps.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin,
            )
        )
        self.spectrum_applications_list_spectrum_applications = async_to_streamed_response_wrapper(
            apps.spectrum_applications_list_spectrum_applications,
        )
