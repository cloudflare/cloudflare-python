# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
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
from ....types.pcaps.ownerships import (
    ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse,
    validate_magic_pcap_collection_validate_buckets_for_full_packet_captures_params,
)

__all__ = ["Validates", "AsyncValidates"]


class Validates(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValidatesWithRawResponse:
        return ValidatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValidatesWithStreamingResponse:
        return ValidatesWithStreamingResponse(self)

    def magic_pcap_collection_validate_buckets_for_full_packet_captures(
        self,
        account_identifier: str,
        *,
        destination_conf: str,
        ownership_challenge: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse:
        """
        Validates buckets added to the packet captures API.

        Args:
          account_identifier: Identifier

          destination_conf: The full URI for the bucket. This field only applies to `full` packet captures.

          ownership_challenge: The ownership challenge filename stored in the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/pcaps/ownership/validate",
            body=maybe_transform(
                {
                    "destination_conf": destination_conf,
                    "ownership_challenge": ownership_challenge,
                },
                validate_magic_pcap_collection_validate_buckets_for_full_packet_captures_params.ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse],
                ResultWrapper[ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse],
            ),
        )


class AsyncValidates(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValidatesWithRawResponse:
        return AsyncValidatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValidatesWithStreamingResponse:
        return AsyncValidatesWithStreamingResponse(self)

    async def magic_pcap_collection_validate_buckets_for_full_packet_captures(
        self,
        account_identifier: str,
        *,
        destination_conf: str,
        ownership_challenge: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse:
        """
        Validates buckets added to the packet captures API.

        Args:
          account_identifier: Identifier

          destination_conf: The full URI for the bucket. This field only applies to `full` packet captures.

          ownership_challenge: The ownership challenge filename stored in the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/pcaps/ownership/validate",
            body=maybe_transform(
                {
                    "destination_conf": destination_conf,
                    "ownership_challenge": ownership_challenge,
                },
                validate_magic_pcap_collection_validate_buckets_for_full_packet_captures_params.ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse],
                ResultWrapper[ValidateMagicPcapCollectionValidateBucketsForFullPacketCapturesResponse],
            ),
        )


class ValidatesWithRawResponse:
    def __init__(self, validates: Validates) -> None:
        self._validates = validates

        self.magic_pcap_collection_validate_buckets_for_full_packet_captures = to_raw_response_wrapper(
            validates.magic_pcap_collection_validate_buckets_for_full_packet_captures,
        )


class AsyncValidatesWithRawResponse:
    def __init__(self, validates: AsyncValidates) -> None:
        self._validates = validates

        self.magic_pcap_collection_validate_buckets_for_full_packet_captures = async_to_raw_response_wrapper(
            validates.magic_pcap_collection_validate_buckets_for_full_packet_captures,
        )


class ValidatesWithStreamingResponse:
    def __init__(self, validates: Validates) -> None:
        self._validates = validates

        self.magic_pcap_collection_validate_buckets_for_full_packet_captures = to_streamed_response_wrapper(
            validates.magic_pcap_collection_validate_buckets_for_full_packet_captures,
        )


class AsyncValidatesWithStreamingResponse:
    def __init__(self, validates: AsyncValidates) -> None:
        self._validates = validates

        self.magic_pcap_collection_validate_buckets_for_full_packet_captures = async_to_streamed_response_wrapper(
            validates.magic_pcap_collection_validate_buckets_for_full_packet_captures,
        )
