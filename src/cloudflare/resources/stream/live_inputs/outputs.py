# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.stream.live_inputs import (
    OutputUpdateResponse,
    OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse,
    OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse,
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
from ....types.stream.live_inputs import output_update_params
from ....types.stream.live_inputs import output_stream_live_inputs_create_a_new_output_connected_to_a_live_input_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Outputs", "AsyncOutputs"]


class Outputs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OutputsWithRawResponse:
        return OutputsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutputsWithStreamingResponse:
        return OutputsWithStreamingResponse(self)

    def update(
        self,
        output_identifier: str,
        *,
        account_id: str,
        live_input_identifier: str,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutputUpdateResponse:
        """
        Updates the state of an output.

        Args:
          account_id: Identifier

          live_input_identifier: A unique identifier for a live input.

          output_identifier: A unique identifier for the output.

          enabled: When enabled, live video streamed to the associated live input will be sent to
              the output URL. When disabled, live video will not be sent to the output URL,
              even when streaming to the associated live input. Use this to control precisely
              when you start and stop simulcasting to specific destinations like YouTube and
              Twitch.

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
        if not output_identifier:
            raise ValueError(f"Expected a non-empty value for `output_identifier` but received {output_identifier!r}")
        return self._put(
            f"/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}",
            body=maybe_transform({"enabled": enabled}, output_update_params.OutputUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OutputUpdateResponse], ResultWrapper[OutputUpdateResponse]),
        )

    def delete(
        self,
        output_identifier: str,
        *,
        account_id: str,
        live_input_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes an output and removes it from the associated live input.

        Args:
          account_id: Identifier

          live_input_identifier: A unique identifier for a live input.

          output_identifier: A unique identifier for the output.

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
        if not output_identifier:
            raise ValueError(f"Expected a non-empty value for `output_identifier` but received {output_identifier!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def stream_live_inputs_create_a_new_output_connected_to_a_live_input(
        self,
        live_input_identifier: str,
        *,
        account_id: str,
        stream_key: str,
        url: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse:
        """
        Creates a new output that can be used to simulcast or restream live video to
        other RTMP or SRT destinations. Outputs are always linked to a specific live
        input — one live input can have many outputs.

        Args:
          account_id: Identifier

          live_input_identifier: A unique identifier for a live input.

          stream_key: The streamKey used to authenticate against an output's target.

          url: The URL an output uses to restream.

          enabled: When enabled, live video streamed to the associated live input will be sent to
              the output URL. When disabled, live video will not be sent to the output URL,
              even when streaming to the associated live input. Use this to control precisely
              when you start and stop simulcasting to specific destinations like YouTube and
              Twitch.

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
        return self._post(
            f"/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs",
            body=maybe_transform(
                {
                    "stream_key": stream_key,
                    "url": url,
                    "enabled": enabled,
                },
                output_stream_live_inputs_create_a_new_output_connected_to_a_live_input_params.OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse],
                ResultWrapper[OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse],
            ),
        )

    def stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
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
    ) -> OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse:
        """
        Retrieves all outputs associated with a specified live input.

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
            f"/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse],
                ResultWrapper[OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse],
            ),
        )


class AsyncOutputs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOutputsWithRawResponse:
        return AsyncOutputsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutputsWithStreamingResponse:
        return AsyncOutputsWithStreamingResponse(self)

    async def update(
        self,
        output_identifier: str,
        *,
        account_id: str,
        live_input_identifier: str,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutputUpdateResponse:
        """
        Updates the state of an output.

        Args:
          account_id: Identifier

          live_input_identifier: A unique identifier for a live input.

          output_identifier: A unique identifier for the output.

          enabled: When enabled, live video streamed to the associated live input will be sent to
              the output URL. When disabled, live video will not be sent to the output URL,
              even when streaming to the associated live input. Use this to control precisely
              when you start and stop simulcasting to specific destinations like YouTube and
              Twitch.

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
        if not output_identifier:
            raise ValueError(f"Expected a non-empty value for `output_identifier` but received {output_identifier!r}")
        return await self._put(
            f"/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}",
            body=maybe_transform({"enabled": enabled}, output_update_params.OutputUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OutputUpdateResponse], ResultWrapper[OutputUpdateResponse]),
        )

    async def delete(
        self,
        output_identifier: str,
        *,
        account_id: str,
        live_input_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes an output and removes it from the associated live input.

        Args:
          account_id: Identifier

          live_input_identifier: A unique identifier for a live input.

          output_identifier: A unique identifier for the output.

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
        if not output_identifier:
            raise ValueError(f"Expected a non-empty value for `output_identifier` but received {output_identifier!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def stream_live_inputs_create_a_new_output_connected_to_a_live_input(
        self,
        live_input_identifier: str,
        *,
        account_id: str,
        stream_key: str,
        url: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse:
        """
        Creates a new output that can be used to simulcast or restream live video to
        other RTMP or SRT destinations. Outputs are always linked to a specific live
        input — one live input can have many outputs.

        Args:
          account_id: Identifier

          live_input_identifier: A unique identifier for a live input.

          stream_key: The streamKey used to authenticate against an output's target.

          url: The URL an output uses to restream.

          enabled: When enabled, live video streamed to the associated live input will be sent to
              the output URL. When disabled, live video will not be sent to the output URL,
              even when streaming to the associated live input. Use this to control precisely
              when you start and stop simulcasting to specific destinations like YouTube and
              Twitch.

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
        return await self._post(
            f"/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs",
            body=maybe_transform(
                {
                    "stream_key": stream_key,
                    "url": url,
                    "enabled": enabled,
                },
                output_stream_live_inputs_create_a_new_output_connected_to_a_live_input_params.OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse],
                ResultWrapper[OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse],
            ),
        )

    async def stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
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
    ) -> OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse:
        """
        Retrieves all outputs associated with a specified live input.

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
            f"/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse],
                ResultWrapper[OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse],
            ),
        )


