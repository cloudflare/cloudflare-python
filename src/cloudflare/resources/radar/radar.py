# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .bgp import (
    BGPResource,
    AsyncBGPResource,
    BGPResourceWithRawResponse,
    AsyncBGPResourceWithRawResponse,
    BGPResourceWithStreamingResponse,
    AsyncBGPResourceWithStreamingResponse,
)
from .dns import (
    DNSResource,
    AsyncDNSResource,
    DNSResourceWithRawResponse,
    AsyncDNSResourceWithRawResponse,
    DNSResourceWithStreamingResponse,
    AsyncDNSResourceWithStreamingResponse,
)
from .http import (
    HTTPResource,
    AsyncHTTPResource,
    HTTPResourceWithRawResponse,
    AsyncHTTPResourceWithRawResponse,
    HTTPResourceWithStreamingResponse,
    AsyncHTTPResourceWithStreamingResponse,
)
from .as112 import (
    AS112Resource,
    AsyncAS112Resource,
    AS112ResourceWithRawResponse,
    AsyncAS112ResourceWithRawResponse,
    AS112ResourceWithStreamingResponse,
    AsyncAS112ResourceWithStreamingResponse,
)
from .email import (
    EmailResource,
    AsyncEmailResource,
    EmailResourceWithRawResponse,
    AsyncEmailResourceWithRawResponse,
    EmailResourceWithStreamingResponse,
    AsyncEmailResourceWithStreamingResponse,
)
from .search import (
    SearchResource,
    AsyncSearchResource,
    SearchResourceWithRawResponse,
    AsyncSearchResourceWithRawResponse,
    SearchResourceWithStreamingResponse,
    AsyncSearchResourceWithStreamingResponse,
)
from .attacks import (
    AttacksResource,
    AsyncAttacksResource,
    AttacksResourceWithRawResponse,
    AsyncAttacksResourceWithRawResponse,
    AttacksResourceWithStreamingResponse,
    AsyncAttacksResourceWithStreamingResponse,
)
from .bgp.bgp import BGPResource, AsyncBGPResource
from .dns.dns import DNSResource, AsyncDNSResource
from .quality import (
    QualityResource,
    AsyncQualityResource,
    QualityResourceWithRawResponse,
    AsyncQualityResourceWithRawResponse,
    QualityResourceWithStreamingResponse,
    AsyncQualityResourceWithStreamingResponse,
)
from .ranking import (
    RankingResource,
    AsyncRankingResource,
    RankingResourceWithRawResponse,
    AsyncRankingResourceWithRawResponse,
    RankingResourceWithStreamingResponse,
    AsyncRankingResourceWithStreamingResponse,
)
from .datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
)
from .entities import (
    EntitiesResource,
    AsyncEntitiesResource,
    EntitiesResourceWithRawResponse,
    AsyncEntitiesResourceWithRawResponse,
    EntitiesResourceWithStreamingResponse,
    AsyncEntitiesResourceWithStreamingResponse,
)
from .netflows import (
    NetflowsResource,
    AsyncNetflowsResource,
    NetflowsResourceWithRawResponse,
    AsyncNetflowsResourceWithRawResponse,
    NetflowsResourceWithStreamingResponse,
    AsyncNetflowsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .http.http import HTTPResource, AsyncHTTPResource
from ..._resource import SyncAPIResource, AsyncAPIResource
from .annotations import (
    AnnotationsResource,
    AsyncAnnotationsResource,
    AnnotationsResourceWithRawResponse,
    AsyncAnnotationsResourceWithRawResponse,
    AnnotationsResourceWithStreamingResponse,
    AsyncAnnotationsResourceWithStreamingResponse,
)
from .as112.as112 import AS112Resource, AsyncAS112Resource
from .email.email import EmailResource, AsyncEmailResource
from .verified_bots import (
    VerifiedBotsResource,
    AsyncVerifiedBotsResource,
    VerifiedBotsResourceWithRawResponse,
    AsyncVerifiedBotsResourceWithRawResponse,
    VerifiedBotsResourceWithStreamingResponse,
    AsyncVerifiedBotsResourceWithStreamingResponse,
)
from .attacks.attacks import AttacksResource, AsyncAttacksResource
from .quality.quality import QualityResource, AsyncQualityResource
from .ranking.ranking import RankingResource, AsyncRankingResource
from .entities.entities import EntitiesResource, AsyncEntitiesResource
from .netflows.netflows import NetflowsResource, AsyncNetflowsResource
from .traffic_anomalies import (
    TrafficAnomaliesResource,
    AsyncTrafficAnomaliesResource,
    TrafficAnomaliesResourceWithRawResponse,
    AsyncTrafficAnomaliesResourceWithRawResponse,
    TrafficAnomaliesResourceWithStreamingResponse,
    AsyncTrafficAnomaliesResourceWithStreamingResponse,
)
from .connection_tampering import (
    ConnectionTamperingResource,
    AsyncConnectionTamperingResource,
    ConnectionTamperingResourceWithRawResponse,
    AsyncConnectionTamperingResourceWithRawResponse,
    ConnectionTamperingResourceWithStreamingResponse,
    AsyncConnectionTamperingResourceWithStreamingResponse,
)
from .annotations.annotations import AnnotationsResource, AsyncAnnotationsResource
from .verified_bots.verified_bots import VerifiedBotsResource, AsyncVerifiedBotsResource
from .traffic_anomalies.traffic_anomalies import TrafficAnomaliesResource, AsyncTrafficAnomaliesResource

__all__ = ["RadarResource", "AsyncRadarResource"]


class RadarResource(SyncAPIResource):
    @cached_property
    def annotations(self) -> AnnotationsResource:
        return AnnotationsResource(self._client)

    @cached_property
    def bgp(self) -> BGPResource:
        return BGPResource(self._client)

    @cached_property
    def datasets(self) -> DatasetsResource:
        return DatasetsResource(self._client)

    @cached_property
    def dns(self) -> DNSResource:
        return DNSResource(self._client)

    @cached_property
    def netflows(self) -> NetflowsResource:
        return NetflowsResource(self._client)

    @cached_property
    def search(self) -> SearchResource:
        return SearchResource(self._client)

    @cached_property
    def verified_bots(self) -> VerifiedBotsResource:
        return VerifiedBotsResource(self._client)

    @cached_property
    def as112(self) -> AS112Resource:
        return AS112Resource(self._client)

    @cached_property
    def connection_tampering(self) -> ConnectionTamperingResource:
        return ConnectionTamperingResource(self._client)

    @cached_property
    def email(self) -> EmailResource:
        return EmailResource(self._client)

    @cached_property
    def attacks(self) -> AttacksResource:
        return AttacksResource(self._client)

    @cached_property
    def entities(self) -> EntitiesResource:
        return EntitiesResource(self._client)

    @cached_property
    def http(self) -> HTTPResource:
        return HTTPResource(self._client)

    @cached_property
    def quality(self) -> QualityResource:
        return QualityResource(self._client)

    @cached_property
    def ranking(self) -> RankingResource:
        return RankingResource(self._client)

    @cached_property
    def traffic_anomalies(self) -> TrafficAnomaliesResource:
        return TrafficAnomaliesResource(self._client)

    @cached_property
    def with_raw_response(self) -> RadarResourceWithRawResponse:
        return RadarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RadarResourceWithStreamingResponse:
        return RadarResourceWithStreamingResponse(self)


class AsyncRadarResource(AsyncAPIResource):
    @cached_property
    def annotations(self) -> AsyncAnnotationsResource:
        return AsyncAnnotationsResource(self._client)

    @cached_property
    def bgp(self) -> AsyncBGPResource:
        return AsyncBGPResource(self._client)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        return AsyncDatasetsResource(self._client)

    @cached_property
    def dns(self) -> AsyncDNSResource:
        return AsyncDNSResource(self._client)

    @cached_property
    def netflows(self) -> AsyncNetflowsResource:
        return AsyncNetflowsResource(self._client)

    @cached_property
    def search(self) -> AsyncSearchResource:
        return AsyncSearchResource(self._client)

    @cached_property
    def verified_bots(self) -> AsyncVerifiedBotsResource:
        return AsyncVerifiedBotsResource(self._client)

    @cached_property
    def as112(self) -> AsyncAS112Resource:
        return AsyncAS112Resource(self._client)

    @cached_property
    def connection_tampering(self) -> AsyncConnectionTamperingResource:
        return AsyncConnectionTamperingResource(self._client)

    @cached_property
    def email(self) -> AsyncEmailResource:
        return AsyncEmailResource(self._client)

    @cached_property
    def attacks(self) -> AsyncAttacksResource:
        return AsyncAttacksResource(self._client)

    @cached_property
    def entities(self) -> AsyncEntitiesResource:
        return AsyncEntitiesResource(self._client)

    @cached_property
    def http(self) -> AsyncHTTPResource:
        return AsyncHTTPResource(self._client)

    @cached_property
    def quality(self) -> AsyncQualityResource:
        return AsyncQualityResource(self._client)

    @cached_property
    def ranking(self) -> AsyncRankingResource:
        return AsyncRankingResource(self._client)

    @cached_property
    def traffic_anomalies(self) -> AsyncTrafficAnomaliesResource:
        return AsyncTrafficAnomaliesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRadarResourceWithRawResponse:
        return AsyncRadarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRadarResourceWithStreamingResponse:
        return AsyncRadarResourceWithStreamingResponse(self)


class RadarResourceWithRawResponse:
    def __init__(self, radar: RadarResource) -> None:
        self._radar = radar

    @cached_property
    def annotations(self) -> AnnotationsResourceWithRawResponse:
        return AnnotationsResourceWithRawResponse(self._radar.annotations)

    @cached_property
    def bgp(self) -> BGPResourceWithRawResponse:
        return BGPResourceWithRawResponse(self._radar.bgp)

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self._radar.datasets)

    @cached_property
    def dns(self) -> DNSResourceWithRawResponse:
        return DNSResourceWithRawResponse(self._radar.dns)

    @cached_property
    def netflows(self) -> NetflowsResourceWithRawResponse:
        return NetflowsResourceWithRawResponse(self._radar.netflows)

    @cached_property
    def search(self) -> SearchResourceWithRawResponse:
        return SearchResourceWithRawResponse(self._radar.search)

    @cached_property
    def verified_bots(self) -> VerifiedBotsResourceWithRawResponse:
        return VerifiedBotsResourceWithRawResponse(self._radar.verified_bots)

    @cached_property
    def as112(self) -> AS112ResourceWithRawResponse:
        return AS112ResourceWithRawResponse(self._radar.as112)

    @cached_property
    def connection_tampering(self) -> ConnectionTamperingResourceWithRawResponse:
        return ConnectionTamperingResourceWithRawResponse(self._radar.connection_tampering)

    @cached_property
    def email(self) -> EmailResourceWithRawResponse:
        return EmailResourceWithRawResponse(self._radar.email)

    @cached_property
    def attacks(self) -> AttacksResourceWithRawResponse:
        return AttacksResourceWithRawResponse(self._radar.attacks)

    @cached_property
    def entities(self) -> EntitiesResourceWithRawResponse:
        return EntitiesResourceWithRawResponse(self._radar.entities)

    @cached_property
    def http(self) -> HTTPResourceWithRawResponse:
        return HTTPResourceWithRawResponse(self._radar.http)

    @cached_property
    def quality(self) -> QualityResourceWithRawResponse:
        return QualityResourceWithRawResponse(self._radar.quality)

    @cached_property
    def ranking(self) -> RankingResourceWithRawResponse:
        return RankingResourceWithRawResponse(self._radar.ranking)

    @cached_property
    def traffic_anomalies(self) -> TrafficAnomaliesResourceWithRawResponse:
        return TrafficAnomaliesResourceWithRawResponse(self._radar.traffic_anomalies)


