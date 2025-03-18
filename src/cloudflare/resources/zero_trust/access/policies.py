# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ....types.zero_trust.access import Decision, policy_create_params, policy_update_params
from ....types.zero_trust.access.decision import Decision
from ....types.zero_trust.access.policy_get_response import PolicyGetResponse
from ....types.zero_trust.access.approval_group_param import ApprovalGroupParam
from ....types.zero_trust.access.policy_list_response import PolicyListResponse
from ....types.zero_trust.access.policy_create_response import PolicyCreateResponse
from ....types.zero_trust.access.policy_delete_response import PolicyDeleteResponse
from ....types.zero_trust.access.policy_update_response import PolicyUpdateResponse
from ....types.zero_trust.access.applications.access_rule_param import AccessRuleParam

__all__ = ["PoliciesResource", "AsyncPoliciesResource"]


class PoliciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        decision: Decision,
        include: Iterable[AccessRuleParam],
        name: str,
        approval_groups: Iterable[ApprovalGroupParam] | NotGiven = NOT_GIVEN,
        approval_required: bool | NotGiven = NOT_GIVEN,
        exclude: Iterable[AccessRuleParam] | NotGiven = NOT_GIVEN,
        isolation_required: bool | NotGiven = NOT_GIVEN,
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
    ) -> Optional[PolicyCreateResponse]:
        """
        Creates a new Access reusable policy.

        Args:
          account_id: Identifier

          decision: The action Access will take if a user matches this policy. Infrastructure
              application policies can only use the Allow action.

          include: Rules evaluated with an OR logical operator. A user needs to meet only one of
              the Include rules.

          name: The name of the Access policy.

          approval_groups: Administrators who can approve a temporary authentication request.

          approval_required: Requires the user to request access from an administrator at the start of each
              session.

          exclude: Rules evaluated with a NOT logical operator. To match the policy, a user cannot
              meet any of the Exclude rules.

          isolation_required: Require this application to be served in an isolated browser for users matching
              this policy. 'Client Web Isolation' must be on for the account in order to use
              this feature.

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
            f"/accounts/{account_id}/access/policies",
            body=maybe_transform(
                {
                    "decision": decision,
                    "include": include,
                    "name": name,
                    "approval_groups": approval_groups,
                    "approval_required": approval_required,
                    "exclude": exclude,
                    "isolation_required": isolation_required,
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
                post_parser=ResultWrapper[Optional[PolicyCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyCreateResponse]], ResultWrapper[PolicyCreateResponse]),
        )

    def update(
        self,
        policy_id: str,
        *,
        account_id: str,
        decision: Decision,
        include: Iterable[AccessRuleParam],
        name: str,
        approval_groups: Iterable[ApprovalGroupParam] | NotGiven = NOT_GIVEN,
        approval_required: bool | NotGiven = NOT_GIVEN,
        exclude: Iterable[AccessRuleParam] | NotGiven = NOT_GIVEN,
        isolation_required: bool | NotGiven = NOT_GIVEN,
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
    ) -> Optional[PolicyUpdateResponse]:
        """
        Updates a Access reusable policy.

        Args:
          account_id: Identifier

          policy_id: The UUID of the policy

          decision: The action Access will take if a user matches this policy. Infrastructure
              application policies can only use the Allow action.

          include: Rules evaluated with an OR logical operator. A user needs to meet only one of
              the Include rules.

          name: The name of the Access policy.

          approval_groups: Administrators who can approve a temporary authentication request.

          approval_required: Requires the user to request access from an administrator at the start of each
              session.

          exclude: Rules evaluated with a NOT logical operator. To match the policy, a user cannot
              meet any of the Exclude rules.

          isolation_required: Require this application to be served in an isolated browser for users matching
              this policy. 'Client Web Isolation' must be on for the account in order to use
              this feature.

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
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._put(
            f"/accounts/{account_id}/access/policies/{policy_id}",
            body=maybe_transform(
                {
                    "decision": decision,
                    "include": include,
                    "name": name,
                    "approval_groups": approval_groups,
                    "approval_required": approval_required,
                    "exclude": exclude,
                    "isolation_required": isolation_required,
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
                post_parser=ResultWrapper[Optional[PolicyUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyUpdateResponse]], ResultWrapper[PolicyUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[PolicyListResponse]:
        """
        Lists Access reusable policies.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/access/policies",
            page=SyncSinglePage[PolicyListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PolicyListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyDeleteResponse]:
        """
        Deletes an Access reusable policy.

        Args:
          account_id: Identifier

          policy_id: The UUID of the policy

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
            f"/accounts/{account_id}/access/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PolicyDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyDeleteResponse]], ResultWrapper[PolicyDeleteResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyGetResponse]:
        """
        Fetches a single Access reusable policy.

        Args:
          account_id: Identifier

          policy_id: The UUID of the policy

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
            f"/accounts/{account_id}/access/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PolicyGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyGetResponse]], ResultWrapper[PolicyGetResponse]),
        )


class AsyncPoliciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        decision: Decision,
        include: Iterable[AccessRuleParam],
        name: str,
        approval_groups: Iterable[ApprovalGroupParam] | NotGiven = NOT_GIVEN,
        approval_required: bool | NotGiven = NOT_GIVEN,
        exclude: Iterable[AccessRuleParam] | NotGiven = NOT_GIVEN,
        isolation_required: bool | NotGiven = NOT_GIVEN,
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
    ) -> Optional[PolicyCreateResponse]:
        """
        Creates a new Access reusable policy.

        Args:
          account_id: Identifier

          decision: The action Access will take if a user matches this policy. Infrastructure
              application policies can only use the Allow action.

          include: Rules evaluated with an OR logical operator. A user needs to meet only one of
              the Include rules.

          name: The name of the Access policy.

          approval_groups: Administrators who can approve a temporary authentication request.

          approval_required: Requires the user to request access from an administrator at the start of each
              session.

          exclude: Rules evaluated with a NOT logical operator. To match the policy, a user cannot
              meet any of the Exclude rules.

          isolation_required: Require this application to be served in an isolated browser for users matching
              this policy. 'Client Web Isolation' must be on for the account in order to use
              this feature.

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
            f"/accounts/{account_id}/access/policies",
            body=await async_maybe_transform(
                {
                    "decision": decision,
                    "include": include,
                    "name": name,
                    "approval_groups": approval_groups,
                    "approval_required": approval_required,
                    "exclude": exclude,
                    "isolation_required": isolation_required,
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
                post_parser=ResultWrapper[Optional[PolicyCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyCreateResponse]], ResultWrapper[PolicyCreateResponse]),
        )

    async def update(
        self,
        policy_id: str,
        *,
        account_id: str,
        decision: Decision,
        include: Iterable[AccessRuleParam],
        name: str,
        approval_groups: Iterable[ApprovalGroupParam] | NotGiven = NOT_GIVEN,
        approval_required: bool | NotGiven = NOT_GIVEN,
        exclude: Iterable[AccessRuleParam] | NotGiven = NOT_GIVEN,
        isolation_required: bool | NotGiven = NOT_GIVEN,
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
    ) -> Optional[PolicyUpdateResponse]:
        """
        Updates a Access reusable policy.

        Args:
          account_id: Identifier

          policy_id: The UUID of the policy

          decision: The action Access will take if a user matches this policy. Infrastructure
              application policies can only use the Allow action.

          include: Rules evaluated with an OR logical operator. A user needs to meet only one of
              the Include rules.

          name: The name of the Access policy.

          approval_groups: Administrators who can approve a temporary authentication request.

          approval_required: Requires the user to request access from an administrator at the start of each
              session.

          exclude: Rules evaluated with a NOT logical operator. To match the policy, a user cannot
              meet any of the Exclude rules.

          isolation_required: Require this application to be served in an isolated browser for users matching
              this policy. 'Client Web Isolation' must be on for the account in order to use
              this feature.

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
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._put(
            f"/accounts/{account_id}/access/policies/{policy_id}",
            body=await async_maybe_transform(
                {
                    "decision": decision,
                    "include": include,
                    "name": name,
                    "approval_groups": approval_groups,
                    "approval_required": approval_required,
                    "exclude": exclude,
                    "isolation_required": isolation_required,
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
                post_parser=ResultWrapper[Optional[PolicyUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyUpdateResponse]], ResultWrapper[PolicyUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PolicyListResponse, AsyncSinglePage[PolicyListResponse]]:
        """
        Lists Access reusable policies.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/access/policies",
            page=AsyncSinglePage[PolicyListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PolicyListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyDeleteResponse]:
        """
        Deletes an Access reusable policy.

        Args:
          account_id: Identifier

          policy_id: The UUID of the policy

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
            f"/accounts/{account_id}/access/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PolicyDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyDeleteResponse]], ResultWrapper[PolicyDeleteResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyGetResponse]:
        """
        Fetches a single Access reusable policy.

        Args:
          account_id: Identifier

          policy_id: The UUID of the policy

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
            f"/accounts/{account_id}/access/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PolicyGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyGetResponse]], ResultWrapper[PolicyGetResponse]),
        )


class PoliciesResourceWithRawResponse:
    def __init__(self, policies: PoliciesResource) -> None:
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


class AsyncPoliciesResourceWithRawResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
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


class PoliciesResourceWithStreamingResponse:
    def __init__(self, policies: PoliciesResource) -> None:
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


class AsyncPoliciesResourceWithStreamingResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
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
