# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .acls import ACLsResource, AsyncACLsResource

from ...._compat import cached_property

from .lans import LANsResource, AsyncLANsResource

from .wans import WANsResource, AsyncWANsResource

from ....types.magic_transit.site import Site

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options, AsyncPaginator

from typing import Type

from ....types.magic_transit.site_location_param import SiteLocationParam

from ....pagination import SyncSinglePage, AsyncSinglePage

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
from ....types.magic_transit import site_create_params
from ....types.magic_transit import site_update_params
from ....types.magic_transit import site_list_params
from ....types.magic_transit import site_edit_params
from ....types.magic_transit import SiteLocation
from ....types.magic_transit import SiteLocation
from ....types.magic_transit import SiteLocation
from .acls import (
    ACLsResource,
    AsyncACLsResource,
    ACLsResourceWithRawResponse,
    AsyncACLsResourceWithRawResponse,
    ACLsResourceWithStreamingResponse,
    AsyncACLsResourceWithStreamingResponse,
)
from .lans import (
    LANsResource,
    AsyncLANsResource,
    LANsResourceWithRawResponse,
    AsyncLANsResourceWithRawResponse,
    LANsResourceWithStreamingResponse,
    AsyncLANsResourceWithStreamingResponse,
)
from .wans import (
    WANsResource,
    AsyncWANsResource,
    WANsResourceWithRawResponse,
    AsyncWANsResourceWithRawResponse,
    WANsResourceWithStreamingResponse,
    AsyncWANsResourceWithStreamingResponse,
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

__all__ = ["SitesResource", "AsyncSitesResource"]


class SitesResource(SyncAPIResource):
    @cached_property
    def acls(self) -> ACLsResource:
        return ACLsResource(self._client)

    @cached_property
    def lans(self) -> LANsResource:
        return LANsResource(self._client)

    @cached_property
    def wans(self) -> WANsResource:
        return WANsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SitesResourceWithRawResponse:
        return SitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SitesResourceWithStreamingResponse:
        return SitesResourceWithStreamingResponse(self)

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

          connector_id: Magic Connector identifier tag.

          ha_mode: Site high availability mode. If set to true, the site can have two connectors
              and runs in high availability mode.

          location: Location of site in latitude and longitude.

          secondary_connector_id: Magic Connector identifier tag. Used when high availability mode is on.

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

          connector_id: Magic Connector identifier tag.

          location: Location of site in latitude and longitude.

          name: The name of the site.

          secondary_connector_id: Magic Connector identifier tag. Used when high availability mode is on.

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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Site]._unwrapper,
            ),
            cast_to=cast(Type[Site], ResultWrapper[Site]),
        )

    def edit(
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
        Patch a specific Site.

        Args:
          account_id: Identifier

          site_id: Identifier

          connector_id: Magic Connector identifier tag.

          location: Location of site in latitude and longitude.

          name: The name of the site.

          secondary_connector_id: Magic Connector identifier tag. Used when high availability mode is on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._patch(
            f"/accounts/{account_id}/magic/sites/{site_id}",
            body=maybe_transform(
                {
                    "connector_id": connector_id,
                    "description": description,
                    "location": location,
                    "name": name,
                    "secondary_connector_id": secondary_connector_id,
                },
                site_edit_params.SiteEditParams,
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


class AsyncSitesResource(AsyncAPIResource):
    @cached_property
    def acls(self) -> AsyncACLsResource:
        return AsyncACLsResource(self._client)

    @cached_property
    def lans(self) -> AsyncLANsResource:
        return AsyncLANsResource(self._client)

    @cached_property
    def wans(self) -> AsyncWANsResource:
        return AsyncWANsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSitesResourceWithRawResponse:
        return AsyncSitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSitesResourceWithStreamingResponse:
        return AsyncSitesResourceWithStreamingResponse(self)

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

          connector_id: Magic Connector identifier tag.

          ha_mode: Site high availability mode. If set to true, the site can have two connectors
              and runs in high availability mode.

          location: Location of site in latitude and longitude.

          secondary_connector_id: Magic Connector identifier tag. Used when high availability mode is on.

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

          connector_id: Magic Connector identifier tag.

          location: Location of site in latitude and longitude.

          name: The name of the site.

          secondary_connector_id: Magic Connector identifier tag. Used when high availability mode is on.

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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Site]._unwrapper,
            ),
            cast_to=cast(Type[Site], ResultWrapper[Site]),
        )

    async def edit(
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
        Patch a specific Site.

        Args:
          account_id: Identifier

          site_id: Identifier

          connector_id: Magic Connector identifier tag.

          location: Location of site in latitude and longitude.

          name: The name of the site.

          secondary_connector_id: Magic Connector identifier tag. Used when high availability mode is on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/magic/sites/{site_id}",
            body=await async_maybe_transform(
                {
                    "connector_id": connector_id,
                    "description": description,
                    "location": location,
                    "name": name,
                    "secondary_connector_id": secondary_connector_id,
                },
                site_edit_params.SiteEditParams,
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


class SitesResourceWithRawResponse:
    def __init__(self, sites: SitesResource) -> None:
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
        self.edit = to_raw_response_wrapper(
            sites.edit,
        )
        self.get = to_raw_response_wrapper(
            sites.get,
        )

    @cached_property
    def acls(self) -> ACLsResourceWithRawResponse:
        return ACLsResourceWithRawResponse(self._sites.acls)

    @cached_property
    def lans(self) -> LANsResourceWithRawResponse:
        return LANsResourceWithRawResponse(self._sites.lans)

    @cached_property
    def wans(self) -> WANsResourceWithRawResponse:
        return WANsResourceWithRawResponse(self._sites.wans)


class AsyncSitesResourceWithRawResponse:
    def __init__(self, sites: AsyncSitesResource) -> None:
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
        self.edit = async_to_raw_response_wrapper(
            sites.edit,
        )
        self.get = async_to_raw_response_wrapper(
            sites.get,
        )

    @cached_property
    def acls(self) -> AsyncACLsResourceWithRawResponse:
        return AsyncACLsResourceWithRawResponse(self._sites.acls)

    @cached_property
    def lans(self) -> AsyncLANsResourceWithRawResponse:
        return AsyncLANsResourceWithRawResponse(self._sites.lans)

    @cached_property
    def wans(self) -> AsyncWANsResourceWithRawResponse:
        return AsyncWANsResourceWithRawResponse(self._sites.wans)


class SitesResourceWithStreamingResponse:
    def __init__(self, sites: SitesResource) -> None:
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
        self.edit = to_streamed_response_wrapper(
            sites.edit,
        )
        self.get = to_streamed_response_wrapper(
            sites.get,
        )

    @cached_property
    def acls(self) -> ACLsResourceWithStreamingResponse:
        return ACLsResourceWithStreamingResponse(self._sites.acls)

    @cached_property
    def lans(self) -> LANsResourceWithStreamingResponse:
        return LANsResourceWithStreamingResponse(self._sites.lans)

    @cached_property
    def wans(self) -> WANsResourceWithStreamingResponse:
        return WANsResourceWithStreamingResponse(self._sites.wans)


class AsyncSitesResourceWithStreamingResponse:
    def __init__(self, sites: AsyncSitesResource) -> None:
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
        self.edit = async_to_streamed_response_wrapper(
            sites.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            sites.get,
        )

    @cached_property
    def acls(self) -> AsyncACLsResourceWithStreamingResponse:
        return AsyncACLsResourceWithStreamingResponse(self._sites.acls)

    @cached_property
    def lans(self) -> AsyncLANsResourceWithStreamingResponse:
        return AsyncLANsResourceWithStreamingResponse(self._sites.lans)

    @cached_property
    def wans(self) -> AsyncWANsResourceWithStreamingResponse:
        return AsyncWANsResourceWithStreamingResponse(self._sites.wans)
