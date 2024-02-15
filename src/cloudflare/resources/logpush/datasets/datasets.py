# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .fields import Fields, AsyncFields

from ...._compat import cached_property

from .jobs import Jobs, AsyncJobs

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
from .fields import (
    Fields,
    AsyncFields,
    FieldsWithRawResponse,
    AsyncFieldsWithRawResponse,
    FieldsWithStreamingResponse,
    AsyncFieldsWithStreamingResponse,
)
from .jobs import (
    Jobs,
    AsyncJobs,
    JobsWithRawResponse,
    AsyncJobsWithRawResponse,
    JobsWithStreamingResponse,
    AsyncJobsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["Datasets", "AsyncDatasets"]


class Datasets(SyncAPIResource):
    @cached_property
    def fields(self) -> Fields:
        return Fields(self._client)

    @cached_property
    def jobs(self) -> Jobs:
        return Jobs(self._client)

    @cached_property
    def with_raw_response(self) -> DatasetsWithRawResponse:
        return DatasetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsWithStreamingResponse:
        return DatasetsWithStreamingResponse(self)


class AsyncDatasets(AsyncAPIResource):
    @cached_property
    def fields(self) -> AsyncFields:
        return AsyncFields(self._client)

    @cached_property
    def jobs(self) -> AsyncJobs:
        return AsyncJobs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasetsWithRawResponse:
        return AsyncDatasetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsWithStreamingResponse:
        return AsyncDatasetsWithStreamingResponse(self)


class DatasetsWithRawResponse:
    def __init__(self, datasets: Datasets) -> None:
        self._datasets = datasets

    @cached_property
    def fields(self) -> FieldsWithRawResponse:
        return FieldsWithRawResponse(self._datasets.fields)

    @cached_property
    def jobs(self) -> JobsWithRawResponse:
        return JobsWithRawResponse(self._datasets.jobs)


class AsyncDatasetsWithRawResponse:
    def __init__(self, datasets: AsyncDatasets) -> None:
        self._datasets = datasets

    @cached_property
    def fields(self) -> AsyncFieldsWithRawResponse:
        return AsyncFieldsWithRawResponse(self._datasets.fields)

    @cached_property
    def jobs(self) -> AsyncJobsWithRawResponse:
        return AsyncJobsWithRawResponse(self._datasets.jobs)


class DatasetsWithStreamingResponse:
    def __init__(self, datasets: Datasets) -> None:
        self._datasets = datasets

    @cached_property
    def fields(self) -> FieldsWithStreamingResponse:
        return FieldsWithStreamingResponse(self._datasets.fields)

    @cached_property
    def jobs(self) -> JobsWithStreamingResponse:
        return JobsWithStreamingResponse(self._datasets.jobs)


class AsyncDatasetsWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasets) -> None:
        self._datasets = datasets

    @cached_property
    def fields(self) -> AsyncFieldsWithStreamingResponse:
        return AsyncFieldsWithStreamingResponse(self._datasets.fields)

    @cached_property
    def jobs(self) -> AsyncJobsWithStreamingResponse:
        return AsyncJobsWithStreamingResponse(self._datasets.jobs)
