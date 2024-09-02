# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.zero_trust.access.users.failed_login_list_response import FailedLoginListResponse

from .....pagination import SyncSinglePage, AsyncSinglePage

from ....._base_client import make_request_options, AsyncPaginator

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params

__all__ = ["FailedLoginsResource", "AsyncFailedLoginsResource"]


class FailedLoginsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FailedLoginsResourceWithRawResponse:
        return FailedLoginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FailedLoginsResourceWithStreamingResponse:
        return FailedLoginsResourceWithStreamingResponse(self)

    def list(
        self,
        user_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[FailedLoginListResponse]:
        """
        Get all failed login attempts for a single user.

        Args:
          account_id: Identifier

          user_id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/access/users/{user_id}/failed_logins",
            page=SyncSinglePage[FailedLoginListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=FailedLoginListResponse,
        )


class AsyncFailedLoginsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFailedLoginsResourceWithRawResponse:
        return AsyncFailedLoginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFailedLoginsResourceWithStreamingResponse:
        return AsyncFailedLoginsResourceWithStreamingResponse(self)

    def list(
        self,
        user_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[FailedLoginListResponse, AsyncSinglePage[FailedLoginListResponse]]:
        """
        Get all failed login attempts for a single user.

        Args:
          account_id: Identifier

          user_id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/access/users/{user_id}/failed_logins",
            page=AsyncSinglePage[FailedLoginListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=FailedLoginListResponse,
        )


class FailedLoginsResourceWithRawResponse:
    def __init__(self, failed_logins: FailedLoginsResource) -> None:
        self._failed_logins = failed_logins

        self.list = to_raw_response_wrapper(
            failed_logins.list,
        )


class AsyncFailedLoginsResourceWithRawResponse:
    def __init__(self, failed_logins: AsyncFailedLoginsResource) -> None:
        self._failed_logins = failed_logins

        self.list = async_to_raw_response_wrapper(
            failed_logins.list,
        )


class FailedLoginsResourceWithStreamingResponse:
    def __init__(self, failed_logins: FailedLoginsResource) -> None:
        self._failed_logins = failed_logins

        self.list = to_streamed_response_wrapper(
            failed_logins.list,
        )


class AsyncFailedLoginsResourceWithStreamingResponse:
    def __init__(self, failed_logins: AsyncFailedLoginsResource) -> None:
        self._failed_logins = failed_logins

        self.list = async_to_streamed_response_wrapper(
            failed_logins.list,
        )
