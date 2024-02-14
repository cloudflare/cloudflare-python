# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
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
from ...types.firewalls import (
    AccessRuleGetResponse,
    AccessRuleListResponse,
    AccessRuleCreateResponse,
    AccessRuleDeleteResponse,
    AccessRuleUpdateResponse,
    access_rule_list_params,
    access_rule_create_params,
    access_rule_update_params,
)

__all__ = ["AccessRules", "AsyncAccessRules"]


class AccessRules(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessRulesWithRawResponse:
        return AccessRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessRulesWithStreamingResponse:
        return AccessRulesWithStreamingResponse(self)

    def create(
        self,
        account_or_zone_id: object,
        *,
        account_or_zone: str,
        configuration: access_rule_create_params.Configuration,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
        notes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRuleCreateResponse]:
        """Creates a new IP Access rule for an account or zone.

        The rule will apply to all
        zones in the account or zone.

        Note: To create an IP Access rule that applies to a single zone, refer to the
        [IP Access rules for a zone](#ip-access-rules-for-a-zone) endpoints.

        Args:
          configuration: The rule configuration.

          mode: The action to apply to a matched request.

          notes: An informative summary of the rule, typically used as a reminder or explanation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        return cast(
            Optional[AccessRuleCreateResponse],
            self._post(
                f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules",
                body=maybe_transform(
                    {
                        "configuration": configuration,
                        "mode": mode,
                        "notes": notes,
                    },
                    access_rule_create_params.AccessRuleCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccessRuleCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        identifier: object,
        *,
        account_identifier: object,
        configuration: access_rule_update_params.Configuration,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
        notes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRuleUpdateResponse]:
        """
        Updates an IP Access rule defined at the account level.

        Note: This operation will affect all zones in the account.

        Args:
          configuration: The rule configuration.

          mode: The action to apply to a matched request.

          notes: An informative summary of the rule, typically used as a reminder or explanation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            Optional[AccessRuleUpdateResponse],
            self._patch(
                f"/{account_identifier}/{identifier}/firewall/access_rules/rules/:identifier",
                body=maybe_transform(
                    {
                        "configuration": configuration,
                        "mode": mode,
                        "notes": notes,
                    },
                    access_rule_update_params.AccessRuleUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccessRuleUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        account_or_zone_id: object,
        *,
        account_or_zone: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        egs_pagination: access_rule_list_params.EgsPagination | NotGiven = NOT_GIVEN,
        filters: access_rule_list_params.Filters | NotGiven = NOT_GIVEN,
        order: Literal["configuration.target", "configuration.value", "mode"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRuleListResponse]:
        """Fetches IP Access rules of an account or zone.

        These rules apply to all the
        zones in the account or zone. You can filter the results using several optional
        parameters.

        Args:
          direction: The direction used to sort returned rules.

          order: The field used to sort returned rules.

          page: Requested page within paginated list of results.

          per_page: Maximum number of results requested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "egs_pagination": egs_pagination,
                        "filters": filters,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    access_rule_list_params.AccessRuleListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccessRuleListResponse]], ResultWrapper[AccessRuleListResponse]),
        )

    def delete(
        self,
        identifier: object,
        *,
        account_or_zone: str,
        account_or_zone_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRuleDeleteResponse]:
        """
        Deletes an existing IP Access rule defined.

        Note: This operation will affect all zones in the account or zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccessRuleDeleteResponse]], ResultWrapper[AccessRuleDeleteResponse]),
        )

    def get(
        self,
        identifier: object,
        *,
        account_or_zone: str,
        account_or_zone_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRuleGetResponse]:
        """
        Fetches the details of an IP Access rule defined.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        return cast(
            Optional[AccessRuleGetResponse],
            self._get(
                f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccessRuleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncAccessRules(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessRulesWithRawResponse:
        return AsyncAccessRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessRulesWithStreamingResponse:
        return AsyncAccessRulesWithStreamingResponse(self)

    async def create(
        self,
        account_or_zone_id: object,
        *,
        account_or_zone: str,
        configuration: access_rule_create_params.Configuration,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
        notes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRuleCreateResponse]:
        """Creates a new IP Access rule for an account or zone.

        The rule will apply to all
        zones in the account or zone.

        Note: To create an IP Access rule that applies to a single zone, refer to the
        [IP Access rules for a zone](#ip-access-rules-for-a-zone) endpoints.

        Args:
          configuration: The rule configuration.

          mode: The action to apply to a matched request.

          notes: An informative summary of the rule, typically used as a reminder or explanation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        return cast(
            Optional[AccessRuleCreateResponse],
            await self._post(
                f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules",
                body=maybe_transform(
                    {
                        "configuration": configuration,
                        "mode": mode,
                        "notes": notes,
                    },
                    access_rule_create_params.AccessRuleCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccessRuleCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        identifier: object,
        *,
        account_identifier: object,
        configuration: access_rule_update_params.Configuration,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
        notes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRuleUpdateResponse]:
        """
        Updates an IP Access rule defined at the account level.

        Note: This operation will affect all zones in the account.

        Args:
          configuration: The rule configuration.

          mode: The action to apply to a matched request.

          notes: An informative summary of the rule, typically used as a reminder or explanation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            Optional[AccessRuleUpdateResponse],
            await self._patch(
                f"/{account_identifier}/{identifier}/firewall/access_rules/rules/:identifier",
                body=maybe_transform(
                    {
                        "configuration": configuration,
                        "mode": mode,
                        "notes": notes,
                    },
                    access_rule_update_params.AccessRuleUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccessRuleUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        account_or_zone_id: object,
        *,
        account_or_zone: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        egs_pagination: access_rule_list_params.EgsPagination | NotGiven = NOT_GIVEN,
        filters: access_rule_list_params.Filters | NotGiven = NOT_GIVEN,
        order: Literal["configuration.target", "configuration.value", "mode"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRuleListResponse]:
        """Fetches IP Access rules of an account or zone.

        These rules apply to all the
        zones in the account or zone. You can filter the results using several optional
        parameters.

        Args:
          direction: The direction used to sort returned rules.

          order: The field used to sort returned rules.

          page: Requested page within paginated list of results.

          per_page: Maximum number of results requested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "egs_pagination": egs_pagination,
                        "filters": filters,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    access_rule_list_params.AccessRuleListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccessRuleListResponse]], ResultWrapper[AccessRuleListResponse]),
        )

    async def delete(
        self,
        identifier: object,
        *,
        account_or_zone: str,
        account_or_zone_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRuleDeleteResponse]:
        """
        Deletes an existing IP Access rule defined.

        Note: This operation will affect all zones in the account or zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccessRuleDeleteResponse]], ResultWrapper[AccessRuleDeleteResponse]),
        )

    async def get(
        self,
        identifier: object,
        *,
        account_or_zone: str,
        account_or_zone_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRuleGetResponse]:
        """
        Fetches the details of an IP Access rule defined.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        return cast(
            Optional[AccessRuleGetResponse],
            await self._get(
                f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccessRuleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AccessRulesWithRawResponse:
    def __init__(self, access_rules: AccessRules) -> None:
        self._access_rules = access_rules

        self.create = to_raw_response_wrapper(
            access_rules.create,
        )
        self.update = to_raw_response_wrapper(
            access_rules.update,
        )
        self.list = to_raw_response_wrapper(
            access_rules.list,
        )
        self.delete = to_raw_response_wrapper(
            access_rules.delete,
        )
        self.get = to_raw_response_wrapper(
            access_rules.get,
        )


class AsyncAccessRulesWithRawResponse:
    def __init__(self, access_rules: AsyncAccessRules) -> None:
        self._access_rules = access_rules

        self.create = async_to_raw_response_wrapper(
            access_rules.create,
        )
        self.update = async_to_raw_response_wrapper(
            access_rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            access_rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            access_rules.delete,
        )
        self.get = async_to_raw_response_wrapper(
            access_rules.get,
        )


class AccessRulesWithStreamingResponse:
    def __init__(self, access_rules: AccessRules) -> None:
        self._access_rules = access_rules

        self.create = to_streamed_response_wrapper(
            access_rules.create,
        )
        self.update = to_streamed_response_wrapper(
            access_rules.update,
        )
        self.list = to_streamed_response_wrapper(
            access_rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            access_rules.delete,
        )
        self.get = to_streamed_response_wrapper(
            access_rules.get,
        )


class AsyncAccessRulesWithStreamingResponse:
    def __init__(self, access_rules: AsyncAccessRules) -> None:
        self._access_rules = access_rules

        self.create = async_to_streamed_response_wrapper(
            access_rules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            access_rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            access_rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            access_rules.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            access_rules.get,
        )
