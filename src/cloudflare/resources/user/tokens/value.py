# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ....types.user.tokens.value import Value

from ...._base_client import make_request_options

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.user.tokens import value_update_params
from typing import cast
from typing import cast

__all__ = ["ValueResource", "AsyncValueResource"]

class ValueResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValueResourceWithRawResponse:
        return ValueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValueResourceWithStreamingResponse:
        return ValueResourceWithStreamingResponse(self)

    def update(self,
    token_id: str,
    *,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> str:
        """
        Roll the token secret.

        Args:
          token_id: Token identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token_id:
          raise ValueError(
            f'Expected a non-empty value for `token_id` but received {token_id!r}'
          )
        return self._put(
            f"/user/tokens/{token_id}/value",
            body=maybe_transform(body, value_update_params.ValueUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Value]]._unwrapper),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

class AsyncValueResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValueResourceWithRawResponse:
        return AsyncValueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValueResourceWithStreamingResponse:
        return AsyncValueResourceWithStreamingResponse(self)

    async def update(self,
    token_id: str,
    *,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> str:
        """
        Roll the token secret.

        Args:
          token_id: Token identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token_id:
          raise ValueError(
            f'Expected a non-empty value for `token_id` but received {token_id!r}'
          )
        return await self._put(
            f"/user/tokens/{token_id}/value",
            body=await async_maybe_transform(body, value_update_params.ValueUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Value]]._unwrapper),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

class ValueResourceWithRawResponse:
    def __init__(self, value: ValueResource) -> None:
        self._value = value

        self.update = to_raw_response_wrapper(
            value.update,
        )

class AsyncValueResourceWithRawResponse:
    def __init__(self, value: AsyncValueResource) -> None:
        self._value = value

        self.update = async_to_raw_response_wrapper(
            value.update,
        )

class ValueResourceWithStreamingResponse:
    def __init__(self, value: ValueResource) -> None:
        self._value = value

        self.update = to_streamed_response_wrapper(
            value.update,
        )

class AsyncValueResourceWithStreamingResponse:
    def __init__(self, value: AsyncValueResource) -> None:
        self._value = value

        self.update = async_to_streamed_response_wrapper(
            value.update,
        )