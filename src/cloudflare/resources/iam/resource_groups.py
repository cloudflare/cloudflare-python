# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.iam import resource_group_list_params, resource_group_create_params, resource_group_update_params
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.iam.resource_group_get_response import ResourceGroupGetResponse
from ...types.iam.resource_group_list_response import ResourceGroupListResponse
from ...types.iam.resource_group_create_response import ResourceGroupCreateResponse
from ...types.iam.resource_group_delete_response import ResourceGroupDeleteResponse
from ...types.iam.resource_group_update_response import ResourceGroupUpdateResponse

__all__ = ["ResourceGroupsResource", "AsyncResourceGroupsResource"]


class ResourceGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourceGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ResourceGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourceGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ResourceGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        scope: resource_group_create_params.Scope,
        meta: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGroupCreateResponse:
        """
        Create a new Resource Group under the specified account.

        Args:
          account_id: Account identifier tag.

          scope: A scope is a combination of scope objects which provides additional context.

          meta: Attributes associated to the resource group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/iam/resource_groups",
            body=maybe_transform(
                {
                    "scope": scope,
                    "meta": meta,
                },
                resource_group_create_params.ResourceGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceGroupCreateResponse,
        )

    def update(
        self,
        resource_group_id: str,
        *,
        account_id: str,
        scope: resource_group_update_params.Scope,
        meta: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGroupUpdateResponse:
        """
        Modify an existing resource group.

        Args:
          account_id: Account identifier tag.

          resource_group_id: Resource Group identifier tag.

          scope: A scope is a combination of scope objects which provides additional context.

          meta: Attributes associated to the resource group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not resource_group_id:
            raise ValueError(f"Expected a non-empty value for `resource_group_id` but received {resource_group_id!r}")
        return self._put(
            f"/accounts/{account_id}/iam/resource_groups/{resource_group_id}",
            body=maybe_transform(
                {
                    "scope": scope,
                    "meta": meta,
                },
                resource_group_update_params.ResourceGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceGroupUpdateResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[ResourceGroupListResponse]:
        """
        List all the resource groups for an account.

        Args:
          account_id: Account identifier tag.

          id: ID of the resource group to be fetched.

          name: Name of the resource group to be fetched.

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
            f"/accounts/{account_id}/iam/resource_groups",
            page=SyncV4PagePaginationArray[ResourceGroupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    resource_group_list_params.ResourceGroupListParams,
                ),
            ),
            model=ResourceGroupListResponse,
        )

    def delete(
        self,
        resource_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ResourceGroupDeleteResponse]:
        """
        Remove a resource group from an account.

        Args:
          account_id: Account identifier tag.

          resource_group_id: Resource Group identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not resource_group_id:
            raise ValueError(f"Expected a non-empty value for `resource_group_id` but received {resource_group_id!r}")
        return self._delete(
            f"/accounts/{account_id}/iam/resource_groups/{resource_group_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceGroupDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceGroupDeleteResponse]], ResultWrapper[ResourceGroupDeleteResponse]),
        )

    def get(
        self,
        resource_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGroupGetResponse:
        """
        Get information about a specific resource group in an account.

        Args:
          account_id: Account identifier tag.

          resource_group_id: Resource Group identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not resource_group_id:
            raise ValueError(f"Expected a non-empty value for `resource_group_id` but received {resource_group_id!r}")
        return self._get(
            f"/accounts/{account_id}/iam/resource_groups/{resource_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceGroupGetResponse,
        )


class AsyncResourceGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourceGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResourceGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourceGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncResourceGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        scope: resource_group_create_params.Scope,
        meta: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGroupCreateResponse:
        """
        Create a new Resource Group under the specified account.

        Args:
          account_id: Account identifier tag.

          scope: A scope is a combination of scope objects which provides additional context.

          meta: Attributes associated to the resource group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/iam/resource_groups",
            body=await async_maybe_transform(
                {
                    "scope": scope,
                    "meta": meta,
                },
                resource_group_create_params.ResourceGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceGroupCreateResponse,
        )

    async def update(
        self,
        resource_group_id: str,
        *,
        account_id: str,
        scope: resource_group_update_params.Scope,
        meta: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGroupUpdateResponse:
        """
        Modify an existing resource group.

        Args:
          account_id: Account identifier tag.

          resource_group_id: Resource Group identifier tag.

          scope: A scope is a combination of scope objects which provides additional context.

          meta: Attributes associated to the resource group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not resource_group_id:
            raise ValueError(f"Expected a non-empty value for `resource_group_id` but received {resource_group_id!r}")
        return await self._put(
            f"/accounts/{account_id}/iam/resource_groups/{resource_group_id}",
            body=await async_maybe_transform(
                {
                    "scope": scope,
                    "meta": meta,
                },
                resource_group_update_params.ResourceGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceGroupUpdateResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ResourceGroupListResponse, AsyncV4PagePaginationArray[ResourceGroupListResponse]]:
        """
        List all the resource groups for an account.

        Args:
          account_id: Account identifier tag.

          id: ID of the resource group to be fetched.

          name: Name of the resource group to be fetched.

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
            f"/accounts/{account_id}/iam/resource_groups",
            page=AsyncV4PagePaginationArray[ResourceGroupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    resource_group_list_params.ResourceGroupListParams,
                ),
            ),
            model=ResourceGroupListResponse,
        )

    async def delete(
        self,
        resource_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ResourceGroupDeleteResponse]:
        """
        Remove a resource group from an account.

        Args:
          account_id: Account identifier tag.

          resource_group_id: Resource Group identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not resource_group_id:
            raise ValueError(f"Expected a non-empty value for `resource_group_id` but received {resource_group_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/iam/resource_groups/{resource_group_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceGroupDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceGroupDeleteResponse]], ResultWrapper[ResourceGroupDeleteResponse]),
        )

    async def get(
        self,
        resource_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGroupGetResponse:
        """
        Get information about a specific resource group in an account.

        Args:
          account_id: Account identifier tag.

          resource_group_id: Resource Group identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not resource_group_id:
            raise ValueError(f"Expected a non-empty value for `resource_group_id` but received {resource_group_id!r}")
        return await self._get(
            f"/accounts/{account_id}/iam/resource_groups/{resource_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceGroupGetResponse,
        )


class ResourceGroupsResourceWithRawResponse:
    def __init__(self, resource_groups: ResourceGroupsResource) -> None:
        self._resource_groups = resource_groups

        self.create = to_raw_response_wrapper(
            resource_groups.create,
        )
        self.update = to_raw_response_wrapper(
            resource_groups.update,
        )
        self.list = to_raw_response_wrapper(
            resource_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            resource_groups.delete,
        )
        self.get = to_raw_response_wrapper(
            resource_groups.get,
        )


class AsyncResourceGroupsResourceWithRawResponse:
    def __init__(self, resource_groups: AsyncResourceGroupsResource) -> None:
        self._resource_groups = resource_groups

        self.create = async_to_raw_response_wrapper(
            resource_groups.create,
        )
        self.update = async_to_raw_response_wrapper(
            resource_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            resource_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            resource_groups.delete,
        )
        self.get = async_to_raw_response_wrapper(
            resource_groups.get,
        )


class ResourceGroupsResourceWithStreamingResponse:
    def __init__(self, resource_groups: ResourceGroupsResource) -> None:
        self._resource_groups = resource_groups

        self.create = to_streamed_response_wrapper(
            resource_groups.create,
        )
        self.update = to_streamed_response_wrapper(
            resource_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            resource_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            resource_groups.delete,
        )
        self.get = to_streamed_response_wrapper(
            resource_groups.get,
        )


class AsyncResourceGroupsResourceWithStreamingResponse:
    def __init__(self, resource_groups: AsyncResourceGroupsResource) -> None:
        self._resource_groups = resource_groups

        self.create = async_to_streamed_response_wrapper(
            resource_groups.create,
        )
        self.update = async_to_streamed_response_wrapper(
            resource_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            resource_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            resource_groups.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            resource_groups.get,
        )
