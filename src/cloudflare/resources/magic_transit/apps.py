# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from typing import Optional, Type

from ...types.magic_transit.app_create_response import AppCreateResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options, AsyncPaginator

from ...types.magic_transit.app_update_response import AppUpdateResponse

from ...types.magic_transit.app_list_response import AppListResponse

from ...pagination import SyncSinglePage, AsyncSinglePage

from ...types.magic_transit.app_delete_response import AppDeleteResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.magic_transit import app_create_params
from ...types.magic_transit import app_update_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["AppsResource", "AsyncAppsResource"]

class AppsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppsResourceWithRawResponse:
        return AppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppsResourceWithStreamingResponse:
        return AppsResourceWithStreamingResponse(self)

    @overload
    def create(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppCreateResponse]:
        """
        Creates a new App for an account

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppCreateResponse]:
        """
        Creates a new App for an account

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @required_args(["account_id", "body"])
    def create(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppCreateResponse]:
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._post(
            f"/accounts/{account_id}/magic/apps",
            body=maybe_transform(body, app_create_params.AppCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[AppCreateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[AppCreateResponse]], ResultWrapper[AppCreateResponse]),
        )

    @overload
    def update(self,
    account_app_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppUpdateResponse]:
        """
        Updates an Account App

        Args:
          account_id: Identifier

          account_app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def update(self,
    account_app_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppUpdateResponse]:
        """
        Updates an Account App

        Args:
          account_id: Identifier

          account_app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def update(self,
    account_app_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppUpdateResponse]:
        """
        Updates an Account App

        Args:
          account_id: Identifier

          account_app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def update(self,
    account_app_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppUpdateResponse]:
        """
        Updates an Account App

        Args:
          account_id: Identifier

          account_app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @required_args(["account_id", "body"])
    def update(self,
    account_app_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppUpdateResponse]:
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not account_app_id:
          raise ValueError(
            f'Expected a non-empty value for `account_app_id` but received {account_app_id!r}'
          )
        return self._put(
            f"/accounts/{account_id}/magic/apps/{account_app_id}",
            body=maybe_transform(body, app_update_params.AppUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[AppUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[AppUpdateResponse]], ResultWrapper[AppUpdateResponse]),
        )

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[AppListResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/magic/apps",
            page = SyncSinglePage[AppListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=cast(Any, AppListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    def delete(self,
    account_app_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppDeleteResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not account_app_id:
          raise ValueError(
            f'Expected a non-empty value for `account_app_id` but received {account_app_id!r}'
          )
        return self._delete(
            f"/accounts/{account_id}/magic/apps/{account_app_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[AppDeleteResponse]]._unwrapper),
            cast_to=cast(Type[Optional[AppDeleteResponse]], ResultWrapper[AppDeleteResponse]),
        )

class AsyncAppsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppsResourceWithRawResponse:
        return AsyncAppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppsResourceWithStreamingResponse:
        return AsyncAppsResourceWithStreamingResponse(self)

    @overload
    async def create(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppCreateResponse]:
        """
        Creates a new App for an account

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppCreateResponse]:
        """
        Creates a new App for an account

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @required_args(["account_id", "body"])
    async def create(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppCreateResponse]:
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/magic/apps",
            body=await async_maybe_transform(body, app_create_params.AppCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[AppCreateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[AppCreateResponse]], ResultWrapper[AppCreateResponse]),
        )

    @overload
    async def update(self,
    account_app_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppUpdateResponse]:
        """
        Updates an Account App

        Args:
          account_id: Identifier

          account_app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def update(self,
    account_app_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppUpdateResponse]:
        """
        Updates an Account App

        Args:
          account_id: Identifier

          account_app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def update(self,
    account_app_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppUpdateResponse]:
        """
        Updates an Account App

        Args:
          account_id: Identifier

          account_app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def update(self,
    account_app_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppUpdateResponse]:
        """
        Updates an Account App

        Args:
          account_id: Identifier

          account_app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @required_args(["account_id", "body"])
    async def update(self,
    account_app_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppUpdateResponse]:
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not account_app_id:
          raise ValueError(
            f'Expected a non-empty value for `account_app_id` but received {account_app_id!r}'
          )
        return await self._put(
            f"/accounts/{account_id}/magic/apps/{account_app_id}",
            body=await async_maybe_transform(body, app_update_params.AppUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[AppUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[AppUpdateResponse]], ResultWrapper[AppUpdateResponse]),
        )

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[AppListResponse, AsyncSinglePage[AppListResponse]]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/magic/apps",
            page = AsyncSinglePage[AppListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=cast(Any, AppListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    async def delete(self,
    account_app_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AppDeleteResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not account_app_id:
          raise ValueError(
            f'Expected a non-empty value for `account_app_id` but received {account_app_id!r}'
          )
        return await self._delete(
            f"/accounts/{account_id}/magic/apps/{account_app_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[AppDeleteResponse]]._unwrapper),
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