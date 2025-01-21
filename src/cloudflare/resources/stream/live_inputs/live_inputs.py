# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .outputs import (
    OutputsResource,
    AsyncOutputsResource,
    OutputsResourceWithRawResponse,
    AsyncOutputsResourceWithRawResponse,
    OutputsResourceWithStreamingResponse,
    AsyncOutputsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ....types.stream import live_input_list_params, live_input_create_params, live_input_update_params
from ....types.stream.live_input import LiveInput
from ....types.stream.live_input_list_response import LiveInputListResponse

__all__ = ["LiveInputsResource", "AsyncLiveInputsResource"]


class LiveInputsResource(SyncAPIResource):
    @cached_property
    def outputs(self) -> OutputsResource:
        return OutputsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LiveInputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LiveInputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LiveInputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LiveInputsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        default_creator: str | NotGiven = NOT_GIVEN,
        delete_recording_after_days: float | NotGiven = NOT_GIVEN,
        meta: object | NotGiven = NOT_GIVEN,
        recording: live_input_create_params.Recording | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LiveInput]:
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
                live_input_create_params.LiveInputCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LiveInput]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LiveInput]], ResultWrapper[LiveInput]),
        )

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
    ) -> Optional[LiveInput]:
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
                post_parser=ResultWrapper[Optional[LiveInput]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LiveInput]], ResultWrapper[LiveInput]),
        )

    def list(
        self,
        *,
        account_id: str,
        include_counts: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LiveInputListResponse]:
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
                query=maybe_transform({"include_counts": include_counts}, live_input_list_params.LiveInputListParams),
                post_parser=ResultWrapper[Optional[LiveInputListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LiveInputListResponse]], ResultWrapper[LiveInputListResponse]),
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
    ) -> Optional[LiveInput]:
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
                post_parser=ResultWrapper[Optional[LiveInput]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LiveInput]], ResultWrapper[LiveInput]),
        )


class AsyncLiveInputsResource(AsyncAPIResource):
    @cached_property
    def outputs(self) -> AsyncOutputsResource:
        return AsyncOutputsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLiveInputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLiveInputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLiveInputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLiveInputsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        default_creator: str | NotGiven = NOT_GIVEN,
        delete_recording_after_days: float | NotGiven = NOT_GIVEN,
        meta: object | NotGiven = NOT_GIVEN,
        recording: live_input_create_params.Recording | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LiveInput]:
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
            body=await async_maybe_transform(
                {
                    "default_creator": default_creator,
                    "delete_recording_after_days": delete_recording_after_days,
                    "meta": meta,
                    "recording": recording,
                },
                live_input_create_params.LiveInputCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LiveInput]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LiveInput]], ResultWrapper[LiveInput]),
        )

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
    ) -> Optional[LiveInput]:
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
            body=await async_maybe_transform(
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
                post_parser=ResultWrapper[Optional[LiveInput]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LiveInput]], ResultWrapper[LiveInput]),
        )

    async def list(
        self,
        *,
        account_id: str,
        include_counts: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LiveInputListResponse]:
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
                query=await async_maybe_transform(
                    {"include_counts": include_counts}, live_input_list_params.LiveInputListParams
                ),
                post_parser=ResultWrapper[Optional[LiveInputListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LiveInputListResponse]], ResultWrapper[LiveInputListResponse]),
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
    ) -> Optional[LiveInput]:
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
                post_parser=ResultWrapper[Optional[LiveInput]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LiveInput]], ResultWrapper[LiveInput]),
        )


class LiveInputsResourceWithRawResponse:
    def __init__(self, live_inputs: LiveInputsResource) -> None:
        self._live_inputs = live_inputs

        self.create = to_raw_response_wrapper(
            live_inputs.create,
        )
        self.update = to_raw_response_wrapper(
            live_inputs.update,
        )
        self.list = to_raw_response_wrapper(
            live_inputs.list,
        )
        self.delete = to_raw_response_wrapper(
            live_inputs.delete,
        )
        self.get = to_raw_response_wrapper(
            live_inputs.get,
        )

    @cached_property
    def outputs(self) -> OutputsResourceWithRawResponse:
        return OutputsResourceWithRawResponse(self._live_inputs.outputs)


class AsyncLiveInputsResourceWithRawResponse:
    def __init__(self, live_inputs: AsyncLiveInputsResource) -> None:
        self._live_inputs = live_inputs

        self.create = async_to_raw_response_wrapper(
            live_inputs.create,
        )
        self.update = async_to_raw_response_wrapper(
            live_inputs.update,
        )
        self.list = async_to_raw_response_wrapper(
            live_inputs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            live_inputs.delete,
        )
        self.get = async_to_raw_response_wrapper(
            live_inputs.get,
        )

    @cached_property
    def outputs(self) -> AsyncOutputsResourceWithRawResponse:
        return AsyncOutputsResourceWithRawResponse(self._live_inputs.outputs)


class LiveInputsResourceWithStreamingResponse:
    def __init__(self, live_inputs: LiveInputsResource) -> None:
        self._live_inputs = live_inputs

        self.create = to_streamed_response_wrapper(
            live_inputs.create,
        )
        self.update = to_streamed_response_wrapper(
            live_inputs.update,
        )
        self.list = to_streamed_response_wrapper(
            live_inputs.list,
        )
        self.delete = to_streamed_response_wrapper(
            live_inputs.delete,
        )
        self.get = to_streamed_response_wrapper(
            live_inputs.get,
        )

    @cached_property
    def outputs(self) -> OutputsResourceWithStreamingResponse:
        return OutputsResourceWithStreamingResponse(self._live_inputs.outputs)


class AsyncLiveInputsResourceWithStreamingResponse:
    def __init__(self, live_inputs: AsyncLiveInputsResource) -> None:
        self._live_inputs = live_inputs

        self.create = async_to_streamed_response_wrapper(
            live_inputs.create,
        )
        self.update = async_to_streamed_response_wrapper(
            live_inputs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            live_inputs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            live_inputs.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            live_inputs.get,
        )

    @cached_property
    def outputs(self) -> AsyncOutputsResourceWithStreamingResponse:
        return AsyncOutputsResourceWithStreamingResponse(self._live_inputs.outputs)
