# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.rulesets import PhaseGetResponse

from typing import Type

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Phases", "AsyncPhases"]


class Phases(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhasesWithRawResponse:
        return PhasesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhasesWithStreamingResponse:
        return PhasesWithStreamingResponse(self)

    def get(
        self,
        ruleset_phase: Literal[
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
        *,
        account_or_zone: str,
        account_or_zone_id: str,
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
          account_or_zone_id: The unique ID of the account.

          ruleset_phase: The phase of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_phase:
            raise ValueError(f"Expected a non-empty value for `ruleset_phase` but received {ruleset_phase!r}")
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PhaseGetResponse], ResultWrapper[PhaseGetResponse]),
        )


class AsyncPhases(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhasesWithRawResponse:
        return AsyncPhasesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhasesWithStreamingResponse:
        return AsyncPhasesWithStreamingResponse(self)

    async def get(
        self,
        ruleset_phase: Literal[
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
        *,
        account_or_zone: str,
        account_or_zone_id: str,
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
          account_or_zone_id: The unique ID of the account.

          ruleset_phase: The phase of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_phase:
            raise ValueError(f"Expected a non-empty value for `ruleset_phase` but received {ruleset_phase!r}")
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PhaseGetResponse], ResultWrapper[PhaseGetResponse]),
        )


class PhasesWithRawResponse:
    def __init__(self, phases: Phases) -> None:
        self._phases = phases

        self.get = to_raw_response_wrapper(
            phases.get,
        )


class AsyncPhasesWithRawResponse:
    def __init__(self, phases: AsyncPhases) -> None:
        self._phases = phases

        self.get = async_to_raw_response_wrapper(
            phases.get,
        )


class PhasesWithStreamingResponse:
    def __init__(self, phases: Phases) -> None:
        self._phases = phases

        self.get = to_streamed_response_wrapper(
            phases.get,
        )


class AsyncPhasesWithStreamingResponse:
    def __init__(self, phases: AsyncPhases) -> None:
        self._phases = phases

        self.get = async_to_streamed_response_wrapper(
            phases.get,
        )
