# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.radar.email.security import (
    summary_arc_params,
    summary_spf_params,
    summary_dkim_params,
    summary_spam_params,
    summary_dmarc_params,
    summary_spoof_params,
    summary_malicious_params,
    summary_tls_version_params,
    summary_threat_category_params,
)
from .....types.radar.email.security.summary_arc_response import SummaryARCResponse
from .....types.radar.email.security.summary_spf_response import SummarySPFResponse
from .....types.radar.email.security.summary_dkim_response import SummaryDKIMResponse
from .....types.radar.email.security.summary_spam_response import SummarySpamResponse
from .....types.radar.email.security.summary_dmarc_response import SummaryDMARCResponse
from .....types.radar.email.security.summary_spoof_response import SummarySpoofResponse
from .....types.radar.email.security.summary_malicious_response import SummaryMaliciousResponse
from .....types.radar.email.security.summary_tls_version_response import SummaryTLSVersionResponse
from .....types.radar.email.security.summary_threat_category_response import SummaryThreatCategoryResponse

__all__ = ["SummaryResource", "AsyncSummaryResource"]


class SummaryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SummaryResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    def arc(
        self,
        *,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryARCResponse:
        """
        Retrieves the distribution of emails by ARC (Authenticated Received Chain)
        validation.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/summary/arc",
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
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    summary_arc_params.SummaryARCParams,
                ),
                post_parser=ResultWrapper[SummaryARCResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryARCResponse], ResultWrapper[SummaryARCResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    def dkim(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryDKIMResponse:
        """
        Retrieves the distribution of emails by DKIM (DomainKeys Identified Mail)
        validation.

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/summary/dkim",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    summary_dkim_params.SummaryDKIMParams,
                ),
                post_parser=ResultWrapper[SummaryDKIMResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryDKIMResponse], ResultWrapper[SummaryDKIMResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    def dmarc(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryDMARCResponse:
        """
        Retrieves the distribution of emails by DMARC (Domain-based Message
        Authentication, Reporting and Conformance) validation.

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/summary/dmarc",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    summary_dmarc_params.SummaryDMARCParams,
                ),
                post_parser=ResultWrapper[SummaryDMARCResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryDMARCResponse], ResultWrapper[SummaryDMARCResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    def malicious(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryMaliciousResponse:
        """
        Retrieves the distribution of emails by malicious classification.

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/summary/malicious",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    summary_malicious_params.SummaryMaliciousParams,
                ),
                post_parser=ResultWrapper[SummaryMaliciousResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryMaliciousResponse], ResultWrapper[SummaryMaliciousResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    def spam(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummarySpamResponse:
        """Retrieves the proportion of emails by spam classification (spam vs.

        non-spam).

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/summary/spam",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    summary_spam_params.SummarySpamParams,
                ),
                post_parser=ResultWrapper[SummarySpamResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummarySpamResponse], ResultWrapper[SummarySpamResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    def spf(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummarySPFResponse:
        """
        Retrieves the distribution of emails by SPF (Sender Policy Framework)
        validation.

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/summary/spf",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "tls_version": tls_version,
                    },
                    summary_spf_params.SummarySPFParams,
                ),
                post_parser=ResultWrapper[SummarySPFResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummarySPFResponse], ResultWrapper[SummarySPFResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    def spoof(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummarySpoofResponse:
        """
        Retrieves the proportion of emails by spoof classification (spoof vs.
        non-spoof).

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/summary/spoof",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    summary_spoof_params.SummarySpoofParams,
                ),
                post_parser=ResultWrapper[SummarySpoofResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummarySpoofResponse], ResultWrapper[SummarySpoofResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    def threat_category(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryThreatCategoryResponse:
        """
        Retrieves the distribution of emails by threat categories.

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/summary/threat_category",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    summary_threat_category_params.SummaryThreatCategoryParams,
                ),
                post_parser=ResultWrapper[SummaryThreatCategoryResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryThreatCategoryResponse], ResultWrapper[SummaryThreatCategoryResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    def tls_version(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryTLSVersionResponse:
        """
        Retrieves the distribution of emails by TLS version.

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/summary/tls_version",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                    },
                    summary_tls_version_params.SummaryTLSVersionParams,
                ),
                post_parser=ResultWrapper[SummaryTLSVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryTLSVersionResponse], ResultWrapper[SummaryTLSVersionResponse]),
        )


class AsyncSummaryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSummaryResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    async def arc(
        self,
        *,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryARCResponse:
        """
        Retrieves the distribution of emails by ARC (Authenticated Received Chain)
        validation.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/summary/arc",
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
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    summary_arc_params.SummaryARCParams,
                ),
                post_parser=ResultWrapper[SummaryARCResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryARCResponse], ResultWrapper[SummaryARCResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    async def dkim(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryDKIMResponse:
        """
        Retrieves the distribution of emails by DKIM (DomainKeys Identified Mail)
        validation.

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/summary/dkim",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    summary_dkim_params.SummaryDKIMParams,
                ),
                post_parser=ResultWrapper[SummaryDKIMResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryDKIMResponse], ResultWrapper[SummaryDKIMResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    async def dmarc(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryDMARCResponse:
        """
        Retrieves the distribution of emails by DMARC (Domain-based Message
        Authentication, Reporting and Conformance) validation.

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/summary/dmarc",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    summary_dmarc_params.SummaryDMARCParams,
                ),
                post_parser=ResultWrapper[SummaryDMARCResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryDMARCResponse], ResultWrapper[SummaryDMARCResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    async def malicious(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryMaliciousResponse:
        """
        Retrieves the distribution of emails by malicious classification.

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/summary/malicious",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    summary_malicious_params.SummaryMaliciousParams,
                ),
                post_parser=ResultWrapper[SummaryMaliciousResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryMaliciousResponse], ResultWrapper[SummaryMaliciousResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    async def spam(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummarySpamResponse:
        """Retrieves the proportion of emails by spam classification (spam vs.

        non-spam).

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/summary/spam",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    summary_spam_params.SummarySpamParams,
                ),
                post_parser=ResultWrapper[SummarySpamResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummarySpamResponse], ResultWrapper[SummarySpamResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    async def spf(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummarySPFResponse:
        """
        Retrieves the distribution of emails by SPF (Sender Policy Framework)
        validation.

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/summary/spf",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "tls_version": tls_version,
                    },
                    summary_spf_params.SummarySPFParams,
                ),
                post_parser=ResultWrapper[SummarySPFResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummarySPFResponse], ResultWrapper[SummarySPFResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    async def spoof(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummarySpoofResponse:
        """
        Retrieves the proportion of emails by spoof classification (spoof vs.
        non-spoof).

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/summary/spoof",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    summary_spoof_params.SummarySpoofParams,
                ),
                post_parser=ResultWrapper[SummarySpoofResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummarySpoofResponse], ResultWrapper[SummarySpoofResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    async def threat_category(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryThreatCategoryResponse:
        """
        Retrieves the distribution of emails by threat categories.

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/summary/threat_category",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    summary_threat_category_params.SummaryThreatCategoryParams,
                ),
                post_parser=ResultWrapper[SummaryThreatCategoryResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryThreatCategoryResponse], ResultWrapper[SummaryThreatCategoryResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar Email Security Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/email/subresources/security/methods/summary_v2/) instead."
    )
    async def tls_version(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryTLSVersionResponse:
        """
        Retrieves the distribution of emails by TLS version.

        Args:
          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/summary/tls_version",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                    },
                    summary_tls_version_params.SummaryTLSVersionParams,
                ),
                post_parser=ResultWrapper[SummaryTLSVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryTLSVersionResponse], ResultWrapper[SummaryTLSVersionResponse]),
        )


class SummaryResourceWithRawResponse:
    def __init__(self, summary: SummaryResource) -> None:
        self._summary = summary

        self.arc = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.arc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dkim = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.dkim,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dmarc = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.dmarc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.malicious = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.malicious,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spam = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.spam,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spf = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.spf,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spoof = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.spoof,  # pyright: ignore[reportDeprecated],
            )
        )
        self.threat_category = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.threat_category,  # pyright: ignore[reportDeprecated],
            )
        )
        self.tls_version = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.tls_version,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncSummaryResourceWithRawResponse:
    def __init__(self, summary: AsyncSummaryResource) -> None:
        self._summary = summary

        self.arc = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.arc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dkim = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.dkim,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dmarc = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.dmarc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.malicious = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.malicious,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spam = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.spam,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spf = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.spf,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spoof = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.spoof,  # pyright: ignore[reportDeprecated],
            )
        )
        self.threat_category = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.threat_category,  # pyright: ignore[reportDeprecated],
            )
        )
        self.tls_version = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.tls_version,  # pyright: ignore[reportDeprecated],
            )
        )


class SummaryResourceWithStreamingResponse:
    def __init__(self, summary: SummaryResource) -> None:
        self._summary = summary

        self.arc = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.arc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dkim = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.dkim,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dmarc = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.dmarc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.malicious = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.malicious,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spam = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.spam,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spf = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.spf,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spoof = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.spoof,  # pyright: ignore[reportDeprecated],
            )
        )
        self.threat_category = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.threat_category,  # pyright: ignore[reportDeprecated],
            )
        )
        self.tls_version = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.tls_version,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncSummaryResourceWithStreamingResponse:
    def __init__(self, summary: AsyncSummaryResource) -> None:
        self._summary = summary

        self.arc = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.arc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dkim = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.dkim,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dmarc = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.dmarc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.malicious = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.malicious,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spam = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.spam,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spf = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.spf,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spoof = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.spoof,  # pyright: ignore[reportDeprecated],
            )
        )
        self.threat_category = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.threat_category,  # pyright: ignore[reportDeprecated],
            )
        )
        self.tls_version = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.tls_version,  # pyright: ignore[reportDeprecated],
            )
        )
