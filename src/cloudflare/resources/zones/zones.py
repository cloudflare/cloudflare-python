# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type as TypingType, Optional, cast
from typing_extensions import Literal

import httpx

from .holds import (
    HoldsResource,
    AsyncHoldsResource,
    HoldsResourceWithRawResponse,
    AsyncHoldsResourceWithRawResponse,
    HoldsResourceWithStreamingResponse,
    AsyncHoldsResourceWithStreamingResponse,
)
from .plans import (
    PlansResource,
    AsyncPlansResource,
    PlansResourceWithRawResponse,
    AsyncPlansResourceWithRawResponse,
    PlansResourceWithStreamingResponse,
    AsyncPlansResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .rate_plans import (
    RatePlansResource,
    AsyncRatePlansResource,
    RatePlansResourceWithRawResponse,
    AsyncRatePlansResourceWithRawResponse,
    RatePlansResourceWithStreamingResponse,
    AsyncRatePlansResourceWithStreamingResponse,
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
from ...types.zones import zone_edit_params, zone_list_params, zone_create_params
from .subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from .activation_check import (
    ActivationCheckResource,
    AsyncActivationCheckResource,
    ActivationCheckResourceWithRawResponse,
    AsyncActivationCheckResourceWithRawResponse,
    ActivationCheckResourceWithStreamingResponse,
    AsyncActivationCheckResourceWithStreamingResponse,
)
from ...types.zones.type import Type as ZonesType
from ...types.zones.zone import Zone
from .custom_nameservers import (
    CustomNameserversResource,
    AsyncCustomNameserversResource,
    CustomNameserversResourceWithRawResponse,
    AsyncCustomNameserversResourceWithRawResponse,
    CustomNameserversResourceWithStreamingResponse,
    AsyncCustomNameserversResourceWithStreamingResponse,
)
from ...types.zones.zone_delete_response import ZoneDeleteResponse

__all__ = ["ZonesResource", "AsyncZonesResource"]


class ZonesResource(SyncAPIResource):
    @cached_property
    def activation_check(self) -> ActivationCheckResource:
        return ActivationCheckResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def custom_nameservers(self) -> CustomNameserversResource:
        return CustomNameserversResource(self._client)

    @cached_property
    def holds(self) -> HoldsResource:
        return HoldsResource(self._client)

    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        return SubscriptionsResource(self._client)

    @cached_property
    def plans(self) -> PlansResource:
        return PlansResource(self._client)

    @cached_property
    def rate_plans(self) -> RatePlansResource:
        return RatePlansResource(self._client)

    @cached_property
    def with_raw_response(self) -> ZonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ZonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ZonesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account: zone_create_params.Account,
        name: str,
        type: ZonesType | NotGiven = NOT_GIVEN,
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
                post_parser=ResultWrapper[Optional[Zone]]._unwrapper,
            ),
            cast_to=cast(TypingType[Optional[Zone]], ResultWrapper[Zone]),
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
        """Lists, searches, sorts, and filters your zones.

        Listing zones across more than
        500 accounts is currently not allowed.

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
                post_parser=ResultWrapper[Optional[ZoneDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(TypingType[Optional[ZoneDeleteResponse]], ResultWrapper[ZoneDeleteResponse]),
        )

    def edit(
        self,
        *,
        zone_id: str,
        type: Literal["full", "partial", "secondary", "internal"] | NotGiven = NOT_GIVEN,
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
                post_parser=ResultWrapper[Optional[Zone]]._unwrapper,
            ),
            cast_to=cast(TypingType[Optional[Zone]], ResultWrapper[Zone]),
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
                post_parser=ResultWrapper[Optional[Zone]]._unwrapper,
            ),
            cast_to=cast(TypingType[Optional[Zone]], ResultWrapper[Zone]),
        )


class AsyncZonesResource(AsyncAPIResource):
    @cached_property
    def activation_check(self) -> AsyncActivationCheckResource:
        return AsyncActivationCheckResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def custom_nameservers(self) -> AsyncCustomNameserversResource:
        return AsyncCustomNameserversResource(self._client)

    @cached_property
    def holds(self) -> AsyncHoldsResource:
        return AsyncHoldsResource(self._client)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        return AsyncPlansResource(self._client)

    @cached_property
    def rate_plans(self) -> AsyncRatePlansResource:
        return AsyncRatePlansResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncZonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncZonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncZonesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account: zone_create_params.Account,
        name: str,
        type: ZonesType | NotGiven = NOT_GIVEN,
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
                post_parser=ResultWrapper[Optional[Zone]]._unwrapper,
            ),
            cast_to=cast(TypingType[Optional[Zone]], ResultWrapper[Zone]),
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
        """Lists, searches, sorts, and filters your zones.

        Listing zones across more than
        500 accounts is currently not allowed.

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
                post_parser=ResultWrapper[Optional[ZoneDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(TypingType[Optional[ZoneDeleteResponse]], ResultWrapper[ZoneDeleteResponse]),
        )

    async def edit(
        self,
        *,
        zone_id: str,
        type: Literal["full", "partial", "secondary", "internal"] | NotGiven = NOT_GIVEN,
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
                post_parser=ResultWrapper[Optional[Zone]]._unwrapper,
            ),
            cast_to=cast(TypingType[Optional[Zone]], ResultWrapper[Zone]),
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
                post_parser=ResultWrapper[Optional[Zone]]._unwrapper,
            ),
            cast_to=cast(TypingType[Optional[Zone]], ResultWrapper[Zone]),
        )


