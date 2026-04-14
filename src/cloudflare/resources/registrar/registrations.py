# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import is_given, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.registrar import registration_edit_params, registration_create_params
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
        auto_renew: bool | Omit = omit,
        contacts: registration_create_params.Contacts | Omit = omit,
        privacy_mode: Literal["redaction"] | Omit = omit,
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
          single account may own up to 100 domains in total across registrations created
          through either the dashboard or this API.
        - The domain must be on a supported extension listed in `info.description`.
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
          account_id: Identifier

          domain_name: Fully qualified domain name (FQDN) including the extension (e.g., `example.com`,
              `mybrand.app`). The domain name uniquely identifies a registration — the same
              domain cannot be registered twice, making it a natural idempotency key for
              registration requests.

          auto_renew: Enable or disable automatic renewal. Defaults to `false` if omitted. Setting
              this field to `true` is an explicit opt-in authorizing Cloudflare to charge the
              account's default payment method up to 30 days before domain expiry to renew the
              domain automatically. Renewal pricing may change over time based on registry
              pricing.

          contacts: Contact data for the registration request.

              If the `contacts` object is omitted entirely from the request, or if
              `contacts.registrant` is not provided, the system will use the account's default
              address book entry as the registrant contact. This default must be
              pre-configured by the account owner at
              `https://dash.cloudflare.com/{account_id}/domains/registrations`, where they can
              create or update the address book entry and accept the required agreement. No
              API exists for managing address book entries at this time.

              If no default address book entry exists and no registrant contact is provided,
              the registration request will fail with a validation error.

          privacy_mode: WHOIS privacy mode for the registration. Defaults to `redaction`.

              - `off`: Do not request WHOIS privacy.
              - `redaction`: Request WHOIS redaction where supported by the extension. Some
                extensions do not support privacy/redaction.

          years: Number of years to register (1–10). If omitted, defaults to the minimum
              registration period required by the registry for this extension. For most
              extensions this is 1 year, but some extensions require longer minimum terms
              (e.g., `.ai` requires a minimum of 2 years).

              The registry for each extension may also enforce its own maximum registration
              term. If the requested value exceeds the registry's maximum, the registration
              will be rejected. When in doubt, use the default by omitting this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {**strip_not_given({"Prefer": prefer}), **(extra_headers or {})}
        return self._post(
            f"/accounts/{account_id}/registrar/registrations",
            body=maybe_transform(
                {
                    "domain_name": domain_name,
                    "auto_renew": auto_renew,
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
          account_id: Identifier

          domain_name: Fully qualified domain name (FQDN) including the extension (e.g., `example.com`,
              `mybrand.app`). The domain name uniquely identifies a registration — the same
              domain cannot be registered twice, making it a natural idempotency key for
              registration requests.

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
            f"/accounts/{account_id}/registrar/registrations/{domain_name}",
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
          account_id: Identifier

          domain_name: Fully qualified domain name (FQDN) including the extension (e.g., `example.com`,
              `mybrand.app`). The domain name uniquely identifies a registration — the same
              domain cannot be registered twice, making it a natural idempotency key for
              registration requests.

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
            f"/accounts/{account_id}/registrar/registrations/{domain_name}",
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
        auto_renew: bool | Omit = omit,
        contacts: registration_create_params.Contacts | Omit = omit,
        privacy_mode: Literal["redaction"] | Omit = omit,
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
          single account may own up to 100 domains in total across registrations created
          through either the dashboard or this API.
        - The domain must be on a supported extension listed in `info.description`.
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
          account_id: Identifier

          domain_name: Fully qualified domain name (FQDN) including the extension (e.g., `example.com`,
              `mybrand.app`). The domain name uniquely identifies a registration — the same
              domain cannot be registered twice, making it a natural idempotency key for
              registration requests.

          auto_renew: Enable or disable automatic renewal. Defaults to `false` if omitted. Setting
              this field to `true` is an explicit opt-in authorizing Cloudflare to charge the
              account's default payment method up to 30 days before domain expiry to renew the
              domain automatically. Renewal pricing may change over time based on registry
              pricing.

          contacts: Contact data for the registration request.

              If the `contacts` object is omitted entirely from the request, or if
              `contacts.registrant` is not provided, the system will use the account's default
              address book entry as the registrant contact. This default must be
              pre-configured by the account owner at
              `https://dash.cloudflare.com/{account_id}/domains/registrations`, where they can
              create or update the address book entry and accept the required agreement. No
              API exists for managing address book entries at this time.

              If no default address book entry exists and no registrant contact is provided,
              the registration request will fail with a validation error.

          privacy_mode: WHOIS privacy mode for the registration. Defaults to `redaction`.

              - `off`: Do not request WHOIS privacy.
              - `redaction`: Request WHOIS redaction where supported by the extension. Some
                extensions do not support privacy/redaction.

          years: Number of years to register (1–10). If omitted, defaults to the minimum
              registration period required by the registry for this extension. For most
              extensions this is 1 year, but some extensions require longer minimum terms
              (e.g., `.ai` requires a minimum of 2 years).

              The registry for each extension may also enforce its own maximum registration
              term. If the requested value exceeds the registry's maximum, the registration
              will be rejected. When in doubt, use the default by omitting this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {**strip_not_given({"Prefer": prefer}), **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/registrar/registrations",
            body=await async_maybe_transform(
                {
                    "domain_name": domain_name,
                    "auto_renew": auto_renew,
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
          account_id: Identifier

          domain_name: Fully qualified domain name (FQDN) including the extension (e.g., `example.com`,
              `mybrand.app`). The domain name uniquely identifies a registration — the same
              domain cannot be registered twice, making it a natural idempotency key for
              registration requests.

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
            f"/accounts/{account_id}/registrar/registrations/{domain_name}",
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
          account_id: Identifier

          domain_name: Fully qualified domain name (FQDN) including the extension (e.g., `example.com`,
              `mybrand.app`). The domain name uniquely identifies a registration — the same
              domain cannot be registered twice, making it a natural idempotency key for
              registration requests.

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
            f"/accounts/{account_id}/registrar/registrations/{domain_name}",
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
        self.edit = async_to_streamed_response_wrapper(
            registrations.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            registrations.get,
        )
