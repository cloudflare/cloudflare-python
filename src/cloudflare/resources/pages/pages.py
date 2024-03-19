# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .projects import (
    Projects,
    AsyncProjects,
    ProjectsWithRawResponse,
    AsyncProjectsWithRawResponse,
    ProjectsWithStreamingResponse,
    AsyncProjectsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .projects.projects import Projects, AsyncProjects

__all__ = ["Pages", "AsyncPages"]


class Pages(SyncAPIResource):
    @cached_property
    def projects(self) -> Projects:
        return Projects(self._client)

    @cached_property
    def with_raw_response(self) -> PagesWithRawResponse:
        return PagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PagesWithStreamingResponse:
        return PagesWithStreamingResponse(self)


class AsyncPages(AsyncAPIResource):
    @cached_property
    def projects(self) -> AsyncProjects:
        return AsyncProjects(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPagesWithRawResponse:
        return AsyncPagesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPagesWithStreamingResponse:
        return AsyncPagesWithStreamingResponse(self)


class PagesWithRawResponse:
    def __init__(self, pages: Pages) -> None:
        self._pages = pages

    @cached_property
    def projects(self) -> ProjectsWithRawResponse:
        return ProjectsWithRawResponse(self._pages.projects)


class AsyncPagesWithRawResponse:
    def __init__(self, pages: AsyncPages) -> None:
        self._pages = pages

    @cached_property
    def projects(self) -> AsyncProjectsWithRawResponse:
        return AsyncProjectsWithRawResponse(self._pages.projects)


class PagesWithStreamingResponse:
    def __init__(self, pages: Pages) -> None:
        self._pages = pages

    @cached_property
    def projects(self) -> ProjectsWithStreamingResponse:
        return ProjectsWithStreamingResponse(self._pages.projects)


class AsyncPagesWithStreamingResponse:
    def __init__(self, pages: AsyncPages) -> None:
        self._pages = pages

    @cached_property
    def projects(self) -> AsyncProjectsWithStreamingResponse:
        return AsyncProjectsWithStreamingResponse(self._pages.projects)
