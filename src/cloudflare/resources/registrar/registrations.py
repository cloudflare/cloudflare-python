# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import is_given, path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncCursorPagination, AsyncCursorPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.registrar import registration_edit_params, registration_list_params, registration_create_params
from ...types.registrar.registration import Registration
from ...types.registrar.workflow_status import WorkflowStatus

__all__ = ["RegistrationsResource", "AsyncRegistrationsResource"]


class RegistrationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegistrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RegistrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegistrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RegistrationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        domain_name: str,
        acknowledgements: Dict[str, object] | Omit = omit,
        auto_renew: bool | Omit = omit,
        contact_extensions: Dict[str, object] | Omit = omit,
        contacts: registration_create_params.Contacts | Omit = omit,
        privacy_mode: Literal["off", "redaction"] | Omit = omit,
        years: int | Omit = omit,
        prefer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowStatus:
        """Starts a domain registration workflow.

        This is a billable operation — successful
        registration charges the account's default payment method. All successful domain
        registrations are non-refundable — once the workflow completes with
        `state: succeeded`, the charge cannot be reversed.

        ### Prerequisites

        - The account must have a billing profile with a valid default payment method.
          Set this up at
          `https://dash.cloudflare.com/{account_id}/billing/payment-info`.
        - The account must not already be at the maximum supported domain limit. A
          single account may own up to 500 domains in total across registrations created
          through either the dashboard or this API.
        - The domain must be on a supported extension for programmatic registration.
        - Use `POST /domain-check` immediately before calling this endpoint to confirm
          real-time availability and pricing.

        ### Express mode

        The only required field is `domain_name`. If `contacts` is omitted, the system
        uses the account's default address book entry as the registrant. If no default
        exists and no contact is provided, the request fails. Set up a default address
        book entry and accept the required agreement at
        `https://dash.cloudflare.com/{account_id}/domains/registrations`.

        ### Defaults

        - `years`: defaults to the extension's minimum registration period (1 year for
          most extensions, but varies — for example, `.ai` (if supported) requires a
          minimum of 2 years).
        - `auto_renew`: defaults to `false`. Setting it to `true` is an explicit opt-in
          authorizing Cloudflare to charge the account's default payment method up to 30
          days before domain expiry to renew the registration. Renewal pricing may
          change over time based on registry pricing.
        - `privacy_mode`: defaults to `redaction`.

        ### Premium domains

        Premium domain registration is not currently supported by this API. If
        `POST /domain-check` returns `tier: premium`, do not call this endpoint for that
        domain.

        ### Response behavior

        By default, the server holds the connection for a bounded, server-defined amount
        of time while the registration completes. Most registrations finish within this
        window and return `201 Created` with a completed workflow status.

        If the registration is still processing after this synchronous wait window, the
        server returns `202 Accepted`. Poll the URL in `links.self` to track progress.

        To skip the wait and receive an immediate `202`, send `Prefer: respond-async`.

        Args:
          account_id: Identifier.

          domain_name: Provides a fully qualified domain name (FQDN), including the extension (e.g.,
              `example.com`, `mybrand.app`). The domain name uniquely identifies a
              registration. Cloudflare permits only one registration per domain, making the
              domain name a natural idempotency key for registration requests.

          acknowledgements: Provides user acknowledgements for a specific extension or premium registration
              flow. The extension registration schema from the extension discovery endpoint
              identifies the required keys.

          auto_renew: Enable or disable automatic renewal. Defaults to `false` if omitted. Setting
              this field to `true` is an explicit opt-in authorizing Cloudflare to charge the
              account's default payment method up to 30 days before domain expiry to renew the
              domain automatically. Renewal pricing may change over time based on registry
              pricing.

          contact_extensions: Provides registry-specific contact extension values for the registrant.
              `GET /accounts/{account_id}/registrar/extensions/{extension}` identifies the
              required keys and allowed values for each extension in the
              `registration_schema.properties.contact_extensions` object.

              Examples include `.us` nexus fields, `.uk` registrant type fields, and `.ca`
              legal type fields. Omit this object when the extension's registration schema
              excludes `contact_extensions`.

          contacts: Provides contact data for the registration request.

              The per-extension schema from
              `GET /accounts/{account_id}/registrar/extensions/{extension}` defines the
              accepted contact roles. Every currently supported extension requires only
              `contacts.registrant` from API callers. Callers may provide additional roles
              such as `technical`, `administrator`, and `billing` when the extension schema
              includes them. When a registry requires an omitted role, Cloudflare may derive
              that contact from `contacts.registrant`.

              When the request omits either the entire `contacts` object or
              `contacts.registrant`, the system uses the account's default address book entry
              as the registrant contact. The account owner must configure this default at
              `https://dash.cloudflare.com/{account_id}/domains/registrations`, where they can
              create or update the address book entry and accept the required agreement.
              Dashboard settings currently provide the only way to manage address book
              entries.

              Without either a default address book entry or a registrant contact, the
              registration request fails validation.

          privacy_mode: Sets the WHOIS privacy mode for the registration. Defaults to `redaction`.

              - `off`: Disables WHOIS privacy.
              - `redaction`: Requests WHOIS redaction where the extension supports it. Some
                extensions exclude privacy and redaction.

          years: Sets the registration term from 1 to 10 years. When omitted, this field defaults
              to the registry's minimum registration period for the extension. Most extensions
              require 1 year, while some require longer minimum terms (e.g., `.ai` requires 2
              years).

              Each registry may also enforce its own maximum registration term. A request
              above that maximum fails. When uncertain, omit this field to use the default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {**strip_not_given({"Prefer": prefer}), **(extra_headers or {})}
        return self._post(
            path_template("/accounts/{account_id}/registrar/registrations", account_id=account_id),
            body=maybe_transform(
                {
                    "domain_name": domain_name,
                    "acknowledgements": acknowledgements,
                    "auto_renew": auto_renew,
                    "contact_extensions": contact_extensions,
                    "contacts": contacts,
                    "privacy_mode": privacy_mode,
                    "years": years,
                },
                registration_create_params.RegistrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WorkflowStatus]._unwrapper,
            ),
            cast_to=cast(Type[WorkflowStatus], ResultWrapper[WorkflowStatus]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        per_page: int | Omit = omit,
        sort_by: Literal["registry_created_at", "registry_expires_at", "name"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[Registration]:
        """
        Returns a paginated list of domain registrations owned by the account.

        This endpoint uses cursor-based pagination. Results are ordered by registration
        date by default. To fetch the next page, pass the `cursor` value from the
        `result_info` object in the response as the `cursor` query parameter in your
        next request. An empty `cursor` string indicates there are no more pages.

        Args:
          account_id: Identifier.

          cursor: Opaque token from a previous response's `result_info.cursor`. Pass this value to
              fetch the next page of results. Omit (or pass an empty string) for the first
              page.

          direction: Sort direction for results. Defaults to ascending order.

          per_page: Number of items to return per page.

          sort_by: Column to sort results by. Defaults to registration date (`registry_created_at`)
              when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/registrar/registrations", account_id=account_id),
            page=SyncCursorPagination[Registration],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "per_page": per_page,
                        "sort_by": sort_by,
                    },
                    registration_list_params.RegistrationListParams,
                ),
            ),
            model=Registration,
        )

    def edit(
        self,
        domain_name: str,
        *,
        account_id: str,
        auto_renew: bool | Omit = omit,
        prefer: Literal["respond-async"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowStatus:
        """
        Updates an existing domain registration.

        By default, the server holds the connection for a bounded, server-defined amount
        of time while the update completes. Most updates finish within this window and
        return `200 OK` with a completed workflow status.

        If the update is still processing after this synchronous wait window, the server
        returns `202 Accepted`. Poll the URL in `links.self` to track progress.

        To skip the wait and receive an immediate `202`, send `Prefer: respond-async`.

        This endpoint currently supports updating `auto_renew` only.

        Args:
          account_id: Identifier.

          domain_name: Provides a fully qualified domain name (FQDN), including the extension (e.g.,
              `example.com`, `mybrand.app`). The domain name uniquely identifies a
              registration. Cloudflare permits only one registration per domain, making the
              domain name a natural idempotency key for registration requests.

          auto_renew: Enable or disable automatic renewal. Setting this field to `true` authorizes
              Cloudflare to charge the account's default payment method up to 30 days before
              domain expiry to renew the domain automatically. Renewal pricing may change over
              time based on registry pricing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        extra_headers = {
            **strip_not_given({"Prefer": str(prefer) if is_given(prefer) else not_given}),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template(
                "/accounts/{account_id}/registrar/registrations/{domain_name}",
                account_id=account_id,
                domain_name=domain_name,
            ),
            body=maybe_transform({"auto_renew": auto_renew}, registration_edit_params.RegistrationEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WorkflowStatus]._unwrapper,
            ),
            cast_to=cast(Type[WorkflowStatus], ResultWrapper[WorkflowStatus]),
        )

    def get(
        self,
        domain_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Registration:
        """
        Returns the current state of a domain registration.

        This is the canonical read endpoint for a domain you own. It returns the full
        registration resource including current settings and expiration. When the
        registration resource is ready, both `created_at` and `expires_at` are present
        in the response.

        Args:
          account_id: Identifier.

          domain_name: Provides a fully qualified domain name (FQDN), including the extension (e.g.,
              `example.com`, `mybrand.app`). The domain name uniquely identifies a
              registration. Cloudflare permits only one registration per domain, making the
              domain name a natural idempotency key for registration requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/registrar/registrations/{domain_name}",
                account_id=account_id,
                domain_name=domain_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Registration]._unwrapper,
            ),
            cast_to=cast(Type[Registration], ResultWrapper[Registration]),
        )


class AsyncRegistrationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegistrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegistrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegistrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRegistrationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        domain_name: str,
        acknowledgements: Dict[str, object] | Omit = omit,
        auto_renew: bool | Omit = omit,
        contact_extensions: Dict[str, object] | Omit = omit,
        contacts: registration_create_params.Contacts | Omit = omit,
        privacy_mode: Literal["off", "redaction"] | Omit = omit,
        years: int | Omit = omit,
        prefer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowStatus:
        """Starts a domain registration workflow.

        This is a billable operation — successful
        registration charges the account's default payment method. All successful domain
        registrations are non-refundable — once the workflow completes with
        `state: succeeded`, the charge cannot be reversed.

        ### Prerequisites

        - The account must have a billing profile with a valid default payment method.
          Set this up at
          `https://dash.cloudflare.com/{account_id}/billing/payment-info`.
        - The account must not already be at the maximum supported domain limit. A
          single account may own up to 500 domains in total across registrations created
          through either the dashboard or this API.
        - The domain must be on a supported extension for programmatic registration.
        - Use `POST /domain-check` immediately before calling this endpoint to confirm
          real-time availability and pricing.

        ### Express mode

        The only required field is `domain_name`. If `contacts` is omitted, the system
        uses the account's default address book entry as the registrant. If no default
        exists and no contact is provided, the request fails. Set up a default address
        book entry and accept the required agreement at
        `https://dash.cloudflare.com/{account_id}/domains/registrations`.

        ### Defaults

        - `years`: defaults to the extension's minimum registration period (1 year for
          most extensions, but varies — for example, `.ai` (if supported) requires a
          minimum of 2 years).
        - `auto_renew`: defaults to `false`. Setting it to `true` is an explicit opt-in
          authorizing Cloudflare to charge the account's default payment method up to 30
          days before domain expiry to renew the registration. Renewal pricing may
          change over time based on registry pricing.
        - `privacy_mode`: defaults to `redaction`.

        ### Premium domains

        Premium domain registration is not currently supported by this API. If
        `POST /domain-check` returns `tier: premium`, do not call this endpoint for that
        domain.

        ### Response behavior

        By default, the server holds the connection for a bounded, server-defined amount
        of time while the registration completes. Most registrations finish within this
        window and return `201 Created` with a completed workflow status.

        If the registration is still processing after this synchronous wait window, the
        server returns `202 Accepted`. Poll the URL in `links.self` to track progress.

        To skip the wait and receive an immediate `202`, send `Prefer: respond-async`.

        Args:
          account_id: Identifier.

          domain_name: Provides a fully qualified domain name (FQDN), including the extension (e.g.,
              `example.com`, `mybrand.app`). The domain name uniquely identifies a
              registration. Cloudflare permits only one registration per domain, making the
              domain name a natural idempotency key for registration requests.

          acknowledgements: Provides user acknowledgements for a specific extension or premium registration
              flow. The extension registration schema from the extension discovery endpoint
              identifies the required keys.

          auto_renew: Enable or disable automatic renewal. Defaults to `false` if omitted. Setting
              this field to `true` is an explicit opt-in authorizing Cloudflare to charge the
              account's default payment method up to 30 days before domain expiry to renew the
              domain automatically. Renewal pricing may change over time based on registry
              pricing.

          contact_extensions: Provides registry-specific contact extension values for the registrant.
              `GET /accounts/{account_id}/registrar/extensions/{extension}` identifies the
              required keys and allowed values for each extension in the
              `registration_schema.properties.contact_extensions` object.

              Examples include `.us` nexus fields, `.uk` registrant type fields, and `.ca`
              legal type fields. Omit this object when the extension's registration schema
              excludes `contact_extensions`.

          contacts: Provides contact data for the registration request.

              The per-extension schema from
              `GET /accounts/{account_id}/registrar/extensions/{extension}` defines the
              accepted contact roles. Every currently supported extension requires only
              `contacts.registrant` from API callers. Callers may provide additional roles
              such as `technical`, `administrator`, and `billing` when the extension schema
              includes them. When a registry requires an omitted role, Cloudflare may derive
              that contact from `contacts.registrant`.

              When the request omits either the entire `contacts` object or
              `contacts.registrant`, the system uses the account's default address book entry
              as the registrant contact. The account owner must configure this default at
              `https://dash.cloudflare.com/{account_id}/domains/registrations`, where they can
              create or update the address book entry and accept the required agreement.
              Dashboard settings currently provide the only way to manage address book
              entries.

              Without either a default address book entry or a registrant contact, the
              registration request fails validation.

          privacy_mode: Sets the WHOIS privacy mode for the registration. Defaults to `redaction`.

              - `off`: Disables WHOIS privacy.
              - `redaction`: Requests WHOIS redaction where the extension supports it. Some
                extensions exclude privacy and redaction.

          years: Sets the registration term from 1 to 10 years. When omitted, this field defaults
              to the registry's minimum registration period for the extension. Most extensions
              require 1 year, while some require longer minimum terms (e.g., `.ai` requires 2
              years).

              Each registry may also enforce its own maximum registration term. A request
              above that maximum fails. When uncertain, omit this field to use the default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {**strip_not_given({"Prefer": prefer}), **(extra_headers or {})}
        return await self._post(
            path_template("/accounts/{account_id}/registrar/registrations", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "domain_name": domain_name,
                    "acknowledgements": acknowledgements,
                    "auto_renew": auto_renew,
                    "contact_extensions": contact_extensions,
                    "contacts": contacts,
                    "privacy_mode": privacy_mode,
                    "years": years,
                },
                registration_create_params.RegistrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WorkflowStatus]._unwrapper,
            ),
            cast_to=cast(Type[WorkflowStatus], ResultWrapper[WorkflowStatus]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        per_page: int | Omit = omit,
        sort_by: Literal["registry_created_at", "registry_expires_at", "name"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Registration, AsyncCursorPagination[Registration]]:
        """
        Returns a paginated list of domain registrations owned by the account.

        This endpoint uses cursor-based pagination. Results are ordered by registration
        date by default. To fetch the next page, pass the `cursor` value from the
        `result_info` object in the response as the `cursor` query parameter in your
        next request. An empty `cursor` string indicates there are no more pages.

        Args:
          account_id: Identifier.

          cursor: Opaque token from a previous response's `result_info.cursor`. Pass this value to
              fetch the next page of results. Omit (or pass an empty string) for the first
              page.

          direction: Sort direction for results. Defaults to ascending order.

          per_page: Number of items to return per page.

          sort_by: Column to sort results by. Defaults to registration date (`registry_created_at`)
              when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/registrar/registrations", account_id=account_id),
            page=AsyncCursorPagination[Registration],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "per_page": per_page,
                        "sort_by": sort_by,
                    },
                    registration_list_params.RegistrationListParams,
                ),
            ),
            model=Registration,
        )

    async def edit(
        self,
        domain_name: str,
        *,
        account_id: str,
        auto_renew: bool | Omit = omit,
        prefer: Literal["respond-async"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowStatus:
        """
        Updates an existing domain registration.

        By default, the server holds the connection for a bounded, server-defined amount
        of time while the update completes. Most updates finish within this window and
        return `200 OK` with a completed workflow status.

        If the update is still processing after this synchronous wait window, the server
        returns `202 Accepted`. Poll the URL in `links.self` to track progress.

        To skip the wait and receive an immediate `202`, send `Prefer: respond-async`.

        This endpoint currently supports updating `auto_renew` only.

        Args:
          account_id: Identifier.

          domain_name: Provides a fully qualified domain name (FQDN), including the extension (e.g.,
              `example.com`, `mybrand.app`). The domain name uniquely identifies a
              registration. Cloudflare permits only one registration per domain, making the
              domain name a natural idempotency key for registration requests.

          auto_renew: Enable or disable automatic renewal. Setting this field to `true` authorizes
              Cloudflare to charge the account's default payment method up to 30 days before
              domain expiry to renew the domain automatically. Renewal pricing may change over
              time based on registry pricing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        extra_headers = {
            **strip_not_given({"Prefer": str(prefer) if is_given(prefer) else not_given}),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template(
                "/accounts/{account_id}/registrar/registrations/{domain_name}",
                account_id=account_id,
                domain_name=domain_name,
            ),
            body=await async_maybe_transform(
                {"auto_renew": auto_renew}, registration_edit_params.RegistrationEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WorkflowStatus]._unwrapper,
            ),
            cast_to=cast(Type[WorkflowStatus], ResultWrapper[WorkflowStatus]),
        )

    async def get(
        self,
        domain_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Registration:
        """
        Returns the current state of a domain registration.

        This is the canonical read endpoint for a domain you own. It returns the full
        registration resource including current settings and expiration. When the
        registration resource is ready, both `created_at` and `expires_at` are present
        in the response.

        Args:
          account_id: Identifier.

          domain_name: Provides a fully qualified domain name (FQDN), including the extension (e.g.,
              `example.com`, `mybrand.app`). The domain name uniquely identifies a
              registration. Cloudflare permits only one registration per domain, making the
              domain name a natural idempotency key for registration requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/registrar/registrations/{domain_name}",
                account_id=account_id,
                domain_name=domain_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Registration]._unwrapper,
            ),
            cast_to=cast(Type[Registration], ResultWrapper[Registration]),
        )


