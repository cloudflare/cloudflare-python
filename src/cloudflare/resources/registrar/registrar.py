# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from .domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
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
from .registrations import (
    RegistrationsResource,
    AsyncRegistrationsResource,
    RegistrationsResourceWithRawResponse,
    AsyncRegistrationsResourceWithRawResponse,
    RegistrationsResourceWithStreamingResponse,
    AsyncRegistrationsResourceWithStreamingResponse,
)
from .update_status import (
    UpdateStatusResource,
    AsyncUpdateStatusResource,
    UpdateStatusResourceWithRawResponse,
    AsyncUpdateStatusResourceWithRawResponse,
    UpdateStatusResourceWithStreamingResponse,
    AsyncUpdateStatusResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.registrar import registrar_check_params, registrar_search_params
from .registration_status import (
    RegistrationStatusResource,
    AsyncRegistrationStatusResource,
    RegistrationStatusResourceWithRawResponse,
    AsyncRegistrationStatusResourceWithRawResponse,
    RegistrationStatusResourceWithStreamingResponse,
    AsyncRegistrationStatusResourceWithStreamingResponse,
)
from ...types.registrar.registrar_check_response import RegistrarCheckResponse
from ...types.registrar.registrar_search_response import RegistrarSearchResponse

__all__ = ["RegistrarResource", "AsyncRegistrarResource"]


class RegistrarResource(SyncAPIResource):
    """
    Registrar API for searching, checking, registering, and managing domains through Cloudflare Registrar.

    ## Prerequisites

    Before using this API, ensure:

    1. **Cloudflare account** — the caller must have a valid Cloudflare account.
    2. **Billing profile** — the account must have a billing profile with a valid,
      current default payment method (credit card or other accepted method).
      This cannot be set up via API — the account owner must configure billing
      at `https://dash.cloudflare.com/{account_id}/billing/payment-info` before
      calling `POST /registrations`.
    3. **API authentication** — use an API token or API key with the appropriate
      Registrar permissions for the operations you are calling.

    ## Terminology: domain extension

    Throughout this API, "extension" refers to the domain extension part of a fully
    qualified domain name — the portion after the registrable label. For example,
    in `example.co.uk`, the extension is `co.uk` (not just `uk`). This covers both
    top-level domains like `com` and multi-level extensions like `co.uk`. This is
    distinct from other uses of the word "extension" (e.g., EPP extensions).

    ## Supported extensions

    This API currently supports programmatic registration for the following
    extensions:

    `com`, `org`, `net`, `app`, `dev`, `cc`, `xyz`, `info`, `cloud`, `studio`,
    `live`, `link`, `pro`, `tech`, `fyi`, `shop`, `online`, `tools`, `run`,
    `games`, `build`, `systems`, `world`, `news`, `site`, `network`, `chat`,
    `space`, `family`, `page`, `life`, `group`, `email`, `solutions`, `day`,
    `blog`, `ing`, `icu`, `academy`, `today`

    Cloudflare Registrar supports 400+ extensions in the dashboard. Extensions
    not listed above can be registered at `https://dash.cloudflare.com/{account_id}/domains/registrations`.

    ## Typical workflow

    1. **Search** — call `GET /domain-search?q={keyword}` to discover available domains.
    2. **Check** — call `POST /domain-check` with candidate domains to verify real-time
      availability and pricing.
    3. **Review the response** — if `registrable: false`, inspect `reason` to
      understand whether the domain is unavailable, the extension is not supported
      by this API, the extension is not supported by Cloudflare Registrar at all,
      or the extension's registry has frozen new registrations.
    4. **Handle premium domains** — if `tier: premium`, premium registration is
      not currently supported by this API. Surface the premium pricing to the user,
      but do not proceed to `POST /registrations` for that domain.
    5. **Register** — call `POST /registrations` with the chosen domain name for
      supported non-premium registrations.
    6. **Confirm completion** — if the response is `201 Created`, registration
      completed within the default timeout and no polling is needed.
    7. **Poll when needed** — if the response is `202 Accepted`, poll
      `links.self` from the workflow response.
    8. **Stop for user action** — if `state: action_required`, stop polling and
      surface `context.action` to the user.
      The workflow will not resolve on its own.
    9. **Continue when blocked** — if `state: blocked`, continue polling and
      inform the user that a third party, such as the extension registry or losing
      registrar, is delaying progress.
    10. **Review failures before retrying** — if `state: failed`, review
      `error.code` and `error.message`, then decide whether user action or a new
      Check call is needed.

    **All successful domain registrations are non-refundable.** Once the registration
    workflow completes with `state: succeeded`, the charge cannot be reversed.
    Confirm pricing and domain choice with the user before calling `POST /registrations`.

    ## Default behavior for mutating operations

    By default, mutating operations such as create and update hold the connection
    for a bounded, server-defined amount of time while the operation completes.
    In most cases, the response contains a completed workflow status and no
    polling is required.

    - **Completed within the synchronous wait window:** Returns `201` (create)
    or `200` (update) with a `workflow_status` where `state: succeeded` and
    `completed: true`.
    - **Still processing after the synchronous wait window:** Returns
    `202 Accepted` with a `workflow_status` where `completed: false`. Use
    the `links.self` URL to poll for completion.

    ## Non-blocking mode

    To receive an immediate `202 Accepted` response without waiting, send the
    `Prefer: respond-async` request header (RFC 7240). The server will acknowledge
    it with a `Preference-Applied: respond-async` response header.

    ## Polling

    When the response is `202`, poll the workflow status endpoint indicated by
    `links.self` in the response body until the workflow reaches a terminal
    state or requires user action.
    """

    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def registrations(self) -> RegistrationsResource:
        return RegistrationsResource(self._client)

    @cached_property
    def registration_status(self) -> RegistrationStatusResource:
        return RegistrationStatusResource(self._client)

    @cached_property
    def update_status(self) -> UpdateStatusResource:
        return UpdateStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> RegistrarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RegistrarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegistrarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RegistrarResourceWithStreamingResponse(self)

    def check(
        self,
        *,
        account_id: str,
        domains: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistrarCheckResponse:
        """
        Performs real-time, authoritative availability checks directly against domain
        registries. Use this endpoint to verify a domain is available before attempting
        registration via `POST /registrations`.

        **Important:** Unlike the Search endpoint, these results are authoritative and
        reflect current registry status. Always check availability immediately before
        registration as domain status can change rapidly.

        **Note:** This endpoint uses POST to accept a list of domains in the request
        body. It is a read-only operation — it does not create, modify, or reserve any
        domains.

        ### Extension support

        Only domains on extensions supported for programmatic registration by this API
        can be registered. If you check a domain on an unsupported extension, the
        response will include `registrable: false` with a `reason` field explaining why:

        - `extension_not_supported_via_api` — Cloudflare Registrar supports this
          extension in the dashboard, but it is not yet available for programmatic
          registration via this API. Register via
          `https://dash.cloudflare.com/{account_id}/domains/registrations` instead.
        - `extension_not_supported` — This extension is not supported by Cloudflare
          Registrar.
        - `extension_disallows_registration` — The extension's registry has temporarily
          or permanently frozen new registrations. No registrar can register domains on
          this extension at this time.
        - `domain_premium` — The domain is premium priced. Premium registration is not
          currently supported by this API.
        - `domain_unavailable` — The domain is already registered, reserved, or
          otherwise not available for registration on a supported extension.

        The `reason` field is only present when `registrable` is `false`.

        ### Behavior

        - Maximum 20 domains per request
        - Pricing is only returned for domains where `registrable: true`
        - Results are not cached; each request queries the registry

        ### Workflow

        1. Call this endpoint with domains the user wants to register.
        2. For each domain where `registrable: true`, present pricing to the user.
        3. If `tier: premium`, note that premium registration is not currently supported
           by this API and do not proceed to `POST /registrations`.
        4. Proceed to `POST /registrations` only for supported non-premium domains.

        Args:
          account_id: Identifier

          domains: List of fully qualified domain names (FQDNs) to check for availability. Each
              domain must include the extension.

              - Minimum: 1 domain
              - Maximum: 20 domains per request
              - Domains on unsupported extensions are returned with `registrable: false` and a
                `reason` field
              - Malformed domain names (e.g., missing extension) may be omitted from the
                response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/registrar/domain-check", account_id=account_id),
            body=maybe_transform({"domains": domains}, registrar_check_params.RegistrarCheckParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegistrarCheckResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegistrarCheckResponse], ResultWrapper[RegistrarCheckResponse]),
        )

    def search(
        self,
        *,
        account_id: str,
        q: str,
        extensions: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistrarSearchResponse:
        """
        Searches for domain name suggestions based on a keyword, phrase, or partial
        domain name. Returns a list of potentially available domains with pricing
        information.

        **Important:** Results are non-authoritative and based on cached data. Always
        use the `/domain-check` endpoint to verify real-time availability before
        attempting registration.

        Suggestions are scoped to extensions supported for programmatic registration via
        this API (`POST /registrations`). Domains on unsupported extensions will not
        appear in results, even if they are available at the registry level.

        ### Use cases

        - Brand name discovery (e.g., "acme corp" → acmecorp.com, acmecorp.dev)
        - Keyword-based suggestions (e.g., "coffee shop" → coffeeshop.com,
          mycoffeeshop.net)
        - Alternative extension discovery (e.g., "example.com" → example.com,
          example.app, example.xyz)

        ### Workflow

        1. Call this endpoint with a keyword or domain name.
        2. Present suggestions to the user.
        3. Call `/domain-check` with the user's chosen domains to confirm real-time
           availability and pricing.
        4. Proceed to `POST /registrations` only for supported non-premium domains where
           the Check response returns `registrable: true`.

        **Note:** Searching with just a domain extension (e.g., "com" or ".app") is not
        supported. Provide a keyword or domain name.

        Args:
          account_id: Identifier

          q: The search term to find domain suggestions. Accepts keywords, phrases, or full
              domain names.

              - Phrases: "coffee shop" returns coffeeshop.com, mycoffeeshop.net, etc.
              - Domain names: "example.com" returns example.com and variations across
                extensions

          extensions: Limits results to specific domain extensions from the supported set. If not
              specified, returns results across all supported extensions. Extensions not in
              the supported set are silently ignored.

          limit: Maximum number of domain suggestions to return. Defaults to 20 if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/registrar/domain-search", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "extensions": extensions,
                        "limit": limit,
                    },
                    registrar_search_params.RegistrarSearchParams,
                ),
                post_parser=ResultWrapper[RegistrarSearchResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegistrarSearchResponse], ResultWrapper[RegistrarSearchResponse]),
        )


