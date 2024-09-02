# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .configs.configs import ConfigsResource, AsyncConfigsResource

from ..._compat import cached_property

from .rules.rules import RulesResource, AsyncRulesResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .configs import (
    ConfigsResource,
    AsyncConfigsResource,
    ConfigsResourceWithRawResponse,
    AsyncConfigsResourceWithRawResponse,
    ConfigsResourceWithStreamingResponse,
    AsyncConfigsResourceWithStreamingResponse,
)
from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)

__all__ = ["MagicNetworkMonitoringResource", "AsyncMagicNetworkMonitoringResource"]


class MagicNetworkMonitoringResource(SyncAPIResource):
    @cached_property
    def configs(self) -> ConfigsResource:
        return ConfigsResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> MagicNetworkMonitoringResourceWithRawResponse:
        return MagicNetworkMonitoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MagicNetworkMonitoringResourceWithStreamingResponse:
        return MagicNetworkMonitoringResourceWithStreamingResponse(self)


class AsyncMagicNetworkMonitoringResource(AsyncAPIResource):
    @cached_property
    def configs(self) -> AsyncConfigsResource:
        return AsyncConfigsResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMagicNetworkMonitoringResourceWithRawResponse:
        return AsyncMagicNetworkMonitoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMagicNetworkMonitoringResourceWithStreamingResponse:
        return AsyncMagicNetworkMonitoringResourceWithStreamingResponse(self)


class MagicNetworkMonitoringResourceWithRawResponse:
    def __init__(self, magic_network_monitoring: MagicNetworkMonitoringResource) -> None:
        self._magic_network_monitoring = magic_network_monitoring

    @cached_property
    def configs(self) -> ConfigsResourceWithRawResponse:
        return ConfigsResourceWithRawResponse(self._magic_network_monitoring.configs)

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._magic_network_monitoring.rules)


class AsyncMagicNetworkMonitoringResourceWithRawResponse:
    def __init__(self, magic_network_monitoring: AsyncMagicNetworkMonitoringResource) -> None:
        self._magic_network_monitoring = magic_network_monitoring

    @cached_property
    def configs(self) -> AsyncConfigsResourceWithRawResponse:
        return AsyncConfigsResourceWithRawResponse(self._magic_network_monitoring.configs)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._magic_network_monitoring.rules)


class MagicNetworkMonitoringResourceWithStreamingResponse:
    def __init__(self, magic_network_monitoring: MagicNetworkMonitoringResource) -> None:
        self._magic_network_monitoring = magic_network_monitoring

    @cached_property
    def configs(self) -> ConfigsResourceWithStreamingResponse:
        return ConfigsResourceWithStreamingResponse(self._magic_network_monitoring.configs)

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._magic_network_monitoring.rules)


class AsyncMagicNetworkMonitoringResourceWithStreamingResponse:
    def __init__(self, magic_network_monitoring: AsyncMagicNetworkMonitoringResource) -> None:
        self._magic_network_monitoring = magic_network_monitoring

    @cached_property
    def configs(self) -> AsyncConfigsResourceWithStreamingResponse:
        return AsyncConfigsResourceWithStreamingResponse(self._magic_network_monitoring.configs)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._magic_network_monitoring.rules)
