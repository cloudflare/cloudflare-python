# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .entries import EntriesResource, AsyncEntriesResource

from ......_compat import cached_property

from ......types.zero_trust.dlp.datasets.version_create_response import VersionCreateResponse

from ......_wrappers import ResultWrapper

from typing import Iterable, Optional, Type

from ......_utils import maybe_transform, async_maybe_transform

from ......_base_client import make_request_options

from ......_response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ......types.zero_trust.dlp.datasets import version_create_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ......_utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ......_types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......types import shared_params
from ......types.zero_trust.dlp.datasets import version_create_params
from .entries import (
    EntriesResource,
    AsyncEntriesResource,
    EntriesResourceWithRawResponse,
    AsyncEntriesResourceWithRawResponse,
    EntriesResourceWithStreamingResponse,
    AsyncEntriesResourceWithStreamingResponse,
)
from typing import cast
from typing import cast

__all__ = ["VersionsResource", "AsyncVersionsResource"]


class VersionsResource(SyncAPIResource):
    @cached_property
    def entries(self) -> EntriesResource:
        return EntriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self)

    def create(
        self,
        version: int,
        *,
        account_id: str,
        dataset_id: str,
        body: Iterable[version_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VersionCreateResponse]:
        """This is used for multi-column EDMv2 datasets.

        The EDMv2 format can only be
        created in the Cloudflare dashboard. The columns in the response appear in the
        same order as in the request.

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
            f"/accounts/{account_id}/dlp/datasets/{dataset_id}/versions/{version}",
            body=maybe_transform(body, Iterable[version_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[VersionCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[VersionCreateResponse]], ResultWrapper[VersionCreateResponse]),
        )


class AsyncVersionsResource(AsyncAPIResource):
    @cached_property
    def entries(self) -> AsyncEntriesResource:
        return AsyncEntriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self)

    async def create(
        self,
        version: int,
        *,
        account_id: str,
        dataset_id: str,
        body: Iterable[version_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VersionCreateResponse]:
        """This is used for multi-column EDMv2 datasets.

        The EDMv2 format can only be
        created in the Cloudflare dashboard. The columns in the response appear in the
        same order as in the request.

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
            f"/accounts/{account_id}/dlp/datasets/{dataset_id}/versions/{version}",
            body=await async_maybe_transform(body, Iterable[version_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[VersionCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[VersionCreateResponse]], ResultWrapper[VersionCreateResponse]),
        )


class VersionsResourceWithRawResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.create = to_raw_response_wrapper(
            versions.create,
        )

    @cached_property
    def entries(self) -> EntriesResourceWithRawResponse:
        return EntriesResourceWithRawResponse(self._versions.entries)


class AsyncVersionsResourceWithRawResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.create = async_to_raw_response_wrapper(
            versions.create,
        )

    @cached_property
    def entries(self) -> AsyncEntriesResourceWithRawResponse:
        return AsyncEntriesResourceWithRawResponse(self._versions.entries)


class VersionsResourceWithStreamingResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.create = to_streamed_response_wrapper(
            versions.create,
        )

    @cached_property
    def entries(self) -> EntriesResourceWithStreamingResponse:
        return EntriesResourceWithStreamingResponse(self._versions.entries)


class AsyncVersionsResourceWithStreamingResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.create = async_to_streamed_response_wrapper(
            versions.create,
        )

    @cached_property
    def entries(self) -> AsyncEntriesResourceWithStreamingResponse:
        return AsyncEntriesResourceWithStreamingResponse(self._versions.entries)
