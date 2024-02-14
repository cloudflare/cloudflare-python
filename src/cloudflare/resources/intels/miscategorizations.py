# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.intels import MiscategorizationMiscategorizationCreateMiscategorizationResponse

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
from ...types.intels import miscategorization_miscategorization_create_miscategorization_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Miscategorizations", "AsyncMiscategorizations"]


class Miscategorizations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MiscategorizationsWithRawResponse:
        return MiscategorizationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MiscategorizationsWithStreamingResponse:
        return MiscategorizationsWithStreamingResponse(self)

    def miscategorization_create_miscategorization(
        self,
        account_id: str,
        *,
        content_adds: object | NotGiven = NOT_GIVEN,
        content_removes: object | NotGiven = NOT_GIVEN,
        indicator_type: Literal["domain", "ipv4", "ipv6", "url"] | NotGiven = NOT_GIVEN,
        ip: object | NotGiven = NOT_GIVEN,
        security_adds: object | NotGiven = NOT_GIVEN,
        security_removes: object | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MiscategorizationMiscategorizationCreateMiscategorizationResponse:
        """
        Create Miscategorization

        Args:
          account_id: Identifier

          content_adds: Content category IDs to add.

          content_removes: Content category IDs to remove.

          ip: Provide only if indicator_type is `ipv4` or `ipv6`.

          security_adds: Security category IDs to add.

          security_removes: Security category IDs to remove.

          url: Provide only if indicator_type is `domain` or `url`. Example if indicator_type
              is `domain`: `example.com`. Example if indicator_type is `url`:
              `https://example.com/news/`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            MiscategorizationMiscategorizationCreateMiscategorizationResponse,
            self._post(
                f"/accounts/{account_id}/intel/miscategorization",
                body=maybe_transform(
                    {
                        "content_adds": content_adds,
                        "content_removes": content_removes,
                        "indicator_type": indicator_type,
                        "ip": ip,
                        "security_adds": security_adds,
                        "security_removes": security_removes,
                        "url": url,
                    },
                    miscategorization_miscategorization_create_miscategorization_params.MiscategorizationMiscategorizationCreateMiscategorizationParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[MiscategorizationMiscategorizationCreateMiscategorizationResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncMiscategorizations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMiscategorizationsWithRawResponse:
        return AsyncMiscategorizationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMiscategorizationsWithStreamingResponse:
        return AsyncMiscategorizationsWithStreamingResponse(self)

    async def miscategorization_create_miscategorization(
        self,
        account_id: str,
        *,
        content_adds: object | NotGiven = NOT_GIVEN,
        content_removes: object | NotGiven = NOT_GIVEN,
        indicator_type: Literal["domain", "ipv4", "ipv6", "url"] | NotGiven = NOT_GIVEN,
        ip: object | NotGiven = NOT_GIVEN,
        security_adds: object | NotGiven = NOT_GIVEN,
        security_removes: object | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MiscategorizationMiscategorizationCreateMiscategorizationResponse:
        """
        Create Miscategorization

        Args:
          account_id: Identifier

          content_adds: Content category IDs to add.

          content_removes: Content category IDs to remove.

          ip: Provide only if indicator_type is `ipv4` or `ipv6`.

          security_adds: Security category IDs to add.

          security_removes: Security category IDs to remove.

          url: Provide only if indicator_type is `domain` or `url`. Example if indicator_type
              is `domain`: `example.com`. Example if indicator_type is `url`:
              `https://example.com/news/`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            MiscategorizationMiscategorizationCreateMiscategorizationResponse,
            await self._post(
                f"/accounts/{account_id}/intel/miscategorization",
                body=maybe_transform(
                    {
                        "content_adds": content_adds,
                        "content_removes": content_removes,
                        "indicator_type": indicator_type,
                        "ip": ip,
                        "security_adds": security_adds,
                        "security_removes": security_removes,
                        "url": url,
                    },
                    miscategorization_miscategorization_create_miscategorization_params.MiscategorizationMiscategorizationCreateMiscategorizationParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[MiscategorizationMiscategorizationCreateMiscategorizationResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class MiscategorizationsWithRawResponse:
    def __init__(self, miscategorizations: Miscategorizations) -> None:
        self._miscategorizations = miscategorizations

        self.miscategorization_create_miscategorization = to_raw_response_wrapper(
            miscategorizations.miscategorization_create_miscategorization,
        )


class AsyncMiscategorizationsWithRawResponse:
    def __init__(self, miscategorizations: AsyncMiscategorizations) -> None:
        self._miscategorizations = miscategorizations

        self.miscategorization_create_miscategorization = async_to_raw_response_wrapper(
            miscategorizations.miscategorization_create_miscategorization,
        )


class MiscategorizationsWithStreamingResponse:
    def __init__(self, miscategorizations: Miscategorizations) -> None:
        self._miscategorizations = miscategorizations

        self.miscategorization_create_miscategorization = to_streamed_response_wrapper(
            miscategorizations.miscategorization_create_miscategorization,
        )


class AsyncMiscategorizationsWithStreamingResponse:
    def __init__(self, miscategorizations: AsyncMiscategorizations) -> None:
        self._miscategorizations = miscategorizations

        self.miscategorization_create_miscategorization = async_to_streamed_response_wrapper(
            miscategorizations.miscategorization_create_miscategorization,
        )
