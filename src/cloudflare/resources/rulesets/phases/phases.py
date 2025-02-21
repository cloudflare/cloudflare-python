# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
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
from ...._base_client import make_request_options
from ....types.rulesets import Phase, phase_update_params
from ....types.rulesets.phase import Phase
from ....types.rulesets.phase_get_response import PhaseGetResponse
from ....types.rulesets.phase_update_response import PhaseUpdateResponse

__all__ = ["PhasesResource", "AsyncPhasesResource"]


class PhasesResource(SyncAPIResource):
    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PhasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PhasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PhasesResourceWithStreamingResponse(self)

    def update(
        self,
        ruleset_phase: Phase,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        rules: Iterable[phase_update_params.Rule] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhaseUpdateResponse:
        """
        Updates an account or zone entry point ruleset, creating a new version.

        Args:
          ruleset_phase: The phase of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          description: An informative description of the ruleset.

          name: The human-readable name of the ruleset.

          rules: The list of rules in the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_phase:
            raise ValueError(f"Expected a non-empty value for `ruleset_phase` but received {ruleset_phase!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "rules": rules,
                },
                phase_update_params.PhaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PhaseUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PhaseUpdateResponse], ResultWrapper[PhaseUpdateResponse]),
        )

    def get(
        self,
        ruleset_phase: Phase,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhaseGetResponse:
        """
        Fetches the latest version of the account or zone entry point ruleset for a
        given phase.

        Args:
          ruleset_phase: The phase of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_phase:
            raise ValueError(f"Expected a non-empty value for `ruleset_phase` but received {ruleset_phase!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PhaseGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[PhaseGetResponse], ResultWrapper[PhaseGetResponse]),
        )


class AsyncPhasesResource(AsyncAPIResource):
    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPhasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPhasesResourceWithStreamingResponse(self)

    async def update(
        self,
        ruleset_phase: Phase,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        rules: Iterable[phase_update_params.Rule] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhaseUpdateResponse:
        """
        Updates an account or zone entry point ruleset, creating a new version.

        Args:
          ruleset_phase: The phase of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          description: An informative description of the ruleset.

          name: The human-readable name of the ruleset.

          rules: The list of rules in the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_phase:
            raise ValueError(f"Expected a non-empty value for `ruleset_phase` but received {ruleset_phase!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "rules": rules,
                },
                phase_update_params.PhaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PhaseUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PhaseUpdateResponse], ResultWrapper[PhaseUpdateResponse]),
        )

    async def get(
        self,
        ruleset_phase: Phase,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhaseGetResponse:
        """
        Fetches the latest version of the account or zone entry point ruleset for a
        given phase.

        Args:
          ruleset_phase: The phase of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_phase:
            raise ValueError(f"Expected a non-empty value for `ruleset_phase` but received {ruleset_phase!r}")
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
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PhaseGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[PhaseGetResponse], ResultWrapper[PhaseGetResponse]),
        )


class PhasesResourceWithRawResponse:
    def __init__(self, phases: PhasesResource) -> None:
        self._phases = phases

        self.update = to_raw_response_wrapper(
            phases.update,
        )
        self.get = to_raw_response_wrapper(
            phases.get,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._phases.versions)


class AsyncPhasesResourceWithRawResponse:
    def __init__(self, phases: AsyncPhasesResource) -> None:
        self._phases = phases

        self.update = async_to_raw_response_wrapper(
            phases.update,
        )
        self.get = async_to_raw_response_wrapper(
            phases.get,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._phases.versions)


class PhasesResourceWithStreamingResponse:
    def __init__(self, phases: PhasesResource) -> None:
        self._phases = phases

        self.update = to_streamed_response_wrapper(
            phases.update,
        )
        self.get = to_streamed_response_wrapper(
            phases.get,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._phases.versions)


class AsyncPhasesResourceWithStreamingResponse:
    def __init__(self, phases: AsyncPhasesResource) -> None:
        self._phases = phases

        self.update = async_to_streamed_response_wrapper(
            phases.update,
        )
        self.get = async_to_streamed_response_wrapper(
            phases.get,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._phases.versions)
