# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.iam import oauth_client_create_params, oauth_client_update_params
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.iam.oauth_client_get_response import OAuthClientGetResponse
from ...types.iam.oauth_client_list_response import OAuthClientListResponse
from ...types.iam.oauth_client_create_response import OAuthClientCreateResponse
from ...types.iam.oauth_client_delete_response import OAuthClientDeleteResponse
from ...types.iam.oauth_client_update_response import OAuthClientUpdateResponse
from ...types.iam.oauth_client_rotate_secret_response import OAuthClientRotateSecretResponse
from ...types.iam.oauth_client_delete_rotated_secret_response import OAuthClientDeleteRotatedSecretResponse

__all__ = ["OAuthClientsResource", "AsyncOAuthClientsResource"]


class OAuthClientsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OAuthClientsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OAuthClientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthClientsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OAuthClientsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        client_name: str,
        grant_types: List[Literal["authorization_code", "refresh_token"]],
        redirect_uris: SequenceNotStr[str],
        response_types: List[Literal["token", "id_token", "code"]],
        scopes: SequenceNotStr[str],
        token_endpoint_auth_method: Literal["none", "client_secret_basic", "client_secret_post"],
        allowed_cors_origins: SequenceNotStr[str] | Omit = omit,
        client_uri: str | Omit = omit,
        logo_uri: str | Omit = omit,
        policy_uri: str | Omit = omit,
        post_logout_redirect_uris: SequenceNotStr[str] | Omit = omit,
        tos_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OAuthClientCreateResponse]:
        """
        Create a new OAuth client for an account.

        Args:
          account_id: Account identifier tag.

          client_name: Human-readable name of the OAuth client.

          grant_types: Array of OAuth grant types the client is allowed to use. `authorization_code` is
              required; `refresh_token` may be included optionally.

          redirect_uris: Array of allowed redirect URIs for the client.

          response_types: Array of OAuth response types the client is allowed to use.

          scopes: Array of OAuth scopes the client is allowed to request. Colon-delimited scopes
              are not accepted. Dot-delimited scopes are validated against available OAuth API
              scopes; simple identity scopes are allowed. Protocol scopes `offline_access` and
              `openid` are added or removed automatically based on `grant_types` and
              `response_types`.

          token_endpoint_auth_method: The authentication method the client uses at the token endpoint.

          allowed_cors_origins: Array of allowed CORS origins.

          client_uri: URL of the home page of the client.

          logo_uri: URL of the client's logo.

          policy_uri: URL that points to a privacy policy document.

          post_logout_redirect_uris: Array of allowed post-logout redirect URIs.

          tos_uri: URL that points to a terms of service document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/oauth_clients", account_id=account_id),
            body=maybe_transform(
                {
                    "client_name": client_name,
                    "grant_types": grant_types,
                    "redirect_uris": redirect_uris,
                    "response_types": response_types,
                    "scopes": scopes,
                    "token_endpoint_auth_method": token_endpoint_auth_method,
                    "allowed_cors_origins": allowed_cors_origins,
                    "client_uri": client_uri,
                    "logo_uri": logo_uri,
                    "policy_uri": policy_uri,
                    "post_logout_redirect_uris": post_logout_redirect_uris,
                    "tos_uri": tos_uri,
                },
                oauth_client_create_params.OAuthClientCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OAuthClientCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OAuthClientCreateResponse]], ResultWrapper[OAuthClientCreateResponse]),
        )

    def update(
        self,
        oauth_client_id: str,
        *,
        account_id: str,
        allowed_cors_origins: SequenceNotStr[str] | Omit = omit,
        client_name: str | Omit = omit,
        client_uri: str | Omit = omit,
        grant_types: List[Literal["authorization_code", "refresh_token"]] | Omit = omit,
        logo_uri: str | Omit = omit,
        policy_uri: str | Omit = omit,
        post_logout_redirect_uris: SequenceNotStr[str] | Omit = omit,
        redirect_uris: SequenceNotStr[str] | Omit = omit,
        response_types: List[Literal["token", "id_token", "code"]] | Omit = omit,
        scopes: SequenceNotStr[str] | Omit = omit,
        token_endpoint_auth_method: Literal["none", "client_secret_basic", "client_secret_post"] | Omit = omit,
        tos_uri: str | Omit = omit,
        visibility: Literal["public"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OAuthClientUpdateResponse]:
        """Update an existing OAuth client.

        Only include fields you want to update.

        Args:
          account_id: Account identifier tag.

          oauth_client_id: The unique identifier for an OAuth client.

          allowed_cors_origins: Array of allowed CORS origins.

          client_name: Human-readable name of the OAuth client.

          client_uri: URL of the home page of the client.

          grant_types: Array of OAuth grant types the client is allowed to use. `authorization_code` is
              required; `refresh_token` may be included optionally.

          logo_uri: URL of the client's logo.

          policy_uri: URL that points to a privacy policy document.

          post_logout_redirect_uris: Array of allowed post-logout redirect URIs.

          redirect_uris: Array of allowed redirect URIs for the client.

          response_types: Array of OAuth response types the client is allowed to use.

          scopes: Array of OAuth scopes the client is allowed to request. Colon-delimited scopes
              are not accepted. Dot-delimited scopes are validated against available OAuth API
              scopes; simple identity scopes are allowed. Protocol scopes `offline_access` and
              `openid` are added or removed automatically based on `grant_types` and
              `response_types`.

          token_endpoint_auth_method: The authentication method the client uses at the token endpoint.

          tos_uri: URL that points to a terms of service document.

          visibility: Promote the OAuth client from private to public visibility. Only `public` is
              accepted; demotion to `private` is not supported. Promotion requires a non-empty
              client name, logo URI, verified client URI host, and at least one non-identity
              scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not oauth_client_id:
            raise ValueError(f"Expected a non-empty value for `oauth_client_id` but received {oauth_client_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/oauth_clients/{oauth_client_id}",
                account_id=account_id,
                oauth_client_id=oauth_client_id,
            ),
            body=maybe_transform(
                {
                    "allowed_cors_origins": allowed_cors_origins,
                    "client_name": client_name,
                    "client_uri": client_uri,
                    "grant_types": grant_types,
                    "logo_uri": logo_uri,
                    "policy_uri": policy_uri,
                    "post_logout_redirect_uris": post_logout_redirect_uris,
                    "redirect_uris": redirect_uris,
                    "response_types": response_types,
                    "scopes": scopes,
                    "token_endpoint_auth_method": token_endpoint_auth_method,
                    "tos_uri": tos_uri,
                    "visibility": visibility,
                },
                oauth_client_update_params.OAuthClientUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OAuthClientUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OAuthClientUpdateResponse]], ResultWrapper[OAuthClientUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[OAuthClientListResponse]:
        """
        List all OAuth clients for an account.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/oauth_clients", account_id=account_id),
            page=SyncSinglePage[OAuthClientListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=OAuthClientListResponse,
        )

    def delete(
        self,
        oauth_client_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OAuthClientDeleteResponse]:
        """
        Delete an OAuth client.

        Args:
          account_id: Account identifier tag.

          oauth_client_id: The unique identifier for an OAuth client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not oauth_client_id:
            raise ValueError(f"Expected a non-empty value for `oauth_client_id` but received {oauth_client_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/oauth_clients/{oauth_client_id}",
                account_id=account_id,
                oauth_client_id=oauth_client_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OAuthClientDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OAuthClientDeleteResponse]], ResultWrapper[OAuthClientDeleteResponse]),
        )

    def delete_rotated_secret(
        self,
        oauth_client_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OAuthClientDeleteRotatedSecretResponse]:
        """Removes the old client secret after a rotation, keeping only the new one.

        Use
        this after you have updated your client configuration to use the new secret. The
        `has_rotated_secret` field on the client indicates whether there is an old
        secret to delete.

        Args:
          account_id: Account identifier tag.

          oauth_client_id: The unique identifier for an OAuth client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not oauth_client_id:
            raise ValueError(f"Expected a non-empty value for `oauth_client_id` but received {oauth_client_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/oauth_clients/{oauth_client_id}/rotate_secret",
                account_id=account_id,
                oauth_client_id=oauth_client_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OAuthClientDeleteRotatedSecretResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OAuthClientDeleteRotatedSecretResponse]],
                ResultWrapper[OAuthClientDeleteRotatedSecretResponse],
            ),
        )

    def get(
        self,
        oauth_client_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OAuthClientGetResponse]:
        """
        Get details of a specific OAuth client.

        Args:
          account_id: Account identifier tag.

          oauth_client_id: The unique identifier for an OAuth client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not oauth_client_id:
            raise ValueError(f"Expected a non-empty value for `oauth_client_id` but received {oauth_client_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/oauth_clients/{oauth_client_id}",
                account_id=account_id,
                oauth_client_id=oauth_client_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OAuthClientGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OAuthClientGetResponse]], ResultWrapper[OAuthClientGetResponse]),
        )

    def rotate_secret(
        self,
        oauth_client_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OAuthClientRotateSecretResponse]:
        """
        Creates a second client secret so you can update your client configuration
        before deleting the old one. The `has_rotated_secret` field on the client will
        be set to `true`.

        Args:
          account_id: Account identifier tag.

          oauth_client_id: The unique identifier for an OAuth client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not oauth_client_id:
            raise ValueError(f"Expected a non-empty value for `oauth_client_id` but received {oauth_client_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/oauth_clients/{oauth_client_id}/rotate_secret",
                account_id=account_id,
                oauth_client_id=oauth_client_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OAuthClientRotateSecretResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OAuthClientRotateSecretResponse]], ResultWrapper[OAuthClientRotateSecretResponse]
            ),
        )


class AsyncOAuthClientsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOAuthClientsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOAuthClientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthClientsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOAuthClientsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        client_name: str,
        grant_types: List[Literal["authorization_code", "refresh_token"]],
        redirect_uris: SequenceNotStr[str],
        response_types: List[Literal["token", "id_token", "code"]],
        scopes: SequenceNotStr[str],
        token_endpoint_auth_method: Literal["none", "client_secret_basic", "client_secret_post"],
        allowed_cors_origins: SequenceNotStr[str] | Omit = omit,
        client_uri: str | Omit = omit,
        logo_uri: str | Omit = omit,
        policy_uri: str | Omit = omit,
        post_logout_redirect_uris: SequenceNotStr[str] | Omit = omit,
        tos_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OAuthClientCreateResponse]:
        """
        Create a new OAuth client for an account.

        Args:
          account_id: Account identifier tag.

          client_name: Human-readable name of the OAuth client.

          grant_types: Array of OAuth grant types the client is allowed to use. `authorization_code` is
              required; `refresh_token` may be included optionally.

          redirect_uris: Array of allowed redirect URIs for the client.

          response_types: Array of OAuth response types the client is allowed to use.

          scopes: Array of OAuth scopes the client is allowed to request. Colon-delimited scopes
              are not accepted. Dot-delimited scopes are validated against available OAuth API
              scopes; simple identity scopes are allowed. Protocol scopes `offline_access` and
              `openid` are added or removed automatically based on `grant_types` and
              `response_types`.

          token_endpoint_auth_method: The authentication method the client uses at the token endpoint.

          allowed_cors_origins: Array of allowed CORS origins.

          client_uri: URL of the home page of the client.

          logo_uri: URL of the client's logo.

          policy_uri: URL that points to a privacy policy document.

          post_logout_redirect_uris: Array of allowed post-logout redirect URIs.

          tos_uri: URL that points to a terms of service document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/oauth_clients", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "client_name": client_name,
                    "grant_types": grant_types,
                    "redirect_uris": redirect_uris,
                    "response_types": response_types,
                    "scopes": scopes,
                    "token_endpoint_auth_method": token_endpoint_auth_method,
                    "allowed_cors_origins": allowed_cors_origins,
                    "client_uri": client_uri,
                    "logo_uri": logo_uri,
                    "policy_uri": policy_uri,
                    "post_logout_redirect_uris": post_logout_redirect_uris,
                    "tos_uri": tos_uri,
                },
                oauth_client_create_params.OAuthClientCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OAuthClientCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OAuthClientCreateResponse]], ResultWrapper[OAuthClientCreateResponse]),
        )

    async def update(
        self,
        oauth_client_id: str,
        *,
        account_id: str,
        allowed_cors_origins: SequenceNotStr[str] | Omit = omit,
        client_name: str | Omit = omit,
        client_uri: str | Omit = omit,
        grant_types: List[Literal["authorization_code", "refresh_token"]] | Omit = omit,
        logo_uri: str | Omit = omit,
        policy_uri: str | Omit = omit,
        post_logout_redirect_uris: SequenceNotStr[str] | Omit = omit,
        redirect_uris: SequenceNotStr[str] | Omit = omit,
        response_types: List[Literal["token", "id_token", "code"]] | Omit = omit,
        scopes: SequenceNotStr[str] | Omit = omit,
        token_endpoint_auth_method: Literal["none", "client_secret_basic", "client_secret_post"] | Omit = omit,
        tos_uri: str | Omit = omit,
        visibility: Literal["public"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OAuthClientUpdateResponse]:
        """Update an existing OAuth client.

        Only include fields you want to update.

        Args:
          account_id: Account identifier tag.

          oauth_client_id: The unique identifier for an OAuth client.

          allowed_cors_origins: Array of allowed CORS origins.

          client_name: Human-readable name of the OAuth client.

          client_uri: URL of the home page of the client.

          grant_types: Array of OAuth grant types the client is allowed to use. `authorization_code` is
              required; `refresh_token` may be included optionally.

          logo_uri: URL of the client's logo.

          policy_uri: URL that points to a privacy policy document.

          post_logout_redirect_uris: Array of allowed post-logout redirect URIs.

          redirect_uris: Array of allowed redirect URIs for the client.

          response_types: Array of OAuth response types the client is allowed to use.

          scopes: Array of OAuth scopes the client is allowed to request. Colon-delimited scopes
              are not accepted. Dot-delimited scopes are validated against available OAuth API
              scopes; simple identity scopes are allowed. Protocol scopes `offline_access` and
              `openid` are added or removed automatically based on `grant_types` and
              `response_types`.

          token_endpoint_auth_method: The authentication method the client uses at the token endpoint.

          tos_uri: URL that points to a terms of service document.

          visibility: Promote the OAuth client from private to public visibility. Only `public` is
              accepted; demotion to `private` is not supported. Promotion requires a non-empty
              client name, logo URI, verified client URI host, and at least one non-identity
              scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not oauth_client_id:
            raise ValueError(f"Expected a non-empty value for `oauth_client_id` but received {oauth_client_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/oauth_clients/{oauth_client_id}",
                account_id=account_id,
                oauth_client_id=oauth_client_id,
            ),
            body=await async_maybe_transform(
                {
                    "allowed_cors_origins": allowed_cors_origins,
                    "client_name": client_name,
                    "client_uri": client_uri,
                    "grant_types": grant_types,
                    "logo_uri": logo_uri,
                    "policy_uri": policy_uri,
                    "post_logout_redirect_uris": post_logout_redirect_uris,
                    "redirect_uris": redirect_uris,
                    "response_types": response_types,
                    "scopes": scopes,
                    "token_endpoint_auth_method": token_endpoint_auth_method,
                    "tos_uri": tos_uri,
                    "visibility": visibility,
                },
                oauth_client_update_params.OAuthClientUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OAuthClientUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OAuthClientUpdateResponse]], ResultWrapper[OAuthClientUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[OAuthClientListResponse, AsyncSinglePage[OAuthClientListResponse]]:
        """
        List all OAuth clients for an account.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/oauth_clients", account_id=account_id),
            page=AsyncSinglePage[OAuthClientListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=OAuthClientListResponse,
        )

    async def delete(
        self,
        oauth_client_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OAuthClientDeleteResponse]:
        """
        Delete an OAuth client.

        Args:
          account_id: Account identifier tag.

          oauth_client_id: The unique identifier for an OAuth client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not oauth_client_id:
            raise ValueError(f"Expected a non-empty value for `oauth_client_id` but received {oauth_client_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/oauth_clients/{oauth_client_id}",
                account_id=account_id,
                oauth_client_id=oauth_client_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OAuthClientDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OAuthClientDeleteResponse]], ResultWrapper[OAuthClientDeleteResponse]),
        )

    async def delete_rotated_secret(
        self,
        oauth_client_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OAuthClientDeleteRotatedSecretResponse]:
        """Removes the old client secret after a rotation, keeping only the new one.

        Use
        this after you have updated your client configuration to use the new secret. The
        `has_rotated_secret` field on the client indicates whether there is an old
        secret to delete.

        Args:
          account_id: Account identifier tag.

          oauth_client_id: The unique identifier for an OAuth client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not oauth_client_id:
            raise ValueError(f"Expected a non-empty value for `oauth_client_id` but received {oauth_client_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/oauth_clients/{oauth_client_id}/rotate_secret",
                account_id=account_id,
                oauth_client_id=oauth_client_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OAuthClientDeleteRotatedSecretResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OAuthClientDeleteRotatedSecretResponse]],
                ResultWrapper[OAuthClientDeleteRotatedSecretResponse],
            ),
        )

    async def get(
        self,
        oauth_client_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OAuthClientGetResponse]:
        """
        Get details of a specific OAuth client.

        Args:
          account_id: Account identifier tag.

          oauth_client_id: The unique identifier for an OAuth client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not oauth_client_id:
            raise ValueError(f"Expected a non-empty value for `oauth_client_id` but received {oauth_client_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/oauth_clients/{oauth_client_id}",
                account_id=account_id,
                oauth_client_id=oauth_client_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OAuthClientGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OAuthClientGetResponse]], ResultWrapper[OAuthClientGetResponse]),
        )

    async def rotate_secret(
        self,
        oauth_client_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OAuthClientRotateSecretResponse]:
        """
        Creates a second client secret so you can update your client configuration
        before deleting the old one. The `has_rotated_secret` field on the client will
        be set to `true`.

        Args:
          account_id: Account identifier tag.

          oauth_client_id: The unique identifier for an OAuth client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not oauth_client_id:
            raise ValueError(f"Expected a non-empty value for `oauth_client_id` but received {oauth_client_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/oauth_clients/{oauth_client_id}/rotate_secret",
                account_id=account_id,
                oauth_client_id=oauth_client_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OAuthClientRotateSecretResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OAuthClientRotateSecretResponse]], ResultWrapper[OAuthClientRotateSecretResponse]
            ),
        )


