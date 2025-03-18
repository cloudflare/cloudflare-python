# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from .download import (
    DownloadResource,
    AsyncDownloadResource,
    DownloadResourceWithRawResponse,
    AsyncDownloadResourceWithRawResponse,
    DownloadResourceWithStreamingResponse,
    AsyncDownloadResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from .ownership import (
    OwnershipResource,
    AsyncOwnershipResource,
    OwnershipResourceWithRawResponse,
    AsyncOwnershipResourceWithRawResponse,
    OwnershipResourceWithStreamingResponse,
    AsyncOwnershipResourceWithStreamingResponse,
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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.magic_transit import pcap_create_params
from ....types.magic_transit.pcap_filter_param import PCAPFilterParam
from ....types.magic_transit.pcap_get_response import PCAPGetResponse
from ....types.magic_transit.pcap_list_response import PCAPListResponse
from ....types.magic_transit.pcap_create_response import PCAPCreateResponse

__all__ = ["PCAPsResource", "AsyncPCAPsResource"]


class PCAPsResource(SyncAPIResource):
    @cached_property
    def ownership(self) -> OwnershipResource:
        return OwnershipResource(self._client)

    @cached_property
    def download(self) -> DownloadResource:
        return DownloadResource(self._client)

    @cached_property
    def with_raw_response(self) -> PCAPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PCAPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PCAPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PCAPsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        account_id: str,
        packet_limit: float,
        system: Literal["magic-transit"],
        time_limit: float,
        type: Literal["simple", "full"],
        filter_v1: PCAPFilterParam | NotGiven = NOT_GIVEN,
        offset_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PCAPCreateResponse:
        """
        Create new PCAP request for account.

        Args:
          account_id: Identifier

          packet_limit: The limit of packets contained in a packet capture.

          system: The system used to collect packet captures.

          time_limit: The packet capture duration in seconds.

          type: The type of packet capture. `Simple` captures sampled packets, and `full`
              captures entire payloads and non-sampled packets.

          filter_v1: The packet capture filter. When this field is empty, all packets are captured.

          offset_time: The RFC 3339 offset timestamp from which to query backwards for packets. Must be
              within the last 24h. When this field is empty, defaults to time of request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        account_id: str,
        colo_name: str,
        destination_conf: str,
        system: Literal["magic-transit"],
        time_limit: float,
        type: Literal["simple", "full"],
        byte_limit: float | NotGiven = NOT_GIVEN,
        filter_v1: PCAPFilterParam | NotGiven = NOT_GIVEN,
        packet_limit: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PCAPCreateResponse:
        """
        Create new PCAP request for account.

        Args:
          account_id: Identifier

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
        ["account_id", "packet_limit", "system", "time_limit", "type"],
        ["account_id", "colo_name", "destination_conf", "system", "time_limit", "type"],
    )
    def create(
        self,
        *,
        account_id: str,
        packet_limit: float | NotGiven = NOT_GIVEN,
        system: Literal["magic-transit"],
        time_limit: float,
        type: Literal["simple", "full"],
        filter_v1: PCAPFilterParam | NotGiven = NOT_GIVEN,
        offset_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        colo_name: str | NotGiven = NOT_GIVEN,
        destination_conf: str | NotGiven = NOT_GIVEN,
        byte_limit: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PCAPCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            PCAPCreateResponse,
            self._post(
                f"/accounts/{account_id}/pcaps",
                body=maybe_transform(
                    {
                        "packet_limit": packet_limit,
                        "system": system,
                        "time_limit": time_limit,
                        "type": type,
                        "filter_v1": filter_v1,
                        "offset_time": offset_time,
                        "colo_name": colo_name,
                        "destination_conf": destination_conf,
                        "byte_limit": byte_limit,
                    },
                    pcap_create_params.PCAPCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[PCAPCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PCAPCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[PCAPListResponse]:
        """
        Lists all packet capture requests for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/pcaps",
            page=SyncSinglePage[PCAPListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, PCAPListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    def get(
        self,
        pcap_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PCAPGetResponse:
        """
        Get information for a PCAP request by id.

        Args:
          account_id: Identifier

          pcap_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pcap_id:
            raise ValueError(f"Expected a non-empty value for `pcap_id` but received {pcap_id!r}")
        return cast(
            PCAPGetResponse,
            self._get(
                f"/accounts/{account_id}/pcaps/{pcap_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[PCAPGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PCAPGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncPCAPsResource(AsyncAPIResource):
    @cached_property
    def ownership(self) -> AsyncOwnershipResource:
        return AsyncOwnershipResource(self._client)

    @cached_property
    def download(self) -> AsyncDownloadResource:
        return AsyncDownloadResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPCAPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPCAPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPCAPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPCAPsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        account_id: str,
        packet_limit: float,
        system: Literal["magic-transit"],
        time_limit: float,
        type: Literal["simple", "full"],
        filter_v1: PCAPFilterParam | NotGiven = NOT_GIVEN,
        offset_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PCAPCreateResponse:
        """
        Create new PCAP request for account.

        Args:
          account_id: Identifier

          packet_limit: The limit of packets contained in a packet capture.

          system: The system used to collect packet captures.

          time_limit: The packet capture duration in seconds.

          type: The type of packet capture. `Simple` captures sampled packets, and `full`
              captures entire payloads and non-sampled packets.

          filter_v1: The packet capture filter. When this field is empty, all packets are captured.

          offset_time: The RFC 3339 offset timestamp from which to query backwards for packets. Must be
              within the last 24h. When this field is empty, defaults to time of request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        account_id: str,
        colo_name: str,
        destination_conf: str,
        system: Literal["magic-transit"],
        time_limit: float,
        type: Literal["simple", "full"],
        byte_limit: float | NotGiven = NOT_GIVEN,
        filter_v1: PCAPFilterParam | NotGiven = NOT_GIVEN,
        packet_limit: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PCAPCreateResponse:
        """
        Create new PCAP request for account.

        Args:
          account_id: Identifier

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
        ["account_id", "packet_limit", "system", "time_limit", "type"],
        ["account_id", "colo_name", "destination_conf", "system", "time_limit", "type"],
    )
    async def create(
        self,
        *,
        account_id: str,
        packet_limit: float | NotGiven = NOT_GIVEN,
        system: Literal["magic-transit"],
        time_limit: float,
        type: Literal["simple", "full"],
        filter_v1: PCAPFilterParam | NotGiven = NOT_GIVEN,
        offset_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        colo_name: str | NotGiven = NOT_GIVEN,
        destination_conf: str | NotGiven = NOT_GIVEN,
        byte_limit: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PCAPCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            PCAPCreateResponse,
            await self._post(
                f"/accounts/{account_id}/pcaps",
                body=await async_maybe_transform(
                    {
                        "packet_limit": packet_limit,
                        "system": system,
                        "time_limit": time_limit,
                        "type": type,
                        "filter_v1": filter_v1,
                        "offset_time": offset_time,
                        "colo_name": colo_name,
                        "destination_conf": destination_conf,
                        "byte_limit": byte_limit,
                    },
                    pcap_create_params.PCAPCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[PCAPCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PCAPCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PCAPListResponse, AsyncSinglePage[PCAPListResponse]]:
        """
        Lists all packet capture requests for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/pcaps",
            page=AsyncSinglePage[PCAPListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, PCAPListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    async def get(
        self,
        pcap_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PCAPGetResponse:
        """
        Get information for a PCAP request by id.

        Args:
          account_id: Identifier

          pcap_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pcap_id:
            raise ValueError(f"Expected a non-empty value for `pcap_id` but received {pcap_id!r}")
        return cast(
            PCAPGetResponse,
            await self._get(
                f"/accounts/{account_id}/pcaps/{pcap_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[PCAPGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PCAPGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class PCAPsResourceWithRawResponse:
    def __init__(self, pcaps: PCAPsResource) -> None:
        self._pcaps = pcaps

        self.create = to_raw_response_wrapper(
            pcaps.create,
        )
        self.list = to_raw_response_wrapper(
            pcaps.list,
        )
        self.get = to_raw_response_wrapper(
            pcaps.get,
        )

    @cached_property
    def ownership(self) -> OwnershipResourceWithRawResponse:
        return OwnershipResourceWithRawResponse(self._pcaps.ownership)

    @cached_property
    def download(self) -> DownloadResourceWithRawResponse:
        return DownloadResourceWithRawResponse(self._pcaps.download)


class AsyncPCAPsResourceWithRawResponse:
    def __init__(self, pcaps: AsyncPCAPsResource) -> None:
        self._pcaps = pcaps

        self.create = async_to_raw_response_wrapper(
            pcaps.create,
        )
        self.list = async_to_raw_response_wrapper(
            pcaps.list,
        )
        self.get = async_to_raw_response_wrapper(
            pcaps.get,
        )

    @cached_property
    def ownership(self) -> AsyncOwnershipResourceWithRawResponse:
        return AsyncOwnershipResourceWithRawResponse(self._pcaps.ownership)

    @cached_property
    def download(self) -> AsyncDownloadResourceWithRawResponse:
        return AsyncDownloadResourceWithRawResponse(self._pcaps.download)


class PCAPsResourceWithStreamingResponse:
    def __init__(self, pcaps: PCAPsResource) -> None:
        self._pcaps = pcaps

        self.create = to_streamed_response_wrapper(
            pcaps.create,
        )
        self.list = to_streamed_response_wrapper(
            pcaps.list,
        )
        self.get = to_streamed_response_wrapper(
            pcaps.get,
        )

    @cached_property
    def ownership(self) -> OwnershipResourceWithStreamingResponse:
        return OwnershipResourceWithStreamingResponse(self._pcaps.ownership)

    @cached_property
    def download(self) -> DownloadResourceWithStreamingResponse:
        return DownloadResourceWithStreamingResponse(self._pcaps.download)


class AsyncPCAPsResourceWithStreamingResponse:
    def __init__(self, pcaps: AsyncPCAPsResource) -> None:
        self._pcaps = pcaps

        self.create = async_to_streamed_response_wrapper(
            pcaps.create,
        )
        self.list = async_to_streamed_response_wrapper(
            pcaps.list,
        )
        self.get = async_to_streamed_response_wrapper(
            pcaps.get,
        )

    @cached_property
    def ownership(self) -> AsyncOwnershipResourceWithStreamingResponse:
        return AsyncOwnershipResourceWithStreamingResponse(self._pcaps.ownership)

    @cached_property
    def download(self) -> AsyncDownloadResourceWithStreamingResponse:
        return AsyncDownloadResourceWithStreamingResponse(self._pcaps.download)
