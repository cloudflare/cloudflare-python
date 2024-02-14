# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import TrueClientIPHeaderUpdateResponse, TrueClientIPHeaderGetResponse

from typing import Type, Optional

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.settings import true_client_ip_header_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["TrueClientIPHeader", "AsyncTrueClientIPHeader"]


class TrueClientIPHeader(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrueClientIPHeaderWithRawResponse:
        return TrueClientIPHeaderWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrueClientIPHeaderWithStreamingResponse:
        return TrueClientIPHeaderWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TrueClientIPHeaderUpdateResponse]:
        """
        Allows customer to continue to use True Client IP (Akamai feature) in the
        headers we send to the origin. This is limited to Enterprise Zones.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/true_client_ip_header",
            body=maybe_transform({"value": value}, true_client_ip_header_update_params.TrueClientIPHeaderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TrueClientIPHeaderUpdateResponse]], ResultWrapper[TrueClientIPHeaderUpdateResponse]
            ),
        )

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TrueClientIPHeaderGetResponse]:
        """
        Allows customer to continue to use True Client IP (Akamai feature) in the
        headers we send to the origin. This is limited to Enterprise Zones.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/true_client_ip_header",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TrueClientIPHeaderGetResponse]], ResultWrapper[TrueClientIPHeaderGetResponse]),
        )


class AsyncTrueClientIPHeader(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrueClientIPHeaderWithRawResponse:
        return AsyncTrueClientIPHeaderWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrueClientIPHeaderWithStreamingResponse:
        return AsyncTrueClientIPHeaderWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TrueClientIPHeaderUpdateResponse]:
        """
        Allows customer to continue to use True Client IP (Akamai feature) in the
        headers we send to the origin. This is limited to Enterprise Zones.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/true_client_ip_header",
            body=maybe_transform({"value": value}, true_client_ip_header_update_params.TrueClientIPHeaderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TrueClientIPHeaderUpdateResponse]], ResultWrapper[TrueClientIPHeaderUpdateResponse]
            ),
        )

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TrueClientIPHeaderGetResponse]:
        """
        Allows customer to continue to use True Client IP (Akamai feature) in the
        headers we send to the origin. This is limited to Enterprise Zones.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/true_client_ip_header",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TrueClientIPHeaderGetResponse]], ResultWrapper[TrueClientIPHeaderGetResponse]),
        )


class TrueClientIPHeaderWithRawResponse:
    def __init__(self, true_client_ip_header: TrueClientIPHeader) -> None:
        self._true_client_ip_header = true_client_ip_header

        self.update = to_raw_response_wrapper(
            true_client_ip_header.update,
        )
        self.get = to_raw_response_wrapper(
            true_client_ip_header.get,
        )


class AsyncTrueClientIPHeaderWithRawResponse:
    def __init__(self, true_client_ip_header: AsyncTrueClientIPHeader) -> None:
        self._true_client_ip_header = true_client_ip_header

        self.update = async_to_raw_response_wrapper(
            true_client_ip_header.update,
        )
        self.get = async_to_raw_response_wrapper(
            true_client_ip_header.get,
        )


class TrueClientIPHeaderWithStreamingResponse:
    def __init__(self, true_client_ip_header: TrueClientIPHeader) -> None:
        self._true_client_ip_header = true_client_ip_header

        self.update = to_streamed_response_wrapper(
            true_client_ip_header.update,
        )
        self.get = to_streamed_response_wrapper(
            true_client_ip_header.get,
        )


class AsyncTrueClientIPHeaderWithStreamingResponse:
    def __init__(self, true_client_ip_header: AsyncTrueClientIPHeader) -> None:
        self._true_client_ip_header = true_client_ip_header

        self.update = async_to_streamed_response_wrapper(
            true_client_ip_header.update,
        )
        self.get = async_to_streamed_response_wrapper(
            true_client_ip_header.get,
        )
