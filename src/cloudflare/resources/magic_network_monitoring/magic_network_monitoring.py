# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .rules.rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from .configs.configs import (
    ConfigsResource,
    AsyncConfigsResource,
    ConfigsResourceWithRawResponse,
    AsyncConfigsResourceWithRawResponse,
    ConfigsResourceWithStreamingResponse,
    AsyncConfigsResourceWithStreamingResponse,
)
from .vpc_flows.vpc_flows import (
    VPCFlowsResource,
    AsyncVPCFlowsResource,
    VPCFlowsResourceWithRawResponse,
    AsyncVPCFlowsResourceWithRawResponse,
    VPCFlowsResourceWithStreamingResponse,
    AsyncVPCFlowsResourceWithStreamingResponse,
)

__all__ = ["MagicNetworkMonitoringResource", "AsyncMagicNetworkMonitoringResource"]


class MagicNetworkMonitoringResource(SyncAPIResource):
    @cached_property
    def vpc_flows(self) -> VPCFlowsResource:
        return VPCFlowsResource(self._client)

    @cached_property
    def configs(self) -> ConfigsResource:
        return ConfigsResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> MagicNetworkMonitoringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MagicNetworkMonitoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MagicNetworkMonitoringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MagicNetworkMonitoringResourceWithStreamingResponse(self)


class AsyncMagicNetworkMonitoringResource(AsyncAPIResource):
    @cached_property
    def vpc_flows(self) -> AsyncVPCFlowsResource:
        return AsyncVPCFlowsResource(self._client)

    @cached_property
    def configs(self) -> AsyncConfigsResource:
        return AsyncConfigsResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMagicNetworkMonitoringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMagicNetworkMonitoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMagicNetworkMonitoringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMagicNetworkMonitoringResourceWithStreamingResponse(self)


class MagicNetworkMonitoringResourceWithRawResponse:
    def __init__(self, magic_network_monitoring: MagicNetworkMonitoringResource) -> None:
        self._magic_network_monitoring = magic_network_monitoring

    @cached_property
    def vpc_flows(self) -> VPCFlowsResourceWithRawResponse:
        return VPCFlowsResourceWithRawResponse(self._magic_network_monitoring.vpc_flows)

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
    def vpc_flows(self) -> AsyncVPCFlowsResourceWithRawResponse:
        return AsyncVPCFlowsResourceWithRawResponse(self._magic_network_monitoring.vpc_flows)

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
    def vpc_flows(self) -> VPCFlowsResourceWithStreamingResponse:
        return VPCFlowsResourceWithStreamingResponse(self._magic_network_monitoring.vpc_flows)

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
    def vpc_flows(self) -> AsyncVPCFlowsResourceWithStreamingResponse:
        return AsyncVPCFlowsResourceWithStreamingResponse(self._magic_network_monitoring.vpc_flows)

    @cached_property
    def configs(self) -> AsyncConfigsResourceWithStreamingResponse:
        return AsyncConfigsResourceWithStreamingResponse(self._magic_network_monitoring.configs)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._magic_network_monitoring.rules)
