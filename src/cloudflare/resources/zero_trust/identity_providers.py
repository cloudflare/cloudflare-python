# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.zero_trust import (
    IdentityProviderType,
    identity_provider_create_params,
    identity_provider_update_params,
)
from ...types.zero_trust.identity_provider import IdentityProvider
from ...types.zero_trust.scim_config_param import ScimConfigParam
from ...types.zero_trust.identity_provider_type import IdentityProviderType
from ...types.zero_trust.generic_oauth_config_param import GenericOAuthConfigParam
from ...types.zero_trust.identity_provider_list_response import IdentityProviderListResponse
from ...types.zero_trust.identity_provider_delete_response import IdentityProviderDeleteResponse

__all__ = ["IdentityProvidersResource", "AsyncIdentityProvidersResource"]


class IdentityProvidersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IdentityProvidersResourceWithRawResponse:
        return IdentityProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentityProvidersResourceWithStreamingResponse:
        return IdentityProvidersResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        config: identity_provider_create_params.AzureADConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: identity_provider_create_params.AccessCentrifyConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: identity_provider_create_params.AccessGoogleConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: identity_provider_create_params.AccessGoogleAppsConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: identity_provider_create_params.AccessOIDCConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: identity_provider_create_params.AccessOktaConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: identity_provider_create_params.AccessOneloginConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: identity_provider_create_params.AccessPingoneConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: identity_provider_create_params.AccessSAMLConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        config: object,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
    )
    def create(
        self,
        *,
        config: identity_provider_create_params.AzureADConfig
        | identity_provider_create_params.AccessCentrifyConfig
        | GenericOAuthConfigParam
        | identity_provider_create_params.AccessGoogleConfig
        | identity_provider_create_params.AccessGoogleAppsConfig
        | identity_provider_create_params.AccessOIDCConfig
        | identity_provider_create_params.AccessOktaConfig
        | identity_provider_create_params.AccessOneloginConfig
        | identity_provider_create_params.AccessPingoneConfig
        | identity_provider_create_params.AccessSAMLConfig
        | object,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            Optional[IdentityProvider],
            self._post(
                f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers",
                body=maybe_transform(
                    {
                        "config": config,
                        "name": name,
                        "type": type,
                        "scim_config": scim_config,
                    },
                    identity_provider_create_params.IdentityProviderCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[IdentityProvider]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IdentityProvider]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        uuid: str,
        *,
        config: identity_provider_update_params.AzureADConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessCentrifyConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessGoogleConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessGoogleAppsConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessOIDCConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessOktaConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessOneloginConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessPingoneConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessSAMLConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: object,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
    )
    def update(
        self,
        uuid: str,
        *,
        config: identity_provider_update_params.AzureADConfig
        | identity_provider_update_params.AccessCentrifyConfig
        | GenericOAuthConfigParam
        | identity_provider_update_params.AccessGoogleConfig
        | identity_provider_update_params.AccessGoogleAppsConfig
        | identity_provider_update_params.AccessOIDCConfig
        | identity_provider_update_params.AccessOktaConfig
        | identity_provider_update_params.AccessOneloginConfig
        | identity_provider_update_params.AccessPingoneConfig
        | identity_provider_update_params.AccessSAMLConfig
        | object,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            Optional[IdentityProvider],
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
                    post_parser=ResultWrapper[Optional[IdentityProvider]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IdentityProvider]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[IdentityProviderListResponse]:
        """
        Lists all configured identity providers.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers",
            page=SyncSinglePage[IdentityProviderListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(
                Any, IdentityProviderListResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )

    def delete(
        self,
        uuid: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProviderDeleteResponse]:
        """
        Deletes an identity provider from Access.

        Args:
          uuid: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IdentityProviderDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IdentityProviderDeleteResponse]], ResultWrapper[IdentityProviderDeleteResponse]),
        )

    def get(
        self,
        uuid: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Fetches a configured identity provider.

        Args:
          uuid: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            Optional[IdentityProvider],
            self._get(
                f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[IdentityProvider]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IdentityProvider]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncIdentityProvidersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIdentityProvidersResourceWithRawResponse:
        return AsyncIdentityProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentityProvidersResourceWithStreamingResponse:
        return AsyncIdentityProvidersResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        config: identity_provider_create_params.AzureADConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: identity_provider_create_params.AccessCentrifyConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: identity_provider_create_params.AccessGoogleConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: identity_provider_create_params.AccessGoogleAppsConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: identity_provider_create_params.AccessOIDCConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: identity_provider_create_params.AccessOktaConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: identity_provider_create_params.AccessOneloginConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: identity_provider_create_params.AccessPingoneConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: identity_provider_create_params.AccessSAMLConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        config: object,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Adds a new identity provider to Access.

        Args:
          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
    )
    async def create(
        self,
        *,
        config: identity_provider_create_params.AzureADConfig
        | identity_provider_create_params.AccessCentrifyConfig
        | GenericOAuthConfigParam
        | identity_provider_create_params.AccessGoogleConfig
        | identity_provider_create_params.AccessGoogleAppsConfig
        | identity_provider_create_params.AccessOIDCConfig
        | identity_provider_create_params.AccessOktaConfig
        | identity_provider_create_params.AccessOneloginConfig
        | identity_provider_create_params.AccessPingoneConfig
        | identity_provider_create_params.AccessSAMLConfig
        | object,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            Optional[IdentityProvider],
            await self._post(
                f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers",
                body=await async_maybe_transform(
                    {
                        "config": config,
                        "name": name,
                        "type": type,
                        "scim_config": scim_config,
                    },
                    identity_provider_create_params.IdentityProviderCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[IdentityProvider]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IdentityProvider]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        uuid: str,
        *,
        config: identity_provider_update_params.AzureADConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessCentrifyConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessGoogleConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessGoogleAppsConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessOIDCConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessOktaConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessOneloginConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessPingoneConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: identity_provider_update_params.AccessSAMLConfig,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: GenericOAuthConfigParam,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
        config: object,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Updates a configured identity provider.

        Args:
          uuid: UUID

          config: The configuration parameters for the identity provider. To view the required
              parameters for a specific provider, refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          name: The name of the identity provider, shown to users on the login page.

          type: The type of identity provider. To determine the value for a specific provider,
              refer to our
              [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          scim_config: The configuration settings for enabling a System for Cross-Domain Identity
              Management (SCIM) with the identity provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
        ["config", "name", "type"],
    )
    async def update(
        self,
        uuid: str,
        *,
        config: identity_provider_update_params.AzureADConfig
        | identity_provider_update_params.AccessCentrifyConfig
        | GenericOAuthConfigParam
        | identity_provider_update_params.AccessGoogleConfig
        | identity_provider_update_params.AccessGoogleAppsConfig
        | identity_provider_update_params.AccessOIDCConfig
        | identity_provider_update_params.AccessOktaConfig
        | identity_provider_update_params.AccessOneloginConfig
        | identity_provider_update_params.AccessPingoneConfig
        | identity_provider_update_params.AccessSAMLConfig
        | object,
        name: str,
        type: IdentityProviderType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        scim_config: ScimConfigParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            Optional[IdentityProvider],
            await self._put(
                f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}",
                body=await async_maybe_transform(
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
                    post_parser=ResultWrapper[Optional[IdentityProvider]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IdentityProvider]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[IdentityProviderListResponse, AsyncSinglePage[IdentityProviderListResponse]]:
        """
        Lists all configured identity providers.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers",
            page=AsyncSinglePage[IdentityProviderListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(
                Any, IdentityProviderListResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )

    async def delete(
        self,
        uuid: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProviderDeleteResponse]:
        """
        Deletes an identity provider from Access.

        Args:
          uuid: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IdentityProviderDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IdentityProviderDeleteResponse]], ResultWrapper[IdentityProviderDeleteResponse]),
        )

    async def get(
        self,
        uuid: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IdentityProvider]:
        """
        Fetches a configured identity provider.

        Args:
          uuid: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            Optional[IdentityProvider],
            await self._get(
                f"/{account_or_zone}/{account_or_zone_id}/access/identity_providers/{uuid}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[IdentityProvider]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IdentityProvider]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class IdentityProvidersResourceWithRawResponse:
    def __init__(self, identity_providers: IdentityProvidersResource) -> None:
        self._identity_providers = identity_providers

        self.create = to_raw_response_wrapper(
            identity_providers.create,
        )
        self.update = to_raw_response_wrapper(
            identity_providers.update,
        )
        self.list = to_raw_response_wrapper(
            identity_providers.list,
        )
        self.delete = to_raw_response_wrapper(
            identity_providers.delete,
        )
        self.get = to_raw_response_wrapper(
            identity_providers.get,
        )


class AsyncIdentityProvidersResourceWithRawResponse:
    def __init__(self, identity_providers: AsyncIdentityProvidersResource) -> None:
        self._identity_providers = identity_providers

        self.create = async_to_raw_response_wrapper(
            identity_providers.create,
        )
        self.update = async_to_raw_response_wrapper(
            identity_providers.update,
        )
        self.list = async_to_raw_response_wrapper(
            identity_providers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            identity_providers.delete,
        )
        self.get = async_to_raw_response_wrapper(
            identity_providers.get,
        )


class IdentityProvidersResourceWithStreamingResponse:
    def __init__(self, identity_providers: IdentityProvidersResource) -> None:
        self._identity_providers = identity_providers

        self.create = to_streamed_response_wrapper(
            identity_providers.create,
        )
        self.update = to_streamed_response_wrapper(
            identity_providers.update,
        )
        self.list = to_streamed_response_wrapper(
            identity_providers.list,
        )
        self.delete = to_streamed_response_wrapper(
            identity_providers.delete,
        )
        self.get = to_streamed_response_wrapper(
            identity_providers.get,
        )


class AsyncIdentityProvidersResourceWithStreamingResponse:
    def __init__(self, identity_providers: AsyncIdentityProvidersResource) -> None:
        self._identity_providers = identity_providers

        self.create = async_to_streamed_response_wrapper(
            identity_providers.create,
        )
        self.update = async_to_streamed_response_wrapper(
            identity_providers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            identity_providers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            identity_providers.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            identity_providers.get,
        )
