# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .custom.custom import (
    CustomResource,
    AsyncCustomResource,
    CustomResourceWithRawResponse,
    AsyncCustomResourceWithRawResponse,
    CustomResourceWithStreamingResponse,
    AsyncCustomResourceWithStreamingResponse,
)
from .default.default import (
    DefaultResource,
    AsyncDefaultResource,
    DefaultResourceWithRawResponse,
    AsyncDefaultResourceWithRawResponse,
    DefaultResourceWithStreamingResponse,
    AsyncDefaultResourceWithStreamingResponse,
)

__all__ = ["PoliciesResource", "AsyncPoliciesResource"]


class PoliciesResource(SyncAPIResource):
    @cached_property
    def default(self) -> DefaultResource:
        return DefaultResource(self._client)

    @cached_property
    def custom(self) -> CustomResource:
        return CustomResource(self._client)

    @cached_property
    def with_raw_response(self) -> PoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PoliciesResourceWithStreamingResponse(self)


class AsyncPoliciesResource(AsyncAPIResource):
    @cached_property
    def default(self) -> AsyncDefaultResource:
        return AsyncDefaultResource(self._client)

    @cached_property
    def custom(self) -> AsyncCustomResource:
        return AsyncCustomResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPoliciesResourceWithStreamingResponse(self)


class PoliciesResourceWithRawResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

    @cached_property
    def default(self) -> DefaultResourceWithRawResponse:
        return DefaultResourceWithRawResponse(self._policies.default)

    @cached_property
    def custom(self) -> CustomResourceWithRawResponse:
        return CustomResourceWithRawResponse(self._policies.custom)


class AsyncPoliciesResourceWithRawResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

    @cached_property
    def default(self) -> AsyncDefaultResourceWithRawResponse:
        return AsyncDefaultResourceWithRawResponse(self._policies.default)

    @cached_property
    def custom(self) -> AsyncCustomResourceWithRawResponse:
        return AsyncCustomResourceWithRawResponse(self._policies.custom)


class PoliciesResourceWithStreamingResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

    @cached_property
    def default(self) -> DefaultResourceWithStreamingResponse:
        return DefaultResourceWithStreamingResponse(self._policies.default)

    @cached_property
    def custom(self) -> CustomResourceWithStreamingResponse:
        return CustomResourceWithStreamingResponse(self._policies.custom)


class AsyncPoliciesResourceWithStreamingResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

    @cached_property
    def default(self) -> AsyncDefaultResourceWithStreamingResponse:
        return AsyncDefaultResourceWithStreamingResponse(self._policies.default)

    @cached_property
    def custom(self) -> AsyncCustomResourceWithStreamingResponse:
        return AsyncCustomResourceWithStreamingResponse(self._policies.custom)
