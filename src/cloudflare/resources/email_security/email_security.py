# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .submissions import (
    SubmissionsResource,
    AsyncSubmissionsResource,
    SubmissionsResourceWithRawResponse,
    AsyncSubmissionsResourceWithRawResponse,
    SubmissionsResourceWithStreamingResponse,
    AsyncSubmissionsResourceWithStreamingResponse,
)
from .settings.settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from .investigate.investigate import (
    InvestigateResource,
    AsyncInvestigateResource,
    InvestigateResourceWithRawResponse,
    AsyncInvestigateResourceWithRawResponse,
    InvestigateResourceWithStreamingResponse,
    AsyncInvestigateResourceWithStreamingResponse,
)

__all__ = ["EmailSecurityResource", "AsyncEmailSecurityResource"]


class EmailSecurityResource(SyncAPIResource):
    @cached_property
    def investigate(self) -> InvestigateResource:
        return InvestigateResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def submissions(self) -> SubmissionsResource:
        return SubmissionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailSecurityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EmailSecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailSecurityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EmailSecurityResourceWithStreamingResponse(self)


class AsyncEmailSecurityResource(AsyncAPIResource):
    @cached_property
    def investigate(self) -> AsyncInvestigateResource:
        return AsyncInvestigateResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def submissions(self) -> AsyncSubmissionsResource:
        return AsyncSubmissionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailSecurityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailSecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailSecurityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEmailSecurityResourceWithStreamingResponse(self)


class EmailSecurityResourceWithRawResponse:
    def __init__(self, email_security: EmailSecurityResource) -> None:
        self._email_security = email_security

    @cached_property
    def investigate(self) -> InvestigateResourceWithRawResponse:
        return InvestigateResourceWithRawResponse(self._email_security.investigate)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._email_security.settings)

    @cached_property
    def submissions(self) -> SubmissionsResourceWithRawResponse:
        return SubmissionsResourceWithRawResponse(self._email_security.submissions)


class AsyncEmailSecurityResourceWithRawResponse:
    def __init__(self, email_security: AsyncEmailSecurityResource) -> None:
        self._email_security = email_security

    @cached_property
    def investigate(self) -> AsyncInvestigateResourceWithRawResponse:
        return AsyncInvestigateResourceWithRawResponse(self._email_security.investigate)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._email_security.settings)

    @cached_property
    def submissions(self) -> AsyncSubmissionsResourceWithRawResponse:
        return AsyncSubmissionsResourceWithRawResponse(self._email_security.submissions)


class EmailSecurityResourceWithStreamingResponse:
    def __init__(self, email_security: EmailSecurityResource) -> None:
        self._email_security = email_security

    @cached_property
    def investigate(self) -> InvestigateResourceWithStreamingResponse:
        return InvestigateResourceWithStreamingResponse(self._email_security.investigate)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._email_security.settings)

    @cached_property
    def submissions(self) -> SubmissionsResourceWithStreamingResponse:
        return SubmissionsResourceWithStreamingResponse(self._email_security.submissions)


class AsyncEmailSecurityResourceWithStreamingResponse:
    def __init__(self, email_security: AsyncEmailSecurityResource) -> None:
        self._email_security = email_security

    @cached_property
    def investigate(self) -> AsyncInvestigateResourceWithStreamingResponse:
        return AsyncInvestigateResourceWithStreamingResponse(self._email_security.investigate)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._email_security.settings)

    @cached_property
    def submissions(self) -> AsyncSubmissionsResourceWithStreamingResponse:
        return AsyncSubmissionsResourceWithStreamingResponse(self._email_security.submissions)
