# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.zaraz import ExportGetResponse
from ..._base_client import (
    make_request_options,
)

__all__ = ["Export", "AsyncExport"]


class Export(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportWithRawResponse:
        return ExportWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportWithStreamingResponse:
        return ExportWithStreamingResponse(self)

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExportGetResponse:
        """
        Exports full current published Zaraz configuration for a zone, secret variables
        included.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/zaraz/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportGetResponse,
        )


class AsyncExport(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportWithRawResponse:
        return AsyncExportWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportWithStreamingResponse:
        return AsyncExportWithStreamingResponse(self)

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExportGetResponse:
        """
        Exports full current published Zaraz configuration for a zone, secret variables
        included.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/zaraz/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportGetResponse,
        )


class ExportWithRawResponse:
    def __init__(self, export: Export) -> None:
        self._export = export

        self.get = to_raw_response_wrapper(
            export.get,
        )


class AsyncExportWithRawResponse:
    def __init__(self, export: AsyncExport) -> None:
        self._export = export

        self.get = async_to_raw_response_wrapper(
            export.get,
        )


class ExportWithStreamingResponse:
    def __init__(self, export: Export) -> None:
        self._export = export

        self.get = to_streamed_response_wrapper(
            export.get,
        )


class AsyncExportWithStreamingResponse:
    def __init__(self, export: AsyncExport) -> None:
        self._export = export

        self.get = async_to_streamed_response_wrapper(
            export.get,
        )
