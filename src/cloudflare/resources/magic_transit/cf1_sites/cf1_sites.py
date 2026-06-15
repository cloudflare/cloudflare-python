# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from .ramps import (
    RampsResource,
    AsyncRampsResource,
    RampsResourceWithRawResponse,
    AsyncRampsResourceWithRawResponse,
    RampsResourceWithStreamingResponse,
    AsyncRampsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
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
from ...._base_client import AsyncPaginator, make_request_options
from ....types.magic_transit import cf1_site_update_params
from ....types.magic_transit.cf1_site import Cf1Site
from ....types.magic_transit.cf1_site_param import Cf1SiteParam
from ....types.magic_transit.cf1_site_location_param import Cf1SiteLocationParam

__all__ = ["Cf1SitesResource", "AsyncCf1SitesResource"]


class Cf1SitesResource(SyncAPIResource):
    @cached_property
    def ramps(self) -> RampsResource:
        return RampsResource(self._client)

    @cached_property
    def with_raw_response(self) -> Cf1SitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return Cf1SitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Cf1SitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return Cf1SitesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        body: Iterable[Cf1SiteParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[Cf1Site]:
        """Creates new CF1 Sites for an account.

        Each site must have a unique name within
        the account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/magic/cf1_sites", account_id=account_id),
            page=SyncSinglePage[Cf1Site],
            body=maybe_transform(body, Iterable[Cf1SiteParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Cf1Site,
            method="post",
        )

    def update(
        self,
        cf1_site_id: str,
        *,
        account_id: str,
        description: str | Omit = omit,
        location: Cf1SiteLocationParam | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Cf1Site:
        """Partially updates a specific CF1 Site for an account.

        Only the fields included
        in the request body are modified; omitted fields retain their existing values.

        Args:
          account_id: Identifier

          cf1_site_id: Identifier

          description: A human-provided description of the CF1 Site.

          name: A human-provided name describing the CF1 Site that should be unique within the
              account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf1_site_id:
            raise ValueError(f"Expected a non-empty value for `cf1_site_id` but received {cf1_site_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}", account_id=account_id, cf1_site_id=cf1_site_id
            ),
            body=maybe_transform(
                {
                    "description": description,
                    "location": location,
                    "name": name,
                },
                cf1_site_update_params.Cf1SiteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Cf1Site]._unwrapper,
            ),
            cast_to=cast(Type[Cf1Site], ResultWrapper[Cf1Site]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[Cf1Site]:
        """Lists CF1 Sites associated with an account.

        A CF1 Site represents a physical
        customer network location with optional geographic coordinates.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/magic/cf1_sites", account_id=account_id),
            page=SyncSinglePage[Cf1Site],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Cf1Site,
        )

    def delete(
        self,
        cf1_site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Cf1Site:
        """
        Deletes a specific CF1 Site for an account.

        Args:
          account_id: Identifier

          cf1_site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf1_site_id:
            raise ValueError(f"Expected a non-empty value for `cf1_site_id` but received {cf1_site_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}", account_id=account_id, cf1_site_id=cf1_site_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Cf1Site]._unwrapper,
            ),
            cast_to=cast(Type[Cf1Site], ResultWrapper[Cf1Site]),
        )

    def get(
        self,
        cf1_site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Cf1Site:
        """
        Gets a specific CF1 Site for an account.

        Args:
          account_id: Identifier

          cf1_site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf1_site_id:
            raise ValueError(f"Expected a non-empty value for `cf1_site_id` but received {cf1_site_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}", account_id=account_id, cf1_site_id=cf1_site_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Cf1Site]._unwrapper,
            ),
            cast_to=cast(Type[Cf1Site], ResultWrapper[Cf1Site]),
        )


class AsyncCf1SitesResource(AsyncAPIResource):
    @cached_property
    def ramps(self) -> AsyncRampsResource:
        return AsyncRampsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCf1SitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCf1SitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCf1SitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCf1SitesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        body: Iterable[Cf1SiteParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Cf1Site, AsyncSinglePage[Cf1Site]]:
        """Creates new CF1 Sites for an account.

        Each site must have a unique name within
        the account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/magic/cf1_sites", account_id=account_id),
            page=AsyncSinglePage[Cf1Site],
            body=maybe_transform(body, Iterable[Cf1SiteParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Cf1Site,
            method="post",
        )

    async def update(
        self,
        cf1_site_id: str,
        *,
        account_id: str,
        description: str | Omit = omit,
        location: Cf1SiteLocationParam | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Cf1Site:
        """Partially updates a specific CF1 Site for an account.

        Only the fields included
        in the request body are modified; omitted fields retain their existing values.

        Args:
          account_id: Identifier

          cf1_site_id: Identifier

          description: A human-provided description of the CF1 Site.

          name: A human-provided name describing the CF1 Site that should be unique within the
              account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf1_site_id:
            raise ValueError(f"Expected a non-empty value for `cf1_site_id` but received {cf1_site_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}", account_id=account_id, cf1_site_id=cf1_site_id
            ),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "location": location,
                    "name": name,
                },
                cf1_site_update_params.Cf1SiteUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Cf1Site]._unwrapper,
            ),
            cast_to=cast(Type[Cf1Site], ResultWrapper[Cf1Site]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Cf1Site, AsyncSinglePage[Cf1Site]]:
        """Lists CF1 Sites associated with an account.

        A CF1 Site represents a physical
        customer network location with optional geographic coordinates.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/magic/cf1_sites", account_id=account_id),
            page=AsyncSinglePage[Cf1Site],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Cf1Site,
        )

    async def delete(
        self,
        cf1_site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Cf1Site:
        """
        Deletes a specific CF1 Site for an account.

        Args:
          account_id: Identifier

          cf1_site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf1_site_id:
            raise ValueError(f"Expected a non-empty value for `cf1_site_id` but received {cf1_site_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}", account_id=account_id, cf1_site_id=cf1_site_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Cf1Site]._unwrapper,
            ),
            cast_to=cast(Type[Cf1Site], ResultWrapper[Cf1Site]),
        )

    async def get(
        self,
        cf1_site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Cf1Site:
        """
        Gets a specific CF1 Site for an account.

        Args:
          account_id: Identifier

          cf1_site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf1_site_id:
            raise ValueError(f"Expected a non-empty value for `cf1_site_id` but received {cf1_site_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}", account_id=account_id, cf1_site_id=cf1_site_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Cf1Site]._unwrapper,
            ),
            cast_to=cast(Type[Cf1Site], ResultWrapper[Cf1Site]),
        )


class Cf1SitesResourceWithRawResponse:
    def __init__(self, cf1_sites: Cf1SitesResource) -> None:
        self._cf1_sites = cf1_sites

        self.create = to_raw_response_wrapper(
            cf1_sites.create,
        )
        self.update = to_raw_response_wrapper(
            cf1_sites.update,
        )
        self.list = to_raw_response_wrapper(
            cf1_sites.list,
        )
        self.delete = to_raw_response_wrapper(
            cf1_sites.delete,
        )
        self.get = to_raw_response_wrapper(
            cf1_sites.get,
        )

    @cached_property
    def ramps(self) -> RampsResourceWithRawResponse:
        return RampsResourceWithRawResponse(self._cf1_sites.ramps)


class AsyncCf1SitesResourceWithRawResponse:
    def __init__(self, cf1_sites: AsyncCf1SitesResource) -> None:
        self._cf1_sites = cf1_sites

        self.create = async_to_raw_response_wrapper(
            cf1_sites.create,
        )
        self.update = async_to_raw_response_wrapper(
            cf1_sites.update,
        )
        self.list = async_to_raw_response_wrapper(
            cf1_sites.list,
        )
        self.delete = async_to_raw_response_wrapper(
            cf1_sites.delete,
        )
        self.get = async_to_raw_response_wrapper(
            cf1_sites.get,
        )

    @cached_property
    def ramps(self) -> AsyncRampsResourceWithRawResponse:
        return AsyncRampsResourceWithRawResponse(self._cf1_sites.ramps)


class Cf1SitesResourceWithStreamingResponse:
    def __init__(self, cf1_sites: Cf1SitesResource) -> None:
        self._cf1_sites = cf1_sites

        self.create = to_streamed_response_wrapper(
            cf1_sites.create,
        )
        self.update = to_streamed_response_wrapper(
            cf1_sites.update,
        )
        self.list = to_streamed_response_wrapper(
            cf1_sites.list,
        )
        self.delete = to_streamed_response_wrapper(
            cf1_sites.delete,
        )
        self.get = to_streamed_response_wrapper(
            cf1_sites.get,
        )

    @cached_property
    def ramps(self) -> RampsResourceWithStreamingResponse:
        return RampsResourceWithStreamingResponse(self._cf1_sites.ramps)


class AsyncCf1SitesResourceWithStreamingResponse:
    def __init__(self, cf1_sites: AsyncCf1SitesResource) -> None:
        self._cf1_sites = cf1_sites

        self.create = async_to_streamed_response_wrapper(
            cf1_sites.create,
        )
        self.update = async_to_streamed_response_wrapper(
            cf1_sites.update,
        )
        self.list = async_to_streamed_response_wrapper(
            cf1_sites.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            cf1_sites.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            cf1_sites.get,
        )

    @cached_property
    def ramps(self) -> AsyncRampsResourceWithStreamingResponse:
        return AsyncRampsResourceWithStreamingResponse(self._cf1_sites.ramps)
