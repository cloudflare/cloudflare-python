# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.workers import (
    RouteGetResponse,
    RouteDeleteResponse,
    RouteUpdateResponse,
    RouteWorkerRoutesListRoutesResponse,
    RouteWorkerRoutesCreateRouteResponse,
    route_update_params,
    route_worker_routes_create_route_params,
)

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
        route_id: str,
        *,
        zone_id: str,
        pattern: str,
        script: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteUpdateResponse:
        """
        Updates the URL pattern or Worker associated with a route.

        Args:
          zone_id: Identifier

          route_id: Identifier

          script: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return self._put(
            f"/zones/{zone_id}/workers/routes/{route_id}",
            body=maybe_transform(
                {
                    "pattern": pattern,
                    "script": script,
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
        route_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteDeleteResponse:
        """
        Deletes a route.

        Args:
          zone_id: Identifier

          route_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return cast(
            RouteDeleteResponse,
            self._delete(
                f"/zones/{zone_id}/workers/routes/{route_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RouteDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        route_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteGetResponse:
        """
        Returns information about a route, including URL pattern and Worker.

        Args:
          zone_id: Identifier

          route_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return self._get(
            f"/zones/{zone_id}/workers/routes/{route_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteGetResponse], ResultWrapper[RouteGetResponse]),
        )

    def worker_routes_create_route(
        self,
        zone_id: str,
        *,
        pattern: str,
        script: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteWorkerRoutesCreateRouteResponse:
        """
        Creates a route that maps a URL pattern to a Worker.

        Args:
          zone_id: Identifier

          script: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            RouteWorkerRoutesCreateRouteResponse,
            self._post(
                f"/zones/{zone_id}/workers/routes",
                body=maybe_transform(
                    {
                        "pattern": pattern,
                        "script": script,
                    },
                    route_worker_routes_create_route_params.RouteWorkerRoutesCreateRouteParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RouteWorkerRoutesCreateRouteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def worker_routes_list_routes(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteWorkerRoutesListRoutesResponse:
        """
        Returns routes for a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/workers/routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteWorkerRoutesListRoutesResponse], ResultWrapper[RouteWorkerRoutesListRoutesResponse]),
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
        route_id: str,
        *,
        zone_id: str,
        pattern: str,
        script: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteUpdateResponse:
        """
        Updates the URL pattern or Worker associated with a route.

        Args:
          zone_id: Identifier

          route_id: Identifier

          script: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return await self._put(
            f"/zones/{zone_id}/workers/routes/{route_id}",
            body=maybe_transform(
                {
                    "pattern": pattern,
                    "script": script,
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
        route_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteDeleteResponse:
        """
        Deletes a route.

        Args:
          zone_id: Identifier

          route_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return cast(
            RouteDeleteResponse,
            await self._delete(
                f"/zones/{zone_id}/workers/routes/{route_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RouteDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        route_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteGetResponse:
        """
        Returns information about a route, including URL pattern and Worker.

        Args:
          zone_id: Identifier

          route_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return await self._get(
            f"/zones/{zone_id}/workers/routes/{route_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteGetResponse], ResultWrapper[RouteGetResponse]),
        )

    async def worker_routes_create_route(
        self,
        zone_id: str,
        *,
        pattern: str,
        script: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteWorkerRoutesCreateRouteResponse:
        """
        Creates a route that maps a URL pattern to a Worker.

        Args:
          zone_id: Identifier

          script: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            RouteWorkerRoutesCreateRouteResponse,
            await self._post(
                f"/zones/{zone_id}/workers/routes",
                body=maybe_transform(
                    {
                        "pattern": pattern,
                        "script": script,
                    },
                    route_worker_routes_create_route_params.RouteWorkerRoutesCreateRouteParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RouteWorkerRoutesCreateRouteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def worker_routes_list_routes(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteWorkerRoutesListRoutesResponse:
        """
        Returns routes for a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/workers/routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RouteWorkerRoutesListRoutesResponse], ResultWrapper[RouteWorkerRoutesListRoutesResponse]),
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
        self.worker_routes_create_route = to_raw_response_wrapper(
            routes.worker_routes_create_route,
        )
        self.worker_routes_list_routes = to_raw_response_wrapper(
            routes.worker_routes_list_routes,
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
        self.worker_routes_create_route = async_to_raw_response_wrapper(
            routes.worker_routes_create_route,
        )
        self.worker_routes_list_routes = async_to_raw_response_wrapper(
            routes.worker_routes_list_routes,
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
        self.worker_routes_create_route = to_streamed_response_wrapper(
            routes.worker_routes_create_route,
        )
        self.worker_routes_list_routes = to_streamed_response_wrapper(
            routes.worker_routes_list_routes,
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
        self.worker_routes_create_route = async_to_streamed_response_wrapper(
            routes.worker_routes_create_route,
        )
        self.worker_routes_list_routes = async_to_streamed_response_wrapper(
            routes.worker_routes_list_routes,
        )
