# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

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
from .......types.radar.email.security.top.ases import DMARCGetResponse, dmarc_get_params

__all__ = ["DMARC", "AsyncDMARC"]


class DMARC(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DMARCWithRawResponse:
        return DMARCWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DMARCWithStreamingResponse:
        return DMARCWithStreamingResponse(self)

    def get(
        self,
        dmarc: Literal["PASS", "NONE", "FAIL"],
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
    ) -> DMARCGetResponse:
        """
        Get the top autonomous systems (AS) by emails DMARC validation.

        Args:
          dmarc: DMARC.

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
        if not dmarc:
            raise ValueError(f"Expected a non-empty value for `dmarc` but received {dmarc!r}")
        return self._get(
            f"/radar/email/security/top/ases/dmarc/{dmarc}",
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
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "spf": spf,
                    },
                    dmarc_get_params.DMARCGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DMARCGetResponse], ResultWrapper[DMARCGetResponse]),
        )


class AsyncDMARC(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDMARCWithRawResponse:
        return AsyncDMARCWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDMARCWithStreamingResponse:
        return AsyncDMARCWithStreamingResponse(self)

    async def get(
        self,
        dmarc: Literal["PASS", "NONE", "FAIL"],
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
    ) -> DMARCGetResponse:
        """
        Get the top autonomous systems (AS) by emails DMARC validation.

        Args:
          dmarc: DMARC.

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
        if not dmarc:
            raise ValueError(f"Expected a non-empty value for `dmarc` but received {dmarc!r}")
        return await self._get(
            f"/radar/email/security/top/ases/dmarc/{dmarc}",
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
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "spf": spf,
                    },
                    dmarc_get_params.DMARCGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DMARCGetResponse], ResultWrapper[DMARCGetResponse]),
        )


class DMARCWithRawResponse:
    def __init__(self, dmarc: DMARC) -> None:
        self._dmarc = dmarc

        self.get = to_raw_response_wrapper(
            dmarc.get,
        )


class AsyncDMARCWithRawResponse:
    def __init__(self, dmarc: AsyncDMARC) -> None:
        self._dmarc = dmarc

        self.get = async_to_raw_response_wrapper(
            dmarc.get,
        )


class DMARCWithStreamingResponse:
    def __init__(self, dmarc: DMARC) -> None:
        self._dmarc = dmarc

        self.get = to_streamed_response_wrapper(
            dmarc.get,
        )


class AsyncDMARCWithStreamingResponse:
    def __init__(self, dmarc: AsyncDMARC) -> None:
        self._dmarc = dmarc

        self.get = async_to_streamed_response_wrapper(
            dmarc.get,
        )
