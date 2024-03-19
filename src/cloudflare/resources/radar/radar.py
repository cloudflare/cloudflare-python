# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .bgp import (
    BGP,
    AsyncBGP,
    BGPWithRawResponse,
    AsyncBGPWithRawResponse,
    BGPWithStreamingResponse,
    AsyncBGPWithStreamingResponse,
)
from .dns import (
    DNS,
    AsyncDNS,
    DNSWithRawResponse,
    AsyncDNSWithRawResponse,
    DNSWithStreamingResponse,
    AsyncDNSWithStreamingResponse,
)
from .http import (
    HTTP,
    AsyncHTTP,
    HTTPWithRawResponse,
    AsyncHTTPWithRawResponse,
    HTTPWithStreamingResponse,
    AsyncHTTPWithStreamingResponse,
)
from .as112 import (
    AS112,
    AsyncAS112,
    AS112WithRawResponse,
    AsyncAS112WithRawResponse,
    AS112WithStreamingResponse,
    AsyncAS112WithStreamingResponse,
)
from .email import (
    Email,
    AsyncEmail,
    EmailWithRawResponse,
    AsyncEmailWithRawResponse,
    EmailWithStreamingResponse,
    AsyncEmailWithStreamingResponse,
)
from .search import (
    Search,
    AsyncSearch,
    SearchWithRawResponse,
    AsyncSearchWithRawResponse,
    SearchWithStreamingResponse,
    AsyncSearchWithStreamingResponse,
)
from .attacks import (
    Attacks,
    AsyncAttacks,
    AttacksWithRawResponse,
    AsyncAttacksWithRawResponse,
    AttacksWithStreamingResponse,
    AsyncAttacksWithStreamingResponse,
)
from .bgp.bgp import BGP, AsyncBGP
from .dns.dns import DNS, AsyncDNS
from .quality import (
    Quality,
    AsyncQuality,
    QualityWithRawResponse,
    AsyncQualityWithRawResponse,
    QualityWithStreamingResponse,
    AsyncQualityWithStreamingResponse,
)
from .ranking import (
    Ranking,
    AsyncRanking,
    RankingWithRawResponse,
    AsyncRankingWithRawResponse,
    RankingWithStreamingResponse,
    AsyncRankingWithStreamingResponse,
)
from .datasets import (
    Datasets,
    AsyncDatasets,
    DatasetsWithRawResponse,
    AsyncDatasetsWithRawResponse,
    DatasetsWithStreamingResponse,
    AsyncDatasetsWithStreamingResponse,
)
from .entities import (
    Entities,
    AsyncEntities,
    EntitiesWithRawResponse,
    AsyncEntitiesWithRawResponse,
    EntitiesWithStreamingResponse,
    AsyncEntitiesWithStreamingResponse,
)
from .netflows import (
    Netflows,
    AsyncNetflows,
    NetflowsWithRawResponse,
    AsyncNetflowsWithRawResponse,
    NetflowsWithStreamingResponse,
    AsyncNetflowsWithStreamingResponse,
)
from ..._compat import cached_property
from .http.http import HTTP, AsyncHTTP
from ..._resource import SyncAPIResource, AsyncAPIResource
from .annotations import (
    Annotations,
    AsyncAnnotations,
    AnnotationsWithRawResponse,
    AsyncAnnotationsWithRawResponse,
    AnnotationsWithStreamingResponse,
    AsyncAnnotationsWithStreamingResponse,
)
from .as112.as112 import AS112, AsyncAS112
from .email.email import Email, AsyncEmail
from .verified_bots import (
    VerifiedBots,
    AsyncVerifiedBots,
    VerifiedBotsWithRawResponse,
    AsyncVerifiedBotsWithRawResponse,
    VerifiedBotsWithStreamingResponse,
    AsyncVerifiedBotsWithStreamingResponse,
)
from .attacks.attacks import Attacks, AsyncAttacks
from .quality.quality import Quality, AsyncQuality
from .ranking.ranking import Ranking, AsyncRanking
from .entities.entities import Entities, AsyncEntities
from .netflows.netflows import Netflows, AsyncNetflows
from .traffic_anomalies import (
    TrafficAnomalies,
    AsyncTrafficAnomalies,
    TrafficAnomaliesWithRawResponse,
    AsyncTrafficAnomaliesWithRawResponse,
    TrafficAnomaliesWithStreamingResponse,
    AsyncTrafficAnomaliesWithStreamingResponse,
)
from .connection_tampering import (
    ConnectionTampering,
    AsyncConnectionTampering,
    ConnectionTamperingWithRawResponse,
    AsyncConnectionTamperingWithRawResponse,
    ConnectionTamperingWithStreamingResponse,
    AsyncConnectionTamperingWithStreamingResponse,
)
from .annotations.annotations import Annotations, AsyncAnnotations
from .verified_bots.verified_bots import VerifiedBots, AsyncVerifiedBots
from .traffic_anomalies.traffic_anomalies import TrafficAnomalies, AsyncTrafficAnomalies

