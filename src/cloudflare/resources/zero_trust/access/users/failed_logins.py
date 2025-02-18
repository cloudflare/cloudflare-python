# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.access.users.failed_login_list_response import FailedLoginListResponse

__all__ = ["FailedLoginsResource", "AsyncFailedLoginsResource"]


class FailedLoginsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FailedLoginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FailedLoginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FailedLoginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFailedLoginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFailedLoginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
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
