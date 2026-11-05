# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....pagination import SyncCursorPagination, AsyncCursorPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.cws import policy_set_list_params, policy_set_create_params, policy_set_update_params
from ....types.zero_trust.cws.policy_set import PolicySet
from ....types.zero_trust.cws.policy_set_delete_response import PolicySetDeleteResponse

__all__ = ["PolicySetsResource", "AsyncPolicySetsResource"]


class PolicySetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PolicySetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PolicySetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolicySetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PolicySetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        policies: Optional[Iterable[policy_set_create_params.Policy]],
        description: str | Omit = omit,
        exclude_workload_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_workload_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySet:
        """
        Creates a policy set containing the specified policies and workload targets.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          name: Name of the policy set

          policies: Policies to include with per-membership enforcement mode

          description: Optional free-form description.

          exclude_workload_ids: Workload IDs that exclude matching requests. Exclusions take precedence.

          include_workload_ids: Workload IDs that include matching requests. Empty or omitted includes all
              requests before exclusions.

          tags: Tags to attach. Keys are limited to 256 UTF-8 bytes and values to 1024 UTF-8
              bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cws/policy-sets", account_id=account_id),
            body=maybe_transform(
                {
                    "name": name,
                    "policies": policies,
                    "description": description,
                    "exclude_workload_ids": exclude_workload_ids,
                    "include_workload_ids": include_workload_ids,
                    "tags": tags,
                },
                policy_set_create_params.PolicySetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PolicySet]._unwrapper,
            ),
            cast_to=cast(Type[PolicySet], ResultWrapper[PolicySet]),
        )

    def update(
        self,
        policy_set_id: str,
        *,
        account_id: str,
        name: str,
        policies: Optional[Iterable[policy_set_update_params.Policy]],
        description: str | Omit = omit,
        exclude_workload_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_workload_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySet:
        """Replaces the policy set's configuration.

        Omit tags or use {} to clear them.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          policy_set_id: ID of the policy set to update

          name: Name of the policy set

          policies: Replacement set of policies with per-membership enforcement mode

          description: Optional free-form description.

          exclude_workload_ids: Replacement set of excluded workload IDs. Exclusions take precedence.

          include_workload_ids: Replacement set of included workload IDs. Empty or omitted includes all requests
              before exclusions.

          tags: Replacement tag set. Omit or use {} to clear. Keys are limited to 256 UTF-8
              bytes and values to 1024 UTF-8 bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/cws/policy-sets/{policy_set_id}",
                account_id=account_id,
                policy_set_id=policy_set_id,
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "policies": policies,
                    "description": description,
                    "exclude_workload_ids": exclude_workload_ids,
                    "include_workload_ids": include_workload_ids,
                    "tags": tags,
                },
                policy_set_update_params.PolicySetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PolicySet]._unwrapper,
            ),
            cast_to=cast(Type[PolicySet], ResultWrapper[PolicySet]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        deployment_id: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[PolicySet]:
        """
        Returns a paginated list of policy sets in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          deployment_id: Filter to policy sets attached to this deployment

          direction: Sort direction (default: asc)

          name: Filter by policy set name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/policy-sets", account_id=account_id),
            page=SyncCursorPagination[PolicySet],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "deployment_id": deployment_id,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "per_page": per_page,
                    },
                    policy_set_list_params.PolicySetListParams,
                ),
            ),
            model=PolicySet,
        )

    def delete(
        self,
        policy_set_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetDeleteResponse:
        """
        Deletes the policy set and cascades its deployment attachment and policy and
        workload membership rows. The referenced deployments, policies, and workloads
        remain.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          policy_set_id: ID of the policy set to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/cws/policy-sets/{policy_set_id}",
                account_id=account_id,
                policy_set_id=policy_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PolicySetDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[PolicySetDeleteResponse], ResultWrapper[PolicySetDeleteResponse]),
        )

    def get(
        self,
        policy_set_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySet:
        """
        Returns the policy set with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          policy_set_id: ID of the policy set to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cws/policy-sets/{policy_set_id}",
                account_id=account_id,
                policy_set_id=policy_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PolicySet]._unwrapper,
            ),
            cast_to=cast(Type[PolicySet], ResultWrapper[PolicySet]),
        )


class AsyncPolicySetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPolicySetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPolicySetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolicySetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPolicySetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        policies: Optional[Iterable[policy_set_create_params.Policy]],
        description: str | Omit = omit,
        exclude_workload_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_workload_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySet:
        """
        Creates a policy set containing the specified policies and workload targets.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          name: Name of the policy set

          policies: Policies to include with per-membership enforcement mode

          description: Optional free-form description.

          exclude_workload_ids: Workload IDs that exclude matching requests. Exclusions take precedence.

          include_workload_ids: Workload IDs that include matching requests. Empty or omitted includes all
              requests before exclusions.

          tags: Tags to attach. Keys are limited to 256 UTF-8 bytes and values to 1024 UTF-8
              bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cws/policy-sets", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "policies": policies,
                    "description": description,
                    "exclude_workload_ids": exclude_workload_ids,
                    "include_workload_ids": include_workload_ids,
                    "tags": tags,
                },
                policy_set_create_params.PolicySetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PolicySet]._unwrapper,
            ),
            cast_to=cast(Type[PolicySet], ResultWrapper[PolicySet]),
        )

    async def update(
        self,
        policy_set_id: str,
        *,
        account_id: str,
        name: str,
        policies: Optional[Iterable[policy_set_update_params.Policy]],
        description: str | Omit = omit,
        exclude_workload_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_workload_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySet:
        """Replaces the policy set's configuration.

        Omit tags or use {} to clear them.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          policy_set_id: ID of the policy set to update

          name: Name of the policy set

          policies: Replacement set of policies with per-membership enforcement mode

          description: Optional free-form description.

          exclude_workload_ids: Replacement set of excluded workload IDs. Exclusions take precedence.

          include_workload_ids: Replacement set of included workload IDs. Empty or omitted includes all requests
              before exclusions.

          tags: Replacement tag set. Omit or use {} to clear. Keys are limited to 256 UTF-8
              bytes and values to 1024 UTF-8 bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/cws/policy-sets/{policy_set_id}",
                account_id=account_id,
                policy_set_id=policy_set_id,
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "policies": policies,
                    "description": description,
                    "exclude_workload_ids": exclude_workload_ids,
                    "include_workload_ids": include_workload_ids,
                    "tags": tags,
                },
                policy_set_update_params.PolicySetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PolicySet]._unwrapper,
            ),
            cast_to=cast(Type[PolicySet], ResultWrapper[PolicySet]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        deployment_id: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PolicySet, AsyncCursorPagination[PolicySet]]:
        """
        Returns a paginated list of policy sets in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          deployment_id: Filter to policy sets attached to this deployment

          direction: Sort direction (default: asc)

          name: Filter by policy set name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/policy-sets", account_id=account_id),
            page=AsyncCursorPagination[PolicySet],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "deployment_id": deployment_id,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "per_page": per_page,
                    },
                    policy_set_list_params.PolicySetListParams,
                ),
            ),
            model=PolicySet,
        )

    async def delete(
        self,
        policy_set_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySetDeleteResponse:
        """
        Deletes the policy set and cascades its deployment attachment and policy and
        workload membership rows. The referenced deployments, policies, and workloads
        remain.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          policy_set_id: ID of the policy set to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cws/policy-sets/{policy_set_id}",
                account_id=account_id,
                policy_set_id=policy_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PolicySetDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[PolicySetDeleteResponse], ResultWrapper[PolicySetDeleteResponse]),
        )

    async def get(
        self,
        policy_set_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicySet:
        """
        Returns the policy set with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          policy_set_id: ID of the policy set to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_set_id:
            raise ValueError(f"Expected a non-empty value for `policy_set_id` but received {policy_set_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cws/policy-sets/{policy_set_id}",
                account_id=account_id,
                policy_set_id=policy_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PolicySet]._unwrapper,
            ),
            cast_to=cast(Type[PolicySet], ResultWrapper[PolicySet]),
        )