class ZonesResourceWithRawResponse:
    def __init__(self, zones: ZonesResource) -> None:
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
    def activation_check(self) -> ActivationCheckResourceWithRawResponse:
        return ActivationCheckResourceWithRawResponse(self._zones.activation_check)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._zones.settings)

    @cached_property
    def custom_nameservers(self) -> CustomNameserversResourceWithRawResponse:
        return CustomNameserversResourceWithRawResponse(self._zones.custom_nameservers)

    @cached_property
    def holds(self) -> HoldsResourceWithRawResponse:
        return HoldsResourceWithRawResponse(self._zones.holds)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        return SubscriptionsResourceWithRawResponse(self._zones.subscriptions)

    @cached_property
    def plans(self) -> PlansResourceWithRawResponse:
        return PlansResourceWithRawResponse(self._zones.plans)

    @cached_property
    def rate_plans(self) -> RatePlansResourceWithRawResponse:
        return RatePlansResourceWithRawResponse(self._zones.rate_plans)


class AsyncZonesResourceWithRawResponse:
    def __init__(self, zones: AsyncZonesResource) -> None:
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
    def activation_check(self) -> AsyncActivationCheckResourceWithRawResponse:
        return AsyncActivationCheckResourceWithRawResponse(self._zones.activation_check)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._zones.settings)

    @cached_property
    def custom_nameservers(self) -> AsyncCustomNameserversResourceWithRawResponse:
        return AsyncCustomNameserversResourceWithRawResponse(self._zones.custom_nameservers)

    @cached_property
    def holds(self) -> AsyncHoldsResourceWithRawResponse:
        return AsyncHoldsResourceWithRawResponse(self._zones.holds)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        return AsyncSubscriptionsResourceWithRawResponse(self._zones.subscriptions)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithRawResponse:
        return AsyncPlansResourceWithRawResponse(self._zones.plans)

    @cached_property
    def rate_plans(self) -> AsyncRatePlansResourceWithRawResponse:
        return AsyncRatePlansResourceWithRawResponse(self._zones.rate_plans)


class ZonesResourceWithStreamingResponse:
    def __init__(self, zones: ZonesResource) -> None:
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
    def activation_check(self) -> ActivationCheckResourceWithStreamingResponse:
        return ActivationCheckResourceWithStreamingResponse(self._zones.activation_check)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._zones.settings)

    @cached_property
    def custom_nameservers(self) -> CustomNameserversResourceWithStreamingResponse:
        return CustomNameserversResourceWithStreamingResponse(self._zones.custom_nameservers)

    @cached_property
    def holds(self) -> HoldsResourceWithStreamingResponse:
        return HoldsResourceWithStreamingResponse(self._zones.holds)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        return SubscriptionsResourceWithStreamingResponse(self._zones.subscriptions)

    @cached_property
    def plans(self) -> PlansResourceWithStreamingResponse:
        return PlansResourceWithStreamingResponse(self._zones.plans)

    @cached_property
    def rate_plans(self) -> RatePlansResourceWithStreamingResponse:
        return RatePlansResourceWithStreamingResponse(self._zones.rate_plans)


class AsyncZonesResourceWithStreamingResponse:
    def __init__(self, zones: AsyncZonesResource) -> None:
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
    def activation_check(self) -> AsyncActivationCheckResourceWithStreamingResponse:
        return AsyncActivationCheckResourceWithStreamingResponse(self._zones.activation_check)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._zones.settings)

    @cached_property
    def custom_nameservers(self) -> AsyncCustomNameserversResourceWithStreamingResponse:
        return AsyncCustomNameserversResourceWithStreamingResponse(self._zones.custom_nameservers)

    @cached_property
    def holds(self) -> AsyncHoldsResourceWithStreamingResponse:
        return AsyncHoldsResourceWithStreamingResponse(self._zones.holds)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        return AsyncSubscriptionsResourceWithStreamingResponse(self._zones.subscriptions)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithStreamingResponse:
        return AsyncPlansResourceWithStreamingResponse(self._zones.plans)

    @cached_property
    def rate_plans(self) -> AsyncRatePlansResourceWithStreamingResponse:
        return AsyncRatePlansResourceWithStreamingResponse(self._zones.rate_plans)
