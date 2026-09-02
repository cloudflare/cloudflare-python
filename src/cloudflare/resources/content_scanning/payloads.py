# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.content_scanning import payload_create_params, payload_update_params
from ...types.content_scanning.payload_list_response import PayloadListResponse
from ...types.content_scanning.payload_create_response import PayloadCreateResponse
from ...types.content_scanning.payload_delete_response import PayloadDeleteResponse
from ...types.content_scanning.payload_update_response import PayloadUpdateResponse

__all__ = ["PayloadsResource", "AsyncPayloadsResource"]


class PayloadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PayloadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PayloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayloadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PayloadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        body: Iterable[payload_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[PayloadCreateResponse]:
        """
        Create one or more Content Scanning custom expressions, appending them to the
        existing list of the zone, and return the updated list. Each expression reaches
        content objects the scanner cannot find automatically, for example
        `lookup_json_string(http.request.body.raw, "file")`.

        Args:
          zone_id: Defines an identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/content-upload-scan/payloads", zone_id=zone_id),
            page=SyncSinglePage[PayloadCreateResponse],
            body=maybe_transform(body, Iterable[payload_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayloadCreateResponse,
            method="post",
        )

    def update(
        self,
        expression_id: str,
        *,
        zone_id: str,
        payload: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[PayloadUpdateResponse]:
        """
        Update the Content Scanning custom expression with the given identifier and
        return the updated list of expressions.

        Args:
          zone_id: Defines an identifier.

          expression_id: Defines the unique ID for this Content Scanning custom expression.

          payload: Defines the custom content extraction expression used to reach content objects
              in the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not expression_id:
            raise ValueError(f"Expected a non-empty value for `expression_id` but received {expression_id!r}")
        return self._get_api_list(
            path_template(
                "/zones/{zone_id}/content-upload-scan/payloads/{expression_id}",
                zone_id=zone_id,
                expression_id=expression_id,
            ),
            page=SyncSinglePage[PayloadUpdateResponse],
            body=maybe_transform({"payload": payload}, payload_update_params.PayloadUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayloadUpdateResponse,
            method="patch",
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[PayloadListResponse]:
        """
        List the Content Scanning custom expressions configured for the zone, each with
        its own identifier. A custom expression tells the scanner how to reach content
        objects in a request it cannot parse on its own, such as files Base64-encoded
        inside a JSON body.

        Args:
          zone_id: Defines an identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/content-upload-scan/payloads", zone_id=zone_id),
            page=SyncSinglePage[PayloadListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayloadListResponse,
        )

    def delete(
        self,
        expression_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[PayloadDeleteResponse]:
        """
        Delete the Content Scanning custom expression with the given identifier and
        return the expressions that remain. Content objects reached only by the deleted
        expression are no longer scanned.

        Args:
          zone_id: Defines an identifier.

          expression_id: Defines the unique ID for this Content Scanning custom expression.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not expression_id:
            raise ValueError(f"Expected a non-empty value for `expression_id` but received {expression_id!r}")
        return self._get_api_list(
            path_template(
                "/zones/{zone_id}/content-upload-scan/payloads/{expression_id}",
                zone_id=zone_id,
                expression_id=expression_id,
            ),
            page=SyncSinglePage[PayloadDeleteResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayloadDeleteResponse,
            method="delete",
        )


class AsyncPayloadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPayloadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPayloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayloadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPayloadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        body: Iterable[payload_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PayloadCreateResponse, AsyncSinglePage[PayloadCreateResponse]]:
        """
        Create one or more Content Scanning custom expressions, appending them to the
        existing list of the zone, and return the updated list. Each expression reaches
        content objects the scanner cannot find automatically, for example
        `lookup_json_string(http.request.body.raw, "file")`.

        Args:
          zone_id: Defines an identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/content-upload-scan/payloads", zone_id=zone_id),
            page=AsyncSinglePage[PayloadCreateResponse],
            body=maybe_transform(body, Iterable[payload_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayloadCreateResponse,
            method="post",
        )

    def update(
        self,
        expression_id: str,
        *,
        zone_id: str,
        payload: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PayloadUpdateResponse, AsyncSinglePage[PayloadUpdateResponse]]:
        """
        Update the Content Scanning custom expression with the given identifier and
        return the updated list of expressions.

        Args:
          zone_id: Defines an identifier.

          expression_id: Defines the unique ID for this Content Scanning custom expression.

          payload: Defines the custom content extraction expression used to reach content objects
              in the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not expression_id:
            raise ValueError(f"Expected a non-empty value for `expression_id` but received {expression_id!r}")
        return self._get_api_list(
            path_template(
                "/zones/{zone_id}/content-upload-scan/payloads/{expression_id}",
                zone_id=zone_id,
                expression_id=expression_id,
            ),
            page=AsyncSinglePage[PayloadUpdateResponse],
            body=maybe_transform({"payload": payload}, payload_update_params.PayloadUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayloadUpdateResponse,
            method="patch",
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PayloadListResponse, AsyncSinglePage[PayloadListResponse]]:
        """
        List the Content Scanning custom expressions configured for the zone, each with
        its own identifier. A custom expression tells the scanner how to reach content
        objects in a request it cannot parse on its own, such as files Base64-encoded
        inside a JSON body.

        Args:
          zone_id: Defines an identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/content-upload-scan/payloads", zone_id=zone_id),
            page=AsyncSinglePage[PayloadListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayloadListResponse,
        )

    def delete(
        self,
        expression_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PayloadDeleteResponse, AsyncSinglePage[PayloadDeleteResponse]]:
        """
        Delete the Content Scanning custom expression with the given identifier and
        return the expressions that remain. Content objects reached only by the deleted
        expression are no longer scanned.

        Args:
          zone_id: Defines an identifier.

          expression_id: Defines the unique ID for this Content Scanning custom expression.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not expression_id:
            raise ValueError(f"Expected a non-empty value for `expression_id` but received {expression_id!r}")
        return self._get_api_list(
            path_template(
                "/zones/{zone_id}/content-upload-scan/payloads/{expression_id}",
                zone_id=zone_id,
                expression_id=expression_id,
            ),
            page=AsyncSinglePage[PayloadDeleteResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PayloadDeleteResponse,
            method="delete",
        )


class PayloadsResourceWithRawResponse:
    def __init__(self, payloads: PayloadsResource) -> None:
        self._payloads = payloads

        self.create = to_raw_response_wrapper(
            payloads.create,
        )
        self.update = to_raw_response_wrapper(
            payloads.update,
        )
        self.list = to_raw_response_wrapper(
            payloads.list,
        )
        self.delete = to_raw_response_wrapper(
            payloads.delete,
        )


class AsyncPayloadsResourceWithRawResponse:
    def __init__(self, payloads: AsyncPayloadsResource) -> None:
        self._payloads = payloads

        self.create = async_to_raw_response_wrapper(
            payloads.create,
        )
        self.update = async_to_raw_response_wrapper(
            payloads.update,
        )
        self.list = async_to_raw_response_wrapper(
            payloads.list,
        )
        self.delete = async_to_raw_response_wrapper(
            payloads.delete,
        )


class PayloadsResourceWithStreamingResponse:
    def __init__(self, payloads: PayloadsResource) -> None:
        self._payloads = payloads

        self.create = to_streamed_response_wrapper(
            payloads.create,
        )
        self.update = to_streamed_response_wrapper(
            payloads.update,
        )
        self.list = to_streamed_response_wrapper(
            payloads.list,
        )
        self.delete = to_streamed_response_wrapper(
            payloads.delete,
        )


class AsyncPayloadsResourceWithStreamingResponse:
    def __init__(self, payloads: AsyncPayloadsResource) -> None:
        self._payloads = payloads

        self.create = async_to_streamed_response_wrapper(
            payloads.create,
        )
        self.update = async_to_streamed_response_wrapper(
            payloads.update,
        )
        self.list = async_to_streamed_response_wrapper(
            payloads.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            payloads.delete,
        )
