# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._base_client import (
    make_request_options,
)

__all__ = ["ContentV2", "AsyncContentV2"]


class ContentV2(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentV2WithRawResponse:
        return ContentV2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentV2WithStreamingResponse:
        return ContentV2WithStreamingResponse(self)

    def get(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Fetch script content only

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        extra_headers = {"Accept": "string", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/content/v2",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncContentV2(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentV2WithRawResponse:
        return AsyncContentV2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentV2WithStreamingResponse:
        return AsyncContentV2WithStreamingResponse(self)

    async def get(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Fetch script content only

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        extra_headers = {"Accept": "string", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/content/v2",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ContentV2WithRawResponse:
    def __init__(self, content_v2: ContentV2) -> None:
        self._content_v2 = content_v2

        self.get = to_custom_raw_response_wrapper(
            content_v2.get,
            BinaryAPIResponse,
        )


class AsyncContentV2WithRawResponse:
    def __init__(self, content_v2: AsyncContentV2) -> None:
        self._content_v2 = content_v2

        self.get = async_to_custom_raw_response_wrapper(
            content_v2.get,
            AsyncBinaryAPIResponse,
        )


class ContentV2WithStreamingResponse:
    def __init__(self, content_v2: ContentV2) -> None:
        self._content_v2 = content_v2

        self.get = to_custom_streamed_response_wrapper(
            content_v2.get,
            StreamedBinaryAPIResponse,
        )


class AsyncContentV2WithStreamingResponse:
    def __init__(self, content_v2: AsyncContentV2) -> None:
        self._content_v2 = content_v2

        self.get = async_to_custom_streamed_response_wrapper(
            content_v2.get,
            AsyncStreamedBinaryAPIResponse,
        )
