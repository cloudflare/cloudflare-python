# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
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
from ...types.resource_sharing import resource_list_params, resource_create_params, resource_update_params
from ...types.resource_sharing.resource_get_response import ResourceGetResponse
from ...types.resource_sharing.resource_list_response import ResourceListResponse
from ...types.resource_sharing.resource_create_response import ResourceCreateResponse
from ...types.resource_sharing.resource_delete_response import ResourceDeleteResponse
from ...types.resource_sharing.resource_update_response import ResourceUpdateResponse

__all__ = ["ResourcesResource", "AsyncResourcesResource"]


class ResourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ResourcesResourceWithStreamingResponse(self)

    def create(
        self,
        share_id: str,
        *,
        account_id: str,
        meta: object,
        resource_account_id: str,
        resource_id: str,
        resource_type: Literal["custom-ruleset", "widget"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ResourceCreateResponse]:
        """
        Create a new share resource

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          meta: Resource Metadata.

          resource_account_id: Account identifier.

          resource_id: Share Resource identifier.

          resource_type: Resource Type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return self._post(
            f"/accounts/{account_id}/shares/{share_id}/resources",
            body=maybe_transform(
                {
                    "meta": meta,
                    "resource_account_id": resource_account_id,
                    "resource_id": resource_id,
                    "resource_type": resource_type,
                },
                resource_create_params.ResourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceCreateResponse]], ResultWrapper[ResourceCreateResponse]),
        )

    def update(
        self,
        resource_id: str,
        *,
        account_id: str,
        share_id: str,
        meta: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ResourceUpdateResponse]:
        """
        Update is not immediate, an updated share resource object with a new status will
        be returned.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          resource_id: Share Resource identifier.

          meta: Resource Metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return self._put(
            f"/accounts/{account_id}/shares/{share_id}/resources/{resource_id}",
            body=maybe_transform({"meta": meta}, resource_update_params.ResourceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceUpdateResponse]], ResultWrapper[ResourceUpdateResponse]),
        )

    def list(
        self,
        share_id: str,
        *,
        account_id: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        resource_type: Literal["custom-ruleset", "widget"] | NotGiven = NOT_GIVEN,
        status: Literal["active", "deleting", "deleted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[ResourceListResponse]:
        """
        List share resources by share ID.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          page: Page number.

          per_page: Number of objects to return per page.

          resource_type: Filter share resources by resource_type.

          status: Filter share resources by status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/shares/{share_id}/resources",
            page=SyncV4PagePaginationArray[ResourceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "resource_type": resource_type,
                        "status": status,
                    },
                    resource_list_params.ResourceListParams,
                ),
            ),
            model=ResourceListResponse,
        )

    def delete(
        self,
        resource_id: str,
        *,
        account_id: str,
        share_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ResourceDeleteResponse]:
        """
        Deletion is not immediate, an updated share resource object with a new status
        will be returned.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          resource_id: Share Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return self._delete(
            f"/accounts/{account_id}/shares/{share_id}/resources/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceDeleteResponse]], ResultWrapper[ResourceDeleteResponse]),
        )

    def get(
        self,
        resource_id: str,
        *,
        account_id: str,
        share_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ResourceGetResponse]:
        """
        Get share resource by ID.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          resource_id: Share Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return self._get(
            f"/accounts/{account_id}/shares/{share_id}/resources/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceGetResponse]], ResultWrapper[ResourceGetResponse]),
        )


class AsyncResourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncResourcesResourceWithStreamingResponse(self)

    async def create(
        self,
        share_id: str,
        *,
        account_id: str,
        meta: object,
        resource_account_id: str,
        resource_id: str,
        resource_type: Literal["custom-ruleset", "widget"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ResourceCreateResponse]:
        """
        Create a new share resource

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          meta: Resource Metadata.

          resource_account_id: Account identifier.

          resource_id: Share Resource identifier.

          resource_type: Resource Type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return await self._post(
            f"/accounts/{account_id}/shares/{share_id}/resources",
            body=await async_maybe_transform(
                {
                    "meta": meta,
                    "resource_account_id": resource_account_id,
                    "resource_id": resource_id,
                    "resource_type": resource_type,
                },
                resource_create_params.ResourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceCreateResponse]], ResultWrapper[ResourceCreateResponse]),
        )

    async def update(
        self,
        resource_id: str,
        *,
        account_id: str,
        share_id: str,
        meta: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ResourceUpdateResponse]:
        """
        Update is not immediate, an updated share resource object with a new status will
        be returned.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          resource_id: Share Resource identifier.

          meta: Resource Metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return await self._put(
            f"/accounts/{account_id}/shares/{share_id}/resources/{resource_id}",
            body=await async_maybe_transform({"meta": meta}, resource_update_params.ResourceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceUpdateResponse]], ResultWrapper[ResourceUpdateResponse]),
        )

    def list(
        self,
        share_id: str,
        *,
        account_id: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        resource_type: Literal["custom-ruleset", "widget"] | NotGiven = NOT_GIVEN,
        status: Literal["active", "deleting", "deleted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ResourceListResponse, AsyncV4PagePaginationArray[ResourceListResponse]]:
        """
        List share resources by share ID.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          page: Page number.

          per_page: Number of objects to return per page.

          resource_type: Filter share resources by resource_type.

          status: Filter share resources by status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/shares/{share_id}/resources",
            page=AsyncV4PagePaginationArray[ResourceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "resource_type": resource_type,
                        "status": status,
                    },
                    resource_list_params.ResourceListParams,
                ),
            ),
            model=ResourceListResponse,
        )

    async def delete(
        self,
        resource_id: str,
        *,
        account_id: str,
        share_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ResourceDeleteResponse]:
        """
        Deletion is not immediate, an updated share resource object with a new status
        will be returned.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          resource_id: Share Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/shares/{share_id}/resources/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceDeleteResponse]], ResultWrapper[ResourceDeleteResponse]),
        )

    async def get(
        self,
        resource_id: str,
        *,
        account_id: str,
        share_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ResourceGetResponse]:
        """
        Get share resource by ID.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          resource_id: Share Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return await self._get(
            f"/accounts/{account_id}/shares/{share_id}/resources/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ResourceGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResourceGetResponse]], ResultWrapper[ResourceGetResponse]),
        )


