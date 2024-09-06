# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List, Optional

from .url_scanner_domain import URLScannerDomain

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = [
    "ScanGetResponse",
    "Scan",
    "ScanCertificate",
    "ScanGeo",
    "ScanMeta",
    "ScanMetaProcessors",
    "ScanMetaProcessorsCategories",
    "ScanMetaProcessorsCategoriesRisk",
    "ScanMetaProcessorsRank",
    "ScanMetaProcessorsTech",
    "ScanMetaProcessorsTechCategory",
    "ScanMetaProcessorsTechEvidence",
    "ScanMetaProcessorsTechEvidencePattern",
    "ScanPage",
    "ScanPageConsole",
    "ScanPageCookie",
    "ScanPageHeader",
    "ScanPageJS",
    "ScanPageJSVariable",
    "ScanPageSecurityViolation",
    "ScanPerformance",
    "ScanTask",
    "ScanTaskError",
    "ScanTaskScannedFrom",
    "ScanVerdicts",
    "ScanVerdictsOverall",
    "ScanVerdictsOverallCategory",
    "ScanASNs",
    "ScanASNsASN",
    "ScanDomains",
    "ScanDomainsExampleCom",
    "ScanDomainsExampleComCategories",
    "ScanDomainsExampleComCategoriesInherited",
    "ScanDomainsExampleComDNS",
    "ScanDomainsExampleComRank",
    "ScanIPs",
    "ScanIPsIP",
    "ScanLinks",
    "ScanLinksLink",
]


class ScanCertificate(BaseModel):
    issuer: str

    subject_name: str = FieldInfo(alias="subjectName")

    valid_from: float = FieldInfo(alias="validFrom")

    valid_to: float = FieldInfo(alias="validTo")


class ScanGeo(BaseModel):
    continents: List[str]
    """GeoIP continent location"""

    locations: List[str]
    """GeoIP country location"""


class ScanMetaProcessorsCategoriesRisk(BaseModel):
    id: int

    name: str

    super_category_id: int


class ScanMetaProcessorsCategories(BaseModel):
    content: List[URLScannerDomain]

    risks: List[ScanMetaProcessorsCategoriesRisk]


class ScanMetaProcessorsRank(BaseModel):
    bucket: str

    name: str

    rank: Optional[int] = None
    """Rank in the Global Radar Rank, if set.

    See more at https://blog.cloudflare.com/radar-domain-rankings/
    """


class ScanMetaProcessorsTechCategory(BaseModel):
    id: int

    groups: List[int]

    name: str

    priority: int

    slug: str


class ScanMetaProcessorsTechEvidencePattern(BaseModel):
    confidence: int

    excludes: List[str]

    implies: List[str]

    match: str

    name: str
    """Header or Cookie name when set"""

    regex: str

    type: str

    value: str

    version: str


class ScanMetaProcessorsTechEvidence(BaseModel):
    implied_by: List[str] = FieldInfo(alias="impliedBy")

    patterns: List[ScanMetaProcessorsTechEvidencePattern]


class ScanMetaProcessorsTech(BaseModel):
    categories: List[ScanMetaProcessorsTechCategory]

    confidence: int

    evidence: ScanMetaProcessorsTechEvidence

    icon: str

    name: str

    slug: str

    website: str

    description: Optional[str] = None


class ScanMetaProcessors(BaseModel):
    categories: ScanMetaProcessorsCategories

    phishing: List[str]

    rank: ScanMetaProcessorsRank

    tech: List[ScanMetaProcessorsTech]


class ScanMeta(BaseModel):
    processors: ScanMetaProcessors


class ScanPageConsole(BaseModel):
    category: str

    text: str

    type: str

    url: Optional[str] = None


class ScanPageCookie(BaseModel):
    domain: str

    expires: float

    http_only: bool = FieldInfo(alias="httpOnly")

    name: str

    path: str

    same_party: bool = FieldInfo(alias="sameParty")

    secure: bool

    session: bool

    size: float

    source_port: float = FieldInfo(alias="sourcePort")

    source_scheme: str = FieldInfo(alias="sourceScheme")

    value: str

    priority: Optional[str] = None


class ScanPageHeader(BaseModel):
    name: str

    value: str


class ScanPageJSVariable(BaseModel):
    name: str

    type: str


class ScanPageJS(BaseModel):
    variables: List[ScanPageJSVariable]


class ScanPageSecurityViolation(BaseModel):
    category: str

    text: str

    url: str


class ScanPage(BaseModel):
    asn: str

    asn_location_alpha2: str = FieldInfo(alias="asnLocationAlpha2")

    asnname: str

    console: List[ScanPageConsole]

    cookies: List[ScanPageCookie]

    country: str

    country_location_alpha2: str = FieldInfo(alias="countryLocationAlpha2")

    domain: str

    headers: List[ScanPageHeader]

    ip: str

    js: ScanPageJS

    security_violations: List[ScanPageSecurityViolation] = FieldInfo(alias="securityViolations")

    status: float

    subdivision1_name: str = FieldInfo(alias="subdivision1Name")

    subdivision2name: str

    url: str


