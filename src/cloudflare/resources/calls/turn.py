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
from ...types.calls import turn_create_params, turn_update_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.calls.turn_get_response import TURNGetResponse
from ...types.calls.turn_list_response import TURNListResponse
from ...types.calls.turn_create_response import TURNCreateResponse
from ...types.calls.turn_delete_response import TURNDeleteResponse
from ...types.calls.turn_update_response import TURNUpdateResponse

__all__ = ["TURNResource", "AsyncTURNResource"]


class TURNResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TURNResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TURNResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TURNResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TURNResourceWithStreamingResponse(self)

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
    ) -> TURNCreateResponse:
        """
        Creates a new Cloudflare Calls TURN key.

        Args:
          account_id: The account identifier tag.

          name: A short description of a TURN key, not shown to end users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/calls/turn_keys",
            body=maybe_transform({"name": name}, turn_create_params.TURNCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TURNCreateResponse,
        )

    def update(
        self,
        key_id: str,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TURNUpdateResponse]:
        """
        Edit details for a single TURN key.

        Args:
          account_id: The account identifier tag.

          key_id: A Cloudflare-generated unique identifier for a item.

          name: A short description of a TURN key, not shown to end users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return self._put(
            f"/accounts/{account_id}/calls/turn_keys/{key_id}",
            body=maybe_transform({"name": name}, turn_update_params.TURNUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TURNUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TURNUpdateResponse]], ResultWrapper[TURNUpdateResponse]),
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
    ) -> SyncSinglePage[TURNListResponse]:
        """
        Lists all TURN keys in the Cloudflare account

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
            f"/accounts/{account_id}/calls/turn_keys",
            page=SyncSinglePage[TURNListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TURNListResponse,
        )

    def delete(
        self,
        key_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TURNDeleteResponse]:
        """
        Deletes a TURN key from Cloudflare Calls

        Args:
          account_id: The account identifier tag.

          key_id: A Cloudflare-generated unique identifier for a item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return self._delete(
            f"/accounts/{account_id}/calls/turn_keys/{key_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TURNDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TURNDeleteResponse]], ResultWrapper[TURNDeleteResponse]),
        )

    def get(
        self,
        key_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TURNGetResponse]:
        """
        Fetches details for a single TURN key.

        Args:
          account_id: The account identifier tag.

          key_id: A Cloudflare-generated unique identifier for a item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return self._get(
            f"/accounts/{account_id}/calls/turn_keys/{key_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TURNGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TURNGetResponse]], ResultWrapper[TURNGetResponse]),
        )


class AsyncTURNResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTURNResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTURNResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTURNResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTURNResourceWithStreamingResponse(self)

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
    ) -> TURNCreateResponse:
        """
        Creates a new Cloudflare Calls TURN key.

        Args:
          account_id: The account identifier tag.

          name: A short description of a TURN key, not shown to end users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/calls/turn_keys",
            body=await async_maybe_transform({"name": name}, turn_create_params.TURNCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TURNCreateResponse,
        )

    async def update(
        self,
        key_id: str,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TURNUpdateResponse]:
        """
        Edit details for a single TURN key.

        Args:
          account_id: The account identifier tag.

          key_id: A Cloudflare-generated unique identifier for a item.

          name: A short description of a TURN key, not shown to end users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return await self._put(
            f"/accounts/{account_id}/calls/turn_keys/{key_id}",
            body=await async_maybe_transform({"name": name}, turn_update_params.TURNUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TURNUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TURNUpdateResponse]], ResultWrapper[TURNUpdateResponse]),
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
    ) -> AsyncPaginator[TURNListResponse, AsyncSinglePage[TURNListResponse]]:
        """
        Lists all TURN keys in the Cloudflare account

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
            f"/accounts/{account_id}/calls/turn_keys",
            page=AsyncSinglePage[TURNListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TURNListResponse,
        )

    async def delete(
        self,
        key_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TURNDeleteResponse]:
        """
        Deletes a TURN key from Cloudflare Calls

        Args:
          account_id: The account identifier tag.

          key_id: A Cloudflare-generated unique identifier for a item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/calls/turn_keys/{key_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TURNDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TURNDeleteResponse]], ResultWrapper[TURNDeleteResponse]),
        )

    async def get(
        self,
        key_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TURNGetResponse]:
        """
        Fetches details for a single TURN key.

        Args:
          account_id: The account identifier tag.

          key_id: A Cloudflare-generated unique identifier for a item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return await self._get(
            f"/accounts/{account_id}/calls/turn_keys/{key_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TURNGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TURNGetResponse]], ResultWrapper[TURNGetResponse]),
        )


class TURNResourceWithRawResponse:
    def __init__(self, turn: TURNResource) -> None:
        self._turn = turn

        self.create = to_raw_response_wrapper(
            turn.create,
        )
        self.update = to_raw_response_wrapper(
            turn.update,
        )
        self.list = to_raw_response_wrapper(
            turn.list,
        )
        self.delete = to_raw_response_wrapper(
            turn.delete,
        )
        self.get = to_raw_response_wrapper(
            turn.get,
        )


class AsyncTURNResourceWithRawResponse:
    def __init__(self, turn: AsyncTURNResource) -> None:
        self._turn = turn

        self.create = async_to_raw_response_wrapper(
            turn.create,
        )
        self.update = async_to_raw_response_wrapper(
            turn.update,
        )
        self.list = async_to_raw_response_wrapper(
            turn.list,
        )
        self.delete = async_to_raw_response_wrapper(
            turn.delete,
        )
        self.get = async_to_raw_response_wrapper(
            turn.get,
        )


class TURNResourceWithStreamingResponse:
    def __init__(self, turn: TURNResource) -> None:
        self._turn = turn

        self.create = to_streamed_response_wrapper(
            turn.create,
        )
        self.update = to_streamed_response_wrapper(
            turn.update,
        )
        self.list = to_streamed_response_wrapper(
            turn.list,
        )
        self.delete = to_streamed_response_wrapper(
            turn.delete,
        )
        self.get = to_streamed_response_wrapper(
            turn.get,
        )


class AsyncTURNResourceWithStreamingResponse:
    def __init__(self, turn: AsyncTURNResource) -> None:
        self._turn = turn

        self.create = async_to_streamed_response_wrapper(
            turn.create,
        )
        self.update = async_to_streamed_response_wrapper(
            turn.update,
        )
        self.list = async_to_streamed_response_wrapper(
            turn.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            turn.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            turn.get,
        )
