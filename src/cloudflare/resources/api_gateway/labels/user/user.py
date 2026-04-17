# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import AsyncPaginator, make_request_options
from .resources.resources import (
    ResourcesResource,
    AsyncResourcesResource,
    ResourcesResourceWithRawResponse,
    AsyncResourcesResourceWithRawResponse,
    ResourcesResourceWithStreamingResponse,
    AsyncResourcesResourceWithStreamingResponse,
)
from .....types.api_gateway.labels import user_get_params, user_edit_params, user_update_params, user_bulk_create_params
from .....types.api_gateway.labels.user_get_response import UserGetResponse
from .....types.api_gateway.labels.user_edit_response import UserEditResponse
from .....types.api_gateway.labels.user_delete_response import UserDeleteResponse
from .....types.api_gateway.labels.user_update_response import UserUpdateResponse
from .....types.api_gateway.labels.user_bulk_create_response import UserBulkCreateResponse
from .....types.api_gateway.labels.user_bulk_delete_response import UserBulkDeleteResponse

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    @cached_property
    def resources(self) -> ResourcesResource:
        return ResourcesResource(self._client)

    @cached_property
    def with_raw_response(self) -> UserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UserResourceWithStreamingResponse(self)

    def update(
        self,
        name: str,
        *,
        zone_id: str | None = None,
        description: str | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserUpdateResponse:
        """
        Update all fields on a label

        Args:
          zone_id: Identifier.

          name: The name of the label

          description: The description of the label

          metadata: Metadata for the label

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._put(
            path_template("/zones/{zone_id}/api_gateway/labels/user/{name}", zone_id=zone_id, name=name),
            body=maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UserUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[UserUpdateResponse], ResultWrapper[UserUpdateResponse]),
        )

    def delete(
        self,
        name: str,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserDeleteResponse:
        """
        Delete user label

        Args:
          zone_id: Identifier.

          name: The name of the label

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._delete(
            path_template("/zones/{zone_id}/api_gateway/labels/user/{name}", zone_id=zone_id, name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UserDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[UserDeleteResponse], ResultWrapper[UserDeleteResponse]),
        )

    def bulk_create(
        self,
        *,
        zone_id: str | None = None,
        body: Iterable[user_bulk_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[UserBulkCreateResponse]:
        """
        Create user labels

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/api_gateway/labels/user", zone_id=zone_id),
            page=SyncSinglePage[UserBulkCreateResponse],
            body=maybe_transform(body, Iterable[user_bulk_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=UserBulkCreateResponse,
            method="post",
        )

    def bulk_delete(
        self,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[UserBulkDeleteResponse]:
        """
        Delete user labels

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/api_gateway/labels/user", zone_id=zone_id),
            page=SyncSinglePage[UserBulkDeleteResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=UserBulkDeleteResponse,
            method="delete",
        )

    def edit(
        self,
        name: str,
        *,
        zone_id: str | None = None,
        description: str | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserEditResponse:
        """
        Update certain fields on a label

        Args:
          zone_id: Identifier.

          name: The name of the label

          description: The description of the label

          metadata: Metadata for the label

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._patch(
            path_template("/zones/{zone_id}/api_gateway/labels/user/{name}", zone_id=zone_id, name=name),
            body=maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                },
                user_edit_params.UserEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UserEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[UserEditResponse], ResultWrapper[UserEditResponse]),
        )

    def get(
        self,
        name: str,
        *,
        zone_id: str | None = None,
        with_mapped_resource_counts: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGetResponse:
        """
        Retrieve user label

        Args:
          zone_id: Identifier.

          name: The name of the label

          with_mapped_resource_counts: Include `mapped_resources` for each label

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            path_template("/zones/{zone_id}/api_gateway/labels/user/{name}", zone_id=zone_id, name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"with_mapped_resource_counts": with_mapped_resource_counts}, user_get_params.UserGetParams
                ),
                post_parser=ResultWrapper[UserGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[UserGetResponse], ResultWrapper[UserGetResponse]),
        )


class AsyncUserResource(AsyncAPIResource):
    @cached_property
    def resources(self) -> AsyncResourcesResource:
        return AsyncResourcesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUserResourceWithStreamingResponse(self)

    async def update(
        self,
        name: str,
        *,
        zone_id: str | None = None,
        description: str | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserUpdateResponse:
        """
        Update all fields on a label

        Args:
          zone_id: Identifier.

          name: The name of the label

          description: The description of the label

          metadata: Metadata for the label

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._put(
            path_template("/zones/{zone_id}/api_gateway/labels/user/{name}", zone_id=zone_id, name=name),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UserUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[UserUpdateResponse], ResultWrapper[UserUpdateResponse]),
        )

    async def delete(
        self,
        name: str,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserDeleteResponse:
        """
        Delete user label

        Args:
          zone_id: Identifier.

          name: The name of the label

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._delete(
            path_template("/zones/{zone_id}/api_gateway/labels/user/{name}", zone_id=zone_id, name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UserDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[UserDeleteResponse], ResultWrapper[UserDeleteResponse]),
        )

    def bulk_create(
        self,
        *,
        zone_id: str | None = None,
        body: Iterable[user_bulk_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[UserBulkCreateResponse, AsyncSinglePage[UserBulkCreateResponse]]:
        """
        Create user labels

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/api_gateway/labels/user", zone_id=zone_id),
            page=AsyncSinglePage[UserBulkCreateResponse],
            body=maybe_transform(body, Iterable[user_bulk_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=UserBulkCreateResponse,
            method="post",
        )

    def bulk_delete(
        self,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[UserBulkDeleteResponse, AsyncSinglePage[UserBulkDeleteResponse]]:
        """
        Delete user labels

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/api_gateway/labels/user", zone_id=zone_id),
            page=AsyncSinglePage[UserBulkDeleteResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=UserBulkDeleteResponse,
            method="delete",
        )

    async def edit(
        self,
        name: str,
        *,
        zone_id: str | None = None,
        description: str | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserEditResponse:
        """
        Update certain fields on a label

        Args:
          zone_id: Identifier.

          name: The name of the label

          description: The description of the label

          metadata: Metadata for the label

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._patch(
            path_template("/zones/{zone_id}/api_gateway/labels/user/{name}", zone_id=zone_id, name=name),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                },
                user_edit_params.UserEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UserEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[UserEditResponse], ResultWrapper[UserEditResponse]),
        )

    async def get(
        self,
        name: str,
        *,
        zone_id: str | None = None,
        with_mapped_resource_counts: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGetResponse:
        """
        Retrieve user label

        Args:
          zone_id: Identifier.

          name: The name of the label

          with_mapped_resource_counts: Include `mapped_resources` for each label

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            path_template("/zones/{zone_id}/api_gateway/labels/user/{name}", zone_id=zone_id, name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"with_mapped_resource_counts": with_mapped_resource_counts}, user_get_params.UserGetParams
                ),
                post_parser=ResultWrapper[UserGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[UserGetResponse], ResultWrapper[UserGetResponse]),
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.update = to_raw_response_wrapper(
            user.update,
        )
        self.delete = to_raw_response_wrapper(
            user.delete,
        )
        self.bulk_create = to_raw_response_wrapper(
            user.bulk_create,
        )
        self.bulk_delete = to_raw_response_wrapper(
            user.bulk_delete,
        )
        self.edit = to_raw_response_wrapper(
            user.edit,
        )
        self.get = to_raw_response_wrapper(
            user.get,
        )

    @cached_property
    def resources(self) -> ResourcesResourceWithRawResponse:
        return ResourcesResourceWithRawResponse(self._user.resources)


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.update = async_to_raw_response_wrapper(
            user.update,
        )
        self.delete = async_to_raw_response_wrapper(
            user.delete,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            user.bulk_create,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            user.bulk_delete,
        )
        self.edit = async_to_raw_response_wrapper(
            user.edit,
        )
        self.get = async_to_raw_response_wrapper(
            user.get,
        )

    @cached_property
    def resources(self) -> AsyncResourcesResourceWithRawResponse:
        return AsyncResourcesResourceWithRawResponse(self._user.resources)


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.update = to_streamed_response_wrapper(
            user.update,
        )
        self.delete = to_streamed_response_wrapper(
            user.delete,
        )
        self.bulk_create = to_streamed_response_wrapper(
            user.bulk_create,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            user.bulk_delete,
        )
        self.edit = to_streamed_response_wrapper(
            user.edit,
        )
        self.get = to_streamed_response_wrapper(
            user.get,
        )

    @cached_property
    def resources(self) -> ResourcesResourceWithStreamingResponse:
        return ResourcesResourceWithStreamingResponse(self._user.resources)


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.update = async_to_streamed_response_wrapper(
            user.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            user.delete,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            user.bulk_create,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            user.bulk_delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            user.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            user.get,
        )

    @cached_property
    def resources(self) -> AsyncResourcesResourceWithStreamingResponse:
        return AsyncResourcesResourceWithStreamingResponse(self._user.resources)
