# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.intel.indicator_feeds import permission_create_params, permission_delete_params
from ....types.intel.indicator_feeds.permission_list_response import PermissionListResponse
from ....types.intel.indicator_feeds.permission_create_response import PermissionCreateResponse
from ....types.intel.indicator_feeds.permission_delete_response import PermissionDeleteResponse

__all__ = ["PermissionsResource", "AsyncPermissionsResource"]


class PermissionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PermissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PermissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PermissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PermissionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        account_tag: str | NotGiven = NOT_GIVEN,
        feed_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PermissionCreateResponse]:
        """
        Grant permission to indicator feed

        Args:
          account_id: Identifier

          account_tag: The Cloudflare account tag of the account to change permissions on

          feed_id: The ID of the feed to add/remove permissions on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/intel/indicator-feeds/permissions/add",
            body=maybe_transform(
                {
                    "account_tag": account_tag,
                    "feed_id": feed_id,
                },
                permission_create_params.PermissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PermissionCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PermissionCreateResponse]], ResultWrapper[PermissionCreateResponse]),
        )

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
    ) -> Optional[PermissionListResponse]:
        """
        List indicator feed permissions

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/indicator-feeds/permissions/view",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PermissionListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PermissionListResponse]], ResultWrapper[PermissionListResponse]),
        )

    def delete(
        self,
        *,
        account_id: str,
        account_tag: str | NotGiven = NOT_GIVEN,
        feed_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PermissionDeleteResponse]:
        """
        Revoke permission to indicator feed

        Args:
          account_id: Identifier

          account_tag: The Cloudflare account tag of the account to change permissions on

          feed_id: The ID of the feed to add/remove permissions on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/intel/indicator-feeds/permissions/remove",
            body=maybe_transform(
                {
                    "account_tag": account_tag,
                    "feed_id": feed_id,
                },
                permission_delete_params.PermissionDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PermissionDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PermissionDeleteResponse]], ResultWrapper[PermissionDeleteResponse]),
        )


class AsyncPermissionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPermissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPermissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPermissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPermissionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        account_tag: str | NotGiven = NOT_GIVEN,
        feed_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PermissionCreateResponse]:
        """
        Grant permission to indicator feed

        Args:
          account_id: Identifier

          account_tag: The Cloudflare account tag of the account to change permissions on

          feed_id: The ID of the feed to add/remove permissions on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/intel/indicator-feeds/permissions/add",
            body=await async_maybe_transform(
                {
                    "account_tag": account_tag,
                    "feed_id": feed_id,
                },
                permission_create_params.PermissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PermissionCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PermissionCreateResponse]], ResultWrapper[PermissionCreateResponse]),
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PermissionListResponse]:
        """
        List indicator feed permissions

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/indicator-feeds/permissions/view",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PermissionListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PermissionListResponse]], ResultWrapper[PermissionListResponse]),
        )

    async def delete(
        self,
        *,
        account_id: str,
        account_tag: str | NotGiven = NOT_GIVEN,
        feed_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PermissionDeleteResponse]:
        """
        Revoke permission to indicator feed

        Args:
          account_id: Identifier

          account_tag: The Cloudflare account tag of the account to change permissions on

          feed_id: The ID of the feed to add/remove permissions on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/intel/indicator-feeds/permissions/remove",
            body=await async_maybe_transform(
                {
                    "account_tag": account_tag,
                    "feed_id": feed_id,
                },
                permission_delete_params.PermissionDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PermissionDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PermissionDeleteResponse]], ResultWrapper[PermissionDeleteResponse]),
        )


class PermissionsResourceWithRawResponse:
    def __init__(self, permissions: PermissionsResource) -> None:
        self._permissions = permissions

        self.create = to_raw_response_wrapper(
            permissions.create,
        )
        self.list = to_raw_response_wrapper(
            permissions.list,
        )
        self.delete = to_raw_response_wrapper(
            permissions.delete,
        )


class AsyncPermissionsResourceWithRawResponse:
    def __init__(self, permissions: AsyncPermissionsResource) -> None:
        self._permissions = permissions

        self.create = async_to_raw_response_wrapper(
            permissions.create,
        )
        self.list = async_to_raw_response_wrapper(
            permissions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            permissions.delete,
        )


class PermissionsResourceWithStreamingResponse:
    def __init__(self, permissions: PermissionsResource) -> None:
        self._permissions = permissions

        self.create = to_streamed_response_wrapper(
            permissions.create,
        )
        self.list = to_streamed_response_wrapper(
            permissions.list,
        )
        self.delete = to_streamed_response_wrapper(
            permissions.delete,
        )


class AsyncPermissionsResourceWithStreamingResponse:
    def __init__(self, permissions: AsyncPermissionsResource) -> None:
        self._permissions = permissions

        self.create = async_to_streamed_response_wrapper(
            permissions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            permissions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            permissions.delete,
        )
