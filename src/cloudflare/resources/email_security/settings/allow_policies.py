# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

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
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.email_security.settings import (
    allow_policy_edit_params,
    allow_policy_list_params,
    allow_policy_create_params,
)
from ....types.email_security.settings.allow_policy_get_response import AllowPolicyGetResponse
from ....types.email_security.settings.allow_policy_edit_response import AllowPolicyEditResponse
from ....types.email_security.settings.allow_policy_list_response import AllowPolicyListResponse
from ....types.email_security.settings.allow_policy_create_response import AllowPolicyCreateResponse
from ....types.email_security.settings.allow_policy_delete_response import AllowPolicyDeleteResponse

__all__ = ["AllowPoliciesResource", "AsyncAllowPoliciesResource"]


class AllowPoliciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AllowPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AllowPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AllowPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AllowPoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        is_acceptable_sender: bool,
        is_exempt_recipient: bool,
        is_regex: bool,
        is_trusted_sender: bool,
        pattern: str,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"],
        verify_sender: bool,
        comments: Optional[str] | Omit = omit,
        is_recipient: bool | Omit = omit,
        is_sender: bool | Omit = omit,
        is_spoof: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AllowPolicyCreateResponse]:
        """Creates a new allow policy that exempts matching emails from security
        detections.

        Use with caution as this bypasses email security scanning. Policies
        can match on sender patterns and apply to specific detections or all detections.

        Args:
          account_id: Identifier.

          is_acceptable_sender: Messages from this sender will be exempted from Spam, Spoof and Bulk
              dispositions. Note - This will not exempt messages with Malicious or Suspicious
              dispositions.

          is_exempt_recipient: Messages to this recipient will bypass all detections

          is_trusted_sender: Messages from this sender will bypass all detections and link following

          pattern_type: Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when
              creating or updating policies, but may be returned for existing entries.

          verify_sender: Enforce DMARC, SPF or DKIM authentication. When on, Email Security only honors
              policies that pass authentication.

          is_recipient:
              Deprecated as of July 1, 2025. Use `is_exempt_recipient` instead. End of life:
              July 1, 2026.

          is_sender:
              Deprecated as of July 1, 2025. Use `is_trusted_sender` instead. End of life:
              July 1, 2026.

          is_spoof:
              Deprecated as of July 1, 2025. Use `is_acceptable_sender` instead. End of life:
              July 1, 2026.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/email-security/settings/allow_policies", account_id=account_id),
            body=maybe_transform(
                {
                    "is_acceptable_sender": is_acceptable_sender,
                    "is_exempt_recipient": is_exempt_recipient,
                    "is_regex": is_regex,
                    "is_trusted_sender": is_trusted_sender,
                    "pattern": pattern,
                    "pattern_type": pattern_type,
                    "verify_sender": verify_sender,
                    "comments": comments,
                    "is_recipient": is_recipient,
                    "is_sender": is_sender,
                    "is_spoof": is_spoof,
                },
                allow_policy_create_params.AllowPolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AllowPolicyCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AllowPolicyCreateResponse]], ResultWrapper[AllowPolicyCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        is_acceptable_sender: bool | Omit = omit,
        is_exempt_recipient: bool | Omit = omit,
        is_trusted_sender: bool | Omit = omit,
        order: Literal["pattern", "created_at"] | Omit = omit,
        page: int | Omit = omit,
        pattern: str | Omit = omit,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        verify_sender: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[AllowPolicyListResponse]:
        """Returns a paginated list of email allow policies.

        These policies exempt matching
        emails from security detection, allowing them to bypass disposition actions.
        Supports filtering by pattern type and policy attributes.

        Args:
          account_id: Identifier.

          direction: The sorting direction.

          is_acceptable_sender: Filter to show only policies where messages from the sender are exempted from
              Spam, Spoof, and Bulk dispositions (not Malicious or Suspicious).

          is_exempt_recipient: Filter to show only policies where messages to the recipient bypass all
              detections.

          is_trusted_sender: Filter to show only policies where messages from the sender bypass all
              detections and link following.

          order: Field to sort by.

          page: Current page within paginated list of results.

          pattern_type: Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when
              creating or updating policies, but may be returned for existing entries.

          per_page: The number of results per page. Maximum value is 1000.

          search: Search term for filtering records. Behavior may change.

          verify_sender: Filter to show only policies that enforce DMARC, SPF, or DKIM authentication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/settings/allow_policies", account_id=account_id),
            page=SyncV4PagePaginationArray[AllowPolicyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "is_acceptable_sender": is_acceptable_sender,
                        "is_exempt_recipient": is_exempt_recipient,
                        "is_trusted_sender": is_trusted_sender,
                        "order": order,
                        "page": page,
                        "pattern": pattern,
                        "pattern_type": pattern_type,
                        "per_page": per_page,
                        "search": search,
                        "verify_sender": verify_sender,
                    },
                    allow_policy_list_params.AllowPolicyListParams,
                ),
            ),
            model=AllowPolicyListResponse,
        )

    def delete(
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
    ) -> Optional[AllowPolicyDeleteResponse]:
        """Removes an allow policy.

        After deletion, emails matching this pattern will be
        subject to normal security scanning and disposition actions.

        Args:
          account_id: Identifier.

          policy_id: Allow policy identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/allow_policies/{policy_id}",
                account_id=account_id,
                policy_id=policy_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AllowPolicyDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AllowPolicyDeleteResponse]], ResultWrapper[AllowPolicyDeleteResponse]),
        )

    def edit(
        self,
        policy_id: str,
        *,
        account_id: str,
        comments: Optional[str] | Omit = omit,
        is_acceptable_sender: bool | Omit = omit,
        is_exempt_recipient: bool | Omit = omit,
        is_recipient: bool | Omit = omit,
        is_regex: bool | Omit = omit,
        is_sender: bool | Omit = omit,
        is_spoof: bool | Omit = omit,
        is_trusted_sender: bool | Omit = omit,
        pattern: str | Omit = omit,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | Omit = omit,
        verify_sender: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AllowPolicyEditResponse]:
        """Updates an existing allow policy.

        Only provided fields will be modified. Changes
        take effect for new emails matching the pattern.

        Args:
          account_id: Identifier.

          policy_id: Allow policy identifier

          is_acceptable_sender: Messages from this sender will be exempted from Spam, Spoof and Bulk
              dispositions. Note - This will not exempt messages with Malicious or Suspicious
              dispositions.

          is_exempt_recipient: Messages to this recipient will bypass all detections

          is_recipient:
              Deprecated as of July 1, 2025. Use `is_exempt_recipient` instead. End of life:
              July 1, 2026.

          is_sender:
              Deprecated as of July 1, 2025. Use `is_trusted_sender` instead. End of life:
              July 1, 2026.

          is_spoof:
              Deprecated as of July 1, 2025. Use `is_acceptable_sender` instead. End of life:
              July 1, 2026.

          is_trusted_sender: Messages from this sender will bypass all detections and link following

          pattern_type: Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when
              creating or updating policies, but may be returned for existing entries.

          verify_sender: Enforce DMARC, SPF or DKIM authentication. When on, Email Security only honors
              policies that pass authentication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/allow_policies/{policy_id}",
                account_id=account_id,
                policy_id=policy_id,
            ),
            body=maybe_transform(
                {
                    "comments": comments,
                    "is_acceptable_sender": is_acceptable_sender,
                    "is_exempt_recipient": is_exempt_recipient,
                    "is_recipient": is_recipient,
                    "is_regex": is_regex,
                    "is_sender": is_sender,
                    "is_spoof": is_spoof,
                    "is_trusted_sender": is_trusted_sender,
                    "pattern": pattern,
                    "pattern_type": pattern_type,
                    "verify_sender": verify_sender,
                },
                allow_policy_edit_params.AllowPolicyEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AllowPolicyEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AllowPolicyEditResponse]], ResultWrapper[AllowPolicyEditResponse]),
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
    ) -> Optional[AllowPolicyGetResponse]:
        """
        Retrieves details for a specific allow policy including its pattern,
        dispositions that are exempted, and whether it applies to all detections.

        Args:
          account_id: Identifier.

          policy_id: Allow policy identifier

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
                "/accounts/{account_id}/email-security/settings/allow_policies/{policy_id}",
                account_id=account_id,
                policy_id=policy_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AllowPolicyGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AllowPolicyGetResponse]], ResultWrapper[AllowPolicyGetResponse]),
        )


class AsyncAllowPoliciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAllowPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAllowPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAllowPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAllowPoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        is_acceptable_sender: bool,
        is_exempt_recipient: bool,
        is_regex: bool,
        is_trusted_sender: bool,
        pattern: str,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"],
        verify_sender: bool,
        comments: Optional[str] | Omit = omit,
        is_recipient: bool | Omit = omit,
        is_sender: bool | Omit = omit,
        is_spoof: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AllowPolicyCreateResponse]:
        """Creates a new allow policy that exempts matching emails from security
        detections.

        Use with caution as this bypasses email security scanning. Policies
        can match on sender patterns and apply to specific detections or all detections.

        Args:
          account_id: Identifier.

          is_acceptable_sender: Messages from this sender will be exempted from Spam, Spoof and Bulk
              dispositions. Note - This will not exempt messages with Malicious or Suspicious
              dispositions.

          is_exempt_recipient: Messages to this recipient will bypass all detections

          is_trusted_sender: Messages from this sender will bypass all detections and link following

          pattern_type: Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when
              creating or updating policies, but may be returned for existing entries.

          verify_sender: Enforce DMARC, SPF or DKIM authentication. When on, Email Security only honors
              policies that pass authentication.

          is_recipient:
              Deprecated as of July 1, 2025. Use `is_exempt_recipient` instead. End of life:
              July 1, 2026.

          is_sender:
              Deprecated as of July 1, 2025. Use `is_trusted_sender` instead. End of life:
              July 1, 2026.

          is_spoof:
              Deprecated as of July 1, 2025. Use `is_acceptable_sender` instead. End of life:
              July 1, 2026.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/email-security/settings/allow_policies", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "is_acceptable_sender": is_acceptable_sender,
                    "is_exempt_recipient": is_exempt_recipient,
                    "is_regex": is_regex,
                    "is_trusted_sender": is_trusted_sender,
                    "pattern": pattern,
                    "pattern_type": pattern_type,
                    "verify_sender": verify_sender,
                    "comments": comments,
                    "is_recipient": is_recipient,
                    "is_sender": is_sender,
                    "is_spoof": is_spoof,
                },
                allow_policy_create_params.AllowPolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AllowPolicyCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AllowPolicyCreateResponse]], ResultWrapper[AllowPolicyCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        is_acceptable_sender: bool | Omit = omit,
        is_exempt_recipient: bool | Omit = omit,
        is_trusted_sender: bool | Omit = omit,
        order: Literal["pattern", "created_at"] | Omit = omit,
        page: int | Omit = omit,
        pattern: str | Omit = omit,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        verify_sender: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AllowPolicyListResponse, AsyncV4PagePaginationArray[AllowPolicyListResponse]]:
        """Returns a paginated list of email allow policies.

        These policies exempt matching
        emails from security detection, allowing them to bypass disposition actions.
        Supports filtering by pattern type and policy attributes.

        Args:
          account_id: Identifier.

          direction: The sorting direction.

          is_acceptable_sender: Filter to show only policies where messages from the sender are exempted from
              Spam, Spoof, and Bulk dispositions (not Malicious or Suspicious).

          is_exempt_recipient: Filter to show only policies where messages to the recipient bypass all
              detections.

          is_trusted_sender: Filter to show only policies where messages from the sender bypass all
              detections and link following.

          order: Field to sort by.

          page: Current page within paginated list of results.

          pattern_type: Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when
              creating or updating policies, but may be returned for existing entries.

          per_page: The number of results per page. Maximum value is 1000.

          search: Search term for filtering records. Behavior may change.

          verify_sender: Filter to show only policies that enforce DMARC, SPF, or DKIM authentication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/settings/allow_policies", account_id=account_id),
            page=AsyncV4PagePaginationArray[AllowPolicyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "is_acceptable_sender": is_acceptable_sender,
                        "is_exempt_recipient": is_exempt_recipient,
                        "is_trusted_sender": is_trusted_sender,
                        "order": order,
                        "page": page,
                        "pattern": pattern,
                        "pattern_type": pattern_type,
                        "per_page": per_page,
                        "search": search,
                        "verify_sender": verify_sender,
                    },
                    allow_policy_list_params.AllowPolicyListParams,
                ),
            ),
            model=AllowPolicyListResponse,
        )

    async def delete(
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
    ) -> Optional[AllowPolicyDeleteResponse]:
        """Removes an allow policy.

        After deletion, emails matching this pattern will be
        subject to normal security scanning and disposition actions.

        Args:
          account_id: Identifier.

          policy_id: Allow policy identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/allow_policies/{policy_id}",
                account_id=account_id,
                policy_id=policy_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AllowPolicyDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AllowPolicyDeleteResponse]], ResultWrapper[AllowPolicyDeleteResponse]),
        )

    async def edit(
        self,
        policy_id: str,
        *,
        account_id: str,
        comments: Optional[str] | Omit = omit,
        is_acceptable_sender: bool | Omit = omit,
        is_exempt_recipient: bool | Omit = omit,
        is_recipient: bool | Omit = omit,
        is_regex: bool | Omit = omit,
        is_sender: bool | Omit = omit,
        is_spoof: bool | Omit = omit,
        is_trusted_sender: bool | Omit = omit,
        pattern: str | Omit = omit,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | Omit = omit,
        verify_sender: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AllowPolicyEditResponse]:
        """Updates an existing allow policy.

        Only provided fields will be modified. Changes
        take effect for new emails matching the pattern.

        Args:
          account_id: Identifier.

          policy_id: Allow policy identifier

          is_acceptable_sender: Messages from this sender will be exempted from Spam, Spoof and Bulk
              dispositions. Note - This will not exempt messages with Malicious or Suspicious
              dispositions.

          is_exempt_recipient: Messages to this recipient will bypass all detections

          is_recipient:
              Deprecated as of July 1, 2025. Use `is_exempt_recipient` instead. End of life:
              July 1, 2026.

          is_sender:
              Deprecated as of July 1, 2025. Use `is_trusted_sender` instead. End of life:
              July 1, 2026.

          is_spoof:
              Deprecated as of July 1, 2025. Use `is_acceptable_sender` instead. End of life:
              July 1, 2026.

          is_trusted_sender: Messages from this sender will bypass all detections and link following

          pattern_type: Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when
              creating or updating policies, but may be returned for existing entries.

          verify_sender: Enforce DMARC, SPF or DKIM authentication. When on, Email Security only honors
              policies that pass authentication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/allow_policies/{policy_id}",
                account_id=account_id,
                policy_id=policy_id,
            ),
            body=await async_maybe_transform(
                {
                    "comments": comments,
                    "is_acceptable_sender": is_acceptable_sender,
                    "is_exempt_recipient": is_exempt_recipient,
                    "is_recipient": is_recipient,
                    "is_regex": is_regex,
                    "is_sender": is_sender,
                    "is_spoof": is_spoof,
                    "is_trusted_sender": is_trusted_sender,
                    "pattern": pattern,
                    "pattern_type": pattern_type,
                    "verify_sender": verify_sender,
                },
                allow_policy_edit_params.AllowPolicyEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AllowPolicyEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AllowPolicyEditResponse]], ResultWrapper[AllowPolicyEditResponse]),
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
    ) -> Optional[AllowPolicyGetResponse]:
        """
        Retrieves details for a specific allow policy including its pattern,
        dispositions that are exempted, and whether it applies to all detections.

        Args:
          account_id: Identifier.

          policy_id: Allow policy identifier

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
                "/accounts/{account_id}/email-security/settings/allow_policies/{policy_id}",
                account_id=account_id,
                policy_id=policy_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AllowPolicyGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AllowPolicyGetResponse]], ResultWrapper[AllowPolicyGetResponse]),
        )


