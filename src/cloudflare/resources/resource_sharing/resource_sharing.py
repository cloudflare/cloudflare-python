# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .resources import (
    ResourcesResource,
    AsyncResourcesResource,
    ResourcesResourceWithRawResponse,
    AsyncResourcesResourceWithRawResponse,
    ResourcesResourceWithStreamingResponse,
    AsyncResourcesResourceWithStreamingResponse,
)
from .recipients import (
    RecipientsResource,
    AsyncRecipientsResource,
    RecipientsResourceWithRawResponse,
    AsyncRecipientsResourceWithRawResponse,
    RecipientsResourceWithStreamingResponse,
    AsyncRecipientsResourceWithStreamingResponse,
)
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
from ...types.resource_sharing import (
    resource_sharing_get_params,
    resource_sharing_list_params,
    resource_sharing_create_params,
    resource_sharing_update_params,
)
from ...types.resource_sharing.resource_sharing_get_response import ResourceSharingGetResponse
from ...types.resource_sharing.resource_sharing_list_response import ResourceSharingListResponse
from ...types.resource_sharing.resource_sharing_create_response import ResourceSharingCreateResponse
from ...types.resource_sharing.resource_sharing_delete_response import ResourceSharingDeleteResponse
from ...types.resource_sharing.resource_sharing_update_response import ResourceSharingUpdateResponse

__all__ = ["ResourceSharingResource", "AsyncResourceSharingResource"]


class ResourceSharingResource(SyncAPIResource):
    @cached_property
    def recipients(self) -> RecipientsResource:
        return RecipientsResource(self._client)

    @cached_property
    def resources(self) -> ResourcesResource:
        return ResourcesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ResourceSharingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def update(
        self,
        share_id: str,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ResourceSharingUpdateResponse]:
        """
        Updating is not immediate, an updated share object with a new status will be
        returned.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          name: The name of the share.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return self._put(
            f"/accounts/{account_id}/shares/{share_id}",
            body=maybe_transform({"name": name}, resource_sharing_update_params.ResourceSharingUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceSharingUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceSharingUpdateResponse]], ResultWrapper[ResourceSharingUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        include_recipient_counts: bool | Omit = omit,
        include_resources: bool | Omit = omit,
        kind: Literal["sent", "received"] | Omit = omit,
        order: Literal["name", "created"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        resource_types: List[
            Literal[
                "custom-ruleset",
                "widget",
                "gateway-policy",
                "gateway-destination-ip",
                "gateway-block-page-settings",
                "gateway-extended-email-matching",
            ]
        ]
        | Omit = omit,
        status: Literal["active", "deleting", "deleted"] | Omit = omit,
        target_type: Literal["account", "organization"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[ResourceSharingListResponse]:
        """
        Lists all account shares.

        Args:
          account_id: Account identifier.

          direction: Direction to sort objects.

          include_recipient_counts: Include recipient counts in the response.

          include_resources: Include resources in the response.

          kind: Filter shares by kind.

          order: Order shares by values in the given field.

          page: Page number.

          per_page: Number of objects to return per page.

          resource_types: Filter share resources by resource_types.

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
                        "include_recipient_counts": include_recipient_counts,
                        "include_resources": include_resources,
                        "kind": kind,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "resource_types": resource_types,
                        "status": status,
                        "target_type": target_type,
                    },
                    resource_sharing_list_params.ResourceSharingListParams,
                ),
            ),
            model=ResourceSharingListResponse,
        )

    def delete(
        self,
        share_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ResourceSharingDeleteResponse]:
        """
        Deletion is not immediate, an updated share object with a new status will be
        returned.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return self._delete(
            f"/accounts/{account_id}/shares/{share_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceSharingDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceSharingDeleteResponse]], ResultWrapper[ResourceSharingDeleteResponse]),
        )

    def get(
        self,
        share_id: str,
        *,
        account_id: str,
        include_recipient_counts: bool | Omit = omit,
        include_resources: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ResourceSharingGetResponse]:
        """
        Fetches share by ID.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          include_recipient_counts: Include recipient counts in the response.

          include_resources: Include resources in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return self._get(
            f"/accounts/{account_id}/shares/{share_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_recipient_counts": include_recipient_counts,
                        "include_resources": include_resources,
                    },
                    resource_sharing_get_params.ResourceSharingGetParams,
                ),
                post_parser=ResultWrapper[Optional[ResourceSharingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceSharingGetResponse]], ResultWrapper[ResourceSharingGetResponse]),
        )


