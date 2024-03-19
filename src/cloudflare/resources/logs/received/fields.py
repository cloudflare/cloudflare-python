# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
from ....types.logs.received import FieldGetResponse

__all__ = ["Fields", "AsyncFields"]


class Fields(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FieldsWithRawResponse:
        return FieldsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FieldsWithStreamingResponse:
        return FieldsWithStreamingResponse(self)

    def get(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldGetResponse:
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
            cast_to=FieldGetResponse,
        )


class AsyncFields(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFieldsWithRawResponse:
        return AsyncFieldsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFieldsWithStreamingResponse:
        return AsyncFieldsWithStreamingResponse(self)

    async def get(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldGetResponse:
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
            cast_to=FieldGetResponse,
        )


class FieldsWithRawResponse:
    def __init__(self, fields: Fields) -> None:
        self._fields = fields

        self.get = to_raw_response_wrapper(
            fields.get,
        )


class AsyncFieldsWithRawResponse:
    def __init__(self, fields: AsyncFields) -> None:
        self._fields = fields

        self.get = async_to_raw_response_wrapper(
            fields.get,
        )


class FieldsWithStreamingResponse:
    def __init__(self, fields: Fields) -> None:
        self._fields = fields

        self.get = to_streamed_response_wrapper(
            fields.get,
        )


class AsyncFieldsWithStreamingResponse:
    def __init__(self, fields: AsyncFields) -> None:
        self._fields = fields

        self.get = async_to_streamed_response_wrapper(
            fields.get,
        )
