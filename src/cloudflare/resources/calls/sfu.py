# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ...types.calls import sfu_create_params, sfu_update_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.calls.sfu_get_response import SFUGetResponse
from ...types.calls.sfu_list_response import SFUListResponse
from ...types.calls.sfu_create_response import SFUCreateResponse
from ...types.calls.sfu_delete_response import SFUDeleteResponse
from ...types.calls.sfu_update_response import SFUUpdateResponse

__all__ = ["SFUResource", "AsyncSFUResource"]


class SFUResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SFUResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SFUResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SFUResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SFUResourceWithStreamingResponse(self)

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
    ) -> Optional[SFUCreateResponse]:
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
            body=maybe_transform({"name": name}, sfu_create_params.SFUCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SFUCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SFUCreateResponse]], ResultWrapper[SFUCreateResponse]),
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
    ) -> Optional[SFUUpdateResponse]:
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
            body=maybe_transform({"name": name}, sfu_update_params.SFUUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SFUUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SFUUpdateResponse]], ResultWrapper[SFUUpdateResponse]),
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
    ) -> SyncSinglePage[SFUListResponse]:
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
            page=SyncSinglePage[SFUListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SFUListResponse,
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
    ) -> Optional[SFUDeleteResponse]:
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
                post_parser=ResultWrapper[Optional[SFUDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SFUDeleteResponse]], ResultWrapper[SFUDeleteResponse]),
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
    ) -> Optional[SFUGetResponse]:
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
                post_parser=ResultWrapper[Optional[SFUGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SFUGetResponse]], ResultWrapper[SFUGetResponse]),
        )


class AsyncSFUResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSFUResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSFUResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSFUResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSFUResourceWithStreamingResponse(self)

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
    ) -> Optional[SFUCreateResponse]:
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
            body=await async_maybe_transform({"name": name}, sfu_create_params.SFUCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SFUCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SFUCreateResponse]], ResultWrapper[SFUCreateResponse]),
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
    ) -> Optional[SFUUpdateResponse]:
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
            body=await async_maybe_transform({"name": name}, sfu_update_params.SFUUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SFUUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SFUUpdateResponse]], ResultWrapper[SFUUpdateResponse]),
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
    ) -> AsyncPaginator[SFUListResponse, AsyncSinglePage[SFUListResponse]]:
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
            page=AsyncSinglePage[SFUListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SFUListResponse,
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
    ) -> Optional[SFUDeleteResponse]:
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
                post_parser=ResultWrapper[Optional[SFUDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SFUDeleteResponse]], ResultWrapper[SFUDeleteResponse]),
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
    ) -> Optional[SFUGetResponse]:
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
                post_parser=ResultWrapper[Optional[SFUGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SFUGetResponse]], ResultWrapper[SFUGetResponse]),
        )


class SFUResourceWithRawResponse:
    def __init__(self, sfu: SFUResource) -> None:
        self._sfu = sfu

        self.create = to_raw_response_wrapper(
            sfu.create,
        )
        self.update = to_raw_response_wrapper(
            sfu.update,
        )
        self.list = to_raw_response_wrapper(
            sfu.list,
        )
        self.delete = to_raw_response_wrapper(
            sfu.delete,
        )
        self.get = to_raw_response_wrapper(
            sfu.get,
        )


class AsyncSFUResourceWithRawResponse:
    def __init__(self, sfu: AsyncSFUResource) -> None:
        self._sfu = sfu

        self.create = async_to_raw_response_wrapper(
            sfu.create,
        )
        self.update = async_to_raw_response_wrapper(
            sfu.update,
        )
        self.list = async_to_raw_response_wrapper(
            sfu.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sfu.delete,
        )
        self.get = async_to_raw_response_wrapper(
            sfu.get,
        )


class SFUResourceWithStreamingResponse:
    def __init__(self, sfu: SFUResource) -> None:
        self._sfu = sfu

        self.create = to_streamed_response_wrapper(
            sfu.create,
        )
        self.update = to_streamed_response_wrapper(
            sfu.update,
        )
        self.list = to_streamed_response_wrapper(
            sfu.list,
        )
        self.delete = to_streamed_response_wrapper(
            sfu.delete,
        )
        self.get = to_streamed_response_wrapper(
            sfu.get,
        )


class AsyncSFUResourceWithStreamingResponse:
    def __init__(self, sfu: AsyncSFUResource) -> None:
        self._sfu = sfu

        self.create = async_to_streamed_response_wrapper(
            sfu.create,
        )
        self.update = async_to_streamed_response_wrapper(
            sfu.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sfu.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sfu.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            sfu.get,
        )
