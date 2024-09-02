# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.iam.resource_group_create_response import ResourceGroupCreateResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options, AsyncPaginator

from ...types.iam.resource_group_update_response import ResourceGroupUpdateResponse

from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

from ...types.iam.resource_group_delete_response import ResourceGroupDeleteResponse

from ..._wrappers import ResultWrapper

from typing import Optional, Type

from ...types.iam.resource_group_get_response import ResourceGroupGetResponse

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ...types.iam import resource_group_create_params, resource_group_update_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.iam import resource_group_create_params
from ...types.iam import resource_group_update_params
from ...types.iam import resource_group_list_params
from typing import cast
from typing import cast

__all__ = ["ResourceGroupsResource", "AsyncResourceGroupsResource"]


class ResourceGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourceGroupsResourceWithRawResponse:
        return ResourceGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourceGroupsResourceWithStreamingResponse:
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
    ) -> SyncV4PagePaginationArray[object]:
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
            page=SyncV4PagePaginationArray[object],
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
            model=object,
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
        return AsyncResourceGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourceGroupsResourceWithStreamingResponse:
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
    ) -> AsyncPaginator[object, AsyncV4PagePaginationArray[object]]:
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
            page=AsyncV4PagePaginationArray[object],
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
            model=object,
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
