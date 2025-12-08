# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .nel import NEL
from .ipv6 import IPV6
from .webp import WebP
from .http2 import HTTP2
from .http3 import HTTP3
from .brotli import Brotli
from .ciphers import Ciphers
from .tls_1_3 import TLS1_3
from .zero_rtt import ZeroRTT
from ..._models import BaseModel
from .websocket import Websocket
from .early_hints import EarlyHints
from .pseudo_ipv4 import PseudoIPV4
from .advanced_ddos import AdvancedDDoS
from .always_online import AlwaysOnline
from .challenge_ttl import ChallengeTTL
from .image_resizing import ImageResizing
from .min_tls_version import MinTLSVersion
from .ssl_recommender import SSLRecommender
from .tls_client_auth import TLSClientAuth
from .development_mode import DevelopmentMode
from .orange_to_orange import OrangeToOrange
from .prefetch_preload import PrefetchPreload
from .security_headers import SecurityHeaders
from .h2_prioritization import H2Prioritization
from .hotlink_protection import HotlinkProtection
from .proxy_read_timeout import ProxyReadTimeout
from .opportunistic_onion import OpportunisticOnion
from .server_side_excludes import ServerSideExcludes
from .automatic_platform_optimization import AutomaticPlatformOptimization

__all__ = [
    "SettingGetResponse",
    "ZonesCacheRulesAegis",
    "ZonesCacheRulesAegisValue",
    "ZonesSchemasAlwaysUseHTTPS",
    "ZonesSchemasAutomaticHTTPSRewrites",
    "ZonesSchemasBrowserCacheTTL",
    "ZonesSchemasBrowserCheck",
    "ZonesSchemasCacheLevel",
    "ZonesChinaNetworkEnabled",
    "ZonesCNAMEFlattening",
    "ZonesSchemasEdgeCacheTTL",
    "ZonesSchemasEmailObfuscation",
    "ZonesSchemasIPGeolocation",
    "ZonesMaxUpload",
    "ZonesSchemasMirage",
    "ZonesSchemasOpportunisticEncryption",
    "ZonesSchemasOriginErrorPagePassThru",
    "ZonesCacheRulesOriginH2MaxStreams",
    "ZonesCacheRulesOriginMaxHTTPVersion",
    "ZonesSchemasPolish",
    "ZonesPrivacyPass",
    "ZonesReplaceInsecureJS",
    "ZonesSchemasResponseBuffering",
    "ZonesSchemasRocketLoader",
    "ZonesSchemasAutomaticPlatformOptimization",
    "ZonesSchemasSecurityLevel",
    "ZonesSha1Support",
    "ZonesSchemasSortQueryStringForCache",
    "ZonesSchemasSSL",
    "ZonesTLS1_2Only",
    "ZonesTransformations",
    "ZonesTransformationsAllowedOrigins",
    "ZonesSchemasTrueClientIPHeader",
    "ZonesSchemasWAF",
]


class ZonesCacheRulesAegisValue(BaseModel):
    """Value of the zone setting."""

    enabled: Optional[bool] = None
    """Whether the feature is enabled or not."""

    pool_id: Optional[str] = None
    """
    Egress pool id which refers to a grouping of dedicated egress IPs through which
    Cloudflare will connect to origin.
    """


class ZonesCacheRulesAegis(BaseModel):
    """
    Aegis provides dedicated egress IPs (from Cloudflare to your origin) for your layer 7 WAF and CDN services. The egress IPs are reserved exclusively for your account so that you can increase your origin security by only allowing traffic from a small list of IP addresses.
    """

    id: Literal["aegis"]
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """Last time this setting was modified."""

    value: Optional[ZonesCacheRulesAegisValue] = None
    """Value of the zone setting."""


