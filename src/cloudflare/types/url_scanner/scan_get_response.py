# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ScanGetResponse",
    "Data",
    "DataConsole",
    "DataConsoleMessage",
    "DataCookie",
    "DataGlobal",
    "DataLink",
    "DataPerformance",
    "DataRequest",
    "DataRequestRequest",
    "DataRequestRequestInitiator",
    "DataRequestRequestRequest",
    "DataRequestRequestRedirectResponse",
    "DataRequestRequestRedirectResponseSecurityHeader",
    "DataRequestResponse",
    "DataRequestResponseASN",
    "DataRequestResponseGeoip",
    "DataRequestResponseResponse",
    "DataRequestResponseResponseSecurityDetails",
    "DataRequestResponseResponseSecurityHeader",
    "Lists",
    "ListsCertificate",
    "Meta",
    "MetaProcessors",
    "MetaProcessorsASN",
    "MetaProcessorsASNData",
    "MetaProcessorsDNS",
    "MetaProcessorsDNSData",
    "MetaProcessorsDomainCategories",
    "MetaProcessorsDomainCategoriesData",
    "MetaProcessorsGeoip",
    "MetaProcessorsGeoipData",
    "MetaProcessorsGeoipDataGeoip",
    "MetaProcessorsPhishing",
    "MetaProcessorsRadarRank",
    "MetaProcessorsRadarRankData",
    "MetaProcessorsWappa",
    "MetaProcessorsWappaData",
    "MetaProcessorsWappaDataCategory",
    "MetaProcessorsWappaDataConfidence",
    "MetaProcessorsAgentReadiness",
    "MetaProcessorsAgentReadinessChecks",
    "MetaProcessorsAgentReadinessChecksBotAccessControl",
    "MetaProcessorsAgentReadinessChecksBotAccessControlContentSignals",
    "MetaProcessorsAgentReadinessChecksBotAccessControlContentSignalsEvidence",
    "MetaProcessorsAgentReadinessChecksBotAccessControlContentSignalsEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksBotAccessControlContentSignalsEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksBotAccessControlContentSignalsEvidenceResponse",
    "MetaProcessorsAgentReadinessChecksBotAccessControlRobotsTXTAIRules",
    "MetaProcessorsAgentReadinessChecksBotAccessControlRobotsTxtaiRulesEvidence",
    "MetaProcessorsAgentReadinessChecksBotAccessControlRobotsTxtaiRulesEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksBotAccessControlRobotsTxtaiRulesEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksBotAccessControlRobotsTxtaiRulesEvidenceResponse",
    "MetaProcessorsAgentReadinessChecksBotAccessControlWebBotAuth",
    "MetaProcessorsAgentReadinessChecksBotAccessControlWebBotAuthEvidence",
    "MetaProcessorsAgentReadinessChecksBotAccessControlWebBotAuthEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksBotAccessControlWebBotAuthEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksBotAccessControlWebBotAuthEvidenceResponse",
    "MetaProcessorsAgentReadinessChecksCommerce",
    "MetaProcessorsAgentReadinessChecksCommerceAcp",
    "MetaProcessorsAgentReadinessChecksCommerceAcpEvidence",
    "MetaProcessorsAgentReadinessChecksCommerceAcpEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksCommerceAcpEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksCommerceAcpEvidenceResponse",
    "MetaProcessorsAgentReadinessChecksCommerceAp2",
    "MetaProcessorsAgentReadinessChecksCommerceAp2Evidence",
    "MetaProcessorsAgentReadinessChecksCommerceAp2EvidenceFinding",
    "MetaProcessorsAgentReadinessChecksCommerceAp2EvidenceRequest",
    "MetaProcessorsAgentReadinessChecksCommerceAp2EvidenceResponse",
    "MetaProcessorsAgentReadinessChecksCommerceUcp",
    "MetaProcessorsAgentReadinessChecksCommerceUcpEvidence",
    "MetaProcessorsAgentReadinessChecksCommerceUcpEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksCommerceUcpEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksCommerceUcpEvidenceResponse",
    "MetaProcessorsAgentReadinessChecksCommerceX402",
    "MetaProcessorsAgentReadinessChecksCommerceX402Evidence",
    "MetaProcessorsAgentReadinessChecksCommerceX402EvidenceFinding",
    "MetaProcessorsAgentReadinessChecksCommerceX402EvidenceRequest",
    "MetaProcessorsAgentReadinessChecksCommerceX402EvidenceResponse",
    "MetaProcessorsAgentReadinessChecksContentAccessibility",
    "MetaProcessorsAgentReadinessChecksContentAccessibilityMarkdownNegotiation",
    "MetaProcessorsAgentReadinessChecksContentAccessibilityMarkdownNegotiationEvidence",
    "MetaProcessorsAgentReadinessChecksContentAccessibilityMarkdownNegotiationEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksContentAccessibilityMarkdownNegotiationEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksContentAccessibilityMarkdownNegotiationEvidenceResponse",
    "MetaProcessorsAgentReadinessChecksDiscoverability",
    "MetaProcessorsAgentReadinessChecksDiscoverabilityLinkHeaders",
    "MetaProcessorsAgentReadinessChecksDiscoverabilityLinkHeadersEvidence",
    "MetaProcessorsAgentReadinessChecksDiscoverabilityLinkHeadersEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksDiscoverabilityLinkHeadersEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksDiscoverabilityLinkHeadersEvidenceResponse",
    "MetaProcessorsAgentReadinessChecksDiscoverabilityRobotsTXT",
    "MetaProcessorsAgentReadinessChecksDiscoverabilityRobotsTXTEvidence",
    "MetaProcessorsAgentReadinessChecksDiscoverabilityRobotsTXTEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksDiscoverabilityRobotsTXTEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksDiscoverabilityRobotsTXTEvidenceResponse",
    "MetaProcessorsAgentReadinessChecksDiscoverabilitySitemap",
    "MetaProcessorsAgentReadinessChecksDiscoverabilitySitemapEvidence",
    "MetaProcessorsAgentReadinessChecksDiscoverabilitySitemapEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksDiscoverabilitySitemapEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksDiscoverabilitySitemapEvidenceResponse",
    "MetaProcessorsAgentReadinessChecksDiscovery",
    "MetaProcessorsAgentReadinessChecksDiscoveryA2aAgentCard",
    "MetaProcessorsAgentReadinessChecksDiscoveryA2aAgentCardEvidence",
    "MetaProcessorsAgentReadinessChecksDiscoveryA2aAgentCardEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksDiscoveryA2aAgentCardEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksDiscoveryA2aAgentCardEvidenceResponse",
    "MetaProcessorsAgentReadinessChecksDiscoveryAgentSkills",
    "MetaProcessorsAgentReadinessChecksDiscoveryAgentSkillsEvidence",
    "MetaProcessorsAgentReadinessChecksDiscoveryAgentSkillsEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksDiscoveryAgentSkillsEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksDiscoveryAgentSkillsEvidenceResponse",
    "MetaProcessorsAgentReadinessChecksDiscoveryAPICatalog",
    "MetaProcessorsAgentReadinessChecksDiscoveryAPICatalogEvidence",
    "MetaProcessorsAgentReadinessChecksDiscoveryAPICatalogEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksDiscoveryAPICatalogEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksDiscoveryAPICatalogEvidenceResponse",
    "MetaProcessorsAgentReadinessChecksDiscoveryMcpServerCard",
    "MetaProcessorsAgentReadinessChecksDiscoveryMcpServerCardEvidence",
    "MetaProcessorsAgentReadinessChecksDiscoveryMcpServerCardEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksDiscoveryMcpServerCardEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksDiscoveryMcpServerCardEvidenceResponse",
    "MetaProcessorsAgentReadinessChecksDiscoveryOAuthDiscovery",
    "MetaProcessorsAgentReadinessChecksDiscoveryOAuthDiscoveryEvidence",
    "MetaProcessorsAgentReadinessChecksDiscoveryOAuthDiscoveryEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksDiscoveryOAuthDiscoveryEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksDiscoveryOAuthDiscoveryEvidenceResponse",
    "MetaProcessorsAgentReadinessChecksDiscoveryOAuthProtectedResource",
    "MetaProcessorsAgentReadinessChecksDiscoveryOAuthProtectedResourceEvidence",
    "MetaProcessorsAgentReadinessChecksDiscoveryOAuthProtectedResourceEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksDiscoveryOAuthProtectedResourceEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksDiscoveryOAuthProtectedResourceEvidenceResponse",
    "MetaProcessorsAgentReadinessChecksDiscoveryWebMcp",
    "MetaProcessorsAgentReadinessChecksDiscoveryWebMcpEvidence",
    "MetaProcessorsAgentReadinessChecksDiscoveryWebMcpEvidenceFinding",
    "MetaProcessorsAgentReadinessChecksDiscoveryWebMcpEvidenceRequest",
    "MetaProcessorsAgentReadinessChecksDiscoveryWebMcpEvidenceResponse",
    "MetaProcessorsAgentReadinessNextLevel",
    "MetaProcessorsAgentReadinessNextLevelRequirement",
    "MetaProcessorsPhishingV2",
    "MetaProcessorsRobotsTXT",
    "MetaProcessorsRobotsTXTData",
    "MetaProcessorsRobotsTXTDataRules",
    "MetaProcessorsRobotsTXTDataRulesapi_empty",
    "MetaProcessorsRobotsTXTDataRulesapi_emptyContentSignal",
    "MetaProcessorsURLCategories",
    "MetaProcessorsURLCategoriesData",
    "MetaProcessorsURLCategoriesDataContent",
    "MetaProcessorsURLCategoriesDataInherited",
    "MetaProcessorsURLCategoriesDataInheritedContent",
    "MetaProcessorsURLCategoriesDataInheritedRisk",
    "MetaProcessorsURLCategoriesDataRisk",
    "Page",
    "PageScreenshot",
    "Scanner",
    "Stats",
    "StatsDomainStat",
    "StatsIPStat",
    "StatsIPStatASN",
    "StatsIPStatGeoip",
    "StatsProtocolStat",
    "StatsResourceStat",
    "StatsServerStat",
    "StatsTLSStat",
    "StatsTLSStatProtocols",
    "Task",
    "TaskOptions",
    "Verdicts",
    "VerdictsOverall",
]


