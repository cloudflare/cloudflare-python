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

    ll: List[object]

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
