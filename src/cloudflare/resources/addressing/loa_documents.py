# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.addressing import loa_document_create_params
from ...types.addressing.loa_document_create_response import LOADocumentCreateResponse

__all__ = ["LOADocumentsResource", "AsyncLOADocumentsResource"]


class LOADocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LOADocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LOADocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LOADocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LOADocumentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        loa_document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LOADocumentCreateResponse]:
        """
        Submit LOA document (pdf format) under the account.

        Args:
          account_id: Identifier of a Cloudflare account.

          loa_document: LOA document to upload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/accounts/{account_id}/addressing/loa_documents",
            body=maybe_transform({"loa_document": loa_document}, loa_document_create_params.LOADocumentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LOADocumentCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LOADocumentCreateResponse]], ResultWrapper[LOADocumentCreateResponse]),
        )

    def get(
        self,
        loa_document_id: Optional[str],
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
        Download specified LOA document under the account.

        Args:
          account_id: Identifier of a Cloudflare account.

          loa_document_id: Identifier for the uploaded LOA document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not loa_document_id:
            raise ValueError(f"Expected a non-empty value for `loa_document_id` but received {loa_document_id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/addressing/loa_documents/{loa_document_id}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncLOADocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLOADocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLOADocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLOADocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLOADocumentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        loa_document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LOADocumentCreateResponse]:
        """
        Submit LOA document (pdf format) under the account.

        Args:
          account_id: Identifier of a Cloudflare account.

          loa_document: LOA document to upload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/addressing/loa_documents",
            body=await async_maybe_transform(
                {"loa_document": loa_document}, loa_document_create_params.LOADocumentCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LOADocumentCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LOADocumentCreateResponse]], ResultWrapper[LOADocumentCreateResponse]),
        )

    async def get(
        self,
        loa_document_id: Optional[str],
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
        Download specified LOA document under the account.

        Args:
          account_id: Identifier of a Cloudflare account.

          loa_document_id: Identifier for the uploaded LOA document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not loa_document_id:
            raise ValueError(f"Expected a non-empty value for `loa_document_id` but received {loa_document_id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/addressing/loa_documents/{loa_document_id}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class LOADocumentsResourceWithRawResponse:
    def __init__(self, loa_documents: LOADocumentsResource) -> None:
        self._loa_documents = loa_documents

        self.create = to_raw_response_wrapper(
            loa_documents.create,
        )
        self.get = to_custom_raw_response_wrapper(
            loa_documents.get,
            BinaryAPIResponse,
        )


class AsyncLOADocumentsResourceWithRawResponse:
    def __init__(self, loa_documents: AsyncLOADocumentsResource) -> None:
        self._loa_documents = loa_documents

        self.create = async_to_raw_response_wrapper(
            loa_documents.create,
        )
        self.get = async_to_custom_raw_response_wrapper(
            loa_documents.get,
            AsyncBinaryAPIResponse,
        )


class LOADocumentsResourceWithStreamingResponse:
    def __init__(self, loa_documents: LOADocumentsResource) -> None:
        self._loa_documents = loa_documents

        self.create = to_streamed_response_wrapper(
            loa_documents.create,
        )
        self.get = to_custom_streamed_response_wrapper(
            loa_documents.get,
            StreamedBinaryAPIResponse,
        )


class AsyncLOADocumentsResourceWithStreamingResponse:
    def __init__(self, loa_documents: AsyncLOADocumentsResource) -> None:
        self._loa_documents = loa_documents

        self.create = async_to_streamed_response_wrapper(
            loa_documents.create,
        )
        self.get = async_to_custom_streamed_response_wrapper(
            loa_documents.get,
            AsyncStreamedBinaryAPIResponse,
        )
