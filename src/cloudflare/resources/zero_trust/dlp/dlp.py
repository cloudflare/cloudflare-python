# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .limits import (
    LimitsResource,
    AsyncLimitsResource,
    LimitsResourceWithRawResponse,
    AsyncLimitsResourceWithRawResponse,
    LimitsResourceWithStreamingResponse,
    AsyncLimitsResourceWithStreamingResponse,
)
from .entries import (
    EntriesResource,
    AsyncEntriesResource,
    EntriesResourceWithRawResponse,
    AsyncEntriesResourceWithRawResponse,
    EntriesResourceWithStreamingResponse,
    AsyncEntriesResourceWithStreamingResponse,
)
from .patterns import (
    PatternsResource,
    AsyncPatternsResource,
    PatternsResourceWithRawResponse,
    AsyncPatternsResourceWithRawResponse,
    PatternsResourceWithStreamingResponse,
    AsyncPatternsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .email.email import (
    EmailResource,
    AsyncEmailResource,
    EmailResourceWithRawResponse,
    AsyncEmailResourceWithRawResponse,
    EmailResourceWithStreamingResponse,
    AsyncEmailResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .payload_logs import (
    PayloadLogsResource,
    AsyncPayloadLogsResource,
    PayloadLogsResourceWithRawResponse,
    AsyncPayloadLogsResourceWithRawResponse,
    PayloadLogsResourceWithStreamingResponse,
    AsyncPayloadLogsResourceWithStreamingResponse,
)
from .datasets.datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
)
from .profiles.profiles import (
    ProfilesResource,
    AsyncProfilesResource,
    ProfilesResourceWithRawResponse,
    AsyncProfilesResourceWithRawResponse,
    ProfilesResourceWithStreamingResponse,
    AsyncProfilesResourceWithStreamingResponse,
)

__all__ = ["DLPResource", "AsyncDLPResource"]


class DLPResource(SyncAPIResource):
    @cached_property
    def datasets(self) -> DatasetsResource:
        return DatasetsResource(self._client)

    @cached_property
    def patterns(self) -> PatternsResource:
        return PatternsResource(self._client)

    @cached_property
    def payload_logs(self) -> PayloadLogsResource:
        return PayloadLogsResource(self._client)

    @cached_property
    def email(self) -> EmailResource:
        return EmailResource(self._client)

    @cached_property
    def profiles(self) -> ProfilesResource:
        return ProfilesResource(self._client)

    @cached_property
    def limits(self) -> LimitsResource:
        return LimitsResource(self._client)

    @cached_property
    def entries(self) -> EntriesResource:
        return EntriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DLPResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DLPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DLPResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DLPResourceWithStreamingResponse(self)


class AsyncDLPResource(AsyncAPIResource):
    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        return AsyncDatasetsResource(self._client)

    @cached_property
    def patterns(self) -> AsyncPatternsResource:
        return AsyncPatternsResource(self._client)

    @cached_property
    def payload_logs(self) -> AsyncPayloadLogsResource:
        return AsyncPayloadLogsResource(self._client)

    @cached_property
    def email(self) -> AsyncEmailResource:
        return AsyncEmailResource(self._client)

    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        return AsyncProfilesResource(self._client)

    @cached_property
    def limits(self) -> AsyncLimitsResource:
        return AsyncLimitsResource(self._client)

    @cached_property
    def entries(self) -> AsyncEntriesResource:
        return AsyncEntriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDLPResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDLPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDLPResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDLPResourceWithStreamingResponse(self)


class DLPResourceWithRawResponse:
    def __init__(self, dlp: DLPResource) -> None:
        self._dlp = dlp

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self._dlp.datasets)

    @cached_property
    def patterns(self) -> PatternsResourceWithRawResponse:
        return PatternsResourceWithRawResponse(self._dlp.patterns)

    @cached_property
    def payload_logs(self) -> PayloadLogsResourceWithRawResponse:
        return PayloadLogsResourceWithRawResponse(self._dlp.payload_logs)

    @cached_property
    def email(self) -> EmailResourceWithRawResponse:
        return EmailResourceWithRawResponse(self._dlp.email)

    @cached_property
    def profiles(self) -> ProfilesResourceWithRawResponse:
        return ProfilesResourceWithRawResponse(self._dlp.profiles)

    @cached_property
    def limits(self) -> LimitsResourceWithRawResponse:
        return LimitsResourceWithRawResponse(self._dlp.limits)

    @cached_property
    def entries(self) -> EntriesResourceWithRawResponse:
        return EntriesResourceWithRawResponse(self._dlp.entries)


