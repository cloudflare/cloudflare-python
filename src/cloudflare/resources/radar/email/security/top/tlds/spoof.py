# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ......._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......._compat import cached_property
from ......._resource import SyncAPIResource, AsyncAPIResource
from ......._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......._wrappers import ResultWrapper
from ......._base_client import make_request_options
from .......types.radar.email.security.top.tlds import spoof_get_params
from .......types.radar.email.security.top.tlds.spoof_get_response import SpoofGetResponse

__all__ = ["SpoofResource", "AsyncSpoofResource"]


class SpoofResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpoofResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SpoofResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpoofResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SpoofResourceWithStreamingResponse(self)

    def get(
        self,
        spoof: Literal["SPOOF", "NOT_SPOOF"],
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tld_category: Literal["CLASSIC", "COUNTRY"] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpoofGetResponse:
        """
        Retrieves the top TLDs by emails classified as spoof or not.

        Args:
          spoof: Spoof classification.

          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tld_category: Filters results by TLD category.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spoof:
            raise ValueError(f"Expected a non-empty value for `spoof` but received {spoof!r}")
        return self._get(
            f"/radar/email/security/top/tlds/spoof/{spoof}",
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
                        "limit": limit,
                        "name": name,
                        "spf": spf,
                        "tld_category": tld_category,
                        "tls_version": tls_version,
                    },
                    spoof_get_params.SpoofGetParams,
                ),
                post_parser=ResultWrapper[SpoofGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SpoofGetResponse], ResultWrapper[SpoofGetResponse]),
        )


class AsyncSpoofResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpoofResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpoofResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpoofResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSpoofResourceWithStreamingResponse(self)

    async def get(
        self,
        spoof: Literal["SPOOF", "NOT_SPOOF"],
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tld_category: Literal["CLASSIC", "COUNTRY"] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpoofGetResponse:
        """
        Retrieves the top TLDs by emails classified as spoof or not.

        Args:
          spoof: Spoof classification.

          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          tld_category: Filters results by TLD category.

          tls_version: Filters results by TLS version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spoof:
            raise ValueError(f"Expected a non-empty value for `spoof` but received {spoof!r}")
        return await self._get(
            f"/radar/email/security/top/tlds/spoof/{spoof}",
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
                        "limit": limit,
                        "name": name,
                        "spf": spf,
                        "tld_category": tld_category,
                        "tls_version": tls_version,
                    },
                    spoof_get_params.SpoofGetParams,
                ),
                post_parser=ResultWrapper[SpoofGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SpoofGetResponse], ResultWrapper[SpoofGetResponse]),
        )


class SpoofResourceWithRawResponse:
    def __init__(self, spoof: SpoofResource) -> None:
        self._spoof = spoof

        self.get = to_raw_response_wrapper(
            spoof.get,
        )


class AsyncSpoofResourceWithRawResponse:
    def __init__(self, spoof: AsyncSpoofResource) -> None:
        self._spoof = spoof

        self.get = async_to_raw_response_wrapper(
            spoof.get,
        )


class SpoofResourceWithStreamingResponse:
    def __init__(self, spoof: SpoofResource) -> None:
        self._spoof = spoof

        self.get = to_streamed_response_wrapper(
            spoof.get,
        )


class AsyncSpoofResourceWithStreamingResponse:
    def __init__(self, spoof: AsyncSpoofResource) -> None:
        self._spoof = spoof

        self.get = async_to_streamed_response_wrapper(
            spoof.get,
        )
