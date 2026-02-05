# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.networks import (
    hostname_route_edit_params,
    hostname_route_list_params,
    hostname_route_create_params,
)
from ....types.zero_trust.networks.hostname_route import HostnameRoute

__all__ = ["HostnameRoutesResource", "AsyncHostnameRoutesResource"]


class HostnameRoutesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HostnameRoutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return HostnameRoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostnameRoutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return HostnameRoutesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        comment: str | Omit = omit,
        hostname: str | Omit = omit,
        tunnel_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostnameRoute:
        """
        Create a hostname route.

        Args:
          account_id: Cloudflare account ID

          comment: An optional description of the hostname route.

          hostname: The hostname of the route.

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/zerotrust/routes/hostname",
            body=maybe_transform(
                {
                    "comment": comment,
                    "hostname": hostname,
                    "tunnel_id": tunnel_id,
                },
                hostname_route_create_params.HostnameRouteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[HostnameRoute]._unwrapper,
            ),
            cast_to=cast(Type[HostnameRoute], ResultWrapper[HostnameRoute]),
        )

    def list(
        self,
        *,
        account_id: str,
        id: str | Omit = omit,
        comment: str | Omit = omit,
        existed_at: str | Omit = omit,
        hostname: str | Omit = omit,
        is_deleted: bool | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        tunnel_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[HostnameRoute]:
        """
        Lists and filters hostname routes in an account.

        Args:
          account_id: Cloudflare account ID

          id: The hostname route ID.

          comment: If set, only list hostname routes with the given comment.

          existed_at: If provided, include only resources that were created (and not deleted) before
              this time. URL encoded.

          hostname: If set, only list hostname routes that contain a substring of the given value,
              the filter is case-insensitive.

          is_deleted: If `true`, only return deleted hostname routes. If `false`, exclude deleted
              hostname routes.

          page: Page number of paginated results.

          per_page: Number of results to display.

          tunnel_id: If set, only list hostname routes that point to a specific tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/zerotrust/routes/hostname",
            page=SyncV4PagePaginationArray[HostnameRoute],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "comment": comment,
                        "existed_at": existed_at,
                        "hostname": hostname,
                        "is_deleted": is_deleted,
                        "page": page,
                        "per_page": per_page,
                        "tunnel_id": tunnel_id,
                    },
                    hostname_route_list_params.HostnameRouteListParams,
                ),
            ),
            model=HostnameRoute,
        )

    def delete(
        self,
        hostname_route_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostnameRoute:
        """
        Delete a hostname route.

        Args:
          account_id: Cloudflare account ID

          hostname_route_id: The hostname route ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hostname_route_id:
            raise ValueError(f"Expected a non-empty value for `hostname_route_id` but received {hostname_route_id!r}")
        return self._delete(
            f"/accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[HostnameRoute]._unwrapper,
            ),
            cast_to=cast(Type[HostnameRoute], ResultWrapper[HostnameRoute]),
        )

    def edit(
        self,
        hostname_route_id: str,
        *,
        account_id: str,
        comment: str | Omit = omit,
        hostname: str | Omit = omit,
        tunnel_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostnameRoute:
        """
        Updates a hostname route.

        Args:
          account_id: Cloudflare account ID

          hostname_route_id: The hostname route ID.

          comment: An optional description of the hostname route.

          hostname: The hostname of the route.

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hostname_route_id:
            raise ValueError(f"Expected a non-empty value for `hostname_route_id` but received {hostname_route_id!r}")
        return self._patch(
            f"/accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}",
            body=maybe_transform(
                {
                    "comment": comment,
                    "hostname": hostname,
                    "tunnel_id": tunnel_id,
                },
                hostname_route_edit_params.HostnameRouteEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[HostnameRoute]._unwrapper,
            ),
            cast_to=cast(Type[HostnameRoute], ResultWrapper[HostnameRoute]),
        )

    def get(
        self,
        hostname_route_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostnameRoute:
        """
        Get a hostname route.

        Args:
          account_id: Cloudflare account ID

          hostname_route_id: The hostname route ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hostname_route_id:
            raise ValueError(f"Expected a non-empty value for `hostname_route_id` but received {hostname_route_id!r}")
        return self._get(
            f"/accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[HostnameRoute]._unwrapper,
            ),
            cast_to=cast(Type[HostnameRoute], ResultWrapper[HostnameRoute]),
        )


class AsyncHostnameRoutesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHostnameRoutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHostnameRoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostnameRoutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncHostnameRoutesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        comment: str | Omit = omit,
        hostname: str | Omit = omit,
        tunnel_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostnameRoute:
        """
        Create a hostname route.

        Args:
          account_id: Cloudflare account ID

          comment: An optional description of the hostname route.

          hostname: The hostname of the route.

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/zerotrust/routes/hostname",
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "hostname": hostname,
                    "tunnel_id": tunnel_id,
                },
                hostname_route_create_params.HostnameRouteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[HostnameRoute]._unwrapper,
            ),
            cast_to=cast(Type[HostnameRoute], ResultWrapper[HostnameRoute]),
        )

    def list(
        self,
        *,
        account_id: str,
        id: str | Omit = omit,
        comment: str | Omit = omit,
        existed_at: str | Omit = omit,
        hostname: str | Omit = omit,
        is_deleted: bool | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        tunnel_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[HostnameRoute, AsyncV4PagePaginationArray[HostnameRoute]]:
        """
        Lists and filters hostname routes in an account.

        Args:
          account_id: Cloudflare account ID

          id: The hostname route ID.

          comment: If set, only list hostname routes with the given comment.

          existed_at: If provided, include only resources that were created (and not deleted) before
              this time. URL encoded.

          hostname: If set, only list hostname routes that contain a substring of the given value,
              the filter is case-insensitive.

          is_deleted: If `true`, only return deleted hostname routes. If `false`, exclude deleted
              hostname routes.

          page: Page number of paginated results.

          per_page: Number of results to display.

          tunnel_id: If set, only list hostname routes that point to a specific tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/zerotrust/routes/hostname",
            page=AsyncV4PagePaginationArray[HostnameRoute],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "comment": comment,
                        "existed_at": existed_at,
                        "hostname": hostname,
                        "is_deleted": is_deleted,
                        "page": page,
                        "per_page": per_page,
                        "tunnel_id": tunnel_id,
                    },
                    hostname_route_list_params.HostnameRouteListParams,
                ),
            ),
            model=HostnameRoute,
        )

    async def delete(
        self,
        hostname_route_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostnameRoute:
        """
        Delete a hostname route.

        Args:
          account_id: Cloudflare account ID

          hostname_route_id: The hostname route ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hostname_route_id:
            raise ValueError(f"Expected a non-empty value for `hostname_route_id` but received {hostname_route_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[HostnameRoute]._unwrapper,
            ),
            cast_to=cast(Type[HostnameRoute], ResultWrapper[HostnameRoute]),
        )

    async def edit(
        self,
        hostname_route_id: str,
        *,
        account_id: str,
        comment: str | Omit = omit,
        hostname: str | Omit = omit,
        tunnel_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostnameRoute:
        """
        Updates a hostname route.

        Args:
          account_id: Cloudflare account ID

          hostname_route_id: The hostname route ID.

          comment: An optional description of the hostname route.

          hostname: The hostname of the route.

          tunnel_id: UUID of the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hostname_route_id:
            raise ValueError(f"Expected a non-empty value for `hostname_route_id` but received {hostname_route_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}",
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "hostname": hostname,
                    "tunnel_id": tunnel_id,
                },
                hostname_route_edit_params.HostnameRouteEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[HostnameRoute]._unwrapper,
            ),
            cast_to=cast(Type[HostnameRoute], ResultWrapper[HostnameRoute]),
        )

    async def get(
        self,
        hostname_route_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostnameRoute:
        """
        Get a hostname route.

        Args:
          account_id: Cloudflare account ID

          hostname_route_id: The hostname route ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hostname_route_id:
            raise ValueError(f"Expected a non-empty value for `hostname_route_id` but received {hostname_route_id!r}")
        return await self._get(
            f"/accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[HostnameRoute]._unwrapper,
            ),
            cast_to=cast(Type[HostnameRoute], ResultWrapper[HostnameRoute]),
        )


