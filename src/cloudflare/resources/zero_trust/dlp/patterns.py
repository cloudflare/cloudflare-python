# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.zero_trust.dlp.pattern_validate_response import PatternValidateResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ...._base_client import make_request_options

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.zero_trust.dlp import pattern_validate_params
from typing import cast
from typing import cast

__all__ = ["PatternsResource", "AsyncPatternsResource"]


class PatternsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PatternsResourceWithRawResponse:
        return PatternsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PatternsResourceWithStreamingResponse:
        return PatternsResourceWithStreamingResponse(self)

    def validate(
        self,
        *,
        account_id: str,
        regex: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PatternValidateResponse]:
        """Validates whether this pattern is a valid regular expression.

        Rejects it if the
        regular expression is too complex or can match an unbounded-length string. The
        regex will be rejected if it uses `*` or `+`. Bound the maximum number of
        characters that can be matched using a range, e.g. `{1,100}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/dlp/patterns/validate",
            body=maybe_transform({"regex": regex}, pattern_validate_params.PatternValidateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PatternValidateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PatternValidateResponse]], ResultWrapper[PatternValidateResponse]),
        )


class AsyncPatternsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPatternsResourceWithRawResponse:
        return AsyncPatternsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPatternsResourceWithStreamingResponse:
        return AsyncPatternsResourceWithStreamingResponse(self)

    async def validate(
        self,
        *,
        account_id: str,
        regex: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PatternValidateResponse]:
        """Validates whether this pattern is a valid regular expression.

        Rejects it if the
        regular expression is too complex or can match an unbounded-length string. The
        regex will be rejected if it uses `*` or `+`. Bound the maximum number of
        characters that can be matched using a range, e.g. `{1,100}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/dlp/patterns/validate",
            body=await async_maybe_transform({"regex": regex}, pattern_validate_params.PatternValidateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PatternValidateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PatternValidateResponse]], ResultWrapper[PatternValidateResponse]),
        )


class PatternsResourceWithRawResponse:
    def __init__(self, patterns: PatternsResource) -> None:
        self._patterns = patterns

        self.validate = to_raw_response_wrapper(
            patterns.validate,
        )


class AsyncPatternsResourceWithRawResponse:
    def __init__(self, patterns: AsyncPatternsResource) -> None:
        self._patterns = patterns

        self.validate = async_to_raw_response_wrapper(
            patterns.validate,
        )


class PatternsResourceWithStreamingResponse:
    def __init__(self, patterns: PatternsResource) -> None:
        self._patterns = patterns

        self.validate = to_streamed_response_wrapper(
            patterns.validate,
        )


class AsyncPatternsResourceWithStreamingResponse:
    def __init__(self, patterns: AsyncPatternsResource) -> None:
        self._patterns = patterns

        self.validate = async_to_streamed_response_wrapper(
            patterns.validate,
        )
