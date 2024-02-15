# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, Optional, cast, overload
from typing_extensions import Literal

import httpx

from ...types import (
    PcapGetResponse,
    PcapMagicPcapCollectionCreatePcapRequestResponse,
    PcapMagicPcapCollectionListPacketCaptureRequestsResponse,
    pcap_magic_pcap_collection_create_pcap_request_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import required_args, maybe_transform
from ..._compat import cached_property
from .downloads import (
    Downloads,
    AsyncDownloads,
    DownloadsWithRawResponse,
    AsyncDownloadsWithRawResponse,
    DownloadsWithStreamingResponse,
    AsyncDownloadsWithStreamingResponse,
)
from .ownerships import (
    Ownerships,
    AsyncOwnerships,
    OwnershipsWithRawResponse,
    AsyncOwnershipsWithRawResponse,
    OwnershipsWithStreamingResponse,
    AsyncOwnershipsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from .ownerships.ownerships import Ownerships, AsyncOwnerships

__all__ = ["Pcaps", "AsyncPcaps"]


class Pcaps(SyncAPIResource):
    @cached_property
    def ownerships(self) -> Ownerships:
        return Ownerships(self._client)

    @cached_property
    def downloads(self) -> Downloads:
        return Downloads(self._client)

    @cached_property
    def with_raw_response(self) -> PcapsWithRawResponse:
        return PcapsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PcapsWithStreamingResponse:
        return PcapsWithStreamingResponse(self)

    def get(
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
    ) -> PcapGetResponse:
        """
        Get information for a PCAP request by id.

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
        return cast(
            PcapGetResponse,
            self._get(
                f"/accounts/{account_identifier}/pcaps/{identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PcapGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def magic_pcap_collection_create_pcap_request(
        self,
        account_identifier: str,
        *,
        packet_limit: float,
        system: Literal["magic-transit"],
        time_limit: float,
        type: Literal["simple", "full"],
        filter_v1: pcap_magic_pcap_collection_create_pcap_request_params._6wtRj17BPcapsRequestSimpleFilterV1
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PcapMagicPcapCollectionCreatePcapRequestResponse:
        """
        Create new PCAP request for account.

        Args:
          account_identifier: Identifier

          packet_limit: The limit of packets contained in a packet capture.

          system: The system used to collect packet captures.

          time_limit: The packet capture duration in seconds.

          type: The type of packet capture. `Simple` captures sampled packets, and `full`
              captures entire payloads and non-sampled packets.

          filter_v1: The packet capture filter. When this field is empty, all packets are captured.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def magic_pcap_collection_create_pcap_request(
        self,
        account_identifier: str,
        *,
        colo_name: str,
        destination_conf: str,
        system: Literal["magic-transit"],
        time_limit: float,
        type: Literal["simple", "full"],
        byte_limit: float | NotGiven = NOT_GIVEN,
        filter_v1: pcap_magic_pcap_collection_create_pcap_request_params._6wtRj17BPcapsRequestFullFilterV1
        | NotGiven = NOT_GIVEN,
        packet_limit: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PcapMagicPcapCollectionCreatePcapRequestResponse:
        """
        Create new PCAP request for account.

        Args:
          account_identifier: Identifier

          colo_name: The name of the data center used for the packet capture. This can be a specific
              colo (ord02) or a multi-colo name (ORD). This field only applies to `full`
              packet captures.

          destination_conf: The full URI for the bucket. This field only applies to `full` packet captures.

          system: The system used to collect packet captures.

          time_limit: The packet capture duration in seconds.

          type: The type of packet capture. `Simple` captures sampled packets, and `full`
              captures entire payloads and non-sampled packets.

          byte_limit: The maximum number of bytes to capture. This field only applies to `full` packet
              captures.

          filter_v1: The packet capture filter. When this field is empty, all packets are captured.

          packet_limit: The limit of packets contained in a packet capture.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["packet_limit", "system", "time_limit", "type"],
        ["colo_name", "destination_conf", "system", "time_limit", "type"],
    )
    def magic_pcap_collection_create_pcap_request(
        self,
        account_identifier: str,
        *,
        packet_limit: float | NotGiven = NOT_GIVEN,
        system: Literal["magic-transit"],
        time_limit: float,
        type: Literal["simple", "full"],
        filter_v1: pcap_magic_pcap_collection_create_pcap_request_params._6wtRj17BPcapsRequestSimpleFilterV1
        | NotGiven = NOT_GIVEN,
        colo_name: str | NotGiven = NOT_GIVEN,
        destination_conf: str | NotGiven = NOT_GIVEN,
        byte_limit: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PcapMagicPcapCollectionCreatePcapRequestResponse:
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return cast(
            PcapMagicPcapCollectionCreatePcapRequestResponse,
            self._post(
                f"/accounts/{account_identifier}/pcaps",
                body=maybe_transform(
                    {
                        "packet_limit": packet_limit,
                        "system": system,
                        "time_limit": time_limit,
                        "type": type,
                        "filter_v1": filter_v1,
                        "colo_name": colo_name,
                        "destination_conf": destination_conf,
                        "byte_limit": byte_limit,
                    },
                    pcap_magic_pcap_collection_create_pcap_request_params.PcapMagicPcapCollectionCreatePcapRequestParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PcapMagicPcapCollectionCreatePcapRequestResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def magic_pcap_collection_list_packet_capture_requests(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PcapMagicPcapCollectionListPacketCaptureRequestsResponse]:
        """
        Lists all packet capture requests for an account.

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
            f"/accounts/{account_identifier}/pcaps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PcapMagicPcapCollectionListPacketCaptureRequestsResponse]],
                ResultWrapper[PcapMagicPcapCollectionListPacketCaptureRequestsResponse],
            ),
        )


class AsyncPcaps(AsyncAPIResource):
    @cached_property
    def ownerships(self) -> AsyncOwnerships:
        return AsyncOwnerships(self._client)

    @cached_property
    def downloads(self) -> AsyncDownloads:
        return AsyncDownloads(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPcapsWithRawResponse:
        return AsyncPcapsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPcapsWithStreamingResponse:
        return AsyncPcapsWithStreamingResponse(self)

    async def get(
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
    ) -> PcapGetResponse:
        """
        Get information for a PCAP request by id.

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
        return cast(
            PcapGetResponse,
            await self._get(
                f"/accounts/{account_identifier}/pcaps/{identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PcapGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def magic_pcap_collection_create_pcap_request(
        self,
        account_identifier: str,
        *,
        packet_limit: float,
        system: Literal["magic-transit"],
        time_limit: float,
        type: Literal["simple", "full"],
        filter_v1: pcap_magic_pcap_collection_create_pcap_request_params._6wtRj17BPcapsRequestSimpleFilterV1
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PcapMagicPcapCollectionCreatePcapRequestResponse:
        """
        Create new PCAP request for account.

        Args:
          account_identifier: Identifier

          packet_limit: The limit of packets contained in a packet capture.

          system: The system used to collect packet captures.

          time_limit: The packet capture duration in seconds.

          type: The type of packet capture. `Simple` captures sampled packets, and `full`
              captures entire payloads and non-sampled packets.

          filter_v1: The packet capture filter. When this field is empty, all packets are captured.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def magic_pcap_collection_create_pcap_request(
        self,
        account_identifier: str,
        *,
        colo_name: str,
        destination_conf: str,
        system: Literal["magic-transit"],
        time_limit: float,
        type: Literal["simple", "full"],
        byte_limit: float | NotGiven = NOT_GIVEN,
        filter_v1: pcap_magic_pcap_collection_create_pcap_request_params._6wtRj17BPcapsRequestFullFilterV1
        | NotGiven = NOT_GIVEN,
        packet_limit: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PcapMagicPcapCollectionCreatePcapRequestResponse:
        """
        Create new PCAP request for account.

        Args:
          account_identifier: Identifier

          colo_name: The name of the data center used for the packet capture. This can be a specific
              colo (ord02) or a multi-colo name (ORD). This field only applies to `full`
              packet captures.

          destination_conf: The full URI for the bucket. This field only applies to `full` packet captures.

          system: The system used to collect packet captures.

          time_limit: The packet capture duration in seconds.

          type: The type of packet capture. `Simple` captures sampled packets, and `full`
              captures entire payloads and non-sampled packets.

          byte_limit: The maximum number of bytes to capture. This field only applies to `full` packet
              captures.

          filter_v1: The packet capture filter. When this field is empty, all packets are captured.

          packet_limit: The limit of packets contained in a packet capture.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["packet_limit", "system", "time_limit", "type"],
        ["colo_name", "destination_conf", "system", "time_limit", "type"],
    )
    async def magic_pcap_collection_create_pcap_request(
        self,
        account_identifier: str,
        *,
        packet_limit: float | NotGiven = NOT_GIVEN,
        system: Literal["magic-transit"],
        time_limit: float,
        type: Literal["simple", "full"],
        filter_v1: pcap_magic_pcap_collection_create_pcap_request_params._6wtRj17BPcapsRequestSimpleFilterV1
        | NotGiven = NOT_GIVEN,
        colo_name: str | NotGiven = NOT_GIVEN,
        destination_conf: str | NotGiven = NOT_GIVEN,
        byte_limit: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PcapMagicPcapCollectionCreatePcapRequestResponse:
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return cast(
            PcapMagicPcapCollectionCreatePcapRequestResponse,
            await self._post(
                f"/accounts/{account_identifier}/pcaps",
                body=maybe_transform(
                    {
                        "packet_limit": packet_limit,
                        "system": system,
                        "time_limit": time_limit,
                        "type": type,
                        "filter_v1": filter_v1,
                        "colo_name": colo_name,
                        "destination_conf": destination_conf,
                        "byte_limit": byte_limit,
                    },
                    pcap_magic_pcap_collection_create_pcap_request_params.PcapMagicPcapCollectionCreatePcapRequestParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PcapMagicPcapCollectionCreatePcapRequestResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def magic_pcap_collection_list_packet_capture_requests(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PcapMagicPcapCollectionListPacketCaptureRequestsResponse]:
        """
        Lists all packet capture requests for an account.

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
            f"/accounts/{account_identifier}/pcaps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PcapMagicPcapCollectionListPacketCaptureRequestsResponse]],
                ResultWrapper[PcapMagicPcapCollectionListPacketCaptureRequestsResponse],
            ),
        )


class PcapsWithRawResponse:
    def __init__(self, pcaps: Pcaps) -> None:
        self._pcaps = pcaps

        self.get = to_raw_response_wrapper(
            pcaps.get,
        )
        self.magic_pcap_collection_create_pcap_request = to_raw_response_wrapper(
            pcaps.magic_pcap_collection_create_pcap_request,
        )
        self.magic_pcap_collection_list_packet_capture_requests = to_raw_response_wrapper(
            pcaps.magic_pcap_collection_list_packet_capture_requests,
        )

    @cached_property
    def ownerships(self) -> OwnershipsWithRawResponse:
        return OwnershipsWithRawResponse(self._pcaps.ownerships)

    @cached_property
    def downloads(self) -> DownloadsWithRawResponse:
        return DownloadsWithRawResponse(self._pcaps.downloads)


class AsyncPcapsWithRawResponse:
    def __init__(self, pcaps: AsyncPcaps) -> None:
        self._pcaps = pcaps

        self.get = async_to_raw_response_wrapper(
            pcaps.get,
        )
        self.magic_pcap_collection_create_pcap_request = async_to_raw_response_wrapper(
            pcaps.magic_pcap_collection_create_pcap_request,
        )
        self.magic_pcap_collection_list_packet_capture_requests = async_to_raw_response_wrapper(
            pcaps.magic_pcap_collection_list_packet_capture_requests,
        )

    @cached_property
    def ownerships(self) -> AsyncOwnershipsWithRawResponse:
        return AsyncOwnershipsWithRawResponse(self._pcaps.ownerships)

    @cached_property
    def downloads(self) -> AsyncDownloadsWithRawResponse:
        return AsyncDownloadsWithRawResponse(self._pcaps.downloads)


class PcapsWithStreamingResponse:
    def __init__(self, pcaps: Pcaps) -> None:
        self._pcaps = pcaps

        self.get = to_streamed_response_wrapper(
            pcaps.get,
        )
        self.magic_pcap_collection_create_pcap_request = to_streamed_response_wrapper(
            pcaps.magic_pcap_collection_create_pcap_request,
        )
        self.magic_pcap_collection_list_packet_capture_requests = to_streamed_response_wrapper(
            pcaps.magic_pcap_collection_list_packet_capture_requests,
        )

    @cached_property
    def ownerships(self) -> OwnershipsWithStreamingResponse:
        return OwnershipsWithStreamingResponse(self._pcaps.ownerships)

    @cached_property
    def downloads(self) -> DownloadsWithStreamingResponse:
        return DownloadsWithStreamingResponse(self._pcaps.downloads)


class AsyncPcapsWithStreamingResponse:
    def __init__(self, pcaps: AsyncPcaps) -> None:
        self._pcaps = pcaps

        self.get = async_to_streamed_response_wrapper(
            pcaps.get,
        )
        self.magic_pcap_collection_create_pcap_request = async_to_streamed_response_wrapper(
            pcaps.magic_pcap_collection_create_pcap_request,
        )
        self.magic_pcap_collection_list_packet_capture_requests = async_to_streamed_response_wrapper(
            pcaps.magic_pcap_collection_list_packet_capture_requests,
        )

    @cached_property
    def ownerships(self) -> AsyncOwnershipsWithStreamingResponse:
        return AsyncOwnershipsWithStreamingResponse(self._pcaps.ownerships)

    @cached_property
    def downloads(self) -> AsyncDownloadsWithStreamingResponse:
        return AsyncDownloadsWithStreamingResponse(self._pcaps.downloads)
