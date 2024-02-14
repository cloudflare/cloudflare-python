# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import HTTP3UpdateResponse, HTTP3GetResponse

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
from ...types.settings import http3_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["HTTP3", "AsyncHTTP3"]


class HTTP3(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HTTP3WithRawResponse:
        return HTTP3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HTTP3WithStreamingResponse:
        return HTTP3WithStreamingResponse(self)

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
    ) -> Optional[HTTP3UpdateResponse]:
        """
        Value of the HTTP3 setting.

        Args:
          zone_id: Identifier

          value: Value of the HTTP3 setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/http3",
            body=maybe_transform({"value": value}, http3_update_params.HTTP3UpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTP3UpdateResponse]], ResultWrapper[HTTP3UpdateResponse]),
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
    ) -> Optional[HTTP3GetResponse]:
        """
        Value of the HTTP3 setting.

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
            f"/zones/{zone_id}/settings/http3",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTP3GetResponse]], ResultWrapper[HTTP3GetResponse]),
        )


class AsyncHTTP3(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHTTP3WithRawResponse:
        return AsyncHTTP3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHTTP3WithStreamingResponse:
        return AsyncHTTP3WithStreamingResponse(self)

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
    ) -> Optional[HTTP3UpdateResponse]:
        """
        Value of the HTTP3 setting.

        Args:
          zone_id: Identifier

          value: Value of the HTTP3 setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/http3",
            body=maybe_transform({"value": value}, http3_update_params.HTTP3UpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTP3UpdateResponse]], ResultWrapper[HTTP3UpdateResponse]),
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
    ) -> Optional[HTTP3GetResponse]:
        """
        Value of the HTTP3 setting.

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
            f"/zones/{zone_id}/settings/http3",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTP3GetResponse]], ResultWrapper[HTTP3GetResponse]),
        )


class HTTP3WithRawResponse:
    def __init__(self, http3: HTTP3) -> None:
        self._http3 = http3

        self.update = to_raw_response_wrapper(
            http3.update,
        )
        self.get = to_raw_response_wrapper(
            http3.get,
        )


class AsyncHTTP3WithRawResponse:
    def __init__(self, http3: AsyncHTTP3) -> None:
        self._http3 = http3

        self.update = async_to_raw_response_wrapper(
            http3.update,
        )
        self.get = async_to_raw_response_wrapper(
            http3.get,
        )


class HTTP3WithStreamingResponse:
    def __init__(self, http3: HTTP3) -> None:
        self._http3 = http3

        self.update = to_streamed_response_wrapper(
            http3.update,
        )
        self.get = to_streamed_response_wrapper(
            http3.get,
        )


class AsyncHTTP3WithStreamingResponse:
    def __init__(self, http3: AsyncHTTP3) -> None:
        self._http3 = http3

        self.update = async_to_streamed_response_wrapper(
            http3.update,
        )
        self.get = async_to_streamed_response_wrapper(
            http3.get,
        )
