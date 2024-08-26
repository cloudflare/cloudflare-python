# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.workers.script import Script

from ...._wrappers import ResultWrapper

from ...._utils import is_given, strip_not_given, maybe_transform, async_maybe_transform

from typing import Optional, Type, List

from ...._base_client import make_request_options

from ...._types import FileTypes

from ....types.workers.worker_metadata_param import WorkerMetadataParam

from ...._response import BinaryAPIResponse, AsyncBinaryAPIResponse, to_raw_response_wrapper, to_custom_raw_response_wrapper, async_to_raw_response_wrapper, async_to_custom_raw_response_wrapper, to_streamed_response_wrapper, to_custom_streamed_response_wrapper, StreamedBinaryAPIResponse, async_to_streamed_response_wrapper, async_to_custom_streamed_response_wrapper, AsyncStreamedBinaryAPIResponse

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.workers.scripts import content_update_params
from ....types.workers import WorkerMetadata
from typing import cast
from typing import cast

__all__ = ["ContentResource", "AsyncContentResource"]

class ContentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentResourceWithRawResponse:
        return ContentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentResourceWithStreamingResponse:
        return ContentResourceWithStreamingResponse(self)

    def update(self,
    script_name: str,
    *,
    account_id: str,
    any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
    metadata: WorkerMetadataParam | NotGiven = NOT_GIVEN,
    cf_worker_body_part: str | NotGiven = NOT_GIVEN,
    cf_worker_main_module_part: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Script]:
        """
        Put script content without touching config or metadata

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be
              present. This should be referenced either in the metadata as `main_module`
              (esm)/`body_part` (service worker) or as a header `CF-WORKER-MAIN-MODULE-PART`
              (esm) /`CF-WORKER-BODY-PART` (service worker) by part name. Source maps may also
              be included using the `application/source-map` content type.

          metadata: JSON encoded metadata about the uploaded parts and Worker configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not script_name:
          raise ValueError(
            f'Expected a non-empty value for `script_name` but received {script_name!r}'
          )
        extra_headers = { **strip_not_given({
            "CF-WORKER-BODY-PART": cf_worker_body_part,
            "CF-WORKER-MAIN-MODULE-PART": cf_worker_main_module_part,
        }), **(extra_headers or {}) }
        body = deepcopy_minimal({
            "any_part_name": any_part_name,
            "metadata": metadata,
        })
        files = extract_files(
          cast(Mapping[str, object], body),
          paths=[["<any part name>", "<array>"]]
        )
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            f"/accounts/{account_id}/workers/scripts/{script_name}/content",
            body=maybe_transform(body, content_update_params.ContentUpdateParams),
            files=files,
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Script]]._unwrapper),
            cast_to=cast(Type[Optional[Script]], ResultWrapper[Script]),
        )

    def get(self,
    script_name: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> BinaryAPIResponse:
        """
        Fetch script content only

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not script_name:
          raise ValueError(
            f'Expected a non-empty value for `script_name` but received {script_name!r}'
          )
        extra_headers = {"Accept": "string", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/content/v2",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BinaryAPIResponse,
        )

class AsyncContentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentResourceWithRawResponse:
        return AsyncContentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentResourceWithStreamingResponse:
        return AsyncContentResourceWithStreamingResponse(self)

    async def update(self,
    script_name: str,
    *,
    account_id: str,
    any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
    metadata: WorkerMetadataParam | NotGiven = NOT_GIVEN,
    cf_worker_body_part: str | NotGiven = NOT_GIVEN,
    cf_worker_main_module_part: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Script]:
        """
        Put script content without touching config or metadata

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be
              present. This should be referenced either in the metadata as `main_module`
              (esm)/`body_part` (service worker) or as a header `CF-WORKER-MAIN-MODULE-PART`
              (esm) /`CF-WORKER-BODY-PART` (service worker) by part name. Source maps may also
              be included using the `application/source-map` content type.

          metadata: JSON encoded metadata about the uploaded parts and Worker configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not script_name:
          raise ValueError(
            f'Expected a non-empty value for `script_name` but received {script_name!r}'
          )
        extra_headers = { **strip_not_given({
            "CF-WORKER-BODY-PART": cf_worker_body_part,
            "CF-WORKER-MAIN-MODULE-PART": cf_worker_main_module_part,
        }), **(extra_headers or {}) }
        body = deepcopy_minimal({
            "any_part_name": any_part_name,
            "metadata": metadata,
        })
        files = extract_files(
          cast(Mapping[str, object], body),
          paths=[["<any part name>", "<array>"]]
        )
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            f"/accounts/{account_id}/workers/scripts/{script_name}/content",
            body=await async_maybe_transform(body, content_update_params.ContentUpdateParams),
            files=files,
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Script]]._unwrapper),
            cast_to=cast(Type[Optional[Script]], ResultWrapper[Script]),
        )

    async def get(self,
    script_name: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncBinaryAPIResponse:
        """
        Fetch script content only

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not script_name:
          raise ValueError(
            f'Expected a non-empty value for `script_name` but received {script_name!r}'
          )
        extra_headers = {"Accept": "string", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/content/v2",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AsyncBinaryAPIResponse,
        )

class ContentResourceWithRawResponse:
    def __init__(self, content: ContentResource) -> None:
        self._content = content

        self.update = to_raw_response_wrapper(
            content.update,
        )
        self.get = to_custom_raw_response_wrapper(
            content.get,
            BinaryAPIResponse,
        )

class AsyncContentResourceWithRawResponse:
    def __init__(self, content: AsyncContentResource) -> None:
        self._content = content

        self.update = async_to_raw_response_wrapper(
            content.update,
        )
        self.get = async_to_custom_raw_response_wrapper(
            content.get,
            AsyncBinaryAPIResponse,
        )

class ContentResourceWithStreamingResponse:
    def __init__(self, content: ContentResource) -> None:
        self._content = content

        self.update = to_streamed_response_wrapper(
            content.update,
        )
        self.get = to_custom_streamed_response_wrapper(
            content.get,
            StreamedBinaryAPIResponse,
        )

class AsyncContentResourceWithStreamingResponse:
    def __init__(self, content: AsyncContentResource) -> None:
        self._content = content

        self.update = async_to_streamed_response_wrapper(
            content.update,
        )
        self.get = async_to_custom_streamed_response_wrapper(
            content.get,
            AsyncStreamedBinaryAPIResponse,
        )