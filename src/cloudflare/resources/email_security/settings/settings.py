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
from .allow_policies import (
    AllowPoliciesResource,
    AsyncAllowPoliciesResource,
    AllowPoliciesResourceWithRawResponse,
    AsyncAllowPoliciesResourceWithRawResponse,
    AllowPoliciesResourceWithStreamingResponse,
    AsyncAllowPoliciesResourceWithStreamingResponse,
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
    def allow_policies(self) -> AllowPoliciesResource:
        return AllowPoliciesResource(self._client)

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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def allow_policies(self) -> AsyncAllowPoliciesResource:
        return AsyncAllowPoliciesResource(self._client)

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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def allow_policies(self) -> AllowPoliciesResourceWithRawResponse:
        return AllowPoliciesResourceWithRawResponse(self._settings.allow_policies)

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
    def allow_policies(self) -> AsyncAllowPoliciesResourceWithRawResponse:
        return AsyncAllowPoliciesResourceWithRawResponse(self._settings.allow_policies)

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
    def allow_policies(self) -> AllowPoliciesResourceWithStreamingResponse:
        return AllowPoliciesResourceWithStreamingResponse(self._settings.allow_policies)

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
    def allow_policies(self) -> AsyncAllowPoliciesResourceWithStreamingResponse:
        return AsyncAllowPoliciesResourceWithStreamingResponse(self._settings.allow_policies)

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