class DataConsoleMessage(BaseModel):
    level: str

    source: str

    text: str

    url: str


class DataConsole(BaseModel):
    message: DataConsoleMessage


class DataCookie(BaseModel):
    domain: str

    expires: float

    http_only: bool = FieldInfo(alias="httpOnly")

    name: str

    path: str

    priority: str

    same_party: bool = FieldInfo(alias="sameParty")

    secure: bool

    session: bool

    size: float

    source_port: float = FieldInfo(alias="sourcePort")

    source_scheme: str = FieldInfo(alias="sourceScheme")

    value: str


class DataGlobal(BaseModel):
    prop: str

    type: str


class DataLink(BaseModel):
    href: str

    text: str


class DataPerformance(BaseModel):
    duration: float

    entry_type: str = FieldInfo(alias="entryType")

    name: str

    start_time: float = FieldInfo(alias="startTime")


class DataRequestRequestInitiator(BaseModel):
    host: str

    type: str

    url: str


class DataRequestRequestRequest(BaseModel):
    initial_priority: str = FieldInfo(alias="initialPriority")

    is_same_site: bool = FieldInfo(alias="isSameSite")

    method: str

    mixed_content_type: str = FieldInfo(alias="mixedContentType")

    referrer_policy: str = FieldInfo(alias="referrerPolicy")

    url: str

    headers: Optional[object] = None


