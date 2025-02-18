# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.iam import permission_group_list_params
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.iam.permission_group_get_response import PermissionGroupGetResponse
from ...types.iam.permission_group_list_response import PermissionGroupListResponse

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
        id: str | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[PermissionGroupListResponse]:
        """
        List all the permissions groups for an account.

        Args:
          account_id: Account identifier tag.

          id: ID of the permission group to be fetched.

          label: Label of the permission group to be fetched.

          name: Name of the permission group to be fetched.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/iam/permission_groups",
            page=SyncV4PagePaginationArray[PermissionGroupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "label": label,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    permission_group_list_params.PermissionGroupListParams,
                ),
            ),
            model=PermissionGroupListResponse,
        )

    def get(
        self,
        permission_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PermissionGroupGetResponse:
        """
        Get information about a specific permission group in an account.

        Args:
          account_id: Account identifier tag.

          permission_group_id: Permission Group identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not permission_group_id:
            raise ValueError(
                f"Expected a non-empty value for `permission_group_id` but received {permission_group_id!r}"
            )
        return self._get(
            f"/accounts/{account_id}/iam/permission_groups/{permission_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PermissionGroupGetResponse,
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
        id: str | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PermissionGroupListResponse, AsyncV4PagePaginationArray[PermissionGroupListResponse]]:
        """
        List all the permissions groups for an account.

        Args:
          account_id: Account identifier tag.

          id: ID of the permission group to be fetched.

          label: Label of the permission group to be fetched.

          name: Name of the permission group to be fetched.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/iam/permission_groups",
            page=AsyncV4PagePaginationArray[PermissionGroupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "label": label,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    permission_group_list_params.PermissionGroupListParams,
                ),
            ),
            model=PermissionGroupListResponse,
        )

    async def get(
        self,
        permission_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PermissionGroupGetResponse:
        """
        Get information about a specific permission group in an account.

        Args:
          account_id: Account identifier tag.

          permission_group_id: Permission Group identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not permission_group_id:
            raise ValueError(
                f"Expected a non-empty value for `permission_group_id` but received {permission_group_id!r}"
            )
        return await self._get(
            f"/accounts/{account_id}/iam/permission_groups/{permission_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PermissionGroupGetResponse,
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
