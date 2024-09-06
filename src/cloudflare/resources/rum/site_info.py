# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.rum.site import Site

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options, AsyncPaginator

from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

from typing_extensions import Literal

from ...types.rum.site_info_delete_response import SiteInfoDeleteResponse

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
from ...types import shared_params
from ...types.rum import site_info_create_params
from ...types.rum import site_info_update_params
from ...types.rum import site_info_list_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["SiteInfoResource", "AsyncSiteInfoResource"]


class SiteInfoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SiteInfoResourceWithRawResponse:
        return SiteInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SiteInfoResourceWithStreamingResponse:
        return SiteInfoResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        auto_install: bool | NotGiven = NOT_GIVEN,
        host: str | NotGiven = NOT_GIVEN,
        zone_tag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Site]:
        """
        Creates a new Web Analytics site.

        Args:
          account_id: Identifier

          auto_install: If enabled, the JavaScript snippet is automatically injected for orange-clouded
              sites.

          host: The hostname to use for gray-clouded sites.

          zone_tag: The zone identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/rum/site_info",
            body=maybe_transform(
                {
                    "auto_install": auto_install,
                    "host": host,
                    "zone_tag": zone_tag,
                },
                site_info_create_params.SiteInfoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Site]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Site]], ResultWrapper[Site]),
        )

    def update(
        self,
        site_id: str,
        *,
        account_id: str,
        auto_install: bool | NotGiven = NOT_GIVEN,
        host: str | NotGiven = NOT_GIVEN,
        zone_tag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Site]:
        """
        Updates an existing Web Analytics site.

        Args:
          account_id: Identifier

          site_id: Identifier

          auto_install: If enabled, the JavaScript snippet is automatically injected for orange-clouded
              sites.

          host: The hostname to use for gray-clouded sites.

          zone_tag: The zone identifier.

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
            f"/accounts/{account_id}/rum/site_info/{site_id}",
            body=maybe_transform(
                {
                    "auto_install": auto_install,
                    "host": host,
                    "zone_tag": zone_tag,
                },
                site_info_update_params.SiteInfoUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Site]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Site]], ResultWrapper[Site]),
        )

    def list(
        self,
        *,
        account_id: str,
        order_by: Literal["host", "created"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[Site]:
        """
        Lists all Web Analytics sites of an account.

        Args:
          account_id: Identifier

          order_by: The property used to sort the list of results.

          page: Current page within the paginated list of results.

          per_page: Number of items to return per page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/rum/site_info/list",
            page=SyncV4PagePaginationArray[Site],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order_by": order_by,
                        "page": page,
                        "per_page": per_page,
                    },
                    site_info_list_params.SiteInfoListParams,
                ),
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
    ) -> Optional[SiteInfoDeleteResponse]:
        """
        Deletes an existing Web Analytics site.

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
            f"/accounts/{account_id}/rum/site_info/{site_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SiteInfoDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SiteInfoDeleteResponse]], ResultWrapper[SiteInfoDeleteResponse]),
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
    ) -> Optional[Site]:
        """
        Retrieves a Web Analytics site.

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
            f"/accounts/{account_id}/rum/site_info/{site_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Site]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Site]], ResultWrapper[Site]),
        )


class AsyncSiteInfoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSiteInfoResourceWithRawResponse:
        return AsyncSiteInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSiteInfoResourceWithStreamingResponse:
        return AsyncSiteInfoResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        auto_install: bool | NotGiven = NOT_GIVEN,
        host: str | NotGiven = NOT_GIVEN,
        zone_tag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Site]:
        """
        Creates a new Web Analytics site.

        Args:
          account_id: Identifier

          auto_install: If enabled, the JavaScript snippet is automatically injected for orange-clouded
              sites.

          host: The hostname to use for gray-clouded sites.

          zone_tag: The zone identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/rum/site_info",
            body=await async_maybe_transform(
                {
                    "auto_install": auto_install,
                    "host": host,
                    "zone_tag": zone_tag,
                },
                site_info_create_params.SiteInfoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Site]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Site]], ResultWrapper[Site]),
        )

    async def update(
        self,
        site_id: str,
        *,
        account_id: str,
        auto_install: bool | NotGiven = NOT_GIVEN,
        host: str | NotGiven = NOT_GIVEN,
        zone_tag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Site]:
        """
        Updates an existing Web Analytics site.

        Args:
          account_id: Identifier

          site_id: Identifier

          auto_install: If enabled, the JavaScript snippet is automatically injected for orange-clouded
              sites.

          host: The hostname to use for gray-clouded sites.

          zone_tag: The zone identifier.

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
            f"/accounts/{account_id}/rum/site_info/{site_id}",
            body=await async_maybe_transform(
                {
                    "auto_install": auto_install,
                    "host": host,
                    "zone_tag": zone_tag,
                },
                site_info_update_params.SiteInfoUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Site]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Site]], ResultWrapper[Site]),
        )

    def list(
        self,
        *,
        account_id: str,
        order_by: Literal["host", "created"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Site, AsyncV4PagePaginationArray[Site]]:
        """
        Lists all Web Analytics sites of an account.

        Args:
          account_id: Identifier

          order_by: The property used to sort the list of results.

          page: Current page within the paginated list of results.

          per_page: Number of items to return per page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/rum/site_info/list",
            page=AsyncV4PagePaginationArray[Site],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order_by": order_by,
                        "page": page,
                        "per_page": per_page,
                    },
                    site_info_list_params.SiteInfoListParams,
                ),
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
    ) -> Optional[SiteInfoDeleteResponse]:
        """
        Deletes an existing Web Analytics site.

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
            f"/accounts/{account_id}/rum/site_info/{site_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SiteInfoDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SiteInfoDeleteResponse]], ResultWrapper[SiteInfoDeleteResponse]),
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
    ) -> Optional[Site]:
        """
        Retrieves a Web Analytics site.

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
            f"/accounts/{account_id}/rum/site_info/{site_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Site]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Site]], ResultWrapper[Site]),
        )


