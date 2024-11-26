# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast
from typing_extensions import Literal

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
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.resource_sharing import resource_sharing_list_params, resource_sharing_create_params
from ...types.resource_sharing.resource_sharing_list_response import ResourceSharingListResponse
from ...types.resource_sharing.resource_sharing_create_response import ResourceSharingCreateResponse

__all__ = ["ResourceSharingResource", "AsyncResourceSharingResource"]


class ResourceSharingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourceSharingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ResourceSharingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourceSharingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ResourceSharingResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        recipients: Iterable[resource_sharing_create_params.Recipient],
        resources: Iterable[resource_sharing_create_params.Resource],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ResourceSharingCreateResponse]:
        """
        Create a new share

        Args:
          account_id: Account identifier.

          name: The name of the share.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/shares",
            body=maybe_transform(
                {
                    "name": name,
                    "recipients": recipients,
                    "resources": resources,
                },
                resource_sharing_create_params.ResourceSharingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceSharingCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceSharingCreateResponse]], ResultWrapper[ResourceSharingCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        kind: Literal["sent", "received"] | NotGiven = NOT_GIVEN,
        order: Literal["name", "created"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "deleting", "deleted"] | NotGiven = NOT_GIVEN,
        target_type: Literal["account", "organization"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[ResourceSharingListResponse]:
        """
        Lists all account shares.

        Args:
          account_id: Account identifier.

          direction: Direction to sort objects.

          kind: Filter shares by kind.

          order: Order shares by values in the given field.

          page: Page number.

          per_page: Number of objects to return per page.

          status: Filter shares by status.

          target_type: Filter shares by target_type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/shares",
            page=SyncV4PagePaginationArray[ResourceSharingListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "kind": kind,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                        "target_type": target_type,
                    },
                    resource_sharing_list_params.ResourceSharingListParams,
                ),
            ),
            model=ResourceSharingListResponse,
        )


class AsyncResourceSharingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourceSharingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResourceSharingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourceSharingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncResourceSharingResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        recipients: Iterable[resource_sharing_create_params.Recipient],
        resources: Iterable[resource_sharing_create_params.Resource],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ResourceSharingCreateResponse]:
        """
        Create a new share

        Args:
          account_id: Account identifier.

          name: The name of the share.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/shares",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "recipients": recipients,
                    "resources": resources,
                },
                resource_sharing_create_params.ResourceSharingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceSharingCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceSharingCreateResponse]], ResultWrapper[ResourceSharingCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        kind: Literal["sent", "received"] | NotGiven = NOT_GIVEN,
        order: Literal["name", "created"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "deleting", "deleted"] | NotGiven = NOT_GIVEN,
        target_type: Literal["account", "organization"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ResourceSharingListResponse, AsyncV4PagePaginationArray[ResourceSharingListResponse]]:
        """
        Lists all account shares.

        Args:
          account_id: Account identifier.

          direction: Direction to sort objects.

          kind: Filter shares by kind.

          order: Order shares by values in the given field.

          page: Page number.

          per_page: Number of objects to return per page.

          status: Filter shares by status.

          target_type: Filter shares by target_type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/shares",
            page=AsyncV4PagePaginationArray[ResourceSharingListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "kind": kind,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                        "target_type": target_type,
                    },
                    resource_sharing_list_params.ResourceSharingListParams,
                ),
            ),
            model=ResourceSharingListResponse,
        )


class ResourceSharingResourceWithRawResponse:
    def __init__(self, resource_sharing: ResourceSharingResource) -> None:
        self._resource_sharing = resource_sharing

        self.create = to_raw_response_wrapper(
            resource_sharing.create,
        )
        self.list = to_raw_response_wrapper(
            resource_sharing.list,
        )


class AsyncResourceSharingResourceWithRawResponse:
    def __init__(self, resource_sharing: AsyncResourceSharingResource) -> None:
        self._resource_sharing = resource_sharing

        self.create = async_to_raw_response_wrapper(
            resource_sharing.create,
        )
        self.list = async_to_raw_response_wrapper(
            resource_sharing.list,
        )


class ResourceSharingResourceWithStreamingResponse:
    def __init__(self, resource_sharing: ResourceSharingResource) -> None:
        self._resource_sharing = resource_sharing

        self.create = to_streamed_response_wrapper(
            resource_sharing.create,
        )
        self.list = to_streamed_response_wrapper(
            resource_sharing.list,
        )


class AsyncResourceSharingResourceWithStreamingResponse:
    def __init__(self, resource_sharing: AsyncResourceSharingResource) -> None:
        self._resource_sharing = resource_sharing

        self.create = async_to_streamed_response_wrapper(
            resource_sharing.create,
        )
        self.list = async_to_streamed_response_wrapper(
            resource_sharing.list,
        )
