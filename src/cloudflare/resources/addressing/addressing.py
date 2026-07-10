# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .services import (
    ServicesResource,
    AsyncServicesResource,
    ServicesResourceWithRawResponse,
    AsyncServicesResourceWithRawResponse,
    ServicesResourceWithStreamingResponse,
    AsyncServicesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .loa_documents import (
    LOADocumentsResource,
    AsyncLOADocumentsResource,
    LOADocumentsResourceWithRawResponse,
    AsyncLOADocumentsResourceWithRawResponse,
    LOADocumentsResourceWithStreamingResponse,
    AsyncLOADocumentsResourceWithStreamingResponse,
)
from .prefixes.prefixes import (
    PrefixesResource,
    AsyncPrefixesResource,
    PrefixesResourceWithRawResponse,
    AsyncPrefixesResourceWithRawResponse,
    PrefixesResourceWithStreamingResponse,
    AsyncPrefixesResourceWithStreamingResponse,
)
from .address_maps.address_maps import (
    AddressMapsResource,
    AsyncAddressMapsResource,
    AddressMapsResourceWithRawResponse,
    AsyncAddressMapsResourceWithRawResponse,
    AddressMapsResourceWithStreamingResponse,
    AsyncAddressMapsResourceWithStreamingResponse,
)
from .regional_hostnames.regional_hostnames import (
    RegionalHostnamesResource,
    AsyncRegionalHostnamesResource,
    RegionalHostnamesResourceWithRawResponse,
    AsyncRegionalHostnamesResourceWithRawResponse,
    RegionalHostnamesResourceWithStreamingResponse,
    AsyncRegionalHostnamesResourceWithStreamingResponse,
)

__all__ = ["AddressingResource", "AsyncAddressingResource"]


class AddressingResource(SyncAPIResource):
    @cached_property
    def regional_hostnames(self) -> RegionalHostnamesResource:
        return RegionalHostnamesResource(self._client)

    @cached_property
    def services(self) -> ServicesResource:
        return ServicesResource(self._client)

    @cached_property
    def address_maps(self) -> AddressMapsResource:
        return AddressMapsResource(self._client)

    @cached_property
    def loa_documents(self) -> LOADocumentsResource:
        return LOADocumentsResource(self._client)

    @cached_property
    def prefixes(self) -> PrefixesResource:
        return PrefixesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AddressingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AddressingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AddressingResourceWithStreamingResponse(self)


class AsyncAddressingResource(AsyncAPIResource):
    @cached_property
    def regional_hostnames(self) -> AsyncRegionalHostnamesResource:
        return AsyncRegionalHostnamesResource(self._client)

    @cached_property
    def services(self) -> AsyncServicesResource:
        return AsyncServicesResource(self._client)

    @cached_property
    def address_maps(self) -> AsyncAddressMapsResource:
        return AsyncAddressMapsResource(self._client)

    @cached_property
    def loa_documents(self) -> AsyncLOADocumentsResource:
        return AsyncLOADocumentsResource(self._client)

    @cached_property
    def prefixes(self) -> AsyncPrefixesResource:
        return AsyncPrefixesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAddressingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAddressingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAddressingResourceWithStreamingResponse(self)


class AddressingResourceWithRawResponse:
    def __init__(self, addressing: AddressingResource) -> None:
        self._addressing = addressing

    @cached_property
    def regional_hostnames(self) -> RegionalHostnamesResourceWithRawResponse:
        return RegionalHostnamesResourceWithRawResponse(self._addressing.regional_hostnames)

    @cached_property
    def services(self) -> ServicesResourceWithRawResponse:
        return ServicesResourceWithRawResponse(self._addressing.services)

    @cached_property
    def address_maps(self) -> AddressMapsResourceWithRawResponse:
        return AddressMapsResourceWithRawResponse(self._addressing.address_maps)

    @cached_property
    def loa_documents(self) -> LOADocumentsResourceWithRawResponse:
        return LOADocumentsResourceWithRawResponse(self._addressing.loa_documents)

    @cached_property
    def prefixes(self) -> PrefixesResourceWithRawResponse:
        return PrefixesResourceWithRawResponse(self._addressing.prefixes)


class AsyncAddressingResourceWithRawResponse:
    def __init__(self, addressing: AsyncAddressingResource) -> None:
        self._addressing = addressing

    @cached_property
    def regional_hostnames(self) -> AsyncRegionalHostnamesResourceWithRawResponse:
        return AsyncRegionalHostnamesResourceWithRawResponse(self._addressing.regional_hostnames)

    @cached_property
    def services(self) -> AsyncServicesResourceWithRawResponse:
        return AsyncServicesResourceWithRawResponse(self._addressing.services)

    @cached_property
    def address_maps(self) -> AsyncAddressMapsResourceWithRawResponse:
        return AsyncAddressMapsResourceWithRawResponse(self._addressing.address_maps)

    @cached_property
    def loa_documents(self) -> AsyncLOADocumentsResourceWithRawResponse:
        return AsyncLOADocumentsResourceWithRawResponse(self._addressing.loa_documents)

    @cached_property
    def prefixes(self) -> AsyncPrefixesResourceWithRawResponse:
        return AsyncPrefixesResourceWithRawResponse(self._addressing.prefixes)


class AddressingResourceWithStreamingResponse:
    def __init__(self, addressing: AddressingResource) -> None:
        self._addressing = addressing

    @cached_property
    def regional_hostnames(self) -> RegionalHostnamesResourceWithStreamingResponse:
        return RegionalHostnamesResourceWithStreamingResponse(self._addressing.regional_hostnames)

    @cached_property
    def services(self) -> ServicesResourceWithStreamingResponse:
        return ServicesResourceWithStreamingResponse(self._addressing.services)

    @cached_property
    def address_maps(self) -> AddressMapsResourceWithStreamingResponse:
        return AddressMapsResourceWithStreamingResponse(self._addressing.address_maps)

    @cached_property
    def loa_documents(self) -> LOADocumentsResourceWithStreamingResponse:
        return LOADocumentsResourceWithStreamingResponse(self._addressing.loa_documents)

    @cached_property
    def prefixes(self) -> PrefixesResourceWithStreamingResponse:
        return PrefixesResourceWithStreamingResponse(self._addressing.prefixes)


class AsyncAddressingResourceWithStreamingResponse:
    def __init__(self, addressing: AsyncAddressingResource) -> None:
        self._addressing = addressing

    @cached_property
    def regional_hostnames(self) -> AsyncRegionalHostnamesResourceWithStreamingResponse:
        return AsyncRegionalHostnamesResourceWithStreamingResponse(self._addressing.regional_hostnames)

    @cached_property
    def services(self) -> AsyncServicesResourceWithStreamingResponse:
        return AsyncServicesResourceWithStreamingResponse(self._addressing.services)

    @cached_property
    def address_maps(self) -> AsyncAddressMapsResourceWithStreamingResponse:
        return AsyncAddressMapsResourceWithStreamingResponse(self._addressing.address_maps)

    @cached_property
    def loa_documents(self) -> AsyncLOADocumentsResourceWithStreamingResponse:
        return AsyncLOADocumentsResourceWithStreamingResponse(self._addressing.loa_documents)

    @cached_property
    def prefixes(self) -> AsyncPrefixesResourceWithStreamingResponse:
        return AsyncPrefixesResourceWithStreamingResponse(self._addressing.prefixes)
