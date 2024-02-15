# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.magics import (
    RouteUpdateResponse,
    RouteDeleteResponse,
    RouteGetResponse,
    RouteMagicStaticRoutesCreateRoutesResponse,
    RouteMagicStaticRoutesListRoutesResponse,
    RouteMagicStaticRoutesUpdateManyRoutesResponse,
    route_update_params,
    route_magic_static_routes_update_many_routes_params,
)

from typing import Type, Iterable

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.magics import route_update_params
from ...types.magics import route_magic_static_routes_create_routes_params
from ...types.magics import route_magic_static_routes_update_many_routes_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Routes", "AsyncRoutes"]


class Routes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutesWithRawResponse:
        return RoutesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutesWithStreamingResponse:
        return RoutesWithStreamingResponse(self)

    def update(
        self,
        route_identifier: str,
        *,
        account_identifier: str,
        nexthop: str,
        prefix: str,
        priority: int,
        description: str | NotGiven = NOT_GIVEN,
        scope: route_update_params.Scope | NotGiven = NOT_GIVEN,
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
          account_identifier: Identifier

          route_identifier: Identifier

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
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not route_identifier:
            raise ValueError(f"Expected a non-empty value for `route_identifier` but received {route_identifier!r}")
        return self._put(
            f"/accounts/{account_identifier}/magic/routes/{route_identifier}",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteUpdateResponse], ResultWrapper[RouteUpdateResponse]),
        )

    def delete(
        self,
        route_identifier: str,
        *,
        account_identifier: str,
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
          account_identifier: Identifier

          route_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not route_identifier:
            raise ValueError(f"Expected a non-empty value for `route_identifier` but received {route_identifier!r}")
        return self._delete(
            f"/accounts/{account_identifier}/magic/routes/{route_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteDeleteResponse], ResultWrapper[RouteDeleteResponse]),
        )

    def get(
        self,
        route_identifier: str,
        *,
        account_identifier: str,
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
          account_identifier: Identifier

          route_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not route_identifier:
            raise ValueError(f"Expected a non-empty value for `route_identifier` but received {route_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/magic/routes/{route_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteGetResponse], ResultWrapper[RouteGetResponse]),
        )

    def magic_static_routes_create_routes(
        self,
        account_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteMagicStaticRoutesCreateRoutesResponse:
        """Creates a new Magic static route.

        Use `?validate_only=true` as an optional query
        parameter to run validation only without persisting changes.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/magic/routes",
            body=maybe_transform(
                body, route_magic_static_routes_create_routes_params.RouteMagicStaticRoutesCreateRoutesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RouteMagicStaticRoutesCreateRoutesResponse],
                ResultWrapper[RouteMagicStaticRoutesCreateRoutesResponse],
            ),
        )

    def magic_static_routes_list_routes(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteMagicStaticRoutesListRoutesResponse:
        """
        List all Magic static routes.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/magic/routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RouteMagicStaticRoutesListRoutesResponse], ResultWrapper[RouteMagicStaticRoutesListRoutesResponse]
            ),
        )

    def magic_static_routes_update_many_routes(
        self,
        account_identifier: str,
        *,
        routes: Iterable[route_magic_static_routes_update_many_routes_params.Route],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteMagicStaticRoutesUpdateManyRoutesResponse:
        """Update multiple Magic static routes.

        Use `?validate_only=true` as an optional
        query parameter to run validation only without persisting changes. Only fields
        for a route that need to be changed need be provided.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._put(
            f"/accounts/{account_identifier}/magic/routes",
            body=maybe_transform(
                {"routes": routes},
                route_magic_static_routes_update_many_routes_params.RouteMagicStaticRoutesUpdateManyRoutesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RouteMagicStaticRoutesUpdateManyRoutesResponse],
                ResultWrapper[RouteMagicStaticRoutesUpdateManyRoutesResponse],
            ),
        )


class AsyncRoutes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutesWithRawResponse:
        return AsyncRoutesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutesWithStreamingResponse:
        return AsyncRoutesWithStreamingResponse(self)

    async def update(
        self,
        route_identifier: str,
        *,
        account_identifier: str,
        nexthop: str,
        prefix: str,
        priority: int,
        description: str | NotGiven = NOT_GIVEN,
        scope: route_update_params.Scope | NotGiven = NOT_GIVEN,
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
          account_identifier: Identifier

          route_identifier: Identifier

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
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not route_identifier:
            raise ValueError(f"Expected a non-empty value for `route_identifier` but received {route_identifier!r}")
        return await self._put(
            f"/accounts/{account_identifier}/magic/routes/{route_identifier}",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteUpdateResponse], ResultWrapper[RouteUpdateResponse]),
        )

    async def delete(
        self,
        route_identifier: str,
        *,
        account_identifier: str,
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
          account_identifier: Identifier

          route_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not route_identifier:
            raise ValueError(f"Expected a non-empty value for `route_identifier` but received {route_identifier!r}")
        return await self._delete(
            f"/accounts/{account_identifier}/magic/routes/{route_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteDeleteResponse], ResultWrapper[RouteDeleteResponse]),
        )

    async def get(
        self,
        route_identifier: str,
        *,
        account_identifier: str,
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
          account_identifier: Identifier

          route_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not route_identifier:
            raise ValueError(f"Expected a non-empty value for `route_identifier` but received {route_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/magic/routes/{route_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteGetResponse], ResultWrapper[RouteGetResponse]),
        )

    async def magic_static_routes_create_routes(
        self,
        account_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteMagicStaticRoutesCreateRoutesResponse:
        """Creates a new Magic static route.

        Use `?validate_only=true` as an optional query
        parameter to run validation only without persisting changes.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/magic/routes",
            body=maybe_transform(
                body, route_magic_static_routes_create_routes_params.RouteMagicStaticRoutesCreateRoutesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RouteMagicStaticRoutesCreateRoutesResponse],
                ResultWrapper[RouteMagicStaticRoutesCreateRoutesResponse],
            ),
        )

    async def magic_static_routes_list_routes(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteMagicStaticRoutesListRoutesResponse:
        """
        List all Magic static routes.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/magic/routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RouteMagicStaticRoutesListRoutesResponse], ResultWrapper[RouteMagicStaticRoutesListRoutesResponse]
            ),
        )

    async def magic_static_routes_update_many_routes(
        self,
        account_identifier: str,
        *,
        routes: Iterable[route_magic_static_routes_update_many_routes_params.Route],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteMagicStaticRoutesUpdateManyRoutesResponse:
        """Update multiple Magic static routes.

        Use `?validate_only=true` as an optional
        query parameter to run validation only without persisting changes. Only fields
        for a route that need to be changed need be provided.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._put(
            f"/accounts/{account_identifier}/magic/routes",
            body=maybe_transform(
                {"routes": routes},
                route_magic_static_routes_update_many_routes_params.RouteMagicStaticRoutesUpdateManyRoutesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RouteMagicStaticRoutesUpdateManyRoutesResponse],
                ResultWrapper[RouteMagicStaticRoutesUpdateManyRoutesResponse],
            ),
        )


