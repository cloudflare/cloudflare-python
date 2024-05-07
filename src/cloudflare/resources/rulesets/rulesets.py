# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from .phases import (
    PhasesResource,
    AsyncPhasesResource,
    PhasesResourceWithRawResponse,
    AsyncPhasesResourceWithRawResponse,
    PhasesResourceWithStreamingResponse,
    AsyncPhasesResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
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
from ...pagination import SyncSinglePage, AsyncSinglePage
from .phases.phases import PhasesResource, AsyncPhasesResource
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.rulesets import Kind, Phase, ruleset_create_params, ruleset_update_params
from .versions.versions import VersionsResource, AsyncVersionsResource
from ...types.rulesets.kind import Kind
from ...types.rulesets.phase import Phase
from ...types.rulesets.ruleset import Ruleset
from ...types.rulesets.ruleset_get_response import RulesetGetResponse
from ...types.rulesets.ruleset_create_response import RulesetCreateResponse
from ...types.rulesets.ruleset_update_response import RulesetUpdateResponse

__all__ = ["RulesetsResource", "AsyncRulesetsResource"]


class RulesetsResource(SyncAPIResource):
    @cached_property
    def phases(self) -> PhasesResource:
        return PhasesResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RulesetsResourceWithRawResponse:
        return RulesetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesetsResourceWithStreamingResponse:
        return RulesetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        kind: Kind,
        name: str,
        phase: Phase,
        rules: Iterable[ruleset_create_params.Rule],
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
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
          kind: The kind of the ruleset.

          name: The human-readable name of the ruleset.

          phase: The phase of the ruleset.

          rules: The list of rules in the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          description: An informative description of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
                post_parser=ResultWrapper[RulesetCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RulesetCreateResponse], ResultWrapper[RulesetCreateResponse]),
        )

    def update(
        self,
        ruleset_id: str,
        *,
        rules: Iterable[ruleset_update_params.Rule],
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        kind: Kind | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        phase: Phase | NotGiven = NOT_GIVEN,
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
          ruleset_id: The unique ID of the ruleset.

          rules: The list of rules in the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          description: An informative description of the ruleset.

          kind: The kind of the ruleset.

          name: The human-readable name of the ruleset.

          phase: The phase of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}",
            body=maybe_transform(
                {
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
                post_parser=ResultWrapper[RulesetUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RulesetUpdateResponse], ResultWrapper[RulesetUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Ruleset]:
        """
        Fetches all rulesets.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
            f"/{account_or_zone}/{account_or_zone_id}/rulesets",
            page=SyncSinglePage[Ruleset],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Ruleset,
        )

    def delete(
        self,
        ruleset_id: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
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
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
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
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RulesetGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[RulesetGetResponse], ResultWrapper[RulesetGetResponse]),
        )


class AsyncRulesetsResource(AsyncAPIResource):
    @cached_property
    def phases(self) -> AsyncPhasesResource:
        return AsyncPhasesResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRulesetsResourceWithRawResponse:
        return AsyncRulesetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesetsResourceWithStreamingResponse:
        return AsyncRulesetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        kind: Kind,
        name: str,
        phase: Phase,
        rules: Iterable[ruleset_create_params.Rule],
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
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
          kind: The kind of the ruleset.

          name: The human-readable name of the ruleset.

          phase: The phase of the ruleset.

          rules: The list of rules in the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          description: An informative description of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
            f"/{account_or_zone}/{account_or_zone_id}/rulesets",
            body=await async_maybe_transform(
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
                post_parser=ResultWrapper[RulesetCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RulesetCreateResponse], ResultWrapper[RulesetCreateResponse]),
        )

    async def update(
        self,
        ruleset_id: str,
        *,
        rules: Iterable[ruleset_update_params.Rule],
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        kind: Kind | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        phase: Phase | NotGiven = NOT_GIVEN,
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
          ruleset_id: The unique ID of the ruleset.

          rules: The list of rules in the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          description: An informative description of the ruleset.

          kind: The kind of the ruleset.

          name: The human-readable name of the ruleset.

          phase: The phase of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}",
            body=await async_maybe_transform(
                {
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
                post_parser=ResultWrapper[RulesetUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RulesetUpdateResponse], ResultWrapper[RulesetUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Ruleset, AsyncSinglePage[Ruleset]]:
        """
        Fetches all rulesets.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
            f"/{account_or_zone}/{account_or_zone_id}/rulesets",
            page=AsyncSinglePage[Ruleset],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Ruleset,
        )

    async def delete(
        self,
        ruleset_id: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
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
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
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
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RulesetGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[RulesetGetResponse], ResultWrapper[RulesetGetResponse]),
        )


class RulesetsResourceWithRawResponse:
    def __init__(self, rulesets: RulesetsResource) -> None:
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
    def phases(self) -> PhasesResourceWithRawResponse:
        return PhasesResourceWithRawResponse(self._rulesets.phases)

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._rulesets.rules)

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._rulesets.versions)


class AsyncRulesetsResourceWithRawResponse:
    def __init__(self, rulesets: AsyncRulesetsResource) -> None:
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
    def phases(self) -> AsyncPhasesResourceWithRawResponse:
        return AsyncPhasesResourceWithRawResponse(self._rulesets.phases)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._rulesets.rules)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._rulesets.versions)


class RulesetsResourceWithStreamingResponse:
    def __init__(self, rulesets: RulesetsResource) -> None:
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
    def phases(self) -> PhasesResourceWithStreamingResponse:
        return PhasesResourceWithStreamingResponse(self._rulesets.phases)

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._rulesets.rules)

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._rulesets.versions)


class AsyncRulesetsResourceWithStreamingResponse:
    def __init__(self, rulesets: AsyncRulesetsResource) -> None:
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
    def phases(self) -> AsyncPhasesResourceWithStreamingResponse:
        return AsyncPhasesResourceWithStreamingResponse(self._rulesets.phases)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._rulesets.rules)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._rulesets.versions)
