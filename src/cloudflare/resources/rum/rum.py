# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .rules import (
    Rules,
    AsyncRules,
    RulesWithRawResponse,
    AsyncRulesWithRawResponse,
    RulesWithStreamingResponse,
    AsyncRulesWithStreamingResponse,
)
from ..._compat import cached_property
from .site_info import (
    SiteInfo,
    AsyncSiteInfo,
    SiteInfoWithRawResponse,
    AsyncSiteInfoWithRawResponse,
    SiteInfoWithStreamingResponse,
    AsyncSiteInfoWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RUM", "AsyncRUM"]


class RUM(SyncAPIResource):
    @cached_property
    def site_info(self) -> SiteInfo:
        return SiteInfo(self._client)

    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def with_raw_response(self) -> RUMWithRawResponse:
        return RUMWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RUMWithStreamingResponse:
        return RUMWithStreamingResponse(self)


class AsyncRUM(AsyncAPIResource):
    @cached_property
    def site_info(self) -> AsyncSiteInfo:
        return AsyncSiteInfo(self._client)

    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRUMWithRawResponse:
        return AsyncRUMWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRUMWithStreamingResponse:
        return AsyncRUMWithStreamingResponse(self)


class RUMWithRawResponse:
    def __init__(self, rum: RUM) -> None:
        self._rum = rum

    @cached_property
    def site_info(self) -> SiteInfoWithRawResponse:
        return SiteInfoWithRawResponse(self._rum.site_info)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._rum.rules)


class AsyncRUMWithRawResponse:
    def __init__(self, rum: AsyncRUM) -> None:
        self._rum = rum

    @cached_property
    def site_info(self) -> AsyncSiteInfoWithRawResponse:
        return AsyncSiteInfoWithRawResponse(self._rum.site_info)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._rum.rules)


class RUMWithStreamingResponse:
    def __init__(self, rum: RUM) -> None:
        self._rum = rum

    @cached_property
    def site_info(self) -> SiteInfoWithStreamingResponse:
        return SiteInfoWithStreamingResponse(self._rum.site_info)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._rum.rules)


class AsyncRUMWithStreamingResponse:
    def __init__(self, rum: AsyncRUM) -> None:
        self._rum = rum

    @cached_property
    def site_info(self) -> AsyncSiteInfoWithStreamingResponse:
        return AsyncSiteInfoWithStreamingResponse(self._rum.site_info)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._rum.rules)
