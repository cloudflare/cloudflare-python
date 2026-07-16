# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .content import (
    ContentResource,
    AsyncContentResource,
    ContentResourceWithRawResponse,
    AsyncContentResourceWithRawResponse,
    ContentResourceWithStreamingResponse,
    AsyncContentResourceWithStreamingResponse,
)
from .exports import (
    ExportsResource,
    AsyncExportsResource,
    ExportsResourceWithRawResponse,
    AsyncExportsResourceWithRawResponse,
    ExportsResourceWithStreamingResponse,
    AsyncExportsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .findings.findings import (
    FindingsResource,
    AsyncFindingsResource,
    FindingsResourceWithRawResponse,
    AsyncFindingsResourceWithRawResponse,
    FindingsResourceWithStreamingResponse,
    AsyncFindingsResourceWithStreamingResponse,
)
from .webhooks.webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
)
from .remediations.remediations import (
    RemediationsResource,
    AsyncRemediationsResource,
    RemediationsResourceWithRawResponse,
    AsyncRemediationsResourceWithRawResponse,
    RemediationsResourceWithStreamingResponse,
    AsyncRemediationsResourceWithStreamingResponse,
)
from .finding_types.finding_types import (
    FindingTypesResource,
    AsyncFindingTypesResource,
    FindingTypesResourceWithRawResponse,
    AsyncFindingTypesResourceWithRawResponse,
    FindingTypesResourceWithStreamingResponse,
    AsyncFindingTypesResourceWithStreamingResponse,
)

__all__ = ["PostureResource", "AsyncPostureResource"]


class PostureResource(SyncAPIResource):
    @cached_property
    def findings(self) -> FindingsResource:
        return FindingsResource(self._client)

    @cached_property
    def exports(self) -> ExportsResource:
        return ExportsResource(self._client)

    @cached_property
    def finding_types(self) -> FindingTypesResource:
        return FindingTypesResource(self._client)

    @cached_property
    def content(self) -> ContentResource:
        return ContentResource(self._client)

    @cached_property
    def remediations(self) -> RemediationsResource:
        return RemediationsResource(self._client)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        return WebhooksResource(self._client)

    @cached_property
    def with_raw_response(self) -> PostureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PostureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PostureResourceWithStreamingResponse(self)


class AsyncPostureResource(AsyncAPIResource):
    @cached_property
    def findings(self) -> AsyncFindingsResource:
        return AsyncFindingsResource(self._client)

    @cached_property
    def exports(self) -> AsyncExportsResource:
        return AsyncExportsResource(self._client)

    @cached_property
    def finding_types(self) -> AsyncFindingTypesResource:
        return AsyncFindingTypesResource(self._client)

    @cached_property
    def content(self) -> AsyncContentResource:
        return AsyncContentResource(self._client)

    @cached_property
    def remediations(self) -> AsyncRemediationsResource:
        return AsyncRemediationsResource(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        return AsyncWebhooksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPostureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPostureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPostureResourceWithStreamingResponse(self)


class PostureResourceWithRawResponse:
    def __init__(self, posture: PostureResource) -> None:
        self._posture = posture

    @cached_property
    def findings(self) -> FindingsResourceWithRawResponse:
        return FindingsResourceWithRawResponse(self._posture.findings)

    @cached_property
    def exports(self) -> ExportsResourceWithRawResponse:
        return ExportsResourceWithRawResponse(self._posture.exports)

    @cached_property
    def finding_types(self) -> FindingTypesResourceWithRawResponse:
        return FindingTypesResourceWithRawResponse(self._posture.finding_types)

    @cached_property
    def content(self) -> ContentResourceWithRawResponse:
        return ContentResourceWithRawResponse(self._posture.content)

    @cached_property
    def remediations(self) -> RemediationsResourceWithRawResponse:
        return RemediationsResourceWithRawResponse(self._posture.remediations)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        return WebhooksResourceWithRawResponse(self._posture.webhooks)


class AsyncPostureResourceWithRawResponse:
    def __init__(self, posture: AsyncPostureResource) -> None:
        self._posture = posture

    @cached_property
    def findings(self) -> AsyncFindingsResourceWithRawResponse:
        return AsyncFindingsResourceWithRawResponse(self._posture.findings)

    @cached_property
    def exports(self) -> AsyncExportsResourceWithRawResponse:
        return AsyncExportsResourceWithRawResponse(self._posture.exports)

    @cached_property
    def finding_types(self) -> AsyncFindingTypesResourceWithRawResponse:
        return AsyncFindingTypesResourceWithRawResponse(self._posture.finding_types)

    @cached_property
    def content(self) -> AsyncContentResourceWithRawResponse:
        return AsyncContentResourceWithRawResponse(self._posture.content)

    @cached_property
    def remediations(self) -> AsyncRemediationsResourceWithRawResponse:
        return AsyncRemediationsResourceWithRawResponse(self._posture.remediations)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        return AsyncWebhooksResourceWithRawResponse(self._posture.webhooks)


class PostureResourceWithStreamingResponse:
    def __init__(self, posture: PostureResource) -> None:
        self._posture = posture

    @cached_property
    def findings(self) -> FindingsResourceWithStreamingResponse:
        return FindingsResourceWithStreamingResponse(self._posture.findings)

    @cached_property
    def exports(self) -> ExportsResourceWithStreamingResponse:
        return ExportsResourceWithStreamingResponse(self._posture.exports)

    @cached_property
    def finding_types(self) -> FindingTypesResourceWithStreamingResponse:
        return FindingTypesResourceWithStreamingResponse(self._posture.finding_types)

    @cached_property
    def content(self) -> ContentResourceWithStreamingResponse:
        return ContentResourceWithStreamingResponse(self._posture.content)

    @cached_property
    def remediations(self) -> RemediationsResourceWithStreamingResponse:
        return RemediationsResourceWithStreamingResponse(self._posture.remediations)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        return WebhooksResourceWithStreamingResponse(self._posture.webhooks)


class AsyncPostureResourceWithStreamingResponse:
    def __init__(self, posture: AsyncPostureResource) -> None:
        self._posture = posture

    @cached_property
    def findings(self) -> AsyncFindingsResourceWithStreamingResponse:
        return AsyncFindingsResourceWithStreamingResponse(self._posture.findings)

    @cached_property
    def exports(self) -> AsyncExportsResourceWithStreamingResponse:
        return AsyncExportsResourceWithStreamingResponse(self._posture.exports)

    @cached_property
    def finding_types(self) -> AsyncFindingTypesResourceWithStreamingResponse:
        return AsyncFindingTypesResourceWithStreamingResponse(self._posture.finding_types)

    @cached_property
    def content(self) -> AsyncContentResourceWithStreamingResponse:
        return AsyncContentResourceWithStreamingResponse(self._posture.content)

    @cached_property
    def remediations(self) -> AsyncRemediationsResourceWithStreamingResponse:
        return AsyncRemediationsResourceWithStreamingResponse(self._posture.remediations)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        return AsyncWebhooksResourceWithStreamingResponse(self._posture.webhooks)