class ScanPerformance(BaseModel):
    connect_end: float = FieldInfo(alias="connectEnd")

    connect_start: float = FieldInfo(alias="connectStart")

    decoded_body_size: float = FieldInfo(alias="decodedBodySize")

    domain_lookup_end: float = FieldInfo(alias="domainLookupEnd")

    domain_lookup_start: float = FieldInfo(alias="domainLookupStart")

    dom_complete: float = FieldInfo(alias="domComplete")

    dom_content_loaded_event_end: float = FieldInfo(alias="domContentLoadedEventEnd")

    dom_content_loaded_event_start: float = FieldInfo(alias="domContentLoadedEventStart")

    dom_interactive: float = FieldInfo(alias="domInteractive")

    duration: float

    encoded_body_size: float = FieldInfo(alias="encodedBodySize")

    entry_type: str = FieldInfo(alias="entryType")

    fetch_start: float = FieldInfo(alias="fetchStart")

    initiator_type: str = FieldInfo(alias="initiatorType")

    load_event_end: float = FieldInfo(alias="loadEventEnd")

    load_event_start: float = FieldInfo(alias="loadEventStart")

    name: str

    next_hop_protocol: str = FieldInfo(alias="nextHopProtocol")

    redirect_count: float = FieldInfo(alias="redirectCount")

    redirect_end: float = FieldInfo(alias="redirectEnd")

    redirect_start: float = FieldInfo(alias="redirectStart")

    request_start: float = FieldInfo(alias="requestStart")

    response_end: float = FieldInfo(alias="responseEnd")

    response_start: float = FieldInfo(alias="responseStart")

    secure_connection_start: float = FieldInfo(alias="secureConnectionStart")

    start_time: float = FieldInfo(alias="startTime")

    transfer_size: float = FieldInfo(alias="transferSize")

    type: str

    unload_event_end: float = FieldInfo(alias="unloadEventEnd")

    unload_event_start: float = FieldInfo(alias="unloadEventStart")

    worker_start: float = FieldInfo(alias="workerStart")


class ScanTaskError(BaseModel):
    message: str


class ScanTaskScannedFrom(BaseModel):
    colo: str
    """IATA code of Cloudflare datacenter"""


class ScanTask(BaseModel):
    client_location: str = FieldInfo(alias="clientLocation")
    """Submitter location"""

    client_type: Literal["Site", "Automatic", "Api"] = FieldInfo(alias="clientType")

    effective_url: str = FieldInfo(alias="effectiveUrl")
    """URL of the primary request, after all HTTP redirects"""

    errors: List[ScanTaskError]

    scanned_from: ScanTaskScannedFrom = FieldInfo(alias="scannedFrom")

    status: Literal["Queued", "InProgress", "InPostProcessing", "Finished"]

    success: bool

    time: str

    time_end: str = FieldInfo(alias="timeEnd")

    url: str
    """Submitted URL"""

    uuid: str
    """Scan ID"""

    visibility: Literal["Public", "Unlisted"]


class ScanVerdictsOverallCategory(BaseModel):
    id: float

    name: str

    super_category_id: float


class ScanVerdictsOverall(BaseModel):
    categories: List[ScanVerdictsOverallCategory]

    malicious: bool
    """
    At least one of our subsystems marked the site as potentially malicious at the
    time of the scan.
    """

    phishing: List[str]


class ScanVerdicts(BaseModel):
    overall: ScanVerdictsOverall


class ScanASNsASN(BaseModel):
    asn: str

    description: str

    location_alpha2: str

    name: str

    org_name: str


class ScanASNs(BaseModel):
    asn: Optional[ScanASNsASN] = None
    """ASN's contacted"""


class ScanDomainsExampleComCategoriesInherited(BaseModel):
    content: Optional[List[URLScannerDomain]] = None

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    risks: Optional[List[URLScannerDomain]] = None


class ScanDomainsExampleComCategories(BaseModel):
    inherited: ScanDomainsExampleComCategoriesInherited

    content: Optional[List[URLScannerDomain]] = None

    risks: Optional[List[URLScannerDomain]] = None


class ScanDomainsExampleComDNS(BaseModel):
    address: str

    dnssec_valid: bool

    name: str

    type: str


class ScanDomainsExampleComRank(BaseModel):
    bucket: str

    name: str

    rank: Optional[int] = None
    """Rank in the Global Radar Rank, if set.

    See more at https://blog.cloudflare.com/radar-domain-rankings/
    """


class ScanDomainsExampleCom(BaseModel):
    categories: ScanDomainsExampleComCategories

    dns: List[ScanDomainsExampleComDNS]

    name: str

    rank: ScanDomainsExampleComRank

    type: str


class ScanDomains(BaseModel):
    example_com: Optional[ScanDomainsExampleCom] = FieldInfo(alias="example.com", default=None)


class ScanIPsIP(BaseModel):
    asn: str

    asn_description: str = FieldInfo(alias="asnDescription")

    asn_location_alpha2: str = FieldInfo(alias="asnLocationAlpha2")

    asn_name: str = FieldInfo(alias="asnName")

    asn_org_name: str = FieldInfo(alias="asnOrgName")

    continent: str

    geoname_id: str = FieldInfo(alias="geonameId")

    ip: str

    ip_version: str = FieldInfo(alias="ipVersion")

    latitude: str

    location_alpha2: str = FieldInfo(alias="locationAlpha2")

    location_name: str = FieldInfo(alias="locationName")

    longitude: str

    subdivision1_name: str = FieldInfo(alias="subdivision1Name")

    subdivision2_name: str = FieldInfo(alias="subdivision2Name")


class ScanIPs(BaseModel):
    ip: Optional[ScanIPsIP] = None


class ScanLinksLink(BaseModel):
    href: str
    """Outgoing link detected in the DOM"""

    text: str


class ScanLinks(BaseModel):
    link: Optional[ScanLinksLink] = None


class Scan(BaseModel):
    certificates: List[ScanCertificate]

    geo: ScanGeo

    meta: ScanMeta

    page: ScanPage

    performance: List[ScanPerformance]

    task: ScanTask

    verdicts: ScanVerdicts

    asns: Optional[ScanASNs] = None
    """Dictionary of Autonomous System Numbers where ASN's are the keys"""

    domains: Optional[ScanDomains] = None

    ips: Optional[ScanIPs] = None

    links: Optional[ScanLinks] = None


class ScanGetResponse(BaseModel):
    scan: Scan
