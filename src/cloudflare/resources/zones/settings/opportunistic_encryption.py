# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

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
from ....types.zones.settings import ZonesOpportunisticEncryption, opportunistic_encryption_edit_params

__all__ = ["OpportunisticEncryption", "AsyncOpportunisticEncryption"]


class OpportunisticEncryption(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OpportunisticEncryptionWithRawResponse:
        return OpportunisticEncryptionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpportunisticEncryptionWithStreamingResponse:
        return OpportunisticEncryptionWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesOpportunisticEncryption]:
        """
        Changes Opportunistic Encryption setting.

        Args:
          zone_id: Identifier

          value: Value of the zone setting. Notes: Default value depends on the zone's plan
              level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/opportunistic_encryption",
            body=maybe_transform(
                {"value": value}, opportunistic_encryption_edit_params.OpportunisticEncryptionEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesOpportunisticEncryption]], ResultWrapper[ZonesOpportunisticEncryption]),
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
    ) -> Optional[ZonesOpportunisticEncryption]:
        """
        Gets Opportunistic Encryption setting.

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
            f"/zones/{zone_id}/settings/opportunistic_encryption",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesOpportunisticEncryption]], ResultWrapper[ZonesOpportunisticEncryption]),
        )


class AsyncOpportunisticEncryption(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOpportunisticEncryptionWithRawResponse:
        return AsyncOpportunisticEncryptionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpportunisticEncryptionWithStreamingResponse:
        return AsyncOpportunisticEncryptionWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesOpportunisticEncryption]:
        """
        Changes Opportunistic Encryption setting.

        Args:
          zone_id: Identifier

          value: Value of the zone setting. Notes: Default value depends on the zone's plan
              level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/opportunistic_encryption",
            body=await async_maybe_transform(
                {"value": value}, opportunistic_encryption_edit_params.OpportunisticEncryptionEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesOpportunisticEncryption]], ResultWrapper[ZonesOpportunisticEncryption]),
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
    ) -> Optional[ZonesOpportunisticEncryption]:
        """
        Gets Opportunistic Encryption setting.

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
            f"/zones/{zone_id}/settings/opportunistic_encryption",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesOpportunisticEncryption]], ResultWrapper[ZonesOpportunisticEncryption]),
        )


class OpportunisticEncryptionWithRawResponse:
    def __init__(self, opportunistic_encryption: OpportunisticEncryption) -> None:
        self._opportunistic_encryption = opportunistic_encryption

        self.edit = to_raw_response_wrapper(
            opportunistic_encryption.edit,
        )
        self.get = to_raw_response_wrapper(
            opportunistic_encryption.get,
        )


class AsyncOpportunisticEncryptionWithRawResponse:
    def __init__(self, opportunistic_encryption: AsyncOpportunisticEncryption) -> None:
        self._opportunistic_encryption = opportunistic_encryption

        self.edit = async_to_raw_response_wrapper(
            opportunistic_encryption.edit,
        )
        self.get = async_to_raw_response_wrapper(
            opportunistic_encryption.get,
        )


class OpportunisticEncryptionWithStreamingResponse:
    def __init__(self, opportunistic_encryption: OpportunisticEncryption) -> None:
        self._opportunistic_encryption = opportunistic_encryption

        self.edit = to_streamed_response_wrapper(
            opportunistic_encryption.edit,
        )
        self.get = to_streamed_response_wrapper(
            opportunistic_encryption.get,
        )


class AsyncOpportunisticEncryptionWithStreamingResponse:
    def __init__(self, opportunistic_encryption: AsyncOpportunisticEncryption) -> None:
        self._opportunistic_encryption = opportunistic_encryption

        self.edit = async_to_streamed_response_wrapper(
            opportunistic_encryption.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            opportunistic_encryption.get,
        )
