# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

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
from .....types.zero_trust.access.applications import (
    AccessPolicies,
    PolicyListResponse,
    PolicyDeleteResponse,
    policy_create_params,
    policy_update_params,
)

__all__ = ["Policies", "AsyncPolicies"]


class Policies(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PoliciesWithRawResponse:
        return PoliciesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoliciesWithStreamingResponse:
        return PoliciesWithStreamingResponse(self)

    def create(
        self,
        uuid: str,
        *,
        decision: Literal["allow", "deny", "non_identity", "bypass"],
        include: Iterable[policy_create_params.Include],
        name: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        approval_groups: Iterable[policy_create_params.ApprovalGroup] | NotGiven = NOT_GIVEN,
        approval_required: bool | NotGiven = NOT_GIVEN,
        exclude: Iterable[policy_create_params.Exclude] | NotGiven = NOT_GIVEN,
        isolation_required: bool | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        purpose_justification_prompt: str | NotGiven = NOT_GIVEN,
        purpose_justification_required: bool | NotGiven = NOT_GIVEN,
        require: Iterable[policy_create_params.Require] | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessPolicies:
        """
        Create a new Access policy for an application.

        Args:
          uuid: UUID

          decision: The action Access will take if a user matches this policy.

          include: Rules evaluated with an OR logical operator. A user needs to meet only one of
              the Include rules.

          name: The name of the Access policy.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          approval_groups: Administrators who can approve a temporary authentication request.

          approval_required: Requires the user to request access from an administrator at the start of each
              session.

          exclude: Rules evaluated with a NOT logical operator. To match the policy, a user cannot
              meet any of the Exclude rules.

          isolation_required: Require this application to be served in an isolated browser for users matching
              this policy. 'Client Web Isolation' must be on for the account in order to use
              this feature.

          precedence: The order of execution for this policy. Must be unique for each policy.

          purpose_justification_prompt: A custom message that will appear on the purpose justification screen.

          purpose_justification_required: Require users to enter a justification when they log in to the application.

          require: Rules evaluated with an AND logical operator. To match the policy, a user must
              meet all of the Require rules.

          session_duration: The amount of time that tokens issued for the application will be valid. Must be
              in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s,
              m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/policies",
            body=maybe_transform(
                {
                    "decision": decision,
                    "include": include,
                    "name": name,
                    "approval_groups": approval_groups,
                    "approval_required": approval_required,
                    "exclude": exclude,
                    "isolation_required": isolation_required,
                    "precedence": precedence,
                    "purpose_justification_prompt": purpose_justification_prompt,
                    "purpose_justification_required": purpose_justification_required,
                    "require": require,
                    "session_duration": session_duration,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessPolicies], ResultWrapper[AccessPolicies]),
        )

    def update(
        self,
        uuid: str,
        *,
        uuid1: str,
        decision: Literal["allow", "deny", "non_identity", "bypass"],
        include: Iterable[policy_update_params.Include],
        name: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        approval_groups: Iterable[policy_update_params.ApprovalGroup] | NotGiven = NOT_GIVEN,
        approval_required: bool | NotGiven = NOT_GIVEN,
        exclude: Iterable[policy_update_params.Exclude] | NotGiven = NOT_GIVEN,
        isolation_required: bool | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        purpose_justification_prompt: str | NotGiven = NOT_GIVEN,
        purpose_justification_required: bool | NotGiven = NOT_GIVEN,
        require: Iterable[policy_update_params.Require] | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessPolicies:
        """
        Update a configured Access policy.

        Args:
          uuid1: UUID

          uuid: UUID

          decision: The action Access will take if a user matches this policy.

          include: Rules evaluated with an OR logical operator. A user needs to meet only one of
              the Include rules.

          name: The name of the Access policy.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          approval_groups: Administrators who can approve a temporary authentication request.

          approval_required: Requires the user to request access from an administrator at the start of each
              session.

          exclude: Rules evaluated with a NOT logical operator. To match the policy, a user cannot
              meet any of the Exclude rules.

          isolation_required: Require this application to be served in an isolated browser for users matching
              this policy. 'Client Web Isolation' must be on for the account in order to use
              this feature.

          precedence: The order of execution for this policy. Must be unique for each policy.

          purpose_justification_prompt: A custom message that will appear on the purpose justification screen.

          purpose_justification_required: Require users to enter a justification when they log in to the application.

          require: Rules evaluated with an AND logical operator. To match the policy, a user must
              meet all of the Require rules.

          session_duration: The amount of time that tokens issued for the application will be valid. Must be
              in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s,
              m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid1:
            raise ValueError(f"Expected a non-empty value for `uuid1` but received {uuid1!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
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
        return self._put(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid1}/policies/{uuid}",
            body=maybe_transform(
                {
                    "decision": decision,
                    "include": include,
                    "name": name,
                    "approval_groups": approval_groups,
                    "approval_required": approval_required,
                    "exclude": exclude,
                    "isolation_required": isolation_required,
                    "precedence": precedence,
                    "purpose_justification_prompt": purpose_justification_prompt,
                    "purpose_justification_required": purpose_justification_required,
                    "require": require,
                    "session_duration": session_duration,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessPolicies], ResultWrapper[AccessPolicies]),
        )

    def list(
        self,
        uuid: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyListResponse]:
        """
        Lists Access policies configured for an application.

        Args:
          uuid: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/policies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyListResponse]], ResultWrapper[PolicyListResponse]),
        )

    def delete(
        self,
        uuid: str,
        *,
        uuid1: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyDeleteResponse:
        """
        Delete an Access policy.

        Args:
          uuid1: UUID

          uuid: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid1:
            raise ValueError(f"Expected a non-empty value for `uuid1` but received {uuid1!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid1}/policies/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PolicyDeleteResponse], ResultWrapper[PolicyDeleteResponse]),
        )

    def get(
        self,
        uuid: str,
        *,
        uuid1: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessPolicies:
        """
        Fetches a single Access policy.

        Args:
          uuid1: UUID

          uuid: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid1:
            raise ValueError(f"Expected a non-empty value for `uuid1` but received {uuid1!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid1}/policies/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessPolicies], ResultWrapper[AccessPolicies]),
        )


class AsyncPolicies(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPoliciesWithRawResponse:
        return AsyncPoliciesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoliciesWithStreamingResponse:
        return AsyncPoliciesWithStreamingResponse(self)

    async def create(
        self,
        uuid: str,
        *,
        decision: Literal["allow", "deny", "non_identity", "bypass"],
        include: Iterable[policy_create_params.Include],
        name: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        approval_groups: Iterable[policy_create_params.ApprovalGroup] | NotGiven = NOT_GIVEN,
        approval_required: bool | NotGiven = NOT_GIVEN,
        exclude: Iterable[policy_create_params.Exclude] | NotGiven = NOT_GIVEN,
        isolation_required: bool | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        purpose_justification_prompt: str | NotGiven = NOT_GIVEN,
        purpose_justification_required: bool | NotGiven = NOT_GIVEN,
        require: Iterable[policy_create_params.Require] | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessPolicies:
        """
        Create a new Access policy for an application.

        Args:
          uuid: UUID

          decision: The action Access will take if a user matches this policy.

          include: Rules evaluated with an OR logical operator. A user needs to meet only one of
              the Include rules.

          name: The name of the Access policy.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          approval_groups: Administrators who can approve a temporary authentication request.

          approval_required: Requires the user to request access from an administrator at the start of each
              session.

          exclude: Rules evaluated with a NOT logical operator. To match the policy, a user cannot
              meet any of the Exclude rules.

          isolation_required: Require this application to be served in an isolated browser for users matching
              this policy. 'Client Web Isolation' must be on for the account in order to use
              this feature.

          precedence: The order of execution for this policy. Must be unique for each policy.

          purpose_justification_prompt: A custom message that will appear on the purpose justification screen.

          purpose_justification_required: Require users to enter a justification when they log in to the application.

          require: Rules evaluated with an AND logical operator. To match the policy, a user must
              meet all of the Require rules.

          session_duration: The amount of time that tokens issued for the application will be valid. Must be
              in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s,
              m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/policies",
            body=await async_maybe_transform(
                {
                    "decision": decision,
                    "include": include,
                    "name": name,
                    "approval_groups": approval_groups,
                    "approval_required": approval_required,
                    "exclude": exclude,
                    "isolation_required": isolation_required,
                    "precedence": precedence,
                    "purpose_justification_prompt": purpose_justification_prompt,
                    "purpose_justification_required": purpose_justification_required,
                    "require": require,
                    "session_duration": session_duration,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessPolicies], ResultWrapper[AccessPolicies]),
        )

    async def update(
        self,
        uuid: str,
        *,
        uuid1: str,
        decision: Literal["allow", "deny", "non_identity", "bypass"],
        include: Iterable[policy_update_params.Include],
        name: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        approval_groups: Iterable[policy_update_params.ApprovalGroup] | NotGiven = NOT_GIVEN,
        approval_required: bool | NotGiven = NOT_GIVEN,
        exclude: Iterable[policy_update_params.Exclude] | NotGiven = NOT_GIVEN,
        isolation_required: bool | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        purpose_justification_prompt: str | NotGiven = NOT_GIVEN,
        purpose_justification_required: bool | NotGiven = NOT_GIVEN,
        require: Iterable[policy_update_params.Require] | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessPolicies:
        """
        Update a configured Access policy.

        Args:
          uuid1: UUID

          uuid: UUID

          decision: The action Access will take if a user matches this policy.

          include: Rules evaluated with an OR logical operator. A user needs to meet only one of
              the Include rules.

          name: The name of the Access policy.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          approval_groups: Administrators who can approve a temporary authentication request.

          approval_required: Requires the user to request access from an administrator at the start of each
              session.

          exclude: Rules evaluated with a NOT logical operator. To match the policy, a user cannot
              meet any of the Exclude rules.

          isolation_required: Require this application to be served in an isolated browser for users matching
              this policy. 'Client Web Isolation' must be on for the account in order to use
              this feature.

          precedence: The order of execution for this policy. Must be unique for each policy.

          purpose_justification_prompt: A custom message that will appear on the purpose justification screen.

          purpose_justification_required: Require users to enter a justification when they log in to the application.

          require: Rules evaluated with an AND logical operator. To match the policy, a user must
              meet all of the Require rules.

          session_duration: The amount of time that tokens issued for the application will be valid. Must be
              in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s,
              m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid1:
            raise ValueError(f"Expected a non-empty value for `uuid1` but received {uuid1!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
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
        return await self._put(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid1}/policies/{uuid}",
            body=await async_maybe_transform(
                {
                    "decision": decision,
                    "include": include,
                    "name": name,
                    "approval_groups": approval_groups,
                    "approval_required": approval_required,
                    "exclude": exclude,
                    "isolation_required": isolation_required,
                    "precedence": precedence,
                    "purpose_justification_prompt": purpose_justification_prompt,
                    "purpose_justification_required": purpose_justification_required,
                    "require": require,
                    "session_duration": session_duration,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessPolicies], ResultWrapper[AccessPolicies]),
        )

    async def list(
        self,
        uuid: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyListResponse]:
        """
        Lists Access policies configured for an application.

        Args:
          uuid: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/policies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyListResponse]], ResultWrapper[PolicyListResponse]),
        )

    async def delete(
        self,
        uuid: str,
        *,
        uuid1: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyDeleteResponse:
        """
        Delete an Access policy.

        Args:
          uuid1: UUID

          uuid: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid1:
            raise ValueError(f"Expected a non-empty value for `uuid1` but received {uuid1!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid1}/policies/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PolicyDeleteResponse], ResultWrapper[PolicyDeleteResponse]),
        )

    async def get(
        self,
        uuid: str,
        *,
        uuid1: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessPolicies:
        """
        Fetches a single Access policy.

        Args:
          uuid1: UUID

          uuid: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid1:
            raise ValueError(f"Expected a non-empty value for `uuid1` but received {uuid1!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid1}/policies/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AccessPolicies], ResultWrapper[AccessPolicies]),
        )


class PoliciesWithRawResponse:
    def __init__(self, policies: Policies) -> None:
        self._policies = policies

        self.create = to_raw_response_wrapper(
            policies.create,
        )
        self.update = to_raw_response_wrapper(
            policies.update,
        )
        self.list = to_raw_response_wrapper(
            policies.list,
        )
        self.delete = to_raw_response_wrapper(
            policies.delete,
        )
        self.get = to_raw_response_wrapper(
            policies.get,
        )


class AsyncPoliciesWithRawResponse:
    def __init__(self, policies: AsyncPolicies) -> None:
        self._policies = policies

        self.create = async_to_raw_response_wrapper(
            policies.create,
        )
        self.update = async_to_raw_response_wrapper(
            policies.update,
        )
        self.list = async_to_raw_response_wrapper(
            policies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            policies.delete,
        )
        self.get = async_to_raw_response_wrapper(
            policies.get,
        )


class PoliciesWithStreamingResponse:
    def __init__(self, policies: Policies) -> None:
        self._policies = policies

        self.create = to_streamed_response_wrapper(
            policies.create,
        )
        self.update = to_streamed_response_wrapper(
            policies.update,
        )
        self.list = to_streamed_response_wrapper(
            policies.list,
        )
        self.delete = to_streamed_response_wrapper(
            policies.delete,
        )
        self.get = to_streamed_response_wrapper(
            policies.get,
        )


class AsyncPoliciesWithStreamingResponse:
    def __init__(self, policies: AsyncPolicies) -> None:
        self._policies = policies

        self.create = async_to_streamed_response_wrapper(
            policies.create,
        )
        self.update = async_to_streamed_response_wrapper(
            policies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            policies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            policies.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            policies.get,
        )
