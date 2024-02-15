# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.workers.scripts import (
    TailDeleteResponse,
    TailWorkerTailLogsListTailsResponse,
    TailWorkerTailLogsStartTailResponse,
)

from typing import Type

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Tails", "AsyncTails"]


class Tails(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TailsWithRawResponse:
        return TailsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TailsWithStreamingResponse:
        return TailsWithStreamingResponse(self)

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
        return cast(
            TailDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/workers/scripts/{script_name}/tails/{id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TailDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def worker_tail_logs_list_tails(
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
    ) -> TailWorkerTailLogsListTailsResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TailWorkerTailLogsListTailsResponse], ResultWrapper[TailWorkerTailLogsListTailsResponse]),
        )

    def worker_tail_logs_start_tail(
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
    ) -> TailWorkerTailLogsStartTailResponse:
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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TailWorkerTailLogsStartTailResponse], ResultWrapper[TailWorkerTailLogsStartTailResponse]),
        )


class AsyncTails(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTailsWithRawResponse:
        return AsyncTailsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTailsWithStreamingResponse:
        return AsyncTailsWithStreamingResponse(self)

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
        return cast(
            TailDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/workers/scripts/{script_name}/tails/{id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TailDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def worker_tail_logs_list_tails(
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
    ) -> TailWorkerTailLogsListTailsResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TailWorkerTailLogsListTailsResponse], ResultWrapper[TailWorkerTailLogsListTailsResponse]),
        )

    async def worker_tail_logs_start_tail(
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
    ) -> TailWorkerTailLogsStartTailResponse:
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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TailWorkerTailLogsStartTailResponse], ResultWrapper[TailWorkerTailLogsStartTailResponse]),
        )


class TailsWithRawResponse:
    def __init__(self, tails: Tails) -> None:
        self._tails = tails

        self.delete = to_raw_response_wrapper(
            tails.delete,
        )
        self.worker_tail_logs_list_tails = to_raw_response_wrapper(
            tails.worker_tail_logs_list_tails,
        )
        self.worker_tail_logs_start_tail = to_raw_response_wrapper(
            tails.worker_tail_logs_start_tail,
        )


class AsyncTailsWithRawResponse:
    def __init__(self, tails: AsyncTails) -> None:
        self._tails = tails

        self.delete = async_to_raw_response_wrapper(
            tails.delete,
        )
        self.worker_tail_logs_list_tails = async_to_raw_response_wrapper(
            tails.worker_tail_logs_list_tails,
        )
        self.worker_tail_logs_start_tail = async_to_raw_response_wrapper(
            tails.worker_tail_logs_start_tail,
        )


class TailsWithStreamingResponse:
    def __init__(self, tails: Tails) -> None:
        self._tails = tails

        self.delete = to_streamed_response_wrapper(
            tails.delete,
        )
        self.worker_tail_logs_list_tails = to_streamed_response_wrapper(
            tails.worker_tail_logs_list_tails,
        )
        self.worker_tail_logs_start_tail = to_streamed_response_wrapper(
            tails.worker_tail_logs_start_tail,
        )


class AsyncTailsWithStreamingResponse:
    def __init__(self, tails: AsyncTails) -> None:
        self._tails = tails

        self.delete = async_to_streamed_response_wrapper(
            tails.delete,
        )
        self.worker_tail_logs_list_tails = async_to_streamed_response_wrapper(
            tails.worker_tail_logs_list_tails,
        )
        self.worker_tail_logs_start_tail = async_to_streamed_response_wrapper(
            tails.worker_tail_logs_start_tail,
        )
