# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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

__all__ = ["RegistrationStatusResource", "AsyncRegistrationStatusResource"]


class RegistrationStatusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegistrationStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RegistrationStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegistrationStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RegistrationStatusResourceWithStreamingResponse(self)

    def get(
        self,
        domain_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowStatus:
        """
        Returns the current status of a domain registration workflow.

        Use this endpoint to poll for completion when the POST response returned
        `202 Accepted`. The URL is provided in the `links.self` field of the workflow
        status response.

        Poll this endpoint until the workflow reaches a terminal state or a state that
        requires user attention.

        **Terminal states:** `succeeded` and `failed` are terminal and always have
        `completed: true`.

        **Non-terminal states:**

        - `action_required` has `completed: false` and will not resolve on its own. The
          workflow is paused pending user intervention.
        - `blocked` has `completed: false` and indicates the workflow is waiting on a
          third party such as the extension registry or losing registrar. Continue
          polling while informing the user of the delay.

        Use increasing backoff between polls. When `state: blocked`, use a longer
        polling interval and do not poll indefinitely.

        A naive polling loop that only checks `completed` can run indefinitely when
        `state: action_required`. Break explicitly on `action_required`:

        ```js
        let status;
        do {
          await new Promise((r) => setTimeout(r, 2000));
          status = await cloudflare.request({
            method: "GET",
            path: reg.result.links.self,
          });
        } while (!status.result.completed && status.result.state !== "action_required");

        if (status.result.state === "action_required") {
          // Surface context.action and context.confirmation_sent_to to the user.
          // Do not re-submit the registration request.
        }
        ```

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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return self._get(
            f"/accounts/{account_id}/registrar/registrations/{domain_name}/registration-status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WorkflowStatus]._unwrapper,
            ),
            cast_to=cast(Type[WorkflowStatus], ResultWrapper[WorkflowStatus]),
        )


class AsyncRegistrationStatusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegistrationStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegistrationStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegistrationStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRegistrationStatusResourceWithStreamingResponse(self)

    async def get(
        self,
        domain_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowStatus:
        """
        Returns the current status of a domain registration workflow.

        Use this endpoint to poll for completion when the POST response returned
        `202 Accepted`. The URL is provided in the `links.self` field of the workflow
        status response.

        Poll this endpoint until the workflow reaches a terminal state or a state that
        requires user attention.

        **Terminal states:** `succeeded` and `failed` are terminal and always have
        `completed: true`.

        **Non-terminal states:**

        - `action_required` has `completed: false` and will not resolve on its own. The
          workflow is paused pending user intervention.
        - `blocked` has `completed: false` and indicates the workflow is waiting on a
          third party such as the extension registry or losing registrar. Continue
          polling while informing the user of the delay.

        Use increasing backoff between polls. When `state: blocked`, use a longer
        polling interval and do not poll indefinitely.

        A naive polling loop that only checks `completed` can run indefinitely when
        `state: action_required`. Break explicitly on `action_required`:

        ```js
        let status;
        do {
          await new Promise((r) => setTimeout(r, 2000));
          status = await cloudflare.request({
            method: "GET",
            path: reg.result.links.self,
          });
        } while (!status.result.completed && status.result.state !== "action_required");

        if (status.result.state === "action_required") {
          // Surface context.action and context.confirmation_sent_to to the user.
          // Do not re-submit the registration request.
        }
        ```

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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return await self._get(
            f"/accounts/{account_id}/registrar/registrations/{domain_name}/registration-status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WorkflowStatus]._unwrapper,
            ),
            cast_to=cast(Type[WorkflowStatus], ResultWrapper[WorkflowStatus]),
        )


class RegistrationStatusResourceWithRawResponse:
    def __init__(self, registration_status: RegistrationStatusResource) -> None:
        self._registration_status = registration_status

        self.get = to_raw_response_wrapper(
            registration_status.get,
        )


class AsyncRegistrationStatusResourceWithRawResponse:
    def __init__(self, registration_status: AsyncRegistrationStatusResource) -> None:
        self._registration_status = registration_status

        self.get = async_to_raw_response_wrapper(
            registration_status.get,
        )


class RegistrationStatusResourceWithStreamingResponse:
    def __init__(self, registration_status: RegistrationStatusResource) -> None:
        self._registration_status = registration_status

        self.get = to_streamed_response_wrapper(
            registration_status.get,
        )


class AsyncRegistrationStatusResourceWithStreamingResponse:
    def __init__(self, registration_status: AsyncRegistrationStatusResource) -> None:
        self._registration_status = registration_status

        self.get = async_to_streamed_response_wrapper(
            registration_status.get,
        )