class ZonesSchemasAlwaysUseHTTPS(BaseModel):
    """
    Reply to all requests for URLs that use "http" with a 301 redirect to the equivalent "https" URL. If you only want to redirect for a subset of requests, consider creating an "Always use HTTPS" page rule.
    """

    id: Literal["always_use_https"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasAutomaticHTTPSRewrites(BaseModel):
    """Enable the Automatic HTTPS Rewrites feature for this zone."""

    id: Literal["automatic_https_rewrites"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasBrowserCacheTTL(BaseModel):
    """
    Browser Cache TTL (in seconds) specifies how long Cloudflare-cached resources will remain on your visitors' computers. Cloudflare will honor any larger times specified by your server. (https://support.cloudflare.com/hc/en-us/articles/200168276).
    """

    id: Literal["browser_cache_ttl"]
    """ID of the zone setting."""

    value: int
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasBrowserCheck(BaseModel):
    """
    Browser Integrity Check is similar to Bad Behavior and looks for common HTTP headers abused most commonly by spammers and denies access to your page.  It will also challenge visitors that do not have a user agent or a non standard user agent (also commonly used by abuse bots, crawlers or visitors). (https://support.cloudflare.com/hc/en-us/articles/200170086).
    """

    id: Literal["browser_check"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasCacheLevel(BaseModel):
    """Cache Level functions based off the setting level.

    The basic setting will cache most static resources (i.e., css, images, and JavaScript). The simplified setting will ignore the query string when delivering a cached resource. The aggressive setting will cache all static resources, including ones with a query string. (https://support.cloudflare.com/hc/en-us/articles/200168256).
    """

    id: Literal["cache_level"]
    """ID of the zone setting."""

    value: Literal["aggressive", "basic", "simplified"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesChinaNetworkEnabled(BaseModel):
    """Determines whether or not the china network is enabled."""

    id: Literal["china_network_enabled"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesCNAMEFlattening(BaseModel):
    """Whether or not cname flattening is on."""

    id: Literal["cname_flattening"]
    """How to flatten the cname destination."""

    value: Literal["flatten_at_root", "flatten_all"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasEdgeCacheTTL(BaseModel):
    """
    Time (in seconds) that a resource will be ensured to remain on Cloudflare's cache servers.
    """

    id: Literal["edge_cache_ttl"]
    """ID of the zone setting."""

    value: Literal[
        30,
        60,
        300,
        1200,
        1800,
        3600,
        7200,
        10800,
        14400,
        18000,
        28800,
        43200,
        57600,
        72000,
        86400,
        172800,
        259200,
        345600,
        432000,
        518400,
        604800,
    ]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasEmailObfuscation(BaseModel):
    """
    Encrypt email adresses on your web page from bots, while keeping them visible to humans. (https://support.cloudflare.com/hc/en-us/articles/200170016).
    """

    id: Literal["email_obfuscation"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasIPGeolocation(BaseModel):
    """
    Enable IP Geolocation to have Cloudflare geolocate visitors to your website and pass the country code to you. (https://support.cloudflare.com/hc/en-us/articles/200168236).
    """

    id: Literal["ip_geolocation"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesMaxUpload(BaseModel):
    """Maximum size of an allowable upload."""

    id: Literal["max_upload"]
    """identifier of the zone setting."""

    value: Literal[100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 1000]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasMirage(BaseModel):
    """Automatically optimize image loading for website visitors on mobile
    devices.

    Refer to [our blog post](http://blog.cloudflare.com/mirage2-solving-mobile-speed)
    for more information.
    """

    id: Literal["mirage"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasOpportunisticEncryption(BaseModel):
    """Enables the Opportunistic Encryption feature for a zone."""

    id: Literal["opportunistic_encryption"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasOriginErrorPagePassThru(BaseModel):
    """
    Cloudflare will proxy customer error pages on any 502,504 errors on origin server instead of showing a default Cloudflare error page. This does not apply to 522 errors and is limited to Enterprise Zones.
    """

    id: Literal["origin_error_page_pass_thru"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesCacheRulesOriginH2MaxStreams(BaseModel):
    """
    Origin H2 Max Streams configures the max number of concurrent requests that Cloudflare will send within the same connection when communicating with the origin server, if the origin supports it. Note that if your origin does not support H2 multiplexing, 5xx errors may be observed, particularly 520s. Also note that the default value is `100` for all plan types except Enterprise where it is `1`. `1` means that H2 multiplexing is disabled.
    """

    id: Literal["origin_h2_max_streams"]
    """Value of the zone setting."""

    modified_on: Optional[datetime] = None
    """Last time this setting was modified."""

    value: Optional[int] = None
    """Value of the Origin H2 Max Streams Setting."""


class ZonesCacheRulesOriginMaxHTTPVersion(BaseModel):
    """
    Origin Max HTTP Setting Version sets the highest HTTP version Cloudflare will attempt to use with your origin. This setting allows Cloudflare to make HTTP/2 requests to your origin. (Refer to [Enable HTTP/2 to Origin](https://developers.cloudflare.com/cache/how-to/enable-http2-to-origin/), for more information.). The default value is "2" for all plan types except Enterprise where it is "1".
    """

    id: Literal["origin_max_http_version"]
    """Value of the zone setting."""

    modified_on: Optional[datetime] = None
    """Last time this setting was modified."""

    value: Optional[Literal["2", "1"]] = None
    """Value of the Origin Max HTTP Version Setting."""


class ZonesSchemasPolish(BaseModel):
    """Removes metadata and compresses your images for faster page load times.

    Basic (Lossless): Reduce the size of PNG, JPEG, and GIF files - no impact on visual quality. Basic + JPEG (Lossy): Further reduce the size of JPEG files for faster image loading. Larger JPEGs are converted to progressive images, loading a lower-resolution image first and ending in a higher-resolution version. Not recommended for hi-res photography sites.
    """

    id: Literal["polish"]
    """ID of the zone setting."""

    value: Literal["off", "lossless", "lossy"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesPrivacyPass(BaseModel):
    """
    Privacy Pass v1 was a browser extension developed by the Privacy Pass Team to improve the browsing experience for your visitors by allowing users to reduce the number of CAPTCHAs shown. (https://support.cloudflare.com/hc/en-us/articles/115001992652-Privacy-Pass).
    """

    id: Literal["privacy_pass"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesReplaceInsecureJS(BaseModel):
    """
    Automatically replace insecure JavaScript libraries with safer and faster alternatives provided under cdnjs and powered by Cloudflare. Currently supports the following libraries: Polyfill under polyfill.io.
    """

    id: Literal["replace_insecure_js"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasResponseBuffering(BaseModel):
    """Enables or disables buffering of responses from the proxied server.

    Cloudflare may buffer the whole payload to deliver it at once to the client versus allowing it to be delivered in chunks. By default, the proxied server streams directly and is not buffered by Cloudflare. This is limited to Enterprise Zones.
    """

    id: Literal["response_buffering"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasRocketLoader(BaseModel):
    """
    Rocket Loader is a general-purpose asynchronous JavaScript optimisation that prioritises rendering your content while loading your site's Javascript asynchronously. Turning on Rocket Loader will immediately improve a web page's rendering time sometimes measured as Time to First Paint (TTFP), and also the `window.onload` time (assuming there is JavaScript on the page). This can have a positive impact on your Google search ranking. When turned on, Rocket Loader will automatically defer the loading of all Javascript referenced in your HTML, with no configuration required. Refer to [Understanding Rocket Loader](https://support.cloudflare.com/hc/articles/200168056) for more information.
    """

    id: Literal["rocket_loader"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasAutomaticPlatformOptimization(BaseModel):
    """
    [Automatic Platform Optimization for WordPress](https://developers.cloudflare.com/automatic-platform-optimization/) serves your WordPress site from Cloudflare's edge network and caches third-party fonts.
    """

    id: Literal["automatic_platform_optimization"]
    """ID of the zone setting."""

    value: AutomaticPlatformOptimization
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasSecurityLevel(BaseModel):
    """
    Choose the appropriate security profile for your website, which will automatically adjust each of the security settings. If you choose to customize an individual security setting, the profile will become Custom. (https://support.cloudflare.com/hc/en-us/articles/200170056).
    """

    id: Literal["security_level"]
    """ID of the zone setting."""

    value: Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSha1Support(BaseModel):
    """Allow SHA1 support."""

    id: Literal["sha1_support"]
    """Zone setting identifier."""

    value: Literal["off", "on"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasSortQueryStringForCache(BaseModel):
    """
    Cloudflare will treat files with the same query strings as the same file in cache, regardless of the order of the query strings. This is limited to Enterprise Zones.
    """

    id: Literal["sort_query_string_for_cache"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasSSL(BaseModel):
    """
    SSL encrypts your visitor's connection and safeguards credit card numbers and other personal data to and from your website. SSL can take up to 5 minutes to fully activate. Requires Cloudflare active on your root domain or www domain. Off: no SSL between the visitor and Cloudflare, and no SSL between Cloudflare and your web server  (all HTTP traffic). Flexible: SSL between the visitor and Cloudflare -- visitor sees HTTPS on your site, but no SSL between Cloudflare and your web server. You don't need to have an SSL cert on your web server, but your vistors will still see the site as being HTTPS enabled. Full:  SSL between the visitor and Cloudflare -- visitor sees HTTPS on your site, and SSL between Cloudflare and your web server. You'll need to have your own SSL cert or self-signed cert at the very least. Full (Strict): SSL between the visitor and Cloudflare -- visitor sees HTTPS on your site, and SSL between Cloudflare and your web server. You'll need to have a valid SSL certificate installed on your web server. This certificate must be signed by a certificate authority, have an expiration date in the future, and respond for the request domain name (hostname). (https://support.cloudflare.com/hc/en-us/articles/200170416).
    """

    id: Literal["ssl"]
    """ID of the zone setting."""

    value: Literal["off", "flexible", "full", "strict"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesTLS1_2Only(BaseModel):
    """Only allows TLS1.2."""

    id: Literal["tls_1_2_only"]
    """Zone setting identifier."""

    value: Literal["off", "on"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesTransformations(BaseModel):
    """
    Media Transformations provides on-demand resizing, conversion and optimization for images and video served through Cloudflare's network. Refer to the [Image Transformations](https://developers.cloudflare.com/images/) and [Video Transformations](https://developers.cloudflare.com/stream/transform-videos/#getting-started) documentation for more information.
    """

    id: Literal["transformations"]
    """ID of the zone setting.

    Shared between Image Transformations and Video Transformations.
    """

    value: Literal["on", "off", "open"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesTransformationsAllowedOrigins(BaseModel):
    """
    Media Transformations Allowed Origins restricts transformations for images and video served through Cloudflare's network. Refer to the [Image Transformations](https://developers.cloudflare.com/images/) and [Video Transformations](https://developers.cloudflare.com/stream/transform-videos/#getting-started) documentation for more information.
    """

    id: Literal["transformations_allowed_origins"]
    """ID of the zone setting.

    Shared between Image Transformations and Video Transformations.
    """

    value: str
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasTrueClientIPHeader(BaseModel):
    """
    Allows customer to continue to use True Client IP (Akamai feature) in the headers we send to the origin. This is limited to Enterprise Zones.
    """

    id: Literal["true_client_ip_header"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class ZonesSchemasWAF(BaseModel):
    """The WAF examines HTTP requests to your website.

    It inspects both GET and POST requests and applies rules to help filter out illegitimate traffic from legitimate website visitors. The Cloudflare WAF inspects website addresses or URLs to detect anything out of the ordinary. If the Cloudflare WAF determines suspicious user behavior, then the WAF will 'challenge' the web visitor with a page that asks them to submit a CAPTCHA successfully  to continue their action. If the challenge is failed, the action will be stopped. What this means is that Cloudflare's WAF will block any traffic identified as illegitimate before it reaches your origin web server. (https://support.cloudflare.com/hc/en-us/articles/200172016).
    """

    id: Literal["waf"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


SettingGetResponse: TypeAlias = Union[
    ZeroRTT,
    AdvancedDDoS,
    ZonesCacheRulesAegis,
    AlwaysOnline,
    ZonesSchemasAlwaysUseHTTPS,
    ZonesSchemasAutomaticHTTPSRewrites,
    Brotli,
    ZonesSchemasBrowserCacheTTL,
    ZonesSchemasBrowserCheck,
    ZonesSchemasCacheLevel,
    ChallengeTTL,
    ZonesChinaNetworkEnabled,
    Ciphers,
    ZonesCNAMEFlattening,
    DevelopmentMode,
    EarlyHints,
    ZonesSchemasEdgeCacheTTL,
    ZonesSchemasEmailObfuscation,
    H2Prioritization,
    HotlinkProtection,
    HTTP2,
    HTTP3,
    ImageResizing,
    ZonesSchemasIPGeolocation,
    IPV6,
    ZonesMaxUpload,
    MinTLSVersion,
    ZonesSchemasMirage,
    NEL,
    ZonesSchemasOpportunisticEncryption,
    OpportunisticOnion,
    OrangeToOrange,
    ZonesSchemasOriginErrorPagePassThru,
    ZonesCacheRulesOriginH2MaxStreams,
    ZonesCacheRulesOriginMaxHTTPVersion,
    ZonesSchemasPolish,
    PrefetchPreload,
    ZonesPrivacyPass,
    ProxyReadTimeout,
    PseudoIPV4,
    ZonesReplaceInsecureJS,
    ZonesSchemasResponseBuffering,
    ZonesSchemasRocketLoader,
    ZonesSchemasAutomaticPlatformOptimization,
    SecurityHeaders,
    ZonesSchemasSecurityLevel,
    ServerSideExcludes,
    ZonesSha1Support,
    ZonesSchemasSortQueryStringForCache,
    ZonesSchemasSSL,
    SSLRecommender,
    ZonesTLS1_2Only,
    TLS1_3,
    TLSClientAuth,
    ZonesTransformations,
    ZonesTransformationsAllowedOrigins,
    ZonesSchemasTrueClientIPHeader,
    ZonesSchemasWAF,
    WebP,
    Websocket,
]
