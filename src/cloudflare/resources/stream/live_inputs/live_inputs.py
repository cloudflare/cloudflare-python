# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .outputs import Outputs, AsyncOutputs

from ...._compat import cached_property

from ....types.stream import (
    LiveInputUpdateResponse,
    LiveInputGetResponse,
    LiveInputStreamLiveInputsCreateALiveInputResponse,
    LiveInputStreamLiveInputsListLiveInputsResponse,
    live_input_update_params,
    live_input_stream_live_inputs_create_a_live_input_params,
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
from ....types.stream import live_input_update_params
from ....types.stream import live_input_stream_live_inputs_create_a_live_input_params
from ....types.stream import live_input_stream_live_inputs_list_live_inputs_params
from .outputs import (
    Outputs,
    AsyncOutputs,
    OutputsWithRawResponse,
    AsyncOutputsWithRawResponse,
    OutputsWithStreamingResponse,
    AsyncOutputsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["LiveInputs", "AsyncLiveInputs"]


class LiveInputs(SyncAPIResource):
    @cached_property
    def outputs(self) -> Outputs:
        return Outputs(self._client)

    @cached_property
    def with_raw_response(self) -> LiveInputsWithRawResponse:
        return LiveInputsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LiveInputsWithStreamingResponse:
        return LiveInputsWithStreamingResponse(self)

    def update(
        self,
        live_input_identifier: str,
        *,
        account_id: str,
        default_creator: str | NotGiven = NOT_GIVEN,
        delete_recording_after_days: float | NotGiven = NOT_GIVEN,
        meta: object | NotGiven = NOT_GIVEN,
        recording: live_input_update_params.Recording | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiveInputUpdateResponse:
        """
        Updates a specified live input.

        Args:
          account_id: Identifier

          live_input_identifier: A unique identifier for a live input.

          default_creator: Sets the creator ID asssociated with this live input.

          delete_recording_after_days: Indicates the number of days after which the live inputs recordings will be
              deleted. When a stream completes and the recording is ready, the value is used
              to calculate a scheduled deletion date for that recording. Omit the field to
              indicate no change, or include with a `null` value to remove an existing
              scheduled deletion.

          meta: A user modifiable key-value store used to reference other systems of record for
              managing live inputs.

          recording: Records the input to a Cloudflare Stream video. Behavior depends on the mode. In
              most cases, the video will initially be viewable as a live video and transition
              to on-demand after a condition is satisfied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not live_input_identifier:
            raise ValueError(
                f"Expected a non-empty value for `live_input_identifier` but received {live_input_identifier!r}"
            )
        return self._put(
            f"/accounts/{account_id}/stream/live_inputs/{live_input_identifier}",
            body=maybe_transform(
                {
                    "default_creator": default_creator,
                    "delete_recording_after_days": delete_recording_after_days,
                    "meta": meta,
                    "recording": recording,
                },
                live_input_update_params.LiveInputUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LiveInputUpdateResponse], ResultWrapper[LiveInputUpdateResponse]),
        )

    def delete(
        self,
        live_input_identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Prevents a live input from being streamed to and makes the live input
        inaccessible to any future API calls.

        Args:
          account_id: Identifier

          live_input_identifier: A unique identifier for a live input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not live_input_identifier:
            raise ValueError(
                f"Expected a non-empty value for `live_input_identifier` but received {live_input_identifier!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/stream/live_inputs/{live_input_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        live_input_identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiveInputGetResponse:
        """
        Retrieves details of an existing live input.

        Args:
          account_id: Identifier

          live_input_identifier: A unique identifier for a live input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not live_input_identifier:
            raise ValueError(
                f"Expected a non-empty value for `live_input_identifier` but received {live_input_identifier!r}"
            )
        return self._get(
            f"/accounts/{account_id}/stream/live_inputs/{live_input_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LiveInputGetResponse], ResultWrapper[LiveInputGetResponse]),
        )

    def stream_live_inputs_create_a_live_input(
        self,
        account_id: str,
        *,
        default_creator: str | NotGiven = NOT_GIVEN,
        delete_recording_after_days: float | NotGiven = NOT_GIVEN,
        meta: object | NotGiven = NOT_GIVEN,
        recording: live_input_stream_live_inputs_create_a_live_input_params.Recording | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiveInputStreamLiveInputsCreateALiveInputResponse:
        """
        Creates a live input, and returns credentials that you or your users can use to
        stream live video to Cloudflare Stream.

        Args:
          account_id: Identifier

          default_creator: Sets the creator ID asssociated with this live input.

          delete_recording_after_days: Indicates the number of days after which the live inputs recordings will be
              deleted. When a stream completes and the recording is ready, the value is used
              to calculate a scheduled deletion date for that recording. Omit the field to
              indicate no change, or include with a `null` value to remove an existing
              scheduled deletion.

          meta: A user modifiable key-value store used to reference other systems of record for
              managing live inputs.

          recording: Records the input to a Cloudflare Stream video. Behavior depends on the mode. In
              most cases, the video will initially be viewable as a live video and transition
              to on-demand after a condition is satisfied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/stream/live_inputs",
            body=maybe_transform(
                {
                    "default_creator": default_creator,
                    "delete_recording_after_days": delete_recording_after_days,
                    "meta": meta,
                    "recording": recording,
                },
                live_input_stream_live_inputs_create_a_live_input_params.LiveInputStreamLiveInputsCreateALiveInputParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[LiveInputStreamLiveInputsCreateALiveInputResponse],
                ResultWrapper[LiveInputStreamLiveInputsCreateALiveInputResponse],
            ),
        )

    def stream_live_inputs_list_live_inputs(
        self,
        account_id: str,
        *,
        include_counts: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiveInputStreamLiveInputsListLiveInputsResponse:
        """Lists the live inputs created for an account.

        To get the credentials needed to
        stream to a specific live input, request a single live input.

        Args:
          account_id: Identifier

          include_counts: Includes the total number of videos associated with the submitted query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/stream/live_inputs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_counts": include_counts},
                    live_input_stream_live_inputs_list_live_inputs_params.LiveInputStreamLiveInputsListLiveInputsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[LiveInputStreamLiveInputsListLiveInputsResponse],
                ResultWrapper[LiveInputStreamLiveInputsListLiveInputsResponse],
            ),
        )


class AsyncLiveInputs(AsyncAPIResource):
    @cached_property
    def outputs(self) -> AsyncOutputs:
        return AsyncOutputs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLiveInputsWithRawResponse:
        return AsyncLiveInputsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLiveInputsWithStreamingResponse:
        return AsyncLiveInputsWithStreamingResponse(self)

    async def update(
        self,
        live_input_identifier: str,
        *,
        account_id: str,
        default_creator: str | NotGiven = NOT_GIVEN,
        delete_recording_after_days: float | NotGiven = NOT_GIVEN,
        meta: object | NotGiven = NOT_GIVEN,
        recording: live_input_update_params.Recording | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiveInputUpdateResponse:
        """
        Updates a specified live input.

        Args:
          account_id: Identifier

          live_input_identifier: A unique identifier for a live input.

          default_creator: Sets the creator ID asssociated with this live input.

          delete_recording_after_days: Indicates the number of days after which the live inputs recordings will be
              deleted. When a stream completes and the recording is ready, the value is used
              to calculate a scheduled deletion date for that recording. Omit the field to
              indicate no change, or include with a `null` value to remove an existing
              scheduled deletion.

          meta: A user modifiable key-value store used to reference other systems of record for
              managing live inputs.

          recording: Records the input to a Cloudflare Stream video. Behavior depends on the mode. In
              most cases, the video will initially be viewable as a live video and transition
              to on-demand after a condition is satisfied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not live_input_identifier:
            raise ValueError(
                f"Expected a non-empty value for `live_input_identifier` but received {live_input_identifier!r}"
            )
        return await self._put(
            f"/accounts/{account_id}/stream/live_inputs/{live_input_identifier}",
            body=maybe_transform(
                {
                    "default_creator": default_creator,
                    "delete_recording_after_days": delete_recording_after_days,
                    "meta": meta,
                    "recording": recording,
                },
                live_input_update_params.LiveInputUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LiveInputUpdateResponse], ResultWrapper[LiveInputUpdateResponse]),
        )

    async def delete(
        self,
        live_input_identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Prevents a live input from being streamed to and makes the live input
        inaccessible to any future API calls.

        Args:
          account_id: Identifier

          live_input_identifier: A unique identifier for a live input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not live_input_identifier:
            raise ValueError(
                f"Expected a non-empty value for `live_input_identifier` but received {live_input_identifier!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/stream/live_inputs/{live_input_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        live_input_identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiveInputGetResponse:
        """
        Retrieves details of an existing live input.

        Args:
          account_id: Identifier

          live_input_identifier: A unique identifier for a live input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not live_input_identifier:
            raise ValueError(
                f"Expected a non-empty value for `live_input_identifier` but received {live_input_identifier!r}"
            )
        return await self._get(
            f"/accounts/{account_id}/stream/live_inputs/{live_input_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LiveInputGetResponse], ResultWrapper[LiveInputGetResponse]),
        )

    async def stream_live_inputs_create_a_live_input(
        self,
        account_id: str,
        *,
        default_creator: str | NotGiven = NOT_GIVEN,
        delete_recording_after_days: float | NotGiven = NOT_GIVEN,
        meta: object | NotGiven = NOT_GIVEN,
        recording: live_input_stream_live_inputs_create_a_live_input_params.Recording | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiveInputStreamLiveInputsCreateALiveInputResponse:
        """
        Creates a live input, and returns credentials that you or your users can use to
        stream live video to Cloudflare Stream.

        Args:
          account_id: Identifier

          default_creator: Sets the creator ID asssociated with this live input.

          delete_recording_after_days: Indicates the number of days after which the live inputs recordings will be
              deleted. When a stream completes and the recording is ready, the value is used
              to calculate a scheduled deletion date for that recording. Omit the field to
              indicate no change, or include with a `null` value to remove an existing
              scheduled deletion.

          meta: A user modifiable key-value store used to reference other systems of record for
              managing live inputs.

          recording: Records the input to a Cloudflare Stream video. Behavior depends on the mode. In
              most cases, the video will initially be viewable as a live video and transition
              to on-demand after a condition is satisfied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/stream/live_inputs",
            body=maybe_transform(
                {
                    "default_creator": default_creator,
                    "delete_recording_after_days": delete_recording_after_days,
                    "meta": meta,
                    "recording": recording,
                },
                live_input_stream_live_inputs_create_a_live_input_params.LiveInputStreamLiveInputsCreateALiveInputParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[LiveInputStreamLiveInputsCreateALiveInputResponse],
                ResultWrapper[LiveInputStreamLiveInputsCreateALiveInputResponse],
            ),
        )

    async def stream_live_inputs_list_live_inputs(
        self,
        account_id: str,
        *,
        include_counts: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiveInputStreamLiveInputsListLiveInputsResponse:
        """Lists the live inputs created for an account.

        To get the credentials needed to
        stream to a specific live input, request a single live input.

        Args:
          account_id: Identifier

          include_counts: Includes the total number of videos associated with the submitted query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/stream/live_inputs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_counts": include_counts},
                    live_input_stream_live_inputs_list_live_inputs_params.LiveInputStreamLiveInputsListLiveInputsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[LiveInputStreamLiveInputsListLiveInputsResponse],
                ResultWrapper[LiveInputStreamLiveInputsListLiveInputsResponse],
            ),
        )


class LiveInputsWithRawResponse:
    def __init__(self, live_inputs: LiveInputs) -> None:
        self._live_inputs = live_inputs

        self.update = to_raw_response_wrapper(
            live_inputs.update,
        )
        self.delete = to_raw_response_wrapper(
            live_inputs.delete,
        )
        self.get = to_raw_response_wrapper(
            live_inputs.get,
        )
        self.stream_live_inputs_create_a_live_input = to_raw_response_wrapper(
            live_inputs.stream_live_inputs_create_a_live_input,
        )
        self.stream_live_inputs_list_live_inputs = to_raw_response_wrapper(
            live_inputs.stream_live_inputs_list_live_inputs,
        )

    @cached_property
    def outputs(self) -> OutputsWithRawResponse:
        return OutputsWithRawResponse(self._live_inputs.outputs)


class AsyncLiveInputsWithRawResponse:
    def __init__(self, live_inputs: AsyncLiveInputs) -> None:
        self._live_inputs = live_inputs

        self.update = async_to_raw_response_wrapper(
            live_inputs.update,
        )
        self.delete = async_to_raw_response_wrapper(
            live_inputs.delete,
        )
        self.get = async_to_raw_response_wrapper(
            live_inputs.get,
        )
        self.stream_live_inputs_create_a_live_input = async_to_raw_response_wrapper(
            live_inputs.stream_live_inputs_create_a_live_input,
        )
        self.stream_live_inputs_list_live_inputs = async_to_raw_response_wrapper(
            live_inputs.stream_live_inputs_list_live_inputs,
        )

    @cached_property
    def outputs(self) -> AsyncOutputsWithRawResponse:
        return AsyncOutputsWithRawResponse(self._live_inputs.outputs)


class LiveInputsWithStreamingResponse:
    def __init__(self, live_inputs: LiveInputs) -> None:
        self._live_inputs = live_inputs

        self.update = to_streamed_response_wrapper(
            live_inputs.update,
        )
        self.delete = to_streamed_response_wrapper(
            live_inputs.delete,
        )
        self.get = to_streamed_response_wrapper(
            live_inputs.get,
        )
        self.stream_live_inputs_create_a_live_input = to_streamed_response_wrapper(
            live_inputs.stream_live_inputs_create_a_live_input,
        )
        self.stream_live_inputs_list_live_inputs = to_streamed_response_wrapper(
            live_inputs.stream_live_inputs_list_live_inputs,
        )

    @cached_property
    def outputs(self) -> OutputsWithStreamingResponse:
        return OutputsWithStreamingResponse(self._live_inputs.outputs)


class AsyncLiveInputsWithStreamingResponse:
    def __init__(self, live_inputs: AsyncLiveInputs) -> None:
        self._live_inputs = live_inputs

        self.update = async_to_streamed_response_wrapper(
            live_inputs.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            live_inputs.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            live_inputs.get,
        )
        self.stream_live_inputs_create_a_live_input = async_to_streamed_response_wrapper(
            live_inputs.stream_live_inputs_create_a_live_input,
        )
        self.stream_live_inputs_list_live_inputs = async_to_streamed_response_wrapper(
            live_inputs.stream_live_inputs_list_live_inputs,
        )

    @cached_property
    def outputs(self) -> AsyncOutputsWithStreamingResponse:
        return AsyncOutputsWithStreamingResponse(self._live_inputs.outputs)
