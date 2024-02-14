# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.access.service_tokens import RotateAccessServiceTokensRotateAServiceTokenResponse

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

__all__ = ["Rotates", "AsyncRotates"]


class Rotates(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RotatesWithRawResponse:
        return RotatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RotatesWithStreamingResponse:
        return RotatesWithStreamingResponse(self)

    def access_service_tokens_rotate_a_service_token(
        self,
        uuid: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RotateAccessServiceTokensRotateAServiceTokenResponse:
        """
        Generates a new Client Secret for a service token and revokes the old one.

        Args:
          identifier: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._post(
            f"/accounts/{identifier}/access/service_tokens/{uuid}/rotate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RotateAccessServiceTokensRotateAServiceTokenResponse],
                ResultWrapper[RotateAccessServiceTokensRotateAServiceTokenResponse],
            ),
        )


class AsyncRotates(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRotatesWithRawResponse:
        return AsyncRotatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRotatesWithStreamingResponse:
        return AsyncRotatesWithStreamingResponse(self)

    async def access_service_tokens_rotate_a_service_token(
        self,
        uuid: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RotateAccessServiceTokensRotateAServiceTokenResponse:
        """
        Generates a new Client Secret for a service token and revokes the old one.

        Args:
          identifier: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._post(
            f"/accounts/{identifier}/access/service_tokens/{uuid}/rotate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RotateAccessServiceTokensRotateAServiceTokenResponse],
                ResultWrapper[RotateAccessServiceTokensRotateAServiceTokenResponse],
            ),
        )


class RotatesWithRawResponse:
    def __init__(self, rotates: Rotates) -> None:
        self._rotates = rotates

        self.access_service_tokens_rotate_a_service_token = to_raw_response_wrapper(
            rotates.access_service_tokens_rotate_a_service_token,
        )


class AsyncRotatesWithRawResponse:
    def __init__(self, rotates: AsyncRotates) -> None:
        self._rotates = rotates

        self.access_service_tokens_rotate_a_service_token = async_to_raw_response_wrapper(
            rotates.access_service_tokens_rotate_a_service_token,
        )


class RotatesWithStreamingResponse:
    def __init__(self, rotates: Rotates) -> None:
        self._rotates = rotates

        self.access_service_tokens_rotate_a_service_token = to_streamed_response_wrapper(
            rotates.access_service_tokens_rotate_a_service_token,
        )


class AsyncRotatesWithStreamingResponse:
    def __init__(self, rotates: AsyncRotates) -> None:
        self._rotates = rotates

        self.access_service_tokens_rotate_a_service_token = async_to_streamed_response_wrapper(
            rotates.access_service_tokens_rotate_a_service_token,
        )