__all__ = ["Radar", "AsyncRadar"]


class Radar(SyncAPIResource):
    @cached_property
    def annotations(self) -> Annotations:
        return Annotations(self._client)

    @cached_property
    def bgp(self) -> BGP:
        return BGP(self._client)

    @cached_property
    def datasets(self) -> Datasets:
        return Datasets(self._client)

    @cached_property
    def dns(self) -> DNS:
        return DNS(self._client)

    @cached_property
    def netflows(self) -> Netflows:
        return Netflows(self._client)

    @cached_property
    def search(self) -> Search:
        return Search(self._client)

    @cached_property
    def verified_bots(self) -> VerifiedBots:
        return VerifiedBots(self._client)

    @cached_property
    def as112(self) -> AS112:
        return AS112(self._client)

    @cached_property
    def connection_tampering(self) -> ConnectionTampering:
        return ConnectionTampering(self._client)

    @cached_property
    def email(self) -> Email:
        return Email(self._client)

    @cached_property
    def attacks(self) -> Attacks:
        return Attacks(self._client)

    @cached_property
    def entities(self) -> Entities:
        return Entities(self._client)

    @cached_property
    def http(self) -> HTTP:
        return HTTP(self._client)

    @cached_property
    def quality(self) -> Quality:
        return Quality(self._client)

    @cached_property
    def ranking(self) -> Ranking:
        return Ranking(self._client)

    @cached_property
    def traffic_anomalies(self) -> TrafficAnomalies:
        return TrafficAnomalies(self._client)

    @cached_property
    def with_raw_response(self) -> RadarWithRawResponse:
        return RadarWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RadarWithStreamingResponse:
        return RadarWithStreamingResponse(self)


