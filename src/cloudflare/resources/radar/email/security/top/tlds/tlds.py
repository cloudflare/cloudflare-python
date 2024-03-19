# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .spam import (
    Spam,
    AsyncSpam,
    SpamWithRawResponse,
    AsyncSpamWithRawResponse,
    SpamWithStreamingResponse,
    AsyncSpamWithStreamingResponse,
)
from .spoof import (
    Spoof,
    AsyncSpoof,
    SpoofWithRawResponse,
    AsyncSpoofWithRawResponse,
    SpoofWithStreamingResponse,
    AsyncSpoofWithStreamingResponse,
)
from .malicious import (
    Malicious,
    AsyncMalicious,
    MaliciousWithRawResponse,
    AsyncMaliciousWithRawResponse,
    MaliciousWithStreamingResponse,
    AsyncMaliciousWithStreamingResponse,
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
from ......._base_client import (
    make_request_options,
)
from .......types.radar.email.security.top import TldGetResponse, tld_get_params

__all__ = ["Tlds", "AsyncTlds"]


class Tlds(SyncAPIResource):
    @cached_property
    def malicious(self) -> Malicious:
        return Malicious(self._client)

    @cached_property
    def spam(self) -> Spam:
        return Spam(self._client)

    @cached_property
    def spoof(self) -> Spoof:
        return Spoof(self._client)

    @cached_property
    def with_raw_response(self) -> TldsWithRawResponse:
        return TldsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TldsWithStreamingResponse:
        return TldsWithStreamingResponse(self)

    def get(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
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
        """Get the top TLDs by email messages.

        Values are a percentage out of the total
        emails.

        Args:
          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tld_category: Filter for TLDs by category.

          tls_version: Filter for tls version.

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TldGetResponse], ResultWrapper[TldGetResponse]),
        )


class AsyncTlds(AsyncAPIResource):
    @cached_property
    def malicious(self) -> AsyncMalicious:
        return AsyncMalicious(self._client)

    @cached_property
    def spam(self) -> AsyncSpam:
        return AsyncSpam(self._client)

    @cached_property
    def spoof(self) -> AsyncSpoof:
        return AsyncSpoof(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTldsWithRawResponse:
        return AsyncTldsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTldsWithStreamingResponse:
        return AsyncTldsWithStreamingResponse(self)

    async def get(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
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
        """Get the top TLDs by email messages.

        Values are a percentage out of the total
        emails.

        Args:
          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tld_category: Filter for TLDs by category.

          tls_version: Filter for tls version.

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TldGetResponse], ResultWrapper[TldGetResponse]),
        )


class TldsWithRawResponse:
    def __init__(self, tlds: Tlds) -> None:
        self._tlds = tlds

        self.get = to_raw_response_wrapper(
            tlds.get,
        )

    @cached_property
    def malicious(self) -> MaliciousWithRawResponse:
        return MaliciousWithRawResponse(self._tlds.malicious)

    @cached_property
    def spam(self) -> SpamWithRawResponse:
        return SpamWithRawResponse(self._tlds.spam)

    @cached_property
    def spoof(self) -> SpoofWithRawResponse:
        return SpoofWithRawResponse(self._tlds.spoof)


class AsyncTldsWithRawResponse:
    def __init__(self, tlds: AsyncTlds) -> None:
        self._tlds = tlds

        self.get = async_to_raw_response_wrapper(
            tlds.get,
        )

    @cached_property
    def malicious(self) -> AsyncMaliciousWithRawResponse:
        return AsyncMaliciousWithRawResponse(self._tlds.malicious)

    @cached_property
    def spam(self) -> AsyncSpamWithRawResponse:
        return AsyncSpamWithRawResponse(self._tlds.spam)

    @cached_property
    def spoof(self) -> AsyncSpoofWithRawResponse:
        return AsyncSpoofWithRawResponse(self._tlds.spoof)


class TldsWithStreamingResponse:
    def __init__(self, tlds: Tlds) -> None:
        self._tlds = tlds

        self.get = to_streamed_response_wrapper(
            tlds.get,
        )

    @cached_property
    def malicious(self) -> MaliciousWithStreamingResponse:
        return MaliciousWithStreamingResponse(self._tlds.malicious)

    @cached_property
    def spam(self) -> SpamWithStreamingResponse:
        return SpamWithStreamingResponse(self._tlds.spam)

    @cached_property
    def spoof(self) -> SpoofWithStreamingResponse:
        return SpoofWithStreamingResponse(self._tlds.spoof)


class AsyncTldsWithStreamingResponse:
    def __init__(self, tlds: AsyncTlds) -> None:
        self._tlds = tlds

        self.get = async_to_streamed_response_wrapper(
            tlds.get,
        )

    @cached_property
    def malicious(self) -> AsyncMaliciousWithStreamingResponse:
        return AsyncMaliciousWithStreamingResponse(self._tlds.malicious)

    @cached_property
    def spam(self) -> AsyncSpamWithStreamingResponse:
        return AsyncSpamWithStreamingResponse(self._tlds.spam)

    @cached_property
    def spoof(self) -> AsyncSpoofWithStreamingResponse:
        return AsyncSpoofWithStreamingResponse(self._tlds.spoof)
