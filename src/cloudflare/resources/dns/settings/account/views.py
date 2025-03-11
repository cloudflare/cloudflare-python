# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .....types.dns.settings.account import view_edit_params, view_list_params, view_create_params
from .....types.dns.settings.account.view_get_response import ViewGetResponse
from .....types.dns.settings.account.view_edit_response import ViewEditResponse
from .....types.dns.settings.account.view_list_response import ViewListResponse
from .....types.dns.settings.account.view_create_response import ViewCreateResponse
from .....types.dns.settings.account.view_delete_response import ViewDeleteResponse

__all__ = ["ViewsResource", "AsyncViewsResource"]


class ViewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ViewsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        zones: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ViewCreateResponse]:
        """
        Create Internal DNS View for an account

        Args:
          account_id: Identifier

          name: The name of the view.

          zones: The list of zones linked to this view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/dns_settings/views",
            body=maybe_transform(
                {
                    "name": name,
                    "zones": zones,
                },
                view_create_params.ViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ViewCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ViewCreateResponse]], ResultWrapper[ViewCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        name: view_list_params.Name | NotGiven = NOT_GIVEN,
        order: Literal["name", "created_on", "modified_on"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        zone_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[ViewListResponse]:
        """
        List DNS Internal Views for an Account

        Args:
          account_id: Identifier

          direction: Direction to order DNS views in.

          match: Whether to match all search requirements or at least one (any). If set to `all`,
              acts like a logical AND between filters. If set to `any`, acts like a logical OR
              instead.

          order: Field to order DNS views by.

          page: Page number of paginated results.

          per_page: Number of DNS views per page.

          zone_id: A zone ID that exists in the zones list for the view.

          zone_name: A zone name that exists in the zones list for the view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dns_settings/views",
            page=SyncV4PagePaginationArray[ViewListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "match": match,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "zone_id": zone_id,
                        "zone_name": zone_name,
                    },
                    view_list_params.ViewListParams,
                ),
            ),
            model=ViewListResponse,
        )

    def delete(
        self,
        view_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ViewDeleteResponse]:
        """
        Delete an existing Internal DNS View

        Args:
          account_id: Identifier

          view_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return self._delete(
            f"/accounts/{account_id}/dns_settings/views/{view_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ViewDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ViewDeleteResponse]], ResultWrapper[ViewDeleteResponse]),
        )

    def edit(
        self,
        view_id: str,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        zones: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ViewEditResponse]:
        """
        Update an existing Internal DNS View

        Args:
          account_id: Identifier

          view_id: Identifier

          name: The name of the view.

          zones: The list of zones linked to this view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return self._patch(
            f"/accounts/{account_id}/dns_settings/views/{view_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "zones": zones,
                },
                view_edit_params.ViewEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ViewEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ViewEditResponse]], ResultWrapper[ViewEditResponse]),
        )

    def get(
        self,
        view_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ViewGetResponse]:
        """
        Get DNS Internal View

        Args:
          account_id: Identifier

          view_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return self._get(
            f"/accounts/{account_id}/dns_settings/views/{view_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ViewGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ViewGetResponse]], ResultWrapper[ViewGetResponse]),
        )


class AsyncViewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncViewsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        zones: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ViewCreateResponse]:
        """
        Create Internal DNS View for an account

        Args:
          account_id: Identifier

          name: The name of the view.

          zones: The list of zones linked to this view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/dns_settings/views",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "zones": zones,
                },
                view_create_params.ViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ViewCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ViewCreateResponse]], ResultWrapper[ViewCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        name: view_list_params.Name | NotGiven = NOT_GIVEN,
        order: Literal["name", "created_on", "modified_on"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        zone_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ViewListResponse, AsyncV4PagePaginationArray[ViewListResponse]]:
        """
        List DNS Internal Views for an Account

        Args:
          account_id: Identifier

          direction: Direction to order DNS views in.

          match: Whether to match all search requirements or at least one (any). If set to `all`,
              acts like a logical AND between filters. If set to `any`, acts like a logical OR
              instead.

          order: Field to order DNS views by.

          page: Page number of paginated results.

          per_page: Number of DNS views per page.

          zone_id: A zone ID that exists in the zones list for the view.

          zone_name: A zone name that exists in the zones list for the view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dns_settings/views",
            page=AsyncV4PagePaginationArray[ViewListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "match": match,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "zone_id": zone_id,
                        "zone_name": zone_name,
                    },
                    view_list_params.ViewListParams,
                ),
            ),
            model=ViewListResponse,
        )

    async def delete(
        self,
        view_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ViewDeleteResponse]:
        """
        Delete an existing Internal DNS View

        Args:
          account_id: Identifier

          view_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/dns_settings/views/{view_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ViewDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ViewDeleteResponse]], ResultWrapper[ViewDeleteResponse]),
        )

    async def edit(
        self,
        view_id: str,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        zones: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ViewEditResponse]:
        """
        Update an existing Internal DNS View

        Args:
          account_id: Identifier

          view_id: Identifier

          name: The name of the view.

          zones: The list of zones linked to this view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/dns_settings/views/{view_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "zones": zones,
                },
                view_edit_params.ViewEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ViewEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ViewEditResponse]], ResultWrapper[ViewEditResponse]),
        )

    async def get(
        self,
        view_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ViewGetResponse]:
        """
        Get DNS Internal View

        Args:
          account_id: Identifier

          view_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dns_settings/views/{view_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ViewGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ViewGetResponse]], ResultWrapper[ViewGetResponse]),
        )


class ViewsResourceWithRawResponse:
    def __init__(self, views: ViewsResource) -> None:
        self._views = views

        self.create = to_raw_response_wrapper(
            views.create,
        )
        self.list = to_raw_response_wrapper(
            views.list,
        )
        self.delete = to_raw_response_wrapper(
            views.delete,
        )
        self.edit = to_raw_response_wrapper(
            views.edit,
        )
        self.get = to_raw_response_wrapper(
            views.get,
        )


class AsyncViewsResourceWithRawResponse:
    def __init__(self, views: AsyncViewsResource) -> None:
        self._views = views

        self.create = async_to_raw_response_wrapper(
            views.create,
        )
        self.list = async_to_raw_response_wrapper(
            views.list,
        )
        self.delete = async_to_raw_response_wrapper(
            views.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            views.edit,
        )
        self.get = async_to_raw_response_wrapper(
            views.get,
        )


class ViewsResourceWithStreamingResponse:
    def __init__(self, views: ViewsResource) -> None:
        self._views = views

        self.create = to_streamed_response_wrapper(
            views.create,
        )
        self.list = to_streamed_response_wrapper(
            views.list,
        )
        self.delete = to_streamed_response_wrapper(
            views.delete,
        )
        self.edit = to_streamed_response_wrapper(
            views.edit,
        )
        self.get = to_streamed_response_wrapper(
            views.get,
        )


class AsyncViewsResourceWithStreamingResponse:
    def __init__(self, views: AsyncViewsResource) -> None:
        self._views = views

        self.create = async_to_streamed_response_wrapper(
            views.create,
        )
        self.list = async_to_streamed_response_wrapper(
            views.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            views.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            views.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            views.get,
        )