class SiteInfoResourceWithRawResponse:
    def __init__(self, site_info: SiteInfoResource) -> None:
        self._site_info = site_info

        self.create = to_raw_response_wrapper(
            site_info.create,
        )
        self.update = to_raw_response_wrapper(
            site_info.update,
        )
        self.list = to_raw_response_wrapper(
            site_info.list,
        )
        self.delete = to_raw_response_wrapper(
            site_info.delete,
        )
        self.get = to_raw_response_wrapper(
            site_info.get,
        )


class AsyncSiteInfoResourceWithRawResponse:
    def __init__(self, site_info: AsyncSiteInfoResource) -> None:
        self._site_info = site_info

        self.create = async_to_raw_response_wrapper(
            site_info.create,
        )
        self.update = async_to_raw_response_wrapper(
            site_info.update,
        )
        self.list = async_to_raw_response_wrapper(
            site_info.list,
        )
        self.delete = async_to_raw_response_wrapper(
            site_info.delete,
        )
        self.get = async_to_raw_response_wrapper(
            site_info.get,
        )


class SiteInfoResourceWithStreamingResponse:
    def __init__(self, site_info: SiteInfoResource) -> None:
        self._site_info = site_info

        self.create = to_streamed_response_wrapper(
            site_info.create,
        )
        self.update = to_streamed_response_wrapper(
            site_info.update,
        )
        self.list = to_streamed_response_wrapper(
            site_info.list,
        )
        self.delete = to_streamed_response_wrapper(
            site_info.delete,
        )
        self.get = to_streamed_response_wrapper(
            site_info.get,
        )


class AsyncSiteInfoResourceWithStreamingResponse:
    def __init__(self, site_info: AsyncSiteInfoResource) -> None:
        self._site_info = site_info

        self.create = async_to_streamed_response_wrapper(
            site_info.create,
        )
        self.update = async_to_streamed_response_wrapper(
            site_info.update,
        )
        self.list = async_to_streamed_response_wrapper(
            site_info.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            site_info.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            site_info.get,
        )
