# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ai.ai import (
    AIResource,
    AsyncAIResource,
    AIResourceWithRawResponse,
    AsyncAIResourceWithRawResponse,
    AIResourceWithStreamingResponse,
    AsyncAIResourceWithStreamingResponse,
)
from .search import (
    SearchResource,
    AsyncSearchResource,
    SearchResourceWithRawResponse,
    AsyncSearchResourceWithRawResponse,
    SearchResourceWithStreamingResponse,
    AsyncSearchResourceWithStreamingResponse,
)
from .bgp.bgp import (
    BGPResource,
    AsyncBGPResource,
    BGPResourceWithRawResponse,
    AsyncBGPResourceWithRawResponse,
    BGPResourceWithStreamingResponse,
    AsyncBGPResourceWithStreamingResponse,
)
from .dns.dns import (
    DNSResource,
    AsyncDNSResource,
    DNSResourceWithRawResponse,
    AsyncDNSResourceWithRawResponse,
    DNSResourceWithStreamingResponse,
    AsyncDNSResourceWithStreamingResponse,
)
from .datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .http.http import (
    HTTPResource,
    AsyncHTTPResource,
    HTTPResourceWithRawResponse,
    AsyncHTTPResourceWithRawResponse,
    HTTPResourceWithStreamingResponse,
    AsyncHTTPResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .as112.as112 import (
    AS112Resource,
    AsyncAS112Resource,
    AS112ResourceWithRawResponse,
    AsyncAS112ResourceWithRawResponse,
    AS112ResourceWithStreamingResponse,
    AsyncAS112ResourceWithStreamingResponse,
)
from .email.email import (
    EmailResource,
    AsyncEmailResource,
    EmailResourceWithRawResponse,
    AsyncEmailResourceWithRawResponse,
    EmailResourceWithStreamingResponse,
    AsyncEmailResourceWithStreamingResponse,
)
from .attacks.attacks import (
    AttacksResource,
    AsyncAttacksResource,
    AttacksResourceWithRawResponse,
    AsyncAttacksResourceWithRawResponse,
    AttacksResourceWithStreamingResponse,
    AsyncAttacksResourceWithStreamingResponse,
)
from .quality.quality import (
    QualityResource,
    AsyncQualityResource,
    QualityResourceWithRawResponse,
    AsyncQualityResourceWithRawResponse,
    QualityResourceWithStreamingResponse,
    AsyncQualityResourceWithStreamingResponse,
)
from .ranking.ranking import (
    RankingResource,
    AsyncRankingResource,
    RankingResourceWithRawResponse,
    AsyncRankingResourceWithRawResponse,
    RankingResourceWithStreamingResponse,
    AsyncRankingResourceWithStreamingResponse,
)
from .entities.entities import (
    EntitiesResource,
    AsyncEntitiesResource,
    EntitiesResourceWithRawResponse,
    AsyncEntitiesResourceWithRawResponse,
    EntitiesResourceWithStreamingResponse,
    AsyncEntitiesResourceWithStreamingResponse,
)
from .netflows.netflows import (
    NetflowsResource,
    AsyncNetflowsResource,
    NetflowsResourceWithRawResponse,
    AsyncNetflowsResourceWithRawResponse,
    NetflowsResourceWithStreamingResponse,
    AsyncNetflowsResourceWithStreamingResponse,
)
from .tcp_resets_timeouts import (
    TCPResetsTimeoutsResource,
    AsyncTCPResetsTimeoutsResource,
    TCPResetsTimeoutsResourceWithRawResponse,
    AsyncTCPResetsTimeoutsResourceWithRawResponse,
    TCPResetsTimeoutsResourceWithStreamingResponse,
    AsyncTCPResetsTimeoutsResourceWithStreamingResponse,
)
from .robots_txt.robots_txt import (
    RobotsTXTResource,
    AsyncRobotsTXTResource,
    RobotsTXTResourceWithRawResponse,
    AsyncRobotsTXTResourceWithRawResponse,
    RobotsTXTResourceWithStreamingResponse,
    AsyncRobotsTXTResourceWithStreamingResponse,
)
from .annotations.annotations import (
    AnnotationsResource,
    AsyncAnnotationsResource,
    AnnotationsResourceWithRawResponse,
    AsyncAnnotationsResourceWithRawResponse,
    AnnotationsResourceWithStreamingResponse,
    AsyncAnnotationsResourceWithStreamingResponse,
)
from .verified_bots.verified_bots import (
    VerifiedBotsResource,
    AsyncVerifiedBotsResource,
    VerifiedBotsResourceWithRawResponse,
    AsyncVerifiedBotsResourceWithRawResponse,
    VerifiedBotsResourceWithStreamingResponse,
    AsyncVerifiedBotsResourceWithStreamingResponse,
)
from .traffic_anomalies.traffic_anomalies import (
    TrafficAnomaliesResource,
    AsyncTrafficAnomaliesResource,
    TrafficAnomaliesResourceWithRawResponse,
    AsyncTrafficAnomaliesResourceWithRawResponse,
    TrafficAnomaliesResourceWithStreamingResponse,
    AsyncTrafficAnomaliesResourceWithStreamingResponse,
)
from .leaked_credentials.leaked_credentials import (
    LeakedCredentialsResource,
    AsyncLeakedCredentialsResource,
    LeakedCredentialsResourceWithRawResponse,
    AsyncLeakedCredentialsResourceWithRawResponse,
    LeakedCredentialsResourceWithStreamingResponse,
    AsyncLeakedCredentialsResourceWithStreamingResponse,
)

__all__ = ["RadarResource", "AsyncRadarResource"]


class RadarResource(SyncAPIResource):
    @cached_property
    def ai(self) -> AIResource:
        return AIResource(self._client)

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
    def tcp_resets_timeouts(self) -> TCPResetsTimeoutsResource:
        return TCPResetsTimeoutsResource(self._client)

    @cached_property
    def robots_txt(self) -> RobotsTXTResource:
        return RobotsTXTResource(self._client)

    @cached_property
    def leaked_credentials(self) -> LeakedCredentialsResource:
        return LeakedCredentialsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RadarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RadarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RadarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RadarResourceWithStreamingResponse(self)


class AsyncRadarResource(AsyncAPIResource):
    @cached_property
    def ai(self) -> AsyncAIResource:
        return AsyncAIResource(self._client)

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
    def tcp_resets_timeouts(self) -> AsyncTCPResetsTimeoutsResource:
        return AsyncTCPResetsTimeoutsResource(self._client)

    @cached_property
    def robots_txt(self) -> AsyncRobotsTXTResource:
        return AsyncRobotsTXTResource(self._client)

    @cached_property
    def leaked_credentials(self) -> AsyncLeakedCredentialsResource:
        return AsyncLeakedCredentialsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRadarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRadarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRadarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRadarResourceWithStreamingResponse(self)


class RadarResourceWithRawResponse:
    def __init__(self, radar: RadarResource) -> None:
        self._radar = radar

    @cached_property
    def ai(self) -> AIResourceWithRawResponse:
        return AIResourceWithRawResponse(self._radar.ai)

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

    @cached_property
    def tcp_resets_timeouts(self) -> TCPResetsTimeoutsResourceWithRawResponse:
        return TCPResetsTimeoutsResourceWithRawResponse(self._radar.tcp_resets_timeouts)

    @cached_property
    def robots_txt(self) -> RobotsTXTResourceWithRawResponse:
        return RobotsTXTResourceWithRawResponse(self._radar.robots_txt)

    @cached_property
    def leaked_credentials(self) -> LeakedCredentialsResourceWithRawResponse:
        return LeakedCredentialsResourceWithRawResponse(self._radar.leaked_credentials)


class AsyncRadarResourceWithRawResponse:
    def __init__(self, radar: AsyncRadarResource) -> None:
        self._radar = radar

    @cached_property
    def ai(self) -> AsyncAIResourceWithRawResponse:
        return AsyncAIResourceWithRawResponse(self._radar.ai)

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

    @cached_property
    def tcp_resets_timeouts(self) -> AsyncTCPResetsTimeoutsResourceWithRawResponse:
        return AsyncTCPResetsTimeoutsResourceWithRawResponse(self._radar.tcp_resets_timeouts)

    @cached_property
    def robots_txt(self) -> AsyncRobotsTXTResourceWithRawResponse:
        return AsyncRobotsTXTResourceWithRawResponse(self._radar.robots_txt)

    @cached_property
    def leaked_credentials(self) -> AsyncLeakedCredentialsResourceWithRawResponse:
        return AsyncLeakedCredentialsResourceWithRawResponse(self._radar.leaked_credentials)


class RadarResourceWithStreamingResponse:
    def __init__(self, radar: RadarResource) -> None:
        self._radar = radar

    @cached_property
    def ai(self) -> AIResourceWithStreamingResponse:
        return AIResourceWithStreamingResponse(self._radar.ai)

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

    @cached_property
    def tcp_resets_timeouts(self) -> TCPResetsTimeoutsResourceWithStreamingResponse:
        return TCPResetsTimeoutsResourceWithStreamingResponse(self._radar.tcp_resets_timeouts)

    @cached_property
    def robots_txt(self) -> RobotsTXTResourceWithStreamingResponse:
        return RobotsTXTResourceWithStreamingResponse(self._radar.robots_txt)

    @cached_property
    def leaked_credentials(self) -> LeakedCredentialsResourceWithStreamingResponse:
        return LeakedCredentialsResourceWithStreamingResponse(self._radar.leaked_credentials)


class AsyncRadarResourceWithStreamingResponse:
    def __init__(self, radar: AsyncRadarResource) -> None:
        self._radar = radar

    @cached_property
    def ai(self) -> AsyncAIResourceWithStreamingResponse:
        return AsyncAIResourceWithStreamingResponse(self._radar.ai)

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

    @cached_property
    def tcp_resets_timeouts(self) -> AsyncTCPResetsTimeoutsResourceWithStreamingResponse:
        return AsyncTCPResetsTimeoutsResourceWithStreamingResponse(self._radar.tcp_resets_timeouts)

    @cached_property
    def robots_txt(self) -> AsyncRobotsTXTResourceWithStreamingResponse:
        return AsyncRobotsTXTResourceWithStreamingResponse(self._radar.robots_txt)

    @cached_property
    def leaked_credentials(self) -> AsyncLeakedCredentialsResourceWithStreamingResponse:
        return AsyncLeakedCredentialsResourceWithStreamingResponse(self._radar.leaked_credentials)