class DataRequestRequestRedirectResponseSecurityHeader(BaseModel):
    name: str

    value: str


class DataRequestRequestRedirectResponse(BaseModel):
    charset: str

    mime_type: str = FieldInfo(alias="mimeType")

    protocol: str

    remote_ip_address: str = FieldInfo(alias="remoteIPAddress")

    remote_port: float = FieldInfo(alias="remotePort")

    security_headers: List[DataRequestRequestRedirectResponseSecurityHeader] = FieldInfo(alias="securityHeaders")

    security_state: str = FieldInfo(alias="securityState")

    status: float

    status_text: str = FieldInfo(alias="statusText")

    url: str

    headers: Optional[object] = None


class DataRequestRequest(BaseModel):
    document_url: str = FieldInfo(alias="documentURL")

    has_user_gesture: bool = FieldInfo(alias="hasUserGesture")

    initiator: DataRequestRequestInitiator

    redirect_has_extra_info: bool = FieldInfo(alias="redirectHasExtraInfo")

    request: DataRequestRequestRequest

    request_id: str = FieldInfo(alias="requestId")

    type: str

    wall_time: float = FieldInfo(alias="wallTime")

    frame_id: Optional[str] = FieldInfo(alias="frameId", default=None)

    loader_id: Optional[str] = FieldInfo(alias="loaderId", default=None)

    primary_request: Optional[bool] = FieldInfo(alias="primaryRequest", default=None)

    redirect_response: Optional[DataRequestRequestRedirectResponse] = FieldInfo(alias="redirectResponse", default=None)


class DataRequestResponseASN(BaseModel):
    asn: str

    country: str

    description: str

    ip: str

    name: str

    org: str


class DataRequestResponseGeoip(BaseModel):
    city: str

    country: str

    country_name: str

    geoname_id: str = FieldInfo(alias="geonameId")

    ll: List[float]

    region: str


class DataRequestResponseResponseSecurityDetails(BaseModel):
    certificate_id: float = FieldInfo(alias="certificateId")

    certificate_transparency_compliance: str = FieldInfo(alias="certificateTransparencyCompliance")

    cipher: str

    encrypted_client_hello: bool = FieldInfo(alias="encryptedClientHello")

    issuer: str

    key_exchange: str = FieldInfo(alias="keyExchange")

    key_exchange_group: str = FieldInfo(alias="keyExchangeGroup")

    protocol: str

    san_list: List[str] = FieldInfo(alias="sanList")

    server_signature_algorithm: float = FieldInfo(alias="serverSignatureAlgorithm")

    subject_name: str = FieldInfo(alias="subjectName")

    valid_from: float = FieldInfo(alias="validFrom")

    valid_to: float = FieldInfo(alias="validTo")


class DataRequestResponseResponseSecurityHeader(BaseModel):
    name: str

    value: str


