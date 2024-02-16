# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .arc import (
    Arc,
    AsyncArc,
    ArcWithRawResponse,
    AsyncArcWithRawResponse,
    ArcWithStreamingResponse,
    AsyncArcWithStreamingResponse,
)
from .dkim import (
    DKIM,
    AsyncDKIM,
    DKIMWithRawResponse,
    AsyncDKIMWithRawResponse,
    DKIMWithStreamingResponse,
    AsyncDKIMWithStreamingResponse,
)
from .dmarc import (
    Dmarc,
    AsyncDmarc,
    DmarcWithRawResponse,
    AsyncDmarcWithRawResponse,
    DmarcWithStreamingResponse,
    AsyncDmarcWithStreamingResponse,
)
from ......._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......._utils import maybe_transform
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
from .......types.radar.emails.security.top import AseListResponse, ase_list_params

__all__ = ["Ases", "AsyncAses"]


class Ases(SyncAPIResource):
    @cached_property
    def arc(self) -> Arc:
        return Arc(self._client)

    @cached_property
    def dkim(self) -> DKIM:
        return DKIM(self._client)

    @cached_property
    def dmarc(self) -> Dmarc:
        return Dmarc(self._client)

    @cached_property
    def with_raw_response(self) -> AsesWithRawResponse:
        return AsesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsesWithStreamingResponse:
        return AsesWithStreamingResponse(self)

    def list(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
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
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AseListResponse:
        """Get the top autonomous systems (AS) by email messages.

        Values are a percentage
        out of the total emails.

        Args:
          arc: Filter for arc (Authenticated Received Chain).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/top/ases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "arc": arc,
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "spf": spf,
                    },
                    ase_list_params.AseListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AseListResponse], ResultWrapper[AseListResponse]),
        )


class AsyncAses(AsyncAPIResource):
    @cached_property
    def arc(self) -> AsyncArc:
        return AsyncArc(self._client)

    @cached_property
    def dkim(self) -> AsyncDKIM:
        return AsyncDKIM(self._client)

    @cached_property
    def dmarc(self) -> AsyncDmarc:
        return AsyncDmarc(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAsesWithRawResponse:
        return AsyncAsesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAsesWithStreamingResponse:
        return AsyncAsesWithStreamingResponse(self)

    async def list(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
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
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AseListResponse:
        """Get the top autonomous systems (AS) by email messages.

        Values are a percentage
        out of the total emails.

        Args:
          arc: Filter for arc (Authenticated Received Chain).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/top/ases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "arc": arc,
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "spf": spf,
                    },
                    ase_list_params.AseListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AseListResponse], ResultWrapper[AseListResponse]),
        )


class AsesWithRawResponse:
    def __init__(self, ases: Ases) -> None:
        self._ases = ases

        self.list = to_raw_response_wrapper(
            ases.list,
        )

    @cached_property
    def arc(self) -> ArcWithRawResponse:
        return ArcWithRawResponse(self._ases.arc)

    @cached_property
    def dkim(self) -> DKIMWithRawResponse:
        return DKIMWithRawResponse(self._ases.dkim)

    @cached_property
    def dmarc(self) -> DmarcWithRawResponse:
        return DmarcWithRawResponse(self._ases.dmarc)


class AsyncAsesWithRawResponse:
    def __init__(self, ases: AsyncAses) -> None:
        self._ases = ases

        self.list = async_to_raw_response_wrapper(
            ases.list,
        )

    @cached_property
    def arc(self) -> AsyncArcWithRawResponse:
        return AsyncArcWithRawResponse(self._ases.arc)

    @cached_property
    def dkim(self) -> AsyncDKIMWithRawResponse:
        return AsyncDKIMWithRawResponse(self._ases.dkim)

    @cached_property
    def dmarc(self) -> AsyncDmarcWithRawResponse:
        return AsyncDmarcWithRawResponse(self._ases.dmarc)


class AsesWithStreamingResponse:
    def __init__(self, ases: Ases) -> None:
        self._ases = ases

        self.list = to_streamed_response_wrapper(
            ases.list,
        )

    @cached_property
    def arc(self) -> ArcWithStreamingResponse:
        return ArcWithStreamingResponse(self._ases.arc)

    @cached_property
    def dkim(self) -> DKIMWithStreamingResponse:
        return DKIMWithStreamingResponse(self._ases.dkim)

    @cached_property
    def dmarc(self) -> DmarcWithStreamingResponse:
        return DmarcWithStreamingResponse(self._ases.dmarc)


class AsyncAsesWithStreamingResponse:
    def __init__(self, ases: AsyncAses) -> None:
        self._ases = ases

        self.list = async_to_streamed_response_wrapper(
            ases.list,
        )

    @cached_property
    def arc(self) -> AsyncArcWithStreamingResponse:
        return AsyncArcWithStreamingResponse(self._ases.arc)

    @cached_property
    def dkim(self) -> AsyncDKIMWithStreamingResponse:
        return AsyncDKIMWithStreamingResponse(self._ases.dkim)

    @cached_property
    def dmarc(self) -> AsyncDmarcWithStreamingResponse:
        return AsyncDmarcWithStreamingResponse(self._ases.dmarc)
