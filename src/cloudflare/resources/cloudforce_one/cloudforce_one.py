# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .scans.scans import (
    ScansResource,
    AsyncScansResource,
    ScansResourceWithRawResponse,
    AsyncScansResourceWithRawResponse,
    ScansResourceWithStreamingResponse,
    AsyncScansResourceWithStreamingResponse,
)
from .binary_storage import (
    BinaryStorageResource,
    AsyncBinaryStorageResource,
    BinaryStorageResourceWithRawResponse,
    AsyncBinaryStorageResourceWithRawResponse,
    BinaryStorageResourceWithStreamingResponse,
    AsyncBinaryStorageResourceWithStreamingResponse,
)
from .requests.requests import (
    RequestsResource,
    AsyncRequestsResource,
    RequestsResourceWithRawResponse,
    AsyncRequestsResourceWithRawResponse,
    RequestsResourceWithStreamingResponse,
    AsyncRequestsResourceWithStreamingResponse,
)
from .threat_events.threat_events import (
    ThreatEventsResource,
    AsyncThreatEventsResource,
    ThreatEventsResourceWithRawResponse,
    AsyncThreatEventsResourceWithRawResponse,
    ThreatEventsResourceWithStreamingResponse,
    AsyncThreatEventsResourceWithStreamingResponse,
)
from .threat_signals.threat_signals import (
    ThreatSignalsResource,
    AsyncThreatSignalsResource,
    ThreatSignalsResourceWithRawResponse,
    AsyncThreatSignalsResourceWithRawResponse,
    ThreatSignalsResourceWithStreamingResponse,
    AsyncThreatSignalsResourceWithStreamingResponse,
)

__all__ = ["CloudforceOneResource", "AsyncCloudforceOneResource"]


class CloudforceOneResource(SyncAPIResource):
    @cached_property
    def binary_storage(self) -> BinaryStorageResource:
        return BinaryStorageResource(self._client)

    @cached_property
    def requests(self) -> RequestsResource:
        return RequestsResource(self._client)

    @cached_property
    def scans(self) -> ScansResource:
        return ScansResource(self._client)

    @cached_property
    def threat_events(self) -> ThreatEventsResource:
        return ThreatEventsResource(self._client)

    @cached_property
    def threat_signals(self) -> ThreatSignalsResource:
        """
        Threat Signals API for managing threat intelligence feeds, articles, indicators, and AI skills in Cloudforce One.

        ## Prerequisites

        1. **API token** — requests must use an API token with Cloudforce One permissions; write operations (creating, editing, or deleting feeds, skills, and tags) require write access.
        2. **Plan limits** — access on the Free plan is limited; feed quotas and managed default skills apply.
        """
        return ThreatSignalsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CloudforceOneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CloudforceOneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloudforceOneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CloudforceOneResourceWithStreamingResponse(self)


class AsyncCloudforceOneResource(AsyncAPIResource):
    @cached_property
    def binary_storage(self) -> AsyncBinaryStorageResource:
        return AsyncBinaryStorageResource(self._client)

    @cached_property
    def requests(self) -> AsyncRequestsResource:
        return AsyncRequestsResource(self._client)

    @cached_property
    def scans(self) -> AsyncScansResource:
        return AsyncScansResource(self._client)

    @cached_property
    def threat_events(self) -> AsyncThreatEventsResource:
        return AsyncThreatEventsResource(self._client)

    @cached_property
    def threat_signals(self) -> AsyncThreatSignalsResource:
        """
        Threat Signals API for managing threat intelligence feeds, articles, indicators, and AI skills in Cloudforce One.

        ## Prerequisites

        1. **API token** — requests must use an API token with Cloudforce One permissions; write operations (creating, editing, or deleting feeds, skills, and tags) require write access.
        2. **Plan limits** — access on the Free plan is limited; feed quotas and managed default skills apply.
        """
        return AsyncThreatSignalsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCloudforceOneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCloudforceOneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloudforceOneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCloudforceOneResourceWithStreamingResponse(self)


class CloudforceOneResourceWithRawResponse:
    def __init__(self, cloudforce_one: CloudforceOneResource) -> None:
        self._cloudforce_one = cloudforce_one

    @cached_property
    def binary_storage(self) -> BinaryStorageResourceWithRawResponse:
        return BinaryStorageResourceWithRawResponse(self._cloudforce_one.binary_storage)

    @cached_property
    def requests(self) -> RequestsResourceWithRawResponse:
        return RequestsResourceWithRawResponse(self._cloudforce_one.requests)

    @cached_property
    def scans(self) -> ScansResourceWithRawResponse:
        return ScansResourceWithRawResponse(self._cloudforce_one.scans)

    @cached_property
    def threat_events(self) -> ThreatEventsResourceWithRawResponse:
        return ThreatEventsResourceWithRawResponse(self._cloudforce_one.threat_events)

    @cached_property
    def threat_signals(self) -> ThreatSignalsResourceWithRawResponse:
        """
        Threat Signals API for managing threat intelligence feeds, articles, indicators, and AI skills in Cloudforce One.

        ## Prerequisites

        1. **API token** — requests must use an API token with Cloudforce One permissions; write operations (creating, editing, or deleting feeds, skills, and tags) require write access.
        2. **Plan limits** — access on the Free plan is limited; feed quotas and managed default skills apply.
        """
        return ThreatSignalsResourceWithRawResponse(self._cloudforce_one.threat_signals)


