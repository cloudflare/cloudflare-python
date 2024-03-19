# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from .....types.radar.attacks.layer7 import (
    SummaryGetResponse,
    SummaryIPVersionResponse,
    SummaryHTTPMethodResponse,
    SummaryHTTPVersionResponse,
    SummaryManagedRulesResponse,
    SummaryMitigationProductResponse,
    summary_get_params,
    summary_ip_version_params,
    summary_http_method_params,
    summary_http_version_params,
    summary_managed_rules_params,
    summary_mitigation_product_params,
)

__all__ = ["Summary", "AsyncSummary"]


class Summary(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SummaryWithRawResponse:
        return SummaryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SummaryWithStreamingResponse:
        return SummaryWithStreamingResponse(self)

    def get(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummaryGetResponse:
        """
        Percentage distribution of mitigation techniques in Layer 7 attacks.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/attacks/layer7/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "location": location,
                        "name": name,
                    },
                    summary_get_params.SummaryGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SummaryGetResponse], ResultWrapper[SummaryGetResponse]),
        )

    def http_method(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        mitigation_product: List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummaryHTTPMethodResponse:
        """
        Percentage distribution of attacks by http method used.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          mitigation_product: Array of L7 mitigation products.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/attacks/layer7/summary/http_method",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "location": location,
                        "mitigation_product": mitigation_product,
                        "name": name,
                    },
                    summary_http_method_params.SummaryHTTPMethodParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SummaryHTTPMethodResponse], ResultWrapper[SummaryHTTPMethodResponse]),
        )

    def http_version(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_method: List[
            Literal[
                "GET",
                "POST",
                "DELETE",
                "PUT",
                "HEAD",
                "PURGE",
                "OPTIONS",
                "PROPFIND",
                "MKCOL",
                "PATCH",
                "ACL",
                "BCOPY",
                "BDELETE",
                "BMOVE",
                "BPROPFIND",
                "BPROPPATCH",
                "CHECKIN",
                "CHECKOUT",
                "CONNECT",
                "COPY",
                "LABEL",
                "LOCK",
                "MERGE",
                "MKACTIVITY",
                "MKWORKSPACE",
                "MOVE",
                "NOTIFY",
                "ORDERPATCH",
                "POLL",
                "PROPPATCH",
                "REPORT",
                "SEARCH",
                "SUBSCRIBE",
                "TRACE",
                "UNCHECKOUT",
                "UNLOCK",
                "UNSUBSCRIBE",
                "UPDATE",
                "VERSIONCONTROL",
                "BASELINECONTROL",
                "XMSENUMATTS",
                "RPC_OUT_DATA",
                "RPC_IN_DATA",
                "JSON",
                "COOK",
                "TRACK",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        mitigation_product: List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummaryHTTPVersionResponse:
        """
        Percentage distribution of attacks by http version used.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          http_method: Filter for http method.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          mitigation_product: Array of L7 mitigation products.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/attacks/layer7/summary/http_version",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "http_method": http_method,
                        "ip_version": ip_version,
                        "location": location,
                        "mitigation_product": mitigation_product,
                        "name": name,
                    },
                    summary_http_version_params.SummaryHTTPVersionParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SummaryHTTPVersionResponse], ResultWrapper[SummaryHTTPVersionResponse]),
        )

    def ip_version(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_method: List[
            Literal[
                "GET",
                "POST",
                "DELETE",
                "PUT",
                "HEAD",
                "PURGE",
                "OPTIONS",
                "PROPFIND",
                "MKCOL",
                "PATCH",
                "ACL",
                "BCOPY",
                "BDELETE",
                "BMOVE",
                "BPROPFIND",
                "BPROPPATCH",
                "CHECKIN",
                "CHECKOUT",
                "CONNECT",
                "COPY",
                "LABEL",
                "LOCK",
                "MERGE",
                "MKACTIVITY",
                "MKWORKSPACE",
                "MOVE",
                "NOTIFY",
                "ORDERPATCH",
                "POLL",
                "PROPPATCH",
                "REPORT",
                "SEARCH",
                "SUBSCRIBE",
                "TRACE",
                "UNCHECKOUT",
                "UNLOCK",
                "UNSUBSCRIBE",
                "UPDATE",
                "VERSIONCONTROL",
                "BASELINECONTROL",
                "XMSENUMATTS",
                "RPC_OUT_DATA",
                "RPC_IN_DATA",
                "JSON",
                "COOK",
                "TRACK",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        mitigation_product: List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummaryIPVersionResponse:
        """
        Percentage distribution of attacks by ip version used.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          http_method: Filter for http method.

          http_version: Filter for http version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          mitigation_product: Array of L7 mitigation products.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/attacks/layer7/summary/ip_version",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "http_method": http_method,
                        "http_version": http_version,
                        "location": location,
                        "mitigation_product": mitigation_product,
                        "name": name,
                    },
                    summary_ip_version_params.SummaryIPVersionParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SummaryIPVersionResponse], ResultWrapper[SummaryIPVersionResponse]),
        )

    def managed_rules(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_method: List[
            Literal[
                "GET",
                "POST",
                "DELETE",
                "PUT",
                "HEAD",
                "PURGE",
                "OPTIONS",
                "PROPFIND",
                "MKCOL",
                "PATCH",
                "ACL",
                "BCOPY",
                "BDELETE",
                "BMOVE",
                "BPROPFIND",
                "BPROPPATCH",
                "CHECKIN",
                "CHECKOUT",
                "CONNECT",
                "COPY",
                "LABEL",
                "LOCK",
                "MERGE",
                "MKACTIVITY",
                "MKWORKSPACE",
                "MOVE",
                "NOTIFY",
                "ORDERPATCH",
                "POLL",
                "PROPPATCH",
                "REPORT",
                "SEARCH",
                "SUBSCRIBE",
                "TRACE",
                "UNCHECKOUT",
                "UNLOCK",
                "UNSUBSCRIBE",
                "UPDATE",
                "VERSIONCONTROL",
                "BASELINECONTROL",
                "XMSENUMATTS",
                "RPC_OUT_DATA",
                "RPC_IN_DATA",
                "JSON",
                "COOK",
                "TRACK",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        mitigation_product: List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummaryManagedRulesResponse:
        """
        Percentage distribution of attacks by managed rules used.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          http_method: Filter for http method.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          mitigation_product: Array of L7 mitigation products.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/attacks/layer7/summary/managed_rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "http_method": http_method,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "location": location,
                        "mitigation_product": mitigation_product,
                        "name": name,
                    },
                    summary_managed_rules_params.SummaryManagedRulesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SummaryManagedRulesResponse], ResultWrapper[SummaryManagedRulesResponse]),
        )

    def mitigation_product(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_method: List[
            Literal[
                "GET",
                "POST",
                "DELETE",
                "PUT",
                "HEAD",
                "PURGE",
                "OPTIONS",
                "PROPFIND",
                "MKCOL",
                "PATCH",
                "ACL",
                "BCOPY",
                "BDELETE",
                "BMOVE",
                "BPROPFIND",
                "BPROPPATCH",
                "CHECKIN",
                "CHECKOUT",
                "CONNECT",
                "COPY",
                "LABEL",
                "LOCK",
                "MERGE",
                "MKACTIVITY",
                "MKWORKSPACE",
                "MOVE",
                "NOTIFY",
                "ORDERPATCH",
                "POLL",
                "PROPPATCH",
                "REPORT",
                "SEARCH",
                "SUBSCRIBE",
                "TRACE",
                "UNCHECKOUT",
                "UNLOCK",
                "UNSUBSCRIBE",
                "UPDATE",
                "VERSIONCONTROL",
                "BASELINECONTROL",
                "XMSENUMATTS",
                "RPC_OUT_DATA",
                "RPC_IN_DATA",
                "JSON",
                "COOK",
                "TRACK",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummaryMitigationProductResponse:
        """
        Percentage distribution of attacks by mitigation product used.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          http_method: Filter for http method.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/attacks/layer7/summary/mitigation_product",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "http_method": http_method,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "location": location,
                        "name": name,
                    },
                    summary_mitigation_product_params.SummaryMitigationProductParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SummaryMitigationProductResponse], ResultWrapper[SummaryMitigationProductResponse]),
        )


