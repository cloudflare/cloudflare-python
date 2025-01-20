# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

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
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.access.applications import policy_create_params, policy_update_params
from .....types.zero_trust.access.approval_group_param import ApprovalGroupParam
from .....types.zero_trust.access.applications.policy_get_response import PolicyGetResponse
from .....types.zero_trust.access.applications.policy_list_response import PolicyListResponse
from .....types.zero_trust.access.applications.policy_create_response import PolicyCreateResponse
from .....types.zero_trust.access.applications.policy_delete_response import PolicyDeleteResponse
from .....types.zero_trust.access.applications.policy_update_response import PolicyUpdateResponse

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
        app_id: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        approval_groups: Iterable[ApprovalGroupParam] | NotGiven = NOT_GIVEN,
        approval_required: bool | NotGiven = NOT_GIVEN,
        isolation_required: bool | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        purpose_justification_prompt: str | NotGiven = NOT_GIVEN,
        purpose_justification_required: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyCreateResponse]:
        """
        Creates a policy applying exclusive to a single application that defines the
        users or groups who can reach it. We recommend creating a reusable policy
        instead and subsequently referencing its ID in the application's 'policies'
        array.

        Args:
          app_id: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          approval_groups: Administrators who can approve a temporary authentication request.

          approval_required: Requires the user to request access from an administrator at the start of each
              session.

          isolation_required: Require this application to be served in an isolated browser for users matching
              this policy. 'Client Web Isolation' must be on for the account in order to use
              this feature.

          precedence: The order of execution for this policy. Must be unique for each policy within an
              app.

          purpose_justification_prompt: A custom message that will appear on the purpose justification screen.

          purpose_justification_required: Require users to enter a justification when they log in to the application.

          session_duration: The amount of time that tokens issued for the application will be valid. Must be
              in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s,
              m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/policies",
            body=maybe_transform(
                {
                    "approval_groups": approval_groups,
                    "approval_required": approval_required,
                    "isolation_required": isolation_required,
                    "precedence": precedence,
                    "purpose_justification_prompt": purpose_justification_prompt,
                    "purpose_justification_required": purpose_justification_required,
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
        app_id: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        approval_groups: Iterable[ApprovalGroupParam] | NotGiven = NOT_GIVEN,
        approval_required: bool | NotGiven = NOT_GIVEN,
        isolation_required: bool | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        purpose_justification_prompt: str | NotGiven = NOT_GIVEN,
        purpose_justification_required: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyUpdateResponse]:
        """Updates an Access policy specific to an application.

        To update a reusable
        policy, use the /account or zones/{account or zone_id}/policies/{uid} endpoint.

        Args:
          app_id: UUID

          policy_id: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          approval_groups: Administrators who can approve a temporary authentication request.

          approval_required: Requires the user to request access from an administrator at the start of each
              session.

          isolation_required: Require this application to be served in an isolated browser for users matching
              this policy. 'Client Web Isolation' must be on for the account in order to use
              this feature.

          precedence: The order of execution for this policy. Must be unique for each policy within an
              app.

          purpose_justification_prompt: A custom message that will appear on the purpose justification screen.

          purpose_justification_required: Require users to enter a justification when they log in to the application.

          session_duration: The amount of time that tokens issued for the application will be valid. Must be
              in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s,
              m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._put(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}",
            body=maybe_transform(
                {
                    "approval_groups": approval_groups,
                    "approval_required": approval_required,
                    "isolation_required": isolation_required,
                    "precedence": precedence,
                    "purpose_justification_prompt": purpose_justification_prompt,
                    "purpose_justification_required": purpose_justification_required,
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
        app_id: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[PolicyListResponse]:
        """Lists Access policies configured for an application.

        Returns both exclusively
        scoped and reusable policies used by the application.

        Args:
          app_id: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/policies",
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
        app_id: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyDeleteResponse]:
        """Deletes an Access policy specific to an application.

        To delete a reusable
        policy, use the /account or zones/{account or zone_id}/policies/{uid} endpoint.

        Args:
          app_id: UUID

          policy_id: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}",
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
        app_id: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyGetResponse]:
        """Fetches a single Access policy configured for an application.

        Returns both
        exclusively owned and reusable policies used by the application.

        Args:
          app_id: UUID

          policy_id: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}",
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
        app_id: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        approval_groups: Iterable[ApprovalGroupParam] | NotGiven = NOT_GIVEN,
        approval_required: bool | NotGiven = NOT_GIVEN,
        isolation_required: bool | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        purpose_justification_prompt: str | NotGiven = NOT_GIVEN,
        purpose_justification_required: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyCreateResponse]:
        """
        Creates a policy applying exclusive to a single application that defines the
        users or groups who can reach it. We recommend creating a reusable policy
        instead and subsequently referencing its ID in the application's 'policies'
        array.

        Args:
          app_id: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          approval_groups: Administrators who can approve a temporary authentication request.

          approval_required: Requires the user to request access from an administrator at the start of each
              session.

          isolation_required: Require this application to be served in an isolated browser for users matching
              this policy. 'Client Web Isolation' must be on for the account in order to use
              this feature.

          precedence: The order of execution for this policy. Must be unique for each policy within an
              app.

          purpose_justification_prompt: A custom message that will appear on the purpose justification screen.

          purpose_justification_required: Require users to enter a justification when they log in to the application.

          session_duration: The amount of time that tokens issued for the application will be valid. Must be
              in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s,
              m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/policies",
            body=await async_maybe_transform(
                {
                    "approval_groups": approval_groups,
                    "approval_required": approval_required,
                    "isolation_required": isolation_required,
                    "precedence": precedence,
                    "purpose_justification_prompt": purpose_justification_prompt,
                    "purpose_justification_required": purpose_justification_required,
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
        app_id: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        approval_groups: Iterable[ApprovalGroupParam] | NotGiven = NOT_GIVEN,
        approval_required: bool | NotGiven = NOT_GIVEN,
        isolation_required: bool | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        purpose_justification_prompt: str | NotGiven = NOT_GIVEN,
        purpose_justification_required: bool | NotGiven = NOT_GIVEN,
        session_duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyUpdateResponse]:
        """Updates an Access policy specific to an application.

        To update a reusable
        policy, use the /account or zones/{account or zone_id}/policies/{uid} endpoint.

        Args:
          app_id: UUID

          policy_id: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          approval_groups: Administrators who can approve a temporary authentication request.

          approval_required: Requires the user to request access from an administrator at the start of each
              session.

          isolation_required: Require this application to be served in an isolated browser for users matching
              this policy. 'Client Web Isolation' must be on for the account in order to use
              this feature.

          precedence: The order of execution for this policy. Must be unique for each policy within an
              app.

          purpose_justification_prompt: A custom message that will appear on the purpose justification screen.

          purpose_justification_required: Require users to enter a justification when they log in to the application.

          session_duration: The amount of time that tokens issued for the application will be valid. Must be
              in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s,
              m, h.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._put(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}",
            body=await async_maybe_transform(
                {
                    "approval_groups": approval_groups,
                    "approval_required": approval_required,
                    "isolation_required": isolation_required,
                    "precedence": precedence,
                    "purpose_justification_prompt": purpose_justification_prompt,
                    "purpose_justification_required": purpose_justification_required,
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
        app_id: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PolicyListResponse, AsyncSinglePage[PolicyListResponse]]:
        """Lists Access policies configured for an application.

        Returns both exclusively
        scoped and reusable policies used by the application.

        Args:
          app_id: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/policies",
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
        app_id: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyDeleteResponse]:
        """Deletes an Access policy specific to an application.

        To delete a reusable
        policy, use the /account or zones/{account or zone_id}/policies/{uid} endpoint.

        Args:
          app_id: UUID

          policy_id: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}",
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
        app_id: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyGetResponse]:
        """Fetches a single Access policy configured for an application.

        Returns both
        exclusively owned and reusable policies used by the application.

        Args:
          app_id: UUID

          policy_id: UUID

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}",
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
