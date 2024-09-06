# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.intel.indicator_feeds.snapshot_update_response import SnapshotUpdateResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ...._base_client import make_request_options

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
from ....types import shared_params
from ....types.intel.indicator_feeds import snapshot_update_params
from typing import cast
from typing import cast

__all__ = ["SnapshotsResource", "AsyncSnapshotsResource"]


class SnapshotsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SnapshotsResourceWithRawResponse:
        return SnapshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SnapshotsResourceWithStreamingResponse:
        return SnapshotsResourceWithStreamingResponse(self)

    def update(
        self,
        feed_id: int,
        *,
        account_id: str,
        source: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SnapshotUpdateResponse]:
        """
        Update indicator feed data

        Args:
          account_id: Identifier

          feed_id: Indicator feed ID

          source: The file to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            f"/accounts/{account_id}/intel/indicator-feeds/{feed_id}/snapshot",
            body=maybe_transform({"source": source}, snapshot_update_params.SnapshotUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SnapshotUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SnapshotUpdateResponse]], ResultWrapper[SnapshotUpdateResponse]),
        )


class AsyncSnapshotsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSnapshotsResourceWithRawResponse:
        return AsyncSnapshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSnapshotsResourceWithStreamingResponse:
        return AsyncSnapshotsResourceWithStreamingResponse(self)

    async def update(
        self,
        feed_id: int,
        *,
        account_id: str,
        source: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SnapshotUpdateResponse]:
        """
        Update indicator feed data

        Args:
          account_id: Identifier

          feed_id: Indicator feed ID

          source: The file to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            f"/accounts/{account_id}/intel/indicator-feeds/{feed_id}/snapshot",
            body=await async_maybe_transform({"source": source}, snapshot_update_params.SnapshotUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SnapshotUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SnapshotUpdateResponse]], ResultWrapper[SnapshotUpdateResponse]),
        )


class SnapshotsResourceWithRawResponse:
    def __init__(self, snapshots: SnapshotsResource) -> None:
        self._snapshots = snapshots

        self.update = to_raw_response_wrapper(
            snapshots.update,
        )


class AsyncSnapshotsResourceWithRawResponse:
    def __init__(self, snapshots: AsyncSnapshotsResource) -> None:
        self._snapshots = snapshots

        self.update = async_to_raw_response_wrapper(
            snapshots.update,
        )


class SnapshotsResourceWithStreamingResponse:
    def __init__(self, snapshots: SnapshotsResource) -> None:
        self._snapshots = snapshots

        self.update = to_streamed_response_wrapper(
            snapshots.update,
        )


class AsyncSnapshotsResourceWithStreamingResponse:
    def __init__(self, snapshots: AsyncSnapshotsResource) -> None:
        self._snapshots = snapshots

        self.update = async_to_streamed_response_wrapper(
            snapshots.update,
        )
