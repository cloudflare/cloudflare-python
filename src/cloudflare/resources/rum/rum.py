# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .site_infos import SiteInfos, AsyncSiteInfos

from ..._compat import cached_property

from .rules import Rules, AsyncRules

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from .site_infos import (
    SiteInfos,
    AsyncSiteInfos,
    SiteInfosWithRawResponse,
    AsyncSiteInfosWithRawResponse,
    SiteInfosWithStreamingResponse,
    AsyncSiteInfosWithStreamingResponse,
)
from .rules import (
    Rules,
    AsyncRules,
    RulesWithRawResponse,
    AsyncRulesWithRawResponse,
    RulesWithStreamingResponse,
    AsyncRulesWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Rum", "AsyncRum"]


class Rum(SyncAPIResource):
    @cached_property
    def site_infos(self) -> SiteInfos:
        return SiteInfos(self._client)

    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def with_raw_response(self) -> RumWithRawResponse:
        return RumWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RumWithStreamingResponse:
        return RumWithStreamingResponse(self)


class AsyncRum(AsyncAPIResource):
    @cached_property
    def site_infos(self) -> AsyncSiteInfos:
        return AsyncSiteInfos(self._client)

    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRumWithRawResponse:
        return AsyncRumWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRumWithStreamingResponse:
        return AsyncRumWithStreamingResponse(self)


class RumWithRawResponse:
    def __init__(self, rum: Rum) -> None:
        self._rum = rum

    @cached_property
    def site_infos(self) -> SiteInfosWithRawResponse:
        return SiteInfosWithRawResponse(self._rum.site_infos)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._rum.rules)


class AsyncRumWithRawResponse:
    def __init__(self, rum: AsyncRum) -> None:
        self._rum = rum

    @cached_property
    def site_infos(self) -> AsyncSiteInfosWithRawResponse:
        return AsyncSiteInfosWithRawResponse(self._rum.site_infos)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._rum.rules)


class RumWithStreamingResponse:
    def __init__(self, rum: Rum) -> None:
        self._rum = rum

    @cached_property
    def site_infos(self) -> SiteInfosWithStreamingResponse:
        return SiteInfosWithStreamingResponse(self._rum.site_infos)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._rum.rules)


class AsyncRumWithStreamingResponse:
    def __init__(self, rum: AsyncRum) -> None:
        self._rum = rum

    @cached_property
    def site_infos(self) -> AsyncSiteInfosWithStreamingResponse:
        return AsyncSiteInfosWithStreamingResponse(self._rum.site_infos)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._rum.rules)