class ResourcesResourceWithRawResponse:
    def __init__(self, resources: ResourcesResource) -> None:
        self._resources = resources

        self.create = to_raw_response_wrapper(
            resources.create,
        )
        self.update = to_raw_response_wrapper(
            resources.update,
        )
        self.list = to_raw_response_wrapper(
            resources.list,
        )
        self.delete = to_raw_response_wrapper(
            resources.delete,
        )
        self.get = to_raw_response_wrapper(
            resources.get,
        )


class AsyncResourcesResourceWithRawResponse:
    def __init__(self, resources: AsyncResourcesResource) -> None:
        self._resources = resources

        self.create = async_to_raw_response_wrapper(
            resources.create,
        )
        self.update = async_to_raw_response_wrapper(
            resources.update,
        )
        self.list = async_to_raw_response_wrapper(
            resources.list,
        )
        self.delete = async_to_raw_response_wrapper(
            resources.delete,
        )
        self.get = async_to_raw_response_wrapper(
            resources.get,
        )


class ResourcesResourceWithStreamingResponse:
    def __init__(self, resources: ResourcesResource) -> None:
        self._resources = resources

        self.create = to_streamed_response_wrapper(
            resources.create,
        )
        self.update = to_streamed_response_wrapper(
            resources.update,
        )
        self.list = to_streamed_response_wrapper(
            resources.list,
        )
        self.delete = to_streamed_response_wrapper(
            resources.delete,
        )
        self.get = to_streamed_response_wrapper(
            resources.get,
        )


class AsyncResourcesResourceWithStreamingResponse:
    def __init__(self, resources: AsyncResourcesResource) -> None:
        self._resources = resources

        self.create = async_to_streamed_response_wrapper(
            resources.create,
        )
        self.update = async_to_streamed_response_wrapper(
            resources.update,
        )
        self.list = async_to_streamed_response_wrapper(
            resources.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            resources.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            resources.get,
        )
