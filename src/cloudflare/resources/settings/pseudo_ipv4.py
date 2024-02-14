# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import PseudoIPV4UpdateResponse, PseudoIPV4GetResponse

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
from ...types.settings import pseudo_ipv4_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["PseudoIPV4", "AsyncPseudoIPV4"]


class PseudoIPV4(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PseudoIPV4WithRawResponse:
        return PseudoIPV4WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PseudoIPV4WithStreamingResponse:
        return PseudoIPV4WithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal["off", "add_header", "overwrite_header"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PseudoIPV4UpdateResponse]:
        """
        Value of the Pseudo IPv4 setting.

        Args:
          zone_id: Identifier

          value: Value of the Pseudo IPv4 setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/pseudo_ipv4",
            body=maybe_transform({"value": value}, pseudo_ipv4_update_params.PseudoIPV4UpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PseudoIPV4UpdateResponse]], ResultWrapper[PseudoIPV4UpdateResponse]),
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
    ) -> Optional[PseudoIPV4GetResponse]:
        """
        Value of the Pseudo IPv4 setting.

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
            f"/zones/{zone_id}/settings/pseudo_ipv4",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PseudoIPV4GetResponse]], ResultWrapper[PseudoIPV4GetResponse]),
        )


class AsyncPseudoIPV4(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPseudoIPV4WithRawResponse:
        return AsyncPseudoIPV4WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPseudoIPV4WithStreamingResponse:
        return AsyncPseudoIPV4WithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal["off", "add_header", "overwrite_header"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PseudoIPV4UpdateResponse]:
        """
        Value of the Pseudo IPv4 setting.

        Args:
          zone_id: Identifier

          value: Value of the Pseudo IPv4 setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/pseudo_ipv4",
            body=maybe_transform({"value": value}, pseudo_ipv4_update_params.PseudoIPV4UpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PseudoIPV4UpdateResponse]], ResultWrapper[PseudoIPV4UpdateResponse]),
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
    ) -> Optional[PseudoIPV4GetResponse]:
        """
        Value of the Pseudo IPv4 setting.

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
            f"/zones/{zone_id}/settings/pseudo_ipv4",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PseudoIPV4GetResponse]], ResultWrapper[PseudoIPV4GetResponse]),
        )


class PseudoIPV4WithRawResponse:
    def __init__(self, pseudo_ipv4: PseudoIPV4) -> None:
        self._pseudo_ipv4 = pseudo_ipv4

        self.update = to_raw_response_wrapper(
            pseudo_ipv4.update,
        )
        self.get = to_raw_response_wrapper(
            pseudo_ipv4.get,
        )


class AsyncPseudoIPV4WithRawResponse:
    def __init__(self, pseudo_ipv4: AsyncPseudoIPV4) -> None:
        self._pseudo_ipv4 = pseudo_ipv4

        self.update = async_to_raw_response_wrapper(
            pseudo_ipv4.update,
        )
        self.get = async_to_raw_response_wrapper(
            pseudo_ipv4.get,
        )


class PseudoIPV4WithStreamingResponse:
    def __init__(self, pseudo_ipv4: PseudoIPV4) -> None:
        self._pseudo_ipv4 = pseudo_ipv4

        self.update = to_streamed_response_wrapper(
            pseudo_ipv4.update,
        )
        self.get = to_streamed_response_wrapper(
            pseudo_ipv4.get,
        )


class AsyncPseudoIPV4WithStreamingResponse:
    def __init__(self, pseudo_ipv4: AsyncPseudoIPV4) -> None:
        self._pseudo_ipv4 = pseudo_ipv4

        self.update = async_to_streamed_response_wrapper(
            pseudo_ipv4.update,
        )
        self.get = async_to_streamed_response_wrapper(
            pseudo_ipv4.get,
        )
