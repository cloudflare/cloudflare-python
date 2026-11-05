# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from .audit import (
    AuditResource,
    AsyncAuditResource,
    AuditResourceWithRawResponse,
    AsyncAuditResourceWithRawResponse,
    AuditResourceWithStreamingResponse,
    AsyncAuditResourceWithStreamingResponse,
)
from .activity import (
    ActivityResource,
    AsyncActivityResource,
    ActivityResourceWithRawResponse,
    AsyncActivityResourceWithRawResponse,
    ActivityResourceWithStreamingResponse,
    AsyncActivityResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.billing import spend_policy_create_params, spend_policy_update_params
from ....types.billing.spend_policy_get_response import SpendPolicyGetResponse
from ....types.billing.spend_policy_list_response import SpendPolicyListResponse
from ....types.billing.spend_policy_create_response import SpendPolicyCreateResponse
from ....types.billing.spend_policy_delete_response import SpendPolicyDeleteResponse
from ....types.billing.spend_policy_update_response import SpendPolicyUpdateResponse

__all__ = ["SpendPoliciesResource", "AsyncSpendPoliciesResource"]


class SpendPoliciesResource(SyncAPIResource):
    @cached_property
    def audit(self) -> AuditResource:
        return AuditResource(self._client)

    @cached_property
    def activity(self) -> ActivityResource:
        return ActivityResource(self._client)

    @cached_property
    def with_raw_response(self) -> SpendPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SpendPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpendPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SpendPoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        action: Literal["notification", "usage_block"],
        enabled: bool,
        name: str,
        product_id: Literal["workers", "durable_objects"],
        threshold_cents: int,
        notification_email: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendPolicyCreateResponse:
        """Creates a spend policy.

        Each account can have only one enabled `usage_block`
        policy per product. A second one returns `409`. There is no limit on
        `notification` policies.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          action: The action taken when the threshold is reached. `notification` sends an email to
              `notification_email`. `usage_block` blocks further usage of the product until
              the end of the billing period. Raising the threshold above the current balance,
              disabling the policy, or deleting it lifts the block early.

          enabled: Whether the policy is evaluated.

          name: Display name of the policy. After surrounding whitespace is trimmed, it must be
              1 to 200 bytes long. The value is stored as sent, untrimmed.

          product_id: The product the policy applies to: `workers` or `durable_objects`. Each
              product's balance and policies are separate. Both products support
              `notification` and `usage_block` policies on create and update.

          threshold_cents: The spend threshold for the current billing period, in US cents. Must be greater
              than zero.

          notification_email: Email address that receives notifications. Required when `action` is
              `notification`. When set, it must be a bare address (`user@example.com`);
              display-name forms such as `Name <user@example.com>` are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/billing/spend-policies", account_id=account_id),
            body=maybe_transform(
                {
                    "action": action,
                    "enabled": enabled,
                    "name": name,
                    "product_id": product_id,
                    "threshold_cents": threshold_cents,
                    "notification_email": notification_email,
                },
                spend_policy_create_params.SpendPolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SpendPolicyCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SpendPolicyCreateResponse], ResultWrapper[SpendPolicyCreateResponse]),
        )

    def update(
        self,
        policy_id: str,
        *,
        account_id: str,
        action: Literal["notification", "usage_block"],
        enabled: bool,
        name: str,
        product_id: Literal["workers", "durable_objects"],
        threshold_cents: int,
        if_match: str,
        notification_email: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendPolicyUpdateResponse:
        """Replaces the whole spend policy.

        Every field is required, as on create; there
        are no partial updates and `PATCH` is not supported. The `If-Match` header must
        equal the policy's current `version`. On success, `version` goes up by one and
        the new value is returned in `ETag`.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          policy_id: The unique identifier of the spend policy.

          action: The action taken when the threshold is reached. `notification` sends an email to
              `notification_email`. `usage_block` blocks further usage of the product until
              the end of the billing period. Raising the threshold above the current balance,
              disabling the policy, or deleting it lifts the block early.

          enabled: Whether the policy is evaluated.

          name: Display name of the policy. After surrounding whitespace is trimmed, it must be
              1 to 200 bytes long. The value is stored as sent, untrimmed.

          product_id: The product the policy applies to: `workers` or `durable_objects`. Each
              product's balance and policies are separate. Both products support
              `notification` and `usage_block` policies on create and update.

          threshold_cents: The spend threshold for the current billing period, in US cents. Must be greater
              than zero.

          notification_email: Email address that receives notifications. Required when `action` is
              `notification`. When set, it must be a bare address (`user@example.com`);
              display-name forms such as `Name <user@example.com>` are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return self._put(
            path_template(
                "/accounts/{account_id}/billing/spend-policies/{policy_id}", account_id=account_id, policy_id=policy_id
            ),
            body=maybe_transform(
                {
                    "action": action,
                    "enabled": enabled,
                    "name": name,
                    "product_id": product_id,
                    "threshold_cents": threshold_cents,
                    "notification_email": notification_email,
                },
                spend_policy_update_params.SpendPolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SpendPolicyUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SpendPolicyUpdateResponse], ResultWrapper[SpendPolicyUpdateResponse]),
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
    ) -> SyncSinglePage[SpendPolicyListResponse]:
        """
        Returns every spend policy on the account that has not been deleted, including
        disabled ones. Results are sorted by `name`, then `id`. There is no pagination.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/billing/spend-policies", account_id=account_id),
            page=SyncSinglePage[SpendPolicyListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SpendPolicyListResponse,
        )

    def delete(
        self,
        policy_id: str,
        *,
        account_id: str,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendPolicyDeleteResponse:
        """Soft-deletes the spend policy.

        The policy is disabled and no longer appears in
        list, get or audit responses. The `If-Match` header must equal the policy's
        current `version`.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          policy_id: The unique identifier of the spend policy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return self._delete(
            path_template(
                "/accounts/{account_id}/billing/spend-policies/{policy_id}", account_id=account_id, policy_id=policy_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SpendPolicyDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[SpendPolicyDeleteResponse], ResultWrapper[SpendPolicyDeleteResponse]),
        )

    def get(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendPolicyGetResponse:
        """Returns one spend policy.

        The `ETag` response header holds the current
        `version`; send it as `If-Match` on a later update or delete.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          policy_id: The unique identifier of the spend policy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/billing/spend-policies/{policy_id}", account_id=account_id, policy_id=policy_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SpendPolicyGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SpendPolicyGetResponse], ResultWrapper[SpendPolicyGetResponse]),
        )


class AsyncSpendPoliciesResource(AsyncAPIResource):
    @cached_property
    def audit(self) -> AsyncAuditResource:
        return AsyncAuditResource(self._client)

    @cached_property
    def activity(self) -> AsyncActivityResource:
        return AsyncActivityResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpendPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpendPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpendPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSpendPoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        action: Literal["notification", "usage_block"],
        enabled: bool,
        name: str,
        product_id: Literal["workers", "durable_objects"],
        threshold_cents: int,
        notification_email: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendPolicyCreateResponse:
        """Creates a spend policy.

        Each account can have only one enabled `usage_block`
        policy per product. A second one returns `409`. There is no limit on
        `notification` policies.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          action: The action taken when the threshold is reached. `notification` sends an email to
              `notification_email`. `usage_block` blocks further usage of the product until
              the end of the billing period. Raising the threshold above the current balance,
              disabling the policy, or deleting it lifts the block early.

          enabled: Whether the policy is evaluated.

          name: Display name of the policy. After surrounding whitespace is trimmed, it must be
              1 to 200 bytes long. The value is stored as sent, untrimmed.

          product_id: The product the policy applies to: `workers` or `durable_objects`. Each
              product's balance and policies are separate. Both products support
              `notification` and `usage_block` policies on create and update.

          threshold_cents: The spend threshold for the current billing period, in US cents. Must be greater
              than zero.

          notification_email: Email address that receives notifications. Required when `action` is
              `notification`. When set, it must be a bare address (`user@example.com`);
              display-name forms such as `Name <user@example.com>` are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/billing/spend-policies", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "action": action,
                    "enabled": enabled,
                    "name": name,
                    "product_id": product_id,
                    "threshold_cents": threshold_cents,
                    "notification_email": notification_email,
                },
                spend_policy_create_params.SpendPolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SpendPolicyCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SpendPolicyCreateResponse], ResultWrapper[SpendPolicyCreateResponse]),
        )

    async def update(
        self,
        policy_id: str,
        *,
        account_id: str,
        action: Literal["notification", "usage_block"],
        enabled: bool,
        name: str,
        product_id: Literal["workers", "durable_objects"],
        threshold_cents: int,
        if_match: str,
        notification_email: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendPolicyUpdateResponse:
        """Replaces the whole spend policy.

        Every field is required, as on create; there
        are no partial updates and `PATCH` is not supported. The `If-Match` header must
        equal the policy's current `version`. On success, `version` goes up by one and
        the new value is returned in `ETag`.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          policy_id: The unique identifier of the spend policy.

          action: The action taken when the threshold is reached. `notification` sends an email to
              `notification_email`. `usage_block` blocks further usage of the product until
              the end of the billing period. Raising the threshold above the current balance,
              disabling the policy, or deleting it lifts the block early.

          enabled: Whether the policy is evaluated.

          name: Display name of the policy. After surrounding whitespace is trimmed, it must be
              1 to 200 bytes long. The value is stored as sent, untrimmed.

          product_id: The product the policy applies to: `workers` or `durable_objects`. Each
              product's balance and policies are separate. Both products support
              `notification` and `usage_block` policies on create and update.

          threshold_cents: The spend threshold for the current billing period, in US cents. Must be greater
              than zero.

          notification_email: Email address that receives notifications. Required when `action` is
              `notification`. When set, it must be a bare address (`user@example.com`);
              display-name forms such as `Name <user@example.com>` are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return await self._put(
            path_template(
                "/accounts/{account_id}/billing/spend-policies/{policy_id}", account_id=account_id, policy_id=policy_id
            ),
            body=await async_maybe_transform(
                {
                    "action": action,
                    "enabled": enabled,
                    "name": name,
                    "product_id": product_id,
                    "threshold_cents": threshold_cents,
                    "notification_email": notification_email,
                },
                spend_policy_update_params.SpendPolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SpendPolicyUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SpendPolicyUpdateResponse], ResultWrapper[SpendPolicyUpdateResponse]),
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
    ) -> AsyncPaginator[SpendPolicyListResponse, AsyncSinglePage[SpendPolicyListResponse]]:
        """
        Returns every spend policy on the account that has not been deleted, including
        disabled ones. Results are sorted by `name`, then `id`. There is no pagination.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/billing/spend-policies", account_id=account_id),
            page=AsyncSinglePage[SpendPolicyListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SpendPolicyListResponse,
        )

    async def delete(
        self,
        policy_id: str,
        *,
        account_id: str,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendPolicyDeleteResponse:
        """Soft-deletes the spend policy.

        The policy is disabled and no longer appears in
        list, get or audit responses. The `If-Match` header must equal the policy's
        current `version`.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          policy_id: The unique identifier of the spend policy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/accounts/{account_id}/billing/spend-policies/{policy_id}", account_id=account_id, policy_id=policy_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SpendPolicyDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[SpendPolicyDeleteResponse], ResultWrapper[SpendPolicyDeleteResponse]),
        )

    async def get(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendPolicyGetResponse:
        """Returns one spend policy.

        The `ETag` response header holds the current
        `version`; send it as `If-Match` on a later update or delete.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          policy_id: The unique identifier of the spend policy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/billing/spend-policies/{policy_id}", account_id=account_id, policy_id=policy_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SpendPolicyGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SpendPolicyGetResponse], ResultWrapper[SpendPolicyGetResponse]),
        )


class SpendPoliciesResourceWithRawResponse:
    def __init__(self, spend_policies: SpendPoliciesResource) -> None:
        self._spend_policies = spend_policies

        self.create = to_raw_response_wrapper(
            spend_policies.create,
        )
        self.update = to_raw_response_wrapper(
            spend_policies.update,
        )
        self.list = to_raw_response_wrapper(
            spend_policies.list,
        )
        self.delete = to_raw_response_wrapper(
            spend_policies.delete,
        )
        self.get = to_raw_response_wrapper(
            spend_policies.get,
        )

    @cached_property
    def audit(self) -> AuditResourceWithRawResponse:
        return AuditResourceWithRawResponse(self._spend_policies.audit)

    @cached_property
    def activity(self) -> ActivityResourceWithRawResponse:
        return ActivityResourceWithRawResponse(self._spend_policies.activity)


class AsyncSpendPoliciesResourceWithRawResponse:
    def __init__(self, spend_policies: AsyncSpendPoliciesResource) -> None:
        self._spend_policies = spend_policies

        self.create = async_to_raw_response_wrapper(
            spend_policies.create,
        )
        self.update = async_to_raw_response_wrapper(
            spend_policies.update,
        )
        self.list = async_to_raw_response_wrapper(
            spend_policies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            spend_policies.delete,
        )
        self.get = async_to_raw_response_wrapper(
            spend_policies.get,
        )

    @cached_property
    def audit(self) -> AsyncAuditResourceWithRawResponse:
        return AsyncAuditResourceWithRawResponse(self._spend_policies.audit)

    @cached_property
    def activity(self) -> AsyncActivityResourceWithRawResponse:
        return AsyncActivityResourceWithRawResponse(self._spend_policies.activity)


class SpendPoliciesResourceWithStreamingResponse:
    def __init__(self, spend_policies: SpendPoliciesResource) -> None:
        self._spend_policies = spend_policies

        self.create = to_streamed_response_wrapper(
            spend_policies.create,
        )
        self.update = to_streamed_response_wrapper(
            spend_policies.update,
        )
        self.list = to_streamed_response_wrapper(
            spend_policies.list,
        )
        self.delete = to_streamed_response_wrapper(
            spend_policies.delete,
        )
        self.get = to_streamed_response_wrapper(
            spend_policies.get,
        )

    @cached_property
    def audit(self) -> AuditResourceWithStreamingResponse:
        return AuditResourceWithStreamingResponse(self._spend_policies.audit)

    @cached_property
    def activity(self) -> ActivityResourceWithStreamingResponse:
        return ActivityResourceWithStreamingResponse(self._spend_policies.activity)


class AsyncSpendPoliciesResourceWithStreamingResponse:
    def __init__(self, spend_policies: AsyncSpendPoliciesResource) -> None:
        self._spend_policies = spend_policies

        self.create = async_to_streamed_response_wrapper(
            spend_policies.create,
        )
        self.update = async_to_streamed_response_wrapper(
            spend_policies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            spend_policies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            spend_policies.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            spend_policies.get,
        )

    @cached_property
    def audit(self) -> AsyncAuditResourceWithStreamingResponse:
        return AsyncAuditResourceWithStreamingResponse(self._spend_policies.audit)

    @cached_property
    def activity(self) -> AsyncActivityResourceWithStreamingResponse:
        return AsyncActivityResourceWithStreamingResponse(self._spend_policies.activity)
