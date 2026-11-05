# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from .roles import (
    RolesResource,
    AsyncRolesResource,
    RolesResourceWithRawResponse,
    AsyncRolesResourceWithRawResponse,
    RolesResourceWithStreamingResponse,
    AsyncRolesResourceWithStreamingResponse,
)
from .members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .invoices import (
    InvoicesResource,
    AsyncInvoicesResource,
    InvoicesResourceWithRawResponse,
    AsyncInvoicesResourceWithRawResponse,
    InvoicesResourceWithStreamingResponse,
    AsyncInvoicesResourceWithStreamingResponse,
)
from .receipts import (
    ReceiptsResource,
    AsyncReceiptsResource,
    ReceiptsResourceWithRawResponse,
    AsyncReceiptsResourceWithRawResponse,
    ReceiptsResourceWithStreamingResponse,
    AsyncReceiptsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .logs.logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from .pay_invoice import (
    PayInvoiceResource,
    AsyncPayInvoiceResource,
    PayInvoiceResourceWithRawResponse,
    AsyncPayInvoiceResourceWithRawResponse,
    PayInvoiceResourceWithStreamingResponse,
    AsyncPayInvoiceResourceWithStreamingResponse,
)
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from .entitlements import (
    EntitlementsResource,
    AsyncEntitlementsResource,
    EntitlementsResourceWithRawResponse,
    AsyncEntitlementsResourceWithRawResponse,
    EntitlementsResourceWithStreamingResponse,
    AsyncEntitlementsResourceWithStreamingResponse,
)
from .client_secret import (
    ClientSecretResource,
    AsyncClientSecretResource,
    ClientSecretResourceWithRawResponse,
    AsyncClientSecretResourceWithRawResponse,
    ClientSecretResourceWithStreamingResponse,
    AsyncClientSecretResourceWithStreamingResponse,
)
from .tokens.tokens import (
    TokensResource,
    AsyncTokensResource,
    TokensResourceWithRawResponse,
    AsyncTokensResourceWithRawResponse,
    TokensResourceWithStreamingResponse,
    AsyncTokensResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from .payment_methods import (
    PaymentMethodsResource,
    AsyncPaymentMethodsResource,
    PaymentMethodsResourceWithRawResponse,
    AsyncPaymentMethodsResourceWithRawResponse,
    PaymentMethodsResourceWithStreamingResponse,
    AsyncPaymentMethodsResourceWithStreamingResponse,
)
from ...types.accounts import account_list_params, account_create_params, account_update_params
from ...types.accounts.account import Account
from .subscriptions.subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)
from .speed_settings.speed_settings import (
    SpeedSettingsResource,
    AsyncSpeedSettingsResource,
    SpeedSettingsResourceWithRawResponse,
    AsyncSpeedSettingsResourceWithRawResponse,
    SpeedSettingsResourceWithStreamingResponse,
    AsyncSpeedSettingsResourceWithStreamingResponse,
)
from ...types.accounts.account_delete_response import AccountDeleteResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def roles(self) -> RolesResource:
        return RolesResource(self._client)

    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        return SubscriptionsResource(self._client)

    @cached_property
    def tokens(self) -> TokensResource:
        return TokensResource(self._client)

    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def entitlements(self) -> EntitlementsResource:
        return EntitlementsResource(self._client)

    @cached_property
    def speed_settings(self) -> SpeedSettingsResource:
        return SpeedSettingsResource(self._client)

    @cached_property
    def payment_methods(self) -> PaymentMethodsResource:
        return PaymentMethodsResource(self._client)

    @cached_property
    def pay_invoice(self) -> PayInvoiceResource:
        return PayInvoiceResource(self._client)

    @cached_property
    def receipts(self) -> ReceiptsResource:
        return ReceiptsResource(self._client)

    @cached_property
    def invoices(self) -> InvoicesResource:
        return InvoicesResource(self._client)

    @cached_property
    def client_secret(self) -> ClientSecretResource:
        return ClientSecretResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        standalone: Literal[True] | Omit = omit,
        type: Literal["standard", "enterprise"] | Omit = omit,
        unit: account_create_params.Unit | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Account]:
        """Create an Account.

        To create the Account within an Organization, provide
        `unit.id` and omit `standalone`. To create a standalone Free Account, provide
        `standalone: true` and omit `unit`. Providing both fields is invalid. If you
        omit both fields, Cloudflare can determine the destination only when the User is
        an administrator of exactly one Organization. Cloudflare creates the Account in
        that Organization; otherwise, the request returns an error. Account names are
        limited to 65 UTF-8 bytes.

        Args:
          name: Account name, limited to 65 UTF-8 bytes.

          standalone: Set to `true` and omit `unit` to create a standalone Free Account. If provided,
              this field must be `true`.

          type: the type of account being created. For self-serve customers, use standard. for
              enterprise customers, use enterprise.

          unit: Information related to the tenant unit. Provide its ID and omit `standalone` to
              create the Account within an Organization. See
              https://developers.cloudflare.com/tenant/how-to/manage-accounts/.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/accounts",
            body=maybe_transform(
                {
                    "name": name,
                    "standalone": standalone,
                    "type": type,
                    "unit": unit,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Account]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Account]], ResultWrapper[Account]),
        )

    def update(
        self,
        *,
        account_id: str,
        id: str,
        name: str,
        type: Literal["standard", "enterprise"],
        managed_by: account_update_params.ManagedBy | Omit = omit,
        settings: account_update_params.Settings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Account]:
        """Update an existing account.

        Account names are limited to 65 UTF-8 bytes.

        Args:
          account_id: Account identifier tag.

          id: Identifier

          name: Account name, limited to 65 UTF-8 bytes.

          managed_by: Parent container details

          settings: Account settings

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            path_template("/accounts/{account_id}", account_id=account_id),
            body=maybe_transform(
                {
                    "id": id,
                    "name": name,
                    "type": type,
                    "managed_by": managed_by,
                    "settings": settings,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Account]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Account]], ResultWrapper[Account]),
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[Account]:
        """
        List all accounts you have ownership or verified access to.

        Args:
          direction: Direction to order results.

          name: Name of the account.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/accounts",
            page=SyncV4PagePaginationArray[Account],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            model=Account,
        )

    def delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccountDeleteResponse]:
        """Delete a specific account (only available for tenant admins at this time).

        This
        is a permanent operation that will delete any zones or other resources under the
        account

        Args:
          account_id: The account ID of the account to be deleted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            path_template("/accounts/{account_id}", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AccountDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountDeleteResponse]], ResultWrapper[AccountDeleteResponse]),
        )

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Account]:
        """
        Get information about a specific account that you are a member of.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Account]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Account]], ResultWrapper[Account]),
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def roles(self) -> AsyncRolesResource:
        return AsyncRolesResource(self._client)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def tokens(self) -> AsyncTokensResource:
        return AsyncTokensResource(self._client)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResource:
        return AsyncEntitlementsResource(self._client)

    @cached_property
    def speed_settings(self) -> AsyncSpeedSettingsResource:
        return AsyncSpeedSettingsResource(self._client)

    @cached_property
    def payment_methods(self) -> AsyncPaymentMethodsResource:
        return AsyncPaymentMethodsResource(self._client)

    @cached_property
    def pay_invoice(self) -> AsyncPayInvoiceResource:
        return AsyncPayInvoiceResource(self._client)

    @cached_property
    def receipts(self) -> AsyncReceiptsResource:
        return AsyncReceiptsResource(self._client)

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        return AsyncInvoicesResource(self._client)

    @cached_property
    def client_secret(self) -> AsyncClientSecretResource:
        return AsyncClientSecretResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        standalone: Literal[True] | Omit = omit,
        type: Literal["standard", "enterprise"] | Omit = omit,
        unit: account_create_params.Unit | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Account]:
        """Create an Account.

        To create the Account within an Organization, provide
        `unit.id` and omit `standalone`. To create a standalone Free Account, provide
        `standalone: true` and omit `unit`. Providing both fields is invalid. If you
        omit both fields, Cloudflare can determine the destination only when the User is
        an administrator of exactly one Organization. Cloudflare creates the Account in
        that Organization; otherwise, the request returns an error. Account names are
        limited to 65 UTF-8 bytes.

        Args:
          name: Account name, limited to 65 UTF-8 bytes.

          standalone: Set to `true` and omit `unit` to create a standalone Free Account. If provided,
              this field must be `true`.

          type: the type of account being created. For self-serve customers, use standard. for
              enterprise customers, use enterprise.

          unit: Information related to the tenant unit. Provide its ID and omit `standalone` to
              create the Account within an Organization. See
              https://developers.cloudflare.com/tenant/how-to/manage-accounts/.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/accounts",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "standalone": standalone,
                    "type": type,
                    "unit": unit,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Account]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Account]], ResultWrapper[Account]),
        )

    async def update(
        self,
        *,
        account_id: str,
        id: str,
        name: str,
        type: Literal["standard", "enterprise"],
        managed_by: account_update_params.ManagedBy | Omit = omit,
        settings: account_update_params.Settings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Account]:
        """Update an existing account.

        Account names are limited to 65 UTF-8 bytes.

        Args:
          account_id: Account identifier tag.

          id: Identifier

          name: Account name, limited to 65 UTF-8 bytes.

          managed_by: Parent container details

          settings: Account settings

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            path_template("/accounts/{account_id}", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "name": name,
                    "type": type,
                    "managed_by": managed_by,
                    "settings": settings,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Account]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Account]], ResultWrapper[Account]),
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Account, AsyncV4PagePaginationArray[Account]]:
        """
        List all accounts you have ownership or verified access to.

        Args:
          direction: Direction to order results.

          name: Name of the account.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/accounts",
            page=AsyncV4PagePaginationArray[Account],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            model=Account,
        )

    async def delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccountDeleteResponse]:
        """Delete a specific account (only available for tenant admins at this time).

        This
        is a permanent operation that will delete any zones or other resources under the
        account

        Args:
          account_id: The account ID of the account to be deleted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            path_template("/accounts/{account_id}", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AccountDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountDeleteResponse]], ResultWrapper[AccountDeleteResponse]),
        )

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Account]:
        """
        Get information about a specific account that you are a member of.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Account]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Account]], ResultWrapper[Account]),
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_raw_response_wrapper(
            accounts.create,
        )
        self.update = to_raw_response_wrapper(
            accounts.update,
        )
        self.list = to_raw_response_wrapper(
            accounts.list,
        )
        self.delete = to_raw_response_wrapper(
            accounts.delete,
        )
        self.get = to_raw_response_wrapper(
            accounts.get,
        )

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._accounts.members)

    @cached_property
    def roles(self) -> RolesResourceWithRawResponse:
        return RolesResourceWithRawResponse(self._accounts.roles)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        return SubscriptionsResourceWithRawResponse(self._accounts.subscriptions)

    @cached_property
    def tokens(self) -> TokensResourceWithRawResponse:
        return TokensResourceWithRawResponse(self._accounts.tokens)

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._accounts.logs)

    @cached_property
    def entitlements(self) -> EntitlementsResourceWithRawResponse:
        return EntitlementsResourceWithRawResponse(self._accounts.entitlements)

    @cached_property
    def speed_settings(self) -> SpeedSettingsResourceWithRawResponse:
        return SpeedSettingsResourceWithRawResponse(self._accounts.speed_settings)

    @cached_property
    def payment_methods(self) -> PaymentMethodsResourceWithRawResponse:
        return PaymentMethodsResourceWithRawResponse(self._accounts.payment_methods)

    @cached_property
    def pay_invoice(self) -> PayInvoiceResourceWithRawResponse:
        return PayInvoiceResourceWithRawResponse(self._accounts.pay_invoice)

    @cached_property
    def receipts(self) -> ReceiptsResourceWithRawResponse:
        return ReceiptsResourceWithRawResponse(self._accounts.receipts)

    @cached_property
    def invoices(self) -> InvoicesResourceWithRawResponse:
        return InvoicesResourceWithRawResponse(self._accounts.invoices)

    @cached_property
    def client_secret(self) -> ClientSecretResourceWithRawResponse:
        return ClientSecretResourceWithRawResponse(self._accounts.client_secret)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_raw_response_wrapper(
            accounts.create,
        )
        self.update = async_to_raw_response_wrapper(
            accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            accounts.delete,
        )
        self.get = async_to_raw_response_wrapper(
            accounts.get,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._accounts.members)

    @cached_property
    def roles(self) -> AsyncRolesResourceWithRawResponse:
        return AsyncRolesResourceWithRawResponse(self._accounts.roles)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        return AsyncSubscriptionsResourceWithRawResponse(self._accounts.subscriptions)

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithRawResponse:
        return AsyncTokensResourceWithRawResponse(self._accounts.tokens)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._accounts.logs)

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResourceWithRawResponse:
        return AsyncEntitlementsResourceWithRawResponse(self._accounts.entitlements)

    @cached_property
    def speed_settings(self) -> AsyncSpeedSettingsResourceWithRawResponse:
        return AsyncSpeedSettingsResourceWithRawResponse(self._accounts.speed_settings)

    @cached_property
    def payment_methods(self) -> AsyncPaymentMethodsResourceWithRawResponse:
        return AsyncPaymentMethodsResourceWithRawResponse(self._accounts.payment_methods)

    @cached_property
    def pay_invoice(self) -> AsyncPayInvoiceResourceWithRawResponse:
        return AsyncPayInvoiceResourceWithRawResponse(self._accounts.pay_invoice)

    @cached_property
    def receipts(self) -> AsyncReceiptsResourceWithRawResponse:
        return AsyncReceiptsResourceWithRawResponse(self._accounts.receipts)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithRawResponse:
        return AsyncInvoicesResourceWithRawResponse(self._accounts.invoices)

    @cached_property
    def client_secret(self) -> AsyncClientSecretResourceWithRawResponse:
        return AsyncClientSecretResourceWithRawResponse(self._accounts.client_secret)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_streamed_response_wrapper(
            accounts.create,
        )
        self.update = to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            accounts.delete,
        )
        self.get = to_streamed_response_wrapper(
            accounts.get,
        )

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._accounts.members)

    @cached_property
    def roles(self) -> RolesResourceWithStreamingResponse:
        return RolesResourceWithStreamingResponse(self._accounts.roles)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        return SubscriptionsResourceWithStreamingResponse(self._accounts.subscriptions)

    @cached_property
    def tokens(self) -> TokensResourceWithStreamingResponse:
        return TokensResourceWithStreamingResponse(self._accounts.tokens)

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._accounts.logs)

    @cached_property
    def entitlements(self) -> EntitlementsResourceWithStreamingResponse:
        return EntitlementsResourceWithStreamingResponse(self._accounts.entitlements)

    @cached_property
    def speed_settings(self) -> SpeedSettingsResourceWithStreamingResponse:
        return SpeedSettingsResourceWithStreamingResponse(self._accounts.speed_settings)

    @cached_property
    def payment_methods(self) -> PaymentMethodsResourceWithStreamingResponse:
        return PaymentMethodsResourceWithStreamingResponse(self._accounts.payment_methods)

    @cached_property
    def pay_invoice(self) -> PayInvoiceResourceWithStreamingResponse:
        return PayInvoiceResourceWithStreamingResponse(self._accounts.pay_invoice)

    @cached_property
    def receipts(self) -> ReceiptsResourceWithStreamingResponse:
        return ReceiptsResourceWithStreamingResponse(self._accounts.receipts)

    @cached_property
    def invoices(self) -> InvoicesResourceWithStreamingResponse:
        return InvoicesResourceWithStreamingResponse(self._accounts.invoices)

    @cached_property
    def client_secret(self) -> ClientSecretResourceWithStreamingResponse:
        return ClientSecretResourceWithStreamingResponse(self._accounts.client_secret)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_streamed_response_wrapper(
            accounts.create,
        )
        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            accounts.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            accounts.get,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._accounts.members)

    @cached_property
    def roles(self) -> AsyncRolesResourceWithStreamingResponse:
        return AsyncRolesResourceWithStreamingResponse(self._accounts.roles)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        return AsyncSubscriptionsResourceWithStreamingResponse(self._accounts.subscriptions)

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithStreamingResponse:
        return AsyncTokensResourceWithStreamingResponse(self._accounts.tokens)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._accounts.logs)

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResourceWithStreamingResponse:
        return AsyncEntitlementsResourceWithStreamingResponse(self._accounts.entitlements)

    @cached_property
    def speed_settings(self) -> AsyncSpeedSettingsResourceWithStreamingResponse:
        return AsyncSpeedSettingsResourceWithStreamingResponse(self._accounts.speed_settings)

    @cached_property
    def payment_methods(self) -> AsyncPaymentMethodsResourceWithStreamingResponse:
        return AsyncPaymentMethodsResourceWithStreamingResponse(self._accounts.payment_methods)

    @cached_property
    def pay_invoice(self) -> AsyncPayInvoiceResourceWithStreamingResponse:
        return AsyncPayInvoiceResourceWithStreamingResponse(self._accounts.pay_invoice)

    @cached_property
    def receipts(self) -> AsyncReceiptsResourceWithStreamingResponse:
        return AsyncReceiptsResourceWithStreamingResponse(self._accounts.receipts)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithStreamingResponse:
        return AsyncInvoicesResourceWithStreamingResponse(self._accounts.invoices)

    @cached_property
    def client_secret(self) -> AsyncClientSecretResourceWithStreamingResponse:
        return AsyncClientSecretResourceWithStreamingResponse(self._accounts.client_secret)