class AsyncRadarResourceWithRawResponse:
    def __init__(self, radar: AsyncRadarResource) -> None:
        self._radar = radar

    @cached_property
    def annotations(self) -> AsyncAnnotationsResourceWithRawResponse:
        return AsyncAnnotationsResourceWithRawResponse(self._radar.annotations)

    @cached_property
    def bgp(self) -> AsyncBGPResourceWithRawResponse:
        return AsyncBGPResourceWithRawResponse(self._radar.bgp)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self._radar.datasets)

    @cached_property
    def dns(self) -> AsyncDNSResourceWithRawResponse:
        return AsyncDNSResourceWithRawResponse(self._radar.dns)

    @cached_property
    def netflows(self) -> AsyncNetflowsResourceWithRawResponse:
        return AsyncNetflowsResourceWithRawResponse(self._radar.netflows)

    @cached_property
    def search(self) -> AsyncSearchResourceWithRawResponse:
        return AsyncSearchResourceWithRawResponse(self._radar.search)

    @cached_property
    def verified_bots(self) -> AsyncVerifiedBotsResourceWithRawResponse:
        return AsyncVerifiedBotsResourceWithRawResponse(self._radar.verified_bots)

    @cached_property
    def as112(self) -> AsyncAS112ResourceWithRawResponse:
        return AsyncAS112ResourceWithRawResponse(self._radar.as112)

    @cached_property
    def connection_tampering(self) -> AsyncConnectionTamperingResourceWithRawResponse:
        return AsyncConnectionTamperingResourceWithRawResponse(self._radar.connection_tampering)

    @cached_property
    def email(self) -> AsyncEmailResourceWithRawResponse:
        return AsyncEmailResourceWithRawResponse(self._radar.email)

    @cached_property
    def attacks(self) -> AsyncAttacksResourceWithRawResponse:
        return AsyncAttacksResourceWithRawResponse(self._radar.attacks)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithRawResponse:
        return AsyncEntitiesResourceWithRawResponse(self._radar.entities)

    @cached_property
    def http(self) -> AsyncHTTPResourceWithRawResponse:
        return AsyncHTTPResourceWithRawResponse(self._radar.http)

    @cached_property
    def quality(self) -> AsyncQualityResourceWithRawResponse:
        return AsyncQualityResourceWithRawResponse(self._radar.quality)

    @cached_property
    def ranking(self) -> AsyncRankingResourceWithRawResponse:
        return AsyncRankingResourceWithRawResponse(self._radar.ranking)

    @cached_property
    def traffic_anomalies(self) -> AsyncTrafficAnomaliesResourceWithRawResponse:
        return AsyncTrafficAnomaliesResourceWithRawResponse(self._radar.traffic_anomalies)


