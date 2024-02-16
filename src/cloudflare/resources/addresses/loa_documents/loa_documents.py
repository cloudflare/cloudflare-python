# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .downloads import Downloads, AsyncDownloads

from ...._compat import cached_property

from ....types.addresses import LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse

from typing import Type

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.addresses import loa_document_ip_address_management_prefixes_upload_loa_document_params
from .downloads import (
    Downloads,
    AsyncDownloads,
    DownloadsWithRawResponse,
    AsyncDownloadsWithRawResponse,
    DownloadsWithStreamingResponse,
    AsyncDownloadsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["LoaDocuments", "AsyncLoaDocuments"]


class LoaDocuments(SyncAPIResource):
    @cached_property
    def downloads(self) -> Downloads:
        return Downloads(self._client)

    @cached_property
    def with_raw_response(self) -> LoaDocumentsWithRawResponse:
        return LoaDocumentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoaDocumentsWithStreamingResponse:
        return LoaDocumentsWithStreamingResponse(self)

    def ip_address_management_prefixes_upload_loa_document(
        self,
        account_id: str,
        *,
        loa_document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse:
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
            body=maybe_transform(
                {"loa_document": loa_document},
                loa_document_ip_address_management_prefixes_upload_loa_document_params.LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse],
                ResultWrapper[LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse],
            ),
        )


class AsyncLoaDocuments(AsyncAPIResource):
    @cached_property
    def downloads(self) -> AsyncDownloads:
        return AsyncDownloads(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLoaDocumentsWithRawResponse:
        return AsyncLoaDocumentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoaDocumentsWithStreamingResponse:
        return AsyncLoaDocumentsWithStreamingResponse(self)

    async def ip_address_management_prefixes_upload_loa_document(
        self,
        account_id: str,
        *,
        loa_document: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse:
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
            body=maybe_transform(
                {"loa_document": loa_document},
                loa_document_ip_address_management_prefixes_upload_loa_document_params.LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse],
                ResultWrapper[LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse],
            ),
        )


class LoaDocumentsWithRawResponse:
    def __init__(self, loa_documents: LoaDocuments) -> None:
        self._loa_documents = loa_documents

        self.ip_address_management_prefixes_upload_loa_document = to_raw_response_wrapper(
            loa_documents.ip_address_management_prefixes_upload_loa_document,
        )

    @cached_property
    def downloads(self) -> DownloadsWithRawResponse:
        return DownloadsWithRawResponse(self._loa_documents.downloads)


class AsyncLoaDocumentsWithRawResponse:
    def __init__(self, loa_documents: AsyncLoaDocuments) -> None:
        self._loa_documents = loa_documents

        self.ip_address_management_prefixes_upload_loa_document = async_to_raw_response_wrapper(
            loa_documents.ip_address_management_prefixes_upload_loa_document,
        )

    @cached_property
    def downloads(self) -> AsyncDownloadsWithRawResponse:
        return AsyncDownloadsWithRawResponse(self._loa_documents.downloads)


class LoaDocumentsWithStreamingResponse:
    def __init__(self, loa_documents: LoaDocuments) -> None:
        self._loa_documents = loa_documents

        self.ip_address_management_prefixes_upload_loa_document = to_streamed_response_wrapper(
            loa_documents.ip_address_management_prefixes_upload_loa_document,
        )

    @cached_property
    def downloads(self) -> DownloadsWithStreamingResponse:
        return DownloadsWithStreamingResponse(self._loa_documents.downloads)


class AsyncLoaDocumentsWithStreamingResponse:
    def __init__(self, loa_documents: AsyncLoaDocuments) -> None:
        self._loa_documents = loa_documents

        self.ip_address_management_prefixes_upload_loa_document = async_to_streamed_response_wrapper(
            loa_documents.ip_address_management_prefixes_upload_loa_document,
        )

    @cached_property
    def downloads(self) -> AsyncDownloadsWithStreamingResponse:
        return AsyncDownloadsWithStreamingResponse(self._loa_documents.downloads)
