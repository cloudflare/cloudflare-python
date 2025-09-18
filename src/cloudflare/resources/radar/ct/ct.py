# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Iterable, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .authorities import (
    AuthoritiesResource,
    AsyncAuthoritiesResource,
    AuthoritiesResourceWithRawResponse,
    AsyncAuthoritiesResourceWithRawResponse,
    AuthoritiesResourceWithStreamingResponse,
    AsyncAuthoritiesResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....types.radar import ct_summary_params, ct_timeseries_params, ct_timeseries_groups_params
from ...._base_client import make_request_options
from ....types.radar.ct_summary_response import CtSummaryResponse
from ....types.radar.ct_timeseries_response import CtTimeseriesResponse
from ....types.radar.ct_timeseries_groups_response import CtTimeseriesGroupsResponse

__all__ = ["CtResource", "AsyncCtResource"]


class CtResource(SyncAPIResource):
    @cached_property
    def authorities(self) -> AuthoritiesResource:
        return AuthoritiesResource(self._client)

    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CtResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CtResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CtResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CtResourceWithStreamingResponse(self)

    def summary(
        self,
        dimension: Literal[
            "CA",
            "CA_OWNER",
            "DURATION",
            "ENTRY_TYPE",
            "EXPIRATION_STATUS",
            "HAS_IPS",
            "HAS_WILDCARDS",
            "LOG",
            "LOG_API",
            "LOG_OPERATOR",
            "PUBLIC_KEY_ALGORITHM",
            "SIGNATURE_ALGORITHM",
            "TLD",
            "VALIDATION_LEVEL",
        ],
        *,
        ca: SequenceNotStr[str] | Omit = omit,
        ca_owner: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        duration: List[
            Literal[
                "LTE_3D",
                "GT_3D_LTE_7D",
                "GT_7D_LTE_10D",
                "GT_10D_LTE_47D",
                "GT_47D_LTE_100D",
                "GT_100D_LTE_200D",
                "GT_200D",
            ]
        ]
        | Omit = omit,
        entry_type: List[Literal["PRECERTIFICATE", "CERTIFICATE"]] | Omit = omit,
        expiration_status: List[Literal["EXPIRED", "VALID"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        has_ips: Iterable[bool] | Omit = omit,
        has_wildcards: Iterable[bool] | Omit = omit,
        limit_per_group: int | Omit = omit,
        log: SequenceNotStr[str] | Omit = omit,
        log_api: List[Literal["RFC6962", "STATIC"]] | Omit = omit,
        log_operator: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["RAW_VALUES", "PERCENTAGE"] | Omit = omit,
        public_key_algorithm: List[Literal["DSA", "ECDSA", "RSA"]] | Omit = omit,
        signature_algorithm: List[
            Literal[
                "DSA_SHA_1",
                "DSA_SHA_256",
                "ECDSA_SHA_1",
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
                "PSS_SHA_256",
                "PSS_SHA_384",
                "PSS_SHA_512",
                "RSA_MD2",
                "RSA_MD5",
                "RSA_SHA_1",
                "RSA_SHA_256",
                "RSA_SHA_384",
                "RSA_SHA_512",
            ]
        ]
        | Omit = omit,
        tld: SequenceNotStr[str] | Omit = omit,
        unique_entries: List[Literal["true", "false"]] | Omit = omit,
        validation_level: List[Literal["DOMAIN", "ORGANIZATION", "EXTENDED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CtSummaryResponse:
        """
        Retrieves an aggregated summary of certificates grouped by the specified
        dimension.

        Args:
          dimension: Specifies the certificate attribute by which to group the results.

          ca: Filters results by certificate authority.

          ca_owner: Filters results by certificate authority owner.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          duration: Filters results by certificate duration.

          entry_type: Filters results by entry type (certificate vs. pre-certificate).

          expiration_status: Filters results by expiration status (expired vs. valid).

          format: Format in which results will be returned.

          has_ips: Filters results based on whether the certificates are bound to specific IP
              addresses.

          has_wildcards: Filters results based on whether the certificates contain wildcard domains.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          log: Filters results by certificate log.

          log_api: Filters results by certificate log API (RFC6962 vs. static).

          log_operator: Filters results by certificate log operator.

          name: Array of names used to label the series in the response.

          normalization: Normalization method applied to the results. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          public_key_algorithm: Filters results by public key algorithm.

          signature_algorithm: Filters results by signature algorithm.

          tld: Filters results by top-level domain.

          unique_entries: Specifies whether to filter out duplicate certificates and pre-certificates. Set
              to true for unique entries only.

          validation_level: Filters results by validation level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            f"/radar/ct/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ca": ca,
                        "ca_owner": ca_owner,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "duration": duration,
                        "entry_type": entry_type,
                        "expiration_status": expiration_status,
                        "format": format,
                        "has_ips": has_ips,
                        "has_wildcards": has_wildcards,
                        "limit_per_group": limit_per_group,
                        "log": log,
                        "log_api": log_api,
                        "log_operator": log_operator,
                        "name": name,
                        "normalization": normalization,
                        "public_key_algorithm": public_key_algorithm,
                        "signature_algorithm": signature_algorithm,
                        "tld": tld,
                        "unique_entries": unique_entries,
                        "validation_level": validation_level,
                    },
                    ct_summary_params.CtSummaryParams,
                ),
                post_parser=ResultWrapper[CtSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[CtSummaryResponse], ResultWrapper[CtSummaryResponse]),
        )

    def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        ca: SequenceNotStr[str] | Omit = omit,
        ca_owner: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        duration: List[
            Literal[
                "LTE_3D",
                "GT_3D_LTE_7D",
                "GT_7D_LTE_10D",
                "GT_10D_LTE_47D",
                "GT_47D_LTE_100D",
                "GT_100D_LTE_200D",
                "GT_200D",
            ]
        ]
        | Omit = omit,
        entry_type: List[Literal["PRECERTIFICATE", "CERTIFICATE"]] | Omit = omit,
        expiration_status: List[Literal["EXPIRED", "VALID"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        has_ips: Iterable[bool] | Omit = omit,
        has_wildcards: Iterable[bool] | Omit = omit,
        log: SequenceNotStr[str] | Omit = omit,
        log_api: List[Literal["RFC6962", "STATIC"]] | Omit = omit,
        log_operator: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        public_key_algorithm: List[Literal["DSA", "ECDSA", "RSA"]] | Omit = omit,
        signature_algorithm: List[
            Literal[
                "DSA_SHA_1",
                "DSA_SHA_256",
                "ECDSA_SHA_1",
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
                "PSS_SHA_256",
                "PSS_SHA_384",
                "PSS_SHA_512",
                "RSA_MD2",
                "RSA_MD5",
                "RSA_SHA_1",
                "RSA_SHA_256",
                "RSA_SHA_384",
                "RSA_SHA_512",
            ]
        ]
        | Omit = omit,
        tld: SequenceNotStr[str] | Omit = omit,
        unique_entries: List[Literal["true", "false"]] | Omit = omit,
        validation_level: List[Literal["DOMAIN", "ORGANIZATION", "EXTENDED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CtTimeseriesResponse:
        """
        Retrieves certificate volume over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          ca: Filters results by certificate authority.

          ca_owner: Filters results by certificate authority owner.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          duration: Filters results by certificate duration.

          entry_type: Filters results by entry type (certificate vs. pre-certificate).

          expiration_status: Filters results by expiration status (expired vs. valid).

          format: Format in which results will be returned.

          has_ips: Filters results based on whether the certificates are bound to specific IP
              addresses.

          has_wildcards: Filters results based on whether the certificates contain wildcard domains.

          log: Filters results by certificate log.

          log_api: Filters results by certificate log API (RFC6962 vs. static).

          log_operator: Filters results by certificate log operator.

          name: Array of names used to label the series in the response.

          public_key_algorithm: Filters results by public key algorithm.

          signature_algorithm: Filters results by signature algorithm.

          tld: Filters results by top-level domain.

          unique_entries: Specifies whether to filter out duplicate certificates and pre-certificates. Set
              to true for unique entries only.

          validation_level: Filters results by validation level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/ct/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "ca": ca,
                        "ca_owner": ca_owner,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "duration": duration,
                        "entry_type": entry_type,
                        "expiration_status": expiration_status,
                        "format": format,
                        "has_ips": has_ips,
                        "has_wildcards": has_wildcards,
                        "log": log,
                        "log_api": log_api,
                        "log_operator": log_operator,
                        "name": name,
                        "public_key_algorithm": public_key_algorithm,
                        "signature_algorithm": signature_algorithm,
                        "tld": tld,
                        "unique_entries": unique_entries,
                        "validation_level": validation_level,
                    },
                    ct_timeseries_params.CtTimeseriesParams,
                ),
                post_parser=ResultWrapper[CtTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[CtTimeseriesResponse], ResultWrapper[CtTimeseriesResponse]),
        )

    def timeseries_groups(
        self,
        dimension: Literal[
            "CA",
            "CA_OWNER",
            "DURATION",
            "ENTRY_TYPE",
            "EXPIRATION_STATUS",
            "HAS_IPS",
            "HAS_WILDCARDS",
            "LOG",
            "LOG_API",
            "LOG_OPERATOR",
            "PUBLIC_KEY_ALGORITHM",
            "SIGNATURE_ALGORITHM",
            "TLD",
            "VALIDATION_LEVEL",
        ],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        ca: SequenceNotStr[str] | Omit = omit,
        ca_owner: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        duration: List[
            Literal[
                "LTE_3D",
                "GT_3D_LTE_7D",
                "GT_7D_LTE_10D",
                "GT_10D_LTE_47D",
                "GT_47D_LTE_100D",
                "GT_100D_LTE_200D",
                "GT_200D",
            ]
        ]
        | Omit = omit,
        entry_type: List[Literal["PRECERTIFICATE", "CERTIFICATE"]] | Omit = omit,
        expiration_status: List[Literal["EXPIRED", "VALID"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        has_ips: Iterable[bool] | Omit = omit,
        has_wildcards: Iterable[bool] | Omit = omit,
        limit_per_group: int | Omit = omit,
        log: SequenceNotStr[str] | Omit = omit,
        log_api: List[Literal["RFC6962", "STATIC"]] | Omit = omit,
        log_operator: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["RAW_VALUES", "PERCENTAGE"] | Omit = omit,
        public_key_algorithm: List[Literal["DSA", "ECDSA", "RSA"]] | Omit = omit,
        signature_algorithm: List[
            Literal[
                "DSA_SHA_1",
                "DSA_SHA_256",
                "ECDSA_SHA_1",
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
                "PSS_SHA_256",
                "PSS_SHA_384",
                "PSS_SHA_512",
                "RSA_MD2",
                "RSA_MD5",
                "RSA_SHA_1",
                "RSA_SHA_256",
                "RSA_SHA_384",
                "RSA_SHA_512",
            ]
        ]
        | Omit = omit,
        tld: SequenceNotStr[str] | Omit = omit,
        unique_entries: List[Literal["true", "false"]] | Omit = omit,
        validation_level: List[Literal["DOMAIN", "ORGANIZATION", "EXTENDED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CtTimeseriesGroupsResponse:
        """
        Retrieves the distribution of certificates grouped by chosen the specified
        dimension over time.

        Args:
          dimension: Specifies the certificate attribute by which to group the results.

          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          ca: Filters results by certificate authority.

          ca_owner: Filters results by certificate authority owner.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          duration: Filters results by certificate duration.

          entry_type: Filters results by entry type (certificate vs. pre-certificate).

          expiration_status: Filters results by expiration status (expired vs. valid).

          format: Format in which results will be returned.

          has_ips: Filters results based on whether the certificates are bound to specific IP
              addresses.

          has_wildcards: Filters results based on whether the certificates contain wildcard domains.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          log: Filters results by certificate log.

          log_api: Filters results by certificate log API (RFC6962 vs. static).

          log_operator: Filters results by certificate log operator.

          name: Array of names used to label the series in the response.

          normalization: Normalization method applied to the results. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          public_key_algorithm: Filters results by public key algorithm.

          signature_algorithm: Filters results by signature algorithm.

          tld: Filters results by top-level domain.

          unique_entries: Specifies whether to filter out duplicate certificates and pre-certificates. Set
              to true for unique entries only.

          validation_level: Filters results by validation level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            f"/radar/ct/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "ca": ca,
                        "ca_owner": ca_owner,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "duration": duration,
                        "entry_type": entry_type,
                        "expiration_status": expiration_status,
                        "format": format,
                        "has_ips": has_ips,
                        "has_wildcards": has_wildcards,
                        "limit_per_group": limit_per_group,
                        "log": log,
                        "log_api": log_api,
                        "log_operator": log_operator,
                        "name": name,
                        "normalization": normalization,
                        "public_key_algorithm": public_key_algorithm,
                        "signature_algorithm": signature_algorithm,
                        "tld": tld,
                        "unique_entries": unique_entries,
                        "validation_level": validation_level,
                    },
                    ct_timeseries_groups_params.CtTimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper[CtTimeseriesGroupsResponse]._unwrapper,
            ),
            cast_to=cast(Type[CtTimeseriesGroupsResponse], ResultWrapper[CtTimeseriesGroupsResponse]),
        )


class AsyncCtResource(AsyncAPIResource):
    @cached_property
    def authorities(self) -> AsyncAuthoritiesResource:
        return AsyncAuthoritiesResource(self._client)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCtResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCtResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCtResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCtResourceWithStreamingResponse(self)

    async def summary(
        self,
        dimension: Literal[
            "CA",
            "CA_OWNER",
            "DURATION",
            "ENTRY_TYPE",
            "EXPIRATION_STATUS",
            "HAS_IPS",
            "HAS_WILDCARDS",
            "LOG",
            "LOG_API",
            "LOG_OPERATOR",
            "PUBLIC_KEY_ALGORITHM",
            "SIGNATURE_ALGORITHM",
            "TLD",
            "VALIDATION_LEVEL",
        ],
        *,
        ca: SequenceNotStr[str] | Omit = omit,
        ca_owner: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        duration: List[
            Literal[
                "LTE_3D",
                "GT_3D_LTE_7D",
                "GT_7D_LTE_10D",
                "GT_10D_LTE_47D",
                "GT_47D_LTE_100D",
                "GT_100D_LTE_200D",
                "GT_200D",
            ]
        ]
        | Omit = omit,
        entry_type: List[Literal["PRECERTIFICATE", "CERTIFICATE"]] | Omit = omit,
        expiration_status: List[Literal["EXPIRED", "VALID"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        has_ips: Iterable[bool] | Omit = omit,
        has_wildcards: Iterable[bool] | Omit = omit,
        limit_per_group: int | Omit = omit,
        log: SequenceNotStr[str] | Omit = omit,
        log_api: List[Literal["RFC6962", "STATIC"]] | Omit = omit,
        log_operator: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["RAW_VALUES", "PERCENTAGE"] | Omit = omit,
        public_key_algorithm: List[Literal["DSA", "ECDSA", "RSA"]] | Omit = omit,
        signature_algorithm: List[
            Literal[
                "DSA_SHA_1",
                "DSA_SHA_256",
                "ECDSA_SHA_1",
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
                "PSS_SHA_256",
                "PSS_SHA_384",
                "PSS_SHA_512",
                "RSA_MD2",
                "RSA_MD5",
                "RSA_SHA_1",
                "RSA_SHA_256",
                "RSA_SHA_384",
                "RSA_SHA_512",
            ]
        ]
        | Omit = omit,
        tld: SequenceNotStr[str] | Omit = omit,
        unique_entries: List[Literal["true", "false"]] | Omit = omit,
        validation_level: List[Literal["DOMAIN", "ORGANIZATION", "EXTENDED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CtSummaryResponse:
        """
        Retrieves an aggregated summary of certificates grouped by the specified
        dimension.

        Args:
          dimension: Specifies the certificate attribute by which to group the results.

          ca: Filters results by certificate authority.

          ca_owner: Filters results by certificate authority owner.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          duration: Filters results by certificate duration.

          entry_type: Filters results by entry type (certificate vs. pre-certificate).

          expiration_status: Filters results by expiration status (expired vs. valid).

          format: Format in which results will be returned.

          has_ips: Filters results based on whether the certificates are bound to specific IP
              addresses.

          has_wildcards: Filters results based on whether the certificates contain wildcard domains.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          log: Filters results by certificate log.

          log_api: Filters results by certificate log API (RFC6962 vs. static).

          log_operator: Filters results by certificate log operator.

          name: Array of names used to label the series in the response.

          normalization: Normalization method applied to the results. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          public_key_algorithm: Filters results by public key algorithm.

          signature_algorithm: Filters results by signature algorithm.

          tld: Filters results by top-level domain.

          unique_entries: Specifies whether to filter out duplicate certificates and pre-certificates. Set
              to true for unique entries only.

          validation_level: Filters results by validation level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            f"/radar/ct/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ca": ca,
                        "ca_owner": ca_owner,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "duration": duration,
                        "entry_type": entry_type,
                        "expiration_status": expiration_status,
                        "format": format,
                        "has_ips": has_ips,
                        "has_wildcards": has_wildcards,
                        "limit_per_group": limit_per_group,
                        "log": log,
                        "log_api": log_api,
                        "log_operator": log_operator,
                        "name": name,
                        "normalization": normalization,
                        "public_key_algorithm": public_key_algorithm,
                        "signature_algorithm": signature_algorithm,
                        "tld": tld,
                        "unique_entries": unique_entries,
                        "validation_level": validation_level,
                    },
                    ct_summary_params.CtSummaryParams,
                ),
                post_parser=ResultWrapper[CtSummaryResponse]._unwrapper,
            ),
            cast_to=cast(Type[CtSummaryResponse], ResultWrapper[CtSummaryResponse]),
        )

    async def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        ca: SequenceNotStr[str] | Omit = omit,
        ca_owner: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        duration: List[
            Literal[
                "LTE_3D",
                "GT_3D_LTE_7D",
                "GT_7D_LTE_10D",
                "GT_10D_LTE_47D",
                "GT_47D_LTE_100D",
                "GT_100D_LTE_200D",
                "GT_200D",
            ]
        ]
        | Omit = omit,
        entry_type: List[Literal["PRECERTIFICATE", "CERTIFICATE"]] | Omit = omit,
        expiration_status: List[Literal["EXPIRED", "VALID"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        has_ips: Iterable[bool] | Omit = omit,
        has_wildcards: Iterable[bool] | Omit = omit,
        log: SequenceNotStr[str] | Omit = omit,
        log_api: List[Literal["RFC6962", "STATIC"]] | Omit = omit,
        log_operator: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        public_key_algorithm: List[Literal["DSA", "ECDSA", "RSA"]] | Omit = omit,
        signature_algorithm: List[
            Literal[
                "DSA_SHA_1",
                "DSA_SHA_256",
                "ECDSA_SHA_1",
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
                "PSS_SHA_256",
                "PSS_SHA_384",
                "PSS_SHA_512",
                "RSA_MD2",
                "RSA_MD5",
                "RSA_SHA_1",
                "RSA_SHA_256",
                "RSA_SHA_384",
                "RSA_SHA_512",
            ]
        ]
        | Omit = omit,
        tld: SequenceNotStr[str] | Omit = omit,
        unique_entries: List[Literal["true", "false"]] | Omit = omit,
        validation_level: List[Literal["DOMAIN", "ORGANIZATION", "EXTENDED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CtTimeseriesResponse:
        """
        Retrieves certificate volume over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          ca: Filters results by certificate authority.

          ca_owner: Filters results by certificate authority owner.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          duration: Filters results by certificate duration.

          entry_type: Filters results by entry type (certificate vs. pre-certificate).

          expiration_status: Filters results by expiration status (expired vs. valid).

          format: Format in which results will be returned.

          has_ips: Filters results based on whether the certificates are bound to specific IP
              addresses.

          has_wildcards: Filters results based on whether the certificates contain wildcard domains.

          log: Filters results by certificate log.

          log_api: Filters results by certificate log API (RFC6962 vs. static).

          log_operator: Filters results by certificate log operator.

          name: Array of names used to label the series in the response.

          public_key_algorithm: Filters results by public key algorithm.

          signature_algorithm: Filters results by signature algorithm.

          tld: Filters results by top-level domain.

          unique_entries: Specifies whether to filter out duplicate certificates and pre-certificates. Set
              to true for unique entries only.

          validation_level: Filters results by validation level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/ct/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "ca": ca,
                        "ca_owner": ca_owner,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "duration": duration,
                        "entry_type": entry_type,
                        "expiration_status": expiration_status,
                        "format": format,
                        "has_ips": has_ips,
                        "has_wildcards": has_wildcards,
                        "log": log,
                        "log_api": log_api,
                        "log_operator": log_operator,
                        "name": name,
                        "public_key_algorithm": public_key_algorithm,
                        "signature_algorithm": signature_algorithm,
                        "tld": tld,
                        "unique_entries": unique_entries,
                        "validation_level": validation_level,
                    },
                    ct_timeseries_params.CtTimeseriesParams,
                ),
                post_parser=ResultWrapper[CtTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[CtTimeseriesResponse], ResultWrapper[CtTimeseriesResponse]),
        )

    async def timeseries_groups(
        self,
        dimension: Literal[
            "CA",
            "CA_OWNER",
            "DURATION",
            "ENTRY_TYPE",
            "EXPIRATION_STATUS",
            "HAS_IPS",
            "HAS_WILDCARDS",
            "LOG",
            "LOG_API",
            "LOG_OPERATOR",
            "PUBLIC_KEY_ALGORITHM",
            "SIGNATURE_ALGORITHM",
            "TLD",
            "VALIDATION_LEVEL",
        ],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        ca: SequenceNotStr[str] | Omit = omit,
        ca_owner: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        duration: List[
            Literal[
                "LTE_3D",
                "GT_3D_LTE_7D",
                "GT_7D_LTE_10D",
                "GT_10D_LTE_47D",
                "GT_47D_LTE_100D",
                "GT_100D_LTE_200D",
                "GT_200D",
            ]
        ]
        | Omit = omit,
        entry_type: List[Literal["PRECERTIFICATE", "CERTIFICATE"]] | Omit = omit,
        expiration_status: List[Literal["EXPIRED", "VALID"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        has_ips: Iterable[bool] | Omit = omit,
        has_wildcards: Iterable[bool] | Omit = omit,
        limit_per_group: int | Omit = omit,
        log: SequenceNotStr[str] | Omit = omit,
        log_api: List[Literal["RFC6962", "STATIC"]] | Omit = omit,
        log_operator: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        normalization: Literal["RAW_VALUES", "PERCENTAGE"] | Omit = omit,
        public_key_algorithm: List[Literal["DSA", "ECDSA", "RSA"]] | Omit = omit,
        signature_algorithm: List[
            Literal[
                "DSA_SHA_1",
                "DSA_SHA_256",
                "ECDSA_SHA_1",
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
                "PSS_SHA_256",
                "PSS_SHA_384",
                "PSS_SHA_512",
                "RSA_MD2",
                "RSA_MD5",
                "RSA_SHA_1",
                "RSA_SHA_256",
                "RSA_SHA_384",
                "RSA_SHA_512",
            ]
        ]
        | Omit = omit,
        tld: SequenceNotStr[str] | Omit = omit,
        unique_entries: List[Literal["true", "false"]] | Omit = omit,
        validation_level: List[Literal["DOMAIN", "ORGANIZATION", "EXTENDED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CtTimeseriesGroupsResponse:
        """
        Retrieves the distribution of certificates grouped by chosen the specified
        dimension over time.

        Args:
          dimension: Specifies the certificate attribute by which to group the results.

          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          ca: Filters results by certificate authority.

          ca_owner: Filters results by certificate authority owner.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          duration: Filters results by certificate duration.

          entry_type: Filters results by entry type (certificate vs. pre-certificate).

          expiration_status: Filters results by expiration status (expired vs. valid).

          format: Format in which results will be returned.

          has_ips: Filters results based on whether the certificates are bound to specific IP
              addresses.

          has_wildcards: Filters results based on whether the certificates contain wildcard domains.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          log: Filters results by certificate log.

          log_api: Filters results by certificate log API (RFC6962 vs. static).

          log_operator: Filters results by certificate log operator.

          name: Array of names used to label the series in the response.

          normalization: Normalization method applied to the results. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          public_key_algorithm: Filters results by public key algorithm.

          signature_algorithm: Filters results by signature algorithm.

          tld: Filters results by top-level domain.

          unique_entries: Specifies whether to filter out duplicate certificates and pre-certificates. Set
              to true for unique entries only.

          validation_level: Filters results by validation level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            f"/radar/ct/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "ca": ca,
                        "ca_owner": ca_owner,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "duration": duration,
                        "entry_type": entry_type,
                        "expiration_status": expiration_status,
                        "format": format,
                        "has_ips": has_ips,
                        "has_wildcards": has_wildcards,
                        "limit_per_group": limit_per_group,
                        "log": log,
                        "log_api": log_api,
                        "log_operator": log_operator,
                        "name": name,
                        "normalization": normalization,
                        "public_key_algorithm": public_key_algorithm,
                        "signature_algorithm": signature_algorithm,
                        "tld": tld,
                        "unique_entries": unique_entries,
                        "validation_level": validation_level,
                    },
                    ct_timeseries_groups_params.CtTimeseriesGroupsParams,
                ),
                post_parser=ResultWrapper[CtTimeseriesGroupsResponse]._unwrapper,
            ),
            cast_to=cast(Type[CtTimeseriesGroupsResponse], ResultWrapper[CtTimeseriesGroupsResponse]),
        )


class CtResourceWithRawResponse:
    def __init__(self, ct: CtResource) -> None:
        self._ct = ct

        self.summary = to_raw_response_wrapper(
            ct.summary,
        )
        self.timeseries = to_raw_response_wrapper(
            ct.timeseries,
        )
        self.timeseries_groups = to_raw_response_wrapper(
            ct.timeseries_groups,
        )

    @cached_property
    def authorities(self) -> AuthoritiesResourceWithRawResponse:
        return AuthoritiesResourceWithRawResponse(self._ct.authorities)

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._ct.logs)


class AsyncCtResourceWithRawResponse:
    def __init__(self, ct: AsyncCtResource) -> None:
        self._ct = ct

        self.summary = async_to_raw_response_wrapper(
            ct.summary,
        )
        self.timeseries = async_to_raw_response_wrapper(
            ct.timeseries,
        )
        self.timeseries_groups = async_to_raw_response_wrapper(
            ct.timeseries_groups,
        )

    @cached_property
    def authorities(self) -> AsyncAuthoritiesResourceWithRawResponse:
        return AsyncAuthoritiesResourceWithRawResponse(self._ct.authorities)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._ct.logs)


class CtResourceWithStreamingResponse:
    def __init__(self, ct: CtResource) -> None:
        self._ct = ct

        self.summary = to_streamed_response_wrapper(
            ct.summary,
        )
        self.timeseries = to_streamed_response_wrapper(
            ct.timeseries,
        )
        self.timeseries_groups = to_streamed_response_wrapper(
            ct.timeseries_groups,
        )

    @cached_property
    def authorities(self) -> AuthoritiesResourceWithStreamingResponse:
        return AuthoritiesResourceWithStreamingResponse(self._ct.authorities)

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._ct.logs)


class AsyncCtResourceWithStreamingResponse:
    def __init__(self, ct: AsyncCtResource) -> None:
        self._ct = ct

        self.summary = async_to_streamed_response_wrapper(
            ct.summary,
        )
        self.timeseries = async_to_streamed_response_wrapper(
            ct.timeseries,
        )
        self.timeseries_groups = async_to_streamed_response_wrapper(
            ct.timeseries_groups,
        )

    @cached_property
    def authorities(self) -> AsyncAuthoritiesResourceWithStreamingResponse:
        return AsyncAuthoritiesResourceWithStreamingResponse(self._ct.authorities)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._ct.logs)