class DataRequestResponseResponse(BaseModel):
    charset: str

    mime_type: str = FieldInfo(alias="mimeType")

    protocol: str

    remote_ip_address: str = FieldInfo(alias="remoteIPAddress")

    remote_port: float = FieldInfo(alias="remotePort")

    security_details: DataRequestResponseResponseSecurityDetails = FieldInfo(alias="securityDetails")

    security_headers: List[DataRequestResponseResponseSecurityHeader] = FieldInfo(alias="securityHeaders")

    security_state: str = FieldInfo(alias="securityState")

    status: float

    status_text: str = FieldInfo(alias="statusText")

    url: str

    headers: Optional[object] = None


class DataRequestResponse(BaseModel):
    asn: DataRequestResponseASN

    data_length: float = FieldInfo(alias="dataLength")

    encoded_data_length: float = FieldInfo(alias="encodedDataLength")

    geoip: DataRequestResponseGeoip

    has_extra_info: bool = FieldInfo(alias="hasExtraInfo")

    request_id: str = FieldInfo(alias="requestId")

    response: DataRequestResponseResponse

    size: float

    type: str

    content_available: Optional[bool] = FieldInfo(alias="contentAvailable", default=None)

    hash: Optional[str] = None


class DataRequest(BaseModel):
    request: DataRequestRequest

    response: DataRequestResponse

    requests: Optional[List[DataRequestRequest]] = None


class Data(BaseModel):
    console: List[DataConsole]

    cookies: List[DataCookie]

    globals: List[DataGlobal]

    links: List[DataLink]

    performance: List[DataPerformance]

    requests: List[DataRequest]


class ListsCertificate(BaseModel):
    issuer: str

    subject_name: str = FieldInfo(alias="subjectName")

    valid_from: float = FieldInfo(alias="validFrom")

    valid_to: float = FieldInfo(alias="validTo")


class Lists(BaseModel):
    asns: List[str]

    certificates: List[ListsCertificate]

    continents: List[str]

    countries: List[str]

    domains: List[str]

    hashes: List[str]

    ips: List[str]

    link_domains: List[str] = FieldInfo(alias="linkDomains")

    servers: List[str]

    urls: List[str]


class MetaProcessorsASNData(BaseModel):
    asn: str

    country: str

    description: str

    ip: str

    name: str


class MetaProcessorsASN(BaseModel):
    data: List[MetaProcessorsASNData]


class MetaProcessorsDNSData(BaseModel):
    address: str

    dnssec_valid: bool

    name: str

    type: str


class MetaProcessorsDNS(BaseModel):
    data: List[MetaProcessorsDNSData]


class MetaProcessorsDomainCategoriesData(BaseModel):
    inherited: object

    is_primary: bool = FieldInfo(alias="isPrimary")

    name: str


class MetaProcessorsDomainCategories(BaseModel):
    data: List[MetaProcessorsDomainCategoriesData]


class MetaProcessorsGeoipDataGeoip(BaseModel):
    city: str

    country: str

    country_name: str

    ll: List[float]

    region: str


class MetaProcessorsGeoipData(BaseModel):
    geoip: MetaProcessorsGeoipDataGeoip

    ip: str


class MetaProcessorsGeoip(BaseModel):
    data: List[MetaProcessorsGeoipData]


class MetaProcessorsPhishing(BaseModel):
    data: List[str]


class MetaProcessorsRadarRankData(BaseModel):
    bucket: str

    hostname: str

    rank: Optional[float] = None


class MetaProcessorsRadarRank(BaseModel):
    data: List[MetaProcessorsRadarRankData]


class MetaProcessorsWappaDataCategory(BaseModel):
    name: str

    priority: float


class MetaProcessorsWappaDataConfidence(BaseModel):
    confidence: float

    name: str

    pattern: str

    pattern_type: str = FieldInfo(alias="patternType")


class MetaProcessorsWappaData(BaseModel):
    app: str

    categories: List[MetaProcessorsWappaDataCategory]

    confidence: List[MetaProcessorsWappaDataConfidence]

    confidence_total: float = FieldInfo(alias="confidenceTotal")

    icon: str

    website: str


class MetaProcessorsWappa(BaseModel):
    data: List[MetaProcessorsWappaData]