class AsyncCloudforceOneResourceWithRawResponse:
    def __init__(self, cloudforce_one: AsyncCloudforceOneResource) -> None:
        self._cloudforce_one = cloudforce_one

    @cached_property
    def binary_storage(self) -> AsyncBinaryStorageResourceWithRawResponse:
        return AsyncBinaryStorageResourceWithRawResponse(self._cloudforce_one.binary_storage)

    @cached_property
    def requests(self) -> AsyncRequestsResourceWithRawResponse:
        return AsyncRequestsResourceWithRawResponse(self._cloudforce_one.requests)

    @cached_property
    def scans(self) -> AsyncScansResourceWithRawResponse:
        return AsyncScansResourceWithRawResponse(self._cloudforce_one.scans)

    @cached_property
    def threat_events(self) -> AsyncThreatEventsResourceWithRawResponse:
        return AsyncThreatEventsResourceWithRawResponse(self._cloudforce_one.threat_events)

    @cached_property
    def threat_signals(self) -> AsyncThreatSignalsResourceWithRawResponse:
        """
        Threat Signals API for managing threat intelligence feeds, articles, indicators, and AI skills in Cloudforce One.

        ## Prerequisites

        1. **API token** — requests must use an API token with Cloudforce One permissions; write operations (creating, editing, or deleting feeds, skills, and tags) require write access.
        2. **Plan limits** — access on the Free plan is limited; feed quotas and managed default skills apply.
        """
        return AsyncThreatSignalsResourceWithRawResponse(self._cloudforce_one.threat_signals)


class CloudforceOneResourceWithStreamingResponse:
    def __init__(self, cloudforce_one: CloudforceOneResource) -> None:
        self._cloudforce_one = cloudforce_one

    @cached_property
    def binary_storage(self) -> BinaryStorageResourceWithStreamingResponse:
        return BinaryStorageResourceWithStreamingResponse(self._cloudforce_one.binary_storage)

    @cached_property
    def requests(self) -> RequestsResourceWithStreamingResponse:
        return RequestsResourceWithStreamingResponse(self._cloudforce_one.requests)

    @cached_property
    def scans(self) -> ScansResourceWithStreamingResponse:
        return ScansResourceWithStreamingResponse(self._cloudforce_one.scans)

    @cached_property
    def threat_events(self) -> ThreatEventsResourceWithStreamingResponse:
        return ThreatEventsResourceWithStreamingResponse(self._cloudforce_one.threat_events)

    @cached_property
    def threat_signals(self) -> ThreatSignalsResourceWithStreamingResponse:
        """
        Threat Signals API for managing threat intelligence feeds, articles, indicators, and AI skills in Cloudforce One.

        ## Prerequisites

        1. **API token** — requests must use an API token with Cloudforce One permissions; write operations (creating, editing, or deleting feeds, skills, and tags) require write access.
        2. **Plan limits** — access on the Free plan is limited; feed quotas and managed default skills apply.
        """
        return ThreatSignalsResourceWithStreamingResponse(self._cloudforce_one.threat_signals)


class AsyncCloudforceOneResourceWithStreamingResponse:
    def __init__(self, cloudforce_one: AsyncCloudforceOneResource) -> None:
        self._cloudforce_one = cloudforce_one

    @cached_property
    def binary_storage(self) -> AsyncBinaryStorageResourceWithStreamingResponse:
        return AsyncBinaryStorageResourceWithStreamingResponse(self._cloudforce_one.binary_storage)

    @cached_property
    def requests(self) -> AsyncRequestsResourceWithStreamingResponse:
        return AsyncRequestsResourceWithStreamingResponse(self._cloudforce_one.requests)

    @cached_property
    def scans(self) -> AsyncScansResourceWithStreamingResponse:
        return AsyncScansResourceWithStreamingResponse(self._cloudforce_one.scans)

    @cached_property
    def threat_events(self) -> AsyncThreatEventsResourceWithStreamingResponse:
        return AsyncThreatEventsResourceWithStreamingResponse(self._cloudforce_one.threat_events)

    @cached_property
    def threat_signals(self) -> AsyncThreatSignalsResourceWithStreamingResponse:
        """
        Threat Signals API for managing threat intelligence feeds, articles, indicators, and AI skills in Cloudforce One.

        ## Prerequisites

        1. **API token** — requests must use an API token with Cloudforce One permissions; write operations (creating, editing, or deleting feeds, skills, and tags) require write access.
        2. **Plan limits** — access on the Free plan is limited; feed quotas and managed default skills apply.
        """
        return AsyncThreatSignalsResourceWithStreamingResponse(self._cloudforce_one.threat_signals)