class AsyncRadar(AsyncAPIResource):
    @cached_property
    def annotations(self) -> AsyncAnnotations:
        return AsyncAnnotations(self._client)

    @cached_property
    def bgp(self) -> AsyncBGP:
        return AsyncBGP(self._client)

    @cached_property
    def datasets(self) -> AsyncDatasets:
        return AsyncDatasets(self._client)

    @cached_property
    def dns(self) -> AsyncDNS:
        return AsyncDNS(self._client)

    @cached_property
    def netflows(self) -> AsyncNetflows:
        return AsyncNetflows(self._client)

    @cached_property
    def search(self) -> AsyncSearch:
        return AsyncSearch(self._client)

    @cached_property
    def verified_bots(self) -> AsyncVerifiedBots:
        return AsyncVerifiedBots(self._client)

    @cached_property
    def as112(self) -> AsyncAS112:
        return AsyncAS112(self._client)

    @cached_property
    def connection_tampering(self) -> AsyncConnectionTampering:
        return AsyncConnectionTampering(self._client)

    @cached_property
    def email(self) -> AsyncEmail:
        return AsyncEmail(self._client)

    @cached_property
    def attacks(self) -> AsyncAttacks:
        return AsyncAttacks(self._client)

    @cached_property
    def entities(self) -> AsyncEntities:
        return AsyncEntities(self._client)

    @cached_property
    def http(self) -> AsyncHTTP:
        return AsyncHTTP(self._client)

    @cached_property
    def quality(self) -> AsyncQuality:
        return AsyncQuality(self._client)

    @cached_property
    def ranking(self) -> AsyncRanking:
        return AsyncRanking(self._client)

    @cached_property
    def traffic_anomalies(self) -> AsyncTrafficAnomalies:
        return AsyncTrafficAnomalies(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRadarWithRawResponse:
        return AsyncRadarWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRadarWithStreamingResponse:
        return AsyncRadarWithStreamingResponse(self)


class RadarWithRawResponse:
    def __init__(self, radar: Radar) -> None:
        self._radar = radar

    @cached_property
    def annotations(self) -> AnnotationsWithRawResponse:
        return AnnotationsWithRawResponse(self._radar.annotations)

    @cached_property
    def bgp(self) -> BGPWithRawResponse:
        return BGPWithRawResponse(self._radar.bgp)

    @cached_property
    def datasets(self) -> DatasetsWithRawResponse:
        return DatasetsWithRawResponse(self._radar.datasets)

    @cached_property
    def dns(self) -> DNSWithRawResponse:
        return DNSWithRawResponse(self._radar.dns)

    @cached_property
    def netflows(self) -> NetflowsWithRawResponse:
        return NetflowsWithRawResponse(self._radar.netflows)

    @cached_property
    def search(self) -> SearchWithRawResponse:
        return SearchWithRawResponse(self._radar.search)

    @cached_property
    def verified_bots(self) -> VerifiedBotsWithRawResponse:
        return VerifiedBotsWithRawResponse(self._radar.verified_bots)

    @cached_property
    def as112(self) -> AS112WithRawResponse:
        return AS112WithRawResponse(self._radar.as112)

    @cached_property
    def connection_tampering(self) -> ConnectionTamperingWithRawResponse:
        return ConnectionTamperingWithRawResponse(self._radar.connection_tampering)

    @cached_property
    def email(self) -> EmailWithRawResponse:
        return EmailWithRawResponse(self._radar.email)

    @cached_property
    def attacks(self) -> AttacksWithRawResponse:
        return AttacksWithRawResponse(self._radar.attacks)

    @cached_property
    def entities(self) -> EntitiesWithRawResponse:
        return EntitiesWithRawResponse(self._radar.entities)

    @cached_property
    def http(self) -> HTTPWithRawResponse:
        return HTTPWithRawResponse(self._radar.http)

    @cached_property
    def quality(self) -> QualityWithRawResponse:
        return QualityWithRawResponse(self._radar.quality)

    @cached_property
    def ranking(self) -> RankingWithRawResponse:
        return RankingWithRawResponse(self._radar.ranking)

    @cached_property
    def traffic_anomalies(self) -> TrafficAnomaliesWithRawResponse:
        return TrafficAnomaliesWithRawResponse(self._radar.traffic_anomalies)


class AsyncRadarWithRawResponse:
    def __init__(self, radar: AsyncRadar) -> None:
        self._radar = radar

    @cached_property
    def annotations(self) -> AsyncAnnotationsWithRawResponse:
        return AsyncAnnotationsWithRawResponse(self._radar.annotations)

    @cached_property
    def bgp(self) -> AsyncBGPWithRawResponse:
        return AsyncBGPWithRawResponse(self._radar.bgp)

    @cached_property
    def datasets(self) -> AsyncDatasetsWithRawResponse:
        return AsyncDatasetsWithRawResponse(self._radar.datasets)

    @cached_property
    def dns(self) -> AsyncDNSWithRawResponse:
        return AsyncDNSWithRawResponse(self._radar.dns)

    @cached_property
    def netflows(self) -> AsyncNetflowsWithRawResponse:
        return AsyncNetflowsWithRawResponse(self._radar.netflows)

    @cached_property
    def search(self) -> AsyncSearchWithRawResponse:
        return AsyncSearchWithRawResponse(self._radar.search)

    @cached_property
    def verified_bots(self) -> AsyncVerifiedBotsWithRawResponse:
        return AsyncVerifiedBotsWithRawResponse(self._radar.verified_bots)

    @cached_property
    def as112(self) -> AsyncAS112WithRawResponse:
        return AsyncAS112WithRawResponse(self._radar.as112)

    @cached_property
    def connection_tampering(self) -> AsyncConnectionTamperingWithRawResponse:
        return AsyncConnectionTamperingWithRawResponse(self._radar.connection_tampering)

    @cached_property
    def email(self) -> AsyncEmailWithRawResponse:
        return AsyncEmailWithRawResponse(self._radar.email)

    @cached_property
    def attacks(self) -> AsyncAttacksWithRawResponse:
        return AsyncAttacksWithRawResponse(self._radar.attacks)

    @cached_property
    def entities(self) -> AsyncEntitiesWithRawResponse:
        return AsyncEntitiesWithRawResponse(self._radar.entities)

    @cached_property
    def http(self) -> AsyncHTTPWithRawResponse:
        return AsyncHTTPWithRawResponse(self._radar.http)

    @cached_property
    def quality(self) -> AsyncQualityWithRawResponse:
        return AsyncQualityWithRawResponse(self._radar.quality)

    @cached_property
    def ranking(self) -> AsyncRankingWithRawResponse:
        return AsyncRankingWithRawResponse(self._radar.ranking)

    @cached_property
    def traffic_anomalies(self) -> AsyncTrafficAnomaliesWithRawResponse:
        return AsyncTrafficAnomaliesWithRawResponse(self._radar.traffic_anomalies)


class RadarWithStreamingResponse:
    def __init__(self, radar: Radar) -> None:
        self._radar = radar

    @cached_property
    def annotations(self) -> AnnotationsWithStreamingResponse:
        return AnnotationsWithStreamingResponse(self._radar.annotations)

    @cached_property
    def bgp(self) -> BGPWithStreamingResponse:
        return BGPWithStreamingResponse(self._radar.bgp)

    @cached_property
    def datasets(self) -> DatasetsWithStreamingResponse:
        return DatasetsWithStreamingResponse(self._radar.datasets)

    @cached_property
    def dns(self) -> DNSWithStreamingResponse:
        return DNSWithStreamingResponse(self._radar.dns)

    @cached_property
    def netflows(self) -> NetflowsWithStreamingResponse:
        return NetflowsWithStreamingResponse(self._radar.netflows)

    @cached_property
    def search(self) -> SearchWithStreamingResponse:
        return SearchWithStreamingResponse(self._radar.search)

    @cached_property
    def verified_bots(self) -> VerifiedBotsWithStreamingResponse:
        return VerifiedBotsWithStreamingResponse(self._radar.verified_bots)

    @cached_property
    def as112(self) -> AS112WithStreamingResponse:
        return AS112WithStreamingResponse(self._radar.as112)

    @cached_property
    def connection_tampering(self) -> ConnectionTamperingWithStreamingResponse:
        return ConnectionTamperingWithStreamingResponse(self._radar.connection_tampering)

    @cached_property
    def email(self) -> EmailWithStreamingResponse:
        return EmailWithStreamingResponse(self._radar.email)

    @cached_property
    def attacks(self) -> AttacksWithStreamingResponse:
        return AttacksWithStreamingResponse(self._radar.attacks)

    @cached_property
    def entities(self) -> EntitiesWithStreamingResponse:
        return EntitiesWithStreamingResponse(self._radar.entities)

    @cached_property
    def http(self) -> HTTPWithStreamingResponse:
        return HTTPWithStreamingResponse(self._radar.http)

    @cached_property
    def quality(self) -> QualityWithStreamingResponse:
        return QualityWithStreamingResponse(self._radar.quality)

    @cached_property
    def ranking(self) -> RankingWithStreamingResponse:
        return RankingWithStreamingResponse(self._radar.ranking)

    @cached_property
    def traffic_anomalies(self) -> TrafficAnomaliesWithStreamingResponse:
        return TrafficAnomaliesWithStreamingResponse(self._radar.traffic_anomalies)


class AsyncRadarWithStreamingResponse:
    def __init__(self, radar: AsyncRadar) -> None:
        self._radar = radar

    @cached_property
    def annotations(self) -> AsyncAnnotationsWithStreamingResponse:
        return AsyncAnnotationsWithStreamingResponse(self._radar.annotations)

    @cached_property
    def bgp(self) -> AsyncBGPWithStreamingResponse:
        return AsyncBGPWithStreamingResponse(self._radar.bgp)

    @cached_property
    def datasets(self) -> AsyncDatasetsWithStreamingResponse:
        return AsyncDatasetsWithStreamingResponse(self._radar.datasets)

    @cached_property
    def dns(self) -> AsyncDNSWithStreamingResponse:
        return AsyncDNSWithStreamingResponse(self._radar.dns)

    @cached_property
    def netflows(self) -> AsyncNetflowsWithStreamingResponse:
        return AsyncNetflowsWithStreamingResponse(self._radar.netflows)

    @cached_property
    def search(self) -> AsyncSearchWithStreamingResponse:
        return AsyncSearchWithStreamingResponse(self._radar.search)

    @cached_property
    def verified_bots(self) -> AsyncVerifiedBotsWithStreamingResponse:
        return AsyncVerifiedBotsWithStreamingResponse(self._radar.verified_bots)

    @cached_property
    def as112(self) -> AsyncAS112WithStreamingResponse:
        return AsyncAS112WithStreamingResponse(self._radar.as112)

    @cached_property
    def connection_tampering(self) -> AsyncConnectionTamperingWithStreamingResponse:
        return AsyncConnectionTamperingWithStreamingResponse(self._radar.connection_tampering)

    @cached_property
    def email(self) -> AsyncEmailWithStreamingResponse:
        return AsyncEmailWithStreamingResponse(self._radar.email)

    @cached_property
    def attacks(self) -> AsyncAttacksWithStreamingResponse:
        return AsyncAttacksWithStreamingResponse(self._radar.attacks)

    @cached_property
    def entities(self) -> AsyncEntitiesWithStreamingResponse:
        return AsyncEntitiesWithStreamingResponse(self._radar.entities)

    @cached_property
    def http(self) -> AsyncHTTPWithStreamingResponse:
        return AsyncHTTPWithStreamingResponse(self._radar.http)

    @cached_property
    def quality(self) -> AsyncQualityWithStreamingResponse:
        return AsyncQualityWithStreamingResponse(self._radar.quality)

    @cached_property
    def ranking(self) -> AsyncRankingWithStreamingResponse:
        return AsyncRankingWithStreamingResponse(self._radar.ranking)

    @cached_property
    def traffic_anomalies(self) -> AsyncTrafficAnomaliesWithStreamingResponse:
        return AsyncTrafficAnomaliesWithStreamingResponse(self._radar.traffic_anomalies)