class OAuthClientsResourceWithRawResponse:
    def __init__(self, oauth_clients: OAuthClientsResource) -> None:
        self._oauth_clients = oauth_clients

        self.create = to_raw_response_wrapper(
            oauth_clients.create,
        )
        self.update = to_raw_response_wrapper(
            oauth_clients.update,
        )
        self.list = to_raw_response_wrapper(
            oauth_clients.list,
        )
        self.delete = to_raw_response_wrapper(
            oauth_clients.delete,
        )
        self.delete_rotated_secret = to_raw_response_wrapper(
            oauth_clients.delete_rotated_secret,
        )
        self.get = to_raw_response_wrapper(
            oauth_clients.get,
        )
        self.rotate_secret = to_raw_response_wrapper(
            oauth_clients.rotate_secret,
        )


class AsyncOAuthClientsResourceWithRawResponse:
    def __init__(self, oauth_clients: AsyncOAuthClientsResource) -> None:
        self._oauth_clients = oauth_clients

        self.create = async_to_raw_response_wrapper(
            oauth_clients.create,
        )
        self.update = async_to_raw_response_wrapper(
            oauth_clients.update,
        )
        self.list = async_to_raw_response_wrapper(
            oauth_clients.list,
        )
        self.delete = async_to_raw_response_wrapper(
            oauth_clients.delete,
        )
        self.delete_rotated_secret = async_to_raw_response_wrapper(
            oauth_clients.delete_rotated_secret,
        )
        self.get = async_to_raw_response_wrapper(
            oauth_clients.get,
        )
        self.rotate_secret = async_to_raw_response_wrapper(
            oauth_clients.rotate_secret,
        )


