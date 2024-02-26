# File generated from our OpenAPI spec by Stainless.

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

__all__ = ["MNMs", "AsyncMNMs"]


class MNMs(SyncAPIResource):
    @cached_property
    def configs(self) -> Configs:
        return Configs(self._client)

    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def with_raw_response(self) -> MNMsWithRawResponse:
        return MNMsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MNMsWithStreamingResponse:
        return MNMsWithStreamingResponse(self)


class AsyncMNMs(AsyncAPIResource):
    @cached_property
    def configs(self) -> AsyncConfigs:
        return AsyncConfigs(self._client)

    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMNMsWithRawResponse:
        return AsyncMNMsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMNMsWithStreamingResponse:
        return AsyncMNMsWithStreamingResponse(self)


class MNMsWithRawResponse:
    def __init__(self, mnms: MNMs) -> None:
        self._mnms = mnms

    @cached_property
    def configs(self) -> ConfigsWithRawResponse:
        return ConfigsWithRawResponse(self._mnms.configs)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._mnms.rules)


class AsyncMNMsWithRawResponse:
    def __init__(self, mnms: AsyncMNMs) -> None:
        self._mnms = mnms

    @cached_property
    def configs(self) -> AsyncConfigsWithRawResponse:
        return AsyncConfigsWithRawResponse(self._mnms.configs)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._mnms.rules)


class MNMsWithStreamingResponse:
    def __init__(self, mnms: MNMs) -> None:
        self._mnms = mnms

    @cached_property
    def configs(self) -> ConfigsWithStreamingResponse:
        return ConfigsWithStreamingResponse(self._mnms.configs)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._mnms.rules)


class AsyncMNMsWithStreamingResponse:
    def __init__(self, mnms: AsyncMNMs) -> None:
        self._mnms = mnms

    @cached_property
    def configs(self) -> AsyncConfigsWithStreamingResponse:
        return AsyncConfigsWithStreamingResponse(self._mnms.configs)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._mnms.rules)
