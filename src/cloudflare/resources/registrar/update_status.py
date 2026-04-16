# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.registrar.workflow_status import WorkflowStatus

__all__ = ["UpdateStatusResource", "AsyncUpdateStatusResource"]


class UpdateStatusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UpdateStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UpdateStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UpdateStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UpdateStatusResourceWithStreamingResponse(self)

    def get(
        self,
        domain_name: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowStatus:
        """
        Returns the current status of a domain update workflow.

        Use this endpoint to poll for completion when the PATCH response returned
        `202 Accepted`. The URL is provided in the `links.self` field of the workflow
        status response.

        Poll this endpoint until the workflow reaches a terminal state or a state that
        requires user attention.

        Use increasing backoff between polls. When the workflow remains blocked on a
        third party, use a longer polling interval and do not poll indefinitely.

        Args:
          account_id: Identifier

          domain_name: Fully qualified domain name (FQDN) including the extension (e.g., `example.com`,
              `mybrand.app`). The domain name uniquely identifies a registration — the same
              domain cannot be registered twice, making it a natural idempotency key for
              registration requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/registrar/registrations/{domain_name}/update-status",
                account_id=account_id,
                domain_name=domain_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WorkflowStatus]._unwrapper,
            ),
            cast_to=cast(Type[WorkflowStatus], ResultWrapper[WorkflowStatus]),
        )


class AsyncUpdateStatusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUpdateStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUpdateStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUpdateStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUpdateStatusResourceWithStreamingResponse(self)

    async def get(
        self,
        domain_name: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowStatus:
        """
        Returns the current status of a domain update workflow.

        Use this endpoint to poll for completion when the PATCH response returned
        `202 Accepted`. The URL is provided in the `links.self` field of the workflow
        status response.

        Poll this endpoint until the workflow reaches a terminal state or a state that
        requires user attention.

        Use increasing backoff between polls. When the workflow remains blocked on a
        third party, use a longer polling interval and do not poll indefinitely.

        Args:
          account_id: Identifier

          domain_name: Fully qualified domain name (FQDN) including the extension (e.g., `example.com`,
              `mybrand.app`). The domain name uniquely identifies a registration — the same
              domain cannot be registered twice, making it a natural idempotency key for
              registration requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/registrar/registrations/{domain_name}/update-status",
                account_id=account_id,
                domain_name=domain_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WorkflowStatus]._unwrapper,
            ),
            cast_to=cast(Type[WorkflowStatus], ResultWrapper[WorkflowStatus]),
        )


class UpdateStatusResourceWithRawResponse:
    def __init__(self, update_status: UpdateStatusResource) -> None:
        self._update_status = update_status

        self.get = to_raw_response_wrapper(
            update_status.get,
        )


class AsyncUpdateStatusResourceWithRawResponse:
    def __init__(self, update_status: AsyncUpdateStatusResource) -> None:
        self._update_status = update_status

        self.get = async_to_raw_response_wrapper(
            update_status.get,
        )


class UpdateStatusResourceWithStreamingResponse:
    def __init__(self, update_status: UpdateStatusResource) -> None:
        self._update_status = update_status

        self.get = to_streamed_response_wrapper(
            update_status.get,
        )


class AsyncUpdateStatusResourceWithStreamingResponse:
    def __init__(self, update_status: AsyncUpdateStatusResource) -> None:
        self._update_status = update_status

        self.get = async_to_streamed_response_wrapper(
            update_status.get,
        )
