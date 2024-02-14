# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .validates import Validates, AsyncValidates

from ...._compat import cached_property

from ....types.pcaps import (
    OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse,
    OwnershipMagicPcapCollectionListPcaPsBucketOwnershipResponse,
)

from typing import Type, Optional

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
from ....types.pcaps import ownership_magic_pcap_collection_add_buckets_for_full_packet_captures_params
from .validates import (
    Validates,
    AsyncValidates,
    ValidatesWithRawResponse,
    AsyncValidatesWithRawResponse,
    ValidatesWithStreamingResponse,
    AsyncValidatesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Ownerships", "AsyncOwnerships"]


class Ownerships(SyncAPIResource):
    @cached_property
    def validates(self) -> Validates:
        return Validates(self._client)

    @cached_property
    def with_raw_response(self) -> OwnershipsWithRawResponse:
        return OwnershipsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OwnershipsWithStreamingResponse:
        return OwnershipsWithStreamingResponse(self)

    def delete(
        self,
        identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes buckets added to the packet captures API.

        Args:
          account_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_identifier}/pcaps/ownership/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def magic_pcap_collection_add_buckets_for_full_packet_captures(
        self,
        account_identifier: str,
        *,
        destination_conf: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse:
        """
        Adds an AWS or GCP bucket to use with full packet captures.

        Args:
          account_identifier: Identifier

          destination_conf: The full URI for the bucket. This field only applies to `full` packet captures.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/pcaps/ownership",
            body=maybe_transform(
                {"destination_conf": destination_conf},
                ownership_magic_pcap_collection_add_buckets_for_full_packet_captures_params.OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse],
                ResultWrapper[OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse],
            ),
        )

    def magic_pcap_collection_list_pca_ps_bucket_ownership(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OwnershipMagicPcapCollectionListPcaPsBucketOwnershipResponse]:
        """
        List all buckets configured for use with PCAPs API.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/pcaps/ownership",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OwnershipMagicPcapCollectionListPcaPsBucketOwnershipResponse]],
                ResultWrapper[OwnershipMagicPcapCollectionListPcaPsBucketOwnershipResponse],
            ),
        )


class AsyncOwnerships(AsyncAPIResource):
    @cached_property
    def validates(self) -> AsyncValidates:
        return AsyncValidates(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOwnershipsWithRawResponse:
        return AsyncOwnershipsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOwnershipsWithStreamingResponse:
        return AsyncOwnershipsWithStreamingResponse(self)

    async def delete(
        self,
        identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes buckets added to the packet captures API.

        Args:
          account_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_identifier}/pcaps/ownership/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def magic_pcap_collection_add_buckets_for_full_packet_captures(
        self,
        account_identifier: str,
        *,
        destination_conf: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse:
        """
        Adds an AWS or GCP bucket to use with full packet captures.

        Args:
          account_identifier: Identifier

          destination_conf: The full URI for the bucket. This field only applies to `full` packet captures.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/pcaps/ownership",
            body=maybe_transform(
                {"destination_conf": destination_conf},
                ownership_magic_pcap_collection_add_buckets_for_full_packet_captures_params.OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse],
                ResultWrapper[OwnershipMagicPcapCollectionAddBucketsForFullPacketCapturesResponse],
            ),
        )

    async def magic_pcap_collection_list_pca_ps_bucket_ownership(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OwnershipMagicPcapCollectionListPcaPsBucketOwnershipResponse]:
        """
        List all buckets configured for use with PCAPs API.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/pcaps/ownership",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OwnershipMagicPcapCollectionListPcaPsBucketOwnershipResponse]],
                ResultWrapper[OwnershipMagicPcapCollectionListPcaPsBucketOwnershipResponse],
            ),
        )


class OwnershipsWithRawResponse:
    def __init__(self, ownerships: Ownerships) -> None:
        self._ownerships = ownerships

        self.delete = to_raw_response_wrapper(
            ownerships.delete,
        )
        self.magic_pcap_collection_add_buckets_for_full_packet_captures = to_raw_response_wrapper(
            ownerships.magic_pcap_collection_add_buckets_for_full_packet_captures,
        )
        self.magic_pcap_collection_list_pca_ps_bucket_ownership = to_raw_response_wrapper(
            ownerships.magic_pcap_collection_list_pca_ps_bucket_ownership,
        )

    @cached_property
    def validates(self) -> ValidatesWithRawResponse:
        return ValidatesWithRawResponse(self._ownerships.validates)


class AsyncOwnershipsWithRawResponse:
    def __init__(self, ownerships: AsyncOwnerships) -> None:
        self._ownerships = ownerships

        self.delete = async_to_raw_response_wrapper(
            ownerships.delete,
        )
        self.magic_pcap_collection_add_buckets_for_full_packet_captures = async_to_raw_response_wrapper(
            ownerships.magic_pcap_collection_add_buckets_for_full_packet_captures,
        )
        self.magic_pcap_collection_list_pca_ps_bucket_ownership = async_to_raw_response_wrapper(
            ownerships.magic_pcap_collection_list_pca_ps_bucket_ownership,
        )

    @cached_property
    def validates(self) -> AsyncValidatesWithRawResponse:
        return AsyncValidatesWithRawResponse(self._ownerships.validates)


class OwnershipsWithStreamingResponse:
    def __init__(self, ownerships: Ownerships) -> None:
        self._ownerships = ownerships

        self.delete = to_streamed_response_wrapper(
            ownerships.delete,
        )
        self.magic_pcap_collection_add_buckets_for_full_packet_captures = to_streamed_response_wrapper(
            ownerships.magic_pcap_collection_add_buckets_for_full_packet_captures,
        )
        self.magic_pcap_collection_list_pca_ps_bucket_ownership = to_streamed_response_wrapper(
            ownerships.magic_pcap_collection_list_pca_ps_bucket_ownership,
        )

    @cached_property
    def validates(self) -> ValidatesWithStreamingResponse:
        return ValidatesWithStreamingResponse(self._ownerships.validates)


class AsyncOwnershipsWithStreamingResponse:
    def __init__(self, ownerships: AsyncOwnerships) -> None:
        self._ownerships = ownerships

        self.delete = async_to_streamed_response_wrapper(
            ownerships.delete,
        )
        self.magic_pcap_collection_add_buckets_for_full_packet_captures = async_to_streamed_response_wrapper(
            ownerships.magic_pcap_collection_add_buckets_for_full_packet_captures,
        )
        self.magic_pcap_collection_list_pca_ps_bucket_ownership = async_to_streamed_response_wrapper(
            ownerships.magic_pcap_collection_list_pca_ps_bucket_ownership,
        )

    @cached_property
    def validates(self) -> AsyncValidatesWithStreamingResponse:
        return AsyncValidatesWithStreamingResponse(self._ownerships.validates)