class AsyncRegistrarResource(AsyncAPIResource):
    """
    Registrar API for searching, checking, registering, and managing domains through Cloudflare Registrar.

    ## Prerequisites

    Before using this API, ensure:

    1. **Cloudflare account** — the caller must have a valid Cloudflare account.
    2. **Billing profile** — the account must have a billing profile with a valid,
      current default payment method (credit card or other accepted method).
      This cannot be set up via API — the account owner must configure billing
      at `https://dash.cloudflare.com/{account_id}/billing/payment-info` before
      calling `POST /registrations`.
    3. **API authentication** — use an API token or API key with the appropriate
      Registrar permissions for the operations you are calling.

    ## Terminology: domain extension

    Throughout this API, "extension" refers to the domain extension part of a fully
    qualified domain name — the portion after the registrable label. For example,
    in `example.co.uk`, the extension is `co.uk` (not just `uk`). This covers both
    top-level domains like `com` and multi-level extensions like `co.uk`. This is
    distinct from other uses of the word "extension" (e.g., EPP extensions).

    ## Supported extensions

    This API currently supports programmatic registration for the following
    extensions:

    `com`, `org`, `net`, `app`, `dev`, `cc`, `xyz`, `info`, `cloud`, `studio`,
    `live`, `link`, `pro`, `tech`, `fyi`, `shop`, `online`, `tools`, `run`,
    `games`, `build`, `systems`, `world`, `news`, `site`, `network`, `chat`,
    `space`, `family`, `page`, `life`, `group`, `email`, `solutions`, `day`,
    `blog`, `ing`, `icu`, `academy`, `today`

    Cloudflare Registrar supports 400+ extensions in the dashboard. Extensions
    not listed above can be registered at `https://dash.cloudflare.com/{account_id}/domains/registrations`.

    ## Typical workflow

    1. **Search** — call `GET /domain-search?q={keyword}` to discover available domains.
    2. **Check** — call `POST /domain-check` with candidate domains to verify real-time
      availability and pricing.
    3. **Review the response** — if `registrable: false`, inspect `reason` to
      understand whether the domain is unavailable, the extension is not supported
      by this API, the extension is not supported by Cloudflare Registrar at all,
      or the extension's registry has frozen new registrations.
    4. **Handle premium domains** — if `tier: premium`, premium registration is
      not currently supported by this API. Surface the premium pricing to the user,
      but do not proceed to `POST /registrations` for that domain.
    5. **Register** — call `POST /registrations` with the chosen domain name for
      supported non-premium registrations.
    6. **Confirm completion** — if the response is `201 Created`, registration
      completed within the default timeout and no polling is needed.
    7. **Poll when needed** — if the response is `202 Accepted`, poll
      `links.self` from the workflow response.
    8. **Stop for user action** — if `state: action_required`, stop polling and
      surface `context.action` to the user.
      The workflow will not resolve on its own.
    9. **Continue when blocked** — if `state: blocked`, continue polling and
      inform the user that a third party, such as the extension registry or losing
      registrar, is delaying progress.
    10. **Review failures before retrying** — if `state: failed`, review
      `error.code` and `error.message`, then decide whether user action or a new
      Check call is needed.

    **All successful domain registrations are non-refundable.** Once the registration
    workflow completes with `state: succeeded`, the charge cannot be reversed.
    Confirm pricing and domain choice with the user before calling `POST /registrations`.

    ## Default behavior for mutating operations

    By default, mutating operations such as create and update hold the connection
    for a bounded, server-defined amount of time while the operation completes.
    In most cases, the response contains a completed workflow status and no
    polling is required.

    - **Completed within the synchronous wait window:** Returns `201` (create)
    or `200` (update) with a `workflow_status` where `state: succeeded` and
    `completed: true`.
    - **Still processing after the synchronous wait window:** Returns
    `202 Accepted` with a `workflow_status` where `completed: false`. Use
    the `links.self` URL to poll for completion.

    ## Non-blocking mode

    To receive an immediate `202 Accepted` response without waiting, send the
    `Prefer: respond-async` request header (RFC 7240). The server will acknowledge
    it with a `Preference-Applied: respond-async` response header.

    ## Polling

    When the response is `202`, poll the workflow status endpoint indicated by
    `links.self` in the response body until the workflow reaches a terminal
    state or requires user action.
    """

    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def registrations(self) -> AsyncRegistrationsResource:
        return AsyncRegistrationsResource(self._client)

    @cached_property
    def registration_status(self) -> AsyncRegistrationStatusResource:
        return AsyncRegistrationStatusResource(self._client)

    @cached_property
    def update_status(self) -> AsyncUpdateStatusResource:
        return AsyncUpdateStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRegistrarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegistrarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegistrarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRegistrarResourceWithStreamingResponse(self)

    async def check(
        self,
        *,
        account_id: str,
        domains: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistrarCheckResponse:
        """
        Performs real-time, authoritative availability checks directly against domain
        registries. Use this endpoint to verify a domain is available before attempting
        registration via `POST /registrations`.

        **Important:** Unlike the Search endpoint, these results are authoritative and
        reflect current registry status. Always check availability immediately before
        registration as domain status can change rapidly.

        **Note:** This endpoint uses POST to accept a list of domains in the request
        body. It is a read-only operation — it does not create, modify, or reserve any
        domains.

        ### Extension support

        Only domains on extensions supported for programmatic registration by this API
        can be registered. If you check a domain on an unsupported extension, the
        response will include `registrable: false` with a `reason` field explaining why:

        - `extension_not_supported_via_api` — Cloudflare Registrar supports this
          extension in the dashboard, but it is not yet available for programmatic
          registration via this API. Register via
          `https://dash.cloudflare.com/{account_id}/domains/registrations` instead.
        - `extension_not_supported` — This extension is not supported by Cloudflare
          Registrar.
        - `extension_disallows_registration` — The extension's registry has temporarily
          or permanently frozen new registrations. No registrar can register domains on
          this extension at this time.
        - `domain_premium` — The domain is premium priced. Premium registration is not
          currently supported by this API.
        - `domain_unavailable` — The domain is already registered, reserved, or
          otherwise not available for registration on a supported extension.

        The `reason` field is only present when `registrable` is `false`.

        ### Behavior

        - Maximum 20 domains per request
        - Pricing is only returned for domains where `registrable: true`
        - Results are not cached; each request queries the registry

        ### Workflow

        1. Call this endpoint with domains the user wants to register.
        2. For each domain where `registrable: true`, present pricing to the user.
        3. If `tier: premium`, note that premium registration is not currently supported
           by this API and do not proceed to `POST /registrations`.
        4. Proceed to `POST /registrations` only for supported non-premium domains.

        Args:
          account_id: Identifier

          domains: List of fully qualified domain names (FQDNs) to check for availability. Each
              domain must include the extension.

              - Minimum: 1 domain
              - Maximum: 20 domains per request
              - Domains on unsupported extensions are returned with `registrable: false` and a
                `reason` field
              - Malformed domain names (e.g., missing extension) may be omitted from the
                response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/registrar/domain-check", account_id=account_id),
            body=await async_maybe_transform({"domains": domains}, registrar_check_params.RegistrarCheckParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegistrarCheckResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegistrarCheckResponse], ResultWrapper[RegistrarCheckResponse]),
        )

    async def search(
        self,
        *,
        account_id: str,
        q: str,
        extensions: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegistrarSearchResponse:
        """
        Searches for domain name suggestions based on a keyword, phrase, or partial
        domain name. Returns a list of potentially available domains with pricing
        information.

        **Important:** Results are non-authoritative and based on cached data. Always
        use the `/domain-check` endpoint to verify real-time availability before
        attempting registration.

        Suggestions are scoped to extensions supported for programmatic registration via
        this API (`POST /registrations`). Domains on unsupported extensions will not
        appear in results, even if they are available at the registry level.

        ### Use cases

        - Brand name discovery (e.g., "acme corp" → acmecorp.com, acmecorp.dev)
        - Keyword-based suggestions (e.g., "coffee shop" → coffeeshop.com,
          mycoffeeshop.net)
        - Alternative extension discovery (e.g., "example.com" → example.com,
          example.app, example.xyz)

        ### Workflow

        1. Call this endpoint with a keyword or domain name.
        2. Present suggestions to the user.
        3. Call `/domain-check` with the user's chosen domains to confirm real-time
           availability and pricing.
        4. Proceed to `POST /registrations` only for supported non-premium domains where
           the Check response returns `registrable: true`.

        **Note:** Searching with just a domain extension (e.g., "com" or ".app") is not
        supported. Provide a keyword or domain name.

        Args:
          account_id: Identifier

          q: The search term to find domain suggestions. Accepts keywords, phrases, or full
              domain names.

              - Phrases: "coffee shop" returns coffeeshop.com, mycoffeeshop.net, etc.
              - Domain names: "example.com" returns example.com and variations across
                extensions

          extensions: Limits results to specific domain extensions from the supported set. If not
              specified, returns results across all supported extensions. Extensions not in
              the supported set are silently ignored.

          limit: Maximum number of domain suggestions to return. Defaults to 20 if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/registrar/domain-search", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "extensions": extensions,
                        "limit": limit,
                    },
                    registrar_search_params.RegistrarSearchParams,
                ),
                post_parser=ResultWrapper[RegistrarSearchResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegistrarSearchResponse], ResultWrapper[RegistrarSearchResponse]),
        )


