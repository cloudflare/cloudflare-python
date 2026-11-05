# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .authenticator_catalog import (
    AuthenticatorCatalogResource,
    AsyncAuthenticatorCatalogResource,
    AuthenticatorCatalogResourceWithRawResponse,
    AsyncAuthenticatorCatalogResourceWithRawResponse,
    AuthenticatorCatalogResourceWithStreamingResponse,
    AsyncAuthenticatorCatalogResourceWithStreamingResponse,
)

__all__ = ["MfaResource", "AsyncMfaResource"]


class MfaResource(SyncAPIResource):
    @cached_property
    def authenticator_catalog(self) -> AuthenticatorCatalogResource:
        return AuthenticatorCatalogResource(self._client)

    @cached_property
    def with_raw_response(self) -> MfaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MfaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MfaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MfaResourceWithStreamingResponse(self)


class AsyncMfaResource(AsyncAPIResource):
    @cached_property
    def authenticator_catalog(self) -> AsyncAuthenticatorCatalogResource:
        return AsyncAuthenticatorCatalogResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMfaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMfaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMfaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMfaResourceWithStreamingResponse(self)


class MfaResourceWithRawResponse:
    def __init__(self, mfa: MfaResource) -> None:
        self._mfa = mfa

    @cached_property
    def authenticator_catalog(self) -> AuthenticatorCatalogResourceWithRawResponse:
        return AuthenticatorCatalogResourceWithRawResponse(self._mfa.authenticator_catalog)


class AsyncMfaResourceWithRawResponse:
    def __init__(self, mfa: AsyncMfaResource) -> None:
        self._mfa = mfa

    @cached_property
    def authenticator_catalog(self) -> AsyncAuthenticatorCatalogResourceWithRawResponse:
        return AsyncAuthenticatorCatalogResourceWithRawResponse(self._mfa.authenticator_catalog)


class MfaResourceWithStreamingResponse:
    def __init__(self, mfa: MfaResource) -> None:
        self._mfa = mfa

    @cached_property
    def authenticator_catalog(self) -> AuthenticatorCatalogResourceWithStreamingResponse:
        return AuthenticatorCatalogResourceWithStreamingResponse(self._mfa.authenticator_catalog)


class AsyncMfaResourceWithStreamingResponse:
    def __init__(self, mfa: AsyncMfaResource) -> None:
        self._mfa = mfa

    @cached_property
    def authenticator_catalog(self) -> AsyncAuthenticatorCatalogResourceWithStreamingResponse:
        return AsyncAuthenticatorCatalogResourceWithStreamingResponse(self._mfa.authenticator_catalog)
