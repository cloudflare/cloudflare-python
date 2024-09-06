# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .turn.turn import TURNResource, AsyncTURNResource

from ..._compat import cached_property

from ...types.calls.calls_app_with_secret import CallsAppWithSecret

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options, AsyncPaginator

from ...types.calls.calls_app import CallsApp

from ...pagination import SyncSinglePage, AsyncSinglePage

from ...types.calls.call_list_response import CallListResponse

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
from ...types.calls import call_create_params
from ...types.calls import call_update_params
from .turn import (
    TURNResource,
    AsyncTURNResource,
    TURNResourceWithRawResponse,
    AsyncTURNResourceWithRawResponse,
    TURNResourceWithStreamingResponse,
    AsyncTURNResourceWithStreamingResponse,
)
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
    @cached_property
    def turn(self) -> TURNResource:
        return TURNResource(self._client)

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
    ) -> SyncSinglePage[CallListResponse]:
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
            page=SyncSinglePage[CallListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=str,
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
    def turn(self) -> AsyncTURNResource:
        return AsyncTURNResource(self._client)

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
    ) -> AsyncPaginator[CallListResponse, AsyncSinglePage[CallListResponse]]:
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
            page=AsyncSinglePage[CallListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=str,
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

    @cached_property
    def turn(self) -> TURNResourceWithRawResponse:
        return TURNResourceWithRawResponse(self._calls.turn)


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

    @cached_property
    def turn(self) -> AsyncTURNResourceWithRawResponse:
        return AsyncTURNResourceWithRawResponse(self._calls.turn)


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

    @cached_property
    def turn(self) -> TURNResourceWithStreamingResponse:
        return TURNResourceWithStreamingResponse(self._calls.turn)


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

    @cached_property
    def turn(self) -> AsyncTURNResourceWithStreamingResponse:
        return AsyncTURNResourceWithStreamingResponse(self._calls.turn)
