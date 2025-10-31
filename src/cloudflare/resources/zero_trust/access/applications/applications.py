# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Iterable, Optional, cast
from typing_extensions import Literal, overload

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
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .user_policy_checks import (
    UserPolicyChecksResource,
    AsyncUserPolicyChecksResource,
    UserPolicyChecksResourceWithRawResponse,
    AsyncUserPolicyChecksResourceWithRawResponse,
    UserPolicyChecksResourceWithStreamingResponse,
    AsyncUserPolicyChecksResourceWithStreamingResponse,
)
from .policy_tests.policy_tests import (
    PolicyTestsResource,
    AsyncPolicyTestsResource,
    PolicyTestsResourceWithRawResponse,
    AsyncPolicyTestsResourceWithRawResponse,
    PolicyTestsResourceWithStreamingResponse,
    AsyncPolicyTestsResourceWithStreamingResponse,
)
from .....types.zero_trust.access import (
    AppID,
    ApplicationType,
    application_list_params,
    application_create_params,
    application_update_params,
)
from .....types.zero_trust.access.app_id import AppID
from .....types.zero_trust.access.allowed_idps import AllowedIdPs
from .....types.zero_trust.access.application_type import ApplicationType
from .....types.zero_trust.access.cors_headers_param import CORSHeadersParam
from .....types.zero_trust.access.self_hosted_domains import SelfHostedDomains
from .....types.zero_trust.access.application_get_response import ApplicationGetResponse
from .....types.zero_trust.access.application_list_response import ApplicationListResponse
from .....types.zero_trust.access.application_create_response import ApplicationCreateResponse
from .....types.zero_trust.access.application_delete_response import ApplicationDeleteResponse
from .....types.zero_trust.access.application_update_response import ApplicationUpdateResponse

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
    def policy_tests(self) -> PolicyTestsResource:
        return PolicyTestsResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ApplicationsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        domain: str,
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_create_params.SelfHostedApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_create_params.SelfHostedApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_create_params.SelfHostedApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Adds a new application to Access.

        Args:
          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        policies: SequenceNotStr[application_create_params.SaaSApplicationPolicy] | Omit = omit,
        saas_app: application_create_params.SaaSApplicationSaaSApp | Omit = omit,
        scim_config: application_create_params.SaaSApplicationSCIMConfig | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        type: ApplicationType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

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
        type: Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ],
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_create_params.BrowserSSHApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_create_params.BrowserSSHApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_create_params.BrowserSSHApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Adds a new application to Access.

        Args:
          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        type: Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ],
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_create_params.BrowserVNCApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_create_params.BrowserVNCApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_create_params.BrowserVNCApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Adds a new application to Access.

        Args:
          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        type: Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ],
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_logo_url: str | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        bg_color: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        footer_links: Iterable[application_create_params.AppLauncherApplicationFooterLink] | Omit = omit,
        header_bg_color: str | Omit = omit,
        landing_page_design: application_create_params.AppLauncherApplicationLandingPageDesign | Omit = omit,
        policies: SequenceNotStr[application_create_params.AppLauncherApplicationPolicy] | Omit = omit,
        session_duration: str | Omit = omit,
        skip_app_launcher_login_page: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Adds a new application to Access.

        Args:
          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_logo_url: The image URL of the logo shown in the App Launcher header.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          bg_color: The background color of the App Launcher page.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          footer_links: The links in the App Launcher footer.

          header_bg_color: The background color of the App Launcher header.

          landing_page_design: The design of the App Launcher landing page shown to users when they log in.

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

          skip_app_launcher_login_page: Determines when to skip the App Launcher landing page.

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
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        policies: SequenceNotStr[application_create_params.DeviceEnrollmentPermissionsApplicationPolicy] | Omit = omit,
        session_duration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
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

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        policies: SequenceNotStr[application_create_params.BrowserIsolationPermissionsApplicationPolicy] | Omit = omit,
        session_duration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
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

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        domain: str | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        type: ApplicationType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
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

    @overload
    def create(
        self,
        *,
        target_criteria: Iterable[application_create_params.InfrastructureApplicationTargetCriterion],
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        name: str | Omit = omit,
        policies: Iterable[application_create_params.InfrastructureApplicationPolicy] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Adds a new application to Access.

        Args:
          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          name: The name of the application.

          policies: The policies that Access applies to the application.

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
        target_criteria: Iterable[application_create_params.BrowserRdpApplicationTargetCriterion],
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_create_params.BrowserRdpApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_create_params.BrowserRdpApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_create_params.BrowserRdpApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Adds a new application to Access.

        Args:
          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def create(
        self,
        *,
        domain: str | Omit = omit,
        type: ApplicationType
        | Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ]
        | Omit = omit,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_create_params.SelfHostedApplicationDestination]
        | Iterable[application_create_params.BrowserSSHApplicationDestination]
        | Iterable[application_create_params.BrowserVNCApplicationDestination]
        | Iterable[application_create_params.BrowserRdpApplicationDestination]
        | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_create_params.SelfHostedApplicationPolicy]
        | SequenceNotStr[application_create_params.SaaSApplicationPolicy]
        | SequenceNotStr[application_create_params.BrowserSSHApplicationPolicy]
        | SequenceNotStr[application_create_params.BrowserVNCApplicationPolicy]
        | SequenceNotStr[application_create_params.AppLauncherApplicationPolicy]
        | SequenceNotStr[application_create_params.DeviceEnrollmentPermissionsApplicationPolicy]
        | SequenceNotStr[application_create_params.BrowserIsolationPermissionsApplicationPolicy]
        | Iterable[application_create_params.InfrastructureApplicationPolicy]
        | SequenceNotStr[application_create_params.BrowserRdpApplicationPolicy]
        | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_create_params.SelfHostedApplicationSCIMConfig
        | application_create_params.SaaSApplicationSCIMConfig
        | application_create_params.BrowserSSHApplicationSCIMConfig
        | application_create_params.BrowserVNCApplicationSCIMConfig
        | application_create_params.BrowserRdpApplicationSCIMConfig
        | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        saas_app: application_create_params.SaaSApplicationSaaSApp | Omit = omit,
        app_launcher_logo_url: str | Omit = omit,
        bg_color: str | Omit = omit,
        footer_links: Iterable[application_create_params.AppLauncherApplicationFooterLink] | Omit = omit,
        header_bg_color: str | Omit = omit,
        landing_page_design: application_create_params.AppLauncherApplicationLandingPageDesign | Omit = omit,
        skip_app_launcher_login_page: bool | Omit = omit,
        target_criteria: Iterable[application_create_params.InfrastructureApplicationTargetCriterion]
        | Iterable[application_create_params.BrowserRdpApplicationTargetCriterion]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
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
            Optional[ApplicationCreateResponse],
            self._post(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps",
                body=maybe_transform(
                    {
                        "domain": domain,
                        "type": type,
                        "allow_authenticate_via_warp": allow_authenticate_via_warp,
                        "allow_iframe": allow_iframe,
                        "allowed_idps": allowed_idps,
                        "app_launcher_visible": app_launcher_visible,
                        "auto_redirect_to_identity": auto_redirect_to_identity,
                        "cors_headers": cors_headers,
                        "custom_deny_message": custom_deny_message,
                        "custom_deny_url": custom_deny_url,
                        "custom_non_identity_deny_url": custom_non_identity_deny_url,
                        "custom_pages": custom_pages,
                        "destinations": destinations,
                        "enable_binding_cookie": enable_binding_cookie,
                        "http_only_cookie_attribute": http_only_cookie_attribute,
                        "logo_url": logo_url,
                        "name": name,
                        "options_preflight_bypass": options_preflight_bypass,
                        "path_cookie_attribute": path_cookie_attribute,
                        "policies": policies,
                        "read_service_tokens_from_header": read_service_tokens_from_header,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "scim_config": scim_config,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "saas_app": saas_app,
                        "app_launcher_logo_url": app_launcher_logo_url,
                        "bg_color": bg_color,
                        "footer_links": footer_links,
                        "header_bg_color": header_bg_color,
                        "landing_page_design": landing_page_design,
                        "skip_app_launcher_login_page": skip_app_launcher_login_page,
                        "target_criteria": target_criteria,
                    },
                    application_create_params.ApplicationCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[ApplicationCreateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ApplicationCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        app_id: AppID,
        *,
        domain: str,
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_update_params.SelfHostedApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_update_params.SelfHostedApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_update_params.SelfHostedApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        app_id: AppID,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        policies: SequenceNotStr[application_update_params.SaaSApplicationPolicy] | Omit = omit,
        saas_app: application_update_params.SaaSApplicationSaaSApp | Omit = omit,
        scim_config: application_update_params.SaaSApplicationSCIMConfig | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        type: ApplicationType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

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
        app_id: AppID,
        *,
        domain: str,
        type: Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ],
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_update_params.BrowserSSHApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_update_params.BrowserSSHApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_update_params.BrowserSSHApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        app_id: AppID,
        *,
        domain: str,
        type: Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ],
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_update_params.BrowserVNCApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_update_params.BrowserVNCApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_update_params.BrowserVNCApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        app_id: AppID,
        *,
        type: Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ],
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_logo_url: str | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        bg_color: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        footer_links: Iterable[application_update_params.AppLauncherApplicationFooterLink] | Omit = omit,
        header_bg_color: str | Omit = omit,
        landing_page_design: application_update_params.AppLauncherApplicationLandingPageDesign | Omit = omit,
        policies: SequenceNotStr[application_update_params.AppLauncherApplicationPolicy] | Omit = omit,
        session_duration: str | Omit = omit,
        skip_app_launcher_login_page: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_logo_url: The image URL of the logo shown in the App Launcher header.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          bg_color: The background color of the App Launcher page.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          footer_links: The links in the App Launcher footer.

          header_bg_color: The background color of the App Launcher header.

          landing_page_design: The design of the App Launcher landing page shown to users when they log in.

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

          skip_app_launcher_login_page: Determines when to skip the App Launcher landing page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_id: AppID,
        *,
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        policies: SequenceNotStr[application_update_params.DeviceEnrollmentPermissionsApplicationPolicy] | Omit = omit,
        session_duration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_id: AppID,
        *,
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        policies: SequenceNotStr[application_update_params.BrowserIsolationPermissionsApplicationPolicy] | Omit = omit,
        session_duration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_id: AppID,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        domain: str | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        type: ApplicationType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

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

    @overload
    def update(
        self,
        app_id: AppID,
        *,
        target_criteria: Iterable[application_update_params.InfrastructureApplicationTargetCriterion],
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        name: str | Omit = omit,
        policies: Iterable[application_update_params.InfrastructureApplicationPolicy] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          name: The name of the application.

          policies: The policies that Access applies to the application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_id: AppID,
        *,
        domain: str,
        target_criteria: Iterable[application_update_params.BrowserRdpApplicationTargetCriterion],
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_update_params.BrowserRdpApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_update_params.BrowserRdpApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_update_params.BrowserRdpApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def update(
        self,
        app_id: AppID,
        *,
        domain: str | Omit = omit,
        type: ApplicationType
        | Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ]
        | Omit = omit,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_update_params.SelfHostedApplicationDestination]
        | Iterable[application_update_params.BrowserSSHApplicationDestination]
        | Iterable[application_update_params.BrowserVNCApplicationDestination]
        | Iterable[application_update_params.BrowserRdpApplicationDestination]
        | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_update_params.SelfHostedApplicationPolicy]
        | SequenceNotStr[application_update_params.SaaSApplicationPolicy]
        | SequenceNotStr[application_update_params.BrowserSSHApplicationPolicy]
        | SequenceNotStr[application_update_params.BrowserVNCApplicationPolicy]
        | SequenceNotStr[application_update_params.AppLauncherApplicationPolicy]
        | SequenceNotStr[application_update_params.DeviceEnrollmentPermissionsApplicationPolicy]
        | SequenceNotStr[application_update_params.BrowserIsolationPermissionsApplicationPolicy]
        | Iterable[application_update_params.InfrastructureApplicationPolicy]
        | SequenceNotStr[application_update_params.BrowserRdpApplicationPolicy]
        | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_update_params.SelfHostedApplicationSCIMConfig
        | application_update_params.SaaSApplicationSCIMConfig
        | application_update_params.BrowserSSHApplicationSCIMConfig
        | application_update_params.BrowserVNCApplicationSCIMConfig
        | application_update_params.BrowserRdpApplicationSCIMConfig
        | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        saas_app: application_update_params.SaaSApplicationSaaSApp | Omit = omit,
        app_launcher_logo_url: str | Omit = omit,
        bg_color: str | Omit = omit,
        footer_links: Iterable[application_update_params.AppLauncherApplicationFooterLink] | Omit = omit,
        header_bg_color: str | Omit = omit,
        landing_page_design: application_update_params.AppLauncherApplicationLandingPageDesign | Omit = omit,
        skip_app_launcher_login_page: bool | Omit = omit,
        target_criteria: Iterable[application_update_params.InfrastructureApplicationTargetCriterion]
        | Iterable[application_update_params.BrowserRdpApplicationTargetCriterion]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
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
            Optional[ApplicationUpdateResponse],
            self._put(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
                body=maybe_transform(
                    {
                        "domain": domain,
                        "type": type,
                        "allow_authenticate_via_warp": allow_authenticate_via_warp,
                        "allow_iframe": allow_iframe,
                        "allowed_idps": allowed_idps,
                        "app_launcher_visible": app_launcher_visible,
                        "auto_redirect_to_identity": auto_redirect_to_identity,
                        "cors_headers": cors_headers,
                        "custom_deny_message": custom_deny_message,
                        "custom_deny_url": custom_deny_url,
                        "custom_non_identity_deny_url": custom_non_identity_deny_url,
                        "custom_pages": custom_pages,
                        "destinations": destinations,
                        "enable_binding_cookie": enable_binding_cookie,
                        "http_only_cookie_attribute": http_only_cookie_attribute,
                        "logo_url": logo_url,
                        "name": name,
                        "options_preflight_bypass": options_preflight_bypass,
                        "path_cookie_attribute": path_cookie_attribute,
                        "policies": policies,
                        "read_service_tokens_from_header": read_service_tokens_from_header,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "scim_config": scim_config,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "saas_app": saas_app,
                        "app_launcher_logo_url": app_launcher_logo_url,
                        "bg_color": bg_color,
                        "footer_links": footer_links,
                        "header_bg_color": header_bg_color,
                        "landing_page_design": landing_page_design,
                        "skip_app_launcher_login_page": skip_app_launcher_login_page,
                        "target_criteria": target_criteria,
                    },
                    application_update_params.ApplicationUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[ApplicationUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ApplicationUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        aud: str | Omit = omit,
        domain: str | Omit = omit,
        exact: bool | Omit = omit,
        name: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        target_attributes: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[ApplicationListResponse]:
        """
        Lists all Access applications in an account or zone.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          aud: The aud of the app.

          domain: The domain of the app.

          exact: True for only exact string matches against passed name/domain query parameters.

          name: The name of the app.

          page: Page number of results.

          per_page: Number of results per page.

          search: Search for apps by other listed query parameters.

          target_attributes: Target Criteria attributes in key=value format.

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
            page=SyncV4PagePaginationArray[ApplicationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "aud": aud,
                        "domain": domain,
                        "exact": exact,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "target_attributes": target_attributes,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            model=cast(Any, ApplicationListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    def delete(
        self,
        app_id: AppID,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationDeleteResponse]:
        """
        Deletes an application from Access.

        Args:
          app_id: Identifier.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
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
        app_id: AppID,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationGetResponse]:
        """
        Fetches information about an Access application.

        Args:
          app_id: Identifier.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
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
            Optional[ApplicationGetResponse],
            self._get(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[ApplicationGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ApplicationGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def revoke_tokens(
        self,
        app_id: AppID,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Revokes all tokens issued for an application.

        Args:
          app_id: Identifier.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
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
    def policy_tests(self) -> AsyncPolicyTestsResource:
        return AsyncPolicyTestsResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncApplicationsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        domain: str,
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_create_params.SelfHostedApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_create_params.SelfHostedApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_create_params.SelfHostedApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Adds a new application to Access.

        Args:
          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        policies: SequenceNotStr[application_create_params.SaaSApplicationPolicy] | Omit = omit,
        saas_app: application_create_params.SaaSApplicationSaaSApp | Omit = omit,
        scim_config: application_create_params.SaaSApplicationSCIMConfig | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        type: ApplicationType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

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
        type: Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ],
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_create_params.BrowserSSHApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_create_params.BrowserSSHApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_create_params.BrowserSSHApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Adds a new application to Access.

        Args:
          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        type: Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ],
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_create_params.BrowserVNCApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_create_params.BrowserVNCApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_create_params.BrowserVNCApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Adds a new application to Access.

        Args:
          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        type: Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ],
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_logo_url: str | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        bg_color: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        footer_links: Iterable[application_create_params.AppLauncherApplicationFooterLink] | Omit = omit,
        header_bg_color: str | Omit = omit,
        landing_page_design: application_create_params.AppLauncherApplicationLandingPageDesign | Omit = omit,
        policies: SequenceNotStr[application_create_params.AppLauncherApplicationPolicy] | Omit = omit,
        session_duration: str | Omit = omit,
        skip_app_launcher_login_page: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Adds a new application to Access.

        Args:
          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_logo_url: The image URL of the logo shown in the App Launcher header.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          bg_color: The background color of the App Launcher page.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          footer_links: The links in the App Launcher footer.

          header_bg_color: The background color of the App Launcher header.

          landing_page_design: The design of the App Launcher landing page shown to users when they log in.

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

          skip_app_launcher_login_page: Determines when to skip the App Launcher landing page.

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
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        policies: SequenceNotStr[application_create_params.DeviceEnrollmentPermissionsApplicationPolicy] | Omit = omit,
        session_duration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
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

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        policies: SequenceNotStr[application_create_params.BrowserIsolationPermissionsApplicationPolicy] | Omit = omit,
        session_duration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
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

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        domain: str | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        type: ApplicationType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
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

    @overload
    async def create(
        self,
        *,
        target_criteria: Iterable[application_create_params.InfrastructureApplicationTargetCriterion],
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        name: str | Omit = omit,
        policies: Iterable[application_create_params.InfrastructureApplicationPolicy] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Adds a new application to Access.

        Args:
          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          name: The name of the application.

          policies: The policies that Access applies to the application.

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
        target_criteria: Iterable[application_create_params.BrowserRdpApplicationTargetCriterion],
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_create_params.BrowserRdpApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_create_params.BrowserRdpApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_create_params.BrowserRdpApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
        """
        Adds a new application to Access.

        Args:
          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def create(
        self,
        *,
        domain: str | Omit = omit,
        type: ApplicationType
        | Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ]
        | Omit = omit,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_create_params.SelfHostedApplicationDestination]
        | Iterable[application_create_params.BrowserSSHApplicationDestination]
        | Iterable[application_create_params.BrowserVNCApplicationDestination]
        | Iterable[application_create_params.BrowserRdpApplicationDestination]
        | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_create_params.SelfHostedApplicationPolicy]
        | SequenceNotStr[application_create_params.SaaSApplicationPolicy]
        | SequenceNotStr[application_create_params.BrowserSSHApplicationPolicy]
        | SequenceNotStr[application_create_params.BrowserVNCApplicationPolicy]
        | SequenceNotStr[application_create_params.AppLauncherApplicationPolicy]
        | SequenceNotStr[application_create_params.DeviceEnrollmentPermissionsApplicationPolicy]
        | SequenceNotStr[application_create_params.BrowserIsolationPermissionsApplicationPolicy]
        | Iterable[application_create_params.InfrastructureApplicationPolicy]
        | SequenceNotStr[application_create_params.BrowserRdpApplicationPolicy]
        | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_create_params.SelfHostedApplicationSCIMConfig
        | application_create_params.SaaSApplicationSCIMConfig
        | application_create_params.BrowserSSHApplicationSCIMConfig
        | application_create_params.BrowserVNCApplicationSCIMConfig
        | application_create_params.BrowserRdpApplicationSCIMConfig
        | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        saas_app: application_create_params.SaaSApplicationSaaSApp | Omit = omit,
        app_launcher_logo_url: str | Omit = omit,
        bg_color: str | Omit = omit,
        footer_links: Iterable[application_create_params.AppLauncherApplicationFooterLink] | Omit = omit,
        header_bg_color: str | Omit = omit,
        landing_page_design: application_create_params.AppLauncherApplicationLandingPageDesign | Omit = omit,
        skip_app_launcher_login_page: bool | Omit = omit,
        target_criteria: Iterable[application_create_params.InfrastructureApplicationTargetCriterion]
        | Iterable[application_create_params.BrowserRdpApplicationTargetCriterion]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationCreateResponse]:
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
            Optional[ApplicationCreateResponse],
            await self._post(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps",
                body=await async_maybe_transform(
                    {
                        "domain": domain,
                        "type": type,
                        "allow_authenticate_via_warp": allow_authenticate_via_warp,
                        "allow_iframe": allow_iframe,
                        "allowed_idps": allowed_idps,
                        "app_launcher_visible": app_launcher_visible,
                        "auto_redirect_to_identity": auto_redirect_to_identity,
                        "cors_headers": cors_headers,
                        "custom_deny_message": custom_deny_message,
                        "custom_deny_url": custom_deny_url,
                        "custom_non_identity_deny_url": custom_non_identity_deny_url,
                        "custom_pages": custom_pages,
                        "destinations": destinations,
                        "enable_binding_cookie": enable_binding_cookie,
                        "http_only_cookie_attribute": http_only_cookie_attribute,
                        "logo_url": logo_url,
                        "name": name,
                        "options_preflight_bypass": options_preflight_bypass,
                        "path_cookie_attribute": path_cookie_attribute,
                        "policies": policies,
                        "read_service_tokens_from_header": read_service_tokens_from_header,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "scim_config": scim_config,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "saas_app": saas_app,
                        "app_launcher_logo_url": app_launcher_logo_url,
                        "bg_color": bg_color,
                        "footer_links": footer_links,
                        "header_bg_color": header_bg_color,
                        "landing_page_design": landing_page_design,
                        "skip_app_launcher_login_page": skip_app_launcher_login_page,
                        "target_criteria": target_criteria,
                    },
                    application_create_params.ApplicationCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[ApplicationCreateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ApplicationCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        app_id: AppID,
        *,
        domain: str,
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_update_params.SelfHostedApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_update_params.SelfHostedApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_update_params.SelfHostedApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        app_id: AppID,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        policies: SequenceNotStr[application_update_params.SaaSApplicationPolicy] | Omit = omit,
        saas_app: application_update_params.SaaSApplicationSaaSApp | Omit = omit,
        scim_config: application_update_params.SaaSApplicationSCIMConfig | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        type: ApplicationType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

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
        app_id: AppID,
        *,
        domain: str,
        type: Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ],
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_update_params.BrowserSSHApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_update_params.BrowserSSHApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_update_params.BrowserSSHApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        app_id: AppID,
        *,
        domain: str,
        type: Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ],
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_update_params.BrowserVNCApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_update_params.BrowserVNCApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_update_params.BrowserVNCApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

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
        app_id: AppID,
        *,
        type: Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ],
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_logo_url: str | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        bg_color: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        footer_links: Iterable[application_update_params.AppLauncherApplicationFooterLink] | Omit = omit,
        header_bg_color: str | Omit = omit,
        landing_page_design: application_update_params.AppLauncherApplicationLandingPageDesign | Omit = omit,
        policies: SequenceNotStr[application_update_params.AppLauncherApplicationPolicy] | Omit = omit,
        session_duration: str | Omit = omit,
        skip_app_launcher_login_page: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          app_launcher_logo_url: The image URL of the logo shown in the App Launcher header.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          bg_color: The background color of the App Launcher page.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          footer_links: The links in the App Launcher footer.

          header_bg_color: The background color of the App Launcher header.

          landing_page_design: The design of the App Launcher landing page shown to users when they log in.

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

          skip_app_launcher_login_page: Determines when to skip the App Launcher landing page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_id: AppID,
        *,
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        policies: SequenceNotStr[application_update_params.DeviceEnrollmentPermissionsApplicationPolicy] | Omit = omit,
        session_duration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_id: AppID,
        *,
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        policies: SequenceNotStr[application_update_params.BrowserIsolationPermissionsApplicationPolicy] | Omit = omit,
        session_duration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_id: AppID,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        domain: str | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        type: ApplicationType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

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

    @overload
    async def update(
        self,
        app_id: AppID,
        *,
        target_criteria: Iterable[application_update_params.InfrastructureApplicationTargetCriterion],
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        name: str | Omit = omit,
        policies: Iterable[application_update_params.InfrastructureApplicationPolicy] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          name: The name of the application.

          policies: The policies that Access applies to the application.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_id: AppID,
        *,
        domain: str,
        target_criteria: Iterable[application_update_params.BrowserRdpApplicationTargetCriterion],
        type: ApplicationType,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_update_params.BrowserRdpApplicationDestination] | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_update_params.BrowserRdpApplicationPolicy] | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_update_params.BrowserRdpApplicationSCIMConfig | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        """
        Updates an Access application.

        Args:
          app_id: Identifier.

          domain: The primary hostname and path secured by Access. This domain will be displayed
              if the app is visible in the App Launcher.

          type: The application type.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allow_iframe: Enables loading application content in an iFrame.

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

          destinations: List of destinations secured by Access. This supersedes `self_hosted_domains` to
              allow for more flexibility in defining different types of domains. If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

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

          policies: The policies that Access applies to the application, in ascending order of
              precedence. Items can reference existing policies or create new policies
              exclusive to the application.

          read_service_tokens_from_header: Allows matching Access Service Tokens passed HTTP in a single header with this
              name. This works as an alternative to the (CF-Access-Client-Id,
              CF-Access-Client-Secret) pair of headers. The header value will be interpreted
              as a json object similar to: { "cf-access-client-id":
              "88bf3b6d86161464f6509f7219099e57.access.example.com",
              "cf-access-client-secret":
              "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }

          same_site_cookie_attribute: Sets the SameSite cookie setting, which provides increased security against CSRF
              attacks.

          scim_config: Configuration for provisioning to this application via SCIM. This is currently
              in closed beta.

          self_hosted_domains: List of public domains that Access will secure. This field is deprecated in
              favor of `destinations` and will be supported until **November 21, 2025.** If
              `destinations` are provided, then `self_hosted_domains` will be ignored.

          service_auth_401_redirect: Returns a 401 status code when the request is blocked by a Service Auth policy.

          session_duration: The amount of time that tokens issued for this application will be valid. Must
              be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms,
              s, m, h. Note: unsupported for infrastructure type applications.

          skip_interstitial: Enables automatic authentication through cloudflared.

          tags: The tags you want assigned to an application. Tags are used to filter
              applications in the App Launcher dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def update(
        self,
        app_id: AppID,
        *,
        domain: str | Omit = omit,
        type: ApplicationType
        | Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
        ]
        | Omit = omit,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        allow_authenticate_via_warp: bool | Omit = omit,
        allow_iframe: bool | Omit = omit,
        allowed_idps: SequenceNotStr[AllowedIdPs] | Omit = omit,
        app_launcher_visible: bool | Omit = omit,
        auto_redirect_to_identity: bool | Omit = omit,
        cors_headers: CORSHeadersParam | Omit = omit,
        custom_deny_message: str | Omit = omit,
        custom_deny_url: str | Omit = omit,
        custom_non_identity_deny_url: str | Omit = omit,
        custom_pages: SequenceNotStr[str] | Omit = omit,
        destinations: Iterable[application_update_params.SelfHostedApplicationDestination]
        | Iterable[application_update_params.BrowserSSHApplicationDestination]
        | Iterable[application_update_params.BrowserVNCApplicationDestination]
        | Iterable[application_update_params.BrowserRdpApplicationDestination]
        | Omit = omit,
        enable_binding_cookie: bool | Omit = omit,
        http_only_cookie_attribute: bool | Omit = omit,
        logo_url: str | Omit = omit,
        name: str | Omit = omit,
        options_preflight_bypass: bool | Omit = omit,
        path_cookie_attribute: bool | Omit = omit,
        policies: SequenceNotStr[application_update_params.SelfHostedApplicationPolicy]
        | SequenceNotStr[application_update_params.SaaSApplicationPolicy]
        | SequenceNotStr[application_update_params.BrowserSSHApplicationPolicy]
        | SequenceNotStr[application_update_params.BrowserVNCApplicationPolicy]
        | SequenceNotStr[application_update_params.AppLauncherApplicationPolicy]
        | SequenceNotStr[application_update_params.DeviceEnrollmentPermissionsApplicationPolicy]
        | SequenceNotStr[application_update_params.BrowserIsolationPermissionsApplicationPolicy]
        | Iterable[application_update_params.InfrastructureApplicationPolicy]
        | SequenceNotStr[application_update_params.BrowserRdpApplicationPolicy]
        | Omit = omit,
        read_service_tokens_from_header: str | Omit = omit,
        same_site_cookie_attribute: str | Omit = omit,
        scim_config: application_update_params.SelfHostedApplicationSCIMConfig
        | application_update_params.SaaSApplicationSCIMConfig
        | application_update_params.BrowserSSHApplicationSCIMConfig
        | application_update_params.BrowserVNCApplicationSCIMConfig
        | application_update_params.BrowserRdpApplicationSCIMConfig
        | Omit = omit,
        self_hosted_domains: SequenceNotStr[SelfHostedDomains] | Omit = omit,
        service_auth_401_redirect: bool | Omit = omit,
        session_duration: str | Omit = omit,
        skip_interstitial: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        saas_app: application_update_params.SaaSApplicationSaaSApp | Omit = omit,
        app_launcher_logo_url: str | Omit = omit,
        bg_color: str | Omit = omit,
        footer_links: Iterable[application_update_params.AppLauncherApplicationFooterLink] | Omit = omit,
        header_bg_color: str | Omit = omit,
        landing_page_design: application_update_params.AppLauncherApplicationLandingPageDesign | Omit = omit,
        skip_app_launcher_login_page: bool | Omit = omit,
        target_criteria: Iterable[application_update_params.InfrastructureApplicationTargetCriterion]
        | Iterable[application_update_params.BrowserRdpApplicationTargetCriterion]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationUpdateResponse]:
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
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
            Optional[ApplicationUpdateResponse],
            await self._put(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
                body=await async_maybe_transform(
                    {
                        "domain": domain,
                        "type": type,
                        "allow_authenticate_via_warp": allow_authenticate_via_warp,
                        "allow_iframe": allow_iframe,
                        "allowed_idps": allowed_idps,
                        "app_launcher_visible": app_launcher_visible,
                        "auto_redirect_to_identity": auto_redirect_to_identity,
                        "cors_headers": cors_headers,
                        "custom_deny_message": custom_deny_message,
                        "custom_deny_url": custom_deny_url,
                        "custom_non_identity_deny_url": custom_non_identity_deny_url,
                        "custom_pages": custom_pages,
                        "destinations": destinations,
                        "enable_binding_cookie": enable_binding_cookie,
                        "http_only_cookie_attribute": http_only_cookie_attribute,
                        "logo_url": logo_url,
                        "name": name,
                        "options_preflight_bypass": options_preflight_bypass,
                        "path_cookie_attribute": path_cookie_attribute,
                        "policies": policies,
                        "read_service_tokens_from_header": read_service_tokens_from_header,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "scim_config": scim_config,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "saas_app": saas_app,
                        "app_launcher_logo_url": app_launcher_logo_url,
                        "bg_color": bg_color,
                        "footer_links": footer_links,
                        "header_bg_color": header_bg_color,
                        "landing_page_design": landing_page_design,
                        "skip_app_launcher_login_page": skip_app_launcher_login_page,
                        "target_criteria": target_criteria,
                    },
                    application_update_params.ApplicationUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[ApplicationUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ApplicationUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        aud: str | Omit = omit,
        domain: str | Omit = omit,
        exact: bool | Omit = omit,
        name: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        target_attributes: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ApplicationListResponse, AsyncV4PagePaginationArray[ApplicationListResponse]]:
        """
        Lists all Access applications in an account or zone.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          aud: The aud of the app.

          domain: The domain of the app.

          exact: True for only exact string matches against passed name/domain query parameters.

          name: The name of the app.

          page: Page number of results.

          per_page: Number of results per page.

          search: Search for apps by other listed query parameters.

          target_attributes: Target Criteria attributes in key=value format.

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
            page=AsyncV4PagePaginationArray[ApplicationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "aud": aud,
                        "domain": domain,
                        "exact": exact,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "target_attributes": target_attributes,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            model=cast(Any, ApplicationListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    async def delete(
        self,
        app_id: AppID,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationDeleteResponse]:
        """
        Deletes an application from Access.

        Args:
          app_id: Identifier.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
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
        app_id: AppID,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationGetResponse]:
        """
        Fetches information about an Access application.

        Args:
          app_id: Identifier.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
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
            Optional[ApplicationGetResponse],
            await self._get(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[ApplicationGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ApplicationGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def revoke_tokens(
        self,
        app_id: AppID,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Revokes all tokens issued for an application.

        Args:
          app_id: Identifier.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
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

    @cached_property
    def policy_tests(self) -> PolicyTestsResourceWithRawResponse:
        return PolicyTestsResourceWithRawResponse(self._applications.policy_tests)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._applications.settings)


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

    @cached_property
    def policy_tests(self) -> AsyncPolicyTestsResourceWithRawResponse:
        return AsyncPolicyTestsResourceWithRawResponse(self._applications.policy_tests)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._applications.settings)


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

    @cached_property
    def policy_tests(self) -> PolicyTestsResourceWithStreamingResponse:
        return PolicyTestsResourceWithStreamingResponse(self._applications.policy_tests)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._applications.settings)


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

    @cached_property
    def policy_tests(self) -> AsyncPolicyTestsResourceWithStreamingResponse:
        return AsyncPolicyTestsResourceWithStreamingResponse(self._applications.policy_tests)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._applications.settings)
