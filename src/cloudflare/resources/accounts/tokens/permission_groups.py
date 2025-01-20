# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options

__all__ = ["PermissionGroupsResource", "AsyncPermissionGroupsResource"]


class PermissionGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PermissionGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PermissionGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PermissionGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PermissionGroupsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[object]:
        """
        Find all available permission groups for Account Owned API Tokens

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/tokens/permission_groups",
            page=SyncSinglePage[object],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=object,
        )


class AsyncPermissionGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPermissionGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPermissionGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPermissionGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPermissionGroupsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[object, AsyncSinglePage[object]]:
        """
        Find all available permission groups for Account Owned API Tokens

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/tokens/permission_groups",
            page=AsyncSinglePage[object],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=object,
        )


class PermissionGroupsResourceWithRawResponse:
    def __init__(self, permission_groups: PermissionGroupsResource) -> None:
        self._permission_groups = permission_groups

        self.list = to_raw_response_wrapper(
            permission_groups.list,
        )


class AsyncPermissionGroupsResourceWithRawResponse:
    def __init__(self, permission_groups: AsyncPermissionGroupsResource) -> None:
        self._permission_groups = permission_groups

        self.list = async_to_raw_response_wrapper(
            permission_groups.list,
        )


class PermissionGroupsResourceWithStreamingResponse:
    def __init__(self, permission_groups: PermissionGroupsResource) -> None:
        self._permission_groups = permission_groups

        self.list = to_streamed_response_wrapper(
            permission_groups.list,
        )


class AsyncPermissionGroupsResourceWithStreamingResponse:
    def __init__(self, permission_groups: AsyncPermissionGroupsResource) -> None:
        self._permission_groups = permission_groups

        self.list = async_to_streamed_response_wrapper(
            permission_groups.list,
        )