class OAuthClientsResourceWithStreamingResponse:
    def __init__(self, oauth_clients: OAuthClientsResource) -> None:
        self._oauth_clients = oauth_clients

        self.create = to_streamed_response_wrapper(
            oauth_clients.create,
        )
        self.update = to_streamed_response_wrapper(
            oauth_clients.update,
        )
        self.list = to_streamed_response_wrapper(
            oauth_clients.list,
        )
        self.delete = to_streamed_response_wrapper(
            oauth_clients.delete,
        )
        self.delete_rotated_secret = to_streamed_response_wrapper(
            oauth_clients.delete_rotated_secret,
        )
        self.get = to_streamed_response_wrapper(
            oauth_clients.get,
        )
        self.rotate_secret = to_streamed_response_wrapper(
            oauth_clients.rotate_secret,
        )


class AsyncOAuthClientsResourceWithStreamingResponse:
    def __init__(self, oauth_clients: AsyncOAuthClientsResource) -> None:
        self._oauth_clients = oauth_clients

        self.create = async_to_streamed_response_wrapper(
            oauth_clients.create,
        )
        self.update = async_to_streamed_response_wrapper(
            oauth_clients.update,
        )
        self.list = async_to_streamed_response_wrapper(
            oauth_clients.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            oauth_clients.delete,
        )
        self.delete_rotated_secret = async_to_streamed_response_wrapper(
            oauth_clients.delete_rotated_secret,
        )
        self.get = async_to_streamed_response_wrapper(
            oauth_clients.get,
        )
        self.rotate_secret = async_to_streamed_response_wrapper(
            oauth_clients.rotate_secret,
        )
