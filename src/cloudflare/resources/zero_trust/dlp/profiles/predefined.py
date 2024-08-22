# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.zero_trust.dlp.profile import Profile

from ....._wrappers import ResultWrapper

from typing import Optional

from ....._base_client import make_request_options

from ....._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["PredefinedResource", "AsyncPredefinedResource"]

class PredefinedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PredefinedResourceWithRawResponse:
        return PredefinedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PredefinedResourceWithStreamingResponse:
        return PredefinedResourceWithStreamingResponse(self)

    def update(self,
    profile_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Profile]:
        """Updates a DLP predefined profile.

        Only supports enabling/disabling entries.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not profile_id:
          raise ValueError(
            f'Expected a non-empty value for `profile_id` but received {profile_id!r}'
          )
        return cast(Optional[Profile], self._put(
            f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Profile]]._unwrapper),
            cast_to=cast(Any, ResultWrapper[Profile]),  # Union types cannot be passed in as arguments in the type system
        ))

    def get(self,
    profile_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Profile]:
        """
        Fetches a predefined DLP profile by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not profile_id:
          raise ValueError(
            f'Expected a non-empty value for `profile_id` but received {profile_id!r}'
          )
        return cast(Optional[Profile], self._get(
            f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Profile]]._unwrapper),
            cast_to=cast(Any, ResultWrapper[Profile]),  # Union types cannot be passed in as arguments in the type system
        ))

class AsyncPredefinedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPredefinedResourceWithRawResponse:
        return AsyncPredefinedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPredefinedResourceWithStreamingResponse:
        return AsyncPredefinedResourceWithStreamingResponse(self)

    async def update(self,
    profile_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Profile]:
        """Updates a DLP predefined profile.

        Only supports enabling/disabling entries.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not profile_id:
          raise ValueError(
            f'Expected a non-empty value for `profile_id` but received {profile_id!r}'
          )
        return cast(Optional[Profile], await self._put(
            f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Profile]]._unwrapper),
            cast_to=cast(Any, ResultWrapper[Profile]),  # Union types cannot be passed in as arguments in the type system
        ))

    async def get(self,
    profile_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Profile]:
        """
        Fetches a predefined DLP profile by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not profile_id:
          raise ValueError(
            f'Expected a non-empty value for `profile_id` but received {profile_id!r}'
          )
        return cast(Optional[Profile], await self._get(
            f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Profile]]._unwrapper),
            cast_to=cast(Any, ResultWrapper[Profile]),  # Union types cannot be passed in as arguments in the type system
        ))

class PredefinedResourceWithRawResponse:
    def __init__(self, predefined: PredefinedResource) -> None:
        self._predefined = predefined

        self.update = to_raw_response_wrapper(
            predefined.update,
        )
        self.get = to_raw_response_wrapper(
            predefined.get,
        )

class AsyncPredefinedResourceWithRawResponse:
    def __init__(self, predefined: AsyncPredefinedResource) -> None:
        self._predefined = predefined

        self.update = async_to_raw_response_wrapper(
            predefined.update,
        )
        self.get = async_to_raw_response_wrapper(
            predefined.get,
        )

class PredefinedResourceWithStreamingResponse:
    def __init__(self, predefined: PredefinedResource) -> None:
        self._predefined = predefined

        self.update = to_streamed_response_wrapper(
            predefined.update,
        )
        self.get = to_streamed_response_wrapper(
            predefined.get,
        )

class AsyncPredefinedResourceWithStreamingResponse:
    def __init__(self, predefined: AsyncPredefinedResource) -> None:
        self._predefined = predefined

        self.update = async_to_streamed_response_wrapper(
            predefined.update,
        )
        self.get = async_to_streamed_response_wrapper(
            predefined.get,
        )