class AllowPoliciesResourceWithRawResponse:
    def __init__(self, allow_policies: AllowPoliciesResource) -> None:
        self._allow_policies = allow_policies

        self.create = to_raw_response_wrapper(
            allow_policies.create,
        )
        self.list = to_raw_response_wrapper(
            allow_policies.list,
        )
        self.delete = to_raw_response_wrapper(
            allow_policies.delete,
        )
        self.edit = to_raw_response_wrapper(
            allow_policies.edit,
        )
        self.get = to_raw_response_wrapper(
            allow_policies.get,
        )


class AsyncAllowPoliciesResourceWithRawResponse:
    def __init__(self, allow_policies: AsyncAllowPoliciesResource) -> None:
        self._allow_policies = allow_policies

        self.create = async_to_raw_response_wrapper(
            allow_policies.create,
        )
        self.list = async_to_raw_response_wrapper(
            allow_policies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            allow_policies.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            allow_policies.edit,
        )
        self.get = async_to_raw_response_wrapper(
            allow_policies.get,
        )


class AllowPoliciesResourceWithStreamingResponse:
    def __init__(self, allow_policies: AllowPoliciesResource) -> None:
        self._allow_policies = allow_policies

        self.create = to_streamed_response_wrapper(
            allow_policies.create,
        )
        self.list = to_streamed_response_wrapper(
            allow_policies.list,
        )
        self.delete = to_streamed_response_wrapper(
            allow_policies.delete,
        )
        self.edit = to_streamed_response_wrapper(
            allow_policies.edit,
        )
        self.get = to_streamed_response_wrapper(
            allow_policies.get,
        )


class AsyncAllowPoliciesResourceWithStreamingResponse:
    def __init__(self, allow_policies: AsyncAllowPoliciesResource) -> None:
        self._allow_policies = allow_policies

        self.create = async_to_streamed_response_wrapper(
            allow_policies.create,
        )
        self.list = async_to_streamed_response_wrapper(
            allow_policies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            allow_policies.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            allow_policies.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            allow_policies.get,
        )