class HostnameRoutesResourceWithRawResponse:
    def __init__(self, hostname_routes: HostnameRoutesResource) -> None:
        self._hostname_routes = hostname_routes

        self.create = to_raw_response_wrapper(
            hostname_routes.create,
        )
        self.list = to_raw_response_wrapper(
            hostname_routes.list,
        )
        self.delete = to_raw_response_wrapper(
            hostname_routes.delete,
        )
        self.edit = to_raw_response_wrapper(
            hostname_routes.edit,
        )
        self.get = to_raw_response_wrapper(
            hostname_routes.get,
        )


class AsyncHostnameRoutesResourceWithRawResponse:
    def __init__(self, hostname_routes: AsyncHostnameRoutesResource) -> None:
        self._hostname_routes = hostname_routes

        self.create = async_to_raw_response_wrapper(
            hostname_routes.create,
        )
        self.list = async_to_raw_response_wrapper(
            hostname_routes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            hostname_routes.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            hostname_routes.edit,
        )
        self.get = async_to_raw_response_wrapper(
            hostname_routes.get,
        )


class HostnameRoutesResourceWithStreamingResponse:
    def __init__(self, hostname_routes: HostnameRoutesResource) -> None:
        self._hostname_routes = hostname_routes

        self.create = to_streamed_response_wrapper(
            hostname_routes.create,
        )
        self.list = to_streamed_response_wrapper(
            hostname_routes.list,
        )
        self.delete = to_streamed_response_wrapper(
            hostname_routes.delete,
        )
        self.edit = to_streamed_response_wrapper(
            hostname_routes.edit,
        )
        self.get = to_streamed_response_wrapper(
            hostname_routes.get,
        )


class AsyncHostnameRoutesResourceWithStreamingResponse:
    def __init__(self, hostname_routes: AsyncHostnameRoutesResource) -> None:
        self._hostname_routes = hostname_routes

        self.create = async_to_streamed_response_wrapper(
            hostname_routes.create,
        )
        self.list = async_to_streamed_response_wrapper(
            hostname_routes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            hostname_routes.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            hostname_routes.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            hostname_routes.get,
        )
