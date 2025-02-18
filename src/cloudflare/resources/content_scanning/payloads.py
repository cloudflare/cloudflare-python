# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.content_scanning import payload_create_params
from ...types.content_scanning.payload_list_response import PayloadListResponse
from ...types.content_scanning.payload_create_response import PayloadCreateResponse
from ...types.content_scanning.payload_delete_response import PayloadDeleteResponse

__all__ = ["PayloadsResource", "AsyncPayloadsResource"]


class PayloadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PayloadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PayloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayloadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PayloadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        body: Iterable[payload_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[PayloadCreateResponse]:
        """
        Add custom scan expressions for Content Scanning

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/content-upload-scan/payloads",
            page=SyncSinglePage[PayloadCreateResponse],
            body=maybe_transform(body, Iterable[payload_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayloadCreateResponse,
            method="post",
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[PayloadListResponse]:
        """
        Get a list of existing custom scan expressions for Content Scanning

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/content-upload-scan/payloads",
            page=SyncSinglePage[PayloadListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayloadListResponse,
        )

    def delete(
        self,
        expression_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[PayloadDeleteResponse]:
        """
        Delete a Content Scan Custom Expression

        Args:
          zone_id: Identifier

          expression_id: The unique ID for this custom scan expression

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not expression_id:
            raise ValueError(f"Expected a non-empty value for `expression_id` but received {expression_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/content-upload-scan/payloads/{expression_id}",
            page=SyncSinglePage[PayloadDeleteResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayloadDeleteResponse,
            method="delete",
        )


class AsyncPayloadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPayloadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPayloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayloadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPayloadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        body: Iterable[payload_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PayloadCreateResponse, AsyncSinglePage[PayloadCreateResponse]]:
        """
        Add custom scan expressions for Content Scanning

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/content-upload-scan/payloads",
            page=AsyncSinglePage[PayloadCreateResponse],
            body=maybe_transform(body, Iterable[payload_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayloadCreateResponse,
            method="post",
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PayloadListResponse, AsyncSinglePage[PayloadListResponse]]:
        """
        Get a list of existing custom scan expressions for Content Scanning

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/content-upload-scan/payloads",
            page=AsyncSinglePage[PayloadListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayloadListResponse,
        )

    def delete(
        self,
        expression_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PayloadDeleteResponse, AsyncSinglePage[PayloadDeleteResponse]]:
        """
        Delete a Content Scan Custom Expression

        Args:
          zone_id: Identifier

          expression_id: The unique ID for this custom scan expression

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not expression_id:
            raise ValueError(f"Expected a non-empty value for `expression_id` but received {expression_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/content-upload-scan/payloads/{expression_id}",
            page=AsyncSinglePage[PayloadDeleteResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayloadDeleteResponse,
            method="delete",
        )


class PayloadsResourceWithRawResponse:
    def __init__(self, payloads: PayloadsResource) -> None:
        self._payloads = payloads

        self.create = to_raw_response_wrapper(
            payloads.create,
        )
        self.list = to_raw_response_wrapper(
            payloads.list,
        )
        self.delete = to_raw_response_wrapper(
            payloads.delete,
        )


class AsyncPayloadsResourceWithRawResponse:
    def __init__(self, payloads: AsyncPayloadsResource) -> None:
        self._payloads = payloads

        self.create = async_to_raw_response_wrapper(
            payloads.create,
        )
        self.list = async_to_raw_response_wrapper(
            payloads.list,
        )
        self.delete = async_to_raw_response_wrapper(
            payloads.delete,
        )


class PayloadsResourceWithStreamingResponse:
    def __init__(self, payloads: PayloadsResource) -> None:
        self._payloads = payloads

        self.create = to_streamed_response_wrapper(
            payloads.create,
        )
        self.list = to_streamed_response_wrapper(
            payloads.list,
        )
        self.delete = to_streamed_response_wrapper(
            payloads.delete,
        )


class AsyncPayloadsResourceWithStreamingResponse:
    def __init__(self, payloads: AsyncPayloadsResource) -> None:
        self._payloads = payloads

        self.create = async_to_streamed_response_wrapper(
            payloads.create,
        )
        self.list = async_to_streamed_response_wrapper(
            payloads.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            payloads.delete,
        )
