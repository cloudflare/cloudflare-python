# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.flagship.apps import evaluate_get_params
from ....types.flagship.apps.evaluate_get_response import EvaluateGetResponse

__all__ = ["EvaluateResource", "AsyncEvaluateResource"]


class EvaluateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EvaluateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EvaluateResourceWithStreamingResponse(self)

    def get(
        self,
        app_id: str,
        *,
        account_id: str,
        flag_key: str,
        targeting_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluateGetResponse:
        """Evaluates a flag against the provided context.

        Pass context attributes as query
        parameters; boolean and numeric strings are coerced automatically. For
        low-latency in-Worker evaluation, prefer the Flagship binding over this
        endpoint.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          flag_key: The flag key to evaluate.

          targeting_key: Context targeting key (per OpenFeature spec); used for percentage rollout
              bucketing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/flagship/apps/{app_id}/evaluate", account_id=account_id, app_id=app_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "flag_key": flag_key,
                        "targeting_key": targeting_key,
                    },
                    evaluate_get_params.EvaluateGetParams,
                ),
            ),
            cast_to=EvaluateGetResponse,
        )


class AsyncEvaluateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEvaluateResourceWithStreamingResponse(self)

    async def get(
        self,
        app_id: str,
        *,
        account_id: str,
        flag_key: str,
        targeting_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluateGetResponse:
        """Evaluates a flag against the provided context.

        Pass context attributes as query
        parameters; boolean and numeric strings are coerced automatically. For
        low-latency in-Worker evaluation, prefer the Flagship binding over this
        endpoint.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          flag_key: The flag key to evaluate.

          targeting_key: Context targeting key (per OpenFeature spec); used for percentage rollout
              bucketing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/flagship/apps/{app_id}/evaluate", account_id=account_id, app_id=app_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "flag_key": flag_key,
                        "targeting_key": targeting_key,
                    },
                    evaluate_get_params.EvaluateGetParams,
                ),
            ),
            cast_to=EvaluateGetResponse,
        )


class EvaluateResourceWithRawResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

        self.get = to_raw_response_wrapper(
            evaluate.get,
        )


class AsyncEvaluateResourceWithRawResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

        self.get = async_to_raw_response_wrapper(
            evaluate.get,
        )


class EvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

        self.get = to_streamed_response_wrapper(
            evaluate.get,
        )


class AsyncEvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

        self.get = async_to_streamed_response_wrapper(
            evaluate.get,
        )