class OutputsWithRawResponse:
    def __init__(self, outputs: Outputs) -> None:
        self._outputs = outputs

        self.update = to_raw_response_wrapper(
            outputs.update,
        )
        self.delete = to_raw_response_wrapper(
            outputs.delete,
        )
        self.stream_live_inputs_create_a_new_output_connected_to_a_live_input = to_raw_response_wrapper(
            outputs.stream_live_inputs_create_a_new_output_connected_to_a_live_input,
        )
        self.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input = to_raw_response_wrapper(
            outputs.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input,
        )


class AsyncOutputsWithRawResponse:
    def __init__(self, outputs: AsyncOutputs) -> None:
        self._outputs = outputs

        self.update = async_to_raw_response_wrapper(
            outputs.update,
        )
        self.delete = async_to_raw_response_wrapper(
            outputs.delete,
        )
        self.stream_live_inputs_create_a_new_output_connected_to_a_live_input = async_to_raw_response_wrapper(
            outputs.stream_live_inputs_create_a_new_output_connected_to_a_live_input,
        )
        self.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input = async_to_raw_response_wrapper(
            outputs.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input,
        )


class OutputsWithStreamingResponse:
    def __init__(self, outputs: Outputs) -> None:
        self._outputs = outputs

        self.update = to_streamed_response_wrapper(
            outputs.update,
        )
        self.delete = to_streamed_response_wrapper(
            outputs.delete,
        )
        self.stream_live_inputs_create_a_new_output_connected_to_a_live_input = to_streamed_response_wrapper(
            outputs.stream_live_inputs_create_a_new_output_connected_to_a_live_input,
        )
        self.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input = to_streamed_response_wrapper(
            outputs.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input,
        )


class AsyncOutputsWithStreamingResponse:
    def __init__(self, outputs: AsyncOutputs) -> None:
        self._outputs = outputs

        self.update = async_to_streamed_response_wrapper(
            outputs.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            outputs.delete,
        )
        self.stream_live_inputs_create_a_new_output_connected_to_a_live_input = async_to_streamed_response_wrapper(
            outputs.stream_live_inputs_create_a_new_output_connected_to_a_live_input,
        )
        self.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input = (
            async_to_streamed_response_wrapper(
                outputs.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input,
            )
        )