class MetaProcessorsAgentReadinessChecksBotAccessControlContentSignalsEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksBotAccessControlContentSignalsEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksBotAccessControlContentSignalsEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksBotAccessControlContentSignalsEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksBotAccessControlContentSignalsEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksBotAccessControlContentSignalsEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksBotAccessControlContentSignalsEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksBotAccessControlContentSignals(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksBotAccessControlContentSignalsEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksBotAccessControlRobotsTxtaiRulesEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksBotAccessControlRobotsTxtaiRulesEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksBotAccessControlRobotsTxtaiRulesEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksBotAccessControlRobotsTxtaiRulesEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksBotAccessControlRobotsTxtaiRulesEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksBotAccessControlRobotsTxtaiRulesEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksBotAccessControlRobotsTxtaiRulesEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksBotAccessControlRobotsTXTAIRules(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksBotAccessControlRobotsTxtaiRulesEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksBotAccessControlWebBotAuthEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksBotAccessControlWebBotAuthEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksBotAccessControlWebBotAuthEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksBotAccessControlWebBotAuthEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksBotAccessControlWebBotAuthEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksBotAccessControlWebBotAuthEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksBotAccessControlWebBotAuthEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksBotAccessControlWebBotAuth(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksBotAccessControlWebBotAuthEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksBotAccessControl(BaseModel):
    content_signals: MetaProcessorsAgentReadinessChecksBotAccessControlContentSignals = FieldInfo(
        alias="contentSignals"
    )

    robots_txt_ai_rules: MetaProcessorsAgentReadinessChecksBotAccessControlRobotsTXTAIRules = FieldInfo(
        alias="robotsTxtAiRules"
    )

    web_bot_auth: MetaProcessorsAgentReadinessChecksBotAccessControlWebBotAuth = FieldInfo(alias="webBotAuth")


class MetaProcessorsAgentReadinessChecksCommerceAcpEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksCommerceAcpEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksCommerceAcpEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksCommerceAcpEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksCommerceAcpEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksCommerceAcpEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksCommerceAcpEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksCommerceAcp(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksCommerceAcpEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksCommerceAp2EvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksCommerceAp2EvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksCommerceAp2EvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksCommerceAp2Evidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksCommerceAp2EvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksCommerceAp2EvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksCommerceAp2EvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksCommerceAp2(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksCommerceAp2Evidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksCommerceUcpEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksCommerceUcpEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksCommerceUcpEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksCommerceUcpEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksCommerceUcpEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksCommerceUcpEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksCommerceUcpEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksCommerceUcp(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksCommerceUcpEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksCommerceX402EvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksCommerceX402EvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksCommerceX402EvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksCommerceX402Evidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksCommerceX402EvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksCommerceX402EvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksCommerceX402EvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksCommerceX402(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksCommerceX402Evidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksCommerce(BaseModel):
    acp: MetaProcessorsAgentReadinessChecksCommerceAcp

    ap2: MetaProcessorsAgentReadinessChecksCommerceAp2

    ucp: MetaProcessorsAgentReadinessChecksCommerceUcp

    x402: MetaProcessorsAgentReadinessChecksCommerceX402


class MetaProcessorsAgentReadinessChecksContentAccessibilityMarkdownNegotiationEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksContentAccessibilityMarkdownNegotiationEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksContentAccessibilityMarkdownNegotiationEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksContentAccessibilityMarkdownNegotiationEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksContentAccessibilityMarkdownNegotiationEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksContentAccessibilityMarkdownNegotiationEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksContentAccessibilityMarkdownNegotiationEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksContentAccessibilityMarkdownNegotiation(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksContentAccessibilityMarkdownNegotiationEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksContentAccessibility(BaseModel):
    markdown_negotiation: MetaProcessorsAgentReadinessChecksContentAccessibilityMarkdownNegotiation = FieldInfo(
        alias="markdownNegotiation"
    )


class MetaProcessorsAgentReadinessChecksDiscoverabilityLinkHeadersEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksDiscoverabilityLinkHeadersEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksDiscoverabilityLinkHeadersEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksDiscoverabilityLinkHeadersEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksDiscoverabilityLinkHeadersEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksDiscoverabilityLinkHeadersEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksDiscoverabilityLinkHeadersEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksDiscoverabilityLinkHeaders(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksDiscoverabilityLinkHeadersEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksDiscoverabilityRobotsTXTEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksDiscoverabilityRobotsTXTEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksDiscoverabilityRobotsTXTEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksDiscoverabilityRobotsTXTEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksDiscoverabilityRobotsTXTEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksDiscoverabilityRobotsTXTEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksDiscoverabilityRobotsTXTEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksDiscoverabilityRobotsTXT(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksDiscoverabilityRobotsTXTEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksDiscoverabilitySitemapEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksDiscoverabilitySitemapEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksDiscoverabilitySitemapEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksDiscoverabilitySitemapEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksDiscoverabilitySitemapEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksDiscoverabilitySitemapEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksDiscoverabilitySitemapEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksDiscoverabilitySitemap(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksDiscoverabilitySitemapEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksDiscoverability(BaseModel):
    link_headers: MetaProcessorsAgentReadinessChecksDiscoverabilityLinkHeaders = FieldInfo(alias="linkHeaders")

    robots_txt: MetaProcessorsAgentReadinessChecksDiscoverabilityRobotsTXT = FieldInfo(alias="robotsTxt")

    sitemap: MetaProcessorsAgentReadinessChecksDiscoverabilitySitemap


class MetaProcessorsAgentReadinessChecksDiscoveryA2aAgentCardEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksDiscoveryA2aAgentCardEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksDiscoveryA2aAgentCardEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksDiscoveryA2aAgentCardEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksDiscoveryA2aAgentCardEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksDiscoveryA2aAgentCardEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksDiscoveryA2aAgentCardEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksDiscoveryA2aAgentCard(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksDiscoveryA2aAgentCardEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksDiscoveryAgentSkillsEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksDiscoveryAgentSkillsEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksDiscoveryAgentSkillsEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksDiscoveryAgentSkillsEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksDiscoveryAgentSkillsEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksDiscoveryAgentSkillsEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksDiscoveryAgentSkillsEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksDiscoveryAgentSkills(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksDiscoveryAgentSkillsEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksDiscoveryAPICatalogEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksDiscoveryAPICatalogEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksDiscoveryAPICatalogEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksDiscoveryAPICatalogEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksDiscoveryAPICatalogEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksDiscoveryAPICatalogEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksDiscoveryAPICatalogEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksDiscoveryAPICatalog(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksDiscoveryAPICatalogEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksDiscoveryMcpServerCardEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksDiscoveryMcpServerCardEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksDiscoveryMcpServerCardEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksDiscoveryMcpServerCardEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksDiscoveryMcpServerCardEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksDiscoveryMcpServerCardEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksDiscoveryMcpServerCardEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksDiscoveryMcpServerCard(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksDiscoveryMcpServerCardEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksDiscoveryOAuthDiscoveryEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksDiscoveryOAuthDiscoveryEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksDiscoveryOAuthDiscoveryEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksDiscoveryOAuthDiscoveryEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksDiscoveryOAuthDiscoveryEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksDiscoveryOAuthDiscoveryEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksDiscoveryOAuthDiscoveryEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksDiscoveryOAuthDiscovery(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksDiscoveryOAuthDiscoveryEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksDiscoveryOAuthProtectedResourceEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksDiscoveryOAuthProtectedResourceEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksDiscoveryOAuthProtectedResourceEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksDiscoveryOAuthProtectedResourceEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksDiscoveryOAuthProtectedResourceEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksDiscoveryOAuthProtectedResourceEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksDiscoveryOAuthProtectedResourceEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksDiscoveryOAuthProtectedResource(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksDiscoveryOAuthProtectedResourceEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksDiscoveryWebMcpEvidenceFinding(BaseModel):
    outcome: str

    summary: str


class MetaProcessorsAgentReadinessChecksDiscoveryWebMcpEvidenceRequest(BaseModel):
    method: str

    url: str

    headers: Optional[object] = None


class MetaProcessorsAgentReadinessChecksDiscoveryWebMcpEvidenceResponse(BaseModel):
    status: int

    status_text: str = FieldInfo(alias="statusText")

    body_preview: Optional[str] = FieldInfo(alias="bodyPreview", default=None)

    body_size: Optional[int] = FieldInfo(alias="bodySize", default=None)

    headers: Optional[object] = None

    redirected_to: Optional[str] = FieldInfo(alias="redirectedTo", default=None)


class MetaProcessorsAgentReadinessChecksDiscoveryWebMcpEvidence(BaseModel):
    action: str

    label: str

    finding: Optional[MetaProcessorsAgentReadinessChecksDiscoveryWebMcpEvidenceFinding] = None

    request: Optional[MetaProcessorsAgentReadinessChecksDiscoveryWebMcpEvidenceRequest] = None

    response: Optional[MetaProcessorsAgentReadinessChecksDiscoveryWebMcpEvidenceResponse] = None


class MetaProcessorsAgentReadinessChecksDiscoveryWebMcp(BaseModel):
    status: str

    details: Optional[object] = None

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    evidence: Optional[List[MetaProcessorsAgentReadinessChecksDiscoveryWebMcpEvidence]] = None

    message: Optional[str] = None


class MetaProcessorsAgentReadinessChecksDiscovery(BaseModel):
    a2a_agent_card: MetaProcessorsAgentReadinessChecksDiscoveryA2aAgentCard = FieldInfo(alias="a2aAgentCard")

    agent_skills: MetaProcessorsAgentReadinessChecksDiscoveryAgentSkills = FieldInfo(alias="agentSkills")

    api_catalog: MetaProcessorsAgentReadinessChecksDiscoveryAPICatalog = FieldInfo(alias="apiCatalog")

    mcp_server_card: MetaProcessorsAgentReadinessChecksDiscoveryMcpServerCard = FieldInfo(alias="mcpServerCard")

    oauth_discovery: MetaProcessorsAgentReadinessChecksDiscoveryOAuthDiscovery = FieldInfo(alias="oauthDiscovery")

    oauth_protected_resource: MetaProcessorsAgentReadinessChecksDiscoveryOAuthProtectedResource = FieldInfo(
        alias="oauthProtectedResource"
    )

    web_mcp: MetaProcessorsAgentReadinessChecksDiscoveryWebMcp = FieldInfo(alias="webMcp")


class MetaProcessorsAgentReadinessChecks(BaseModel):
    bot_access_control: MetaProcessorsAgentReadinessChecksBotAccessControl = FieldInfo(alias="botAccessControl")

    commerce: MetaProcessorsAgentReadinessChecksCommerce

    content_accessibility: MetaProcessorsAgentReadinessChecksContentAccessibility = FieldInfo(
        alias="contentAccessibility"
    )

    discoverability: MetaProcessorsAgentReadinessChecksDiscoverability

    discovery: MetaProcessorsAgentReadinessChecksDiscovery


class MetaProcessorsAgentReadinessNextLevelRequirement(BaseModel):
    check: str

    description: str

    prompt: str

    skill_url: str = FieldInfo(alias="skillUrl")

    spec_urls: List[str] = FieldInfo(alias="specUrls")


class MetaProcessorsAgentReadinessNextLevel(BaseModel):
    name: str

    requirements: List[MetaProcessorsAgentReadinessNextLevelRequirement]

    target: int


class MetaProcessorsAgentReadiness(BaseModel):
    checks: MetaProcessorsAgentReadinessChecks

    level: int

    level_name: str = FieldInfo(alias="levelName")

    commerce_signals: Optional[List[str]] = FieldInfo(alias="commerceSignals", default=None)

    is_commerce: Optional[bool] = FieldInfo(alias="isCommerce", default=None)

    next_level: Optional[MetaProcessorsAgentReadinessNextLevel] = FieldInfo(alias="nextLevel", default=None)


class MetaProcessorsPhishingV2(BaseModel):
    data: List[str]


class MetaProcessorsRobotsTXTDataRulesapi_emptyContentSignal(BaseModel):
    ai_input: Optional[str] = FieldInfo(alias="ai-input", default=None)

    ai_train: Optional[str] = FieldInfo(alias="ai-train", default=None)

    search: Optional[str] = None


class MetaProcessorsRobotsTXTDataRulesapi_empty(BaseModel):
    allow: List[str]

    disallow: List[str]

    content_signal: Optional[MetaProcessorsRobotsTXTDataRulesapi_emptyContentSignal] = FieldInfo(
        alias="contentSignal", default=None
    )

    crawl_delay: Optional[float] = FieldInfo(alias="crawlDelay", default=None)


class MetaProcessorsRobotsTXTDataRules(BaseModel):
    api_empty: MetaProcessorsRobotsTXTDataRulesapi_empty = FieldInfo(alias="*")


class MetaProcessorsRobotsTXTData(BaseModel):
    rules: MetaProcessorsRobotsTXTDataRules

    sitemaps: List[str]

    hash: Optional[str] = None


class MetaProcessorsRobotsTXT(BaseModel):
    data: List[MetaProcessorsRobotsTXTData]


class MetaProcessorsURLCategoriesDataContent(BaseModel):
    id: float

    name: str

    super_category_id: float


class MetaProcessorsURLCategoriesDataInheritedContent(BaseModel):
    id: float

    name: str

    super_category_id: float


class MetaProcessorsURLCategoriesDataInheritedRisk(BaseModel):
    id: float

    name: str

    super_category_id: float


class MetaProcessorsURLCategoriesDataInherited(BaseModel):
    content: List[MetaProcessorsURLCategoriesDataInheritedContent]

    from_: str = FieldInfo(alias="from")

    risks: List[MetaProcessorsURLCategoriesDataInheritedRisk]


class MetaProcessorsURLCategoriesDataRisk(BaseModel):
    id: float

    name: str

    super_category_id: float


class MetaProcessorsURLCategoriesData(BaseModel):
    content: List[MetaProcessorsURLCategoriesDataContent]

    inherited: MetaProcessorsURLCategoriesDataInherited

    name: str

    risks: List[MetaProcessorsURLCategoriesDataRisk]


class MetaProcessorsURLCategories(BaseModel):
    data: List[MetaProcessorsURLCategoriesData]


class MetaProcessors(BaseModel):
    asn: MetaProcessorsASN

    dns: MetaProcessorsDNS

    domain_categories: MetaProcessorsDomainCategories = FieldInfo(alias="domainCategories")

    geoip: MetaProcessorsGeoip

    phishing: MetaProcessorsPhishing

    radar_rank: MetaProcessorsRadarRank = FieldInfo(alias="radarRank")

    wappa: MetaProcessorsWappa

    agent_readiness: Optional[MetaProcessorsAgentReadiness] = FieldInfo(alias="agentReadiness", default=None)

    phishing_v2: Optional[MetaProcessorsPhishingV2] = None

    robots_txt: Optional[MetaProcessorsRobotsTXT] = FieldInfo(alias="robotsTxt", default=None)

    url_categories: Optional[MetaProcessorsURLCategories] = FieldInfo(alias="urlCategories", default=None)


class Meta(BaseModel):
    processors: MetaProcessors


class PageScreenshot(BaseModel):
    dhash: str

    mm3_hash: float = FieldInfo(alias="mm3Hash")

    name: str

    phash: str


class Page(BaseModel):
    apex_domain: str = FieldInfo(alias="apexDomain")

    asn: str

    asnname: str

    city: str

    country: str

    domain: str

    ip: str

    mime_type: str = FieldInfo(alias="mimeType")

    server: str

    status: str

    title: str

    tls_age_days: float = FieldInfo(alias="tlsAgeDays")

    tls_issuer: str = FieldInfo(alias="tlsIssuer")

    tls_valid_days: float = FieldInfo(alias="tlsValidDays")

    tls_valid_from: str = FieldInfo(alias="tlsValidFrom")

    url: str

    screenshot: Optional[PageScreenshot] = None


class Scanner(BaseModel):
    colo: str

    country: str


class StatsDomainStat(BaseModel):
    count: float

    countries: List[str]

    domain: str

    encoded_size: float = FieldInfo(alias="encodedSize")

    index: float

    initiators: List[str]

    ips: List[str]

    redirects: float

    size: float


class StatsIPStatASN(BaseModel):
    asn: str

    country: str

    description: str

    ip: str

    name: str

    org: str


class StatsIPStatGeoip(BaseModel):
    city: str

    country: str

    country_name: str

    ll: List[float]

    region: str


class StatsIPStat(BaseModel):
    asn: StatsIPStatASN

    countries: List[str]

    domains: List[str]

    encoded_size: float = FieldInfo(alias="encodedSize")

    geoip: StatsIPStatGeoip

    index: float

    ip: str

    ipv6: bool

    redirects: float

    requests: float

    size: float

    count: Optional[float] = None


class StatsProtocolStat(BaseModel):
    count: float

    countries: List[str]

    encoded_size: float = FieldInfo(alias="encodedSize")

    ips: List[str]

    protocol: str

    size: float


class StatsResourceStat(BaseModel):
    compression: float

    count: float

    countries: List[str]

    encoded_size: float = FieldInfo(alias="encodedSize")

    ips: List[str]

    percentage: float

    size: float

    type: str


class StatsServerStat(BaseModel):
    count: float

    countries: List[str]

    encoded_size: float = FieldInfo(alias="encodedSize")

    ips: List[str]

    server: str

    size: float


class StatsTLSStatProtocols(BaseModel):
    tls_1_3_aes_128_gcm: float = FieldInfo(alias="TLS 1.3 / AES_128_GCM")


class StatsTLSStat(BaseModel):
    count: float

    countries: List[str]

    encoded_size: float = FieldInfo(alias="encodedSize")

    ips: List[str]

    protocols: StatsTLSStatProtocols

    security_state: str = FieldInfo(alias="securityState")

    size: float


class Stats(BaseModel):
    domain_stats: List[StatsDomainStat] = FieldInfo(alias="domainStats")

    ip_stats: List[StatsIPStat] = FieldInfo(alias="ipStats")

    i_pv6_percentage: float = FieldInfo(alias="IPv6Percentage")

    malicious: float

    protocol_stats: List[StatsProtocolStat] = FieldInfo(alias="protocolStats")

    resource_stats: List[StatsResourceStat] = FieldInfo(alias="resourceStats")

    secure_percentage: float = FieldInfo(alias="securePercentage")

    secure_requests: float = FieldInfo(alias="secureRequests")

    server_stats: List[StatsServerStat] = FieldInfo(alias="serverStats")

    tls_stats: List[StatsTLSStat] = FieldInfo(alias="tlsStats")

    total_links: float = FieldInfo(alias="totalLinks")

    uniq_asns: float = FieldInfo(alias="uniqASNs")

    uniq_countries: float = FieldInfo(alias="uniqCountries")


class TaskOptions(BaseModel):
    custom_headers: Optional[object] = FieldInfo(alias="customHeaders", default=None)
    """Custom headers set."""

    screenshots_resolutions: Optional[List[str]] = FieldInfo(alias="screenshotsResolutions", default=None)


class Task(BaseModel):
    apex_domain: str = FieldInfo(alias="apexDomain")

    domain: str

    dom_url: str = FieldInfo(alias="domURL")

    method: str

    options: TaskOptions

    report_url: str = FieldInfo(alias="reportURL")

    screenshot_url: str = FieldInfo(alias="screenshotURL")

    source: str

    success: bool

    time: str

    url: str

    uuid: str

    visibility: str


class VerdictsOverall(BaseModel):
    categories: List[str]

    has_verdicts: bool = FieldInfo(alias="hasVerdicts")

    malicious: bool

    tags: List[str]


class Verdicts(BaseModel):
    overall: VerdictsOverall


class ScanGetResponse(BaseModel):
    data: Data

    lists: Lists

    meta: Meta

    page: Page

    scanner: Scanner

    stats: Stats

    task: Task

    verdicts: Verdicts
