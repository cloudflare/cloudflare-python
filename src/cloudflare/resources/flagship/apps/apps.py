# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from .evaluate import (
    EvaluateResource,
    AsyncEvaluateResource,
    EvaluateResourceWithRawResponse,
    AsyncEvaluateResourceWithRawResponse,
    EvaluateResourceWithStreamingResponse,
    AsyncEvaluateResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .flags.flags import (
    FlagsResource,
    AsyncFlagsResource,
    FlagsResourceWithRawResponse,
    AsyncFlagsResourceWithRawResponse,
    FlagsResourceWithStreamingResponse,
    AsyncFlagsResourceWithStreamingResponse,
)
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
from ....types.flagship import app_create_params, app_update_params
from ....types.flagship.app_get_response import AppGetResponse
from ....types.flagship.app_list_response import AppListResponse
from ....types.flagship.app_create_response import AppCreateResponse
from ....types.flagship.app_delete_response import AppDeleteResponse
from ....types.flagship.app_update_response import AppUpdateResponse

__all__ = ["AppsResource", "AsyncAppsResource"]


class AppsResource(SyncAPIResource):
    @cached_property
    def flags(self) -> FlagsResource:
        return FlagsResource(self._client)

    @cached_property
    def evaluate(self) -> EvaluateResource:
        return EvaluateResource(self._client)

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppCreateResponse:
        """Creates an app.

        The returned `id` is used in all subsequent flag, changelog, and
        evaluation requests.

        Args:
          account_id: Cloudflare account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/flagship/apps", account_id=account_id),
            body=maybe_transform({"name": name}, app_create_params.AppCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AppCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[AppCreateResponse], ResultWrapper[AppCreateResponse]),
        )

    def update(
        self,
        app_id: str,
        *,
        account_id: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppUpdateResponse:
        """Updates an app.

        Only `name` is mutable.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._put(
            path_template("/accounts/{account_id}/flagship/apps/{app_id}", account_id=account_id, app_id=app_id),
            body=maybe_transform({"name": name}, app_update_params.AppUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AppUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[AppUpdateResponse], ResultWrapper[AppUpdateResponse]),
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
    ) -> SyncSinglePage[AppListResponse]:
        """Lists all apps in the account.

        Returns identity and audit fields only — flag
        definitions are not included.

        Args:
          account_id: Cloudflare account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/flagship/apps", account_id=account_id),
            page=SyncSinglePage[AppListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AppListResponse,
        )

    def delete(
        self,
        app_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppDeleteResponse:
        """Deletes an app and all its flags and changelog history.

        Returns 409 if any
        Worker still references this app via a Flagship binding.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._delete(
            path_template("/accounts/{account_id}/flagship/apps/{app_id}", account_id=account_id, app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AppDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[AppDeleteResponse], ResultWrapper[AppDeleteResponse]),
        )

    def get(
        self,
        app_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppGetResponse:
        """Returns an app's name and audit fields.

        Flag definitions are not included.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/flagship/apps/{app_id}", account_id=account_id, app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AppGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AppGetResponse], ResultWrapper[AppGetResponse]),
        )


class AsyncAppsResource(AsyncAPIResource):
    @cached_property
    def flags(self) -> AsyncFlagsResource:
        return AsyncFlagsResource(self._client)

    @cached_property
    def evaluate(self) -> AsyncEvaluateResource:
        return AsyncEvaluateResource(self._client)

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppCreateResponse:
        """Creates an app.

        The returned `id` is used in all subsequent flag, changelog, and
        evaluation requests.

        Args:
          account_id: Cloudflare account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/flagship/apps", account_id=account_id),
            body=await async_maybe_transform({"name": name}, app_create_params.AppCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AppCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[AppCreateResponse], ResultWrapper[AppCreateResponse]),
        )

    async def update(
        self,
        app_id: str,
        *,
        account_id: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppUpdateResponse:
        """Updates an app.

        Only `name` is mutable.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._put(
            path_template("/accounts/{account_id}/flagship/apps/{app_id}", account_id=account_id, app_id=app_id),
            body=await async_maybe_transform({"name": name}, app_update_params.AppUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AppUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[AppUpdateResponse], ResultWrapper[AppUpdateResponse]),
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
    ) -> AsyncPaginator[AppListResponse, AsyncSinglePage[AppListResponse]]:
        """Lists all apps in the account.

        Returns identity and audit fields only — flag
        definitions are not included.

        Args:
          account_id: Cloudflare account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/flagship/apps", account_id=account_id),
            page=AsyncSinglePage[AppListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AppListResponse,
        )

    async def delete(
        self,
        app_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppDeleteResponse:
        """Deletes an app and all its flags and changelog history.

        Returns 409 if any
        Worker still references this app via a Flagship binding.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._delete(
            path_template("/accounts/{account_id}/flagship/apps/{app_id}", account_id=account_id, app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AppDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[AppDeleteResponse], ResultWrapper[AppDeleteResponse]),
        )

    async def get(
        self,
        app_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppGetResponse:
        """Returns an app's name and audit fields.

        Flag definitions are not included.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/flagship/apps/{app_id}", account_id=account_id, app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AppGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AppGetResponse], ResultWrapper[AppGetResponse]),
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
        self.get = to_raw_response_wrapper(
            apps.get,
        )

    @cached_property
    def flags(self) -> FlagsResourceWithRawResponse:
        return FlagsResourceWithRawResponse(self._apps.flags)

    @cached_property
    def evaluate(self) -> EvaluateResourceWithRawResponse:
        return EvaluateResourceWithRawResponse(self._apps.evaluate)


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
        self.get = async_to_raw_response_wrapper(
            apps.get,
        )

    @cached_property
    def flags(self) -> AsyncFlagsResourceWithRawResponse:
        return AsyncFlagsResourceWithRawResponse(self._apps.flags)

    @cached_property
    def evaluate(self) -> AsyncEvaluateResourceWithRawResponse:
        return AsyncEvaluateResourceWithRawResponse(self._apps.evaluate)


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
        self.get = to_streamed_response_wrapper(
            apps.get,
        )

    @cached_property
    def flags(self) -> FlagsResourceWithStreamingResponse:
        return FlagsResourceWithStreamingResponse(self._apps.flags)

    @cached_property
    def evaluate(self) -> EvaluateResourceWithStreamingResponse:
        return EvaluateResourceWithStreamingResponse(self._apps.evaluate)


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
        self.get = async_to_streamed_response_wrapper(
            apps.get,
        )

    @cached_property
    def flags(self) -> AsyncFlagsResourceWithStreamingResponse:
        return AsyncFlagsResourceWithStreamingResponse(self._apps.flags)

    @cached_property
    def evaluate(self) -> AsyncEvaluateResourceWithStreamingResponse:
        return AsyncEvaluateResourceWithStreamingResponse(self._apps.evaluate)
