# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal

import httpx

from .holds import (
    Holds,
    AsyncHolds,
    HoldsWithRawResponse,
    AsyncHoldsWithRawResponse,
    HoldsWithStreamingResponse,
    AsyncHoldsWithStreamingResponse,
)
from ...types import Zone, ZoneDeleteResponse, zone_edit_params, zone_list_params, zone_create_params
from .workers import (
    Workers,
    AsyncWorkers,
    WorkersWithRawResponse,
    AsyncWorkersWithRawResponse,
    WorkersWithStreamingResponse,
    AsyncWorkersWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .settings import (
    Settings,
    AsyncSettings,
    SettingsWithRawResponse,
    AsyncSettingsWithRawResponse,
    SettingsWithStreamingResponse,
    AsyncSettingsWithStreamingResponse,
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
from .dns_settings import (
    DNSSettings,
    AsyncDNSSettings,
    DNSSettingsWithRawResponse,
    AsyncDNSSettingsWithRawResponse,
    DNSSettingsWithStreamingResponse,
    AsyncDNSSettingsWithStreamingResponse,
)
from .subscriptions import (
    Subscriptions,
    AsyncSubscriptions,
    SubscriptionsWithRawResponse,
    AsyncSubscriptionsWithRawResponse,
    SubscriptionsWithStreamingResponse,
    AsyncSubscriptionsWithStreamingResponse,
)
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .workers.workers import Workers, AsyncWorkers
from .activation_check import (
    ActivationCheck,
    AsyncActivationCheck,
    ActivationCheckWithRawResponse,
    AsyncActivationCheckWithRawResponse,
    ActivationCheckWithStreamingResponse,
    AsyncActivationCheckWithStreamingResponse,
)
from .settings.settings import Settings, AsyncSettings
from .custom_nameservers import (
    CustomNameservers,
    AsyncCustomNameservers,
    CustomNameserversWithRawResponse,
    AsyncCustomNameserversWithRawResponse,
    CustomNameserversWithStreamingResponse,
    AsyncCustomNameserversWithStreamingResponse,
)

__all__ = ["Zones", "AsyncZones"]


class Zones(SyncAPIResource):
    @cached_property
    def activation_check(self) -> ActivationCheck:
        return ActivationCheck(self._client)

    @cached_property
    def dns_settings(self) -> DNSSettings:
        return DNSSettings(self._client)

    @cached_property
    def settings(self) -> Settings:
        return Settings(self._client)

    @cached_property
    def custom_nameservers(self) -> CustomNameservers:
        return CustomNameservers(self._client)

    @cached_property
    def holds(self) -> Holds:
        return Holds(self._client)

    @cached_property
    def workers(self) -> Workers:
        return Workers(self._client)

    @cached_property
    def subscriptions(self) -> Subscriptions:
        return Subscriptions(self._client)

    @cached_property
    def with_raw_response(self) -> ZonesWithRawResponse:
        return ZonesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZonesWithStreamingResponse:
        return ZonesWithStreamingResponse(self)

    def create(
        self,
        *,
        account: zone_create_params.Account,
        name: str,
        type: Literal["full", "partial", "secondary"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Zone]:
        """
        Create Zone

        Args:
          name: The domain name

          type: A full zone implies that DNS is hosted with Cloudflare. A partial zone is
              typically a partner-hosted zone or a CNAME setup.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/zones",
            body=maybe_transform(
                {
                    "account": account,
                    "name": name,
                    "type": type,
                },
                zone_create_params.ZoneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Zone]], ResultWrapper[Zone]),
        )

    def list(
        self,
        *,
        account: zone_list_params.Account | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal["name", "status", "account.id", "account.name"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        status: Literal["initializing", "pending", "active", "moved"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[Zone]:
        """
        Lists, searches, sorts, and filters your zones.

        Args:
          direction: Direction to order zones.

          match: Whether to match all search requirements or at least one (any).

          name: A domain name. Optional filter operators can be provided to extend refine the
              search:

              - `equal` (default)
              - `not_equal`
              - `starts_with`
              - `ends_with`
              - `contains`
              - `starts_with_case_sensitive`
              - `ends_with_case_sensitive`
              - `contains_case_sensitive`

          order: Field to order zones by.

          page: Page number of paginated results.

          per_page: Number of zones per page.

          status: A zone status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/zones",
            page=SyncV4PagePaginationArray[Zone],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account": account,
                        "direction": direction,
                        "match": match,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    zone_list_params.ZoneListParams,
                ),
            ),
            model=Zone,
        )

    def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneDeleteResponse]:
        """
        Deletes an existing zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._delete(
            f"/zones/{zone_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneDeleteResponse]], ResultWrapper[ZoneDeleteResponse]),
        )

    def edit(
        self,
        *,
        zone_id: str,
        plan: zone_edit_params.Plan | NotGiven = NOT_GIVEN,
        type: Literal["full", "partial", "secondary"] | NotGiven = NOT_GIVEN,
        vanity_name_servers: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Zone]:
        """Edits a zone.

        Only one zone property can be changed at a time.

        Args:
          zone_id: Identifier

          plan: (Deprecated) Please use the `/zones/{zone_id}/subscription` API to update a
              zone's plan. Changing this value will create/cancel associated subscriptions. To
              view available plans for this zone, see Zone Plans.

          type: A full zone implies that DNS is hosted with Cloudflare. A partial zone is
              typically a partner-hosted zone or a CNAME setup. This parameter is only
              available to Enterprise customers or if it has been explicitly enabled on a
              zone.

          vanity_name_servers: An array of domains used for custom name servers. This is only available for
              Business and Enterprise plans.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}",
            body=maybe_transform(
                {
                    "plan": plan,
                    "type": type,
                    "vanity_name_servers": vanity_name_servers,
                },
                zone_edit_params.ZoneEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Zone]], ResultWrapper[Zone]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Zone]:
        """
        Zone Details

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
            f"/zones/{zone_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Zone]], ResultWrapper[Zone]),
        )


class AsyncZones(AsyncAPIResource):
    @cached_property
    def activation_check(self) -> AsyncActivationCheck:
        return AsyncActivationCheck(self._client)

    @cached_property
    def dns_settings(self) -> AsyncDNSSettings:
        return AsyncDNSSettings(self._client)

    @cached_property
    def settings(self) -> AsyncSettings:
        return AsyncSettings(self._client)

    @cached_property
    def custom_nameservers(self) -> AsyncCustomNameservers:
        return AsyncCustomNameservers(self._client)

    @cached_property
    def holds(self) -> AsyncHolds:
        return AsyncHolds(self._client)

    @cached_property
    def workers(self) -> AsyncWorkers:
        return AsyncWorkers(self._client)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptions:
        return AsyncSubscriptions(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncZonesWithRawResponse:
        return AsyncZonesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZonesWithStreamingResponse:
        return AsyncZonesWithStreamingResponse(self)

    async def create(
        self,
        *,
        account: zone_create_params.Account,
        name: str,
        type: Literal["full", "partial", "secondary"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Zone]:
        """
        Create Zone

        Args:
          name: The domain name

          type: A full zone implies that DNS is hosted with Cloudflare. A partial zone is
              typically a partner-hosted zone or a CNAME setup.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/zones",
            body=await async_maybe_transform(
                {
                    "account": account,
                    "name": name,
                    "type": type,
                },
                zone_create_params.ZoneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Zone]], ResultWrapper[Zone]),
        )

    def list(
        self,
        *,
        account: zone_list_params.Account | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal["name", "status", "account.id", "account.name"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        status: Literal["initializing", "pending", "active", "moved"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Zone, AsyncV4PagePaginationArray[Zone]]:
        """
        Lists, searches, sorts, and filters your zones.

        Args:
          direction: Direction to order zones.

          match: Whether to match all search requirements or at least one (any).

          name: A domain name. Optional filter operators can be provided to extend refine the
              search:

              - `equal` (default)
              - `not_equal`
              - `starts_with`
              - `ends_with`
              - `contains`
              - `starts_with_case_sensitive`
              - `ends_with_case_sensitive`
              - `contains_case_sensitive`

          order: Field to order zones by.

          page: Page number of paginated results.

          per_page: Number of zones per page.

          status: A zone status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/zones",
            page=AsyncV4PagePaginationArray[Zone],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account": account,
                        "direction": direction,
                        "match": match,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    zone_list_params.ZoneListParams,
                ),
            ),
            model=Zone,
        )

    async def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneDeleteResponse]:
        """
        Deletes an existing zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._delete(
            f"/zones/{zone_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneDeleteResponse]], ResultWrapper[ZoneDeleteResponse]),
        )

    async def edit(
        self,
        *,
        zone_id: str,
        plan: zone_edit_params.Plan | NotGiven = NOT_GIVEN,
        type: Literal["full", "partial", "secondary"] | NotGiven = NOT_GIVEN,
        vanity_name_servers: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Zone]:
        """Edits a zone.

        Only one zone property can be changed at a time.

        Args:
          zone_id: Identifier

          plan: (Deprecated) Please use the `/zones/{zone_id}/subscription` API to update a
              zone's plan. Changing this value will create/cancel associated subscriptions. To
              view available plans for this zone, see Zone Plans.

          type: A full zone implies that DNS is hosted with Cloudflare. A partial zone is
              typically a partner-hosted zone or a CNAME setup. This parameter is only
              available to Enterprise customers or if it has been explicitly enabled on a
              zone.

          vanity_name_servers: An array of domains used for custom name servers. This is only available for
              Business and Enterprise plans.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}",
            body=await async_maybe_transform(
                {
                    "plan": plan,
                    "type": type,
                    "vanity_name_servers": vanity_name_servers,
                },
                zone_edit_params.ZoneEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Zone]], ResultWrapper[Zone]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Zone]:
        """
        Zone Details

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
            f"/zones/{zone_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[Zone]], ResultWrapper[Zone]),
        )


class ZonesWithRawResponse:
    def __init__(self, zones: Zones) -> None:
        self._zones = zones

        self.create = to_raw_response_wrapper(
            zones.create,
        )
        self.list = to_raw_response_wrapper(
            zones.list,
        )
        self.delete = to_raw_response_wrapper(
            zones.delete,
        )
        self.edit = to_raw_response_wrapper(
            zones.edit,
        )
        self.get = to_raw_response_wrapper(
            zones.get,
        )

    @cached_property
    def activation_check(self) -> ActivationCheckWithRawResponse:
        return ActivationCheckWithRawResponse(self._zones.activation_check)

    @cached_property
    def dns_settings(self) -> DNSSettingsWithRawResponse:
        return DNSSettingsWithRawResponse(self._zones.dns_settings)

    @cached_property
    def settings(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self._zones.settings)

    @cached_property
    def custom_nameservers(self) -> CustomNameserversWithRawResponse:
        return CustomNameserversWithRawResponse(self._zones.custom_nameservers)

    @cached_property
    def holds(self) -> HoldsWithRawResponse:
        return HoldsWithRawResponse(self._zones.holds)

    @cached_property
    def workers(self) -> WorkersWithRawResponse:
        return WorkersWithRawResponse(self._zones.workers)

    @cached_property
    def subscriptions(self) -> SubscriptionsWithRawResponse:
        return SubscriptionsWithRawResponse(self._zones.subscriptions)


class AsyncZonesWithRawResponse:
    def __init__(self, zones: AsyncZones) -> None:
        self._zones = zones

        self.create = async_to_raw_response_wrapper(
            zones.create,
        )
        self.list = async_to_raw_response_wrapper(
            zones.list,
        )
        self.delete = async_to_raw_response_wrapper(
            zones.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            zones.edit,
        )
        self.get = async_to_raw_response_wrapper(
            zones.get,
        )

    @cached_property
    def activation_check(self) -> AsyncActivationCheckWithRawResponse:
        return AsyncActivationCheckWithRawResponse(self._zones.activation_check)

    @cached_property
    def dns_settings(self) -> AsyncDNSSettingsWithRawResponse:
        return AsyncDNSSettingsWithRawResponse(self._zones.dns_settings)

    @cached_property
    def settings(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self._zones.settings)

    @cached_property
    def custom_nameservers(self) -> AsyncCustomNameserversWithRawResponse:
        return AsyncCustomNameserversWithRawResponse(self._zones.custom_nameservers)

    @cached_property
    def holds(self) -> AsyncHoldsWithRawResponse:
        return AsyncHoldsWithRawResponse(self._zones.holds)

    @cached_property
    def workers(self) -> AsyncWorkersWithRawResponse:
        return AsyncWorkersWithRawResponse(self._zones.workers)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsWithRawResponse:
        return AsyncSubscriptionsWithRawResponse(self._zones.subscriptions)


class ZonesWithStreamingResponse:
    def __init__(self, zones: Zones) -> None:
        self._zones = zones

        self.create = to_streamed_response_wrapper(
            zones.create,
        )
        self.list = to_streamed_response_wrapper(
            zones.list,
        )
        self.delete = to_streamed_response_wrapper(
            zones.delete,
        )
        self.edit = to_streamed_response_wrapper(
            zones.edit,
        )
        self.get = to_streamed_response_wrapper(
            zones.get,
        )

    @cached_property
    def activation_check(self) -> ActivationCheckWithStreamingResponse:
        return ActivationCheckWithStreamingResponse(self._zones.activation_check)

    @cached_property
    def dns_settings(self) -> DNSSettingsWithStreamingResponse:
        return DNSSettingsWithStreamingResponse(self._zones.dns_settings)

    @cached_property
    def settings(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self._zones.settings)

    @cached_property
    def custom_nameservers(self) -> CustomNameserversWithStreamingResponse:
        return CustomNameserversWithStreamingResponse(self._zones.custom_nameservers)

    @cached_property
    def holds(self) -> HoldsWithStreamingResponse:
        return HoldsWithStreamingResponse(self._zones.holds)

    @cached_property
    def workers(self) -> WorkersWithStreamingResponse:
        return WorkersWithStreamingResponse(self._zones.workers)

    @cached_property
    def subscriptions(self) -> SubscriptionsWithStreamingResponse:
        return SubscriptionsWithStreamingResponse(self._zones.subscriptions)


class AsyncZonesWithStreamingResponse:
    def __init__(self, zones: AsyncZones) -> None:
        self._zones = zones

        self.create = async_to_streamed_response_wrapper(
            zones.create,
        )
        self.list = async_to_streamed_response_wrapper(
            zones.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            zones.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            zones.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            zones.get,
        )

    @cached_property
    def activation_check(self) -> AsyncActivationCheckWithStreamingResponse:
        return AsyncActivationCheckWithStreamingResponse(self._zones.activation_check)

    @cached_property
    def dns_settings(self) -> AsyncDNSSettingsWithStreamingResponse:
        return AsyncDNSSettingsWithStreamingResponse(self._zones.dns_settings)

    @cached_property
    def settings(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self._zones.settings)

    @cached_property
    def custom_nameservers(self) -> AsyncCustomNameserversWithStreamingResponse:
        return AsyncCustomNameserversWithStreamingResponse(self._zones.custom_nameservers)

    @cached_property
    def holds(self) -> AsyncHoldsWithStreamingResponse:
        return AsyncHoldsWithStreamingResponse(self._zones.holds)

    @cached_property
    def workers(self) -> AsyncWorkersWithStreamingResponse:
        return AsyncWorkersWithStreamingResponse(self._zones.workers)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsWithStreamingResponse:
        return AsyncSubscriptionsWithStreamingResponse(self._zones.subscriptions)
