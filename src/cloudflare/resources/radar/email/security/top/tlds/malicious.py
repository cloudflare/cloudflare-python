# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......._compat import cached_property

from .......types.radar.email.security.top.tlds.malicious_get_response import MaliciousGetResponse

from ......._wrappers import ResultWrapper

from ......._utils import maybe_transform, async_maybe_transform

from ......._base_client import make_request_options

from typing import Type, List, Union

from typing_extensions import Literal

from datetime import datetime

from ......._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ......._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ......._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ......._resource import SyncAPIResource, AsyncAPIResource
from .......types import shared_params
from .......types.radar.email.security.top.tlds import malicious_get_params
from typing import cast
from typing import cast

__all__ = ["MaliciousResource", "AsyncMaliciousResource"]

class MaliciousResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MaliciousResourceWithRawResponse:
        return MaliciousResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MaliciousResourceWithStreamingResponse:
        return MaliciousResourceWithStreamingResponse(self)

    def get(self,
    malicious: Literal["MALICIOUS", "NOT_MALICIOUS"],
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> MaliciousGetResponse:
        """
        Get the TLDs by emails classified as malicious or not.

        Args:
          malicious: Malicious.

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
        if not malicious:
          raise ValueError(
            f'Expected a non-empty value for `malicious` but received {malicious!r}'
          )
        return self._get(
            f"/radar/email/security/top/tlds/malicious/{malicious}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
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
            }, malicious_get_params.MaliciousGetParams), post_parser=ResultWrapper[MaliciousGetResponse]._unwrapper),
            cast_to=cast(Type[MaliciousGetResponse], ResultWrapper[MaliciousGetResponse]),
        )

class AsyncMaliciousResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMaliciousResourceWithRawResponse:
        return AsyncMaliciousResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMaliciousResourceWithStreamingResponse:
        return AsyncMaliciousResourceWithStreamingResponse(self)

    async def get(self,
    malicious: Literal["MALICIOUS", "NOT_MALICIOUS"],
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> MaliciousGetResponse:
        """
        Get the TLDs by emails classified as malicious or not.

        Args:
          malicious: Malicious.

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
        if not malicious:
          raise ValueError(
            f'Expected a non-empty value for `malicious` but received {malicious!r}'
          )
        return await self._get(
            f"/radar/email/security/top/tlds/malicious/{malicious}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
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
            }, malicious_get_params.MaliciousGetParams), post_parser=ResultWrapper[MaliciousGetResponse]._unwrapper),
            cast_to=cast(Type[MaliciousGetResponse], ResultWrapper[MaliciousGetResponse]),
        )

class MaliciousResourceWithRawResponse:
    def __init__(self, malicious: MaliciousResource) -> None:
        self._malicious = malicious

        self.get = to_raw_response_wrapper(
            malicious.get,
        )

class AsyncMaliciousResourceWithRawResponse:
    def __init__(self, malicious: AsyncMaliciousResource) -> None:
        self._malicious = malicious

        self.get = async_to_raw_response_wrapper(
            malicious.get,
        )

class MaliciousResourceWithStreamingResponse:
    def __init__(self, malicious: MaliciousResource) -> None:
        self._malicious = malicious

        self.get = to_streamed_response_wrapper(
            malicious.get,
        )

class AsyncMaliciousResourceWithStreamingResponse:
    def __init__(self, malicious: AsyncMaliciousResource) -> None:
        self._malicious = malicious

        self.get = async_to_streamed_response_wrapper(
            malicious.get,
        )