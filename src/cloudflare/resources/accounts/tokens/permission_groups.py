# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.accounts.tokens import permission_group_get_params, permission_group_list_params
from ....types.accounts.tokens.permission_group_get_response import PermissionGroupGetResponse
from ....types.accounts.tokens.permission_group_list_response import PermissionGroupListResponse

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
        account_id: str | None = None,
        name: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[PermissionGroupListResponse]:
        """
        Find all available permission groups for Account Owned API Tokens

        Args:
          account_id: Account identifier tag.

          name: Filter by the name of the permission group. The value must be URL-encoded.

          scope: Filter by the scope of the permission group. The value must be URL-encoded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/tokens/permission_groups", account_id=account_id),
            page=SyncSinglePage[PermissionGroupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "scope": scope,
                    },
                    permission_group_list_params.PermissionGroupListParams,
                ),
            ),
            model=PermissionGroupListResponse,
        )

    def get(
        self,
        *,
        account_id: str | None = None,
        name: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PermissionGroupGetResponse]:
        """
        Find all available permission groups for Account Owned API Tokens

        Args:
          account_id: Account identifier tag.

          name: Filter by the name of the permission group. The value must be URL-encoded.

          scope: Filter by the scope of the permission group. The value must be URL-encoded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/tokens/permission_groups", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "scope": scope,
                    },
                    permission_group_get_params.PermissionGroupGetParams,
                ),
                post_parser=ResultWrapper[Optional[PermissionGroupGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PermissionGroupGetResponse]], ResultWrapper[PermissionGroupGetResponse]),
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
        account_id: str | None = None,
        name: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PermissionGroupListResponse, AsyncSinglePage[PermissionGroupListResponse]]:
        """
        Find all available permission groups for Account Owned API Tokens

        Args:
          account_id: Account identifier tag.

          name: Filter by the name of the permission group. The value must be URL-encoded.

          scope: Filter by the scope of the permission group. The value must be URL-encoded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/tokens/permission_groups", account_id=account_id),
            page=AsyncSinglePage[PermissionGroupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "scope": scope,
                    },
                    permission_group_list_params.PermissionGroupListParams,
                ),
            ),
            model=PermissionGroupListResponse,
        )

    async def get(
        self,
        *,
        account_id: str | None = None,
        name: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PermissionGroupGetResponse]:
        """
        Find all available permission groups for Account Owned API Tokens

        Args:
          account_id: Account identifier tag.

          name: Filter by the name of the permission group. The value must be URL-encoded.

          scope: Filter by the scope of the permission group. The value must be URL-encoded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/tokens/permission_groups", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "scope": scope,
                    },
                    permission_group_get_params.PermissionGroupGetParams,
                ),
                post_parser=ResultWrapper[Optional[PermissionGroupGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PermissionGroupGetResponse]], ResultWrapper[PermissionGroupGetResponse]),
        )


class PermissionGroupsResourceWithRawResponse:
    def __init__(self, permission_groups: PermissionGroupsResource) -> None:
        self._permission_groups = permission_groups

        self.list = to_raw_response_wrapper(
            permission_groups.list,
        )
        self.get = to_raw_response_wrapper(
            permission_groups.get,
        )


class AsyncPermissionGroupsResourceWithRawResponse:
    def __init__(self, permission_groups: AsyncPermissionGroupsResource) -> None:
        self._permission_groups = permission_groups

        self.list = async_to_raw_response_wrapper(
            permission_groups.list,
        )
        self.get = async_to_raw_response_wrapper(
            permission_groups.get,
        )


class PermissionGroupsResourceWithStreamingResponse:
    def __init__(self, permission_groups: PermissionGroupsResource) -> None:
        self._permission_groups = permission_groups

        self.list = to_streamed_response_wrapper(
            permission_groups.list,
        )
        self.get = to_streamed_response_wrapper(
            permission_groups.get,
        )


class AsyncPermissionGroupsResourceWithStreamingResponse:
    def __init__(self, permission_groups: AsyncPermissionGroupsResource) -> None:
        self._permission_groups = permission_groups

        self.list = async_to_streamed_response_wrapper(
            permission_groups.list,
        )
        self.get = async_to_streamed_response_wrapper(
            permission_groups.get,
        )
