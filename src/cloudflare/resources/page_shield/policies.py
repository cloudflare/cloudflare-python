# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.page_shield import (
    PolicyListResponse,
    PageShieldPageshieldPolicy,
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
        *,
        zone_id: str,
        action: Literal["allow", "log"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageShieldPageshieldPolicy:
        """
        Create a Page Shield policy.

        Args:
          zone_id: Identifier

          action: The action to take if the expression matches

          description: A description for the policy

          enabled: Whether the policy is enabled

          expression: The expression which must match for the policy to be applied, using the
              Cloudflare Firewall rule expression syntax

          value: The policy which will be applied

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/page_shield/policies",
            body=maybe_transform(
                {
                    "action": action,
                    "description": description,
                    "enabled": enabled,
                    "expression": expression,
                    "value": value,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageShieldPageshieldPolicy,
        )

    def update(
        self,
        policy_id: str,
        *,
        zone_id: str,
        action: Literal["allow", "log"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageShieldPageshieldPolicy:
        """
        Update a Page Shield policy by ID.

        Args:
          zone_id: Identifier

          policy_id: The ID of the policy.

          action: The action to take if the expression matches

          description: A description for the policy

          enabled: Whether the policy is enabled

          expression: The expression which must match for the policy to be applied, using the
              Cloudflare Firewall rule expression syntax

          value: The policy which will be applied

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._put(
            f"/zones/{zone_id}/page_shield/policies/{policy_id}",
            body=maybe_transform(
                {
                    "action": action,
                    "description": description,
                    "enabled": enabled,
                    "expression": expression,
                    "value": value,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageShieldPageshieldPolicy,
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyListResponse]:
        """
        Lists all Page Shield policies.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/page_shield/policies",
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
        policy_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a Page Shield policy by ID.

        Args:
          zone_id: Identifier

          policy_id: The ID of the policy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/zones/{zone_id}/page_shield/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        policy_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageShieldPageshieldPolicy:
        """
        Fetches a Page Shield policy by ID.

        Args:
          zone_id: Identifier

          policy_id: The ID of the policy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get(
            f"/zones/{zone_id}/page_shield/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageShieldPageshieldPolicy,
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
        *,
        zone_id: str,
        action: Literal["allow", "log"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageShieldPageshieldPolicy:
        """
        Create a Page Shield policy.

        Args:
          zone_id: Identifier

          action: The action to take if the expression matches

          description: A description for the policy

          enabled: Whether the policy is enabled

          expression: The expression which must match for the policy to be applied, using the
              Cloudflare Firewall rule expression syntax

          value: The policy which will be applied

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/page_shield/policies",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "description": description,
                    "enabled": enabled,
                    "expression": expression,
                    "value": value,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageShieldPageshieldPolicy,
        )

    async def update(
        self,
        policy_id: str,
        *,
        zone_id: str,
        action: Literal["allow", "log"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageShieldPageshieldPolicy:
        """
        Update a Page Shield policy by ID.

        Args:
          zone_id: Identifier

          policy_id: The ID of the policy.

          action: The action to take if the expression matches

          description: A description for the policy

          enabled: Whether the policy is enabled

          expression: The expression which must match for the policy to be applied, using the
              Cloudflare Firewall rule expression syntax

          value: The policy which will be applied

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._put(
            f"/zones/{zone_id}/page_shield/policies/{policy_id}",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "description": description,
                    "enabled": enabled,
                    "expression": expression,
                    "value": value,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageShieldPageshieldPolicy,
        )

    async def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyListResponse]:
        """
        Lists all Page Shield policies.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/page_shield/policies",
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
        policy_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a Page Shield policy by ID.

        Args:
          zone_id: Identifier

          policy_id: The ID of the policy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/zones/{zone_id}/page_shield/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        policy_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageShieldPageshieldPolicy:
        """
        Fetches a Page Shield policy by ID.

        Args:
          zone_id: Identifier

          policy_id: The ID of the policy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._get(
            f"/zones/{zone_id}/page_shield/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageShieldPageshieldPolicy,
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
