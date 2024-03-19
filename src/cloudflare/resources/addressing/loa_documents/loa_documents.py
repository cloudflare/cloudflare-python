# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .downloads import (
    Downloads,
    AsyncDownloads,
    DownloadsWithRawResponse,
    AsyncDownloadsWithRawResponse,
    DownloadsWithStreamingResponse,
    AsyncDownloadsWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.addressing import LOADocumentCreateResponse, loa_document_create_params

__all__ = ["LOADocuments", "AsyncLOADocuments"]


class LOADocuments(SyncAPIResource):
    @cached_property
    def downloads(self) -> Downloads:
        return Downloads(self._client)

    @cached_property
    def with_raw_response(self) -> LOADocumentsWithRawResponse:
        return LOADocumentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LOADocumentsWithStreamingResponse:
        return LOADocumentsWithStreamingResponse(self)

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
    ) -> LOADocumentCreateResponse:
        """
        Submit LOA document (pdf format) under the account.

        Args:
          account_id: Identifier

          loa_document: LOA document to upload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/addressing/loa_documents",
            body=maybe_transform({"loa_document": loa_document}, loa_document_create_params.LOADocumentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LOADocumentCreateResponse], ResultWrapper[LOADocumentCreateResponse]),
        )


class AsyncLOADocuments(AsyncAPIResource):
    @cached_property
    def downloads(self) -> AsyncDownloads:
        return AsyncDownloads(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLOADocumentsWithRawResponse:
        return AsyncLOADocumentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLOADocumentsWithStreamingResponse:
        return AsyncLOADocumentsWithStreamingResponse(self)

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
    ) -> LOADocumentCreateResponse:
        """
        Submit LOA document (pdf format) under the account.

        Args:
          account_id: Identifier

          loa_document: LOA document to upload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LOADocumentCreateResponse], ResultWrapper[LOADocumentCreateResponse]),
        )


class LOADocumentsWithRawResponse:
    def __init__(self, loa_documents: LOADocuments) -> None:
        self._loa_documents = loa_documents

        self.create = to_raw_response_wrapper(
            loa_documents.create,
        )

    @cached_property
    def downloads(self) -> DownloadsWithRawResponse:
        return DownloadsWithRawResponse(self._loa_documents.downloads)


class AsyncLOADocumentsWithRawResponse:
    def __init__(self, loa_documents: AsyncLOADocuments) -> None:
        self._loa_documents = loa_documents

        self.create = async_to_raw_response_wrapper(
            loa_documents.create,
        )

    @cached_property
    def downloads(self) -> AsyncDownloadsWithRawResponse:
        return AsyncDownloadsWithRawResponse(self._loa_documents.downloads)


class LOADocumentsWithStreamingResponse:
    def __init__(self, loa_documents: LOADocuments) -> None:
        self._loa_documents = loa_documents

        self.create = to_streamed_response_wrapper(
            loa_documents.create,
        )

    @cached_property
    def downloads(self) -> DownloadsWithStreamingResponse:
        return DownloadsWithStreamingResponse(self._loa_documents.downloads)


class AsyncLOADocumentsWithStreamingResponse:
    def __init__(self, loa_documents: AsyncLOADocuments) -> None:
        self._loa_documents = loa_documents

        self.create = async_to_streamed_response_wrapper(
            loa_documents.create,
        )

    @cached_property
    def downloads(self) -> AsyncDownloadsWithStreamingResponse:
        return AsyncDownloadsWithStreamingResponse(self._loa_documents.downloads)
