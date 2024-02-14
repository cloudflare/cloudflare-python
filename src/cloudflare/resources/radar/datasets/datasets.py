# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .downloads import Downloads, AsyncDownloads

from ...._compat import cached_property

from ....types.radar import DatasetListResponse, DatasetGetResponse

from typing import Type, Optional

from typing_extensions import Literal

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
from ....types.radar import dataset_list_params
from ....types.radar import dataset_get_params
from .downloads import (
    Downloads,
    AsyncDownloads,
    DownloadsWithRawResponse,
    AsyncDownloadsWithRawResponse,
    DownloadsWithStreamingResponse,
    AsyncDownloadsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Datasets", "AsyncDatasets"]


class Datasets(SyncAPIResource):
    @cached_property
    def downloads(self) -> Downloads:
        return Downloads(self._client)

    @cached_property
    def with_raw_response(self) -> DatasetsWithRawResponse:
        return DatasetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsWithStreamingResponse:
        return DatasetsWithStreamingResponse(self)

    def list(
        self,
        *,
        dataset_type: Literal["RANKING_BUCKET", "REPORT"] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListResponse:
        """
        Get a list of datasets.

        Args:
          dataset_type: Dataset type.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          offset: Number of objects to skip before grabbing results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset_type": dataset_type,
                        "format": format,
                        "limit": limit,
                        "offset": offset,
                    },
                    dataset_list_params.DatasetListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DatasetListResponse], ResultWrapper[DatasetListResponse]),
        )

    def get(
        self,
        alias: str,
        *,
        date: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Get the csv content of a given dataset by alias or id.

        When getting the content
        by alias the latest dataset is returned, optionally filtered by the latest
        available at a given date.

        Args:
          alias: Dataset alias or id

          date: Filter dataset alias by date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alias:
            raise ValueError(f"Expected a non-empty value for `alias` but received {alias!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return self._get(
            f"/radar/datasets/{alias}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, dataset_get_params.DatasetGetParams),
            ),
            cast_to=str,
        )


class AsyncDatasets(AsyncAPIResource):
    @cached_property
    def downloads(self) -> AsyncDownloads:
        return AsyncDownloads(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasetsWithRawResponse:
        return AsyncDatasetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsWithStreamingResponse:
        return AsyncDatasetsWithStreamingResponse(self)

    async def list(
        self,
        *,
        dataset_type: Literal["RANKING_BUCKET", "REPORT"] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListResponse:
        """
        Get a list of datasets.

        Args:
          dataset_type: Dataset type.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          offset: Number of objects to skip before grabbing results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset_type": dataset_type,
                        "format": format,
                        "limit": limit,
                        "offset": offset,
                    },
                    dataset_list_params.DatasetListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DatasetListResponse], ResultWrapper[DatasetListResponse]),
        )

    async def get(
        self,
        alias: str,
        *,
        date: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Get the csv content of a given dataset by alias or id.

        When getting the content
        by alias the latest dataset is returned, optionally filtered by the latest
        available at a given date.

        Args:
          alias: Dataset alias or id

          date: Filter dataset alias by date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alias:
            raise ValueError(f"Expected a non-empty value for `alias` but received {alias!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return await self._get(
            f"/radar/datasets/{alias}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, dataset_get_params.DatasetGetParams),
            ),
            cast_to=str,
        )


class DatasetsWithRawResponse:
    def __init__(self, datasets: Datasets) -> None:
        self._datasets = datasets

        self.list = to_raw_response_wrapper(
            datasets.list,
        )
        self.get = to_raw_response_wrapper(
            datasets.get,
        )

    @cached_property
    def downloads(self) -> DownloadsWithRawResponse:
        return DownloadsWithRawResponse(self._datasets.downloads)


class AsyncDatasetsWithRawResponse:
    def __init__(self, datasets: AsyncDatasets) -> None:
        self._datasets = datasets

        self.list = async_to_raw_response_wrapper(
            datasets.list,
        )
        self.get = async_to_raw_response_wrapper(
            datasets.get,
        )

    @cached_property
    def downloads(self) -> AsyncDownloadsWithRawResponse:
        return AsyncDownloadsWithRawResponse(self._datasets.downloads)


class DatasetsWithStreamingResponse:
    def __init__(self, datasets: Datasets) -> None:
        self._datasets = datasets

        self.list = to_streamed_response_wrapper(
            datasets.list,
        )
        self.get = to_streamed_response_wrapper(
            datasets.get,
        )

    @cached_property
    def downloads(self) -> DownloadsWithStreamingResponse:
        return DownloadsWithStreamingResponse(self._datasets.downloads)


class AsyncDatasetsWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasets) -> None:
        self._datasets = datasets

        self.list = async_to_streamed_response_wrapper(
            datasets.list,
        )
        self.get = async_to_streamed_response_wrapper(
            datasets.get,
        )

    @cached_property
    def downloads(self) -> AsyncDownloadsWithStreamingResponse:
        return AsyncDownloadsWithStreamingResponse(self._datasets.downloads)
