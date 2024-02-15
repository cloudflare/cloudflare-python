# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .rules import Rules, AsyncRules

from ....._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .rules import (
    Rules,
    AsyncRules,
    RulesWithRawResponse,
    AsyncRulesWithRawResponse,
    RulesWithStreamingResponse,
    AsyncRulesWithStreamingResponse,
)
from ....._wrappers import ResultWrapper

__all__ = ["AccessRules", "AsyncAccessRules"]


class AccessRules(SyncAPIResource):
    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def with_raw_response(self) -> AccessRulesWithRawResponse:
        return AccessRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessRulesWithStreamingResponse:
        return AccessRulesWithStreamingResponse(self)


class AsyncAccessRules(AsyncAPIResource):
    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccessRulesWithRawResponse:
        return AsyncAccessRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessRulesWithStreamingResponse:
        return AsyncAccessRulesWithStreamingResponse(self)


class AccessRulesWithRawResponse:
    def __init__(self, access_rules: AccessRules) -> None:
        self._access_rules = access_rules

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._access_rules.rules)


class AsyncAccessRulesWithRawResponse:
    def __init__(self, access_rules: AsyncAccessRules) -> None:
        self._access_rules = access_rules

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._access_rules.rules)


class AccessRulesWithStreamingResponse:
    def __init__(self, access_rules: AccessRules) -> None:
        self._access_rules = access_rules

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._access_rules.rules)


class AsyncAccessRulesWithStreamingResponse:
    def __init__(self, access_rules: AsyncAccessRules) -> None:
        self._access_rules = access_rules

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._access_rules.rules)
