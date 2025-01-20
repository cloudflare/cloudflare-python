# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
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
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.magic_transit import app_create_params, app_update_params
from ...types.magic_transit.app_list_response import AppListResponse
from ...types.magic_transit.app_create_response import AppCreateResponse
from ...types.magic_transit.app_delete_response import AppDeleteResponse
from ...types.magic_transit.app_update_response import AppUpdateResponse

__all__ = ["AppsResource", "AsyncAppsResource"]


class AppsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AppsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        type: str,
        hostnames: List[str] | NotGiven = NOT_GIVEN,
        ip_subnets: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppCreateResponse]:
        """
        Creates a new App for an account

        Args:
          account_id: Identifier

          name: Display name for the app.

          type: Category of the app.

          hostnames: FQDNs to associate with traffic decisions.

          ip_subnets: CIDRs to associate with traffic decisions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/apps",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "hostnames": hostnames,
                    "ip_subnets": ip_subnets,
                },
                app_create_params.AppCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AppCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppCreateResponse]], ResultWrapper[AppCreateResponse]),
        )

    def update(
        self,
        account_app_id: str,
        *,
        account_id: str,
        hostnames: List[str] | NotGiven = NOT_GIVEN,
        ip_subnets: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppUpdateResponse]:
        """
        Updates an Account App

        Args:
          account_id: Identifier

          account_app_id: Identifier

          hostnames: FQDNs to associate with traffic decisions.

          ip_subnets: CIDRs to associate with traffic decisions.

          name: Display name for the app.

          type: Category of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not account_app_id:
            raise ValueError(f"Expected a non-empty value for `account_app_id` but received {account_app_id!r}")
        return self._put(
            f"/accounts/{account_id}/magic/apps/{account_app_id}",
            body=maybe_transform(
                {
                    "hostnames": hostnames,
                    "ip_subnets": ip_subnets,
                    "name": name,
                    "type": type,
                },
                app_update_params.AppUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AppUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppUpdateResponse]], ResultWrapper[AppUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[AppListResponse]:
        """
        Lists Apps associated with an account.

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
            f"/accounts/{account_id}/magic/apps",
            page=SyncSinglePage[AppListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, AppListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    def delete(
        self,
        account_app_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppDeleteResponse]:
        """
        Deletes specific Account App.

        Args:
          account_id: Identifier

          account_app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not account_app_id:
            raise ValueError(f"Expected a non-empty value for `account_app_id` but received {account_app_id!r}")
        return self._delete(
            f"/accounts/{account_id}/magic/apps/{account_app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AppDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppDeleteResponse]], ResultWrapper[AppDeleteResponse]),
        )


class AsyncAppsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAppsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        type: str,
        hostnames: List[str] | NotGiven = NOT_GIVEN,
        ip_subnets: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppCreateResponse]:
        """
        Creates a new App for an account

        Args:
          account_id: Identifier

          name: Display name for the app.

          type: Category of the app.

          hostnames: FQDNs to associate with traffic decisions.

          ip_subnets: CIDRs to associate with traffic decisions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/apps",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "hostnames": hostnames,
                    "ip_subnets": ip_subnets,
                },
                app_create_params.AppCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AppCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppCreateResponse]], ResultWrapper[AppCreateResponse]),
        )

    async def update(
        self,
        account_app_id: str,
        *,
        account_id: str,
        hostnames: List[str] | NotGiven = NOT_GIVEN,
        ip_subnets: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppUpdateResponse]:
        """
        Updates an Account App

        Args:
          account_id: Identifier

          account_app_id: Identifier

          hostnames: FQDNs to associate with traffic decisions.

          ip_subnets: CIDRs to associate with traffic decisions.

          name: Display name for the app.

          type: Category of the app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not account_app_id:
            raise ValueError(f"Expected a non-empty value for `account_app_id` but received {account_app_id!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/apps/{account_app_id}",
            body=await async_maybe_transform(
                {
                    "hostnames": hostnames,
                    "ip_subnets": ip_subnets,
                    "name": name,
                    "type": type,
                },
                app_update_params.AppUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AppUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppUpdateResponse]], ResultWrapper[AppUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AppListResponse, AsyncSinglePage[AppListResponse]]:
        """
        Lists Apps associated with an account.

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
            f"/accounts/{account_id}/magic/apps",
            page=AsyncSinglePage[AppListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, AppListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    async def delete(
        self,
        account_app_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppDeleteResponse]:
        """
        Deletes specific Account App.

        Args:
          account_id: Identifier

          account_app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not account_app_id:
            raise ValueError(f"Expected a non-empty value for `account_app_id` but received {account_app_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/magic/apps/{account_app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AppDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppDeleteResponse]], ResultWrapper[AppDeleteResponse]),
        )


class AppsResourceWithRawResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.create = to_raw_response_wrapper(
            apps.create,
        )
        self.update = to_raw_response_wrapper(
            apps.update,
        )
        self.list = to_raw_response_wrapper(
            apps.list,
        )
        self.delete = to_raw_response_wrapper(
            apps.delete,
        )


class AsyncAppsResourceWithRawResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.create = async_to_raw_response_wrapper(
            apps.create,
        )
        self.update = async_to_raw_response_wrapper(
            apps.update,
        )
        self.list = async_to_raw_response_wrapper(
            apps.list,
        )
        self.delete = async_to_raw_response_wrapper(
            apps.delete,
        )


class AppsResourceWithStreamingResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.create = to_streamed_response_wrapper(
            apps.create,
        )
        self.update = to_streamed_response_wrapper(
            apps.update,
        )
        self.list = to_streamed_response_wrapper(
            apps.list,
        )
        self.delete = to_streamed_response_wrapper(
            apps.delete,
        )


class AsyncAppsResourceWithStreamingResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.create = async_to_streamed_response_wrapper(
            apps.create,
        )
        self.update = async_to_streamed_response_wrapper(
            apps.update,
        )
        self.list = async_to_streamed_response_wrapper(
            apps.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            apps.delete,
        )