class AsyncDLPResourceWithRawResponse:
    def __init__(self, dlp: AsyncDLPResource) -> None:
        self._dlp = dlp

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self._dlp.datasets)

    @cached_property
    def patterns(self) -> AsyncPatternsResourceWithRawResponse:
        return AsyncPatternsResourceWithRawResponse(self._dlp.patterns)

    @cached_property
    def payload_logs(self) -> AsyncPayloadLogsResourceWithRawResponse:
        return AsyncPayloadLogsResourceWithRawResponse(self._dlp.payload_logs)

    @cached_property
    def email(self) -> AsyncEmailResourceWithRawResponse:
        return AsyncEmailResourceWithRawResponse(self._dlp.email)

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithRawResponse:
        return AsyncProfilesResourceWithRawResponse(self._dlp.profiles)

    @cached_property
    def limits(self) -> AsyncLimitsResourceWithRawResponse:
        return AsyncLimitsResourceWithRawResponse(self._dlp.limits)

    @cached_property
    def entries(self) -> AsyncEntriesResourceWithRawResponse:
        return AsyncEntriesResourceWithRawResponse(self._dlp.entries)


class DLPResourceWithStreamingResponse:
    def __init__(self, dlp: DLPResource) -> None:
        self._dlp = dlp

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self._dlp.datasets)

    @cached_property
    def patterns(self) -> PatternsResourceWithStreamingResponse:
        return PatternsResourceWithStreamingResponse(self._dlp.patterns)

    @cached_property
    def payload_logs(self) -> PayloadLogsResourceWithStreamingResponse:
        return PayloadLogsResourceWithStreamingResponse(self._dlp.payload_logs)

    @cached_property
    def email(self) -> EmailResourceWithStreamingResponse:
        return EmailResourceWithStreamingResponse(self._dlp.email)

    @cached_property
    def profiles(self) -> ProfilesResourceWithStreamingResponse:
        return ProfilesResourceWithStreamingResponse(self._dlp.profiles)

    @cached_property
    def limits(self) -> LimitsResourceWithStreamingResponse:
        return LimitsResourceWithStreamingResponse(self._dlp.limits)

    @cached_property
    def entries(self) -> EntriesResourceWithStreamingResponse:
        return EntriesResourceWithStreamingResponse(self._dlp.entries)


class AsyncDLPResourceWithStreamingResponse:
    def __init__(self, dlp: AsyncDLPResource) -> None:
        self._dlp = dlp

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self._dlp.datasets)

    @cached_property
    def patterns(self) -> AsyncPatternsResourceWithStreamingResponse:
        return AsyncPatternsResourceWithStreamingResponse(self._dlp.patterns)

    @cached_property
    def payload_logs(self) -> AsyncPayloadLogsResourceWithStreamingResponse:
        return AsyncPayloadLogsResourceWithStreamingResponse(self._dlp.payload_logs)

    @cached_property
    def email(self) -> AsyncEmailResourceWithStreamingResponse:
        return AsyncEmailResourceWithStreamingResponse(self._dlp.email)

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithStreamingResponse:
        return AsyncProfilesResourceWithStreamingResponse(self._dlp.profiles)

    @cached_property
    def limits(self) -> AsyncLimitsResourceWithStreamingResponse:
        return AsyncLimitsResourceWithStreamingResponse(self._dlp.limits)

    @cached_property
    def entries(self) -> AsyncEntriesResourceWithStreamingResponse:
        return AsyncEntriesResourceWithStreamingResponse(self._dlp.entries)
