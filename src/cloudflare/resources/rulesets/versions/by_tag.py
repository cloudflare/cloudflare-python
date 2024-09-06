# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.rulesets.versions.by_tag_get_response import ByTagGetResponse

from ...._wrappers import ResultWrapper

from ...._base_client import make_request_options

from typing import Type

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from typing import cast
from typing import cast

__all__ = ["ByTagResource", "AsyncByTagResource"]


class ByTagResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ByTagResourceWithRawResponse:
        return ByTagResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ByTagResourceWithStreamingResponse:
        return ByTagResourceWithStreamingResponse(self)

    def get(
        self,
        rule_tag: str,
        *,
        account_id: str,
        ruleset_id: str,
        ruleset_version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ByTagGetResponse:
        """
        Fetches the rules of a managed account ruleset version for a given tag.

        Args:
          account_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          ruleset_version: The version of the ruleset.

          rule_tag: A category of the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not ruleset_version:
            raise ValueError(f"Expected a non-empty value for `ruleset_version` but received {ruleset_version!r}")
        if not rule_tag:
            raise ValueError(f"Expected a non-empty value for `rule_tag` but received {rule_tag!r}")
        return self._get(
            f"/accounts/{account_id}/rulesets/{ruleset_id}/versions/{ruleset_version}/by_tag/{rule_tag}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ByTagGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ByTagGetResponse], ResultWrapper[ByTagGetResponse]),
        )


class AsyncByTagResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncByTagResourceWithRawResponse:
        return AsyncByTagResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncByTagResourceWithStreamingResponse:
        return AsyncByTagResourceWithStreamingResponse(self)

    async def get(
        self,
        rule_tag: str,
        *,
        account_id: str,
        ruleset_id: str,
        ruleset_version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ByTagGetResponse:
        """
        Fetches the rules of a managed account ruleset version for a given tag.

        Args:
          account_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          ruleset_version: The version of the ruleset.

          rule_tag: A category of the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not ruleset_version:
            raise ValueError(f"Expected a non-empty value for `ruleset_version` but received {ruleset_version!r}")
        if not rule_tag:
            raise ValueError(f"Expected a non-empty value for `rule_tag` but received {rule_tag!r}")
        return await self._get(
            f"/accounts/{account_id}/rulesets/{ruleset_id}/versions/{ruleset_version}/by_tag/{rule_tag}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ByTagGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ByTagGetResponse], ResultWrapper[ByTagGetResponse]),
        )


class ByTagResourceWithRawResponse:
    def __init__(self, by_tag: ByTagResource) -> None:
        self._by_tag = by_tag

        self.get = to_raw_response_wrapper(
            by_tag.get,
        )


class AsyncByTagResourceWithRawResponse:
    def __init__(self, by_tag: AsyncByTagResource) -> None:
        self._by_tag = by_tag

        self.get = async_to_raw_response_wrapper(
            by_tag.get,
        )


class ByTagResourceWithStreamingResponse:
    def __init__(self, by_tag: ByTagResource) -> None:
        self._by_tag = by_tag

        self.get = to_streamed_response_wrapper(
            by_tag.get,
        )


class AsyncByTagResourceWithStreamingResponse:
    def __init__(self, by_tag: AsyncByTagResource) -> None:
        self._by_tag = by_tag

        self.get = async_to_streamed_response_wrapper(
            by_tag.get,
        )
