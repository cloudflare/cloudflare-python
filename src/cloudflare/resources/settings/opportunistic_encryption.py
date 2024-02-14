# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import OpportunisticEncryptionUpdateResponse, OpportunisticEncryptionGetResponse

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
from ...types.settings import opportunistic_encryption_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["OpportunisticEncryption", "AsyncOpportunisticEncryption"]


class OpportunisticEncryption(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OpportunisticEncryptionWithRawResponse:
        return OpportunisticEncryptionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpportunisticEncryptionWithStreamingResponse:
        return OpportunisticEncryptionWithStreamingResponse(self)

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
    ) -> Optional[OpportunisticEncryptionUpdateResponse]:
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
                {"value": value}, opportunistic_encryption_update_params.OpportunisticEncryptionUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OpportunisticEncryptionUpdateResponse]],
                ResultWrapper[OpportunisticEncryptionUpdateResponse],
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
    ) -> Optional[OpportunisticEncryptionGetResponse]:
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
            cast_to=cast(
                Type[Optional[OpportunisticEncryptionGetResponse]], ResultWrapper[OpportunisticEncryptionGetResponse]
            ),
        )


class AsyncOpportunisticEncryption(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOpportunisticEncryptionWithRawResponse:
        return AsyncOpportunisticEncryptionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpportunisticEncryptionWithStreamingResponse:
        return AsyncOpportunisticEncryptionWithStreamingResponse(self)

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
    ) -> Optional[OpportunisticEncryptionUpdateResponse]:
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
            body=maybe_transform(
                {"value": value}, opportunistic_encryption_update_params.OpportunisticEncryptionUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OpportunisticEncryptionUpdateResponse]],
                ResultWrapper[OpportunisticEncryptionUpdateResponse],
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
    ) -> Optional[OpportunisticEncryptionGetResponse]:
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
            cast_to=cast(
                Type[Optional[OpportunisticEncryptionGetResponse]], ResultWrapper[OpportunisticEncryptionGetResponse]
            ),
        )


class OpportunisticEncryptionWithRawResponse:
    def __init__(self, opportunistic_encryption: OpportunisticEncryption) -> None:
        self._opportunistic_encryption = opportunistic_encryption

        self.update = to_raw_response_wrapper(
            opportunistic_encryption.update,
        )
        self.get = to_raw_response_wrapper(
            opportunistic_encryption.get,
        )


class AsyncOpportunisticEncryptionWithRawResponse:
    def __init__(self, opportunistic_encryption: AsyncOpportunisticEncryption) -> None:
        self._opportunistic_encryption = opportunistic_encryption

        self.update = async_to_raw_response_wrapper(
            opportunistic_encryption.update,
        )
        self.get = async_to_raw_response_wrapper(
            opportunistic_encryption.get,
        )


class OpportunisticEncryptionWithStreamingResponse:
    def __init__(self, opportunistic_encryption: OpportunisticEncryption) -> None:
        self._opportunistic_encryption = opportunistic_encryption

        self.update = to_streamed_response_wrapper(
            opportunistic_encryption.update,
        )
        self.get = to_streamed_response_wrapper(
            opportunistic_encryption.get,
        )


class AsyncOpportunisticEncryptionWithStreamingResponse:
    def __init__(self, opportunistic_encryption: AsyncOpportunisticEncryption) -> None:
        self._opportunistic_encryption = opportunistic_encryption

        self.update = async_to_streamed_response_wrapper(
            opportunistic_encryption.update,
        )
        self.get = async_to_streamed_response_wrapper(
            opportunistic_encryption.get,
        )