class AsyncSummary(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSummaryWithRawResponse:
        return AsyncSummaryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSummaryWithStreamingResponse:
        return AsyncSummaryWithStreamingResponse(self)

    async def get(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummaryGetResponse:
        """
        Percentage distribution of mitigation techniques in Layer 7 attacks.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/attacks/layer7/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "location": location,
                        "name": name,
                    },
                    summary_get_params.SummaryGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SummaryGetResponse], ResultWrapper[SummaryGetResponse]),
        )

    async def http_method(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        mitigation_product: List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummaryHTTPMethodResponse:
        """
        Percentage distribution of attacks by http method used.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          mitigation_product: Array of L7 mitigation products.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/attacks/layer7/summary/http_method",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "location": location,
                        "mitigation_product": mitigation_product,
                        "name": name,
                    },
                    summary_http_method_params.SummaryHTTPMethodParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SummaryHTTPMethodResponse], ResultWrapper[SummaryHTTPMethodResponse]),
        )

    async def http_version(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_method: List[
            Literal[
                "GET",
                "POST",
                "DELETE",
                "PUT",
                "HEAD",
                "PURGE",
                "OPTIONS",
                "PROPFIND",
                "MKCOL",
                "PATCH",
                "ACL",
                "BCOPY",
                "BDELETE",
                "BMOVE",
                "BPROPFIND",
                "BPROPPATCH",
                "CHECKIN",
                "CHECKOUT",
                "CONNECT",
                "COPY",
                "LABEL",
                "LOCK",
                "MERGE",
                "MKACTIVITY",
                "MKWORKSPACE",
                "MOVE",
                "NOTIFY",
                "ORDERPATCH",
                "POLL",
                "PROPPATCH",
                "REPORT",
                "SEARCH",
                "SUBSCRIBE",
                "TRACE",
                "UNCHECKOUT",
                "UNLOCK",
                "UNSUBSCRIBE",
                "UPDATE",
                "VERSIONCONTROL",
                "BASELINECONTROL",
                "XMSENUMATTS",
                "RPC_OUT_DATA",
                "RPC_IN_DATA",
                "JSON",
                "COOK",
                "TRACK",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        mitigation_product: List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummaryHTTPVersionResponse:
        """
        Percentage distribution of attacks by http version used.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          http_method: Filter for http method.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          mitigation_product: Array of L7 mitigation products.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/attacks/layer7/summary/http_version",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "http_method": http_method,
                        "ip_version": ip_version,
                        "location": location,
                        "mitigation_product": mitigation_product,
                        "name": name,
                    },
                    summary_http_version_params.SummaryHTTPVersionParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SummaryHTTPVersionResponse], ResultWrapper[SummaryHTTPVersionResponse]),
        )

    async def ip_version(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_method: List[
            Literal[
                "GET",
                "POST",
                "DELETE",
                "PUT",
                "HEAD",
                "PURGE",
                "OPTIONS",
                "PROPFIND",
                "MKCOL",
                "PATCH",
                "ACL",
                "BCOPY",
                "BDELETE",
                "BMOVE",
                "BPROPFIND",
                "BPROPPATCH",
                "CHECKIN",
                "CHECKOUT",
                "CONNECT",
                "COPY",
                "LABEL",
                "LOCK",
                "MERGE",
                "MKACTIVITY",
                "MKWORKSPACE",
                "MOVE",
                "NOTIFY",
                "ORDERPATCH",
                "POLL",
                "PROPPATCH",
                "REPORT",
                "SEARCH",
                "SUBSCRIBE",
                "TRACE",
                "UNCHECKOUT",
                "UNLOCK",
                "UNSUBSCRIBE",
                "UPDATE",
                "VERSIONCONTROL",
                "BASELINECONTROL",
                "XMSENUMATTS",
                "RPC_OUT_DATA",
                "RPC_IN_DATA",
                "JSON",
                "COOK",
                "TRACK",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        mitigation_product: List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummaryIPVersionResponse:
        """
        Percentage distribution of attacks by ip version used.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          http_method: Filter for http method.

          http_version: Filter for http version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          mitigation_product: Array of L7 mitigation products.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/attacks/layer7/summary/ip_version",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "http_method": http_method,
                        "http_version": http_version,
                        "location": location,
                        "mitigation_product": mitigation_product,
                        "name": name,
                    },
                    summary_ip_version_params.SummaryIPVersionParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SummaryIPVersionResponse], ResultWrapper[SummaryIPVersionResponse]),
        )

    async def managed_rules(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_method: List[
            Literal[
                "GET",
                "POST",
                "DELETE",
                "PUT",
                "HEAD",
                "PURGE",
                "OPTIONS",
                "PROPFIND",
                "MKCOL",
                "PATCH",
                "ACL",
                "BCOPY",
                "BDELETE",
                "BMOVE",
                "BPROPFIND",
                "BPROPPATCH",
                "CHECKIN",
                "CHECKOUT",
                "CONNECT",
                "COPY",
                "LABEL",
                "LOCK",
                "MERGE",
                "MKACTIVITY",
                "MKWORKSPACE",
                "MOVE",
                "NOTIFY",
                "ORDERPATCH",
                "POLL",
                "PROPPATCH",
                "REPORT",
                "SEARCH",
                "SUBSCRIBE",
                "TRACE",
                "UNCHECKOUT",
                "UNLOCK",
                "UNSUBSCRIBE",
                "UPDATE",
                "VERSIONCONTROL",
                "BASELINECONTROL",
                "XMSENUMATTS",
                "RPC_OUT_DATA",
                "RPC_IN_DATA",
                "JSON",
                "COOK",
                "TRACK",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        mitigation_product: List[
            Literal[
                "DDOS", "WAF", "BOT_MANAGEMENT", "ACCESS_RULES", "IP_REPUTATION", "API_SHIELD", "DATA_LOSS_PREVENTION"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummaryManagedRulesResponse:
        """
        Percentage distribution of attacks by managed rules used.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          http_method: Filter for http method.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          mitigation_product: Array of L7 mitigation products.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/attacks/layer7/summary/managed_rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "http_method": http_method,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "location": location,
                        "mitigation_product": mitigation_product,
                        "name": name,
                    },
                    summary_managed_rules_params.SummaryManagedRulesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SummaryManagedRulesResponse], ResultWrapper[SummaryManagedRulesResponse]),
        )

    async def mitigation_product(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        http_method: List[
            Literal[
                "GET",
                "POST",
                "DELETE",
                "PUT",
                "HEAD",
                "PURGE",
                "OPTIONS",
                "PROPFIND",
                "MKCOL",
                "PATCH",
                "ACL",
                "BCOPY",
                "BDELETE",
                "BMOVE",
                "BPROPFIND",
                "BPROPPATCH",
                "CHECKIN",
                "CHECKOUT",
                "CONNECT",
                "COPY",
                "LABEL",
                "LOCK",
                "MERGE",
                "MKACTIVITY",
                "MKWORKSPACE",
                "MOVE",
                "NOTIFY",
                "ORDERPATCH",
                "POLL",
                "PROPPATCH",
                "REPORT",
                "SEARCH",
                "SUBSCRIBE",
                "TRACE",
                "UNCHECKOUT",
                "UNLOCK",
                "UNSUBSCRIBE",
                "UPDATE",
                "VERSIONCONTROL",
                "BASELINECONTROL",
                "XMSENUMATTS",
                "RPC_OUT_DATA",
                "RPC_IN_DATA",
                "JSON",
                "COOK",
                "TRACK",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        http_version: List[Literal["HTTPv1", "HTTPv2", "HTTPv3"]] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummaryMitigationProductResponse:
        """
        Percentage distribution of attacks by mitigation product used.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          continent: Array of comma separated list of continents (alpha-2 continent codes). Start
              with `-` to exclude from results. For example, `-EU,NA` excludes results from
              Europe, but includes results from North America.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          http_method: Filter for http method.

          http_version: Filter for http version.

          ip_version: Filter for ip version.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/attacks/layer7/summary/mitigation_product",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "http_method": http_method,
                        "http_version": http_version,
                        "ip_version": ip_version,
                        "location": location,
                        "name": name,
                    },
                    summary_mitigation_product_params.SummaryMitigationProductParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SummaryMitigationProductResponse], ResultWrapper[SummaryMitigationProductResponse]),
        )


class SummaryWithRawResponse:
    def __init__(self, summary: Summary) -> None:
        self._summary = summary

        self.get = to_raw_response_wrapper(
            summary.get,
        )
        self.http_method = to_raw_response_wrapper(
            summary.http_method,
        )
        self.http_version = to_raw_response_wrapper(
            summary.http_version,
        )
        self.ip_version = to_raw_response_wrapper(
            summary.ip_version,
        )
        self.managed_rules = to_raw_response_wrapper(
            summary.managed_rules,
        )
        self.mitigation_product = to_raw_response_wrapper(
            summary.mitigation_product,
        )


class AsyncSummaryWithRawResponse:
    def __init__(self, summary: AsyncSummary) -> None:
        self._summary = summary

        self.get = async_to_raw_response_wrapper(
            summary.get,
        )
        self.http_method = async_to_raw_response_wrapper(
            summary.http_method,
        )
        self.http_version = async_to_raw_response_wrapper(
            summary.http_version,
        )
        self.ip_version = async_to_raw_response_wrapper(
            summary.ip_version,
        )
        self.managed_rules = async_to_raw_response_wrapper(
            summary.managed_rules,
        )
        self.mitigation_product = async_to_raw_response_wrapper(
            summary.mitigation_product,
        )


class SummaryWithStreamingResponse:
    def __init__(self, summary: Summary) -> None:
        self._summary = summary

        self.get = to_streamed_response_wrapper(
            summary.get,
        )
        self.http_method = to_streamed_response_wrapper(
            summary.http_method,
        )
        self.http_version = to_streamed_response_wrapper(
            summary.http_version,
        )
        self.ip_version = to_streamed_response_wrapper(
            summary.ip_version,
        )
        self.managed_rules = to_streamed_response_wrapper(
            summary.managed_rules,
        )
        self.mitigation_product = to_streamed_response_wrapper(
            summary.mitigation_product,
        )


class AsyncSummaryWithStreamingResponse:
    def __init__(self, summary: AsyncSummary) -> None:
        self._summary = summary

        self.get = async_to_streamed_response_wrapper(
            summary.get,
        )
        self.http_method = async_to_streamed_response_wrapper(
            summary.http_method,
        )
        self.http_version = async_to_streamed_response_wrapper(
            summary.http_version,
        )
        self.ip_version = async_to_streamed_response_wrapper(
            summary.ip_version,
        )
        self.managed_rules = async_to_streamed_response_wrapper(
            summary.managed_rules,
        )
        self.mitigation_product = async_to_streamed_response_wrapper(
            summary.mitigation_product,
        )
