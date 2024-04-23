# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from .acls import (
    ACLs,
    AsyncACLs,
    ACLsWithRawResponse,
    AsyncACLsWithRawResponse,
    ACLsWithStreamingResponse,
    AsyncACLsWithStreamingResponse,
)
from .lans import (
    LANs,
    AsyncLANs,
    LANsWithRawResponse,
    AsyncLANsWithRawResponse,
    LANsWithStreamingResponse,
    AsyncLANsWithStreamingResponse,
)
from .wans import (
    WANs,
    AsyncWANs,
    WANsWithRawResponse,
    AsyncWANsWithRawResponse,
    WANsWithStreamingResponse,
    AsyncWANsWithStreamingResponse,
)
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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.magic_transit import (
    site_list_params,
    site_create_params,
    site_delete_params,
    site_update_params,
)
from ....types.magic_transit.site import Site
from ....types.magic_transit.site_location_param import SiteLocationParam

__all__ = ["Sites", "AsyncSites"]


class Sites(SyncAPIResource):
    @cached_property
    def acls(self) -> ACLs:
        return ACLs(self._client)

    @cached_property
    def lans(self) -> LANs:
        return LANs(self._client)

    @cached_property
    def wans(self) -> WANs:
        return WANs(self._client)

    @cached_property
    def with_raw_response(self) -> SitesWithRawResponse:
        return SitesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SitesWithStreamingResponse:
        return SitesWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        connector_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        ha_mode: bool | NotGiven = NOT_GIVEN,
        location: SiteLocationParam | NotGiven = NOT_GIVEN,
        secondary_connector_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Site:
        """
        Creates a new Site

        Args:
          account_id: Identifier

          name: The name of the site.

          connector_id: Magic WAN Connector identifier tag.

          ha_mode: Site high availability mode. If set to true, the site can have two connectors
              and runs in high availability mode.

          location: Location of site in latitude and longitude.

          secondary_connector_id: Magic WAN Connector identifier tag. Used when high availability mode is on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/sites",
            body=maybe_transform(
                {
                    "name": name,
                    "connector_id": connector_id,
                    "description": description,
                    "ha_mode": ha_mode,
                    "location": location,
                    "secondary_connector_id": secondary_connector_id,
                },
                site_create_params.SiteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Site]._unwrapper,
            ),
            cast_to=cast(Type[Site], ResultWrapper[Site]),
        )

    def update(
        self,
        site_id: str,
        *,
        account_id: str,
        connector_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        location: SiteLocationParam | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        secondary_connector_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Site:
        """
        Update a specific Site.

        Args:
          account_id: Identifier

          site_id: Identifier

          connector_id: Magic WAN Connector identifier tag.

          location: Location of site in latitude and longitude.

          name: The name of the site.

          secondary_connector_id: Magic WAN Connector identifier tag. Used when high availability mode is on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._put(
            f"/accounts/{account_id}/magic/sites/{site_id}",
            body=maybe_transform(
                {
                    "connector_id": connector_id,
                    "description": description,
                    "location": location,
                    "name": name,
                    "secondary_connector_id": secondary_connector_id,
                },
                site_update_params.SiteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Site]._unwrapper,
            ),
            cast_to=cast(Type[Site], ResultWrapper[Site]),
        )

    def list(
        self,
        *,
        account_id: str,
        connector_identifier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Site]:
        """Lists Sites associated with an account.

        Use connector_identifier query param to
        return sites where connector_identifier matches either site.ConnectorID or
        site.SecondaryConnectorID.

        Args:
          account_id: Identifier

          connector_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/sites",
            page=SyncSinglePage[Site],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"connector_identifier": connector_identifier}, site_list_params.SiteListParams),
            ),
            model=Site,
        )

    def delete(
        self,
        site_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Site:
        """
        Remove a specific Site.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._delete(
            f"/accounts/{account_id}/magic/sites/{site_id}",
            body=maybe_transform(body, site_delete_params.SiteDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Site]._unwrapper,
            ),
            cast_to=cast(Type[Site], ResultWrapper[Site]),
        )

    def get(
        self,
        site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Site:
        """
        Get a specific Site.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Site]._unwrapper,
            ),
            cast_to=cast(Type[Site], ResultWrapper[Site]),
        )


class AsyncSites(AsyncAPIResource):
    @cached_property
    def acls(self) -> AsyncACLs:
        return AsyncACLs(self._client)

    @cached_property
    def lans(self) -> AsyncLANs:
        return AsyncLANs(self._client)

    @cached_property
    def wans(self) -> AsyncWANs:
        return AsyncWANs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSitesWithRawResponse:
        return AsyncSitesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSitesWithStreamingResponse:
        return AsyncSitesWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        connector_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        ha_mode: bool | NotGiven = NOT_GIVEN,
        location: SiteLocationParam | NotGiven = NOT_GIVEN,
        secondary_connector_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Site:
        """
        Creates a new Site

        Args:
          account_id: Identifier

          name: The name of the site.

          connector_id: Magic WAN Connector identifier tag.

          ha_mode: Site high availability mode. If set to true, the site can have two connectors
              and runs in high availability mode.

          location: Location of site in latitude and longitude.

          secondary_connector_id: Magic WAN Connector identifier tag. Used when high availability mode is on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/sites",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "connector_id": connector_id,
                    "description": description,
                    "ha_mode": ha_mode,
                    "location": location,
                    "secondary_connector_id": secondary_connector_id,
                },
                site_create_params.SiteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Site]._unwrapper,
            ),
            cast_to=cast(Type[Site], ResultWrapper[Site]),
        )

    async def update(
        self,
        site_id: str,
        *,
        account_id: str,
        connector_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        location: SiteLocationParam | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        secondary_connector_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Site:
        """
        Update a specific Site.

        Args:
          account_id: Identifier

          site_id: Identifier

          connector_id: Magic WAN Connector identifier tag.

          location: Location of site in latitude and longitude.

          name: The name of the site.

          secondary_connector_id: Magic WAN Connector identifier tag. Used when high availability mode is on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/sites/{site_id}",
            body=await async_maybe_transform(
                {
                    "connector_id": connector_id,
                    "description": description,
                    "location": location,
                    "name": name,
                    "secondary_connector_id": secondary_connector_id,
                },
                site_update_params.SiteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Site]._unwrapper,
            ),
            cast_to=cast(Type[Site], ResultWrapper[Site]),
        )

    def list(
        self,
        *,
        account_id: str,
        connector_identifier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Site, AsyncSinglePage[Site]]:
        """Lists Sites associated with an account.

        Use connector_identifier query param to
        return sites where connector_identifier matches either site.ConnectorID or
        site.SecondaryConnectorID.

        Args:
          account_id: Identifier

          connector_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/sites",
            page=AsyncSinglePage[Site],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"connector_identifier": connector_identifier}, site_list_params.SiteListParams),
            ),
            model=Site,
        )

    async def delete(
        self,
        site_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Site:
        """
        Remove a specific Site.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/magic/sites/{site_id}",
            body=await async_maybe_transform(body, site_delete_params.SiteDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Site]._unwrapper,
            ),
            cast_to=cast(Type[Site], ResultWrapper[Site]),
        )

    async def get(
        self,
        site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Site:
        """
        Get a specific Site.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Site]._unwrapper,
            ),
            cast_to=cast(Type[Site], ResultWrapper[Site]),
        )


