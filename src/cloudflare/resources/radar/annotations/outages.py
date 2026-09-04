# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.radar.annotations import outage_get_params, outage_locations_params
from ....types.radar.annotations.outage_get_response import OutageGetResponse
from ....types.radar.annotations.outage_locations_response import OutageLocationsResponse

__all__ = ["OutagesResource", "AsyncOutagesResource"]


class OutagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OutagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OutagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OutagesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        asn: int | Omit = omit,
        bot: str | Omit = omit,
        ca: str | Omit = omit,
        data_source: Literal[
            "ALL",
            "AI_BOTS",
            "AI_GATEWAY",
            "BGP",
            "BOTS",
            "CONNECTION_ANOMALY",
            "CT",
            "DNS",
            "DNS_MAGNITUDE",
            "DNS_AS112",
            "DOS",
            "EMAIL_ROUTING",
            "EMAIL_SECURITY",
            "FW",
            "FW_PG",
            "HTTP",
            "HTTP_CONTROL",
            "HTTP_CRAWLER_REFERER",
            "HTTP_ORIGINS",
            "IQI",
            "LEAKED_CREDENTIALS",
            "NET",
            "ROBOTS_TXT",
            "SPEED",
            "WORKERS_AI",
        ]
        | Omit = omit,
        date_end: Union[str, datetime] | Omit = omit,
        date_range: str | Omit = omit,
        date_start: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: str | Omit = omit,
        limit: int | Omit = omit,
        location: str | Omit = omit,
        log: str | Omit = omit,
        offset: int | Omit = omit,
        origin: str | Omit = omit,
        outage_cause: Literal[
            "BLOCKING",
            "CABLE_CUT",
            "CYBERATTACK",
            "DNS",
            "FIRE",
            "GOVERNMENT_DIRECTED",
            "MAINTENANCE",
            "MECHANICAL",
            "MILITARY_ACTION",
            "MISCONFIGURATION",
            "NATURAL_DISASTER",
            "NETWORK_PROBLEM",
            "POWER_OUTAGE",
            "SOFTWARE",
            "TECHNICAL_PROBLEM",
            "UNKNOWN",
            "WEATHER",
        ]
        | Omit = omit,
        outage_type: Literal["NATIONWIDE", "REGIONAL", "NETWORK", "PLATFORM"] | Omit = omit,
        query: str | Omit = omit,
        tags: List[
            Literal[
                "ADM1",
                "ADM2",
                "API_TRAFFIC",
                "ARC",
                "AS",
                "ASN",
                "ATTACKS",
                "AUTHOR",
                "BANDWIDTH",
                "BITRATE",
                "BOT",
                "BOT_CATEGORY",
                "BOT_CLASS",
                "BOT_KIND",
                "BOT_OPERATOR",
                "BROWSER",
                "BROWSER_FAMILY",
                "BYTES",
                "CA",
                "CACHE_HIT",
                "CA_OWNER",
                "CHECK_RESULT",
                "CLIENT_TYPE",
                "COMPROMISED",
                "CONTENT_TYPE",
                "CRAWL_PURPOSE",
                "CRAWL_REFER_RATIO",
                "DEVICE_TYPE",
                "DKIM",
                "DMARC",
                "DNS",
                "DNSSEC",
                "DNSSEC_AWARE",
                "DNSSEC_E2E",
                "DOMAIN_CATEGORY",
                "DURATION",
                "EDNS",
                "ENCRYPTED",
                "ENTRY_TYPE",
                "EXPIRATION_STATUS",
                "HAS_IPS",
                "HAS_MATCHING_ANSWER",
                "HAS_WILDCARDS",
                "HTTP_METHOD",
                "HTTP_PROTOCOL",
                "HTTP_VERSION",
                "INDUSTRY",
                "IP_VERSION",
                "JITTER",
                "KEY_AGREEMENT",
                "LATENCY",
                "LOCATION",
                "LOCATION_LATENCY",
                "LOG",
                "LOG_API",
                "LOG_OPERATOR",
                "MALICIOUS",
                "MANAGED_RULES",
                "MITIGATION_PRODUCT",
                "MODEL",
                "NAMESERVER_LATENCY",
                "ORIGIN",
                "ORIGIN_AS",
                "ORIGIN_LOCATION",
                "ORIGIN_TARGET_LOCATION_PAIR",
                "OS",
                "PERCENTILE",
                "POST_QUANTUM",
                "PREFIX",
                "PRODUCT",
                "PROTOCOL",
                "PROVIDER",
                "PUBLIC_KEY_ALGORITHM",
                "QUERY_TYPE",
                "REFERER",
                "REGION",
                "RESPONSE_CODE",
                "RESPONSE_STATUS",
                "RESPONSE_STATUS_CATEGORY",
                "RESPONSE_TTL",
                "SIGNATURE_ALGORITHM",
                "SPAM",
                "SPF",
                "SPOOF",
                "SUCCESS_RATE",
                "TARGET_LOCATION",
                "TASK",
                "THREAT_CATEGORY",
                "TLD",
                "TLD_DNS_MAGNITUDE",
                "TLS_VERSION",
                "UPDATE_TYPE",
                "USER_AGENT",
                "VALIDATION_LEVEL",
                "VECTOR",
                "VERTICAL",
            ]
        ]
        | Omit = omit,
        tld: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OutageGetResponse:
        """
        Retrieves the latest Internet outages and anomalies.

        Args:
          asn: Filters results by Autonomous System. Specify a single Autonomous System Number
              (ASN) as integer.

          bot: Filters results by bot.

          ca: Filters results by certificate authority.

          data_source: Filters results by data source.

          date_end: End of the date range (inclusive). Alternative to `dateRange`; provide together
              with `dateStart`.

          date_range: Filters results by a relative date range ending at the current time. Use `<n>d`
              for days (up to `364d`) or `<n>w` for weeks (up to `52w`), e.g. `7d`. Append
              `control` to request the equivalent previous period for comparison: the
              comparison window is shifted back by the current window's length rounded up to a
              whole number of weeks, so it keeps the same weekday alignment and does not
              overlap the current window (e.g. `3dcontrol` covers days -10 to -7, `7dcontrol`
              covers days -14 to -7, `28dcontrol` covers days -56 to -28, and `10dcontrol`
              covers days -24 to -14). Mutually exclusive with `dateStart`/`dateEnd`.

          date_start: Start of the date range (inclusive). Alternative to `dateRange`; provide
              together with `dateEnd`.

          format: Format in which results will be returned.

          geo_id: Filters results by geolocation. Refer to
              [GeoNames](https://download.geonames.org/export/dump/readme.txt).

          limit: Limits the number of objects returned in the response.

          location: Filters results by location. Specify an alpha-2 location code.

          log: Filters results by certificate log.

          offset: Skips the specified number of objects before fetching the results.

          origin: Filters results by origin.

          outage_cause: Filters results by outage cause.

          outage_type: Filters results by outage type.

          query: Filters results by a free-text match on the annotation description, id, or
              linked entities (location, ASN, origin).

          tags: Filters results by annotation tag. Matches annotations carrying at least one of
              the given tags.

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/annotations/outages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "bot": bot,
                        "ca": ca,
                        "data_source": data_source,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "geo_id": geo_id,
                        "limit": limit,
                        "location": location,
                        "log": log,
                        "offset": offset,
                        "origin": origin,
                        "outage_cause": outage_cause,
                        "outage_type": outage_type,
                        "query": query,
                        "tags": tags,
                        "tld": tld,
                    },
                    outage_get_params.OutageGetParams,
                ),
                post_parser=ResultWrapper[OutageGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[OutageGetResponse], ResultWrapper[OutageGetResponse]),
        )

    def locations(
        self,
        *,
        date_end: Union[str, datetime] | Omit = omit,
        date_range: str | Omit = omit,
        date_start: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OutageLocationsResponse:
        """
        Retrieves the number of outages by location.

        Args:
          date_end: End of the date range (inclusive). Alternative to `dateRange`; provide together
              with `dateStart`.

          date_range: Filters results by a relative date range ending at the current time. Use `<n>d`
              for days (up to `364d`) or `<n>w` for weeks (up to `52w`), e.g. `7d`. Append
              `control` to request the equivalent previous period for comparison: the
              comparison window is shifted back by the current window's length rounded up to a
              whole number of weeks, so it keeps the same weekday alignment and does not
              overlap the current window (e.g. `3dcontrol` covers days -10 to -7, `7dcontrol`
              covers days -14 to -7, `28dcontrol` covers days -56 to -28, and `10dcontrol`
              covers days -24 to -14). Mutually exclusive with `dateStart`/`dateEnd`.

          date_start: Start of the date range (inclusive). Alternative to `dateRange`; provide
              together with `dateEnd`.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/annotations/outages/locations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit": limit,
                    },
                    outage_locations_params.OutageLocationsParams,
                ),
                post_parser=ResultWrapper[OutageLocationsResponse]._unwrapper,
            ),
            cast_to=cast(Type[OutageLocationsResponse], ResultWrapper[OutageLocationsResponse]),
        )


class AsyncOutagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOutagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOutagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOutagesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        asn: int | Omit = omit,
        bot: str | Omit = omit,
        ca: str | Omit = omit,
        data_source: Literal[
            "ALL",
            "AI_BOTS",
            "AI_GATEWAY",
            "BGP",
            "BOTS",
            "CONNECTION_ANOMALY",
            "CT",
            "DNS",
            "DNS_MAGNITUDE",
            "DNS_AS112",
            "DOS",
            "EMAIL_ROUTING",
            "EMAIL_SECURITY",
            "FW",
            "FW_PG",
            "HTTP",
            "HTTP_CONTROL",
            "HTTP_CRAWLER_REFERER",
            "HTTP_ORIGINS",
            "IQI",
            "LEAKED_CREDENTIALS",
            "NET",
            "ROBOTS_TXT",
            "SPEED",
            "WORKERS_AI",
        ]
        | Omit = omit,
        date_end: Union[str, datetime] | Omit = omit,
        date_range: str | Omit = omit,
        date_start: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: str | Omit = omit,
        limit: int | Omit = omit,
        location: str | Omit = omit,
        log: str | Omit = omit,
        offset: int | Omit = omit,
        origin: str | Omit = omit,
        outage_cause: Literal[
            "BLOCKING",
            "CABLE_CUT",
            "CYBERATTACK",
            "DNS",
            "FIRE",
            "GOVERNMENT_DIRECTED",
            "MAINTENANCE",
            "MECHANICAL",
            "MILITARY_ACTION",
            "MISCONFIGURATION",
            "NATURAL_DISASTER",
            "NETWORK_PROBLEM",
            "POWER_OUTAGE",
            "SOFTWARE",
            "TECHNICAL_PROBLEM",
            "UNKNOWN",
            "WEATHER",
        ]
        | Omit = omit,
        outage_type: Literal["NATIONWIDE", "REGIONAL", "NETWORK", "PLATFORM"] | Omit = omit,
        query: str | Omit = omit,
        tags: List[
            Literal[
                "ADM1",
                "ADM2",
                "API_TRAFFIC",
                "ARC",
                "AS",
                "ASN",
                "ATTACKS",
                "AUTHOR",
                "BANDWIDTH",
                "BITRATE",
                "BOT",
                "BOT_CATEGORY",
                "BOT_CLASS",
                "BOT_KIND",
                "BOT_OPERATOR",
                "BROWSER",
                "BROWSER_FAMILY",
                "BYTES",
                "CA",
                "CACHE_HIT",
                "CA_OWNER",
                "CHECK_RESULT",
                "CLIENT_TYPE",
                "COMPROMISED",
                "CONTENT_TYPE",
                "CRAWL_PURPOSE",
                "CRAWL_REFER_RATIO",
                "DEVICE_TYPE",
                "DKIM",
                "DMARC",
                "DNS",
                "DNSSEC",
                "DNSSEC_AWARE",
                "DNSSEC_E2E",
                "DOMAIN_CATEGORY",
                "DURATION",
                "EDNS",
                "ENCRYPTED",
                "ENTRY_TYPE",
                "EXPIRATION_STATUS",
                "HAS_IPS",
                "HAS_MATCHING_ANSWER",
                "HAS_WILDCARDS",
                "HTTP_METHOD",
                "HTTP_PROTOCOL",
                "HTTP_VERSION",
                "INDUSTRY",
                "IP_VERSION",
                "JITTER",
                "KEY_AGREEMENT",
                "LATENCY",
                "LOCATION",
                "LOCATION_LATENCY",
                "LOG",
                "LOG_API",
                "LOG_OPERATOR",
                "MALICIOUS",
                "MANAGED_RULES",
                "MITIGATION_PRODUCT",
                "MODEL",
                "NAMESERVER_LATENCY",
                "ORIGIN",
                "ORIGIN_AS",
                "ORIGIN_LOCATION",
                "ORIGIN_TARGET_LOCATION_PAIR",
                "OS",
                "PERCENTILE",
                "POST_QUANTUM",
                "PREFIX",
                "PRODUCT",
                "PROTOCOL",
                "PROVIDER",
                "PUBLIC_KEY_ALGORITHM",
                "QUERY_TYPE",
                "REFERER",
                "REGION",
                "RESPONSE_CODE",
                "RESPONSE_STATUS",
                "RESPONSE_STATUS_CATEGORY",
                "RESPONSE_TTL",
                "SIGNATURE_ALGORITHM",
                "SPAM",
                "SPF",
                "SPOOF",
                "SUCCESS_RATE",
                "TARGET_LOCATION",
                "TASK",
                "THREAT_CATEGORY",
                "TLD",
                "TLD_DNS_MAGNITUDE",
                "TLS_VERSION",
                "UPDATE_TYPE",
                "USER_AGENT",
                "VALIDATION_LEVEL",
                "VECTOR",
                "VERTICAL",
            ]
        ]
        | Omit = omit,
        tld: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OutageGetResponse:
        """
        Retrieves the latest Internet outages and anomalies.

        Args:
          asn: Filters results by Autonomous System. Specify a single Autonomous System Number
              (ASN) as integer.

          bot: Filters results by bot.

          ca: Filters results by certificate authority.

          data_source: Filters results by data source.

          date_end: End of the date range (inclusive). Alternative to `dateRange`; provide together
              with `dateStart`.

          date_range: Filters results by a relative date range ending at the current time. Use `<n>d`
              for days (up to `364d`) or `<n>w` for weeks (up to `52w`), e.g. `7d`. Append
              `control` to request the equivalent previous period for comparison: the
              comparison window is shifted back by the current window's length rounded up to a
              whole number of weeks, so it keeps the same weekday alignment and does not
              overlap the current window (e.g. `3dcontrol` covers days -10 to -7, `7dcontrol`
              covers days -14 to -7, `28dcontrol` covers days -56 to -28, and `10dcontrol`
              covers days -24 to -14). Mutually exclusive with `dateStart`/`dateEnd`.

          date_start: Start of the date range (inclusive). Alternative to `dateRange`; provide
              together with `dateEnd`.

          format: Format in which results will be returned.

          geo_id: Filters results by geolocation. Refer to
              [GeoNames](https://download.geonames.org/export/dump/readme.txt).

          limit: Limits the number of objects returned in the response.

          location: Filters results by location. Specify an alpha-2 location code.

          log: Filters results by certificate log.

          offset: Skips the specified number of objects before fetching the results.

          origin: Filters results by origin.

          outage_cause: Filters results by outage cause.

          outage_type: Filters results by outage type.

          query: Filters results by a free-text match on the annotation description, id, or
              linked entities (location, ASN, origin).

          tags: Filters results by annotation tag. Matches annotations carrying at least one of
              the given tags.

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/annotations/outages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "bot": bot,
                        "ca": ca,
                        "data_source": data_source,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "geo_id": geo_id,
                        "limit": limit,
                        "location": location,
                        "log": log,
                        "offset": offset,
                        "origin": origin,
                        "outage_cause": outage_cause,
                        "outage_type": outage_type,
                        "query": query,
                        "tags": tags,
                        "tld": tld,
                    },
                    outage_get_params.OutageGetParams,
                ),
                post_parser=ResultWrapper[OutageGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[OutageGetResponse], ResultWrapper[OutageGetResponse]),
        )

    async def locations(
        self,
        *,
        date_end: Union[str, datetime] | Omit = omit,
        date_range: str | Omit = omit,
        date_start: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OutageLocationsResponse:
        """
        Retrieves the number of outages by location.

        Args:
          date_end: End of the date range (inclusive). Alternative to `dateRange`; provide together
              with `dateStart`.

          date_range: Filters results by a relative date range ending at the current time. Use `<n>d`
              for days (up to `364d`) or `<n>w` for weeks (up to `52w`), e.g. `7d`. Append
              `control` to request the equivalent previous period for comparison: the
              comparison window is shifted back by the current window's length rounded up to a
              whole number of weeks, so it keeps the same weekday alignment and does not
              overlap the current window (e.g. `3dcontrol` covers days -10 to -7, `7dcontrol`
              covers days -14 to -7, `28dcontrol` covers days -56 to -28, and `10dcontrol`
              covers days -24 to -14). Mutually exclusive with `dateStart`/`dateEnd`.

          date_start: Start of the date range (inclusive). Alternative to `dateRange`; provide
              together with `dateEnd`.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/annotations/outages/locations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit": limit,
                    },
                    outage_locations_params.OutageLocationsParams,
                ),
                post_parser=ResultWrapper[OutageLocationsResponse]._unwrapper,
            ),
            cast_to=cast(Type[OutageLocationsResponse], ResultWrapper[OutageLocationsResponse]),
        )


class OutagesResourceWithRawResponse:
    def __init__(self, outages: OutagesResource) -> None:
        self._outages = outages

        self.get = to_raw_response_wrapper(
            outages.get,
        )
        self.locations = to_raw_response_wrapper(
            outages.locations,
        )


class AsyncOutagesResourceWithRawResponse:
    def __init__(self, outages: AsyncOutagesResource) -> None:
        self._outages = outages

        self.get = async_to_raw_response_wrapper(
            outages.get,
        )
        self.locations = async_to_raw_response_wrapper(
            outages.locations,
        )


class OutagesResourceWithStreamingResponse:
    def __init__(self, outages: OutagesResource) -> None:
        self._outages = outages

        self.get = to_streamed_response_wrapper(
            outages.get,
        )
        self.locations = to_streamed_response_wrapper(
            outages.locations,
        )


class AsyncOutagesResourceWithStreamingResponse:
    def __init__(self, outages: AsyncOutagesResource) -> None:
        self._outages = outages

        self.get = async_to_streamed_response_wrapper(
            outages.get,
        )
        self.locations = async_to_streamed_response_wrapper(
            outages.locations,
        )
