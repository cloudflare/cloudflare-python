# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .hold import Hold, AsyncHold

from ..._compat import cached_property

from ...types import (
    ZoneCreateResponse,
    ZoneUpdateResponse,
    ZoneListResponse,
    ZoneDeleteResponse,
    ZoneGetResponse,
    zone_create_params,
    zone_update_params,
    zone_list_params,
)

from typing import Type, Optional, List

from typing_extensions import Literal

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
from ...types import zone_create_params
from ...types import zone_update_params
from ...types import zone_list_params
from .hold import (
    Hold,
    AsyncHold,
    HoldWithRawResponse,
    AsyncHoldWithRawResponse,
    HoldWithStreamingResponse,
    AsyncHoldWithStreamingResponse,
)
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

__all__ = ["Zones", "AsyncZones"]


class Zones(SyncAPIResource):
    @cached_property
    def hold(self) -> Hold:
        return Hold(self._client)

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
    ) -> Optional[ZoneCreateResponse]:
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
            cast_to=cast(Type[Optional[ZoneCreateResponse]], ResultWrapper[ZoneCreateResponse]),
        )

    def update(
        self,
        zone_id: str,
        *,
        plan: zone_update_params.Plan | NotGiven = NOT_GIVEN,
        type: Literal["full", "partial", "secondary"] | NotGiven = NOT_GIVEN,
        vanity_name_servers: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneUpdateResponse]:
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
                zone_update_params.ZoneUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneUpdateResponse]], ResultWrapper[ZoneUpdateResponse]),
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
    ) -> Optional[ZoneListResponse]:
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
        return self._get(
            "/zones",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneListResponse]], ResultWrapper[ZoneListResponse]),
        )

    def delete(
        self,
        zone_id: str,
        *,
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

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneGetResponse]:
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
            cast_to=cast(Type[Optional[ZoneGetResponse]], ResultWrapper[ZoneGetResponse]),
        )


class AsyncZones(AsyncAPIResource):
    @cached_property
    def hold(self) -> AsyncHold:
        return AsyncHold(self._client)

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
    ) -> Optional[ZoneCreateResponse]:
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
            cast_to=cast(Type[Optional[ZoneCreateResponse]], ResultWrapper[ZoneCreateResponse]),
        )

    async def update(
        self,
        zone_id: str,
        *,
        plan: zone_update_params.Plan | NotGiven = NOT_GIVEN,
        type: Literal["full", "partial", "secondary"] | NotGiven = NOT_GIVEN,
        vanity_name_servers: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneUpdateResponse]:
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
            body=maybe_transform(
                {
                    "plan": plan,
                    "type": type,
                    "vanity_name_servers": vanity_name_servers,
                },
                zone_update_params.ZoneUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneUpdateResponse]], ResultWrapper[ZoneUpdateResponse]),
        )

    async def list(
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
    ) -> Optional[ZoneListResponse]:
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
        return await self._get(
            "/zones",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneListResponse]], ResultWrapper[ZoneListResponse]),
        )

    async def delete(
        self,
        zone_id: str,
        *,
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

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneGetResponse]:
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
            cast_to=cast(Type[Optional[ZoneGetResponse]], ResultWrapper[ZoneGetResponse]),
        )


class ZonesWithRawResponse:
    def __init__(self, zones: Zones) -> None:
        self._zones = zones

        self.create = to_raw_response_wrapper(
            zones.create,
        )
        self.update = to_raw_response_wrapper(
            zones.update,
        )
        self.list = to_raw_response_wrapper(
            zones.list,
        )
        self.delete = to_raw_response_wrapper(
            zones.delete,
        )
        self.get = to_raw_response_wrapper(
            zones.get,
        )

    @cached_property
    def hold(self) -> HoldWithRawResponse:
        return HoldWithRawResponse(self._zones.hold)


class AsyncZonesWithRawResponse:
    def __init__(self, zones: AsyncZones) -> None:
        self._zones = zones

        self.create = async_to_raw_response_wrapper(
            zones.create,
        )
        self.update = async_to_raw_response_wrapper(
            zones.update,
        )
        self.list = async_to_raw_response_wrapper(
            zones.list,
        )
        self.delete = async_to_raw_response_wrapper(
            zones.delete,
        )
        self.get = async_to_raw_response_wrapper(
            zones.get,
        )

    @cached_property
    def hold(self) -> AsyncHoldWithRawResponse:
        return AsyncHoldWithRawResponse(self._zones.hold)


class ZonesWithStreamingResponse:
    def __init__(self, zones: Zones) -> None:
        self._zones = zones

        self.create = to_streamed_response_wrapper(
            zones.create,
        )
        self.update = to_streamed_response_wrapper(
            zones.update,
        )
        self.list = to_streamed_response_wrapper(
            zones.list,
        )
        self.delete = to_streamed_response_wrapper(
            zones.delete,
        )
        self.get = to_streamed_response_wrapper(
            zones.get,
        )

    @cached_property
    def hold(self) -> HoldWithStreamingResponse:
        return HoldWithStreamingResponse(self._zones.hold)


class AsyncZonesWithStreamingResponse:
    def __init__(self, zones: AsyncZones) -> None:
        self._zones = zones

        self.create = async_to_streamed_response_wrapper(
            zones.create,
        )
        self.update = async_to_streamed_response_wrapper(
            zones.update,
        )
        self.list = async_to_streamed_response_wrapper(
            zones.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            zones.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            zones.get,
        )

    @cached_property
    def hold(self) -> AsyncHoldWithStreamingResponse:
        return AsyncHoldWithStreamingResponse(self._zones.hold)
