# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.zero_trust.dlp.datasets.new_version import NewVersion

from ....._wrappers import ResultWrapper

from typing import Optional, Type

from ....._base_client import make_request_options

from .....types.zero_trust.dlp.dataset import Dataset

from ....._utils import maybe_transform, async_maybe_transform

from ....._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.zero_trust.dlp.datasets import upload_edit_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["UploadResource", "AsyncUploadResource"]

class UploadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadResourceWithRawResponse:
        return UploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadResourceWithStreamingResponse:
        return UploadResourceWithStreamingResponse(self)

    def create(self,
    dataset_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[NewVersion]:
        """
        Prepare to upload a new version of a dataset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not dataset_id:
          raise ValueError(
            f'Expected a non-empty value for `dataset_id` but received {dataset_id!r}'
          )
        return self._post(
            f"/accounts/{account_id}/dlp/datasets/{dataset_id}/upload",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[NewVersion]]._unwrapper),
            cast_to=cast(Type[Optional[NewVersion]], ResultWrapper[NewVersion]),
        )

    def edit(self,
    version: int,
    *,
    account_id: str,
    dataset_id: str,
    body: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Dataset]:
        """This is used for single-column EDMv1 and Custom Word Lists.

        The EDM format can
        only be created in the Cloudflare dashboard. For other clients, this operation
        can only be used for non-secret Custom Word Lists. The body must be a UTF-8
        encoded, newline (NL or CRNL) separated list of words to be matched.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not dataset_id:
          raise ValueError(
            f'Expected a non-empty value for `dataset_id` but received {dataset_id!r}'
          )
        return self._post(
            f"/accounts/{account_id}/dlp/datasets/{dataset_id}/upload/{version}",
            body=maybe_transform(body, upload_edit_params.UploadEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Dataset]]._unwrapper),
            cast_to=cast(Type[Optional[Dataset]], ResultWrapper[Dataset]),
        )

class AsyncUploadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadResourceWithRawResponse:
        return AsyncUploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadResourceWithStreamingResponse:
        return AsyncUploadResourceWithStreamingResponse(self)

    async def create(self,
    dataset_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[NewVersion]:
        """
        Prepare to upload a new version of a dataset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not dataset_id:
          raise ValueError(
            f'Expected a non-empty value for `dataset_id` but received {dataset_id!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/dlp/datasets/{dataset_id}/upload",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[NewVersion]]._unwrapper),
            cast_to=cast(Type[Optional[NewVersion]], ResultWrapper[NewVersion]),
        )

    async def edit(self,
    version: int,
    *,
    account_id: str,
    dataset_id: str,
    body: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Dataset]:
        """This is used for single-column EDMv1 and Custom Word Lists.

        The EDM format can
        only be created in the Cloudflare dashboard. For other clients, this operation
        can only be used for non-secret Custom Word Lists. The body must be a UTF-8
        encoded, newline (NL or CRNL) separated list of words to be matched.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not dataset_id:
          raise ValueError(
            f'Expected a non-empty value for `dataset_id` but received {dataset_id!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/dlp/datasets/{dataset_id}/upload/{version}",
            body=await async_maybe_transform(body, upload_edit_params.UploadEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Dataset]]._unwrapper),
            cast_to=cast(Type[Optional[Dataset]], ResultWrapper[Dataset]),
        )

class UploadResourceWithRawResponse:
    def __init__(self, upload: UploadResource) -> None:
        self._upload = upload

        self.create = to_raw_response_wrapper(
            upload.create,
        )
        self.edit = to_raw_response_wrapper(
            upload.edit,
        )

class AsyncUploadResourceWithRawResponse:
    def __init__(self, upload: AsyncUploadResource) -> None:
        self._upload = upload

        self.create = async_to_raw_response_wrapper(
            upload.create,
        )
        self.edit = async_to_raw_response_wrapper(
            upload.edit,
        )

class UploadResourceWithStreamingResponse:
    def __init__(self, upload: UploadResource) -> None:
        self._upload = upload

        self.create = to_streamed_response_wrapper(
            upload.create,
        )
        self.edit = to_streamed_response_wrapper(
            upload.edit,
        )

class AsyncUploadResourceWithStreamingResponse:
    def __init__(self, upload: AsyncUploadResource) -> None:
        self._upload = upload

        self.create = async_to_streamed_response_wrapper(
            upload.create,
        )
        self.edit = async_to_streamed_response_wrapper(
            upload.edit,
        )