# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .issues import (
    Issues,
    AsyncIssues,
    IssuesWithRawResponse,
    AsyncIssuesWithRawResponse,
    IssuesWithStreamingResponse,
    AsyncIssuesWithStreamingResponse,
)
from ...._compat import cached_property
from .issue_types import (
    IssueTypes,
    AsyncIssueTypes,
    IssueTypesWithRawResponse,
    AsyncIssueTypesWithRawResponse,
    IssueTypesWithStreamingResponse,
    AsyncIssueTypesWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AttackSurfaceReport", "AsyncAttackSurfaceReport"]


class AttackSurfaceReport(SyncAPIResource):
    @cached_property
    def issue_types(self) -> IssueTypes:
        return IssueTypes(self._client)

    @cached_property
    def issues(self) -> Issues:
        return Issues(self._client)

    @cached_property
    def with_raw_response(self) -> AttackSurfaceReportWithRawResponse:
        return AttackSurfaceReportWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttackSurfaceReportWithStreamingResponse:
        return AttackSurfaceReportWithStreamingResponse(self)


class AsyncAttackSurfaceReport(AsyncAPIResource):
    @cached_property
    def issue_types(self) -> AsyncIssueTypes:
        return AsyncIssueTypes(self._client)

    @cached_property
    def issues(self) -> AsyncIssues:
        return AsyncIssues(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAttackSurfaceReportWithRawResponse:
        return AsyncAttackSurfaceReportWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttackSurfaceReportWithStreamingResponse:
        return AsyncAttackSurfaceReportWithStreamingResponse(self)


class AttackSurfaceReportWithRawResponse:
    def __init__(self, attack_surface_report: AttackSurfaceReport) -> None:
        self._attack_surface_report = attack_surface_report

    @cached_property
    def issue_types(self) -> IssueTypesWithRawResponse:
        return IssueTypesWithRawResponse(self._attack_surface_report.issue_types)

    @cached_property
    def issues(self) -> IssuesWithRawResponse:
        return IssuesWithRawResponse(self._attack_surface_report.issues)


class AsyncAttackSurfaceReportWithRawResponse:
    def __init__(self, attack_surface_report: AsyncAttackSurfaceReport) -> None:
        self._attack_surface_report = attack_surface_report

    @cached_property
    def issue_types(self) -> AsyncIssueTypesWithRawResponse:
        return AsyncIssueTypesWithRawResponse(self._attack_surface_report.issue_types)

    @cached_property
    def issues(self) -> AsyncIssuesWithRawResponse:
        return AsyncIssuesWithRawResponse(self._attack_surface_report.issues)


class AttackSurfaceReportWithStreamingResponse:
    def __init__(self, attack_surface_report: AttackSurfaceReport) -> None:
        self._attack_surface_report = attack_surface_report

    @cached_property
    def issue_types(self) -> IssueTypesWithStreamingResponse:
        return IssueTypesWithStreamingResponse(self._attack_surface_report.issue_types)

    @cached_property
    def issues(self) -> IssuesWithStreamingResponse:
        return IssuesWithStreamingResponse(self._attack_surface_report.issues)


class AsyncAttackSurfaceReportWithStreamingResponse:
    def __init__(self, attack_surface_report: AsyncAttackSurfaceReport) -> None:
        self._attack_surface_report = attack_surface_report

    @cached_property
    def issue_types(self) -> AsyncIssueTypesWithStreamingResponse:
        return AsyncIssueTypesWithStreamingResponse(self._attack_surface_report.issue_types)

    @cached_property
    def issues(self) -> AsyncIssuesWithStreamingResponse:
        return AsyncIssuesWithStreamingResponse(self._attack_surface_report.issues)
