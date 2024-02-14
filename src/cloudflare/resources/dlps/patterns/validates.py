# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.dlps.patterns import ValidateDLPPatternValidationValidatePatternResponse

from typing import Type

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
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.dlps.patterns import validate_dlp_pattern_validation_validate_pattern_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Validates", "AsyncValidates"]


class Validates(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValidatesWithRawResponse:
        return ValidatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValidatesWithStreamingResponse:
        return ValidatesWithStreamingResponse(self)

    def dlp_pattern_validation_validate_pattern(
        self,
        account_id: str,
        *,
        regex: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValidateDLPPatternValidationValidatePatternResponse:
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
            body=maybe_transform(
                {"regex": regex},
                validate_dlp_pattern_validation_validate_pattern_params.ValidateDLPPatternValidationValidatePatternParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ValidateDLPPatternValidationValidatePatternResponse],
                ResultWrapper[ValidateDLPPatternValidationValidatePatternResponse],
            ),
        )


class AsyncValidates(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValidatesWithRawResponse:
        return AsyncValidatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValidatesWithStreamingResponse:
        return AsyncValidatesWithStreamingResponse(self)

    async def dlp_pattern_validation_validate_pattern(
        self,
        account_id: str,
        *,
        regex: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValidateDLPPatternValidationValidatePatternResponse:
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
            body=maybe_transform(
                {"regex": regex},
                validate_dlp_pattern_validation_validate_pattern_params.ValidateDLPPatternValidationValidatePatternParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ValidateDLPPatternValidationValidatePatternResponse],
                ResultWrapper[ValidateDLPPatternValidationValidatePatternResponse],
            ),
        )


class ValidatesWithRawResponse:
    def __init__(self, validates: Validates) -> None:
        self._validates = validates

        self.dlp_pattern_validation_validate_pattern = to_raw_response_wrapper(
            validates.dlp_pattern_validation_validate_pattern,
        )


class AsyncValidatesWithRawResponse:
    def __init__(self, validates: AsyncValidates) -> None:
        self._validates = validates

        self.dlp_pattern_validation_validate_pattern = async_to_raw_response_wrapper(
            validates.dlp_pattern_validation_validate_pattern,
        )


class ValidatesWithStreamingResponse:
    def __init__(self, validates: Validates) -> None:
        self._validates = validates

        self.dlp_pattern_validation_validate_pattern = to_streamed_response_wrapper(
            validates.dlp_pattern_validation_validate_pattern,
        )


class AsyncValidatesWithStreamingResponse:
    def __init__(self, validates: AsyncValidates) -> None:
        self._validates = validates

        self.dlp_pattern_validation_validate_pattern = async_to_streamed_response_wrapper(
            validates.dlp_pattern_validation_validate_pattern,
        )
