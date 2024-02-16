# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .audit_ssh_settings import (
    AuditSSHSettings,
    AsyncAuditSSHSettings,
    AuditSSHSettingsWithRawResponse,
    AsyncAuditSSHSettingsWithRawResponse,
    AuditSSHSettingsWithStreamingResponse,
    AsyncAuditSSHSettingsWithStreamingResponse,
)

__all__ = ["Gateway", "AsyncGateway"]


class Gateway(SyncAPIResource):
    @cached_property
    def audit_ssh_settings(self) -> AuditSSHSettings:
        return AuditSSHSettings(self._client)

    @cached_property
    def with_raw_response(self) -> GatewayWithRawResponse:
        return GatewayWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GatewayWithStreamingResponse:
        return GatewayWithStreamingResponse(self)


class AsyncGateway(AsyncAPIResource):
    @cached_property
    def audit_ssh_settings(self) -> AsyncAuditSSHSettings:
        return AsyncAuditSSHSettings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGatewayWithRawResponse:
        return AsyncGatewayWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGatewayWithStreamingResponse:
        return AsyncGatewayWithStreamingResponse(self)


class GatewayWithRawResponse:
    def __init__(self, gateway: Gateway) -> None:
        self._gateway = gateway

    @cached_property
    def audit_ssh_settings(self) -> AuditSSHSettingsWithRawResponse:
        return AuditSSHSettingsWithRawResponse(self._gateway.audit_ssh_settings)


class AsyncGatewayWithRawResponse:
    def __init__(self, gateway: AsyncGateway) -> None:
        self._gateway = gateway

    @cached_property
    def audit_ssh_settings(self) -> AsyncAuditSSHSettingsWithRawResponse:
        return AsyncAuditSSHSettingsWithRawResponse(self._gateway.audit_ssh_settings)


class GatewayWithStreamingResponse:
    def __init__(self, gateway: Gateway) -> None:
        self._gateway = gateway

    @cached_property
    def audit_ssh_settings(self) -> AuditSSHSettingsWithStreamingResponse:
        return AuditSSHSettingsWithStreamingResponse(self._gateway.audit_ssh_settings)


class AsyncGatewayWithStreamingResponse:
    def __init__(self, gateway: AsyncGateway) -> None:
        self._gateway = gateway

    @cached_property
    def audit_ssh_settings(self) -> AsyncAuditSSHSettingsWithStreamingResponse:
        return AsyncAuditSSHSettingsWithStreamingResponse(self._gateway.audit_ssh_settings)