class RegistrarResourceWithRawResponse:
    def __init__(self, registrar: RegistrarResource) -> None:
        self._registrar = registrar

        self.check = to_raw_response_wrapper(
            registrar.check,
        )
        self.search = to_raw_response_wrapper(
            registrar.search,
        )

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._registrar.domains)

    @cached_property
    def registrations(self) -> RegistrationsResourceWithRawResponse:
        return RegistrationsResourceWithRawResponse(self._registrar.registrations)

    @cached_property
    def registration_status(self) -> RegistrationStatusResourceWithRawResponse:
        return RegistrationStatusResourceWithRawResponse(self._registrar.registration_status)

    @cached_property
    def update_status(self) -> UpdateStatusResourceWithRawResponse:
        return UpdateStatusResourceWithRawResponse(self._registrar.update_status)


class AsyncRegistrarResourceWithRawResponse:
    def __init__(self, registrar: AsyncRegistrarResource) -> None:
        self._registrar = registrar

        self.check = async_to_raw_response_wrapper(
            registrar.check,
        )
        self.search = async_to_raw_response_wrapper(
            registrar.search,
        )

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._registrar.domains)

    @cached_property
    def registrations(self) -> AsyncRegistrationsResourceWithRawResponse:
        return AsyncRegistrationsResourceWithRawResponse(self._registrar.registrations)

    @cached_property
    def registration_status(self) -> AsyncRegistrationStatusResourceWithRawResponse:
        return AsyncRegistrationStatusResourceWithRawResponse(self._registrar.registration_status)

    @cached_property
    def update_status(self) -> AsyncUpdateStatusResourceWithRawResponse:
        return AsyncUpdateStatusResourceWithRawResponse(self._registrar.update_status)


