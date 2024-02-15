# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import (
    make_request_options,
)
from ....types.logs.receiveds import FieldLogsReceivedListFieldsResponse

__all__ = ["Fields", "AsyncFields"]


class Fields(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FieldsWithRawResponse:
        return FieldsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FieldsWithStreamingResponse:
        return FieldsWithStreamingResponse(self)

    def logs_received_list_fields(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldLogsReceivedListFieldsResponse:
        """Lists all fields available.

        The response is json object with key-value pairs,
        where keys are field names, and values are descriptions.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/logs/received/fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldLogsReceivedListFieldsResponse,
        )


class AsyncFields(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFieldsWithRawResponse:
        return AsyncFieldsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFieldsWithStreamingResponse:
        return AsyncFieldsWithStreamingResponse(self)

    async def logs_received_list_fields(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldLogsReceivedListFieldsResponse:
        """Lists all fields available.

        The response is json object with key-value pairs,
        where keys are field names, and values are descriptions.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/logs/received/fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldLogsReceivedListFieldsResponse,
        )


class FieldsWithRawResponse:
    def __init__(self, fields: Fields) -> None:
        self._fields = fields

        self.logs_received_list_fields = to_raw_response_wrapper(
            fields.logs_received_list_fields,
        )


class AsyncFieldsWithRawResponse:
    def __init__(self, fields: AsyncFields) -> None:
        self._fields = fields

        self.logs_received_list_fields = async_to_raw_response_wrapper(
            fields.logs_received_list_fields,
        )


class FieldsWithStreamingResponse:
    def __init__(self, fields: Fields) -> None:
        self._fields = fields

        self.logs_received_list_fields = to_streamed_response_wrapper(
            fields.logs_received_list_fields,
        )


class AsyncFieldsWithStreamingResponse:
    def __init__(self, fields: AsyncFields) -> None:
        self._fields = fields

        self.logs_received_list_fields = async_to_streamed_response_wrapper(
            fields.logs_received_list_fields,
        )
