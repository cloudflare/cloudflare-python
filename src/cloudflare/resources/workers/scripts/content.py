# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Mapping, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ...._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
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
from ...._base_client import (
    make_request_options,
)
from ....types.workers import WorkersScript
from ....types.workers.scripts import content_update_params

__all__ = ["Content", "AsyncContent"]


class Content(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentWithRawResponse:
        return ContentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentWithStreamingResponse:
        return ContentWithStreamingResponse(self)

    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: content_update_params.Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkersScript:
        """
        Put script content without touching config or metadata

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be
              present. This should be referenced either in the metadata as `main_module`
              (esm)/`body_part` (service worker) or as a header `CF-WORKER-MAIN-MODULE-PART`
              (esm) /`CF-WORKER-BODY-PART` (service worker) by part name.

          metadata: JSON encoded metadata about the uploaded parts and Worker configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        body = deepcopy_minimal(
            {
                "any_part_name": any_part_name,
                "metadata": metadata,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["<any part name>", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            f"/accounts/{account_id}/workers/scripts/{script_name}/content",
            body=maybe_transform(body, content_update_params.ContentUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WorkersScript], ResultWrapper[WorkersScript]),
        )


class AsyncContent(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentWithRawResponse:
        return AsyncContentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentWithStreamingResponse:
        return AsyncContentWithStreamingResponse(self)

    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: content_update_params.Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkersScript:
        """
        Put script content without touching config or metadata

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be
              present. This should be referenced either in the metadata as `main_module`
              (esm)/`body_part` (service worker) or as a header `CF-WORKER-MAIN-MODULE-PART`
              (esm) /`CF-WORKER-BODY-PART` (service worker) by part name.

          metadata: JSON encoded metadata about the uploaded parts and Worker configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        body = deepcopy_minimal(
            {
                "any_part_name": any_part_name,
                "metadata": metadata,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["<any part name>", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            f"/accounts/{account_id}/workers/scripts/{script_name}/content",
            body=await async_maybe_transform(body, content_update_params.ContentUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WorkersScript], ResultWrapper[WorkersScript]),
        )


class ContentWithRawResponse:
    def __init__(self, content: Content) -> None:
        self._content = content

        self.update = to_raw_response_wrapper(
            content.update,
        )


class AsyncContentWithRawResponse:
    def __init__(self, content: AsyncContent) -> None:
        self._content = content

        self.update = async_to_raw_response_wrapper(
            content.update,
        )


class ContentWithStreamingResponse:
    def __init__(self, content: Content) -> None:
        self._content = content

        self.update = to_streamed_response_wrapper(
            content.update,
        )


class AsyncContentWithStreamingResponse:
    def __init__(self, content: AsyncContent) -> None:
        self._content = content

        self.update = async_to_streamed_response_wrapper(
            content.update,
        )
