# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

from .rules import (
    Rules,
    AsyncRules,
    RulesWithRawResponse,
    AsyncRulesWithRawResponse,
    RulesWithStreamingResponse,
    AsyncRulesWithStreamingResponse,
)
from .phases import (
    Phases,
    AsyncPhases,
    PhasesWithRawResponse,
    AsyncPhasesWithRawResponse,
    PhasesWithStreamingResponse,
    AsyncPhasesWithStreamingResponse,
)
from ...types import (
    RulesetGetResponse,
    RulesetListResponse,
    RulesetCreateResponse,
    RulesetUpdateResponse,
    ruleset_create_params,
    ruleset_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from .versions import (
    Versions,
    AsyncVersions,
    VersionsWithRawResponse,
    AsyncVersionsWithRawResponse,
    VersionsWithStreamingResponse,
    AsyncVersionsWithStreamingResponse,
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
from .versions.versions import Versions, AsyncVersions

__all__ = ["Rulesets", "AsyncRulesets"]


class Rulesets(SyncAPIResource):
    @cached_property
    def phases(self) -> Phases:
        return Phases(self._client)

    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def versions(self) -> Versions:
        return Versions(self._client)

    @cached_property
    def with_raw_response(self) -> RulesetsWithRawResponse:
        return RulesetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesetsWithStreamingResponse:
        return RulesetsWithStreamingResponse(self)

    def create(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        kind: Literal["managed", "custom", "root", "zone"],
        name: str,
        phase: Literal[
            "ddos_l4",
            "ddos_l7",
            "http_config_settings",
            "http_custom_errors",
            "http_log_custom_fields",
            "http_ratelimit",
            "http_request_cache_settings",
            "http_request_dynamic_redirect",
            "http_request_firewall_custom",
            "http_request_firewall_managed",
            "http_request_late_transform",
            "http_request_origin",
            "http_request_redirect",
            "http_request_sanitize",
            "http_request_sbfm",
            "http_request_select_configuration",
            "http_request_transform",
            "http_response_compression",
            "http_response_firewall_managed",
            "http_response_headers_transform",
            "magic_transit",
            "magic_transit_ids_managed",
            "magic_transit_managed",
        ],
        rules: Iterable[ruleset_create_params.Rule],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetCreateResponse:
        """
        Creates a ruleset.

        Args:
          account_or_zone_id: The unique ID of the account.

          kind: The kind of the ruleset.

          name: The human-readable name of the ruleset.

          phase: The phase of the ruleset.

          rules: The list of rules in the ruleset.

          description: An informative description of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets",
            body=maybe_transform(
                {
                    "kind": kind,
                    "name": name,
                    "phase": phase,
                    "rules": rules,
                    "description": description,
                },
                ruleset_create_params.RulesetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetCreateResponse], ResultWrapper[RulesetCreateResponse]),
        )

    def update(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        id: str,
        rules: Iterable[ruleset_update_params.Rule],
        description: str | NotGiven = NOT_GIVEN,
        kind: Literal["managed", "custom", "root", "zone"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        phase: Literal[
            "ddos_l4",
            "ddos_l7",
            "http_config_settings",
            "http_custom_errors",
            "http_log_custom_fields",
            "http_ratelimit",
            "http_request_cache_settings",
            "http_request_dynamic_redirect",
            "http_request_firewall_custom",
            "http_request_firewall_managed",
            "http_request_late_transform",
            "http_request_origin",
            "http_request_redirect",
            "http_request_sanitize",
            "http_request_sbfm",
            "http_request_select_configuration",
            "http_request_transform",
            "http_response_compression",
            "http_response_firewall_managed",
            "http_response_headers_transform",
            "magic_transit",
            "magic_transit_ids_managed",
            "magic_transit_managed",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetUpdateResponse:
        """
        Updates an account or zone ruleset, creating a new version.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          id: The unique ID of the ruleset.

          rules: The list of rules in the ruleset.

          description: An informative description of the ruleset.

          kind: The kind of the ruleset.

          name: The human-readable name of the ruleset.

          phase: The phase of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        return self._put(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}",
            body=maybe_transform(
                {
                    "id": id,
                    "rules": rules,
                    "description": description,
                    "kind": kind,
                    "name": name,
                    "phase": phase,
                },
                ruleset_update_params.RulesetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetUpdateResponse], ResultWrapper[RulesetUpdateResponse]),
        )

    def list(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetListResponse:
        """
        Fetches all rulesets.

        Args:
          account_or_zone_id: The unique ID of the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetListResponse], ResultWrapper[RulesetListResponse]),
        )

    def delete(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes all versions of an existing account or zone ruleset.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetGetResponse:
        """
        Fetches the latest version of an account or zone ruleset.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetGetResponse], ResultWrapper[RulesetGetResponse]),
        )