class RoutesWithRawResponse:
    def __init__(self, routes: Routes) -> None:
        self._routes = routes

        self.update = to_raw_response_wrapper(
            routes.update,
        )
        self.delete = to_raw_response_wrapper(
            routes.delete,
        )
        self.get = to_raw_response_wrapper(
            routes.get,
        )
        self.magic_static_routes_create_routes = to_raw_response_wrapper(
            routes.magic_static_routes_create_routes,
        )
        self.magic_static_routes_list_routes = to_raw_response_wrapper(
            routes.magic_static_routes_list_routes,
        )
        self.magic_static_routes_update_many_routes = to_raw_response_wrapper(
            routes.magic_static_routes_update_many_routes,
        )


class AsyncRoutesWithRawResponse:
    def __init__(self, routes: AsyncRoutes) -> None:
        self._routes = routes

        self.update = async_to_raw_response_wrapper(
            routes.update,
        )
        self.delete = async_to_raw_response_wrapper(
            routes.delete,
        )
        self.get = async_to_raw_response_wrapper(
            routes.get,
        )
        self.magic_static_routes_create_routes = async_to_raw_response_wrapper(
            routes.magic_static_routes_create_routes,
        )
        self.magic_static_routes_list_routes = async_to_raw_response_wrapper(
            routes.magic_static_routes_list_routes,
        )
        self.magic_static_routes_update_many_routes = async_to_raw_response_wrapper(
            routes.magic_static_routes_update_many_routes,
        )


class RoutesWithStreamingResponse:
    def __init__(self, routes: Routes) -> None:
        self._routes = routes

        self.update = to_streamed_response_wrapper(
            routes.update,
        )
        self.delete = to_streamed_response_wrapper(
            routes.delete,
        )
        self.get = to_streamed_response_wrapper(
            routes.get,
        )
        self.magic_static_routes_create_routes = to_streamed_response_wrapper(
            routes.magic_static_routes_create_routes,
        )
        self.magic_static_routes_list_routes = to_streamed_response_wrapper(
            routes.magic_static_routes_list_routes,
        )
        self.magic_static_routes_update_many_routes = to_streamed_response_wrapper(
            routes.magic_static_routes_update_many_routes,
        )


class AsyncRoutesWithStreamingResponse:
    def __init__(self, routes: AsyncRoutes) -> None:
        self._routes = routes

        self.update = async_to_streamed_response_wrapper(
            routes.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            routes.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            routes.get,
        )
        self.magic_static_routes_create_routes = async_to_streamed_response_wrapper(
            routes.magic_static_routes_create_routes,
        )
        self.magic_static_routes_list_routes = async_to_streamed_response_wrapper(
            routes.magic_static_routes_list_routes,
        )
        self.magic_static_routes_update_many_routes = async_to_streamed_response_wrapper(
            routes.magic_static_routes_update_many_routes,
        )
