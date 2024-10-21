# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.zero_trust.access import Decision
from ......types.zero_trust.access.decision import Decision
from ......types.zero_trust.access_rule_param import AccessRuleParam
from ......types.zero_trust.access.applications import policy_test_create_params
from ......types.zero_trust.access.approval_group_param import ApprovalGroupParam
from ......types.zero_trust.access.applications.policy_test_get_response import PolicyTestGetResponse
from ......types.zero_trust.access.applications.policy_test_create_response import PolicyTestCreateResponse

__all__ = ["PolicyTestsResource", "AsyncPolicyTestsResource"]


class PolicyTestsResource(SyncAPIResource):
    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> PolicyTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PolicyTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolicyTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PolicyTestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        approval_groups: Iterable[ApprovalGroupParam] | NotGiven = NOT_GIVEN,
        approval_required: bool | NotGiven = NOT_GIVEN,
        connection_rules: policy_test_create_params.ConnectionRules | NotGiven = NOT_GIVEN,
        decision: Decision | NotGiven = NOT_GIVEN,
        exclude: Iterable[AccessRuleParam] | NotGiven = NOT_GIVEN,
        include: Iterable[AccessRuleParam] | NotGiven = NOT_GIVEN,
        isolation_required: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        purpose_justification_prompt: str | NotGiven = NOT_GIVEN,
        purpose_justification_required: bool | NotGiven = NOT_GIVEN,
        require: Iterable[AccessRuleParam] | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyTestCreateResponse:
        """
        Starts an Access policy test.

        Args:
          account_id: Identifier

          id: The UUID of the policy

          approval_groups: Administrators who can approve a temporary authentication request.

          approval_required: Requires the user to request access from an administrator at the start of each
              session.

          connection_rules: The rules that define how users may connect to the targets secured by your
              application.

          decision: The action Access will take if a user matches this policy.

          exclude: Rules evaluated with a NOT logical operator. To match the policy, a user cannot
              meet any of the Exclude rules.

          include: Rules evaluated with an OR logical operator. A user needs to meet only one of
              the Include rules.

          isolation_required: Require this application to be served in an isolated browser for users matching
              this policy. 'Client Web Isolation' must be on for the account in order to use
              this feature.

          name: The name of the Access policy.

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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/access/policy-tests",
            body=maybe_transform(
                {
                    "id": id,
                    "approval_groups": approval_groups,
                    "approval_required": approval_required,
                    "connection_rules": connection_rules,
                    "decision": decision,
                    "exclude": exclude,
                    "include": include,
                    "isolation_required": isolation_required,
                    "name": name,
                    "purpose_justification_prompt": purpose_justification_prompt,
                    "purpose_justification_required": purpose_justification_required,
                    "require": require,
                    "session_duration": session_duration,
                },
                policy_test_create_params.PolicyTestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyTestCreateResponse,
        )

    def get(
        self,
        policy_test_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyTestGetResponse:
        """
        Fetches the current status of a given Access policy test.

        Args:
          account_id: Identifier

          policy_test_id: The UUID of the policy test.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_test_id:
            raise ValueError(f"Expected a non-empty value for `policy_test_id` but received {policy_test_id!r}")
        return self._get(
            f"/accounts/{account_id}/access/policy-tests/{policy_test_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyTestGetResponse,
        )


class AsyncPolicyTestsResource(AsyncAPIResource):
    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPolicyTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPolicyTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolicyTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPolicyTestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        approval_groups: Iterable[ApprovalGroupParam] | NotGiven = NOT_GIVEN,
        approval_required: bool | NotGiven = NOT_GIVEN,
        connection_rules: policy_test_create_params.ConnectionRules | NotGiven = NOT_GIVEN,
        decision: Decision | NotGiven = NOT_GIVEN,
        exclude: Iterable[AccessRuleParam] | NotGiven = NOT_GIVEN,
        include: Iterable[AccessRuleParam] | NotGiven = NOT_GIVEN,
        isolation_required: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        purpose_justification_prompt: str | NotGiven = NOT_GIVEN,
        purpose_justification_required: bool | NotGiven = NOT_GIVEN,
        require: Iterable[AccessRuleParam] | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyTestCreateResponse:
        """
        Starts an Access policy test.

        Args:
          account_id: Identifier

          id: The UUID of the policy

          approval_groups: Administrators who can approve a temporary authentication request.

          approval_required: Requires the user to request access from an administrator at the start of each
              session.

          connection_rules: The rules that define how users may connect to the targets secured by your
              application.

          decision: The action Access will take if a user matches this policy.

          exclude: Rules evaluated with a NOT logical operator. To match the policy, a user cannot
              meet any of the Exclude rules.

          include: Rules evaluated with an OR logical operator. A user needs to meet only one of
              the Include rules.

          isolation_required: Require this application to be served in an isolated browser for users matching
              this policy. 'Client Web Isolation' must be on for the account in order to use
              this feature.

          name: The name of the Access policy.

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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/access/policy-tests",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "approval_groups": approval_groups,
                    "approval_required": approval_required,
                    "connection_rules": connection_rules,
                    "decision": decision,
                    "exclude": exclude,
                    "include": include,
                    "isolation_required": isolation_required,
                    "name": name,
                    "purpose_justification_prompt": purpose_justification_prompt,
                    "purpose_justification_required": purpose_justification_required,
                    "require": require,
                    "session_duration": session_duration,
                },
                policy_test_create_params.PolicyTestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyTestCreateResponse,
        )

    async def get(
        self,
        policy_test_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyTestGetResponse:
        """
        Fetches the current status of a given Access policy test.

        Args:
          account_id: Identifier

          policy_test_id: The UUID of the policy test.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_test_id:
            raise ValueError(f"Expected a non-empty value for `policy_test_id` but received {policy_test_id!r}")
        return await self._get(
            f"/accounts/{account_id}/access/policy-tests/{policy_test_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyTestGetResponse,
        )


class PolicyTestsResourceWithRawResponse:
    def __init__(self, policy_tests: PolicyTestsResource) -> None:
        self._policy_tests = policy_tests

        self.create = to_raw_response_wrapper(
            policy_tests.create,
        )
        self.get = to_raw_response_wrapper(
            policy_tests.get,
        )

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._policy_tests.users)


class AsyncPolicyTestsResourceWithRawResponse:
    def __init__(self, policy_tests: AsyncPolicyTestsResource) -> None:
        self._policy_tests = policy_tests

        self.create = async_to_raw_response_wrapper(
            policy_tests.create,
        )
        self.get = async_to_raw_response_wrapper(
            policy_tests.get,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._policy_tests.users)


class PolicyTestsResourceWithStreamingResponse:
    def __init__(self, policy_tests: PolicyTestsResource) -> None:
        self._policy_tests = policy_tests

        self.create = to_streamed_response_wrapper(
            policy_tests.create,
        )
        self.get = to_streamed_response_wrapper(
            policy_tests.get,
        )

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._policy_tests.users)


class AsyncPolicyTestsResourceWithStreamingResponse:
    def __init__(self, policy_tests: AsyncPolicyTestsResource) -> None:
        self._policy_tests = policy_tests

        self.create = async_to_streamed_response_wrapper(
            policy_tests.create,
        )
        self.get = async_to_streamed_response_wrapper(
            policy_tests.get,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._policy_tests.users)