class AsyncRulesets(AsyncAPIResource):
    @cached_property
    def phases(self) -> AsyncPhases:
        return AsyncPhases(self._client)

    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def versions(self) -> AsyncVersions:
        return AsyncVersions(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRulesetsWithRawResponse:
        return AsyncRulesetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesetsWithStreamingResponse:
        return AsyncRulesetsWithStreamingResponse(self)

    async def create(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        kind: Literal["managed", "custom", "root", "zone"],
        name: str,
        phase: Literal[
            "ddos_l4",
            "ddos_l7",
            "http_config_settings",
            "http_custom_errors",
            "http_log_custom_fields",
            "http_ratelimit",
            "http_request_cache_settings",
            "http_request_dynamic_redirect",
            "http_request_firewall_custom",
            "http_request_firewall_managed",
            "http_request_late_transform",
            "http_request_origin",
            "http_request_redirect",
            "http_request_sanitize",
            "http_request_sbfm",
            "http_request_select_configuration",
            "http_request_transform",
            "http_response_compression",
            "http_response_firewall_managed",
            "http_response_headers_transform",
            "magic_transit",
            "magic_transit_ids_managed",
            "magic_transit_managed",
        ],
        rules: Iterable[ruleset_create_params.Rule],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetCreateResponse:
        """
        Creates a ruleset.

        Args:
          account_or_zone_id: The unique ID of the account.

          kind: The kind of the ruleset.

          name: The human-readable name of the ruleset.

          phase: The phase of the ruleset.

          rules: The list of rules in the ruleset.

          description: An informative description of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets",
            body=maybe_transform(
                {
                    "kind": kind,
                    "name": name,
                    "phase": phase,
                    "rules": rules,
                    "description": description,
                },
                ruleset_create_params.RulesetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetCreateResponse], ResultWrapper[RulesetCreateResponse]),
        )

    async def update(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        id: str,
        rules: Iterable[ruleset_update_params.Rule],
        description: str | NotGiven = NOT_GIVEN,
        kind: Literal["managed", "custom", "root", "zone"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        phase: Literal[
            "ddos_l4",
            "ddos_l7",
            "http_config_settings",
            "http_custom_errors",
            "http_log_custom_fields",
            "http_ratelimit",
            "http_request_cache_settings",
            "http_request_dynamic_redirect",
            "http_request_firewall_custom",
            "http_request_firewall_managed",
            "http_request_late_transform",
            "http_request_origin",
            "http_request_redirect",
            "http_request_sanitize",
            "http_request_sbfm",
            "http_request_select_configuration",
            "http_request_transform",
            "http_response_compression",
            "http_response_firewall_managed",
            "http_response_headers_transform",
            "magic_transit",
            "magic_transit_ids_managed",
            "magic_transit_managed",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetUpdateResponse:
        """
        Updates an account or zone ruleset, creating a new version.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          id: The unique ID of the ruleset.

          rules: The list of rules in the ruleset.

          description: An informative description of the ruleset.

          kind: The kind of the ruleset.

          name: The human-readable name of the ruleset.

          phase: The phase of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        return await self._put(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}",
            body=maybe_transform(
                {
                    "id": id,
                    "rules": rules,
                    "description": description,
                    "kind": kind,
                    "name": name,
                    "phase": phase,
                },
                ruleset_update_params.RulesetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetUpdateResponse], ResultWrapper[RulesetUpdateResponse]),
        )

    async def list(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetListResponse:
        """
        Fetches all rulesets.

        Args:
          account_or_zone_id: The unique ID of the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetListResponse], ResultWrapper[RulesetListResponse]),
        )

    async def delete(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes all versions of an existing account or zone ruleset.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetGetResponse:
        """
        Fetches the latest version of an account or zone ruleset.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetGetResponse], ResultWrapper[RulesetGetResponse]),
        )


