# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.zero_trust.dlp import DLPDataset
from .....types.zero_trust.dlp.datasets import DLPDatasetNewVersion

__all__ = ["Upload", "AsyncUpload"]


class Upload(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadWithRawResponse:
        return UploadWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadWithStreamingResponse:
        return UploadWithStreamingResponse(self)

    def create(
        self,
        dataset_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DLPDatasetNewVersion]:
        """
        Prepare to upload a new version of a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._post(
            f"/accounts/{account_id}/dlp/datasets/{dataset_id}/upload",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DLPDatasetNewVersion]], ResultWrapper[DLPDatasetNewVersion]),
        )

    def edit(
        self,
        version: int,
        *,
        account_id: str,
        dataset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DLPDataset]:
        """
        Upload a new version of a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._post(
            f"/accounts/{account_id}/dlp/datasets/{dataset_id}/upload/{version}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DLPDataset]], ResultWrapper[DLPDataset]),
        )


class AsyncUpload(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadWithRawResponse:
        return AsyncUploadWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadWithStreamingResponse:
        return AsyncUploadWithStreamingResponse(self)

    async def create(
        self,
        dataset_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DLPDatasetNewVersion]:
        """
        Prepare to upload a new version of a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._post(
            f"/accounts/{account_id}/dlp/datasets/{dataset_id}/upload",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DLPDatasetNewVersion]], ResultWrapper[DLPDatasetNewVersion]),
        )

    async def edit(
        self,
        version: int,
        *,
        account_id: str,
        dataset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DLPDataset]:
        """
        Upload a new version of a dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._post(
            f"/accounts/{account_id}/dlp/datasets/{dataset_id}/upload/{version}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DLPDataset]], ResultWrapper[DLPDataset]),
        )


class UploadWithRawResponse:
    def __init__(self, upload: Upload) -> None:
        self._upload = upload

        self.create = to_raw_response_wrapper(
            upload.create,
        )
        self.edit = to_raw_response_wrapper(
            upload.edit,
        )


class AsyncUploadWithRawResponse:
    def __init__(self, upload: AsyncUpload) -> None:
        self._upload = upload

        self.create = async_to_raw_response_wrapper(
            upload.create,
        )
        self.edit = async_to_raw_response_wrapper(
            upload.edit,
        )


class UploadWithStreamingResponse:
    def __init__(self, upload: Upload) -> None:
        self._upload = upload

        self.create = to_streamed_response_wrapper(
            upload.create,
        )
        self.edit = to_streamed_response_wrapper(
            upload.edit,
        )


class AsyncUploadWithStreamingResponse:
    def __init__(self, upload: AsyncUpload) -> None:
        self._upload = upload

        self.create = async_to_streamed_response_wrapper(
            upload.create,
        )
        self.edit = async_to_streamed_response_wrapper(
            upload.edit,
        )
