# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .projects.projects import ProjectsResource, AsyncProjectsResource

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .projects import ProjectsResource, AsyncProjectsResource, ProjectsResourceWithRawResponse, AsyncProjectsResourceWithRawResponse, ProjectsResourceWithStreamingResponse, AsyncProjectsResourceWithStreamingResponse

__all__ = ["PagesResource", "AsyncPagesResource"]

class PagesResource(SyncAPIResource):
    @cached_property
    def projects(self) -> ProjectsResource:
        return ProjectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PagesResourceWithRawResponse:
        return PagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PagesResourceWithStreamingResponse:
        return PagesResourceWithStreamingResponse(self)

class AsyncPagesResource(AsyncAPIResource):
    @cached_property
    def projects(self) -> AsyncProjectsResource:
        return AsyncProjectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPagesResourceWithRawResponse:
        return AsyncPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPagesResourceWithStreamingResponse:
        return AsyncPagesResourceWithStreamingResponse(self)

class PagesResourceWithRawResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

    @cached_property
    def projects(self) -> ProjectsResourceWithRawResponse:
        return ProjectsResourceWithRawResponse(self._pages.projects)

class AsyncPagesResourceWithRawResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithRawResponse:
        return AsyncProjectsResourceWithRawResponse(self._pages.projects)

class PagesResourceWithStreamingResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

    @cached_property
    def projects(self) -> ProjectsResourceWithStreamingResponse:
        return ProjectsResourceWithStreamingResponse(self._pages.projects)

class AsyncPagesResourceWithStreamingResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self._pages.projects)