class RulesetsWithRawResponse:
    def __init__(self, rulesets: Rulesets) -> None:
        self._rulesets = rulesets

        self.create = to_raw_response_wrapper(
            rulesets.create,
        )
        self.update = to_raw_response_wrapper(
            rulesets.update,
        )
        self.list = to_raw_response_wrapper(
            rulesets.list,
        )
        self.delete = to_raw_response_wrapper(
            rulesets.delete,
        )
        self.get = to_raw_response_wrapper(
            rulesets.get,
        )

    @cached_property
    def phases(self) -> PhasesWithRawResponse:
        return PhasesWithRawResponse(self._rulesets.phases)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._rulesets.rules)

    @cached_property
    def versions(self) -> VersionsWithRawResponse:
        return VersionsWithRawResponse(self._rulesets.versions)


class AsyncRulesetsWithRawResponse:
    def __init__(self, rulesets: AsyncRulesets) -> None:
        self._rulesets = rulesets

        self.create = async_to_raw_response_wrapper(
            rulesets.create,
        )
        self.update = async_to_raw_response_wrapper(
            rulesets.update,
        )
        self.list = async_to_raw_response_wrapper(
            rulesets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rulesets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            rulesets.get,
        )

    @cached_property
    def phases(self) -> AsyncPhasesWithRawResponse:
        return AsyncPhasesWithRawResponse(self._rulesets.phases)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._rulesets.rules)

    @cached_property
    def versions(self) -> AsyncVersionsWithRawResponse:
        return AsyncVersionsWithRawResponse(self._rulesets.versions)


class RulesetsWithStreamingResponse:
    def __init__(self, rulesets: Rulesets) -> None:
        self._rulesets = rulesets

        self.create = to_streamed_response_wrapper(
            rulesets.create,
        )
        self.update = to_streamed_response_wrapper(
            rulesets.update,
        )
        self.list = to_streamed_response_wrapper(
            rulesets.list,
        )
        self.delete = to_streamed_response_wrapper(
            rulesets.delete,
        )
        self.get = to_streamed_response_wrapper(
            rulesets.get,
        )

    @cached_property
    def phases(self) -> PhasesWithStreamingResponse:
        return PhasesWithStreamingResponse(self._rulesets.phases)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._rulesets.rules)

    @cached_property
    def versions(self) -> VersionsWithStreamingResponse:
        return VersionsWithStreamingResponse(self._rulesets.versions)


class AsyncRulesetsWithStreamingResponse:
    def __init__(self, rulesets: AsyncRulesets) -> None:
        self._rulesets = rulesets

        self.create = async_to_streamed_response_wrapper(
            rulesets.create,
        )
        self.update = async_to_streamed_response_wrapper(
            rulesets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rulesets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rulesets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            rulesets.get,
        )

    @cached_property
    def phases(self) -> AsyncPhasesWithStreamingResponse:
        return AsyncPhasesWithStreamingResponse(self._rulesets.phases)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._rulesets.rules)

    @cached_property
    def versions(self) -> AsyncVersionsWithStreamingResponse:
        return AsyncVersionsWithStreamingResponse(self._rulesets.versions)
