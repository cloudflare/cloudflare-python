# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.dex import ColoListResponse

from typing import Type, Optional

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.dex import colo_list_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Colos", "AsyncColos"]


class Colos(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ColosWithRawResponse:
        return ColosWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ColosWithStreamingResponse:
        return ColosWithStreamingResponse(self)

    def list(
        self,
        account_id: str,
        *,
        time_end: str,
        time_start: str,
        sort_by: Literal["fleet-status-usage", "application-tests-usage"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ColoListResponse]:
        """
        List Cloudflare colos that account's devices were connected to during a time
        period, sorted by usage starting from the most used colo. Colos without traffic
        are also returned and sorted alphabetically.

        Args:
          time_end: End time for connection period in RFC3339 (ISO 8601) format.

          time_start: Start time for connection period in RFC3339 (ISO 8601) format.

          sort_by: Type of usage that colos should be sorted by. If unspecified, returns all
              Cloudflare colos sorted alphabetically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/dex/colos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_end": time_end,
                        "time_start": time_start,
                        "sort_by": sort_by,
                    },
                    colo_list_params.ColoListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ColoListResponse]], ResultWrapper[ColoListResponse]),
        )


class AsyncColos(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncColosWithRawResponse:
        return AsyncColosWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncColosWithStreamingResponse:
        return AsyncColosWithStreamingResponse(self)

    async def list(
        self,
        account_id: str,
        *,
        time_end: str,
        time_start: str,
        sort_by: Literal["fleet-status-usage", "application-tests-usage"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ColoListResponse]:
        """
        List Cloudflare colos that account's devices were connected to during a time
        period, sorted by usage starting from the most used colo. Colos without traffic
        are also returned and sorted alphabetically.

        Args:
          time_end: End time for connection period in RFC3339 (ISO 8601) format.

          time_start: Start time for connection period in RFC3339 (ISO 8601) format.

          sort_by: Type of usage that colos should be sorted by. If unspecified, returns all
              Cloudflare colos sorted alphabetically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dex/colos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_end": time_end,
                        "time_start": time_start,
                        "sort_by": sort_by,
                    },
                    colo_list_params.ColoListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ColoListResponse]], ResultWrapper[ColoListResponse]),
        )


class ColosWithRawResponse:
    def __init__(self, colos: Colos) -> None:
        self._colos = colos

        self.list = to_raw_response_wrapper(
            colos.list,
        )


class AsyncColosWithRawResponse:
    def __init__(self, colos: AsyncColos) -> None:
        self._colos = colos

        self.list = async_to_raw_response_wrapper(
            colos.list,
        )


class ColosWithStreamingResponse:
    def __init__(self, colos: Colos) -> None:
        self._colos = colos

        self.list = to_streamed_response_wrapper(
            colos.list,
        )


class AsyncColosWithStreamingResponse:
    def __init__(self, colos: AsyncColos) -> None:
        self._colos = colos

        self.list = async_to_streamed_response_wrapper(
            colos.list,
        )
