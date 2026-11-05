# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, cast
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
from ....pagination import SyncCursorPagination, AsyncCursorPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.cws import policy_list_params, policy_create_params, policy_update_params
from ....types.zero_trust.cws.policy import Policy
from ....types.zero_trust.cws.policy_delete_response import PolicyDeleteResponse

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
        entrypoint: str,
        filter: str,
        name: str,
        rego_source: str,
        description: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Policy:
        """
        Creates a policy from inline Rego source, an entrypoint, and a filter
        expression.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          entrypoint: Non-function rule declared in rego_source. Evaluation uses
              data.<package_path>.<entrypoint>.

          filter: Filter expression that determines whether this policy applies. Maximum 4096
              UTF-8 bytes.

          name: Name of the policy

          rego_source: Inline Rego source with a package beginning with "policy." Maximum 16384 UTF-8
              bytes.

          description: Optional free-form description.

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
            path_template("/accounts/{account_id}/cws/policies", account_id=account_id),
            body=maybe_transform(
                {
                    "entrypoint": entrypoint,
                    "filter": filter,
                    "name": name,
                    "rego_source": rego_source,
                    "description": description,
                    "tags": tags,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Policy]._unwrapper,
            ),
            cast_to=cast(Type[Policy], ResultWrapper[Policy]),
        )

    def update(
        self,
        policy_id: str,
        *,
        account_id: str,
        entrypoint: str,
        filter: str,
        name: str,
        rego_source: str,
        description: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Policy:
        """Replaces the policy's configuration.

        Omit tags or use {} to clear them.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          policy_id: ID of the policy to update

          entrypoint: Non-function rule declared in rego_source. Evaluation uses
              data.<package_path>.<entrypoint>.

          filter: Filter expression that determines whether this policy applies. Maximum 4096
              UTF-8 bytes.

          name: Name of the policy

          rego_source: Inline Rego source with a package beginning with "policy." Maximum 16384 UTF-8
              bytes.

          description: Optional free-form description.

          tags: Replacement tag set. Omit or use {} to clear. Keys are limited to 256 UTF-8
              bytes and values to 1024 UTF-8 bytes.

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
            path_template(
                "/accounts/{account_id}/cws/policies/{policy_id}", account_id=account_id, policy_id=policy_id
            ),
            body=maybe_transform(
                {
                    "entrypoint": entrypoint,
                    "filter": filter,
                    "name": name,
                    "rego_source": rego_source,
                    "description": description,
                    "tags": tags,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Policy]._unwrapper,
            ),
            cast_to=cast(Type[Policy], ResultWrapper[Policy]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        package_path: str | Omit = omit,
        per_page: int | Omit = omit,
        policy_set_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[Policy]:
        """
        Returns a paginated list of policies in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          name: Filter by policy name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          package_path: Filter by package path (case-sensitive literal substring match)

          per_page: Number of items per page (1-100, default 20)

          policy_set_id: Filter to policies attached to (members of) this policy set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/policies", account_id=account_id),
            page=SyncCursorPagination[Policy],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "package_path": package_path,
                        "per_page": per_page,
                        "policy_set_id": policy_set_id,
                    },
                    policy_list_params.PolicyListParams,
                ),
            ),
            model=Policy,
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
    ) -> PolicyDeleteResponse:
        """Deletes the policy and cascades its policy-set membership rows.

        The policy sets
        remain.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          policy_id: ID of the policy to delete

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
                "/accounts/{account_id}/cws/policies/{policy_id}", account_id=account_id, policy_id=policy_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PolicyDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[PolicyDeleteResponse], ResultWrapper[PolicyDeleteResponse]),
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
    ) -> Policy:
        """
        Returns the policy with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          policy_id: ID of the policy to retrieve

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
                "/accounts/{account_id}/cws/policies/{policy_id}", account_id=account_id, policy_id=policy_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Policy]._unwrapper,
            ),
            cast_to=cast(Type[Policy], ResultWrapper[Policy]),
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
        entrypoint: str,
        filter: str,
        name: str,
        rego_source: str,
        description: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Policy:
        """
        Creates a policy from inline Rego source, an entrypoint, and a filter
        expression.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          entrypoint: Non-function rule declared in rego_source. Evaluation uses
              data.<package_path>.<entrypoint>.

          filter: Filter expression that determines whether this policy applies. Maximum 4096
              UTF-8 bytes.

          name: Name of the policy

          rego_source: Inline Rego source with a package beginning with "policy." Maximum 16384 UTF-8
              bytes.

          description: Optional free-form description.

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
            path_template("/accounts/{account_id}/cws/policies", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "entrypoint": entrypoint,
                    "filter": filter,
                    "name": name,
                    "rego_source": rego_source,
                    "description": description,
                    "tags": tags,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Policy]._unwrapper,
            ),
            cast_to=cast(Type[Policy], ResultWrapper[Policy]),
        )

    async def update(
        self,
        policy_id: str,
        *,
        account_id: str,
        entrypoint: str,
        filter: str,
        name: str,
        rego_source: str,
        description: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Policy:
        """Replaces the policy's configuration.

        Omit tags or use {} to clear them.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          policy_id: ID of the policy to update

          entrypoint: Non-function rule declared in rego_source. Evaluation uses
              data.<package_path>.<entrypoint>.

          filter: Filter expression that determines whether this policy applies. Maximum 4096
              UTF-8 bytes.

          name: Name of the policy

          rego_source: Inline Rego source with a package beginning with "policy." Maximum 16384 UTF-8
              bytes.

          description: Optional free-form description.

          tags: Replacement tag set. Omit or use {} to clear. Keys are limited to 256 UTF-8
              bytes and values to 1024 UTF-8 bytes.

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
            path_template(
                "/accounts/{account_id}/cws/policies/{policy_id}", account_id=account_id, policy_id=policy_id
            ),
            body=await async_maybe_transform(
                {
                    "entrypoint": entrypoint,
                    "filter": filter,
                    "name": name,
                    "rego_source": rego_source,
                    "description": description,
                    "tags": tags,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Policy]._unwrapper,
            ),
            cast_to=cast(Type[Policy], ResultWrapper[Policy]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        package_path: str | Omit = omit,
        per_page: int | Omit = omit,
        policy_set_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Policy, AsyncCursorPagination[Policy]]:
        """
        Returns a paginated list of policies in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          name: Filter by policy name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          package_path: Filter by package path (case-sensitive literal substring match)

          per_page: Number of items per page (1-100, default 20)

          policy_set_id: Filter to policies attached to (members of) this policy set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/policies", account_id=account_id),
            page=AsyncCursorPagination[Policy],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "package_path": package_path,
                        "per_page": per_page,
                        "policy_set_id": policy_set_id,
                    },
                    policy_list_params.PolicyListParams,
                ),
            ),
            model=Policy,
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
    ) -> PolicyDeleteResponse:
        """Deletes the policy and cascades its policy-set membership rows.

        The policy sets
        remain.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          policy_id: ID of the policy to delete

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
                "/accounts/{account_id}/cws/policies/{policy_id}", account_id=account_id, policy_id=policy_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PolicyDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[PolicyDeleteResponse], ResultWrapper[PolicyDeleteResponse]),
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
    ) -> Policy:
        """
        Returns the policy with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          policy_id: ID of the policy to retrieve

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
                "/accounts/{account_id}/cws/policies/{policy_id}", account_id=account_id, policy_id=policy_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Policy]._unwrapper,
            ),
            cast_to=cast(Type[Policy], ResultWrapper[Policy]),
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
