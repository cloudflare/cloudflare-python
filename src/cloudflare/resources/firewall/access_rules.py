# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.firewall.access_rule_create_response import AccessRuleCreateResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options, AsyncPaginator

from typing_extensions import Literal

from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

from ...types.firewall.access_rule_delete_response import AccessRuleDeleteResponse

from typing import Optional, Type

from ...types.firewall.access_rule_edit_response import AccessRuleEditResponse

from ...types.firewall.access_rule_get_response import AccessRuleGetResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from ...types.firewall import access_rule_create_params, access_rule_list_params, access_rule_edit_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.firewall import access_rule_create_params
from ...types.firewall import access_rule_list_params
from ...types.firewall import access_rule_edit_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["AccessRulesResource", "AsyncAccessRulesResource"]

class AccessRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessRulesResourceWithRawResponse:
        return AccessRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessRulesResourceWithStreamingResponse:
        return AccessRulesResourceWithStreamingResponse(self)

    def create(self,
    *,
    configuration: access_rule_create_params.Configuration,
    mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    notes: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AccessRuleCreateResponse:
        """Creates a new IP Access rule for an account or zone.

        The rule will apply to all
        zones in the account or zone.

        Note: To create an IP Access rule that applies to a single zone, refer to the
        [IP Access rules for a zone](#ip-access-rules-for-a-zone) endpoints.

        Args:
          configuration: The rule configuration.

          mode: The action to apply to a matched request.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          notes: An informative summary of the rule, typically used as a reminder or explanation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return cast(AccessRuleCreateResponse, self._post(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules",
            body=maybe_transform({
                "configuration": configuration,
                "mode": mode,
                "notes": notes,
            }, access_rule_create_params.AccessRuleCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AccessRuleCreateResponse]._unwrapper),
            cast_to=cast(Any, ResultWrapper[AccessRuleCreateResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

    def list(self,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    configuration: access_rule_list_params.Configuration | NotGiven = NOT_GIVEN,
    direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
    match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
    mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"] | NotGiven = NOT_GIVEN,
    notes: str | NotGiven = NOT_GIVEN,
    order: Literal["configuration.target", "configuration.value", "mode"] | NotGiven = NOT_GIVEN,
    page: float | NotGiven = NOT_GIVEN,
    per_page: float | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncV4PagePaginationArray[object]:
        """Fetches IP Access rules of an account or zone.

        These rules apply to all the
        zones in the account or zone. You can filter the results using several optional
        parameters.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          direction: The direction used to sort returned rules.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          mode: The action to apply to a matched request.

          notes: The string to search for in the notes of existing IP Access rules. Notes: For
              example, the string 'attack' would match IP Access rules with notes 'Attack
              26/02' and 'Attack 27/02'. The search is case insensitive.

          order: The field used to sort returned rules.

          page: Requested page within paginated list of results.

          per_page: Maximum number of results requested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules",
            page = SyncV4PagePaginationArray[object],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "configuration": configuration,
                "direction": direction,
                "match": match,
                "mode": mode,
                "notes": notes,
                "order": order,
                "page": page,
                "per_page": per_page,
            }, access_rule_list_params.AccessRuleListParams)),
            model=object,
        )

    def delete(self,
    identifier: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AccessRuleDeleteResponse]:
        """
        Deletes an existing IP Access rule defined.

        Note: This operation will affect all zones in the account or zone.

        Args:
          identifier: The unique identifier of the resource.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
          raise ValueError(
            f'Expected a non-empty value for `identifier` but received {identifier!r}'
          )
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[AccessRuleDeleteResponse]]._unwrapper),
            cast_to=cast(Type[Optional[AccessRuleDeleteResponse]], ResultWrapper[AccessRuleDeleteResponse]),
        )

    def edit(self,
    identifier: str,
    *,
    configuration: access_rule_edit_params.Configuration,
    mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    notes: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AccessRuleEditResponse:
        """
        Updates an IP Access rule defined.

        Note: This operation will affect all zones in the account or zone.

        Args:
          identifier: The unique identifier of the resource.

          configuration: The rule configuration.

          mode: The action to apply to a matched request.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          notes: An informative summary of the rule, typically used as a reminder or explanation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
          raise ValueError(
            f'Expected a non-empty value for `identifier` but received {identifier!r}'
          )
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return cast(AccessRuleEditResponse, self._patch(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}",
            body=maybe_transform({
                "configuration": configuration,
                "mode": mode,
                "notes": notes,
            }, access_rule_edit_params.AccessRuleEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AccessRuleEditResponse]._unwrapper),
            cast_to=cast(Any, ResultWrapper[AccessRuleEditResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

    def get(self,
    identifier: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AccessRuleGetResponse:
        """
        Fetches the details of an IP Access rule defined.

        Args:
          identifier: The unique identifier of the resource.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
          raise ValueError(
            f'Expected a non-empty value for `identifier` but received {identifier!r}'
          )
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return cast(AccessRuleGetResponse, self._get(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AccessRuleGetResponse]._unwrapper),
            cast_to=cast(Any, ResultWrapper[AccessRuleGetResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

class AsyncAccessRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessRulesResourceWithRawResponse:
        return AsyncAccessRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessRulesResourceWithStreamingResponse:
        return AsyncAccessRulesResourceWithStreamingResponse(self)

    async def create(self,
    *,
    configuration: access_rule_create_params.Configuration,
    mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    notes: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AccessRuleCreateResponse:
        """Creates a new IP Access rule for an account or zone.

        The rule will apply to all
        zones in the account or zone.

        Note: To create an IP Access rule that applies to a single zone, refer to the
        [IP Access rules for a zone](#ip-access-rules-for-a-zone) endpoints.

        Args:
          configuration: The rule configuration.

          mode: The action to apply to a matched request.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          notes: An informative summary of the rule, typically used as a reminder or explanation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return cast(AccessRuleCreateResponse, await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules",
            body=await async_maybe_transform({
                "configuration": configuration,
                "mode": mode,
                "notes": notes,
            }, access_rule_create_params.AccessRuleCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AccessRuleCreateResponse]._unwrapper),
            cast_to=cast(Any, ResultWrapper[AccessRuleCreateResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

    def list(self,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    configuration: access_rule_list_params.Configuration | NotGiven = NOT_GIVEN,
    direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
    match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
    mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"] | NotGiven = NOT_GIVEN,
    notes: str | NotGiven = NOT_GIVEN,
    order: Literal["configuration.target", "configuration.value", "mode"] | NotGiven = NOT_GIVEN,
    page: float | NotGiven = NOT_GIVEN,
    per_page: float | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[object, AsyncV4PagePaginationArray[object]]:
        """Fetches IP Access rules of an account or zone.

        These rules apply to all the
        zones in the account or zone. You can filter the results using several optional
        parameters.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          direction: The direction used to sort returned rules.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          mode: The action to apply to a matched request.

          notes: The string to search for in the notes of existing IP Access rules. Notes: For
              example, the string 'attack' would match IP Access rules with notes 'Attack
              26/02' and 'Attack 27/02'. The search is case insensitive.

          order: The field used to sort returned rules.

          page: Requested page within paginated list of results.

          per_page: Maximum number of results requested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules",
            page = AsyncV4PagePaginationArray[object],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "configuration": configuration,
                "direction": direction,
                "match": match,
                "mode": mode,
                "notes": notes,
                "order": order,
                "page": page,
                "per_page": per_page,
            }, access_rule_list_params.AccessRuleListParams)),
            model=object,
        )

    async def delete(self,
    identifier: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[AccessRuleDeleteResponse]:
        """
        Deletes an existing IP Access rule defined.

        Note: This operation will affect all zones in the account or zone.

        Args:
          identifier: The unique identifier of the resource.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
          raise ValueError(
            f'Expected a non-empty value for `identifier` but received {identifier!r}'
          )
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[AccessRuleDeleteResponse]]._unwrapper),
            cast_to=cast(Type[Optional[AccessRuleDeleteResponse]], ResultWrapper[AccessRuleDeleteResponse]),
        )

    async def edit(self,
    identifier: str,
    *,
    configuration: access_rule_edit_params.Configuration,
    mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    notes: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AccessRuleEditResponse:
        """
        Updates an IP Access rule defined.

        Note: This operation will affect all zones in the account or zone.

        Args:
          identifier: The unique identifier of the resource.

          configuration: The rule configuration.

          mode: The action to apply to a matched request.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          notes: An informative summary of the rule, typically used as a reminder or explanation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
          raise ValueError(
            f'Expected a non-empty value for `identifier` but received {identifier!r}'
          )
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return cast(AccessRuleEditResponse, await self._patch(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}",
            body=await async_maybe_transform({
                "configuration": configuration,
                "mode": mode,
                "notes": notes,
            }, access_rule_edit_params.AccessRuleEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AccessRuleEditResponse]._unwrapper),
            cast_to=cast(Any, ResultWrapper[AccessRuleEditResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

    async def get(self,
    identifier: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AccessRuleGetResponse:
        """
        Fetches the details of an IP Access rule defined.

        Args:
          identifier: The unique identifier of the resource.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
          raise ValueError(
            f'Expected a non-empty value for `identifier` but received {identifier!r}'
          )
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return cast(AccessRuleGetResponse, await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules/{identifier}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AccessRuleGetResponse]._unwrapper),
            cast_to=cast(Any, ResultWrapper[AccessRuleGetResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

class AccessRulesResourceWithRawResponse:
    def __init__(self, access_rules: AccessRulesResource) -> None:
        self._access_rules = access_rules

        self.create = to_raw_response_wrapper(
            access_rules.create,
        )
        self.list = to_raw_response_wrapper(
            access_rules.list,
        )
        self.delete = to_raw_response_wrapper(
            access_rules.delete,
        )
        self.edit = to_raw_response_wrapper(
            access_rules.edit,
        )
        self.get = to_raw_response_wrapper(
            access_rules.get,
        )

class AsyncAccessRulesResourceWithRawResponse:
    def __init__(self, access_rules: AsyncAccessRulesResource) -> None:
        self._access_rules = access_rules

        self.create = async_to_raw_response_wrapper(
            access_rules.create,
        )
        self.list = async_to_raw_response_wrapper(
            access_rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            access_rules.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            access_rules.edit,
        )
        self.get = async_to_raw_response_wrapper(
            access_rules.get,
        )

class AccessRulesResourceWithStreamingResponse:
    def __init__(self, access_rules: AccessRulesResource) -> None:
        self._access_rules = access_rules

        self.create = to_streamed_response_wrapper(
            access_rules.create,
        )
        self.list = to_streamed_response_wrapper(
            access_rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            access_rules.delete,
        )
        self.edit = to_streamed_response_wrapper(
            access_rules.edit,
        )
        self.get = to_streamed_response_wrapper(
            access_rules.get,
        )

class AsyncAccessRulesResourceWithStreamingResponse:
    def __init__(self, access_rules: AsyncAccessRulesResource) -> None:
        self._access_rules = access_rules

        self.create = async_to_streamed_response_wrapper(
            access_rules.create,
        )
        self.list = async_to_streamed_response_wrapper(
            access_rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            access_rules.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            access_rules.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            access_rules.get,
        )