class PolicySetsResourceWithRawResponse:
    def __init__(self, policy_sets: PolicySetsResource) -> None:
        self._policy_sets = policy_sets

        self.create = to_raw_response_wrapper(
            policy_sets.create,
        )
        self.update = to_raw_response_wrapper(
            policy_sets.update,
        )
        self.list = to_raw_response_wrapper(
            policy_sets.list,
        )
        self.delete = to_raw_response_wrapper(
            policy_sets.delete,
        )
        self.get = to_raw_response_wrapper(
            policy_sets.get,
        )


class AsyncPolicySetsResourceWithRawResponse:
    def __init__(self, policy_sets: AsyncPolicySetsResource) -> None:
        self._policy_sets = policy_sets

        self.create = async_to_raw_response_wrapper(
            policy_sets.create,
        )
        self.update = async_to_raw_response_wrapper(
            policy_sets.update,
        )
        self.list = async_to_raw_response_wrapper(
            policy_sets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            policy_sets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            policy_sets.get,
        )


class PolicySetsResourceWithStreamingResponse:
    def __init__(self, policy_sets: PolicySetsResource) -> None:
        self._policy_sets = policy_sets

        self.create = to_streamed_response_wrapper(
            policy_sets.create,
        )
        self.update = to_streamed_response_wrapper(
            policy_sets.update,
        )
        self.list = to_streamed_response_wrapper(
            policy_sets.list,
        )
        self.delete = to_streamed_response_wrapper(
            policy_sets.delete,
        )
        self.get = to_streamed_response_wrapper(
            policy_sets.get,
        )


class AsyncPolicySetsResourceWithStreamingResponse:
    def __init__(self, policy_sets: AsyncPolicySetsResource) -> None:
        self._policy_sets = policy_sets

        self.create = async_to_streamed_response_wrapper(
            policy_sets.create,
        )
        self.update = async_to_streamed_response_wrapper(
            policy_sets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            policy_sets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            policy_sets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            policy_sets.get,
        )