class RegistrarResourceWithStreamingResponse:
    def __init__(self, registrar: RegistrarResource) -> None:
        self._registrar = registrar

        self.check = to_streamed_response_wrapper(
            registrar.check,
        )
        self.search = to_streamed_response_wrapper(
            registrar.search,
        )

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._registrar.domains)

    @cached_property
    def registrations(self) -> RegistrationsResourceWithStreamingResponse:
        return RegistrationsResourceWithStreamingResponse(self._registrar.registrations)

    @cached_property
    def registration_status(self) -> RegistrationStatusResourceWithStreamingResponse:
        return RegistrationStatusResourceWithStreamingResponse(self._registrar.registration_status)

    @cached_property
    def update_status(self) -> UpdateStatusResourceWithStreamingResponse:
        return UpdateStatusResourceWithStreamingResponse(self._registrar.update_status)


class AsyncRegistrarResourceWithStreamingResponse:
    def __init__(self, registrar: AsyncRegistrarResource) -> None:
        self._registrar = registrar

        self.check = async_to_streamed_response_wrapper(
            registrar.check,
        )
        self.search = async_to_streamed_response_wrapper(
            registrar.search,
        )

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._registrar.domains)

    @cached_property
    def registrations(self) -> AsyncRegistrationsResourceWithStreamingResponse:
        return AsyncRegistrationsResourceWithStreamingResponse(self._registrar.registrations)

    @cached_property
    def registration_status(self) -> AsyncRegistrationStatusResourceWithStreamingResponse:
        return AsyncRegistrationStatusResourceWithStreamingResponse(self._registrar.registration_status)

    @cached_property
    def update_status(self) -> AsyncUpdateStatusResourceWithStreamingResponse:
        return AsyncUpdateStatusResourceWithStreamingResponse(self._registrar.update_status)
