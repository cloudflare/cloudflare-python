# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.radar import dataset_get_params, dataset_list_params, dataset_download_params
from ..._base_client import (
    make_request_options,
)
from ...types.radar.dataset_list_response import DatasetListResponse
from ...types.radar.dataset_download_response import DatasetDownloadResponse

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self)

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
                post_parser=ResultWrapper[DatasetListResponse]._unwrapper,
            ),
            cast_to=cast(Type[DatasetListResponse], ResultWrapper[DatasetListResponse]),
        )

    def download(
        self,
        *,
        dataset_id: int,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetDownloadResponse:
        """
        Get a url to download a single dataset.

        Args:
          format: Format results are returned in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/radar/datasets/download",
            body=maybe_transform({"dataset_id": dataset_id}, dataset_download_params.DatasetDownloadParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, dataset_download_params.DatasetDownloadParams),
                post_parser=ResultWrapper[DatasetDownloadResponse]._unwrapper,
            ),
            cast_to=cast(Type[DatasetDownloadResponse], ResultWrapper[DatasetDownloadResponse]),
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


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self)

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
                query=await async_maybe_transform(
                    {
                        "dataset_type": dataset_type,
                        "format": format,
                        "limit": limit,
                        "offset": offset,
                    },
                    dataset_list_params.DatasetListParams,
                ),
                post_parser=ResultWrapper[DatasetListResponse]._unwrapper,
            ),
            cast_to=cast(Type[DatasetListResponse], ResultWrapper[DatasetListResponse]),
        )

    async def download(
        self,
        *,
        dataset_id: int,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetDownloadResponse:
        """
        Get a url to download a single dataset.

        Args:
          format: Format results are returned in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/radar/datasets/download",
            body=await async_maybe_transform({"dataset_id": dataset_id}, dataset_download_params.DatasetDownloadParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, dataset_download_params.DatasetDownloadParams),
                post_parser=ResultWrapper[DatasetDownloadResponse]._unwrapper,
            ),
            cast_to=cast(Type[DatasetDownloadResponse], ResultWrapper[DatasetDownloadResponse]),
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
                query=await async_maybe_transform({"date": date}, dataset_get_params.DatasetGetParams),
            ),
            cast_to=str,
        )


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.list = to_raw_response_wrapper(
            datasets.list,
        )
        self.download = to_raw_response_wrapper(
            datasets.download,
        )
        self.get = to_raw_response_wrapper(
            datasets.get,
        )


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.list = async_to_raw_response_wrapper(
            datasets.list,
        )
        self.download = async_to_raw_response_wrapper(
            datasets.download,
        )
        self.get = async_to_raw_response_wrapper(
            datasets.get,
        )


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.list = to_streamed_response_wrapper(
            datasets.list,
        )
        self.download = to_streamed_response_wrapper(
            datasets.download,
        )
        self.get = to_streamed_response_wrapper(
            datasets.get,
        )


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.list = async_to_streamed_response_wrapper(
            datasets.list,
        )
        self.download = async_to_streamed_response_wrapper(
            datasets.download,
        )
        self.get = async_to_streamed_response_wrapper(
            datasets.get,
        )
