# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .health import HealthResource, AsyncHealthResource

from ...._compat import cached_property

from .references import ReferencesResource, AsyncReferencesResource

from ....types.load_balancers.pool import Pool

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options, AsyncPaginator

from typing import Type, Iterable, Optional, List

from ....types.load_balancers.origin_param import OriginParam

from ....types.load_balancers.load_shedding_param import LoadSheddingParam

from ....types.load_balancers.notification_filter_param import NotificationFilterParam

from ....types.load_balancers.origin_steering_param import OriginSteeringParam

from ....types.load_balancers.check_region import CheckRegion

from ....pagination import SyncSinglePage, AsyncSinglePage

from ....types.load_balancers.pool_delete_response import PoolDeleteResponse

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.load_balancers import pool_create_params
from ....types.load_balancers import pool_update_params
from ....types.load_balancers import pool_list_params
from ....types.load_balancers import pool_edit_params
from ....types.load_balancers import LoadShedding
from ....types.load_balancers import NotificationFilter
from ....types.load_balancers import OriginSteering
from ....types.load_balancers import LoadShedding
from ....types.load_balancers import NotificationFilter
from ....types.load_balancers import OriginSteering
from ....types.load_balancers import LoadShedding
from ....types.load_balancers import NotificationFilter
from ....types.load_balancers import OriginSteering
from .health import (
    HealthResource,
    AsyncHealthResource,
    HealthResourceWithRawResponse,
    AsyncHealthResourceWithRawResponse,
    HealthResourceWithStreamingResponse,
    AsyncHealthResourceWithStreamingResponse,
)
from .references import (
    ReferencesResource,
    AsyncReferencesResource,
    ReferencesResourceWithRawResponse,
    AsyncReferencesResourceWithRawResponse,
    ReferencesResourceWithStreamingResponse,
    AsyncReferencesResourceWithStreamingResponse,
)
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

__all__ = ["PoolsResource", "AsyncPoolsResource"]


