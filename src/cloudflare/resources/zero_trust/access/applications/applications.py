# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Type, Optional, cast, overload

import httpx

from .cas import (
    CAsResource,
    AsyncCAsResource,
    CAsResourceWithRawResponse,
    AsyncCAsResourceWithRawResponse,
    CAsResourceWithStreamingResponse,
    AsyncCAsResourceWithStreamingResponse,
)
from .policies import (
    PoliciesResource,
    AsyncPoliciesResource,
    PoliciesResourceWithRawResponse,
    AsyncPoliciesResourceWithRawResponse,
    PoliciesResourceWithStreamingResponse,
    AsyncPoliciesResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .user_policy_checks import (
    UserPolicyChecksResource,
    AsyncUserPolicyChecksResource,
    UserPolicyChecksResourceWithRawResponse,
    AsyncUserPolicyChecksResourceWithRawResponse,
    UserPolicyChecksResourceWithStreamingResponse,
    AsyncUserPolicyChecksResourceWithStreamingResponse,
)
from .....types.zero_trust.access import (
    ApplicationType,
    application_create_params,
    application_update_params,
)
from .....types.zero_trust.access.application import Application
from .....types.zero_trust.access.allowed_idps import AllowedIdPs
from .....types.zero_trust.access.app_id_param import AppIDParam
from .....types.zero_trust.access.application_type import ApplicationType
from .....types.zero_trust.access.cors_headers_param import CORSHeadersParam
from .....types.zero_trust.access.self_hosted_domains import SelfHostedDomains
from .....types.zero_trust.access.application_delete_response import ApplicationDeleteResponse

__all__ = ["ApplicationsResource", "AsyncApplicationsResource"]


class ApplicationsResource(SyncAPIResource):
    @cached_property
    def cas(self) -> CAsResource:
        return CAsResource(self._client)

    @cached_property
    def user_policy_checks(self) -> UserPolicyChecksResource:
        return UserPolicyChecksResource(self._client)

    @cached_property
    def policies(self) -> PoliciesResource:
        return PoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ApplicationsResourceWithRawResponse:
        return ApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApplicationsResourceWithStreamingResponse:
        return ApplicationsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        domain: str,
        type: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          enable_binding_cookie: Enables the binding cookie, which increases security against compromised
              authorization tokens and CSRF attacks.

          http_only_cookie_attribute: Enables the HttpOnly cookie attribute, which increases security against XSS
              attacks.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          options_preflight_bypass: Allows options preflight requests to bypass Access authentication and go
              directly to the origin. Cannot turn on if cors_headers is set.

          path_cookie_attribute: Enables cookie paths to scope an application's JWT to the application path. If
              disabled, the JWT will scope to the hostname by default

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          self_hosted_domains: List of domains that Access will secure.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        saas_app: application_create_params.SaaSApplicationSaaSApp | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_pages: The custom pages that will be displayed when applicable for this application

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          type: The application type.

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
        domain: str,
        type: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          enable_binding_cookie: Enables the binding cookie, which increases security against compromised
              authorization tokens and CSRF attacks.

          http_only_cookie_attribute: Enables the HttpOnly cookie attribute, which increases security against XSS
              attacks.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          options_preflight_bypass: Allows options preflight requests to bypass Access authentication and go
              directly to the origin. Cannot turn on if cors_headers is set.

          path_cookie_attribute: Enables cookie paths to scope an application's JWT to the application path. If
              disabled, the JWT will scope to the hostname by default

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          self_hosted_domains: List of domains that Access will secure.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

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
        domain: str,
        type: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          enable_binding_cookie: Enables the binding cookie, which increases security against compromised
              authorization tokens and CSRF attacks.

          http_only_cookie_attribute: Enables the HttpOnly cookie attribute, which increases security against XSS
              attacks.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          options_preflight_bypass: Allows options preflight requests to bypass Access authentication and go
              directly to the origin. Cannot turn on if cors_headers is set.

          path_cookie_attribute: Enables cookie paths to scope an application's JWT to the application path. If
              disabled, the JWT will scope to the hostname by default

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          self_hosted_domains: List of domains that Access will secure.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

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
        type: ApplicationType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

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
        type: ApplicationType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

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
        type: ApplicationType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        domain: str | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          app_launcher_visible: Displays the application in the App Launcher.

          domain: The URL or domain of the bookmark.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          type: The application type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def create(
        self,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        type: str | ApplicationType | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        saas_app: application_create_params.SaaSApplicationSaaSApp | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
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
            Optional[Application],
            self._post(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps",
                body=maybe_transform(
                    {
                        "domain": domain,
                        "type": type,
                        "allow_authenticate_via_warp": allow_authenticate_via_warp,
                        "allowed_idps": allowed_idps,
                        "app_launcher_visible": app_launcher_visible,
                        "auto_redirect_to_identity": auto_redirect_to_identity,
                        "cors_headers": cors_headers,
                        "custom_deny_message": custom_deny_message,
                        "custom_deny_url": custom_deny_url,
                        "custom_non_identity_deny_url": custom_non_identity_deny_url,
                        "custom_pages": custom_pages,
                        "enable_binding_cookie": enable_binding_cookie,
                        "http_only_cookie_attribute": http_only_cookie_attribute,
                        "logo_url": logo_url,
                        "name": name,
                        "options_preflight_bypass": options_preflight_bypass,
                        "path_cookie_attribute": path_cookie_attribute,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "saas_app": saas_app,
                    },
                    application_create_params.ApplicationCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Application]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Application]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        app_id: AppIDParam,
        *,
        domain: str,
        type: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          enable_binding_cookie: Enables the binding cookie, which increases security against compromised
              authorization tokens and CSRF attacks.

          http_only_cookie_attribute: Enables the HttpOnly cookie attribute, which increases security against XSS
              attacks.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          options_preflight_bypass: Allows options preflight requests to bypass Access authentication and go
              directly to the origin. Cannot turn on if cors_headers is set.

          path_cookie_attribute: Enables cookie paths to scope an application's JWT to the application path. If
              disabled, the JWT will scope to the hostname by default

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          self_hosted_domains: List of domains that Access will secure.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_id: AppIDParam,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        saas_app: application_update_params.SaaSApplicationSaaSApp | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_pages: The custom pages that will be displayed when applicable for this application

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          type: The application type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_id: AppIDParam,
        *,
        domain: str,
        type: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          enable_binding_cookie: Enables the binding cookie, which increases security against compromised
              authorization tokens and CSRF attacks.

          http_only_cookie_attribute: Enables the HttpOnly cookie attribute, which increases security against XSS
              attacks.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          options_preflight_bypass: Allows options preflight requests to bypass Access authentication and go
              directly to the origin. Cannot turn on if cors_headers is set.

          path_cookie_attribute: Enables cookie paths to scope an application's JWT to the application path. If
              disabled, the JWT will scope to the hostname by default

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          self_hosted_domains: List of domains that Access will secure.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_id: AppIDParam,
        *,
        domain: str,
        type: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          enable_binding_cookie: Enables the binding cookie, which increases security against compromised
              authorization tokens and CSRF attacks.

          http_only_cookie_attribute: Enables the HttpOnly cookie attribute, which increases security against XSS
              attacks.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          options_preflight_bypass: Allows options preflight requests to bypass Access authentication and go
              directly to the origin. Cannot turn on if cors_headers is set.

          path_cookie_attribute: Enables cookie paths to scope an application's JWT to the application path. If
              disabled, the JWT will scope to the hostname by default

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          self_hosted_domains: List of domains that Access will secure.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_id: AppIDParam,
        *,
        type: ApplicationType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_id: AppIDParam,
        *,
        type: ApplicationType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_id: AppIDParam,
        *,
        type: ApplicationType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_id: AppIDParam,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        domain: str | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          app_launcher_visible: Displays the application in the App Launcher.

          domain: The URL or domain of the bookmark.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          type: The application type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def update(
        self,
        app_id: AppIDParam,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        type: str | ApplicationType | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        saas_app: application_update_params.SaaSApplicationSaaSApp | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
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
            Optional[Application],
            self._put(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
                body=maybe_transform(
                    {
                        "domain": domain,
                        "type": type,
                        "allow_authenticate_via_warp": allow_authenticate_via_warp,
                        "allowed_idps": allowed_idps,
                        "app_launcher_visible": app_launcher_visible,
                        "auto_redirect_to_identity": auto_redirect_to_identity,
                        "cors_headers": cors_headers,
                        "custom_deny_message": custom_deny_message,
                        "custom_deny_url": custom_deny_url,
                        "custom_non_identity_deny_url": custom_non_identity_deny_url,
                        "custom_pages": custom_pages,
                        "enable_binding_cookie": enable_binding_cookie,
                        "http_only_cookie_attribute": http_only_cookie_attribute,
                        "logo_url": logo_url,
                        "name": name,
                        "options_preflight_bypass": options_preflight_bypass,
                        "path_cookie_attribute": path_cookie_attribute,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "saas_app": saas_app,
                    },
                    application_update_params.ApplicationUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Application]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Application]
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
    ) -> SyncSinglePage[Application]:
        """
        Lists all Access applications in an account or zone.

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
            f"/{account_or_zone}/{account_or_zone_id}/access/apps",
            page=SyncSinglePage[Application],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, Application),  # Union types cannot be passed in as arguments in the type system
        )

    def delete(
        self,
        app_id: AppIDParam,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ApplicationDeleteResponse]:
        """
        Deletes an application from Access.

        Args:
          app_id: Identifier

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
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ApplicationDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ApplicationDeleteResponse]], ResultWrapper[ApplicationDeleteResponse]),
        )

    def get(
        self,
        app_id: AppIDParam,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Fetches information about an Access application.

        Args:
          app_id: Identifier

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
        return cast(
            Optional[Application],
            self._get(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Application]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Application]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def revoke_tokens(
        self,
        app_id: AppIDParam,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Revokes all tokens issued for an application.

        Args:
          app_id: Identifier

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
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/revoke_tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncApplicationsResource(AsyncAPIResource):
    @cached_property
    def cas(self) -> AsyncCAsResource:
        return AsyncCAsResource(self._client)

    @cached_property
    def user_policy_checks(self) -> AsyncUserPolicyChecksResource:
        return AsyncUserPolicyChecksResource(self._client)

    @cached_property
    def policies(self) -> AsyncPoliciesResource:
        return AsyncPoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncApplicationsResourceWithRawResponse:
        return AsyncApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApplicationsResourceWithStreamingResponse:
        return AsyncApplicationsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        domain: str,
        type: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          enable_binding_cookie: Enables the binding cookie, which increases security against compromised
              authorization tokens and CSRF attacks.

          http_only_cookie_attribute: Enables the HttpOnly cookie attribute, which increases security against XSS
              attacks.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          options_preflight_bypass: Allows options preflight requests to bypass Access authentication and go
              directly to the origin. Cannot turn on if cors_headers is set.

          path_cookie_attribute: Enables cookie paths to scope an application's JWT to the application path. If
              disabled, the JWT will scope to the hostname by default

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          self_hosted_domains: List of domains that Access will secure.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        saas_app: application_create_params.SaaSApplicationSaaSApp | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_pages: The custom pages that will be displayed when applicable for this application

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          type: The application type.

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
        domain: str,
        type: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          enable_binding_cookie: Enables the binding cookie, which increases security against compromised
              authorization tokens and CSRF attacks.

          http_only_cookie_attribute: Enables the HttpOnly cookie attribute, which increases security against XSS
              attacks.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          options_preflight_bypass: Allows options preflight requests to bypass Access authentication and go
              directly to the origin. Cannot turn on if cors_headers is set.

          path_cookie_attribute: Enables cookie paths to scope an application's JWT to the application path. If
              disabled, the JWT will scope to the hostname by default

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          self_hosted_domains: List of domains that Access will secure.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

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
        domain: str,
        type: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          enable_binding_cookie: Enables the binding cookie, which increases security against compromised
              authorization tokens and CSRF attacks.

          http_only_cookie_attribute: Enables the HttpOnly cookie attribute, which increases security against XSS
              attacks.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          options_preflight_bypass: Allows options preflight requests to bypass Access authentication and go
              directly to the origin. Cannot turn on if cors_headers is set.

          path_cookie_attribute: Enables cookie paths to scope an application's JWT to the application path. If
              disabled, the JWT will scope to the hostname by default

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          self_hosted_domains: List of domains that Access will secure.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

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
        type: ApplicationType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

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
        type: ApplicationType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

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
        type: ApplicationType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        domain: str | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Adds a new application to Access.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          app_launcher_visible: Displays the application in the App Launcher.

          domain: The URL or domain of the bookmark.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          type: The application type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def create(
        self,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        type: str | ApplicationType | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        saas_app: application_create_params.SaaSApplicationSaaSApp | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
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
            Optional[Application],
            await self._post(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps",
                body=await async_maybe_transform(
                    {
                        "domain": domain,
                        "type": type,
                        "allow_authenticate_via_warp": allow_authenticate_via_warp,
                        "allowed_idps": allowed_idps,
                        "app_launcher_visible": app_launcher_visible,
                        "auto_redirect_to_identity": auto_redirect_to_identity,
                        "cors_headers": cors_headers,
                        "custom_deny_message": custom_deny_message,
                        "custom_deny_url": custom_deny_url,
                        "custom_non_identity_deny_url": custom_non_identity_deny_url,
                        "custom_pages": custom_pages,
                        "enable_binding_cookie": enable_binding_cookie,
                        "http_only_cookie_attribute": http_only_cookie_attribute,
                        "logo_url": logo_url,
                        "name": name,
                        "options_preflight_bypass": options_preflight_bypass,
                        "path_cookie_attribute": path_cookie_attribute,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "saas_app": saas_app,
                    },
                    application_create_params.ApplicationCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Application]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Application]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        app_id: AppIDParam,
        *,
        domain: str,
        type: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          enable_binding_cookie: Enables the binding cookie, which increases security against compromised
              authorization tokens and CSRF attacks.

          http_only_cookie_attribute: Enables the HttpOnly cookie attribute, which increases security against XSS
              attacks.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          options_preflight_bypass: Allows options preflight requests to bypass Access authentication and go
              directly to the origin. Cannot turn on if cors_headers is set.

          path_cookie_attribute: Enables cookie paths to scope an application's JWT to the application path. If
              disabled, the JWT will scope to the hostname by default

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          self_hosted_domains: List of domains that Access will secure.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_id: AppIDParam,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        saas_app: application_update_params.SaaSApplicationSaaSApp | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_pages: The custom pages that will be displayed when applicable for this application

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          type: The application type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_id: AppIDParam,
        *,
        domain: str,
        type: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          enable_binding_cookie: Enables the binding cookie, which increases security against compromised
              authorization tokens and CSRF attacks.

          http_only_cookie_attribute: Enables the HttpOnly cookie attribute, which increases security against XSS
              attacks.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          options_preflight_bypass: Allows options preflight requests to bypass Access authentication and go
              directly to the origin. Cannot turn on if cors_headers is set.

          path_cookie_attribute: Enables cookie paths to scope an application's JWT to the application path. If
              disabled, the JWT will scope to the hostname by default

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          self_hosted_domains: List of domains that Access will secure.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_id: AppIDParam,
        *,
        domain: str,
        type: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_visible: Displays the application in the App Launcher.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          enable_binding_cookie: Enables the binding cookie, which increases security against compromised
              authorization tokens and CSRF attacks.

          http_only_cookie_attribute: Enables the HttpOnly cookie attribute, which increases security against XSS
              attacks.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          options_preflight_bypass: Allows options preflight requests to bypass Access authentication and go
              directly to the origin. Cannot turn on if cors_headers is set.

          path_cookie_attribute: Enables cookie paths to scope an application's JWT to the application path. If
              disabled, the JWT will scope to the hostname by default

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          self_hosted_domains: List of domains that Access will secure.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_id: AppIDParam,
        *,
        type: ApplicationType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_id: AppIDParam,
        *,
        type: ApplicationType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_id: AppIDParam,
        *,
        type: ApplicationType,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_id: AppIDParam,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        domain: str | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          app_launcher_visible: Displays the application in the App Launcher.

          domain: The URL or domain of the bookmark.

          logo_url: The image URL for the logo shown in the App Launcher dashboard.

          name: The name of the application.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          type: The application type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def update(
        self,
        app_id: AppIDParam,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        type: str | ApplicationType | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[AllowedIdPs] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: CORSHeadersParam | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        options_preflight_bypass: bool | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[SelfHostedDomains] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        saas_app: application_update_params.SaaSApplicationSaaSApp | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
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
            Optional[Application],
            await self._put(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
                body=await async_maybe_transform(
                    {
                        "domain": domain,
                        "type": type,
                        "allow_authenticate_via_warp": allow_authenticate_via_warp,
                        "allowed_idps": allowed_idps,
                        "app_launcher_visible": app_launcher_visible,
                        "auto_redirect_to_identity": auto_redirect_to_identity,
                        "cors_headers": cors_headers,
                        "custom_deny_message": custom_deny_message,
                        "custom_deny_url": custom_deny_url,
                        "custom_non_identity_deny_url": custom_non_identity_deny_url,
                        "custom_pages": custom_pages,
                        "enable_binding_cookie": enable_binding_cookie,
                        "http_only_cookie_attribute": http_only_cookie_attribute,
                        "logo_url": logo_url,
                        "name": name,
                        "options_preflight_bypass": options_preflight_bypass,
                        "path_cookie_attribute": path_cookie_attribute,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "saas_app": saas_app,
                    },
                    application_update_params.ApplicationUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Application]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Application]
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
    ) -> AsyncPaginator[Application, AsyncSinglePage[Application]]:
        """
        Lists all Access applications in an account or zone.

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
            f"/{account_or_zone}/{account_or_zone_id}/access/apps",
            page=AsyncSinglePage[Application],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, Application),  # Union types cannot be passed in as arguments in the type system
        )

    async def delete(
        self,
        app_id: AppIDParam,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ApplicationDeleteResponse]:
        """
        Deletes an application from Access.

        Args:
          app_id: Identifier

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
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ApplicationDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ApplicationDeleteResponse]], ResultWrapper[ApplicationDeleteResponse]),
        )

    async def get(
        self,
        app_id: AppIDParam,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Application]:
        """
        Fetches information about an Access application.

        Args:
          app_id: Identifier

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
        return cast(
            Optional[Application],
            await self._get(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Application]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Application]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def revoke_tokens(
        self,
        app_id: AppIDParam,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Revokes all tokens issued for an application.

        Args:
          app_id: Identifier

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
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/revoke_tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class ApplicationsResourceWithRawResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.create = to_raw_response_wrapper(
            applications.create,
        )
        self.update = to_raw_response_wrapper(
            applications.update,
        )
        self.list = to_raw_response_wrapper(
            applications.list,
        )
        self.delete = to_raw_response_wrapper(
            applications.delete,
        )
        self.get = to_raw_response_wrapper(
            applications.get,
        )
        self.revoke_tokens = to_raw_response_wrapper(
            applications.revoke_tokens,
        )

    @cached_property
    def cas(self) -> CAsResourceWithRawResponse:
        return CAsResourceWithRawResponse(self._applications.cas)

    @cached_property
    def user_policy_checks(self) -> UserPolicyChecksResourceWithRawResponse:
        return UserPolicyChecksResourceWithRawResponse(self._applications.user_policy_checks)

    @cached_property
    def policies(self) -> PoliciesResourceWithRawResponse:
        return PoliciesResourceWithRawResponse(self._applications.policies)


class AsyncApplicationsResourceWithRawResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.create = async_to_raw_response_wrapper(
            applications.create,
        )
        self.update = async_to_raw_response_wrapper(
            applications.update,
        )
        self.list = async_to_raw_response_wrapper(
            applications.list,
        )
        self.delete = async_to_raw_response_wrapper(
            applications.delete,
        )
        self.get = async_to_raw_response_wrapper(
            applications.get,
        )
        self.revoke_tokens = async_to_raw_response_wrapper(
            applications.revoke_tokens,
        )

    @cached_property
    def cas(self) -> AsyncCAsResourceWithRawResponse:
        return AsyncCAsResourceWithRawResponse(self._applications.cas)

    @cached_property
    def user_policy_checks(self) -> AsyncUserPolicyChecksResourceWithRawResponse:
        return AsyncUserPolicyChecksResourceWithRawResponse(self._applications.user_policy_checks)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithRawResponse:
        return AsyncPoliciesResourceWithRawResponse(self._applications.policies)


class ApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.create = to_streamed_response_wrapper(
            applications.create,
        )
        self.update = to_streamed_response_wrapper(
            applications.update,
        )
        self.list = to_streamed_response_wrapper(
            applications.list,
        )
        self.delete = to_streamed_response_wrapper(
            applications.delete,
        )
        self.get = to_streamed_response_wrapper(
            applications.get,
        )
        self.revoke_tokens = to_streamed_response_wrapper(
            applications.revoke_tokens,
        )

    @cached_property
    def cas(self) -> CAsResourceWithStreamingResponse:
        return CAsResourceWithStreamingResponse(self._applications.cas)

    @cached_property
    def user_policy_checks(self) -> UserPolicyChecksResourceWithStreamingResponse:
        return UserPolicyChecksResourceWithStreamingResponse(self._applications.user_policy_checks)

    @cached_property
    def policies(self) -> PoliciesResourceWithStreamingResponse:
        return PoliciesResourceWithStreamingResponse(self._applications.policies)


class AsyncApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.create = async_to_streamed_response_wrapper(
            applications.create,
        )
        self.update = async_to_streamed_response_wrapper(
            applications.update,
        )
        self.list = async_to_streamed_response_wrapper(
            applications.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            applications.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            applications.get,
        )
        self.revoke_tokens = async_to_streamed_response_wrapper(
            applications.revoke_tokens,
        )

    @cached_property
    def cas(self) -> AsyncCAsResourceWithStreamingResponse:
        return AsyncCAsResourceWithStreamingResponse(self._applications.cas)

    @cached_property
    def user_policy_checks(self) -> AsyncUserPolicyChecksResourceWithStreamingResponse:
        return AsyncUserPolicyChecksResourceWithStreamingResponse(self._applications.user_policy_checks)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        return AsyncPoliciesResourceWithStreamingResponse(self._applications.policies)
