# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .block_senders import (
    BlockSendersResource,
    AsyncBlockSendersResource,
    BlockSendersResourceWithRawResponse,
    AsyncBlockSendersResourceWithRawResponse,
    BlockSendersResourceWithStreamingResponse,
    AsyncBlockSendersResourceWithStreamingResponse,
)
from .allow_patterns import (
    AllowPatternsResource,
    AsyncAllowPatternsResource,
    AllowPatternsResourceWithRawResponse,
    AsyncAllowPatternsResourceWithRawResponse,
    AllowPatternsResourceWithStreamingResponse,
    AsyncAllowPatternsResourceWithStreamingResponse,
)
from .trusted_domains import (
    TrustedDomainsResource,
    AsyncTrustedDomainsResource,
    TrustedDomainsResourceWithRawResponse,
    AsyncTrustedDomainsResourceWithRawResponse,
    TrustedDomainsResourceWithStreamingResponse,
    AsyncTrustedDomainsResourceWithStreamingResponse,
)
from .impersonation_registry import (
    ImpersonationRegistryResource,
    AsyncImpersonationRegistryResource,
    ImpersonationRegistryResourceWithRawResponse,
    AsyncImpersonationRegistryResourceWithRawResponse,
    ImpersonationRegistryResourceWithStreamingResponse,
    AsyncImpersonationRegistryResourceWithStreamingResponse,
)

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def allow_patterns(self) -> AllowPatternsResource:
        return AllowPatternsResource(self._client)

    @cached_property
    def block_senders(self) -> BlockSendersResource:
        return BlockSendersResource(self._client)

    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def impersonation_registry(self) -> ImpersonationRegistryResource:
        return ImpersonationRegistryResource(self._client)

    @cached_property
    def trusted_domains(self) -> TrustedDomainsResource:
        return TrustedDomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self)


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def allow_patterns(self) -> AsyncAllowPatternsResource:
        return AsyncAllowPatternsResource(self._client)

    @cached_property
    def block_senders(self) -> AsyncBlockSendersResource:
        return AsyncBlockSendersResource(self._client)

    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def impersonation_registry(self) -> AsyncImpersonationRegistryResource:
        return AsyncImpersonationRegistryResource(self._client)

    @cached_property
    def trusted_domains(self) -> AsyncTrustedDomainsResource:
        return AsyncTrustedDomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self)


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def allow_patterns(self) -> AllowPatternsResourceWithRawResponse:
        return AllowPatternsResourceWithRawResponse(self._settings.allow_patterns)

    @cached_property
    def block_senders(self) -> BlockSendersResourceWithRawResponse:
        return BlockSendersResourceWithRawResponse(self._settings.block_senders)

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._settings.domains)

    @cached_property
    def impersonation_registry(self) -> ImpersonationRegistryResourceWithRawResponse:
        return ImpersonationRegistryResourceWithRawResponse(self._settings.impersonation_registry)

    @cached_property
    def trusted_domains(self) -> TrustedDomainsResourceWithRawResponse:
        return TrustedDomainsResourceWithRawResponse(self._settings.trusted_domains)


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def allow_patterns(self) -> AsyncAllowPatternsResourceWithRawResponse:
        return AsyncAllowPatternsResourceWithRawResponse(self._settings.allow_patterns)

    @cached_property
    def block_senders(self) -> AsyncBlockSendersResourceWithRawResponse:
        return AsyncBlockSendersResourceWithRawResponse(self._settings.block_senders)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._settings.domains)

    @cached_property
    def impersonation_registry(self) -> AsyncImpersonationRegistryResourceWithRawResponse:
        return AsyncImpersonationRegistryResourceWithRawResponse(self._settings.impersonation_registry)

    @cached_property
    def trusted_domains(self) -> AsyncTrustedDomainsResourceWithRawResponse:
        return AsyncTrustedDomainsResourceWithRawResponse(self._settings.trusted_domains)


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def allow_patterns(self) -> AllowPatternsResourceWithStreamingResponse:
        return AllowPatternsResourceWithStreamingResponse(self._settings.allow_patterns)

    @cached_property
    def block_senders(self) -> BlockSendersResourceWithStreamingResponse:
        return BlockSendersResourceWithStreamingResponse(self._settings.block_senders)

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._settings.domains)

    @cached_property
    def impersonation_registry(self) -> ImpersonationRegistryResourceWithStreamingResponse:
        return ImpersonationRegistryResourceWithStreamingResponse(self._settings.impersonation_registry)

    @cached_property
    def trusted_domains(self) -> TrustedDomainsResourceWithStreamingResponse:
        return TrustedDomainsResourceWithStreamingResponse(self._settings.trusted_domains)


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def allow_patterns(self) -> AsyncAllowPatternsResourceWithStreamingResponse:
        return AsyncAllowPatternsResourceWithStreamingResponse(self._settings.allow_patterns)

    @cached_property
    def block_senders(self) -> AsyncBlockSendersResourceWithStreamingResponse:
        return AsyncBlockSendersResourceWithStreamingResponse(self._settings.block_senders)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._settings.domains)

    @cached_property
    def impersonation_registry(self) -> AsyncImpersonationRegistryResourceWithStreamingResponse:
        return AsyncImpersonationRegistryResourceWithStreamingResponse(self._settings.impersonation_registry)

    @cached_property
    def trusted_domains(self) -> AsyncTrustedDomainsResourceWithStreamingResponse:
        return AsyncTrustedDomainsResourceWithStreamingResponse(self._settings.trusted_domains)
