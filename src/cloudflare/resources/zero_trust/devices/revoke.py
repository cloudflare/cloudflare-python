# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.zero_trust.devices.revoke_create_response import RevokeCreateResponse

from ...._wrappers import ResultWrapper

from typing import Optional, List

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.zero_trust.devices import revoke_create_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["RevokeResource", "AsyncRevokeResource"]

class RevokeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevokeResourceWithRawResponse:
        return RevokeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevokeResourceWithStreamingResponse:
        return RevokeResourceWithStreamingResponse(self)

    def create(self,
    *,
    account_id: str,
    body: List[str],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RevokeCreateResponse]:
        """
        Revokes a list of devices.

        Args:
          body: A list of device ids to revoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return cast(Optional[RevokeCreateResponse], self._post(
            f"/accounts/{account_id}/devices/revoke",
            body=maybe_transform(body, List[str]),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RevokeCreateResponse]]._unwrapper),
            cast_to=cast(Any, ResultWrapper[RevokeCreateResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

class AsyncRevokeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevokeResourceWithRawResponse:
        return AsyncRevokeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevokeResourceWithStreamingResponse:
        return AsyncRevokeResourceWithStreamingResponse(self)

    async def create(self,
    *,
    account_id: str,
    body: List[str],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RevokeCreateResponse]:
        """
        Revokes a list of devices.

        Args:
          body: A list of device ids to revoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return cast(Optional[RevokeCreateResponse], await self._post(
            f"/accounts/{account_id}/devices/revoke",
            body=await async_maybe_transform(body, List[str]),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RevokeCreateResponse]]._unwrapper),
            cast_to=cast(Any, ResultWrapper[RevokeCreateResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

class RevokeResourceWithRawResponse:
    def __init__(self, revoke: RevokeResource) -> None:
        self._revoke = revoke

        self.create = to_raw_response_wrapper(
            revoke.create,
        )

class AsyncRevokeResourceWithRawResponse:
    def __init__(self, revoke: AsyncRevokeResource) -> None:
        self._revoke = revoke

        self.create = async_to_raw_response_wrapper(
            revoke.create,
        )

class RevokeResourceWithStreamingResponse:
    def __init__(self, revoke: RevokeResource) -> None:
        self._revoke = revoke

        self.create = to_streamed_response_wrapper(
            revoke.create,
        )

class AsyncRevokeResourceWithStreamingResponse:
    def __init__(self, revoke: AsyncRevokeResource) -> None:
        self._revoke = revoke

        self.create = async_to_streamed_response_wrapper(
            revoke.create,
        )