# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, List, Type, Union, Optional, cast

import httpx

from .cas import (
    CAs,
    AsyncCAs,
    CAsWithRawResponse,
    AsyncCAsWithRawResponse,
    CAsWithStreamingResponse,
    AsyncCAsWithStreamingResponse,
)
from .policies import (
    Policies,
    AsyncPolicies,
    PoliciesWithRawResponse,
    AsyncPoliciesWithRawResponse,
    PoliciesWithStreamingResponse,
    AsyncPoliciesWithStreamingResponse,
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
from ....._base_client import (
    make_request_options,
)
from .user_policy_checks import (
    UserPolicyChecks,
    AsyncUserPolicyChecks,
    UserPolicyChecksWithRawResponse,
    AsyncUserPolicyChecksWithRawResponse,
    UserPolicyChecksWithStreamingResponse,
    AsyncUserPolicyChecksWithStreamingResponse,
)
from .....types.zero_trust.access import (
    AccessApps,
    ApplicationListResponse,
    ApplicationDeleteResponse,
    application_create_params,
    application_update_params,
)

__all__ = ["Applications", "AsyncApplications"]


class Applications(SyncAPIResource):
    @cached_property
    def cas(self) -> CAs:
        return CAs(self._client)

    @cached_property
    def user_policy_checks(self) -> UserPolicyChecks:
        return UserPolicyChecks(self._client)

    @cached_property
    def policies(self) -> Policies:
        return Policies(self._client)

    @cached_property
    def with_raw_response(self) -> ApplicationsWithRawResponse:
        return ApplicationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApplicationsWithStreamingResponse:
        return ApplicationsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: object | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: application_create_params.CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        domain: object | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        saas_app: application_create_params.SaasApp | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessApps:
        """
        Adds a new application to Access.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          domain: The URL or domain of the bookmark.

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

          type: The application type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            AccessApps,
            self._post(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps",
                body=maybe_transform(
                    {
                        "allow_authenticate_via_warp": allow_authenticate_via_warp,
                        "allowed_idps": allowed_idps,
                        "app_launcher_visible": app_launcher_visible,
                        "auto_redirect_to_identity": auto_redirect_to_identity,
                        "cors_headers": cors_headers,
                        "custom_deny_message": custom_deny_message,
                        "custom_deny_url": custom_deny_url,
                        "custom_non_identity_deny_url": custom_non_identity_deny_url,
                        "custom_pages": custom_pages,
                        "domain": domain,
                        "enable_binding_cookie": enable_binding_cookie,
                        "http_only_cookie_attribute": http_only_cookie_attribute,
                        "logo_url": logo_url,
                        "name": name,
                        "path_cookie_attribute": path_cookie_attribute,
                        "saas_app": saas_app,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "type": type,
                    },
                    application_create_params.ApplicationCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccessApps]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        app_id: Union[str, str],
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: object | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: application_update_params.CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        domain: object | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        saas_app: application_update_params.SaasApp | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessApps:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          domain: The URL or domain of the bookmark.

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

          type: The application type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            AccessApps,
            self._put(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
                body=maybe_transform(
                    {
                        "allow_authenticate_via_warp": allow_authenticate_via_warp,
                        "allowed_idps": allowed_idps,
                        "app_launcher_visible": app_launcher_visible,
                        "auto_redirect_to_identity": auto_redirect_to_identity,
                        "cors_headers": cors_headers,
                        "custom_deny_message": custom_deny_message,
                        "custom_deny_url": custom_deny_url,
                        "custom_non_identity_deny_url": custom_non_identity_deny_url,
                        "custom_pages": custom_pages,
                        "domain": domain,
                        "enable_binding_cookie": enable_binding_cookie,
                        "http_only_cookie_attribute": http_only_cookie_attribute,
                        "logo_url": logo_url,
                        "name": name,
                        "path_cookie_attribute": path_cookie_attribute,
                        "saas_app": saas_app,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "type": type,
                    },
                    application_update_params.ApplicationUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccessApps]
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
    ) -> Optional[ApplicationListResponse]:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ApplicationListResponse]], ResultWrapper[ApplicationListResponse]),
        )

    def delete(
        self,
        app_id: Union[str, str],
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationDeleteResponse:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ApplicationDeleteResponse], ResultWrapper[ApplicationDeleteResponse]),
        )

    def get(
        self,
        app_id: Union[str, str],
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessApps:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            AccessApps,
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
                    Any, ResultWrapper[AccessApps]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def revoke_tokens(
        self,
        app_id: Union[str, str],
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/revoke_tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncApplications(AsyncAPIResource):
    @cached_property
    def cas(self) -> AsyncCAs:
        return AsyncCAs(self._client)

    @cached_property
    def user_policy_checks(self) -> AsyncUserPolicyChecks:
        return AsyncUserPolicyChecks(self._client)

    @cached_property
    def policies(self) -> AsyncPolicies:
        return AsyncPolicies(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncApplicationsWithRawResponse:
        return AsyncApplicationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApplicationsWithStreamingResponse:
        return AsyncApplicationsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: object | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: application_create_params.CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        domain: object | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        saas_app: application_create_params.SaasApp | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessApps:
        """
        Adds a new application to Access.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          domain: The URL or domain of the bookmark.

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

          type: The application type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            AccessApps,
            await self._post(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps",
                body=await async_maybe_transform(
                    {
                        "allow_authenticate_via_warp": allow_authenticate_via_warp,
                        "allowed_idps": allowed_idps,
                        "app_launcher_visible": app_launcher_visible,
                        "auto_redirect_to_identity": auto_redirect_to_identity,
                        "cors_headers": cors_headers,
                        "custom_deny_message": custom_deny_message,
                        "custom_deny_url": custom_deny_url,
                        "custom_non_identity_deny_url": custom_non_identity_deny_url,
                        "custom_pages": custom_pages,
                        "domain": domain,
                        "enable_binding_cookie": enable_binding_cookie,
                        "http_only_cookie_attribute": http_only_cookie_attribute,
                        "logo_url": logo_url,
                        "name": name,
                        "path_cookie_attribute": path_cookie_attribute,
                        "saas_app": saas_app,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "type": type,
                    },
                    application_create_params.ApplicationCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccessApps]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        app_id: Union[str, str],
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        allow_authenticate_via_warp: bool | NotGiven = NOT_GIVEN,
        allowed_idps: List[str] | NotGiven = NOT_GIVEN,
        app_launcher_visible: object | NotGiven = NOT_GIVEN,
        auto_redirect_to_identity: bool | NotGiven = NOT_GIVEN,
        cors_headers: application_update_params.CorsHeaders | NotGiven = NOT_GIVEN,
        custom_deny_message: str | NotGiven = NOT_GIVEN,
        custom_deny_url: str | NotGiven = NOT_GIVEN,
        custom_non_identity_deny_url: str | NotGiven = NOT_GIVEN,
        custom_pages: List[str] | NotGiven = NOT_GIVEN,
        domain: object | NotGiven = NOT_GIVEN,
        enable_binding_cookie: bool | NotGiven = NOT_GIVEN,
        http_only_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        path_cookie_attribute: bool | NotGiven = NOT_GIVEN,
        saas_app: application_update_params.SaasApp | NotGiven = NOT_GIVEN,
        same_site_cookie_attribute: str | NotGiven = NOT_GIVEN,
        self_hosted_domains: List[str] | NotGiven = NOT_GIVEN,
        service_auth_401_redirect: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        skip_interstitial: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessApps:
        """
        Updates an Access application.

        Args:
          app_id: Identifier

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          allow_authenticate_via_warp: When set to true, users can authenticate to this application using their WARP
              session. When set to false this application will always require direct IdP
              authentication. This setting always overrides the organization setting for WARP
              authentication.

          allowed_idps: The identity providers your users can select when connecting to this
              application. Defaults to all IdPs configured in your account.

          auto_redirect_to_identity: When set to `true`, users skip the identity provider selection step during
              login. You must specify only one identity provider in allowed_idps.

          custom_deny_message: The custom error message shown to a user when they are denied access to the
              application.

          custom_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing identity-based rules.

          custom_non_identity_deny_url: The custom URL a user is redirected to when they are denied access to the
              application when failing non-identity rules.

          custom_pages: The custom pages that will be displayed when applicable for this application

          domain: The URL or domain of the bookmark.

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

          type: The application type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            AccessApps,
            await self._put(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
                body=await async_maybe_transform(
                    {
                        "allow_authenticate_via_warp": allow_authenticate_via_warp,
                        "allowed_idps": allowed_idps,
                        "app_launcher_visible": app_launcher_visible,
                        "auto_redirect_to_identity": auto_redirect_to_identity,
                        "cors_headers": cors_headers,
                        "custom_deny_message": custom_deny_message,
                        "custom_deny_url": custom_deny_url,
                        "custom_non_identity_deny_url": custom_non_identity_deny_url,
                        "custom_pages": custom_pages,
                        "domain": domain,
                        "enable_binding_cookie": enable_binding_cookie,
                        "http_only_cookie_attribute": http_only_cookie_attribute,
                        "logo_url": logo_url,
                        "name": name,
                        "path_cookie_attribute": path_cookie_attribute,
                        "saas_app": saas_app,
                        "same_site_cookie_attribute": same_site_cookie_attribute,
                        "self_hosted_domains": self_hosted_domains,
                        "service_auth_401_redirect": service_auth_401_redirect,
                        "session_duration": session_duration,
                        "skip_interstitial": skip_interstitial,
                        "tags": tags,
                        "type": type,
                    },
                    application_update_params.ApplicationUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccessApps]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
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
    ) -> Optional[ApplicationListResponse]:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ApplicationListResponse]], ResultWrapper[ApplicationListResponse]),
        )

    async def delete(
        self,
        app_id: Union[str, str],
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationDeleteResponse:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ApplicationDeleteResponse], ResultWrapper[ApplicationDeleteResponse]),
        )

    async def get(
        self,
        app_id: Union[str, str],
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessApps:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            AccessApps,
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
                    Any, ResultWrapper[AccessApps]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def revoke_tokens(
        self,
        app_id: Union[str, str],
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/revoke_tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class ApplicationsWithRawResponse:
    def __init__(self, applications: Applications) -> None:
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
    def cas(self) -> CAsWithRawResponse:
        return CAsWithRawResponse(self._applications.cas)

    @cached_property
    def user_policy_checks(self) -> UserPolicyChecksWithRawResponse:
        return UserPolicyChecksWithRawResponse(self._applications.user_policy_checks)

    @cached_property
    def policies(self) -> PoliciesWithRawResponse:
        return PoliciesWithRawResponse(self._applications.policies)


class AsyncApplicationsWithRawResponse:
    def __init__(self, applications: AsyncApplications) -> None:
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
    def cas(self) -> AsyncCAsWithRawResponse:
        return AsyncCAsWithRawResponse(self._applications.cas)

    @cached_property
    def user_policy_checks(self) -> AsyncUserPolicyChecksWithRawResponse:
        return AsyncUserPolicyChecksWithRawResponse(self._applications.user_policy_checks)

    @cached_property
    def policies(self) -> AsyncPoliciesWithRawResponse:
        return AsyncPoliciesWithRawResponse(self._applications.policies)


class ApplicationsWithStreamingResponse:
    def __init__(self, applications: Applications) -> None:
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
    def cas(self) -> CAsWithStreamingResponse:
        return CAsWithStreamingResponse(self._applications.cas)

    @cached_property
    def user_policy_checks(self) -> UserPolicyChecksWithStreamingResponse:
        return UserPolicyChecksWithStreamingResponse(self._applications.user_policy_checks)

    @cached_property
    def policies(self) -> PoliciesWithStreamingResponse:
        return PoliciesWithStreamingResponse(self._applications.policies)


class AsyncApplicationsWithStreamingResponse:
    def __init__(self, applications: AsyncApplications) -> None:
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
    def cas(self) -> AsyncCAsWithStreamingResponse:
        return AsyncCAsWithStreamingResponse(self._applications.cas)

    @cached_property
    def user_policy_checks(self) -> AsyncUserPolicyChecksWithStreamingResponse:
        return AsyncUserPolicyChecksWithStreamingResponse(self._applications.user_policy_checks)

    @cached_property
    def policies(self) -> AsyncPoliciesWithStreamingResponse:
        return AsyncPoliciesWithStreamingResponse(self._applications.policies)
