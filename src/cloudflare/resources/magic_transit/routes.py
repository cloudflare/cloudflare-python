# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

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
from ..._base_client import make_request_options
from ...types.magic_transit import route_create_params, route_update_params, route_bulk_update_params
from ...types.magic_transit.scope_param import ScopeParam
from ...types.magic_transit.route_get_response import RouteGetResponse
from ...types.magic_transit.route_list_response import RouteListResponse
from ...types.magic_transit.route_empty_response import RouteEmptyResponse
from ...types.magic_transit.route_create_response import RouteCreateResponse
from ...types.magic_transit.route_delete_response import RouteDeleteResponse
from ...types.magic_transit.route_update_response import RouteUpdateResponse
from ...types.magic_transit.route_bulk_update_response import RouteBulkUpdateResponse

__all__ = ["RoutesResource", "AsyncRoutesResource"]


class RoutesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RoutesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteCreateResponse:
        """Creates a new Magic static route.

        Use `?validate_only=true` as an optional query
        parameter to run validation only without persisting changes.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/routes",
            body=maybe_transform(body, route_create_params.RouteCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RouteCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteCreateResponse], ResultWrapper[RouteCreateResponse]),
        )

    def update(
        self,
        route_id: str,
        *,
        account_id: str,
        nexthop: str,
        prefix: str,
        priority: int,
        description: str | NotGiven = NOT_GIVEN,
        scope: ScopeParam | NotGiven = NOT_GIVEN,
        weight: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteUpdateResponse:
        """Update a specific Magic static route.

        Use `?validate_only=true` as an optional
        query parameter to run validation only without persisting changes.

        Args:
          account_id: Identifier

          route_id: Identifier

          nexthop: The next-hop IP Address for the static route.

          prefix: IP Prefix in Classless Inter-Domain Routing format.

          priority: Priority of the static route.

          description: An optional human provided description of the static route.

          scope: Used only for ECMP routes.

          weight: Optional weight of the ECMP scope - if provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return self._put(
            f"/accounts/{account_id}/magic/routes/{route_id}",
            body=maybe_transform(
                {
                    "nexthop": nexthop,
                    "prefix": prefix,
                    "priority": priority,
                    "description": description,
                    "scope": scope,
                    "weight": weight,
                },
                route_update_params.RouteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RouteUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteUpdateResponse], ResultWrapper[RouteUpdateResponse]),
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
    ) -> RouteListResponse:
        """
        List all Magic static routes.

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
            f"/accounts/{account_id}/magic/routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RouteListResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteListResponse], ResultWrapper[RouteListResponse]),
        )

    def delete(
        self,
        route_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteDeleteResponse:
        """
        Disable and remove a specific Magic static route.

        Args:
          account_id: Identifier

          route_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return self._delete(
            f"/accounts/{account_id}/magic/routes/{route_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RouteDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteDeleteResponse], ResultWrapper[RouteDeleteResponse]),
        )

    def bulk_update(
        self,
        *,
        account_id: str,
        routes: Iterable[route_bulk_update_params.Route],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteBulkUpdateResponse:
        """Update multiple Magic static routes.

        Use `?validate_only=true` as an optional
        query parameter to run validation only without persisting changes. Only fields
        for a route that need to be changed need be provided.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/magic/routes",
            body=maybe_transform({"routes": routes}, route_bulk_update_params.RouteBulkUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RouteBulkUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteBulkUpdateResponse], ResultWrapper[RouteBulkUpdateResponse]),
        )

    def empty(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteEmptyResponse:
        """
        Delete multiple Magic static routes.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            f"/accounts/{account_id}/magic/routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RouteEmptyResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteEmptyResponse], ResultWrapper[RouteEmptyResponse]),
        )

    def get(
        self,
        route_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteGetResponse:
        """
        Get a specific Magic static route.

        Args:
          account_id: Identifier

          route_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/routes/{route_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RouteGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteGetResponse], ResultWrapper[RouteGetResponse]),
        )


class AsyncRoutesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRoutesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteCreateResponse:
        """Creates a new Magic static route.

        Use `?validate_only=true` as an optional query
        parameter to run validation only without persisting changes.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/routes",
            body=await async_maybe_transform(body, route_create_params.RouteCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RouteCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteCreateResponse], ResultWrapper[RouteCreateResponse]),
        )

    async def update(
        self,
        route_id: str,
        *,
        account_id: str,
        nexthop: str,
        prefix: str,
        priority: int,
        description: str | NotGiven = NOT_GIVEN,
        scope: ScopeParam | NotGiven = NOT_GIVEN,
        weight: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteUpdateResponse:
        """Update a specific Magic static route.

        Use `?validate_only=true` as an optional
        query parameter to run validation only without persisting changes.

        Args:
          account_id: Identifier

          route_id: Identifier

          nexthop: The next-hop IP Address for the static route.

          prefix: IP Prefix in Classless Inter-Domain Routing format.

          priority: Priority of the static route.

          description: An optional human provided description of the static route.

          scope: Used only for ECMP routes.

          weight: Optional weight of the ECMP scope - if provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/routes/{route_id}",
            body=await async_maybe_transform(
                {
                    "nexthop": nexthop,
                    "prefix": prefix,
                    "priority": priority,
                    "description": description,
                    "scope": scope,
                    "weight": weight,
                },
                route_update_params.RouteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RouteUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteUpdateResponse], ResultWrapper[RouteUpdateResponse]),
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
    ) -> RouteListResponse:
        """
        List all Magic static routes.

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
            f"/accounts/{account_id}/magic/routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RouteListResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteListResponse], ResultWrapper[RouteListResponse]),
        )

    async def delete(
        self,
        route_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteDeleteResponse:
        """
        Disable and remove a specific Magic static route.

        Args:
          account_id: Identifier

          route_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/magic/routes/{route_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RouteDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteDeleteResponse], ResultWrapper[RouteDeleteResponse]),
        )

    async def bulk_update(
        self,
        *,
        account_id: str,
        routes: Iterable[route_bulk_update_params.Route],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteBulkUpdateResponse:
        """Update multiple Magic static routes.

        Use `?validate_only=true` as an optional
        query parameter to run validation only without persisting changes. Only fields
        for a route that need to be changed need be provided.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/routes",
            body=await async_maybe_transform({"routes": routes}, route_bulk_update_params.RouteBulkUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RouteBulkUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteBulkUpdateResponse], ResultWrapper[RouteBulkUpdateResponse]),
        )

    async def empty(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteEmptyResponse:
        """
        Delete multiple Magic static routes.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/magic/routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RouteEmptyResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteEmptyResponse], ResultWrapper[RouteEmptyResponse]),
        )

    async def get(
        self,
        route_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteGetResponse:
        """
        Get a specific Magic static route.

        Args:
          account_id: Identifier

          route_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/routes/{route_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RouteGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[RouteGetResponse], ResultWrapper[RouteGetResponse]),
        )


