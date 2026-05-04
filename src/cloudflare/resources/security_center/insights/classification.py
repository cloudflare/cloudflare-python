# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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
from ...._base_client import make_request_options
from ....types.security_center.insights import classification_update_params
from ....types.security_center.insights.classification_update_response import ClassificationUpdateResponse

__all__ = ["ClassificationResource", "AsyncClassificationResource"]


class ClassificationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ClassificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ClassificationResourceWithStreamingResponse(self)

    def update(
        self,
        issue_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        classification: Optional[Literal["false_positive", "accept_risk", "other"]] | Omit = omit,
        rationale: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassificationUpdateResponse:
        """Updates the user classification for a Security Center insight.

        Valid values are
        'false_positive' or 'accept_risk'. To reset, set classification to null. Cannot
        change directly between classification values - must reset to null first.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          classification: User-defined classification for the insight. Can be 'false_positive',
              'accept_risk', 'other', or null.

          rationale: Rationale for the classification change. Required when classification is
              'accept_risk' or 'other'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not issue_id:
            raise ValueError(f"Expected a non-empty value for `issue_id` but received {issue_id!r}")
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
        return self._patch(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/security-center/insights/{issue_id}/classification",
                issue_id=issue_id,
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            body=maybe_transform(
                {
                    "classification": classification,
                    "rationale": rationale,
                },
                classification_update_params.ClassificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassificationUpdateResponse,
        )


class AsyncClassificationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClassificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncClassificationResourceWithStreamingResponse(self)

    async def update(
        self,
        issue_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        classification: Optional[Literal["false_positive", "accept_risk", "other"]] | Omit = omit,
        rationale: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassificationUpdateResponse:
        """Updates the user classification for a Security Center insight.

        Valid values are
        'false_positive' or 'accept_risk'. To reset, set classification to null. Cannot
        change directly between classification values - must reset to null first.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          classification: User-defined classification for the insight. Can be 'false_positive',
              'accept_risk', 'other', or null.

          rationale: Rationale for the classification change. Required when classification is
              'accept_risk' or 'other'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not issue_id:
            raise ValueError(f"Expected a non-empty value for `issue_id` but received {issue_id!r}")
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
        return await self._patch(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/security-center/insights/{issue_id}/classification",
                issue_id=issue_id,
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            body=await async_maybe_transform(
                {
                    "classification": classification,
                    "rationale": rationale,
                },
                classification_update_params.ClassificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassificationUpdateResponse,
        )


class ClassificationResourceWithRawResponse:
    def __init__(self, classification: ClassificationResource) -> None:
        self._classification = classification

        self.update = to_raw_response_wrapper(
            classification.update,
        )


class AsyncClassificationResourceWithRawResponse:
    def __init__(self, classification: AsyncClassificationResource) -> None:
        self._classification = classification

        self.update = async_to_raw_response_wrapper(
            classification.update,
        )


class ClassificationResourceWithStreamingResponse:
    def __init__(self, classification: ClassificationResource) -> None:
        self._classification = classification

        self.update = to_streamed_response_wrapper(
            classification.update,
        )


class AsyncClassificationResourceWithStreamingResponse:
    def __init__(self, classification: AsyncClassificationResource) -> None:
        self._classification = classification

        self.update = async_to_streamed_response_wrapper(
            classification.update,
        )
