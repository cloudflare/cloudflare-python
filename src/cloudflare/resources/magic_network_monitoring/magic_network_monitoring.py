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
from .configs import (
    Configs,
    AsyncConfigs,
    ConfigsWithRawResponse,
    AsyncConfigsWithRawResponse,
    ConfigsWithStreamingResponse,
    AsyncConfigsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .rules.rules import Rules, AsyncRules
from .configs.configs import Configs, AsyncConfigs

__all__ = ["MagicNetworkMonitoring", "AsyncMagicNetworkMonitoring"]


class MagicNetworkMonitoring(SyncAPIResource):
    @cached_property
    def configs(self) -> Configs:
        return Configs(self._client)

    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def with_raw_response(self) -> MagicNetworkMonitoringWithRawResponse:
        return MagicNetworkMonitoringWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MagicNetworkMonitoringWithStreamingResponse:
        return MagicNetworkMonitoringWithStreamingResponse(self)


class AsyncMagicNetworkMonitoring(AsyncAPIResource):
    @cached_property
    def configs(self) -> AsyncConfigs:
        return AsyncConfigs(self._client)

    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMagicNetworkMonitoringWithRawResponse:
        return AsyncMagicNetworkMonitoringWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMagicNetworkMonitoringWithStreamingResponse:
        return AsyncMagicNetworkMonitoringWithStreamingResponse(self)


class MagicNetworkMonitoringWithRawResponse:
    def __init__(self, magic_network_monitoring: MagicNetworkMonitoring) -> None:
        self._magic_network_monitoring = magic_network_monitoring

    @cached_property
    def configs(self) -> ConfigsWithRawResponse:
        return ConfigsWithRawResponse(self._magic_network_monitoring.configs)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._magic_network_monitoring.rules)


class AsyncMagicNetworkMonitoringWithRawResponse:
    def __init__(self, magic_network_monitoring: AsyncMagicNetworkMonitoring) -> None:
        self._magic_network_monitoring = magic_network_monitoring

    @cached_property
    def configs(self) -> AsyncConfigsWithRawResponse:
        return AsyncConfigsWithRawResponse(self._magic_network_monitoring.configs)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._magic_network_monitoring.rules)


class MagicNetworkMonitoringWithStreamingResponse:
    def __init__(self, magic_network_monitoring: MagicNetworkMonitoring) -> None:
        self._magic_network_monitoring = magic_network_monitoring

    @cached_property
    def configs(self) -> ConfigsWithStreamingResponse:
        return ConfigsWithStreamingResponse(self._magic_network_monitoring.configs)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._magic_network_monitoring.rules)


class AsyncMagicNetworkMonitoringWithStreamingResponse:
    def __init__(self, magic_network_monitoring: AsyncMagicNetworkMonitoring) -> None:
        self._magic_network_monitoring = magic_network_monitoring

    @cached_property
    def configs(self) -> AsyncConfigsWithStreamingResponse:
        return AsyncConfigsWithStreamingResponse(self._magic_network_monitoring.configs)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._magic_network_monitoring.rules)
