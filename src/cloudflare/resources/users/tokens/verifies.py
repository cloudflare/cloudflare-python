# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.users.tokens import VerifyUserAPITokensVerifyTokenResponse

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
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Verifies", "AsyncVerifies"]


class Verifies(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VerifiesWithRawResponse:
        return VerifiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerifiesWithStreamingResponse:
        return VerifiesWithStreamingResponse(self)

    def user_api_tokens_verify_token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerifyUserAPITokensVerifyTokenResponse:
        """Test whether a token works."""
        return self._get(
            "/user/tokens/verify",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[VerifyUserAPITokensVerifyTokenResponse], ResultWrapper[VerifyUserAPITokensVerifyTokenResponse]
            ),
        )


class AsyncVerifies(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVerifiesWithRawResponse:
        return AsyncVerifiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerifiesWithStreamingResponse:
        return AsyncVerifiesWithStreamingResponse(self)

    async def user_api_tokens_verify_token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerifyUserAPITokensVerifyTokenResponse:
        """Test whether a token works."""
        return await self._get(
            "/user/tokens/verify",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[VerifyUserAPITokensVerifyTokenResponse], ResultWrapper[VerifyUserAPITokensVerifyTokenResponse]
            ),
        )


class VerifiesWithRawResponse:
    def __init__(self, verifies: Verifies) -> None:
        self._verifies = verifies

        self.user_api_tokens_verify_token = to_raw_response_wrapper(
            verifies.user_api_tokens_verify_token,
        )


class AsyncVerifiesWithRawResponse:
    def __init__(self, verifies: AsyncVerifies) -> None:
        self._verifies = verifies

        self.user_api_tokens_verify_token = async_to_raw_response_wrapper(
            verifies.user_api_tokens_verify_token,
        )


class VerifiesWithStreamingResponse:
    def __init__(self, verifies: Verifies) -> None:
        self._verifies = verifies

        self.user_api_tokens_verify_token = to_streamed_response_wrapper(
            verifies.user_api_tokens_verify_token,
        )


class AsyncVerifiesWithStreamingResponse:
    def __init__(self, verifies: AsyncVerifies) -> None:
        self._verifies = verifies

        self.user_api_tokens_verify_token = async_to_streamed_response_wrapper(
            verifies.user_api_tokens_verify_token,
        )