class SitesWithRawResponse:
    def __init__(self, sites: Sites) -> None:
        self._sites = sites

        self.create = to_raw_response_wrapper(
            sites.create,
        )
        self.update = to_raw_response_wrapper(
            sites.update,
        )
        self.list = to_raw_response_wrapper(
            sites.list,
        )
        self.delete = to_raw_response_wrapper(
            sites.delete,
        )
        self.get = to_raw_response_wrapper(
            sites.get,
        )

    @cached_property
    def acls(self) -> ACLsWithRawResponse:
        return ACLsWithRawResponse(self._sites.acls)

    @cached_property
    def lans(self) -> LANsWithRawResponse:
        return LANsWithRawResponse(self._sites.lans)

    @cached_property
    def wans(self) -> WANsWithRawResponse:
        return WANsWithRawResponse(self._sites.wans)


class AsyncSitesWithRawResponse:
    def __init__(self, sites: AsyncSites) -> None:
        self._sites = sites

        self.create = async_to_raw_response_wrapper(
            sites.create,
        )
        self.update = async_to_raw_response_wrapper(
            sites.update,
        )
        self.list = async_to_raw_response_wrapper(
            sites.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sites.delete,
        )
        self.get = async_to_raw_response_wrapper(
            sites.get,
        )

    @cached_property
    def acls(self) -> AsyncACLsWithRawResponse:
        return AsyncACLsWithRawResponse(self._sites.acls)

    @cached_property
    def lans(self) -> AsyncLANsWithRawResponse:
        return AsyncLANsWithRawResponse(self._sites.lans)

    @cached_property
    def wans(self) -> AsyncWANsWithRawResponse:
        return AsyncWANsWithRawResponse(self._sites.wans)


class SitesWithStreamingResponse:
    def __init__(self, sites: Sites) -> None:
        self._sites = sites

        self.create = to_streamed_response_wrapper(
            sites.create,
        )
        self.update = to_streamed_response_wrapper(
            sites.update,
        )
        self.list = to_streamed_response_wrapper(
            sites.list,
        )
        self.delete = to_streamed_response_wrapper(
            sites.delete,
        )
        self.get = to_streamed_response_wrapper(
            sites.get,
        )

    @cached_property
    def acls(self) -> ACLsWithStreamingResponse:
        return ACLsWithStreamingResponse(self._sites.acls)

    @cached_property
    def lans(self) -> LANsWithStreamingResponse:
        return LANsWithStreamingResponse(self._sites.lans)

    @cached_property
    def wans(self) -> WANsWithStreamingResponse:
        return WANsWithStreamingResponse(self._sites.wans)


class AsyncSitesWithStreamingResponse:
    def __init__(self, sites: AsyncSites) -> None:
        self._sites = sites

        self.create = async_to_streamed_response_wrapper(
            sites.create,
        )
        self.update = async_to_streamed_response_wrapper(
            sites.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sites.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sites.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            sites.get,
        )

    @cached_property
    def acls(self) -> AsyncACLsWithStreamingResponse:
        return AsyncACLsWithStreamingResponse(self._sites.acls)

    @cached_property
    def lans(self) -> AsyncLANsWithStreamingResponse:
        return AsyncLANsWithStreamingResponse(self._sites.lans)

    @cached_property
    def wans(self) -> AsyncWANsWithStreamingResponse:
        return AsyncWANsWithStreamingResponse(self._sites.wans)