class RadarResourceWithStreamingResponse:
    def __init__(self, radar: RadarResource) -> None:
        self._radar = radar

    @cached_property
    def annotations(self) -> AnnotationsResourceWithStreamingResponse:
        return AnnotationsResourceWithStreamingResponse(self._radar.annotations)

    @cached_property
    def bgp(self) -> BGPResourceWithStreamingResponse:
        return BGPResourceWithStreamingResponse(self._radar.bgp)

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self._radar.datasets)

    @cached_property
    def dns(self) -> DNSResourceWithStreamingResponse:
        return DNSResourceWithStreamingResponse(self._radar.dns)

    @cached_property
    def netflows(self) -> NetflowsResourceWithStreamingResponse:
        return NetflowsResourceWithStreamingResponse(self._radar.netflows)

    @cached_property
    def search(self) -> SearchResourceWithStreamingResponse:
        return SearchResourceWithStreamingResponse(self._radar.search)

    @cached_property
    def verified_bots(self) -> VerifiedBotsResourceWithStreamingResponse:
        return VerifiedBotsResourceWithStreamingResponse(self._radar.verified_bots)

    @cached_property
    def as112(self) -> AS112ResourceWithStreamingResponse:
        return AS112ResourceWithStreamingResponse(self._radar.as112)

    @cached_property
    def connection_tampering(self) -> ConnectionTamperingResourceWithStreamingResponse:
        return ConnectionTamperingResourceWithStreamingResponse(self._radar.connection_tampering)

    @cached_property
    def email(self) -> EmailResourceWithStreamingResponse:
        return EmailResourceWithStreamingResponse(self._radar.email)

    @cached_property
    def attacks(self) -> AttacksResourceWithStreamingResponse:
        return AttacksResourceWithStreamingResponse(self._radar.attacks)

    @cached_property
    def entities(self) -> EntitiesResourceWithStreamingResponse:
        return EntitiesResourceWithStreamingResponse(self._radar.entities)

    @cached_property
    def http(self) -> HTTPResourceWithStreamingResponse:
        return HTTPResourceWithStreamingResponse(self._radar.http)

    @cached_property
    def quality(self) -> QualityResourceWithStreamingResponse:
        return QualityResourceWithStreamingResponse(self._radar.quality)

    @cached_property
    def ranking(self) -> RankingResourceWithStreamingResponse:
        return RankingResourceWithStreamingResponse(self._radar.ranking)

    @cached_property
    def traffic_anomalies(self) -> TrafficAnomaliesResourceWithStreamingResponse:
        return TrafficAnomaliesResourceWithStreamingResponse(self._radar.traffic_anomalies)


