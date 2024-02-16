# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .configs.configs import Configs, AsyncConfigs

from ..._compat import cached_property

from .rules.rules import Rules, AsyncRules

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
from .configs import (
    Configs,
    AsyncConfigs,
    ConfigsWithRawResponse,
    AsyncConfigsWithRawResponse,
    ConfigsWithStreamingResponse,
    AsyncConfigsWithStreamingResponse,
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

__all__ = ["Mnms", "AsyncMnms"]


class Mnms(SyncAPIResource):
    @cached_property
    def configs(self) -> Configs:
        return Configs(self._client)

    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def with_raw_response(self) -> MnmsWithRawResponse:
        return MnmsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MnmsWithStreamingResponse:
        return MnmsWithStreamingResponse(self)


class AsyncMnms(AsyncAPIResource):
    @cached_property
    def configs(self) -> AsyncConfigs:
        return AsyncConfigs(self._client)

    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMnmsWithRawResponse:
        return AsyncMnmsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMnmsWithStreamingResponse:
        return AsyncMnmsWithStreamingResponse(self)


class MnmsWithRawResponse:
    def __init__(self, mnms: Mnms) -> None:
        self._mnms = mnms

    @cached_property
    def configs(self) -> ConfigsWithRawResponse:
        return ConfigsWithRawResponse(self._mnms.configs)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._mnms.rules)


class AsyncMnmsWithRawResponse:
    def __init__(self, mnms: AsyncMnms) -> None:
        self._mnms = mnms

    @cached_property
    def configs(self) -> AsyncConfigsWithRawResponse:
        return AsyncConfigsWithRawResponse(self._mnms.configs)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._mnms.rules)


class MnmsWithStreamingResponse:
    def __init__(self, mnms: Mnms) -> None:
        self._mnms = mnms

    @cached_property
    def configs(self) -> ConfigsWithStreamingResponse:
        return ConfigsWithStreamingResponse(self._mnms.configs)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._mnms.rules)


class AsyncMnmsWithStreamingResponse:
    def __init__(self, mnms: AsyncMnms) -> None:
        self._mnms = mnms

    @cached_property
    def configs(self) -> AsyncConfigsWithStreamingResponse:
        return AsyncConfigsWithStreamingResponse(self._mnms.configs)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._mnms.rules)
