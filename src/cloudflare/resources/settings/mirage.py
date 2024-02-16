# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import MirageUpdateResponse, MirageGetResponse

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
from ...types.settings import mirage_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Mirage", "AsyncMirage"]


class Mirage(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MirageWithRawResponse:
        return MirageWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MirageWithStreamingResponse:
        return MirageWithStreamingResponse(self)

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
    ) -> Optional[MirageUpdateResponse]:
        """
        Automatically optimize image loading for website visitors on mobile devices.
        Refer to our
        [blog post](http://blog.cloudflare.com/mirage2-solving-mobile-speed) for more
        information.

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
            f"/zones/{zone_id}/settings/mirage",
            body=maybe_transform({"value": value}, mirage_update_params.MirageUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[MirageUpdateResponse]], ResultWrapper[MirageUpdateResponse]),
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
    ) -> Optional[MirageGetResponse]:
        """
        Automatically optimize image loading for website visitors on mobile devices.
        Refer to our
        [blog post](http://blog.cloudflare.com/mirage2-solving-mobile-speed) for more
        information.

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
            f"/zones/{zone_id}/settings/mirage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[MirageGetResponse]], ResultWrapper[MirageGetResponse]),
        )


class AsyncMirage(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMirageWithRawResponse:
        return AsyncMirageWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMirageWithStreamingResponse:
        return AsyncMirageWithStreamingResponse(self)

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
    ) -> Optional[MirageUpdateResponse]:
        """
        Automatically optimize image loading for website visitors on mobile devices.
        Refer to our
        [blog post](http://blog.cloudflare.com/mirage2-solving-mobile-speed) for more
        information.

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
            f"/zones/{zone_id}/settings/mirage",
            body=maybe_transform({"value": value}, mirage_update_params.MirageUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[MirageUpdateResponse]], ResultWrapper[MirageUpdateResponse]),
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
    ) -> Optional[MirageGetResponse]:
        """
        Automatically optimize image loading for website visitors on mobile devices.
        Refer to our
        [blog post](http://blog.cloudflare.com/mirage2-solving-mobile-speed) for more
        information.

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
            f"/zones/{zone_id}/settings/mirage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[MirageGetResponse]], ResultWrapper[MirageGetResponse]),
        )


class MirageWithRawResponse:
    def __init__(self, mirage: Mirage) -> None:
        self._mirage = mirage

        self.update = to_raw_response_wrapper(
            mirage.update,
        )
        self.get = to_raw_response_wrapper(
            mirage.get,
        )


class AsyncMirageWithRawResponse:
    def __init__(self, mirage: AsyncMirage) -> None:
        self._mirage = mirage

        self.update = async_to_raw_response_wrapper(
            mirage.update,
        )
        self.get = async_to_raw_response_wrapper(
            mirage.get,
        )


class MirageWithStreamingResponse:
    def __init__(self, mirage: Mirage) -> None:
        self._mirage = mirage

        self.update = to_streamed_response_wrapper(
            mirage.update,
        )
        self.get = to_streamed_response_wrapper(
            mirage.get,
        )


class AsyncMirageWithStreamingResponse:
    def __init__(self, mirage: AsyncMirage) -> None:
        self._mirage = mirage

        self.update = async_to_streamed_response_wrapper(
            mirage.update,
        )
        self.get = async_to_streamed_response_wrapper(
            mirage.get,
        )