class PoolsResource(SyncAPIResource):
    @cached_property
    def health(self) -> HealthResource:
        return HealthResource(self._client)

    @cached_property
    def references(self) -> ReferencesResource:
        return ReferencesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PoolsResourceWithRawResponse:
        return PoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoolsResourceWithStreamingResponse:
        return PoolsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        origins: Iterable[OriginParam],
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        latitude: float | NotGiven = NOT_GIVEN,
        load_shedding: LoadSheddingParam | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        minimum_origins: int | NotGiven = NOT_GIVEN,
        monitor: str | NotGiven = NOT_GIVEN,
        notification_email: str | NotGiven = NOT_GIVEN,
        notification_filter: Optional[NotificationFilterParam] | NotGiven = NOT_GIVEN,
        origin_steering: OriginSteeringParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pool:
        """
        Create a new pool.

        Args:
          account_id: Identifier

          name: A short name (tag) for the pool. Only alphanumeric characters, hyphens, and
              underscores are allowed.

          origins: The list of origins within this pool. Traffic directed at this pool is balanced
              across all currently healthy origins, provided the pool itself is healthy.

          description: A human-readable description of the pool.

          enabled: Whether to enable (the default) or disable this pool. Disabled pools will not
              receive traffic and are excluded from health checks. Disabling a pool will cause
              any load balancers using it to failover to the next pool (if any).

          latitude: The latitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, longitude must also be set.

          load_shedding: Configures load shedding policies and percentages for the pool.

          longitude: The longitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, latitude must also be set.

          minimum_origins: The minimum number of origins that must be healthy for this pool to serve
              traffic. If the number of healthy origins falls below this number, the pool will
              be marked unhealthy and will failover to the next available pool.

          monitor: The ID of the Monitor to use for checking the health of origins within this
              pool.

          notification_email: This field is now deprecated. It has been moved to Cloudflare's Centralized
              Notification service
              https://developers.cloudflare.com/fundamentals/notifications/. The email address
              to send health status notifications to. This can be an individual mailbox or a
              mailing list. Multiple emails can be supplied as a comma delimited list.

          notification_filter: Filter pool and origin health notifications by resource type or health status.
              Use null to reset.

          origin_steering: Configures origin steering for the pool. Controls how origins are selected for
              new sessions and traffic without session affinity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/load_balancers/pools",
            body=maybe_transform(
                {
                    "name": name,
                    "origins": origins,
                    "description": description,
                    "enabled": enabled,
                    "latitude": latitude,
                    "load_shedding": load_shedding,
                    "longitude": longitude,
                    "minimum_origins": minimum_origins,
                    "monitor": monitor,
                    "notification_email": notification_email,
                    "notification_filter": notification_filter,
                    "origin_steering": origin_steering,
                },
                pool_create_params.PoolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Pool]._unwrapper,
            ),
            cast_to=cast(Type[Pool], ResultWrapper[Pool]),
        )

    def update(
        self,
        pool_id: str,
        *,
        account_id: str,
        name: str,
        origins: Iterable[OriginParam],
        check_regions: Optional[List[CheckRegion]] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        latitude: float | NotGiven = NOT_GIVEN,
        load_shedding: LoadSheddingParam | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        minimum_origins: int | NotGiven = NOT_GIVEN,
        monitor: str | NotGiven = NOT_GIVEN,
        notification_email: str | NotGiven = NOT_GIVEN,
        notification_filter: Optional[NotificationFilterParam] | NotGiven = NOT_GIVEN,
        origin_steering: OriginSteeringParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pool:
        """
        Modify a configured pool.

        Args:
          account_id: Identifier

          name: A short name (tag) for the pool. Only alphanumeric characters, hyphens, and
              underscores are allowed.

          origins: The list of origins within this pool. Traffic directed at this pool is balanced
              across all currently healthy origins, provided the pool itself is healthy.

          check_regions: A list of regions from which to run health checks. Null means every Cloudflare
              data center.

          description: A human-readable description of the pool.

          enabled: Whether to enable (the default) or disable this pool. Disabled pools will not
              receive traffic and are excluded from health checks. Disabling a pool will cause
              any load balancers using it to failover to the next pool (if any).

          latitude: The latitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, longitude must also be set.

          load_shedding: Configures load shedding policies and percentages for the pool.

          longitude: The longitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, latitude must also be set.

          minimum_origins: The minimum number of origins that must be healthy for this pool to serve
              traffic. If the number of healthy origins falls below this number, the pool will
              be marked unhealthy and will failover to the next available pool.

          monitor: The ID of the Monitor to use for checking the health of origins within this
              pool.

          notification_email: This field is now deprecated. It has been moved to Cloudflare's Centralized
              Notification service
              https://developers.cloudflare.com/fundamentals/notifications/. The email address
              to send health status notifications to. This can be an individual mailbox or a
              mailing list. Multiple emails can be supplied as a comma delimited list.

          notification_filter: Filter pool and origin health notifications by resource type or health status.
              Use null to reset.

          origin_steering: Configures origin steering for the pool. Controls how origins are selected for
              new sessions and traffic without session affinity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._put(
            f"/accounts/{account_id}/load_balancers/pools/{pool_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "origins": origins,
                    "check_regions": check_regions,
                    "description": description,
                    "enabled": enabled,
                    "latitude": latitude,
                    "load_shedding": load_shedding,
                    "longitude": longitude,
                    "minimum_origins": minimum_origins,
                    "monitor": monitor,
                    "notification_email": notification_email,
                    "notification_filter": notification_filter,
                    "origin_steering": origin_steering,
                },
                pool_update_params.PoolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Pool]._unwrapper,
            ),
            cast_to=cast(Type[Pool], ResultWrapper[Pool]),
        )

    def list(
        self,
        *,
        account_id: str,
        monitor: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Pool]:
        """
        List configured pools.

        Args:
          account_id: Identifier

          monitor: The ID of the Monitor to use for checking the health of origins within this
              pool.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/load_balancers/pools",
            page=SyncSinglePage[Pool],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"monitor": monitor}, pool_list_params.PoolListParams),
            ),
            model=Pool,
        )

    def delete(
        self,
        pool_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoolDeleteResponse:
        """
        Delete a configured pool.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._delete(
            f"/accounts/{account_id}/load_balancers/pools/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PoolDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[PoolDeleteResponse], ResultWrapper[PoolDeleteResponse]),
        )

    def edit(
        self,
        pool_id: str,
        *,
        account_id: str,
        check_regions: Optional[List[CheckRegion]] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        latitude: float | NotGiven = NOT_GIVEN,
        load_shedding: LoadSheddingParam | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        minimum_origins: int | NotGiven = NOT_GIVEN,
        monitor: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notification_email: str | NotGiven = NOT_GIVEN,
        notification_filter: Optional[NotificationFilterParam] | NotGiven = NOT_GIVEN,
        origin_steering: OriginSteeringParam | NotGiven = NOT_GIVEN,
        origins: Iterable[OriginParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pool:
        """
        Apply changes to an existing pool, overwriting the supplied properties.

        Args:
          account_id: Identifier

          check_regions: A list of regions from which to run health checks. Null means every Cloudflare
              data center.

          description: A human-readable description of the pool.

          enabled: Whether to enable (the default) or disable this pool. Disabled pools will not
              receive traffic and are excluded from health checks. Disabling a pool will cause
              any load balancers using it to failover to the next pool (if any).

          latitude: The latitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, longitude must also be set.

          load_shedding: Configures load shedding policies and percentages for the pool.

          longitude: The longitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, latitude must also be set.

          minimum_origins: The minimum number of origins that must be healthy for this pool to serve
              traffic. If the number of healthy origins falls below this number, the pool will
              be marked unhealthy and will failover to the next available pool.

          monitor: The ID of the Monitor to use for checking the health of origins within this
              pool.

          name: A short name (tag) for the pool. Only alphanumeric characters, hyphens, and
              underscores are allowed.

          notification_email: This field is now deprecated. It has been moved to Cloudflare's Centralized
              Notification service
              https://developers.cloudflare.com/fundamentals/notifications/. The email address
              to send health status notifications to. This can be an individual mailbox or a
              mailing list. Multiple emails can be supplied as a comma delimited list.

          notification_filter: Filter pool and origin health notifications by resource type or health status.
              Use null to reset.

          origin_steering: Configures origin steering for the pool. Controls how origins are selected for
              new sessions and traffic without session affinity.

          origins: The list of origins within this pool. Traffic directed at this pool is balanced
              across all currently healthy origins, provided the pool itself is healthy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._patch(
            f"/accounts/{account_id}/load_balancers/pools/{pool_id}",
            body=maybe_transform(
                {
                    "check_regions": check_regions,
                    "description": description,
                    "enabled": enabled,
                    "latitude": latitude,
                    "load_shedding": load_shedding,
                    "longitude": longitude,
                    "minimum_origins": minimum_origins,
                    "monitor": monitor,
                    "name": name,
                    "notification_email": notification_email,
                    "notification_filter": notification_filter,
                    "origin_steering": origin_steering,
                    "origins": origins,
                },
                pool_edit_params.PoolEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Pool]._unwrapper,
            ),
            cast_to=cast(Type[Pool], ResultWrapper[Pool]),
        )

    def get(
        self,
        pool_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pool:
        """
        Fetch a single configured pool.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._get(
            f"/accounts/{account_id}/load_balancers/pools/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Pool]._unwrapper,
            ),
            cast_to=cast(Type[Pool], ResultWrapper[Pool]),
        )


class AsyncPoolsResource(AsyncAPIResource):
    @cached_property
    def health(self) -> AsyncHealthResource:
        return AsyncHealthResource(self._client)

    @cached_property
    def references(self) -> AsyncReferencesResource:
        return AsyncReferencesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPoolsResourceWithRawResponse:
        return AsyncPoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoolsResourceWithStreamingResponse:
        return AsyncPoolsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        origins: Iterable[OriginParam],
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        latitude: float | NotGiven = NOT_GIVEN,
        load_shedding: LoadSheddingParam | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        minimum_origins: int | NotGiven = NOT_GIVEN,
        monitor: str | NotGiven = NOT_GIVEN,
        notification_email: str | NotGiven = NOT_GIVEN,
        notification_filter: Optional[NotificationFilterParam] | NotGiven = NOT_GIVEN,
        origin_steering: OriginSteeringParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pool:
        """
        Create a new pool.

        Args:
          account_id: Identifier

          name: A short name (tag) for the pool. Only alphanumeric characters, hyphens, and
              underscores are allowed.

          origins: The list of origins within this pool. Traffic directed at this pool is balanced
              across all currently healthy origins, provided the pool itself is healthy.

          description: A human-readable description of the pool.

          enabled: Whether to enable (the default) or disable this pool. Disabled pools will not
              receive traffic and are excluded from health checks. Disabling a pool will cause
              any load balancers using it to failover to the next pool (if any).

          latitude: The latitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, longitude must also be set.

          load_shedding: Configures load shedding policies and percentages for the pool.

          longitude: The longitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, latitude must also be set.

          minimum_origins: The minimum number of origins that must be healthy for this pool to serve
              traffic. If the number of healthy origins falls below this number, the pool will
              be marked unhealthy and will failover to the next available pool.

          monitor: The ID of the Monitor to use for checking the health of origins within this
              pool.

          notification_email: This field is now deprecated. It has been moved to Cloudflare's Centralized
              Notification service
              https://developers.cloudflare.com/fundamentals/notifications/. The email address
              to send health status notifications to. This can be an individual mailbox or a
              mailing list. Multiple emails can be supplied as a comma delimited list.

          notification_filter: Filter pool and origin health notifications by resource type or health status.
              Use null to reset.

          origin_steering: Configures origin steering for the pool. Controls how origins are selected for
              new sessions and traffic without session affinity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/load_balancers/pools",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "origins": origins,
                    "description": description,
                    "enabled": enabled,
                    "latitude": latitude,
                    "load_shedding": load_shedding,
                    "longitude": longitude,
                    "minimum_origins": minimum_origins,
                    "monitor": monitor,
                    "notification_email": notification_email,
                    "notification_filter": notification_filter,
                    "origin_steering": origin_steering,
                },
                pool_create_params.PoolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Pool]._unwrapper,
            ),
            cast_to=cast(Type[Pool], ResultWrapper[Pool]),
        )

    async def update(
        self,
        pool_id: str,
        *,
        account_id: str,
        name: str,
        origins: Iterable[OriginParam],
        check_regions: Optional[List[CheckRegion]] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        latitude: float | NotGiven = NOT_GIVEN,
        load_shedding: LoadSheddingParam | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        minimum_origins: int | NotGiven = NOT_GIVEN,
        monitor: str | NotGiven = NOT_GIVEN,
        notification_email: str | NotGiven = NOT_GIVEN,
        notification_filter: Optional[NotificationFilterParam] | NotGiven = NOT_GIVEN,
        origin_steering: OriginSteeringParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pool:
        """
        Modify a configured pool.

        Args:
          account_id: Identifier

          name: A short name (tag) for the pool. Only alphanumeric characters, hyphens, and
              underscores are allowed.

          origins: The list of origins within this pool. Traffic directed at this pool is balanced
              across all currently healthy origins, provided the pool itself is healthy.

          check_regions: A list of regions from which to run health checks. Null means every Cloudflare
              data center.

          description: A human-readable description of the pool.

          enabled: Whether to enable (the default) or disable this pool. Disabled pools will not
              receive traffic and are excluded from health checks. Disabling a pool will cause
              any load balancers using it to failover to the next pool (if any).

          latitude: The latitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, longitude must also be set.

          load_shedding: Configures load shedding policies and percentages for the pool.

          longitude: The longitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, latitude must also be set.

          minimum_origins: The minimum number of origins that must be healthy for this pool to serve
              traffic. If the number of healthy origins falls below this number, the pool will
              be marked unhealthy and will failover to the next available pool.

          monitor: The ID of the Monitor to use for checking the health of origins within this
              pool.

          notification_email: This field is now deprecated. It has been moved to Cloudflare's Centralized
              Notification service
              https://developers.cloudflare.com/fundamentals/notifications/. The email address
              to send health status notifications to. This can be an individual mailbox or a
              mailing list. Multiple emails can be supplied as a comma delimited list.

          notification_filter: Filter pool and origin health notifications by resource type or health status.
              Use null to reset.

          origin_steering: Configures origin steering for the pool. Controls how origins are selected for
              new sessions and traffic without session affinity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._put(
            f"/accounts/{account_id}/load_balancers/pools/{pool_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "origins": origins,
                    "check_regions": check_regions,
                    "description": description,
                    "enabled": enabled,
                    "latitude": latitude,
                    "load_shedding": load_shedding,
                    "longitude": longitude,
                    "minimum_origins": minimum_origins,
                    "monitor": monitor,
                    "notification_email": notification_email,
                    "notification_filter": notification_filter,
                    "origin_steering": origin_steering,
                },
                pool_update_params.PoolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Pool]._unwrapper,
            ),
            cast_to=cast(Type[Pool], ResultWrapper[Pool]),
        )

    def list(
        self,
        *,
        account_id: str,
        monitor: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Pool, AsyncSinglePage[Pool]]:
        """
        List configured pools.

        Args:
          account_id: Identifier

          monitor: The ID of the Monitor to use for checking the health of origins within this
              pool.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/load_balancers/pools",
            page=AsyncSinglePage[Pool],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"monitor": monitor}, pool_list_params.PoolListParams),
            ),
            model=Pool,
        )

    async def delete(
        self,
        pool_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PoolDeleteResponse:
        """
        Delete a configured pool.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/load_balancers/pools/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PoolDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[PoolDeleteResponse], ResultWrapper[PoolDeleteResponse]),
        )

    async def edit(
        self,
        pool_id: str,
        *,
        account_id: str,
        check_regions: Optional[List[CheckRegion]] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        latitude: float | NotGiven = NOT_GIVEN,
        load_shedding: LoadSheddingParam | NotGiven = NOT_GIVEN,
        longitude: float | NotGiven = NOT_GIVEN,
        minimum_origins: int | NotGiven = NOT_GIVEN,
        monitor: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notification_email: str | NotGiven = NOT_GIVEN,
        notification_filter: Optional[NotificationFilterParam] | NotGiven = NOT_GIVEN,
        origin_steering: OriginSteeringParam | NotGiven = NOT_GIVEN,
        origins: Iterable[OriginParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pool:
        """
        Apply changes to an existing pool, overwriting the supplied properties.

        Args:
          account_id: Identifier

          check_regions: A list of regions from which to run health checks. Null means every Cloudflare
              data center.

          description: A human-readable description of the pool.

          enabled: Whether to enable (the default) or disable this pool. Disabled pools will not
              receive traffic and are excluded from health checks. Disabling a pool will cause
              any load balancers using it to failover to the next pool (if any).

          latitude: The latitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, longitude must also be set.

          load_shedding: Configures load shedding policies and percentages for the pool.

          longitude: The longitude of the data center containing the origins used in this pool in
              decimal degrees. If this is set, latitude must also be set.

          minimum_origins: The minimum number of origins that must be healthy for this pool to serve
              traffic. If the number of healthy origins falls below this number, the pool will
              be marked unhealthy and will failover to the next available pool.

          monitor: The ID of the Monitor to use for checking the health of origins within this
              pool.

          name: A short name (tag) for the pool. Only alphanumeric characters, hyphens, and
              underscores are allowed.

          notification_email: This field is now deprecated. It has been moved to Cloudflare's Centralized
              Notification service
              https://developers.cloudflare.com/fundamentals/notifications/. The email address
              to send health status notifications to. This can be an individual mailbox or a
              mailing list. Multiple emails can be supplied as a comma delimited list.

          notification_filter: Filter pool and origin health notifications by resource type or health status.
              Use null to reset.

          origin_steering: Configures origin steering for the pool. Controls how origins are selected for
              new sessions and traffic without session affinity.

          origins: The list of origins within this pool. Traffic directed at this pool is balanced
              across all currently healthy origins, provided the pool itself is healthy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/load_balancers/pools/{pool_id}",
            body=await async_maybe_transform(
                {
                    "check_regions": check_regions,
                    "description": description,
                    "enabled": enabled,
                    "latitude": latitude,
                    "load_shedding": load_shedding,
                    "longitude": longitude,
                    "minimum_origins": minimum_origins,
                    "monitor": monitor,
                    "name": name,
                    "notification_email": notification_email,
                    "notification_filter": notification_filter,
                    "origin_steering": origin_steering,
                    "origins": origins,
                },
                pool_edit_params.PoolEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Pool]._unwrapper,
            ),
            cast_to=cast(Type[Pool], ResultWrapper[Pool]),
        )

    async def get(
        self,
        pool_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pool:
        """
        Fetch a single configured pool.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._get(
            f"/accounts/{account_id}/load_balancers/pools/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Pool]._unwrapper,
            ),
            cast_to=cast(Type[Pool], ResultWrapper[Pool]),
        )


class PoolsResourceWithRawResponse:
    def __init__(self, pools: PoolsResource) -> None:
        self._pools = pools

        self.create = to_raw_response_wrapper(
            pools.create,
        )
        self.update = to_raw_response_wrapper(
            pools.update,
        )
        self.list = to_raw_response_wrapper(
            pools.list,
        )
        self.delete = to_raw_response_wrapper(
            pools.delete,
        )
        self.edit = to_raw_response_wrapper(
            pools.edit,
        )
        self.get = to_raw_response_wrapper(
            pools.get,
        )

    @cached_property
    def health(self) -> HealthResourceWithRawResponse:
        return HealthResourceWithRawResponse(self._pools.health)

    @cached_property
    def references(self) -> ReferencesResourceWithRawResponse:
        return ReferencesResourceWithRawResponse(self._pools.references)


class AsyncPoolsResourceWithRawResponse:
    def __init__(self, pools: AsyncPoolsResource) -> None:
        self._pools = pools

        self.create = async_to_raw_response_wrapper(
            pools.create,
        )
        self.update = async_to_raw_response_wrapper(
            pools.update,
        )
        self.list = async_to_raw_response_wrapper(
            pools.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pools.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            pools.edit,
        )
        self.get = async_to_raw_response_wrapper(
            pools.get,
        )

    @cached_property
    def health(self) -> AsyncHealthResourceWithRawResponse:
        return AsyncHealthResourceWithRawResponse(self._pools.health)

    @cached_property
    def references(self) -> AsyncReferencesResourceWithRawResponse:
        return AsyncReferencesResourceWithRawResponse(self._pools.references)


class PoolsResourceWithStreamingResponse:
    def __init__(self, pools: PoolsResource) -> None:
        self._pools = pools

        self.create = to_streamed_response_wrapper(
            pools.create,
        )
        self.update = to_streamed_response_wrapper(
            pools.update,
        )
        self.list = to_streamed_response_wrapper(
            pools.list,
        )
        self.delete = to_streamed_response_wrapper(
            pools.delete,
        )
        self.edit = to_streamed_response_wrapper(
            pools.edit,
        )
        self.get = to_streamed_response_wrapper(
            pools.get,
        )

    @cached_property
    def health(self) -> HealthResourceWithStreamingResponse:
        return HealthResourceWithStreamingResponse(self._pools.health)

    @cached_property
    def references(self) -> ReferencesResourceWithStreamingResponse:
        return ReferencesResourceWithStreamingResponse(self._pools.references)


class AsyncPoolsResourceWithStreamingResponse:
    def __init__(self, pools: AsyncPoolsResource) -> None:
        self._pools = pools

        self.create = async_to_streamed_response_wrapper(
            pools.create,
        )
        self.update = async_to_streamed_response_wrapper(
            pools.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pools.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pools.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            pools.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            pools.get,
        )

    @cached_property
    def health(self) -> AsyncHealthResourceWithStreamingResponse:
        return AsyncHealthResourceWithStreamingResponse(self._pools.health)

    @cached_property
    def references(self) -> AsyncReferencesResourceWithStreamingResponse:
        return AsyncReferencesResourceWithStreamingResponse(self._pools.references)
