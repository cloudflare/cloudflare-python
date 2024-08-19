# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .issues import (
    IssuesResource,
    AsyncIssuesResource,
    IssuesResourceWithRawResponse,
    AsyncIssuesResourceWithRawResponse,
    IssuesResourceWithStreamingResponse,
    AsyncIssuesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .issue_types import (
    IssueTypesResource,
    AsyncIssueTypesResource,
    IssueTypesResourceWithRawResponse,
    AsyncIssueTypesResourceWithRawResponse,
    IssueTypesResourceWithStreamingResponse,
    AsyncIssueTypesResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AttackSurfaceReportResource", "AsyncAttackSurfaceReportResource"]


class AttackSurfaceReportResource(SyncAPIResource):
    @cached_property
    def issue_types(self) -> IssueTypesResource:
        return IssueTypesResource(self._client)

    @cached_property
    def issues(self) -> IssuesResource:
        return IssuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AttackSurfaceReportResourceWithRawResponse:
        return AttackSurfaceReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttackSurfaceReportResourceWithStreamingResponse:
        return AttackSurfaceReportResourceWithStreamingResponse(self)


class AsyncAttackSurfaceReportResource(AsyncAPIResource):
    @cached_property
    def issue_types(self) -> AsyncIssueTypesResource:
        return AsyncIssueTypesResource(self._client)

    @cached_property
    def issues(self) -> AsyncIssuesResource:
        return AsyncIssuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAttackSurfaceReportResourceWithRawResponse:
        return AsyncAttackSurfaceReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttackSurfaceReportResourceWithStreamingResponse:
        return AsyncAttackSurfaceReportResourceWithStreamingResponse(self)


class AttackSurfaceReportResourceWithRawResponse:
    def __init__(self, attack_surface_report: AttackSurfaceReportResource) -> None:
        self._attack_surface_report = attack_surface_report

    @cached_property
    def issue_types(self) -> IssueTypesResourceWithRawResponse:
        return IssueTypesResourceWithRawResponse(self._attack_surface_report.issue_types)

    @cached_property
    def issues(self) -> IssuesResourceWithRawResponse:
        return IssuesResourceWithRawResponse(self._attack_surface_report.issues)


class AsyncAttackSurfaceReportResourceWithRawResponse:
    def __init__(self, attack_surface_report: AsyncAttackSurfaceReportResource) -> None:
        self._attack_surface_report = attack_surface_report

    @cached_property
    def issue_types(self) -> AsyncIssueTypesResourceWithRawResponse:
        return AsyncIssueTypesResourceWithRawResponse(self._attack_surface_report.issue_types)

    @cached_property
    def issues(self) -> AsyncIssuesResourceWithRawResponse:
        return AsyncIssuesResourceWithRawResponse(self._attack_surface_report.issues)


class AttackSurfaceReportResourceWithStreamingResponse:
    def __init__(self, attack_surface_report: AttackSurfaceReportResource) -> None:
        self._attack_surface_report = attack_surface_report

    @cached_property
    def issue_types(self) -> IssueTypesResourceWithStreamingResponse:
        return IssueTypesResourceWithStreamingResponse(self._attack_surface_report.issue_types)

    @cached_property
    def issues(self) -> IssuesResourceWithStreamingResponse:
        return IssuesResourceWithStreamingResponse(self._attack_surface_report.issues)


class AsyncAttackSurfaceReportResourceWithStreamingResponse:
    def __init__(self, attack_surface_report: AsyncAttackSurfaceReportResource) -> None:
        self._attack_surface_report = attack_surface_report

    @cached_property
    def issue_types(self) -> AsyncIssueTypesResourceWithStreamingResponse:
        return AsyncIssueTypesResourceWithStreamingResponse(self._attack_surface_report.issue_types)

    @cached_property
    def issues(self) -> AsyncIssuesResourceWithStreamingResponse:
        return AsyncIssuesResourceWithStreamingResponse(self._attack_surface_report.issues)
