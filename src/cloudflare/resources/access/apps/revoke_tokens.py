# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from typing import Type, Optional, Union

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

__all__ = ["RevokeTokens", "AsyncRevokeTokens"]


class RevokeTokens(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevokeTokensWithRawResponse:
        return RevokeTokensWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevokeTokensWithStreamingResponse:
        return RevokeTokensWithStreamingResponse(self)

    def access_applications_revoke_service_tokens(
        self,
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Revokes all tokens issued for an application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/revoke_tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncRevokeTokens(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevokeTokensWithRawResponse:
        return AsyncRevokeTokensWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevokeTokensWithStreamingResponse:
        return AsyncRevokeTokensWithStreamingResponse(self)

    async def access_applications_revoke_service_tokens(
        self,
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Revokes all tokens issued for an application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/revoke_tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class RevokeTokensWithRawResponse:
    def __init__(self, revoke_tokens: RevokeTokens) -> None:
        self._revoke_tokens = revoke_tokens

        self.access_applications_revoke_service_tokens = to_raw_response_wrapper(
            revoke_tokens.access_applications_revoke_service_tokens,
        )


class AsyncRevokeTokensWithRawResponse:
    def __init__(self, revoke_tokens: AsyncRevokeTokens) -> None:
        self._revoke_tokens = revoke_tokens

        self.access_applications_revoke_service_tokens = async_to_raw_response_wrapper(
            revoke_tokens.access_applications_revoke_service_tokens,
        )


class RevokeTokensWithStreamingResponse:
    def __init__(self, revoke_tokens: RevokeTokens) -> None:
        self._revoke_tokens = revoke_tokens

        self.access_applications_revoke_service_tokens = to_streamed_response_wrapper(
            revoke_tokens.access_applications_revoke_service_tokens,
        )


class AsyncRevokeTokensWithStreamingResponse:
    def __init__(self, revoke_tokens: AsyncRevokeTokens) -> None:
        self._revoke_tokens = revoke_tokens

        self.access_applications_revoke_service_tokens = async_to_streamed_response_wrapper(
            revoke_tokens.access_applications_revoke_service_tokens,
        )
