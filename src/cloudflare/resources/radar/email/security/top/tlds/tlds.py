# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .spam import (
    SpamResource,
    AsyncSpamResource,
    SpamResourceWithRawResponse,
    AsyncSpamResourceWithRawResponse,
    SpamResourceWithStreamingResponse,
    AsyncSpamResourceWithStreamingResponse,
)
from .spoof import (
    SpoofResource,
    AsyncSpoofResource,
    SpoofResourceWithRawResponse,
    AsyncSpoofResourceWithRawResponse,
    SpoofResourceWithStreamingResponse,
    AsyncSpoofResourceWithStreamingResponse,
)
from .malicious import (
    MaliciousResource,
    AsyncMaliciousResource,
    MaliciousResourceWithRawResponse,
    AsyncMaliciousResourceWithRawResponse,
    MaliciousResourceWithStreamingResponse,
    AsyncMaliciousResourceWithStreamingResponse,
)
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
from .......types.radar.email.security.top import tld_get_params
from .......types.radar.email.security.top.tld_get_response import TldGetResponse

__all__ = ["TldsResource", "AsyncTldsResource"]


class TldsResource(SyncAPIResource):
    @cached_property
    def malicious(self) -> MaliciousResource:
        return MaliciousResource(self._client)

    @cached_property
    def spam(self) -> SpamResource:
        return SpamResource(self._client)

    @cached_property
    def spoof(self) -> SpoofResource:
        return SpoofResource(self._client)

    @cached_property
    def with_raw_response(self) -> TldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TldsResourceWithStreamingResponse(self)

    def get(
        self,
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
    ) -> TldGetResponse:
        """
        Retrieves the top TLDs by number of email messages.

        Args:
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
        return self._get(
            "/radar/email/security/top/tlds",
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
                    tld_get_params.TldGetParams,
                ),
                post_parser=ResultWrapper[TldGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[TldGetResponse], ResultWrapper[TldGetResponse]),
        )


class AsyncTldsResource(AsyncAPIResource):
    @cached_property
    def malicious(self) -> AsyncMaliciousResource:
        return AsyncMaliciousResource(self._client)

    @cached_property
    def spam(self) -> AsyncSpamResource:
        return AsyncSpamResource(self._client)

    @cached_property
    def spoof(self) -> AsyncSpoofResource:
        return AsyncSpoofResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTldsResourceWithStreamingResponse(self)

    async def get(
        self,
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
    ) -> TldGetResponse:
        """
        Retrieves the top TLDs by number of email messages.

        Args:
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
        return await self._get(
            "/radar/email/security/top/tlds",
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
                    tld_get_params.TldGetParams,
                ),
                post_parser=ResultWrapper[TldGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[TldGetResponse], ResultWrapper[TldGetResponse]),
        )


class TldsResourceWithRawResponse:
    def __init__(self, tlds: TldsResource) -> None:
        self._tlds = tlds

        self.get = to_raw_response_wrapper(
            tlds.get,
        )

    @cached_property
    def malicious(self) -> MaliciousResourceWithRawResponse:
        return MaliciousResourceWithRawResponse(self._tlds.malicious)

    @cached_property
    def spam(self) -> SpamResourceWithRawResponse:
        return SpamResourceWithRawResponse(self._tlds.spam)

    @cached_property
    def spoof(self) -> SpoofResourceWithRawResponse:
        return SpoofResourceWithRawResponse(self._tlds.spoof)


class AsyncTldsResourceWithRawResponse:
    def __init__(self, tlds: AsyncTldsResource) -> None:
        self._tlds = tlds

        self.get = async_to_raw_response_wrapper(
            tlds.get,
        )

    @cached_property
    def malicious(self) -> AsyncMaliciousResourceWithRawResponse:
        return AsyncMaliciousResourceWithRawResponse(self._tlds.malicious)

    @cached_property
    def spam(self) -> AsyncSpamResourceWithRawResponse:
        return AsyncSpamResourceWithRawResponse(self._tlds.spam)

    @cached_property
    def spoof(self) -> AsyncSpoofResourceWithRawResponse:
        return AsyncSpoofResourceWithRawResponse(self._tlds.spoof)


class TldsResourceWithStreamingResponse:
    def __init__(self, tlds: TldsResource) -> None:
        self._tlds = tlds

        self.get = to_streamed_response_wrapper(
            tlds.get,
        )

    @cached_property
    def malicious(self) -> MaliciousResourceWithStreamingResponse:
        return MaliciousResourceWithStreamingResponse(self._tlds.malicious)

    @cached_property
    def spam(self) -> SpamResourceWithStreamingResponse:
        return SpamResourceWithStreamingResponse(self._tlds.spam)

    @cached_property
    def spoof(self) -> SpoofResourceWithStreamingResponse:
        return SpoofResourceWithStreamingResponse(self._tlds.spoof)


class AsyncTldsResourceWithStreamingResponse:
    def __init__(self, tlds: AsyncTldsResource) -> None:
        self._tlds = tlds

        self.get = async_to_streamed_response_wrapper(
            tlds.get,
        )

    @cached_property
    def malicious(self) -> AsyncMaliciousResourceWithStreamingResponse:
        return AsyncMaliciousResourceWithStreamingResponse(self._tlds.malicious)

    @cached_property
    def spam(self) -> AsyncSpamResourceWithStreamingResponse:
        return AsyncSpamResourceWithStreamingResponse(self._tlds.spam)

    @cached_property
    def spoof(self) -> AsyncSpoofResourceWithStreamingResponse:
        return AsyncSpoofResourceWithStreamingResponse(self._tlds.spoof)
