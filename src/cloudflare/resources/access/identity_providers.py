# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, Optional, cast, overload
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import required_args, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.access import (
    IdentityProviderGetResponse,
    IdentityProviderDeleteResponse,
    IdentityProviderUpdateResponse,
    IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse,
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponse,
    identity_provider_update_params,
    identity_provider_access_identity_providers_add_an_access_identity_provider_params,
)

__all__ = ["IdentityProviders", "AsyncIdentityProviders"]


class IdentityProviders(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IdentityProvidersWithRawResponse:
        return IdentityProvidersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentityProvidersWithStreamingResponse:
        return IdentityProvidersWithStreamingResponse(self)

    @overload
    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessAzureAdConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessAzureAdScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessCentrifyConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessCentrifyScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessFacebookConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessFacebookScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessGitHubConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessGitHubScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessGoogleConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessGoogleScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessGoogleAppsConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessGoogleAppsScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessLinkedinConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessLinkedinScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessOidcConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessOidcScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessOktaConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessOktaScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessOneloginConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessOneloginScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessPingoneConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessPingoneScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessSamlConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessSamlScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessYandexConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessYandexScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: object,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessOnetimepinScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
    )
    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessAzureAdConfig
        | identity_provider_update_params.AccessCentrifyConfig
        | identity_provider_update_params.AccessFacebookConfig
        | identity_provider_update_params.AccessGoogleConfig
        | identity_provider_update_params.AccessGoogleAppsConfig
        | identity_provider_update_params.AccessOidcConfig
        | identity_provider_update_params.AccessOktaConfig
        | identity_provider_update_params.AccessOneloginConfig
        | identity_provider_update_params.AccessPingoneConfig
        | identity_provider_update_params.AccessSamlConfig
        | object,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessAzureAdScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return cast(
            IdentityProviderUpdateResponse,
            self._put(
                f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}",
                body=maybe_transform(
                    {
                        "config": config,
                        "name": name,
                        "type": type,
                        "scim_config": scim_config,
                    },
                    identity_provider_update_params.IdentityProviderUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IdentityProviderUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderDeleteResponse:
        """
        Deletes an identity provider from Access.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IdentityProviderDeleteResponse], ResultWrapper[IdentityProviderDeleteResponse]),
        )

    @overload
    def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessAzureAdConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessAzureAdScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessCentrifyConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessCentrifyScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessFacebookConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessFacebookScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGitHubConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGitHubScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGoogleConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGoogleScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGoogleAppsConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGoogleAppsScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessLinkedinConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessLinkedinScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOidcConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOidcScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOktaConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOktaScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOneloginConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOneloginScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessPingoneConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessPingoneScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessSamlConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessSamlScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessYandexConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessYandexScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: object,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOnetimepinScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
    )
    def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessAzureAdConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessCentrifyConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessFacebookConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGoogleConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGoogleAppsConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOidcConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOktaConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOneloginConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessPingoneConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessSamlConfig
        | object,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessAzureAdScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return cast(
            IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse,
            self._post(
                f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers",
                body=maybe_transform(
                    {
                        "config": config,
                        "name": name,
                        "type": type,
                        "scim_config": scim_config,
                    },
                    identity_provider_access_identity_providers_add_an_access_identity_provider_params.IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def access_identity_providers_list_access_identity_providers(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponse]:
        """
        Lists all configured identity providers.

        Args:
          account_or_zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponse]],
                ResultWrapper[IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponse],
            ),
        )

    def get(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderGetResponse:
        """
        Fetches a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return cast(
            IdentityProviderGetResponse,
            self._get(
                f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IdentityProviderGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncIdentityProviders(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIdentityProvidersWithRawResponse:
        return AsyncIdentityProvidersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentityProvidersWithStreamingResponse:
        return AsyncIdentityProvidersWithStreamingResponse(self)

    @overload
    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessAzureAdConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessAzureAdScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessCentrifyConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessCentrifyScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessFacebookConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessFacebookScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessGitHubConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessGitHubScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessGoogleConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessGoogleScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessGoogleAppsConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessGoogleAppsScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessLinkedinConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessLinkedinScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessOidcConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessOidcScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessOktaConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessOktaScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessOneloginConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessOneloginScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessPingoneConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessPingoneScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessSamlConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessSamlScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessYandexConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessYandexScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: object,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessOnetimepinScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        """
        Updates a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
        ["account_or_zone", "account_or_zone_id", "config", "name", "type"],
    )
    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        config: identity_provider_update_params.AccessAzureAdConfig
        | identity_provider_update_params.AccessCentrifyConfig
        | identity_provider_update_params.AccessFacebookConfig
        | identity_provider_update_params.AccessGoogleConfig
        | identity_provider_update_params.AccessGoogleAppsConfig
        | identity_provider_update_params.AccessOidcConfig
        | identity_provider_update_params.AccessOktaConfig
        | identity_provider_update_params.AccessOneloginConfig
        | identity_provider_update_params.AccessPingoneConfig
        | identity_provider_update_params.AccessSamlConfig
        | object,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_update_params.AccessAzureAdScimConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderUpdateResponse:
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return cast(
            IdentityProviderUpdateResponse,
            await self._put(
                f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}",
                body=maybe_transform(
                    {
                        "config": config,
                        "name": name,
                        "type": type,
                        "scim_config": scim_config,
                    },
                    identity_provider_update_params.IdentityProviderUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IdentityProviderUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderDeleteResponse:
        """
        Deletes an identity provider from Access.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IdentityProviderDeleteResponse], ResultWrapper[IdentityProviderDeleteResponse]),
        )

    @overload
    async def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessAzureAdConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessAzureAdScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessCentrifyConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessCentrifyScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessFacebookConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessFacebookScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGitHubConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGitHubScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGoogleConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGoogleScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGoogleAppsConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGoogleAppsScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessLinkedinConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessLinkedinScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOidcConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOidcScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOktaConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOktaScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOneloginConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOneloginScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessPingoneConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessPingoneScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessSamlConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessSamlScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessYandexConfig,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessYandexScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: object,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOnetimepinScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        """
        Adds a new identity provider to Access.

        Args:
          account_or_zone_id: Identifier

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
        ["account_or_zone", "config", "name", "type"],
    )
    async def access_identity_providers_add_an_access_identity_provider(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessAzureAdConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessCentrifyConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessFacebookConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGoogleConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessGoogleAppsConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOidcConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOktaConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessOneloginConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessPingoneConfig
        | identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessSamlConfig
        | object,
        name: str,
        type: Literal[
            "onetimepin",
            "azureAD",
            "saml",
            "centrify",
            "facebook",
            "github",
            "google-apps",
            "google",
            "linkedin",
            "oidc",
            "okta",
            "onelogin",
            "pingone",
            "yandex",
        ],
        scim_config: identity_provider_access_identity_providers_add_an_access_identity_provider_params.AccessAzureAdScimConfig
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse:
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return cast(
            IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse,
            await self._post(
                f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers",
                body=maybe_transform(
                    {
                        "config": config,
                        "name": name,
                        "type": type,
                        "scim_config": scim_config,
                    },
                    identity_provider_access_identity_providers_add_an_access_identity_provider_params.IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IdentityProviderAccessIdentityProvidersAddAnAccessIdentityProviderResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def access_identity_providers_list_access_identity_providers(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponse]:
        """
        Lists all configured identity providers.

        Args:
          account_or_zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponse]],
                ResultWrapper[IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponse],
            ),
        )

    async def get(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityProviderGetResponse:
        """
        Fetches a configured identity provider.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return cast(
            IdentityProviderGetResponse,
            await self._get(
                f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IdentityProviderGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class IdentityProvidersWithRawResponse:
    def __init__(self, identity_providers: IdentityProviders) -> None:
        self._identity_providers = identity_providers

        self.update = to_raw_response_wrapper(
            identity_providers.update,
        )
        self.delete = to_raw_response_wrapper(
            identity_providers.delete,
        )
        self.access_identity_providers_add_an_access_identity_provider = to_raw_response_wrapper(
            identity_providers.access_identity_providers_add_an_access_identity_provider,
        )
        self.access_identity_providers_list_access_identity_providers = to_raw_response_wrapper(
            identity_providers.access_identity_providers_list_access_identity_providers,
        )
        self.get = to_raw_response_wrapper(
            identity_providers.get,
        )


class AsyncIdentityProvidersWithRawResponse:
    def __init__(self, identity_providers: AsyncIdentityProviders) -> None:
        self._identity_providers = identity_providers

        self.update = async_to_raw_response_wrapper(
            identity_providers.update,
        )
        self.delete = async_to_raw_response_wrapper(
            identity_providers.delete,
        )
        self.access_identity_providers_add_an_access_identity_provider = async_to_raw_response_wrapper(
            identity_providers.access_identity_providers_add_an_access_identity_provider,
        )
        self.access_identity_providers_list_access_identity_providers = async_to_raw_response_wrapper(
            identity_providers.access_identity_providers_list_access_identity_providers,
        )
        self.get = async_to_raw_response_wrapper(
            identity_providers.get,
        )


class IdentityProvidersWithStreamingResponse:
    def __init__(self, identity_providers: IdentityProviders) -> None:
        self._identity_providers = identity_providers

        self.update = to_streamed_response_wrapper(
            identity_providers.update,
        )
        self.delete = to_streamed_response_wrapper(
            identity_providers.delete,
        )
        self.access_identity_providers_add_an_access_identity_provider = to_streamed_response_wrapper(
            identity_providers.access_identity_providers_add_an_access_identity_provider,
        )
        self.access_identity_providers_list_access_identity_providers = to_streamed_response_wrapper(
            identity_providers.access_identity_providers_list_access_identity_providers,
        )
        self.get = to_streamed_response_wrapper(
            identity_providers.get,
        )


class AsyncIdentityProvidersWithStreamingResponse:
    def __init__(self, identity_providers: AsyncIdentityProviders) -> None:
        self._identity_providers = identity_providers

        self.update = async_to_streamed_response_wrapper(
            identity_providers.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            identity_providers.delete,
        )
        self.access_identity_providers_add_an_access_identity_provider = async_to_streamed_response_wrapper(
            identity_providers.access_identity_providers_add_an_access_identity_provider,
        )
        self.access_identity_providers_list_access_identity_providers = async_to_streamed_response_wrapper(
            identity_providers.access_identity_providers_list_access_identity_providers,
        )
        self.get = async_to_streamed_response_wrapper(
            identity_providers.get,
        )