class AsyncRadarResourceWithStreamingResponse:
    def __init__(self, radar: AsyncRadarResource) -> None:
        self._radar = radar

    @cached_property
    def annotations(self) -> AsyncAnnotationsResourceWithStreamingResponse:
        return AsyncAnnotationsResourceWithStreamingResponse(self._radar.annotations)

    @cached_property
    def bgp(self) -> AsyncBGPResourceWithStreamingResponse:
        return AsyncBGPResourceWithStreamingResponse(self._radar.bgp)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self._radar.datasets)

    @cached_property
    def dns(self) -> AsyncDNSResourceWithStreamingResponse:
        return AsyncDNSResourceWithStreamingResponse(self._radar.dns)

    @cached_property
    def netflows(self) -> AsyncNetflowsResourceWithStreamingResponse:
        return AsyncNetflowsResourceWithStreamingResponse(self._radar.netflows)

    @cached_property
    def search(self) -> AsyncSearchResourceWithStreamingResponse:
        return AsyncSearchResourceWithStreamingResponse(self._radar.search)

    @cached_property
    def verified_bots(self) -> AsyncVerifiedBotsResourceWithStreamingResponse:
        return AsyncVerifiedBotsResourceWithStreamingResponse(self._radar.verified_bots)

    @cached_property
    def as112(self) -> AsyncAS112ResourceWithStreamingResponse:
        return AsyncAS112ResourceWithStreamingResponse(self._radar.as112)

    @cached_property
    def connection_tampering(self) -> AsyncConnectionTamperingResourceWithStreamingResponse:
        return AsyncConnectionTamperingResourceWithStreamingResponse(self._radar.connection_tampering)

    @cached_property
    def email(self) -> AsyncEmailResourceWithStreamingResponse:
        return AsyncEmailResourceWithStreamingResponse(self._radar.email)

    @cached_property
    def attacks(self) -> AsyncAttacksResourceWithStreamingResponse:
        return AsyncAttacksResourceWithStreamingResponse(self._radar.attacks)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithStreamingResponse:
        return AsyncEntitiesResourceWithStreamingResponse(self._radar.entities)

    @cached_property
    def http(self) -> AsyncHTTPResourceWithStreamingResponse:
        return AsyncHTTPResourceWithStreamingResponse(self._radar.http)

    @cached_property
    def quality(self) -> AsyncQualityResourceWithStreamingResponse:
        return AsyncQualityResourceWithStreamingResponse(self._radar.quality)

    @cached_property
    def ranking(self) -> AsyncRankingResourceWithStreamingResponse:
        return AsyncRankingResourceWithStreamingResponse(self._radar.ranking)

    @cached_property
    def traffic_anomalies(self) -> AsyncTrafficAnomaliesResourceWithStreamingResponse:
        return AsyncTrafficAnomaliesResourceWithStreamingResponse(self._radar.traffic_anomalies)