class RoutesResourceWithRawResponse:
    def __init__(self, routes: RoutesResource) -> None:
        self._routes = routes

        self.create = to_raw_response_wrapper(
            routes.create,
        )
        self.update = to_raw_response_wrapper(
            routes.update,
        )
        self.list = to_raw_response_wrapper(
            routes.list,
        )
        self.delete = to_raw_response_wrapper(
            routes.delete,
        )
        self.bulk_update = to_raw_response_wrapper(
            routes.bulk_update,
        )
        self.empty = to_raw_response_wrapper(
            routes.empty,
        )
        self.get = to_raw_response_wrapper(
            routes.get,
        )


class AsyncRoutesResourceWithRawResponse:
    def __init__(self, routes: AsyncRoutesResource) -> None:
        self._routes = routes

        self.create = async_to_raw_response_wrapper(
            routes.create,
        )
        self.update = async_to_raw_response_wrapper(
            routes.update,
        )
        self.list = async_to_raw_response_wrapper(
            routes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            routes.delete,
        )
        self.bulk_update = async_to_raw_response_wrapper(
            routes.bulk_update,
        )
        self.empty = async_to_raw_response_wrapper(
            routes.empty,
        )
        self.get = async_to_raw_response_wrapper(
            routes.get,
        )


class RoutesResourceWithStreamingResponse:
    def __init__(self, routes: RoutesResource) -> None:
        self._routes = routes

        self.create = to_streamed_response_wrapper(
            routes.create,
        )
        self.update = to_streamed_response_wrapper(
            routes.update,
        )
        self.list = to_streamed_response_wrapper(
            routes.list,
        )
        self.delete = to_streamed_response_wrapper(
            routes.delete,
        )
        self.bulk_update = to_streamed_response_wrapper(
            routes.bulk_update,
        )
        self.empty = to_streamed_response_wrapper(
            routes.empty,
        )
        self.get = to_streamed_response_wrapper(
            routes.get,
        )


class AsyncRoutesResourceWithStreamingResponse:
    def __init__(self, routes: AsyncRoutesResource) -> None:
        self._routes = routes

        self.create = async_to_streamed_response_wrapper(
            routes.create,
        )
        self.update = async_to_streamed_response_wrapper(
            routes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            routes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            routes.delete,
        )
        self.bulk_update = async_to_streamed_response_wrapper(
            routes.bulk_update,
        )
        self.empty = async_to_streamed_response_wrapper(
            routes.empty,
        )
        self.get = async_to_streamed_response_wrapper(
            routes.get,
        )
