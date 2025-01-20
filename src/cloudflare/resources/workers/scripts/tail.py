# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

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
from ...._base_client import make_request_options
from ....types.workers.scripts import tail_create_params
from ....types.workers.scripts.tail_get_response import TailGetResponse
from ....types.workers.scripts.tail_create_response import TailCreateResponse
from ....types.workers.scripts.tail_delete_response import TailDeleteResponse

__all__ = ["TailResource", "AsyncTailResource"]


class TailResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TailResourceWithStreamingResponse(self)

    def create(
        self,
        script_name: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TailCreateResponse]:
        """
        Starts a tail that receives logs and exception from a Worker.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._post(
            f"/accounts/{account_id}/workers/scripts/{script_name}/tails",
            body=maybe_transform(body, tail_create_params.TailCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TailCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TailCreateResponse]], ResultWrapper[TailCreateResponse]),
        )

    def delete(
        self,
        id: str,
        *,
        account_id: str,
        script_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TailDeleteResponse:
        """
        Deletes a tail from a Worker.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          id: Identifier for the tail.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/accounts/{account_id}/workers/scripts/{script_name}/tails/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TailDeleteResponse,
        )

    def get(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TailGetResponse]:
        """
        Get list of tails currently deployed on a Worker.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/tails",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TailGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TailGetResponse]], ResultWrapper[TailGetResponse]),
        )


class AsyncTailResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTailResourceWithStreamingResponse(self)

    async def create(
        self,
        script_name: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TailCreateResponse]:
        """
        Starts a tail that receives logs and exception from a Worker.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._post(
            f"/accounts/{account_id}/workers/scripts/{script_name}/tails",
            body=await async_maybe_transform(body, tail_create_params.TailCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TailCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TailCreateResponse]], ResultWrapper[TailCreateResponse]),
        )

    async def delete(
        self,
        id: str,
        *,
        account_id: str,
        script_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TailDeleteResponse:
        """
        Deletes a tail from a Worker.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          id: Identifier for the tail.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/accounts/{account_id}/workers/scripts/{script_name}/tails/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TailDeleteResponse,
        )

    async def get(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TailGetResponse]:
        """
        Get list of tails currently deployed on a Worker.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/tails",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TailGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TailGetResponse]], ResultWrapper[TailGetResponse]),
        )


class TailResourceWithRawResponse:
    def __init__(self, tail: TailResource) -> None:
        self._tail = tail

        self.create = to_raw_response_wrapper(
            tail.create,
        )
        self.delete = to_raw_response_wrapper(
            tail.delete,
        )
        self.get = to_raw_response_wrapper(
            tail.get,
        )


class AsyncTailResourceWithRawResponse:
    def __init__(self, tail: AsyncTailResource) -> None:
        self._tail = tail

        self.create = async_to_raw_response_wrapper(
            tail.create,
        )
        self.delete = async_to_raw_response_wrapper(
            tail.delete,
        )
        self.get = async_to_raw_response_wrapper(
            tail.get,
        )


class TailResourceWithStreamingResponse:
    def __init__(self, tail: TailResource) -> None:
        self._tail = tail

        self.create = to_streamed_response_wrapper(
            tail.create,
        )
        self.delete = to_streamed_response_wrapper(
            tail.delete,
        )
        self.get = to_streamed_response_wrapper(
            tail.get,
        )


class AsyncTailResourceWithStreamingResponse:
    def __init__(self, tail: AsyncTailResource) -> None:
        self._tail = tail

        self.create = async_to_streamed_response_wrapper(
            tail.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            tail.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            tail.get,
        )
