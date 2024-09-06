# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .investigate import InvestigateResource, AsyncInvestigateResource

from ..._compat import cached_property

from .phishguard import PhishguardResource, AsyncPhishguardResource

from .settings.settings import SettingsResource, AsyncSettingsResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .investigate import (
    InvestigateResource,
    AsyncInvestigateResource,
    InvestigateResourceWithRawResponse,
    AsyncInvestigateResourceWithRawResponse,
    InvestigateResourceWithStreamingResponse,
    AsyncInvestigateResourceWithStreamingResponse,
)
from .phishguard import (
    PhishguardResource,
    AsyncPhishguardResource,
    PhishguardResourceWithRawResponse,
    AsyncPhishguardResourceWithRawResponse,
    PhishguardResourceWithStreamingResponse,
    AsyncPhishguardResourceWithStreamingResponse,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)

__all__ = ["EmailSecurityResource", "AsyncEmailSecurityResource"]


class EmailSecurityResource(SyncAPIResource):
    @cached_property
    def investigate(self) -> InvestigateResource:
        return InvestigateResource(self._client)

    @cached_property
    def phishguard(self) -> PhishguardResource:
        return PhishguardResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailSecurityResourceWithRawResponse:
        return EmailSecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailSecurityResourceWithStreamingResponse:
        return EmailSecurityResourceWithStreamingResponse(self)


class AsyncEmailSecurityResource(AsyncAPIResource):
    @cached_property
    def investigate(self) -> AsyncInvestigateResource:
        return AsyncInvestigateResource(self._client)

    @cached_property
    def phishguard(self) -> AsyncPhishguardResource:
        return AsyncPhishguardResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailSecurityResourceWithRawResponse:
        return AsyncEmailSecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailSecurityResourceWithStreamingResponse:
        return AsyncEmailSecurityResourceWithStreamingResponse(self)


class EmailSecurityResourceWithRawResponse:
    def __init__(self, email_security: EmailSecurityResource) -> None:
        self._email_security = email_security

    @cached_property
    def investigate(self) -> InvestigateResourceWithRawResponse:
        return InvestigateResourceWithRawResponse(self._email_security.investigate)

    @cached_property
    def phishguard(self) -> PhishguardResourceWithRawResponse:
        return PhishguardResourceWithRawResponse(self._email_security.phishguard)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._email_security.settings)


class AsyncEmailSecurityResourceWithRawResponse:
    def __init__(self, email_security: AsyncEmailSecurityResource) -> None:
        self._email_security = email_security

    @cached_property
    def investigate(self) -> AsyncInvestigateResourceWithRawResponse:
        return AsyncInvestigateResourceWithRawResponse(self._email_security.investigate)

    @cached_property
    def phishguard(self) -> AsyncPhishguardResourceWithRawResponse:
        return AsyncPhishguardResourceWithRawResponse(self._email_security.phishguard)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._email_security.settings)


class EmailSecurityResourceWithStreamingResponse:
    def __init__(self, email_security: EmailSecurityResource) -> None:
        self._email_security = email_security

    @cached_property
    def investigate(self) -> InvestigateResourceWithStreamingResponse:
        return InvestigateResourceWithStreamingResponse(self._email_security.investigate)

    @cached_property
    def phishguard(self) -> PhishguardResourceWithStreamingResponse:
        return PhishguardResourceWithStreamingResponse(self._email_security.phishguard)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._email_security.settings)


class AsyncEmailSecurityResourceWithStreamingResponse:
    def __init__(self, email_security: AsyncEmailSecurityResource) -> None:
        self._email_security = email_security

    @cached_property
    def investigate(self) -> AsyncInvestigateResourceWithStreamingResponse:
        return AsyncInvestigateResourceWithStreamingResponse(self._email_security.investigate)

    @cached_property
    def phishguard(self) -> AsyncPhishguardResourceWithStreamingResponse:
        return AsyncPhishguardResourceWithStreamingResponse(self._email_security.phishguard)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._email_security.settings)
