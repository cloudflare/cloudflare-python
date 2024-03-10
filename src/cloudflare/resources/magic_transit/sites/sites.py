# File generated from our OpenAPI spec by Stainless.

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
    Lans,
    AsyncLans,
    LansWithRawResponse,
    AsyncLansWithRawResponse,
    LansWithStreamingResponse,
    AsyncLansWithStreamingResponse,
)
from .wans import (
    Wans,
    AsyncWans,
    WansWithRawResponse,
    AsyncWansWithRawResponse,
    WansWithStreamingResponse,
    AsyncWansWithStreamingResponse,
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
from ...._base_client import (
    make_request_options,
)
from ....types.magic_transit import (
    SiteGetResponse,
    SiteListResponse,
    SiteCreateResponse,
    SiteDeleteResponse,
    SiteUpdateResponse,
    site_create_params,
    site_update_params,
)

__all__ = ["Sites", "AsyncSites"]


class Sites(SyncAPIResource):
    @cached_property
    def acls(self) -> ACLs:
        return ACLs(self._client)

    @cached_property
    def lans(self) -> Lans:
        return Lans(self._client)

    @cached_property
    def wans(self) -> Wans:
        return Wans(self._client)

    @cached_property
    def with_raw_response(self) -> SitesWithRawResponse:
        return SitesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SitesWithStreamingResponse:
        return SitesWithStreamingResponse(self)

    def create(
        self,
        account_identifier: str,
        *,
        site: site_create_params.Site | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiteCreateResponse:
        """
        Creates a new Site

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
            f"/accounts/{account_identifier}/magic/sites",
            body=maybe_transform({"site": site}, site_create_params.SiteCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SiteCreateResponse], ResultWrapper[SiteCreateResponse]),
        )

    def update(
        self,
        site_identifier: str,
        *,
        account_identifier: str,
        site: site_update_params.Site | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiteUpdateResponse:
        """
        Update a specific Site.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        return self._put(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}",
            body=maybe_transform({"site": site}, site_update_params.SiteUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SiteUpdateResponse], ResultWrapper[SiteUpdateResponse]),
        )

    def list(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiteListResponse:
        """Lists Sites associated with an account.

        Use connector_identifier query param to
        return sites where connector_identifier matches either site.ConnectorID or
        site.SecondaryConnectorID.

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
            f"/accounts/{account_identifier}/magic/sites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SiteListResponse], ResultWrapper[SiteListResponse]),
        )

    def delete(
        self,
        site_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiteDeleteResponse:
        """
        Remove a specific Site.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        return self._delete(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SiteDeleteResponse], ResultWrapper[SiteDeleteResponse]),
        )

    def get(
        self,
        site_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiteGetResponse:
        """
        Get a specific Site.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SiteGetResponse], ResultWrapper[SiteGetResponse]),
        )


class AsyncSites(AsyncAPIResource):
    @cached_property
    def acls(self) -> AsyncACLs:
        return AsyncACLs(self._client)

    @cached_property
    def lans(self) -> AsyncLans:
        return AsyncLans(self._client)

    @cached_property
    def wans(self) -> AsyncWans:
        return AsyncWans(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSitesWithRawResponse:
        return AsyncSitesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSitesWithStreamingResponse:
        return AsyncSitesWithStreamingResponse(self)

    async def create(
        self,
        account_identifier: str,
        *,
        site: site_create_params.Site | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiteCreateResponse:
        """
        Creates a new Site

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
            f"/accounts/{account_identifier}/magic/sites",
            body=await async_maybe_transform({"site": site}, site_create_params.SiteCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SiteCreateResponse], ResultWrapper[SiteCreateResponse]),
        )

    async def update(
        self,
        site_identifier: str,
        *,
        account_identifier: str,
        site: site_update_params.Site | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiteUpdateResponse:
        """
        Update a specific Site.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        return await self._put(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}",
            body=await async_maybe_transform({"site": site}, site_update_params.SiteUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SiteUpdateResponse], ResultWrapper[SiteUpdateResponse]),
        )

    async def list(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiteListResponse:
        """Lists Sites associated with an account.

        Use connector_identifier query param to
        return sites where connector_identifier matches either site.ConnectorID or
        site.SecondaryConnectorID.

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
            f"/accounts/{account_identifier}/magic/sites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SiteListResponse], ResultWrapper[SiteListResponse]),
        )

    async def delete(
        self,
        site_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiteDeleteResponse:
        """
        Remove a specific Site.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        return await self._delete(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SiteDeleteResponse], ResultWrapper[SiteDeleteResponse]),
        )

    async def get(
        self,
        site_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiteGetResponse:
        """
        Get a specific Site.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SiteGetResponse], ResultWrapper[SiteGetResponse]),
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
    def lans(self) -> LansWithRawResponse:
        return LansWithRawResponse(self._sites.lans)

    @cached_property
    def wans(self) -> WansWithRawResponse:
        return WansWithRawResponse(self._sites.wans)


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
    def lans(self) -> AsyncLansWithRawResponse:
        return AsyncLansWithRawResponse(self._sites.lans)

    @cached_property
    def wans(self) -> AsyncWansWithRawResponse:
        return AsyncWansWithRawResponse(self._sites.wans)


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
    def lans(self) -> LansWithStreamingResponse:
        return LansWithStreamingResponse(self._sites.lans)

    @cached_property
    def wans(self) -> WansWithStreamingResponse:
        return WansWithStreamingResponse(self._sites.wans)


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
    def lans(self) -> AsyncLansWithStreamingResponse:
        return AsyncLansWithStreamingResponse(self._sites.lans)

    @cached_property
    def wans(self) -> AsyncWansWithStreamingResponse:
        return AsyncWansWithStreamingResponse(self._sites.wans)
