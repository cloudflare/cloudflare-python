# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .cas import Cas, AsyncCas

from ...._compat import cached_property

from .revoke_tokens import RevokeTokens, AsyncRevokeTokens

from .user_policy_checks import UserPolicyChecks, AsyncUserPolicyChecks

from .policies import Policies, AsyncPolicies

from typing import List, Union, Type, Optional

from ....types.access import (
    AppCreateResponse,
    AppUpdateResponse,
    AppListResponse,
    AppDeleteResponse,
    AppGetResponse,
    app_create_params,
    app_update_params,
)

from typing_extensions import Literal

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.access import app_create_params
from ....types.access import app_update_params
from .cas import (
    Cas,
    AsyncCas,
    CasWithRawResponse,
    AsyncCasWithRawResponse,
    CasWithStreamingResponse,
    AsyncCasWithStreamingResponse,
)
from .revoke_tokens import (
    RevokeTokens,
    AsyncRevokeTokens,
    RevokeTokensWithRawResponse,
    AsyncRevokeTokensWithRawResponse,
    RevokeTokensWithStreamingResponse,
    AsyncRevokeTokensWithStreamingResponse,
)
from .user_policy_checks import (
    UserPolicyChecks,
    AsyncUserPolicyChecks,
    UserPolicyChecksWithRawResponse,
    AsyncUserPolicyChecksWithRawResponse,
    UserPolicyChecksWithStreamingResponse,
    AsyncUserPolicyChecksWithStreamingResponse,
)
from .policies import (
    Policies,
    AsyncPolicies,
    PoliciesWithRawResponse,
    AsyncPoliciesWithRawResponse,
    PoliciesWithStreamingResponse,
    AsyncPoliciesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Apps", "AsyncApps"]


class Apps(SyncAPIResource):
    @cached_property
    def cas(self) -> Cas:
        return Cas(self._client)

    @cached_property
    def revoke_tokens(self) -> RevokeTokens:
        return RevokeTokens(self._client)

    @cached_property
    def user_policy_checks(self) -> UserPolicyChecks:
        return UserPolicyChecks(self._client)

    @cached_property
    def policies(self) -> Policies:
        return Policies(self._client)

    @cached_property
    def with_raw_response(self) -> AppsWithRawResponse:
        return AppsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppsWithStreamingResponse:
        return AppsWithStreamingResponse(self)

    @overload
    def create(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        domain: str,
        type: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_create_params.Variant0CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

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
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        saas_app: app_create_params.Variant1SaasApp | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

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
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        domain: str,
        type: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_create_params.Variant2CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

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
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        domain: str,
        type: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_create_params.Variant3CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

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
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        type: Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"],
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

          type: The application type.

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
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        type: Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"],
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

          type: The application type.

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
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        type: Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"],
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

          type: The application type.

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
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        app_launcher_visible: object | NotGiven = NOT_GIVEN,
        domain: object | NotGiven = NOT_GIVEN,
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
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

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

    @required_args(
        ["account_or_zone", "domain", "type"],
        ["account_or_zone"],
        ["account_or_zone", "domain", "type"],
        ["account_or_zone", "domain", "type"],
        ["account_or_zone", "type"],
        ["account_or_zone", "type"],
        ["account_or_zone", "type"],
        ["account_or_zone"],
    )
    def create(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        domain: str | object | NotGiven = NOT_GIVEN,
        type: str
        | Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"]
        | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | object | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_create_params.Variant0CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        saas_app: app_create_params.Variant1SaasApp | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppCreateResponse:
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return cast(
            AppCreateResponse,
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
                        "path_cookie_attribute": path_cookie_attribute,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "saas_app": saas_app,
                    },
                    app_create_params.AppCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AppCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        domain: str,
        type: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_update_params.Variant0CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

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
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        saas_app: app_update_params.Variant1SaasApp | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

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
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        domain: str,
        type: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_update_params.Variant2CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

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
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        domain: str,
        type: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_update_params.Variant3CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

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
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        type: Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"],
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          type: The application type.

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
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        type: Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"],
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          type: The application type.

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
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        type: Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"],
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          type: The application type.

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
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        app_launcher_visible: object | NotGiven = NOT_GIVEN,
        domain: object | NotGiven = NOT_GIVEN,
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
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

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

    @required_args(
        ["account_or_zone", "account_or_zone_id", "domain", "type"],
        ["account_or_zone", "account_or_zone_id"],
        ["account_or_zone", "account_or_zone_id", "domain", "type"],
        ["account_or_zone", "account_or_zone_id", "domain", "type"],
        ["account_or_zone", "account_or_zone_id", "type"],
        ["account_or_zone", "account_or_zone_id", "type"],
        ["account_or_zone", "account_or_zone_id", "type"],
        ["account_or_zone", "account_or_zone_id"],
    )
    def update(
        self,
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        domain: str | object | NotGiven = NOT_GIVEN,
        type: str
        | Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"]
        | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | object | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_update_params.Variant0CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        saas_app: app_update_params.Variant1SaasApp | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppUpdateResponse:
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return cast(
            AppUpdateResponse,
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
                        "path_cookie_attribute": path_cookie_attribute,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "saas_app": saas_app,
                    },
                    app_update_params.AppUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AppUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
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
    ) -> Optional[AppListResponse]:
        """
        Lists all Access applications in an account or zone.

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
            f"/{account_or_zone}/{account_or_zone_id}/access/apps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppListResponse]], ResultWrapper[AppListResponse]),
        )

    def delete(
        self,
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppDeleteResponse:
        """
        Deletes an application from Access.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AppDeleteResponse], ResultWrapper[AppDeleteResponse]),
        )

    def get(
        self,
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppGetResponse:
        """
        Fetches information about an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return cast(
            AppGetResponse,
            self._get(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AppGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncApps(AsyncAPIResource):
    @cached_property
    def cas(self) -> AsyncCas:
        return AsyncCas(self._client)

    @cached_property
    def revoke_tokens(self) -> AsyncRevokeTokens:
        return AsyncRevokeTokens(self._client)

    @cached_property
    def user_policy_checks(self) -> AsyncUserPolicyChecks:
        return AsyncUserPolicyChecks(self._client)

    @cached_property
    def policies(self) -> AsyncPolicies:
        return AsyncPolicies(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAppsWithRawResponse:
        return AsyncAppsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppsWithStreamingResponse:
        return AsyncAppsWithStreamingResponse(self)

    @overload
    async def create(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        domain: str,
        type: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_create_params.Variant0CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

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
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        saas_app: app_create_params.Variant1SaasApp | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

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
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        domain: str,
        type: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_create_params.Variant2CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

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
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        domain: str,
        type: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_create_params.Variant3CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

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
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        type: Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"],
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

          type: The application type.

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
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        type: Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"],
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

          type: The application type.

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
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        type: Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"],
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

          type: The application type.

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
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        app_launcher_visible: object | NotGiven = NOT_GIVEN,
        domain: object | NotGiven = NOT_GIVEN,
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
    ) -> AppCreateResponse:
        """
        Adds a new application to Access.

        Args:
          account_or_zone_id: Identifier

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

    @required_args(
        ["account_or_zone", "domain", "type"],
        ["account_or_zone"],
        ["account_or_zone", "domain", "type"],
        ["account_or_zone", "domain", "type"],
        ["account_or_zone", "type"],
        ["account_or_zone", "type"],
        ["account_or_zone", "type"],
        ["account_or_zone"],
    )
    async def create(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        domain: str | object | NotGiven = NOT_GIVEN,
        type: str
        | Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"]
        | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | object | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_create_params.Variant0CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        saas_app: app_create_params.Variant1SaasApp | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppCreateResponse:
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return cast(
            AppCreateResponse,
            await self._post(
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
                        "path_cookie_attribute": path_cookie_attribute,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "saas_app": saas_app,
                    },
                    app_create_params.AppCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AppCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        domain: str,
        type: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_update_params.Variant0CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

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
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        saas_app: app_update_params.Variant1SaasApp | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

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
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        domain: str,
        type: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_update_params.Variant2CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

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
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        domain: str,
        type: str,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_update_params.Variant3CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
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
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          domain: The primary hostname and path that Access will secure. If the app is visible in
              the App Launcher dashboard, this is the domain that will be displayed.

          type: The application type.

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
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        type: Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"],
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          type: The application type.

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
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        type: Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"],
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          type: The application type.

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
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        type: Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"],
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          type: The application type.

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
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        app_launcher_visible: object | NotGiven = NOT_GIVEN,
        domain: object | NotGiven = NOT_GIVEN,
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
    ) -> AppUpdateResponse:
        """
        Updates an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

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

    @required_args(
        ["account_or_zone", "account_or_zone_id", "domain", "type"],
        ["account_or_zone", "account_or_zone_id"],
        ["account_or_zone", "account_or_zone_id", "domain", "type"],
        ["account_or_zone", "account_or_zone_id", "domain", "type"],
        ["account_or_zone", "account_or_zone_id", "type"],
        ["account_or_zone", "account_or_zone_id", "type"],
        ["account_or_zone", "account_or_zone_id", "type"],
        ["account_or_zone", "account_or_zone_id"],
    )
    async def update(
        self,
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        domain: str | object | NotGiven = NOT_GIVEN,
        type: str
        | Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"]
        | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: bool | object | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: app_update_params.Variant0CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        saas_app: app_update_params.Variant1SaasApp | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppUpdateResponse:
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return cast(
            AppUpdateResponse,
            await self._put(
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
                        "path_cookie_attribute": path_cookie_attribute,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "saas_app": saas_app,
                    },
                    app_update_params.AppUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AppUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
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
    ) -> Optional[AppListResponse]:
        """
        Lists all Access applications in an account or zone.

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
            f"/{account_or_zone}/{account_or_zone_id}/access/apps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppListResponse]], ResultWrapper[AppListResponse]),
        )

    async def delete(
        self,
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppDeleteResponse:
        """
        Deletes an application from Access.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AppDeleteResponse], ResultWrapper[AppDeleteResponse]),
        )

    async def get(
        self,
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppGetResponse:
        """
        Fetches information about an Access application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return cast(
            AppGetResponse,
            await self._get(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AppGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AppsWithRawResponse:
    def __init__(self, apps: Apps) -> None:
        self._apps = apps

        self.create = to_raw_response_wrapper(
            apps.create,
        )
        self.update = to_raw_response_wrapper(
            apps.update,
        )
        self.list = to_raw_response_wrapper(
            apps.list,
        )
        self.delete = to_raw_response_wrapper(
            apps.delete,
        )
        self.get = to_raw_response_wrapper(
            apps.get,
        )

    @cached_property
    def cas(self) -> CasWithRawResponse:
        return CasWithRawResponse(self._apps.cas)

    @cached_property
    def revoke_tokens(self) -> RevokeTokensWithRawResponse:
        return RevokeTokensWithRawResponse(self._apps.revoke_tokens)

    @cached_property
    def user_policy_checks(self) -> UserPolicyChecksWithRawResponse:
        return UserPolicyChecksWithRawResponse(self._apps.user_policy_checks)

    @cached_property
    def policies(self) -> PoliciesWithRawResponse:
        return PoliciesWithRawResponse(self._apps.policies)


class AsyncAppsWithRawResponse:
    def __init__(self, apps: AsyncApps) -> None:
        self._apps = apps

        self.create = async_to_raw_response_wrapper(
            apps.create,
        )
        self.update = async_to_raw_response_wrapper(
            apps.update,
        )
        self.list = async_to_raw_response_wrapper(
            apps.list,
        )
        self.delete = async_to_raw_response_wrapper(
            apps.delete,
        )
        self.get = async_to_raw_response_wrapper(
            apps.get,
        )

    @cached_property
    def cas(self) -> AsyncCasWithRawResponse:
        return AsyncCasWithRawResponse(self._apps.cas)

    @cached_property
    def revoke_tokens(self) -> AsyncRevokeTokensWithRawResponse:
        return AsyncRevokeTokensWithRawResponse(self._apps.revoke_tokens)

    @cached_property
    def user_policy_checks(self) -> AsyncUserPolicyChecksWithRawResponse:
        return AsyncUserPolicyChecksWithRawResponse(self._apps.user_policy_checks)

    @cached_property
    def policies(self) -> AsyncPoliciesWithRawResponse:
        return AsyncPoliciesWithRawResponse(self._apps.policies)


class AppsWithStreamingResponse:
    def __init__(self, apps: Apps) -> None:
        self._apps = apps

        self.create = to_streamed_response_wrapper(
            apps.create,
        )
        self.update = to_streamed_response_wrapper(
            apps.update,
        )
        self.list = to_streamed_response_wrapper(
            apps.list,
        )
        self.delete = to_streamed_response_wrapper(
            apps.delete,
        )
        self.get = to_streamed_response_wrapper(
            apps.get,
        )

    @cached_property
    def cas(self) -> CasWithStreamingResponse:
        return CasWithStreamingResponse(self._apps.cas)

    @cached_property
    def revoke_tokens(self) -> RevokeTokensWithStreamingResponse:
        return RevokeTokensWithStreamingResponse(self._apps.revoke_tokens)

    @cached_property
    def user_policy_checks(self) -> UserPolicyChecksWithStreamingResponse:
        return UserPolicyChecksWithStreamingResponse(self._apps.user_policy_checks)

    @cached_property
    def policies(self) -> PoliciesWithStreamingResponse:
        return PoliciesWithStreamingResponse(self._apps.policies)


class AsyncAppsWithStreamingResponse:
    def __init__(self, apps: AsyncApps) -> None:
        self._apps = apps

        self.create = async_to_streamed_response_wrapper(
            apps.create,
        )
        self.update = async_to_streamed_response_wrapper(
            apps.update,
        )
        self.list = async_to_streamed_response_wrapper(
            apps.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            apps.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            apps.get,
        )

    @cached_property
    def cas(self) -> AsyncCasWithStreamingResponse:
        return AsyncCasWithStreamingResponse(self._apps.cas)

    @cached_property
    def revoke_tokens(self) -> AsyncRevokeTokensWithStreamingResponse:
        return AsyncRevokeTokensWithStreamingResponse(self._apps.revoke_tokens)

    @cached_property
    def user_policy_checks(self) -> AsyncUserPolicyChecksWithStreamingResponse:
        return AsyncUserPolicyChecksWithStreamingResponse(self._apps.user_policy_checks)

    @cached_property
    def policies(self) -> AsyncPoliciesWithStreamingResponse:
        return AsyncPoliciesWithStreamingResponse(self._apps.policies)
