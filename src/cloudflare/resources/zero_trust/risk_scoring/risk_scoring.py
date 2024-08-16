# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .integrations import (
    IntegrationsResource,
    AsyncIntegrationsResource,
    IntegrationsResourceWithRawResponse,
    AsyncIntegrationsResourceWithRawResponse,
    IntegrationsResourceWithStreamingResponse,
    AsyncIntegrationsResourceWithStreamingResponse,
)
from .integrations.integrations import IntegrationsResource, AsyncIntegrationsResource

__all__ = ["RiskScoringResource", "AsyncRiskScoringResource"]


class RiskScoringResource(SyncAPIResource):
    @cached_property
    def integrations(self) -> IntegrationsResource:
        return IntegrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RiskScoringResourceWithRawResponse:
        return RiskScoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RiskScoringResourceWithStreamingResponse:
        return RiskScoringResourceWithStreamingResponse(self)


class AsyncRiskScoringResource(AsyncAPIResource):
    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        return AsyncIntegrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRiskScoringResourceWithRawResponse:
        return AsyncRiskScoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRiskScoringResourceWithStreamingResponse:
        return AsyncRiskScoringResourceWithStreamingResponse(self)


class RiskScoringResourceWithRawResponse:
    def __init__(self, risk_scoring: RiskScoringResource) -> None:
        self._risk_scoring = risk_scoring

    @cached_property
    def integrations(self) -> IntegrationsResourceWithRawResponse:
        return IntegrationsResourceWithRawResponse(self._risk_scoring.integrations)


class AsyncRiskScoringResourceWithRawResponse:
    def __init__(self, risk_scoring: AsyncRiskScoringResource) -> None:
        self._risk_scoring = risk_scoring

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithRawResponse:
        return AsyncIntegrationsResourceWithRawResponse(self._risk_scoring.integrations)


class RiskScoringResourceWithStreamingResponse:
    def __init__(self, risk_scoring: RiskScoringResource) -> None:
        self._risk_scoring = risk_scoring

    @cached_property
    def integrations(self) -> IntegrationsResourceWithStreamingResponse:
        return IntegrationsResourceWithStreamingResponse(self._risk_scoring.integrations)


class AsyncRiskScoringResourceWithStreamingResponse:
    def __init__(self, risk_scoring: AsyncRiskScoringResource) -> None:
        self._risk_scoring = risk_scoring

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        return AsyncIntegrationsResourceWithStreamingResponse(self._risk_scoring.integrations)
