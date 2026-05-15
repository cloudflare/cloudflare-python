# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.zero_trust.identity_providers.saml_certificate_create_response import SAMLCertificateCreateResponse

__all__ = ["SAMLCertificateResource", "AsyncSAMLCertificateResource"]


class SAMLCertificateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SAMLCertificateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SAMLCertificateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SAMLCertificateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SAMLCertificateResourceWithStreamingResponse(self)

    def create(
        self,
        identity_provider_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SAMLCertificateCreateResponse]:
        """
        Creates a new SAML encryption certificate set and assigns it to the specified
        SAML Identity Provider. This endpoint is idempotent - if the IdP already has a
        certificate set assigned, the existing certificate set is returned with a 200
        status.

        **Workflow for enabling SAML encryption:**

        1. Call this endpoint to create and assign a certificate set to the IdP
        2. Update the IdP configuration (PUT `/identity_providers/{id}`) with:
           - `config.enable_encryption: true`
           - `saml_certificate_set_id: <uid from step 1>`
        3. Configure the certificate's public key in your external SAML Identity
           Provider

        Args:
          account_id: Identifier.

          identity_provider_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identity_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `identity_provider_id` but received {identity_provider_id!r}"
            )
        return self._post(
            path_template(
                "/accounts/{account_id}/access/identity_providers/{identity_provider_id}/saml_certificate",
                account_id=account_id,
                identity_provider_id=identity_provider_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SAMLCertificateCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SAMLCertificateCreateResponse]], ResultWrapper[SAMLCertificateCreateResponse]),
        )


class AsyncSAMLCertificateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSAMLCertificateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSAMLCertificateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSAMLCertificateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSAMLCertificateResourceWithStreamingResponse(self)

    async def create(
        self,
        identity_provider_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SAMLCertificateCreateResponse]:
        """
        Creates a new SAML encryption certificate set and assigns it to the specified
        SAML Identity Provider. This endpoint is idempotent - if the IdP already has a
        certificate set assigned, the existing certificate set is returned with a 200
        status.

        **Workflow for enabling SAML encryption:**

        1. Call this endpoint to create and assign a certificate set to the IdP
        2. Update the IdP configuration (PUT `/identity_providers/{id}`) with:
           - `config.enable_encryption: true`
           - `saml_certificate_set_id: <uid from step 1>`
        3. Configure the certificate's public key in your external SAML Identity
           Provider

        Args:
          account_id: Identifier.

          identity_provider_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identity_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `identity_provider_id` but received {identity_provider_id!r}"
            )
        return await self._post(
            path_template(
                "/accounts/{account_id}/access/identity_providers/{identity_provider_id}/saml_certificate",
                account_id=account_id,
                identity_provider_id=identity_provider_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SAMLCertificateCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SAMLCertificateCreateResponse]], ResultWrapper[SAMLCertificateCreateResponse]),
        )


class SAMLCertificateResourceWithRawResponse:
    def __init__(self, saml_certificate: SAMLCertificateResource) -> None:
        self._saml_certificate = saml_certificate

        self.create = to_raw_response_wrapper(
            saml_certificate.create,
        )


class AsyncSAMLCertificateResourceWithRawResponse:
    def __init__(self, saml_certificate: AsyncSAMLCertificateResource) -> None:
        self._saml_certificate = saml_certificate

        self.create = async_to_raw_response_wrapper(
            saml_certificate.create,
        )


class SAMLCertificateResourceWithStreamingResponse:
    def __init__(self, saml_certificate: SAMLCertificateResource) -> None:
        self._saml_certificate = saml_certificate

        self.create = to_streamed_response_wrapper(
            saml_certificate.create,
        )


class AsyncSAMLCertificateResourceWithStreamingResponse:
    def __init__(self, saml_certificate: AsyncSAMLCertificateResource) -> None:
        self._saml_certificate = saml_certificate

        self.create = async_to_streamed_response_wrapper(
            saml_certificate.create,
        )
