# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from ..pagination import SyncSinglePage, AsyncSinglePage
from ..types.calls import call_create_params, call_update_params
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ..types.calls.calls_app import CallsApp
from ..types.calls.calls_app_with_secret import CallsAppWithSecret

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallsResourceWithRawResponse:
        return CallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallsResourceWithStreamingResponse:
        return CallsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CallsAppWithSecret]:
        """Creates a new Cloudflare calls app.

        An app is an unique enviroment where each
        Session can access all Tracks within the app.

        Args:
          account_id: The account identifier tag.

          name: A short description of Calls app, not shown to end users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/calls/apps",
            body=maybe_transform({"name": name}, call_create_params.CallCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CallsAppWithSecret]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CallsAppWithSecret]], ResultWrapper[CallsAppWithSecret]),
        )

    def update(
        self,
        app_id: str,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CallsApp]:
        """
        Edit details for a single app.

        Args:
          account_id: The account identifier tag.

          app_id: A Cloudflare-generated unique identifier for a item.

          name: A short description of Calls app, not shown to end users.

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
            f"/accounts/{account_id}/calls/apps/{app_id}",
            body=maybe_transform({"name": name}, call_update_params.CallUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CallsApp]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CallsApp]], ResultWrapper[CallsApp]),
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
    ) -> SyncSinglePage[CallsApp]:
        """
        Lists all apps in the Cloudflare account

        Args:
          account_id: The account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/calls/apps",
            page=SyncSinglePage[CallsApp],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CallsApp,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CallsApp]:
        """
        Deletes an app from Cloudflare Calls

        Args:
          account_id: The account identifier tag.

          app_id: A Cloudflare-generated unique identifier for a item.

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
            f"/accounts/{account_id}/calls/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CallsApp]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CallsApp]], ResultWrapper[CallsApp]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CallsApp]:
        """
        Fetches details for a single Calls app.

        Args:
          account_id: The account identifier tag.

          app_id: A Cloudflare-generated unique identifier for a item.

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
            f"/accounts/{account_id}/calls/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CallsApp]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CallsApp]], ResultWrapper[CallsApp]),
        )


class AsyncCallsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallsResourceWithRawResponse:
        return AsyncCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallsResourceWithStreamingResponse:
        return AsyncCallsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CallsAppWithSecret]:
        """Creates a new Cloudflare calls app.

        An app is an unique enviroment where each
        Session can access all Tracks within the app.

        Args:
          account_id: The account identifier tag.

          name: A short description of Calls app, not shown to end users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/calls/apps",
            body=await async_maybe_transform({"name": name}, call_create_params.CallCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CallsAppWithSecret]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CallsAppWithSecret]], ResultWrapper[CallsAppWithSecret]),
        )

    async def update(
        self,
        app_id: str,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CallsApp]:
        """
        Edit details for a single app.

        Args:
          account_id: The account identifier tag.

          app_id: A Cloudflare-generated unique identifier for a item.

          name: A short description of Calls app, not shown to end users.

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
            f"/accounts/{account_id}/calls/apps/{app_id}",
            body=await async_maybe_transform({"name": name}, call_update_params.CallUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CallsApp]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CallsApp]], ResultWrapper[CallsApp]),
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
    ) -> AsyncPaginator[CallsApp, AsyncSinglePage[CallsApp]]:
        """
        Lists all apps in the Cloudflare account

        Args:
          account_id: The account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/calls/apps",
            page=AsyncSinglePage[CallsApp],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CallsApp,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CallsApp]:
        """
        Deletes an app from Cloudflare Calls

        Args:
          account_id: The account identifier tag.

          app_id: A Cloudflare-generated unique identifier for a item.

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
            f"/accounts/{account_id}/calls/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CallsApp]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CallsApp]], ResultWrapper[CallsApp]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CallsApp]:
        """
        Fetches details for a single Calls app.

        Args:
          account_id: The account identifier tag.

          app_id: A Cloudflare-generated unique identifier for a item.

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
            f"/accounts/{account_id}/calls/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CallsApp]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CallsApp]], ResultWrapper[CallsApp]),
        )


class CallsResourceWithRawResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.create = to_raw_response_wrapper(
            calls.create,
        )
        self.update = to_raw_response_wrapper(
            calls.update,
        )
        self.list = to_raw_response_wrapper(
            calls.list,
        )
        self.delete = to_raw_response_wrapper(
            calls.delete,
        )
        self.get = to_raw_response_wrapper(
            calls.get,
        )


class AsyncCallsResourceWithRawResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.create = async_to_raw_response_wrapper(
            calls.create,
        )
        self.update = async_to_raw_response_wrapper(
            calls.update,
        )
        self.list = async_to_raw_response_wrapper(
            calls.list,
        )
        self.delete = async_to_raw_response_wrapper(
            calls.delete,
        )
        self.get = async_to_raw_response_wrapper(
            calls.get,
        )


class CallsResourceWithStreamingResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.create = to_streamed_response_wrapper(
            calls.create,
        )
        self.update = to_streamed_response_wrapper(
            calls.update,
        )
        self.list = to_streamed_response_wrapper(
            calls.list,
        )
        self.delete = to_streamed_response_wrapper(
            calls.delete,
        )
        self.get = to_streamed_response_wrapper(
            calls.get,
        )


class AsyncCallsResourceWithStreamingResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.create = async_to_streamed_response_wrapper(
            calls.create,
        )
        self.update = async_to_streamed_response_wrapper(
            calls.update,
        )
        self.list = async_to_streamed_response_wrapper(
            calls.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            calls.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            calls.get,
        )
