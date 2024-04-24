# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ....types.zero_trust.dlp import pattern_validate_params
from ....types.logpush.ownership_validation import OwnershipValidation

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
    ) -> Optional[OwnershipValidation]:
        """Validates whether this pattern is a valid regular expression.

        Rejects it if the
        regular expression is too complex or can match an unbounded-length string. Your
        regex will be rejected if it uses the Kleene Star -- be sure to bound the
        maximum number of characters that can be matched.

        Args:
          account_id: Identifier

          regex: The regex pattern.

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
                post_parser=ResultWrapper[Optional[OwnershipValidation]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OwnershipValidation]], ResultWrapper[OwnershipValidation]),
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
    ) -> Optional[OwnershipValidation]:
        """Validates whether this pattern is a valid regular expression.

        Rejects it if the
        regular expression is too complex or can match an unbounded-length string. Your
        regex will be rejected if it uses the Kleene Star -- be sure to bound the
        maximum number of characters that can be matched.

        Args:
          account_id: Identifier

          regex: The regex pattern.

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
                post_parser=ResultWrapper[Optional[OwnershipValidation]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OwnershipValidation]], ResultWrapper[OwnershipValidation]),
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