class RegistrationsResourceWithRawResponse:
    def __init__(self, registrations: RegistrationsResource) -> None:
        self._registrations = registrations

        self.create = to_raw_response_wrapper(
            registrations.create,
        )
        self.list = to_raw_response_wrapper(
            registrations.list,
        )
        self.edit = to_raw_response_wrapper(
            registrations.edit,
        )
        self.get = to_raw_response_wrapper(
            registrations.get,
        )


class AsyncRegistrationsResourceWithRawResponse:
    def __init__(self, registrations: AsyncRegistrationsResource) -> None:
        self._registrations = registrations

        self.create = async_to_raw_response_wrapper(
            registrations.create,
        )
        self.list = async_to_raw_response_wrapper(
            registrations.list,
        )
        self.edit = async_to_raw_response_wrapper(
            registrations.edit,
        )
        self.get = async_to_raw_response_wrapper(
            registrations.get,
        )


class RegistrationsResourceWithStreamingResponse:
    def __init__(self, registrations: RegistrationsResource) -> None:
        self._registrations = registrations

        self.create = to_streamed_response_wrapper(
            registrations.create,
        )
        self.list = to_streamed_response_wrapper(
            registrations.list,
        )
        self.edit = to_streamed_response_wrapper(
            registrations.edit,
        )
        self.get = to_streamed_response_wrapper(
            registrations.get,
        )


class AsyncRegistrationsResourceWithStreamingResponse:
    def __init__(self, registrations: AsyncRegistrationsResource) -> None:
        self._registrations = registrations

        self.create = async_to_streamed_response_wrapper(
            registrations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            registrations.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            registrations.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            registrations.get,
        )