class AsyncResourceSharingResource(AsyncAPIResource):
    @cached_property
    def recipients(self) -> AsyncRecipientsResource:
        return AsyncRecipientsResource(self._client)

    @cached_property
    def resources(self) -> AsyncResourcesResource:
        return AsyncResourcesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncResourceSharingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    async def update(
        self,
        share_id: str,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ResourceSharingUpdateResponse]:
        """
        Updating is not immediate, an updated share object with a new status will be
        returned.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          name: The name of the share.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return await self._put(
            f"/accounts/{account_id}/shares/{share_id}",
            body=await async_maybe_transform(
                {"name": name}, resource_sharing_update_params.ResourceSharingUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceSharingUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceSharingUpdateResponse]], ResultWrapper[ResourceSharingUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        include_recipient_counts: bool | Omit = omit,
        include_resources: bool | Omit = omit,
        kind: Literal["sent", "received"] | Omit = omit,
        order: Literal["name", "created"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        resource_types: List[
            Literal[
                "custom-ruleset",
                "widget",
                "gateway-policy",
                "gateway-destination-ip",
                "gateway-block-page-settings",
                "gateway-extended-email-matching",
            ]
        ]
        | Omit = omit,
        status: Literal["active", "deleting", "deleted"] | Omit = omit,
        target_type: Literal["account", "organization"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ResourceSharingListResponse, AsyncV4PagePaginationArray[ResourceSharingListResponse]]:
        """
        Lists all account shares.

        Args:
          account_id: Account identifier.

          direction: Direction to sort objects.

          include_recipient_counts: Include recipient counts in the response.

          include_resources: Include resources in the response.

          kind: Filter shares by kind.

          order: Order shares by values in the given field.

          page: Page number.

          per_page: Number of objects to return per page.

          resource_types: Filter share resources by resource_types.

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
                        "include_recipient_counts": include_recipient_counts,
                        "include_resources": include_resources,
                        "kind": kind,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "resource_types": resource_types,
                        "status": status,
                        "target_type": target_type,
                    },
                    resource_sharing_list_params.ResourceSharingListParams,
                ),
            ),
            model=ResourceSharingListResponse,
        )

    async def delete(
        self,
        share_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ResourceSharingDeleteResponse]:
        """
        Deletion is not immediate, an updated share object with a new status will be
        returned.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/shares/{share_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceSharingDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceSharingDeleteResponse]], ResultWrapper[ResourceSharingDeleteResponse]),
        )

    async def get(
        self,
        share_id: str,
        *,
        account_id: str,
        include_recipient_counts: bool | Omit = omit,
        include_resources: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ResourceSharingGetResponse]:
        """
        Fetches share by ID.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          include_recipient_counts: Include recipient counts in the response.

          include_resources: Include resources in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return await self._get(
            f"/accounts/{account_id}/shares/{share_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_recipient_counts": include_recipient_counts,
                        "include_resources": include_resources,
                    },
                    resource_sharing_get_params.ResourceSharingGetParams,
                ),
                post_parser=ResultWrapper[Optional[ResourceSharingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceSharingGetResponse]], ResultWrapper[ResourceSharingGetResponse]),
        )


class ResourceSharingResourceWithRawResponse:
    def __init__(self, resource_sharing: ResourceSharingResource) -> None:
        self._resource_sharing = resource_sharing

        self.create = to_raw_response_wrapper(
            resource_sharing.create,
        )
        self.update = to_raw_response_wrapper(
            resource_sharing.update,
        )
        self.list = to_raw_response_wrapper(
            resource_sharing.list,
        )
        self.delete = to_raw_response_wrapper(
            resource_sharing.delete,
        )
        self.get = to_raw_response_wrapper(
            resource_sharing.get,
        )

    @cached_property
    def recipients(self) -> RecipientsResourceWithRawResponse:
        return RecipientsResourceWithRawResponse(self._resource_sharing.recipients)

    @cached_property
    def resources(self) -> ResourcesResourceWithRawResponse:
        return ResourcesResourceWithRawResponse(self._resource_sharing.resources)


class AsyncResourceSharingResourceWithRawResponse:
    def __init__(self, resource_sharing: AsyncResourceSharingResource) -> None:
        self._resource_sharing = resource_sharing

        self.create = async_to_raw_response_wrapper(
            resource_sharing.create,
        )
        self.update = async_to_raw_response_wrapper(
            resource_sharing.update,
        )
        self.list = async_to_raw_response_wrapper(
            resource_sharing.list,
        )
        self.delete = async_to_raw_response_wrapper(
            resource_sharing.delete,
        )
        self.get = async_to_raw_response_wrapper(
            resource_sharing.get,
        )

    @cached_property
    def recipients(self) -> AsyncRecipientsResourceWithRawResponse:
        return AsyncRecipientsResourceWithRawResponse(self._resource_sharing.recipients)

    @cached_property
    def resources(self) -> AsyncResourcesResourceWithRawResponse:
        return AsyncResourcesResourceWithRawResponse(self._resource_sharing.resources)


class ResourceSharingResourceWithStreamingResponse:
    def __init__(self, resource_sharing: ResourceSharingResource) -> None:
        self._resource_sharing = resource_sharing

        self.create = to_streamed_response_wrapper(
            resource_sharing.create,
        )
        self.update = to_streamed_response_wrapper(
            resource_sharing.update,
        )
        self.list = to_streamed_response_wrapper(
            resource_sharing.list,
        )
        self.delete = to_streamed_response_wrapper(
            resource_sharing.delete,
        )
        self.get = to_streamed_response_wrapper(
            resource_sharing.get,
        )

    @cached_property
    def recipients(self) -> RecipientsResourceWithStreamingResponse:
        return RecipientsResourceWithStreamingResponse(self._resource_sharing.recipients)

    @cached_property
    def resources(self) -> ResourcesResourceWithStreamingResponse:
        return ResourcesResourceWithStreamingResponse(self._resource_sharing.resources)


class AsyncResourceSharingResourceWithStreamingResponse:
    def __init__(self, resource_sharing: AsyncResourceSharingResource) -> None:
        self._resource_sharing = resource_sharing

        self.create = async_to_streamed_response_wrapper(
            resource_sharing.create,
        )
        self.update = async_to_streamed_response_wrapper(
            resource_sharing.update,
        )
        self.list = async_to_streamed_response_wrapper(
            resource_sharing.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            resource_sharing.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            resource_sharing.get,
        )

    @cached_property
    def recipients(self) -> AsyncRecipientsResourceWithStreamingResponse:
        return AsyncRecipientsResourceWithStreamingResponse(self._resource_sharing.recipients)

    @cached_property
    def resources(self) -> AsyncResourcesResourceWithStreamingResponse:
        return AsyncResourcesResourceWithStreamingResponse(self._resource_sharing.resources)
