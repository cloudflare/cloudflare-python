# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
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
from ....types.zones.settings import ZonesCiphers, cipher_edit_params

__all__ = ["Ciphers", "AsyncCiphers"]


class Ciphers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CiphersWithRawResponse:
        return CiphersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CiphersWithStreamingResponse:
        return CiphersWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesCiphers]:
        """
        Changes ciphers setting.

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
            f"/zones/{zone_id}/settings/ciphers",
            body=maybe_transform({"value": value}, cipher_edit_params.CipherEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesCiphers]], ResultWrapper[ZonesCiphers]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesCiphers]:
        """
        Gets ciphers setting.

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
            f"/zones/{zone_id}/settings/ciphers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesCiphers]], ResultWrapper[ZonesCiphers]),
        )


class AsyncCiphers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCiphersWithRawResponse:
        return AsyncCiphersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCiphersWithStreamingResponse:
        return AsyncCiphersWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesCiphers]:
        """
        Changes ciphers setting.

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
            f"/zones/{zone_id}/settings/ciphers",
            body=await async_maybe_transform({"value": value}, cipher_edit_params.CipherEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesCiphers]], ResultWrapper[ZonesCiphers]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesCiphers]:
        """
        Gets ciphers setting.

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
            f"/zones/{zone_id}/settings/ciphers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesCiphers]], ResultWrapper[ZonesCiphers]),
        )


class CiphersWithRawResponse:
    def __init__(self, ciphers: Ciphers) -> None:
        self._ciphers = ciphers

        self.edit = to_raw_response_wrapper(
            ciphers.edit,
        )
        self.get = to_raw_response_wrapper(
            ciphers.get,
        )


class AsyncCiphersWithRawResponse:
    def __init__(self, ciphers: AsyncCiphers) -> None:
        self._ciphers = ciphers

        self.edit = async_to_raw_response_wrapper(
            ciphers.edit,
        )
        self.get = async_to_raw_response_wrapper(
            ciphers.get,
        )


class CiphersWithStreamingResponse:
    def __init__(self, ciphers: Ciphers) -> None:
        self._ciphers = ciphers

        self.edit = to_streamed_response_wrapper(
            ciphers.edit,
        )
        self.get = to_streamed_response_wrapper(
            ciphers.get,
        )


class AsyncCiphersWithStreamingResponse:
    def __init__(self, ciphers: AsyncCiphers) -> None:
        self._ciphers = ciphers

        self.edit = async_to_streamed_response_wrapper(
            ciphers.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            ciphers.get,
        )
