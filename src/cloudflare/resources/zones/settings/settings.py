# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .nel import (
    NELResource,
    AsyncNELResource,
    NELResourceWithRawResponse,
    AsyncNELResourceWithRawResponse,
    NELResourceWithStreamingResponse,
    AsyncNELResourceWithStreamingResponse,
)
from .ssl import (
    SSLResource,
    AsyncSSLResource,
    SSLResourceWithRawResponse,
    AsyncSSLResourceWithRawResponse,
    SSLResourceWithStreamingResponse,
    AsyncSSLResourceWithStreamingResponse,
)
from .waf import (
    WAFResource,
    AsyncWAFResource,
    WAFResourceWithRawResponse,
    AsyncWAFResourceWithRawResponse,
    WAFResourceWithStreamingResponse,
    AsyncWAFResourceWithStreamingResponse,
)
from .ipv6 import (
    IPV6Resource,
    AsyncIPV6Resource,
    IPV6ResourceWithRawResponse,
    AsyncIPV6ResourceWithRawResponse,
    IPV6ResourceWithStreamingResponse,
    AsyncIPV6ResourceWithStreamingResponse,
)
from .webp import (
    WebPResource,
    AsyncWebPResource,
    WebPResourceWithRawResponse,
    AsyncWebPResourceWithRawResponse,
    WebPResourceWithStreamingResponse,
    AsyncWebPResourceWithStreamingResponse,
)
from .http2 import (
    HTTP2Resource,
    AsyncHTTP2Resource,
    HTTP2ResourceWithRawResponse,
    AsyncHTTP2ResourceWithRawResponse,
    HTTP2ResourceWithStreamingResponse,
    AsyncHTTP2ResourceWithStreamingResponse,
)
from .http3 import (
    HTTP3Resource,
    AsyncHTTP3Resource,
    HTTP3ResourceWithRawResponse,
    AsyncHTTP3ResourceWithRawResponse,
    HTTP3ResourceWithStreamingResponse,
    AsyncHTTP3ResourceWithStreamingResponse,
)
from .brotli import (
    BrotliResource,
    AsyncBrotliResource,
    BrotliResourceWithRawResponse,
    AsyncBrotliResourceWithRawResponse,
    BrotliResourceWithStreamingResponse,
    AsyncBrotliResourceWithStreamingResponse,
)
from .minify import (
    MinifyResource,
    AsyncMinifyResource,
    MinifyResourceWithRawResponse,
    AsyncMinifyResourceWithRawResponse,
    MinifyResourceWithStreamingResponse,
    AsyncMinifyResourceWithStreamingResponse,
)
from .mirage import (
    MirageResource,
    AsyncMirageResource,
    MirageResourceWithRawResponse,
    AsyncMirageResourceWithRawResponse,
    MirageResourceWithStreamingResponse,
    AsyncMirageResourceWithStreamingResponse,
)
from .polish import (
    PolishResource,
    AsyncPolishResource,
    PolishResourceWithRawResponse,
    AsyncPolishResourceWithRawResponse,
    PolishResourceWithStreamingResponse,
    AsyncPolishResourceWithStreamingResponse,
)
from .ciphers import (
    Ciphers,
    AsyncCiphers,
    CiphersWithRawResponse,
    AsyncCiphersWithRawResponse,
    CiphersWithStreamingResponse,
    AsyncCiphersWithStreamingResponse,
)
from .tls_1_3 import (
    TLS1_3Resource,
    AsyncTLS1_3Resource,
    TLS1_3ResourceWithRawResponse,
    AsyncTLS1_3ResourceWithRawResponse,
    TLS1_3ResourceWithStreamingResponse,
    AsyncTLS1_3ResourceWithStreamingResponse,
)
from .zero_rtt import (
    ZeroRTTResource,
    AsyncZeroRTTResource,
    ZeroRTTResourceWithRawResponse,
    AsyncZeroRTTResourceWithRawResponse,
    ZeroRTTResourceWithStreamingResponse,
    AsyncZeroRTTResourceWithStreamingResponse,
)
from .websocket import (
    WebsocketResource,
    AsyncWebsocketResource,
    WebsocketResourceWithRawResponse,
    AsyncWebsocketResourceWithRawResponse,
    WebsocketResourceWithStreamingResponse,
    AsyncWebsocketResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .cache_level import (
    CacheLevelResource,
    AsyncCacheLevelResource,
    CacheLevelResourceWithRawResponse,
    AsyncCacheLevelResourceWithRawResponse,
    CacheLevelResourceWithStreamingResponse,
    AsyncCacheLevelResourceWithStreamingResponse,
)
from .early_hints import (
    EarlyHints,
    AsyncEarlyHints,
    EarlyHintsWithRawResponse,
    AsyncEarlyHintsWithRawResponse,
    EarlyHintsWithStreamingResponse,
    AsyncEarlyHintsWithStreamingResponse,
)
from .pseudo_ipv4 import (
    PseudoIPV4Resource,
    AsyncPseudoIPV4Resource,
    PseudoIPV4ResourceWithRawResponse,
    AsyncPseudoIPV4ResourceWithRawResponse,
    PseudoIPV4ResourceWithStreamingResponse,
    AsyncPseudoIPV4ResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .advanced_ddos import (
    AdvancedDDoS,
    AsyncAdvancedDDoS,
    AdvancedDDoSWithRawResponse,
    AsyncAdvancedDDoSWithRawResponse,
    AdvancedDDoSWithStreamingResponse,
    AsyncAdvancedDDoSWithStreamingResponse,
)
from .always_online import (
    AlwaysOnlineResource,
    AsyncAlwaysOnlineResource,
    AlwaysOnlineResourceWithRawResponse,
    AsyncAlwaysOnlineResourceWithRawResponse,
    AlwaysOnlineResourceWithStreamingResponse,
    AsyncAlwaysOnlineResourceWithStreamingResponse,
)
from .browser_check import (
    BrowserCheckResource,
    AsyncBrowserCheckResource,
    BrowserCheckResourceWithRawResponse,
    AsyncBrowserCheckResourceWithRawResponse,
    BrowserCheckResourceWithStreamingResponse,
    AsyncBrowserCheckResourceWithStreamingResponse,
)
from .challenge_ttl import (
    ChallengeTTLResource,
    AsyncChallengeTTLResource,
    ChallengeTTLResourceWithRawResponse,
    AsyncChallengeTTLResourceWithRawResponse,
    ChallengeTTLResourceWithStreamingResponse,
    AsyncChallengeTTLResourceWithStreamingResponse,
)
from .font_settings import (
    FontSettings,
    AsyncFontSettings,
    FontSettingsWithRawResponse,
    AsyncFontSettingsWithRawResponse,
    FontSettingsWithStreamingResponse,
    AsyncFontSettingsWithStreamingResponse,
)
from .rocket_loader import (
    RocketLoaderResource,
    AsyncRocketLoaderResource,
    RocketLoaderResourceWithRawResponse,
    AsyncRocketLoaderResourceWithRawResponse,
    RocketLoaderResourceWithStreamingResponse,
    AsyncRocketLoaderResourceWithStreamingResponse,
)
from .image_resizing import (
    ImageResizingResource,
    AsyncImageResizingResource,
    ImageResizingResourceWithRawResponse,
    AsyncImageResizingResourceWithRawResponse,
    ImageResizingResourceWithStreamingResponse,
    AsyncImageResizingResourceWithStreamingResponse,
)
from .ip_geolocation import (
    IPGeolocationResource,
    AsyncIPGeolocationResource,
    IPGeolocationResourceWithRawResponse,
    AsyncIPGeolocationResourceWithRawResponse,
    IPGeolocationResourceWithStreamingResponse,
    AsyncIPGeolocationResourceWithStreamingResponse,
)
from .security_level import (
    SecurityLevelResource,
    AsyncSecurityLevelResource,
    SecurityLevelResourceWithRawResponse,
    AsyncSecurityLevelResourceWithRawResponse,
    SecurityLevelResourceWithStreamingResponse,
    AsyncSecurityLevelResourceWithStreamingResponse,
)
from .min_tls_version import (
    MinTLSVersionResource,
    AsyncMinTLSVersionResource,
    MinTLSVersionResourceWithRawResponse,
    AsyncMinTLSVersionResourceWithRawResponse,
    MinTLSVersionResourceWithStreamingResponse,
    AsyncMinTLSVersionResourceWithStreamingResponse,
)
from .mobile_redirect import (
    MobileRedirectResource,
    AsyncMobileRedirectResource,
    MobileRedirectResourceWithRawResponse,
    AsyncMobileRedirectResourceWithRawResponse,
    MobileRedirectResourceWithStreamingResponse,
    AsyncMobileRedirectResourceWithStreamingResponse,
)
from .ssl_recommender import (
    SSLRecommenderResource,
    AsyncSSLRecommenderResource,
    SSLRecommenderResourceWithRawResponse,
    AsyncSSLRecommenderResourceWithRawResponse,
    SSLRecommenderResourceWithStreamingResponse,
    AsyncSSLRecommenderResourceWithStreamingResponse,
)
from .tls_client_auth import (
    TLSClientAuthResource,
    AsyncTLSClientAuthResource,
    TLSClientAuthResourceWithRawResponse,
    AsyncTLSClientAuthResourceWithRawResponse,
    TLSClientAuthResourceWithStreamingResponse,
    AsyncTLSClientAuthResourceWithStreamingResponse,
)
from .always_use_https import (
    AlwaysUseHTTPS,
    AsyncAlwaysUseHTTPS,
    AlwaysUseHTTPSWithRawResponse,
    AsyncAlwaysUseHTTPSWithRawResponse,
    AlwaysUseHTTPSWithStreamingResponse,
    AsyncAlwaysUseHTTPSWithStreamingResponse,
)
from .development_mode import (
    DevelopmentModeResource,
    AsyncDevelopmentModeResource,
    DevelopmentModeResourceWithRawResponse,
    AsyncDevelopmentModeResourceWithRawResponse,
    DevelopmentModeResourceWithStreamingResponse,
    AsyncDevelopmentModeResourceWithStreamingResponse,
)
from .orange_to_orange import (
    OrangeToOrangeResource,
    AsyncOrangeToOrangeResource,
    OrangeToOrangeResourceWithRawResponse,
    AsyncOrangeToOrangeResourceWithRawResponse,
    OrangeToOrangeResourceWithStreamingResponse,
    AsyncOrangeToOrangeResourceWithStreamingResponse,
)
from .prefetch_preload import (
    PrefetchPreloadResource,
    AsyncPrefetchPreloadResource,
    PrefetchPreloadResourceWithRawResponse,
    AsyncPrefetchPreloadResourceWithRawResponse,
    PrefetchPreloadResourceWithStreamingResponse,
    AsyncPrefetchPreloadResourceWithStreamingResponse,
)
from .security_headers import (
    SecurityHeaders,
    AsyncSecurityHeaders,
    SecurityHeadersWithRawResponse,
    AsyncSecurityHeadersWithRawResponse,
    SecurityHeadersWithStreamingResponse,
    AsyncSecurityHeadersWithStreamingResponse,
)
from .browser_cache_ttl import (
    BrowserCacheTTLResource,
    AsyncBrowserCacheTTLResource,
    BrowserCacheTTLResourceWithRawResponse,
    AsyncBrowserCacheTTLResourceWithRawResponse,
    BrowserCacheTTLResourceWithStreamingResponse,
    AsyncBrowserCacheTTLResourceWithStreamingResponse,
)
from .email_obfuscation import (
    EmailObfuscationResource,
    AsyncEmailObfuscationResource,
    EmailObfuscationResourceWithRawResponse,
    AsyncEmailObfuscationResourceWithRawResponse,
    EmailObfuscationResourceWithStreamingResponse,
    AsyncEmailObfuscationResourceWithStreamingResponse,
)
from .h2_prioritization import (
    H2PrioritizationResource,
    AsyncH2PrioritizationResource,
    H2PrioritizationResourceWithRawResponse,
    AsyncH2PrioritizationResourceWithRawResponse,
    H2PrioritizationResourceWithStreamingResponse,
    AsyncH2PrioritizationResourceWithStreamingResponse,
)
from .hotlink_protection import (
    HotlinkProtectionResource,
    AsyncHotlinkProtectionResource,
    HotlinkProtectionResourceWithRawResponse,
    AsyncHotlinkProtectionResourceWithRawResponse,
    HotlinkProtectionResourceWithStreamingResponse,
    AsyncHotlinkProtectionResourceWithStreamingResponse,
)
from .proxy_read_timeout import (
    ProxyReadTimeoutResource,
    AsyncProxyReadTimeoutResource,
    ProxyReadTimeoutResourceWithRawResponse,
    AsyncProxyReadTimeoutResourceWithRawResponse,
    ProxyReadTimeoutResourceWithStreamingResponse,
    AsyncProxyReadTimeoutResourceWithStreamingResponse,
)
from .response_buffering import (
    ResponseBufferingResource,
    AsyncResponseBufferingResource,
    ResponseBufferingResourceWithRawResponse,
    AsyncResponseBufferingResourceWithRawResponse,
    ResponseBufferingResourceWithStreamingResponse,
    AsyncResponseBufferingResourceWithStreamingResponse,
)
from .opportunistic_onion import (
    OpportunisticOnionResource,
    AsyncOpportunisticOnionResource,
    OpportunisticOnionResourceWithRawResponse,
    AsyncOpportunisticOnionResourceWithRawResponse,
    OpportunisticOnionResourceWithStreamingResponse,
    AsyncOpportunisticOnionResourceWithStreamingResponse,
)
from .server_side_excludes import (
    ServerSideExcludes,
    AsyncServerSideExcludes,
    ServerSideExcludesWithRawResponse,
    AsyncServerSideExcludesWithRawResponse,
    ServerSideExcludesWithStreamingResponse,
    AsyncServerSideExcludesWithStreamingResponse,
)
from .true_client_ip_header import (
    TrueClientIPHeaderResource,
    AsyncTrueClientIPHeaderResource,
    TrueClientIPHeaderResourceWithRawResponse,
    AsyncTrueClientIPHeaderResourceWithRawResponse,
    TrueClientIPHeaderResourceWithStreamingResponse,
    AsyncTrueClientIPHeaderResourceWithStreamingResponse,
)
from .origin_max_http_version import (
    OriginMaxHTTPVersionResource,
    AsyncOriginMaxHTTPVersionResource,
    OriginMaxHTTPVersionResourceWithRawResponse,
    AsyncOriginMaxHTTPVersionResourceWithRawResponse,
    OriginMaxHTTPVersionResourceWithStreamingResponse,
    AsyncOriginMaxHTTPVersionResourceWithStreamingResponse,
)
from .automatic_https_rewrites import (
    AutomaticHTTPSRewrites,
    AsyncAutomaticHTTPSRewrites,
    AutomaticHTTPSRewritesWithRawResponse,
    AsyncAutomaticHTTPSRewritesWithRawResponse,
    AutomaticHTTPSRewritesWithStreamingResponse,
    AsyncAutomaticHTTPSRewritesWithStreamingResponse,
)
from .opportunistic_encryption import (
    OpportunisticEncryptionResource,
    AsyncOpportunisticEncryptionResource,
    OpportunisticEncryptionResourceWithRawResponse,
    AsyncOpportunisticEncryptionResourceWithRawResponse,
    OpportunisticEncryptionResourceWithStreamingResponse,
    AsyncOpportunisticEncryptionResourceWithStreamingResponse,
)
from .origin_error_page_pass_thru import (
    OriginErrorPagePassThruResource,
    AsyncOriginErrorPagePassThruResource,
    OriginErrorPagePassThruResourceWithRawResponse,
    AsyncOriginErrorPagePassThruResourceWithRawResponse,
    OriginErrorPagePassThruResourceWithStreamingResponse,
    AsyncOriginErrorPagePassThruResourceWithStreamingResponse,
)
from .sort_query_string_for_cache import (
    SortQueryStringForCacheResource,
    AsyncSortQueryStringForCacheResource,
    SortQueryStringForCacheResourceWithRawResponse,
    AsyncSortQueryStringForCacheResourceWithRawResponse,
    SortQueryStringForCacheResourceWithStreamingResponse,
    AsyncSortQueryStringForCacheResourceWithStreamingResponse,
)
from .automatic_platform_optimization import (
    AutomaticPlatformOptimizationResource,
    AsyncAutomaticPlatformOptimizationResource,
    AutomaticPlatformOptimizationResourceWithRawResponse,
    AsyncAutomaticPlatformOptimizationResourceWithRawResponse,
    AutomaticPlatformOptimizationResourceWithStreamingResponse,
    AsyncAutomaticPlatformOptimizationResourceWithStreamingResponse,
)

__all__ = ["Settings", "AsyncSettings"]


class Settings(SyncAPIResource):
    @cached_property
    def zero_rtt(self) -> ZeroRTTResource:
        return ZeroRTTResource(self._client)

    @cached_property
    def advanced_ddos(self) -> AdvancedDDoS:
        return AdvancedDDoS(self._client)

    @cached_property
    def always_online(self) -> AlwaysOnlineResource:
        return AlwaysOnlineResource(self._client)

    @cached_property
    def always_use_https(self) -> AlwaysUseHTTPS:
        return AlwaysUseHTTPS(self._client)

    @cached_property
    def automatic_https_rewrites(self) -> AutomaticHTTPSRewrites:
        return AutomaticHTTPSRewrites(self._client)

    @cached_property
    def automatic_platform_optimization(self) -> AutomaticPlatformOptimizationResource:
        return AutomaticPlatformOptimizationResource(self._client)

    @cached_property
    def brotli(self) -> BrotliResource:
        return BrotliResource(self._client)

    @cached_property
    def browser_cache_ttl(self) -> BrowserCacheTTLResource:
        return BrowserCacheTTLResource(self._client)

    @cached_property
    def browser_check(self) -> BrowserCheckResource:
        return BrowserCheckResource(self._client)

    @cached_property
    def cache_level(self) -> CacheLevelResource:
        return CacheLevelResource(self._client)

    @cached_property
    def challenge_ttl(self) -> ChallengeTTLResource:
        return ChallengeTTLResource(self._client)

    @cached_property
    def ciphers(self) -> Ciphers:
        return Ciphers(self._client)

    @cached_property
    def development_mode(self) -> DevelopmentModeResource:
        return DevelopmentModeResource(self._client)

    @cached_property
    def early_hints(self) -> EarlyHints:
        return EarlyHints(self._client)

    @cached_property
    def email_obfuscation(self) -> EmailObfuscationResource:
        return EmailObfuscationResource(self._client)

    @cached_property
    def h2_prioritization(self) -> H2PrioritizationResource:
        return H2PrioritizationResource(self._client)

    @cached_property
    def hotlink_protection(self) -> HotlinkProtectionResource:
        return HotlinkProtectionResource(self._client)

    @cached_property
    def http2(self) -> HTTP2Resource:
        return HTTP2Resource(self._client)

    @cached_property
    def http3(self) -> HTTP3Resource:
        return HTTP3Resource(self._client)

    @cached_property
    def image_resizing(self) -> ImageResizingResource:
        return ImageResizingResource(self._client)

    @cached_property
    def ip_geolocation(self) -> IPGeolocationResource:
        return IPGeolocationResource(self._client)

    @cached_property
    def ipv6(self) -> IPV6Resource:
        return IPV6Resource(self._client)

    @cached_property
    def min_tls_version(self) -> MinTLSVersionResource:
        return MinTLSVersionResource(self._client)

    @cached_property
    def minify(self) -> MinifyResource:
        return MinifyResource(self._client)

    @cached_property
    def mirage(self) -> MirageResource:
        return MirageResource(self._client)

    @cached_property
    def mobile_redirect(self) -> MobileRedirectResource:
        return MobileRedirectResource(self._client)

    @cached_property
    def nel(self) -> NELResource:
        return NELResource(self._client)

    @cached_property
    def opportunistic_encryption(self) -> OpportunisticEncryptionResource:
        return OpportunisticEncryptionResource(self._client)

    @cached_property
    def opportunistic_onion(self) -> OpportunisticOnionResource:
        return OpportunisticOnionResource(self._client)

    @cached_property
    def orange_to_orange(self) -> OrangeToOrangeResource:
        return OrangeToOrangeResource(self._client)

    @cached_property
    def origin_error_page_pass_thru(self) -> OriginErrorPagePassThruResource:
        return OriginErrorPagePassThruResource(self._client)

    @cached_property
    def origin_max_http_version(self) -> OriginMaxHTTPVersionResource:
        return OriginMaxHTTPVersionResource(self._client)

    @cached_property
    def polish(self) -> PolishResource:
        return PolishResource(self._client)

    @cached_property
    def prefetch_preload(self) -> PrefetchPreloadResource:
        return PrefetchPreloadResource(self._client)

    @cached_property
    def proxy_read_timeout(self) -> ProxyReadTimeoutResource:
        return ProxyReadTimeoutResource(self._client)

    @cached_property
    def pseudo_ipv4(self) -> PseudoIPV4Resource:
        return PseudoIPV4Resource(self._client)

    @cached_property
    def response_buffering(self) -> ResponseBufferingResource:
        return ResponseBufferingResource(self._client)

    @cached_property
    def rocket_loader(self) -> RocketLoaderResource:
        return RocketLoaderResource(self._client)

    @cached_property
    def security_headers(self) -> SecurityHeaders:
        return SecurityHeaders(self._client)

    @cached_property
    def security_level(self) -> SecurityLevelResource:
        return SecurityLevelResource(self._client)

    @cached_property
    def server_side_excludes(self) -> ServerSideExcludes:
        return ServerSideExcludes(self._client)

    @cached_property
    def sort_query_string_for_cache(self) -> SortQueryStringForCacheResource:
        return SortQueryStringForCacheResource(self._client)

    @cached_property
    def ssl(self) -> SSLResource:
        return SSLResource(self._client)

    @cached_property
    def ssl_recommender(self) -> SSLRecommenderResource:
        return SSLRecommenderResource(self._client)

    @cached_property
    def tls_1_3(self) -> TLS1_3Resource:
        return TLS1_3Resource(self._client)

    @cached_property
    def tls_client_auth(self) -> TLSClientAuthResource:
        return TLSClientAuthResource(self._client)

    @cached_property
    def true_client_ip_header(self) -> TrueClientIPHeaderResource:
        return TrueClientIPHeaderResource(self._client)

    @cached_property
    def waf(self) -> WAFResource:
        return WAFResource(self._client)

    @cached_property
    def webp(self) -> WebPResource:
        return WebPResource(self._client)

    @cached_property
    def websocket(self) -> WebsocketResource:
        return WebsocketResource(self._client)

    @cached_property
    def font_settings(self) -> FontSettings:
        return FontSettings(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self)


class AsyncSettings(AsyncAPIResource):
    @cached_property
    def zero_rtt(self) -> AsyncZeroRTTResource:
        return AsyncZeroRTTResource(self._client)

    @cached_property
    def advanced_ddos(self) -> AsyncAdvancedDDoS:
        return AsyncAdvancedDDoS(self._client)

    @cached_property
    def always_online(self) -> AsyncAlwaysOnlineResource:
        return AsyncAlwaysOnlineResource(self._client)

    @cached_property
    def always_use_https(self) -> AsyncAlwaysUseHTTPS:
        return AsyncAlwaysUseHTTPS(self._client)

    @cached_property
    def automatic_https_rewrites(self) -> AsyncAutomaticHTTPSRewrites:
        return AsyncAutomaticHTTPSRewrites(self._client)

    @cached_property
    def automatic_platform_optimization(self) -> AsyncAutomaticPlatformOptimizationResource:
        return AsyncAutomaticPlatformOptimizationResource(self._client)

    @cached_property
    def brotli(self) -> AsyncBrotliResource:
        return AsyncBrotliResource(self._client)

    @cached_property
    def browser_cache_ttl(self) -> AsyncBrowserCacheTTLResource:
        return AsyncBrowserCacheTTLResource(self._client)

    @cached_property
    def browser_check(self) -> AsyncBrowserCheckResource:
        return AsyncBrowserCheckResource(self._client)

    @cached_property
    def cache_level(self) -> AsyncCacheLevelResource:
        return AsyncCacheLevelResource(self._client)

    @cached_property
    def challenge_ttl(self) -> AsyncChallengeTTLResource:
        return AsyncChallengeTTLResource(self._client)

    @cached_property
    def ciphers(self) -> AsyncCiphers:
        return AsyncCiphers(self._client)

    @cached_property
    def development_mode(self) -> AsyncDevelopmentModeResource:
        return AsyncDevelopmentModeResource(self._client)

    @cached_property
    def early_hints(self) -> AsyncEarlyHints:
        return AsyncEarlyHints(self._client)

    @cached_property
    def email_obfuscation(self) -> AsyncEmailObfuscationResource:
        return AsyncEmailObfuscationResource(self._client)

    @cached_property
    def h2_prioritization(self) -> AsyncH2PrioritizationResource:
        return AsyncH2PrioritizationResource(self._client)

    @cached_property
    def hotlink_protection(self) -> AsyncHotlinkProtectionResource:
        return AsyncHotlinkProtectionResource(self._client)

    @cached_property
    def http2(self) -> AsyncHTTP2Resource:
        return AsyncHTTP2Resource(self._client)

    @cached_property
    def http3(self) -> AsyncHTTP3Resource:
        return AsyncHTTP3Resource(self._client)

    @cached_property
    def image_resizing(self) -> AsyncImageResizingResource:
        return AsyncImageResizingResource(self._client)

    @cached_property
    def ip_geolocation(self) -> AsyncIPGeolocationResource:
        return AsyncIPGeolocationResource(self._client)

    @cached_property
    def ipv6(self) -> AsyncIPV6Resource:
        return AsyncIPV6Resource(self._client)

    @cached_property
    def min_tls_version(self) -> AsyncMinTLSVersionResource:
        return AsyncMinTLSVersionResource(self._client)

    @cached_property
    def minify(self) -> AsyncMinifyResource:
        return AsyncMinifyResource(self._client)

    @cached_property
    def mirage(self) -> AsyncMirageResource:
        return AsyncMirageResource(self._client)

    @cached_property
    def mobile_redirect(self) -> AsyncMobileRedirectResource:
        return AsyncMobileRedirectResource(self._client)

    @cached_property
    def nel(self) -> AsyncNELResource:
        return AsyncNELResource(self._client)

    @cached_property
    def opportunistic_encryption(self) -> AsyncOpportunisticEncryptionResource:
        return AsyncOpportunisticEncryptionResource(self._client)

    @cached_property
    def opportunistic_onion(self) -> AsyncOpportunisticOnionResource:
        return AsyncOpportunisticOnionResource(self._client)

    @cached_property
    def orange_to_orange(self) -> AsyncOrangeToOrangeResource:
        return AsyncOrangeToOrangeResource(self._client)

    @cached_property
    def origin_error_page_pass_thru(self) -> AsyncOriginErrorPagePassThruResource:
        return AsyncOriginErrorPagePassThruResource(self._client)

    @cached_property
    def origin_max_http_version(self) -> AsyncOriginMaxHTTPVersionResource:
        return AsyncOriginMaxHTTPVersionResource(self._client)

    @cached_property
    def polish(self) -> AsyncPolishResource:
        return AsyncPolishResource(self._client)

    @cached_property
    def prefetch_preload(self) -> AsyncPrefetchPreloadResource:
        return AsyncPrefetchPreloadResource(self._client)

    @cached_property
    def proxy_read_timeout(self) -> AsyncProxyReadTimeoutResource:
        return AsyncProxyReadTimeoutResource(self._client)

    @cached_property
    def pseudo_ipv4(self) -> AsyncPseudoIPV4Resource:
        return AsyncPseudoIPV4Resource(self._client)

    @cached_property
    def response_buffering(self) -> AsyncResponseBufferingResource:
        return AsyncResponseBufferingResource(self._client)

    @cached_property
    def rocket_loader(self) -> AsyncRocketLoaderResource:
        return AsyncRocketLoaderResource(self._client)

    @cached_property
    def security_headers(self) -> AsyncSecurityHeaders:
        return AsyncSecurityHeaders(self._client)

    @cached_property
    def security_level(self) -> AsyncSecurityLevelResource:
        return AsyncSecurityLevelResource(self._client)

    @cached_property
    def server_side_excludes(self) -> AsyncServerSideExcludes:
        return AsyncServerSideExcludes(self._client)

    @cached_property
    def sort_query_string_for_cache(self) -> AsyncSortQueryStringForCacheResource:
        return AsyncSortQueryStringForCacheResource(self._client)

    @cached_property
    def ssl(self) -> AsyncSSLResource:
        return AsyncSSLResource(self._client)

    @cached_property
    def ssl_recommender(self) -> AsyncSSLRecommenderResource:
        return AsyncSSLRecommenderResource(self._client)

    @cached_property
    def tls_1_3(self) -> AsyncTLS1_3Resource:
        return AsyncTLS1_3Resource(self._client)

    @cached_property
    def tls_client_auth(self) -> AsyncTLSClientAuthResource:
        return AsyncTLSClientAuthResource(self._client)

    @cached_property
    def true_client_ip_header(self) -> AsyncTrueClientIPHeaderResource:
        return AsyncTrueClientIPHeaderResource(self._client)

    @cached_property
    def waf(self) -> AsyncWAFResource:
        return AsyncWAFResource(self._client)

    @cached_property
    def webp(self) -> AsyncWebPResource:
        return AsyncWebPResource(self._client)

    @cached_property
    def websocket(self) -> AsyncWebsocketResource:
        return AsyncWebsocketResource(self._client)

    @cached_property
    def font_settings(self) -> AsyncFontSettings:
        return AsyncFontSettings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self)


class SettingsWithRawResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    @cached_property
    def zero_rtt(self) -> ZeroRTTResourceWithRawResponse:
        return ZeroRTTResourceWithRawResponse(self._settings.zero_rtt)

    @cached_property
    def advanced_ddos(self) -> AdvancedDDoSWithRawResponse:
        return AdvancedDDoSWithRawResponse(self._settings.advanced_ddos)

    @cached_property
    def always_online(self) -> AlwaysOnlineResourceWithRawResponse:
        return AlwaysOnlineResourceWithRawResponse(self._settings.always_online)

    @cached_property
    def always_use_https(self) -> AlwaysUseHTTPSWithRawResponse:
        return AlwaysUseHTTPSWithRawResponse(self._settings.always_use_https)

    @cached_property
    def automatic_https_rewrites(self) -> AutomaticHTTPSRewritesWithRawResponse:
        return AutomaticHTTPSRewritesWithRawResponse(self._settings.automatic_https_rewrites)

    @cached_property
    def automatic_platform_optimization(self) -> AutomaticPlatformOptimizationResourceWithRawResponse:
        return AutomaticPlatformOptimizationResourceWithRawResponse(self._settings.automatic_platform_optimization)

    @cached_property
    def brotli(self) -> BrotliResourceWithRawResponse:
        return BrotliResourceWithRawResponse(self._settings.brotli)

    @cached_property
    def browser_cache_ttl(self) -> BrowserCacheTTLResourceWithRawResponse:
        return BrowserCacheTTLResourceWithRawResponse(self._settings.browser_cache_ttl)

    @cached_property
    def browser_check(self) -> BrowserCheckResourceWithRawResponse:
        return BrowserCheckResourceWithRawResponse(self._settings.browser_check)

    @cached_property
    def cache_level(self) -> CacheLevelResourceWithRawResponse:
        return CacheLevelResourceWithRawResponse(self._settings.cache_level)

    @cached_property
    def challenge_ttl(self) -> ChallengeTTLResourceWithRawResponse:
        return ChallengeTTLResourceWithRawResponse(self._settings.challenge_ttl)

    @cached_property
    def ciphers(self) -> CiphersWithRawResponse:
        return CiphersWithRawResponse(self._settings.ciphers)

    @cached_property
    def development_mode(self) -> DevelopmentModeResourceWithRawResponse:
        return DevelopmentModeResourceWithRawResponse(self._settings.development_mode)

    @cached_property
    def early_hints(self) -> EarlyHintsWithRawResponse:
        return EarlyHintsWithRawResponse(self._settings.early_hints)

    @cached_property
    def email_obfuscation(self) -> EmailObfuscationResourceWithRawResponse:
        return EmailObfuscationResourceWithRawResponse(self._settings.email_obfuscation)

    @cached_property
    def h2_prioritization(self) -> H2PrioritizationResourceWithRawResponse:
        return H2PrioritizationResourceWithRawResponse(self._settings.h2_prioritization)

    @cached_property
    def hotlink_protection(self) -> HotlinkProtectionResourceWithRawResponse:
        return HotlinkProtectionResourceWithRawResponse(self._settings.hotlink_protection)

    @cached_property
    def http2(self) -> HTTP2ResourceWithRawResponse:
        return HTTP2ResourceWithRawResponse(self._settings.http2)

    @cached_property
    def http3(self) -> HTTP3ResourceWithRawResponse:
        return HTTP3ResourceWithRawResponse(self._settings.http3)

    @cached_property
    def image_resizing(self) -> ImageResizingResourceWithRawResponse:
        return ImageResizingResourceWithRawResponse(self._settings.image_resizing)

    @cached_property
    def ip_geolocation(self) -> IPGeolocationResourceWithRawResponse:
        return IPGeolocationResourceWithRawResponse(self._settings.ip_geolocation)

    @cached_property
    def ipv6(self) -> IPV6ResourceWithRawResponse:
        return IPV6ResourceWithRawResponse(self._settings.ipv6)

    @cached_property
    def min_tls_version(self) -> MinTLSVersionResourceWithRawResponse:
        return MinTLSVersionResourceWithRawResponse(self._settings.min_tls_version)

    @cached_property
    def minify(self) -> MinifyResourceWithRawResponse:
        return MinifyResourceWithRawResponse(self._settings.minify)

    @cached_property
    def mirage(self) -> MirageResourceWithRawResponse:
        return MirageResourceWithRawResponse(self._settings.mirage)

    @cached_property
    def mobile_redirect(self) -> MobileRedirectResourceWithRawResponse:
        return MobileRedirectResourceWithRawResponse(self._settings.mobile_redirect)

    @cached_property
    def nel(self) -> NELResourceWithRawResponse:
        return NELResourceWithRawResponse(self._settings.nel)

    @cached_property
    def opportunistic_encryption(self) -> OpportunisticEncryptionResourceWithRawResponse:
        return OpportunisticEncryptionResourceWithRawResponse(self._settings.opportunistic_encryption)

    @cached_property
    def opportunistic_onion(self) -> OpportunisticOnionResourceWithRawResponse:
        return OpportunisticOnionResourceWithRawResponse(self._settings.opportunistic_onion)

    @cached_property
    def orange_to_orange(self) -> OrangeToOrangeResourceWithRawResponse:
        return OrangeToOrangeResourceWithRawResponse(self._settings.orange_to_orange)

    @cached_property
    def origin_error_page_pass_thru(self) -> OriginErrorPagePassThruResourceWithRawResponse:
        return OriginErrorPagePassThruResourceWithRawResponse(self._settings.origin_error_page_pass_thru)

    @cached_property
    def origin_max_http_version(self) -> OriginMaxHTTPVersionResourceWithRawResponse:
        return OriginMaxHTTPVersionResourceWithRawResponse(self._settings.origin_max_http_version)

    @cached_property
    def polish(self) -> PolishResourceWithRawResponse:
        return PolishResourceWithRawResponse(self._settings.polish)

    @cached_property
    def prefetch_preload(self) -> PrefetchPreloadResourceWithRawResponse:
        return PrefetchPreloadResourceWithRawResponse(self._settings.prefetch_preload)

    @cached_property
    def proxy_read_timeout(self) -> ProxyReadTimeoutResourceWithRawResponse:
        return ProxyReadTimeoutResourceWithRawResponse(self._settings.proxy_read_timeout)

    @cached_property
    def pseudo_ipv4(self) -> PseudoIPV4ResourceWithRawResponse:
        return PseudoIPV4ResourceWithRawResponse(self._settings.pseudo_ipv4)

    @cached_property
    def response_buffering(self) -> ResponseBufferingResourceWithRawResponse:
        return ResponseBufferingResourceWithRawResponse(self._settings.response_buffering)

    @cached_property
    def rocket_loader(self) -> RocketLoaderResourceWithRawResponse:
        return RocketLoaderResourceWithRawResponse(self._settings.rocket_loader)

    @cached_property
    def security_headers(self) -> SecurityHeadersWithRawResponse:
        return SecurityHeadersWithRawResponse(self._settings.security_headers)

    @cached_property
    def security_level(self) -> SecurityLevelResourceWithRawResponse:
        return SecurityLevelResourceWithRawResponse(self._settings.security_level)

    @cached_property
    def server_side_excludes(self) -> ServerSideExcludesWithRawResponse:
        return ServerSideExcludesWithRawResponse(self._settings.server_side_excludes)

    @cached_property
    def sort_query_string_for_cache(self) -> SortQueryStringForCacheResourceWithRawResponse:
        return SortQueryStringForCacheResourceWithRawResponse(self._settings.sort_query_string_for_cache)

    @cached_property
    def ssl(self) -> SSLResourceWithRawResponse:
        return SSLResourceWithRawResponse(self._settings.ssl)

    @cached_property
    def ssl_recommender(self) -> SSLRecommenderResourceWithRawResponse:
        return SSLRecommenderResourceWithRawResponse(self._settings.ssl_recommender)

    @cached_property
    def tls_1_3(self) -> TLS1_3ResourceWithRawResponse:
        return TLS1_3ResourceWithRawResponse(self._settings.tls_1_3)

    @cached_property
    def tls_client_auth(self) -> TLSClientAuthResourceWithRawResponse:
        return TLSClientAuthResourceWithRawResponse(self._settings.tls_client_auth)

    @cached_property
    def true_client_ip_header(self) -> TrueClientIPHeaderResourceWithRawResponse:
        return TrueClientIPHeaderResourceWithRawResponse(self._settings.true_client_ip_header)

    @cached_property
    def waf(self) -> WAFResourceWithRawResponse:
        return WAFResourceWithRawResponse(self._settings.waf)

    @cached_property
    def webp(self) -> WebPResourceWithRawResponse:
        return WebPResourceWithRawResponse(self._settings.webp)

    @cached_property
    def websocket(self) -> WebsocketResourceWithRawResponse:
        return WebsocketResourceWithRawResponse(self._settings.websocket)

    @cached_property
    def font_settings(self) -> FontSettingsWithRawResponse:
        return FontSettingsWithRawResponse(self._settings.font_settings)


class AsyncSettingsWithRawResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

    @cached_property
    def zero_rtt(self) -> AsyncZeroRTTResourceWithRawResponse:
        return AsyncZeroRTTResourceWithRawResponse(self._settings.zero_rtt)

    @cached_property
    def advanced_ddos(self) -> AsyncAdvancedDDoSWithRawResponse:
        return AsyncAdvancedDDoSWithRawResponse(self._settings.advanced_ddos)

    @cached_property
    def always_online(self) -> AsyncAlwaysOnlineResourceWithRawResponse:
        return AsyncAlwaysOnlineResourceWithRawResponse(self._settings.always_online)

    @cached_property
    def always_use_https(self) -> AsyncAlwaysUseHTTPSWithRawResponse:
        return AsyncAlwaysUseHTTPSWithRawResponse(self._settings.always_use_https)

    @cached_property
    def automatic_https_rewrites(self) -> AsyncAutomaticHTTPSRewritesWithRawResponse:
        return AsyncAutomaticHTTPSRewritesWithRawResponse(self._settings.automatic_https_rewrites)

    @cached_property
    def automatic_platform_optimization(self) -> AsyncAutomaticPlatformOptimizationResourceWithRawResponse:
        return AsyncAutomaticPlatformOptimizationResourceWithRawResponse(self._settings.automatic_platform_optimization)

    @cached_property
    def brotli(self) -> AsyncBrotliResourceWithRawResponse:
        return AsyncBrotliResourceWithRawResponse(self._settings.brotli)

    @cached_property
    def browser_cache_ttl(self) -> AsyncBrowserCacheTTLResourceWithRawResponse:
        return AsyncBrowserCacheTTLResourceWithRawResponse(self._settings.browser_cache_ttl)

    @cached_property
    def browser_check(self) -> AsyncBrowserCheckResourceWithRawResponse:
        return AsyncBrowserCheckResourceWithRawResponse(self._settings.browser_check)

    @cached_property
    def cache_level(self) -> AsyncCacheLevelResourceWithRawResponse:
        return AsyncCacheLevelResourceWithRawResponse(self._settings.cache_level)

    @cached_property
    def challenge_ttl(self) -> AsyncChallengeTTLResourceWithRawResponse:
        return AsyncChallengeTTLResourceWithRawResponse(self._settings.challenge_ttl)

    @cached_property
    def ciphers(self) -> AsyncCiphersWithRawResponse:
        return AsyncCiphersWithRawResponse(self._settings.ciphers)

    @cached_property
    def development_mode(self) -> AsyncDevelopmentModeResourceWithRawResponse:
        return AsyncDevelopmentModeResourceWithRawResponse(self._settings.development_mode)

    @cached_property
    def early_hints(self) -> AsyncEarlyHintsWithRawResponse:
        return AsyncEarlyHintsWithRawResponse(self._settings.early_hints)

    @cached_property
    def email_obfuscation(self) -> AsyncEmailObfuscationResourceWithRawResponse:
        return AsyncEmailObfuscationResourceWithRawResponse(self._settings.email_obfuscation)

    @cached_property
    def h2_prioritization(self) -> AsyncH2PrioritizationResourceWithRawResponse:
        return AsyncH2PrioritizationResourceWithRawResponse(self._settings.h2_prioritization)

    @cached_property
    def hotlink_protection(self) -> AsyncHotlinkProtectionResourceWithRawResponse:
        return AsyncHotlinkProtectionResourceWithRawResponse(self._settings.hotlink_protection)

    @cached_property
    def http2(self) -> AsyncHTTP2ResourceWithRawResponse:
        return AsyncHTTP2ResourceWithRawResponse(self._settings.http2)

    @cached_property
    def http3(self) -> AsyncHTTP3ResourceWithRawResponse:
        return AsyncHTTP3ResourceWithRawResponse(self._settings.http3)

    @cached_property
    def image_resizing(self) -> AsyncImageResizingResourceWithRawResponse:
        return AsyncImageResizingResourceWithRawResponse(self._settings.image_resizing)

    @cached_property
    def ip_geolocation(self) -> AsyncIPGeolocationResourceWithRawResponse:
        return AsyncIPGeolocationResourceWithRawResponse(self._settings.ip_geolocation)

    @cached_property
    def ipv6(self) -> AsyncIPV6ResourceWithRawResponse:
        return AsyncIPV6ResourceWithRawResponse(self._settings.ipv6)

    @cached_property
    def min_tls_version(self) -> AsyncMinTLSVersionResourceWithRawResponse:
        return AsyncMinTLSVersionResourceWithRawResponse(self._settings.min_tls_version)

    @cached_property
    def minify(self) -> AsyncMinifyResourceWithRawResponse:
        return AsyncMinifyResourceWithRawResponse(self._settings.minify)

    @cached_property
    def mirage(self) -> AsyncMirageResourceWithRawResponse:
        return AsyncMirageResourceWithRawResponse(self._settings.mirage)

    @cached_property
    def mobile_redirect(self) -> AsyncMobileRedirectResourceWithRawResponse:
        return AsyncMobileRedirectResourceWithRawResponse(self._settings.mobile_redirect)

    @cached_property
    def nel(self) -> AsyncNELResourceWithRawResponse:
        return AsyncNELResourceWithRawResponse(self._settings.nel)

    @cached_property
    def opportunistic_encryption(self) -> AsyncOpportunisticEncryptionResourceWithRawResponse:
        return AsyncOpportunisticEncryptionResourceWithRawResponse(self._settings.opportunistic_encryption)

    @cached_property
    def opportunistic_onion(self) -> AsyncOpportunisticOnionResourceWithRawResponse:
        return AsyncOpportunisticOnionResourceWithRawResponse(self._settings.opportunistic_onion)

    @cached_property
    def orange_to_orange(self) -> AsyncOrangeToOrangeResourceWithRawResponse:
        return AsyncOrangeToOrangeResourceWithRawResponse(self._settings.orange_to_orange)

    @cached_property
    def origin_error_page_pass_thru(self) -> AsyncOriginErrorPagePassThruResourceWithRawResponse:
        return AsyncOriginErrorPagePassThruResourceWithRawResponse(self._settings.origin_error_page_pass_thru)

    @cached_property
    def origin_max_http_version(self) -> AsyncOriginMaxHTTPVersionResourceWithRawResponse:
        return AsyncOriginMaxHTTPVersionResourceWithRawResponse(self._settings.origin_max_http_version)

    @cached_property
    def polish(self) -> AsyncPolishResourceWithRawResponse:
        return AsyncPolishResourceWithRawResponse(self._settings.polish)

    @cached_property
    def prefetch_preload(self) -> AsyncPrefetchPreloadResourceWithRawResponse:
        return AsyncPrefetchPreloadResourceWithRawResponse(self._settings.prefetch_preload)

    @cached_property
    def proxy_read_timeout(self) -> AsyncProxyReadTimeoutResourceWithRawResponse:
        return AsyncProxyReadTimeoutResourceWithRawResponse(self._settings.proxy_read_timeout)

    @cached_property
    def pseudo_ipv4(self) -> AsyncPseudoIPV4ResourceWithRawResponse:
        return AsyncPseudoIPV4ResourceWithRawResponse(self._settings.pseudo_ipv4)

    @cached_property
    def response_buffering(self) -> AsyncResponseBufferingResourceWithRawResponse:
        return AsyncResponseBufferingResourceWithRawResponse(self._settings.response_buffering)

    @cached_property
    def rocket_loader(self) -> AsyncRocketLoaderResourceWithRawResponse:
        return AsyncRocketLoaderResourceWithRawResponse(self._settings.rocket_loader)

    @cached_property
    def security_headers(self) -> AsyncSecurityHeadersWithRawResponse:
        return AsyncSecurityHeadersWithRawResponse(self._settings.security_headers)

    @cached_property
    def security_level(self) -> AsyncSecurityLevelResourceWithRawResponse:
        return AsyncSecurityLevelResourceWithRawResponse(self._settings.security_level)

    @cached_property
    def server_side_excludes(self) -> AsyncServerSideExcludesWithRawResponse:
        return AsyncServerSideExcludesWithRawResponse(self._settings.server_side_excludes)

    @cached_property
    def sort_query_string_for_cache(self) -> AsyncSortQueryStringForCacheResourceWithRawResponse:
        return AsyncSortQueryStringForCacheResourceWithRawResponse(self._settings.sort_query_string_for_cache)

    @cached_property
    def ssl(self) -> AsyncSSLResourceWithRawResponse:
        return AsyncSSLResourceWithRawResponse(self._settings.ssl)

    @cached_property
    def ssl_recommender(self) -> AsyncSSLRecommenderResourceWithRawResponse:
        return AsyncSSLRecommenderResourceWithRawResponse(self._settings.ssl_recommender)

    @cached_property
    def tls_1_3(self) -> AsyncTLS1_3ResourceWithRawResponse:
        return AsyncTLS1_3ResourceWithRawResponse(self._settings.tls_1_3)

    @cached_property
    def tls_client_auth(self) -> AsyncTLSClientAuthResourceWithRawResponse:
        return AsyncTLSClientAuthResourceWithRawResponse(self._settings.tls_client_auth)

    @cached_property
    def true_client_ip_header(self) -> AsyncTrueClientIPHeaderResourceWithRawResponse:
        return AsyncTrueClientIPHeaderResourceWithRawResponse(self._settings.true_client_ip_header)

    @cached_property
    def waf(self) -> AsyncWAFResourceWithRawResponse:
        return AsyncWAFResourceWithRawResponse(self._settings.waf)

    @cached_property
    def webp(self) -> AsyncWebPResourceWithRawResponse:
        return AsyncWebPResourceWithRawResponse(self._settings.webp)

    @cached_property
    def websocket(self) -> AsyncWebsocketResourceWithRawResponse:
        return AsyncWebsocketResourceWithRawResponse(self._settings.websocket)

    @cached_property
    def font_settings(self) -> AsyncFontSettingsWithRawResponse:
        return AsyncFontSettingsWithRawResponse(self._settings.font_settings)


class SettingsWithStreamingResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    @cached_property
    def zero_rtt(self) -> ZeroRTTResourceWithStreamingResponse:
        return ZeroRTTResourceWithStreamingResponse(self._settings.zero_rtt)

    @cached_property
    def advanced_ddos(self) -> AdvancedDDoSWithStreamingResponse:
        return AdvancedDDoSWithStreamingResponse(self._settings.advanced_ddos)

    @cached_property
    def always_online(self) -> AlwaysOnlineResourceWithStreamingResponse:
        return AlwaysOnlineResourceWithStreamingResponse(self._settings.always_online)

    @cached_property
    def always_use_https(self) -> AlwaysUseHTTPSWithStreamingResponse:
        return AlwaysUseHTTPSWithStreamingResponse(self._settings.always_use_https)

    @cached_property
    def automatic_https_rewrites(self) -> AutomaticHTTPSRewritesWithStreamingResponse:
        return AutomaticHTTPSRewritesWithStreamingResponse(self._settings.automatic_https_rewrites)

    @cached_property
    def automatic_platform_optimization(self) -> AutomaticPlatformOptimizationResourceWithStreamingResponse:
        return AutomaticPlatformOptimizationResourceWithStreamingResponse(
            self._settings.automatic_platform_optimization
        )

    @cached_property
    def brotli(self) -> BrotliResourceWithStreamingResponse:
        return BrotliResourceWithStreamingResponse(self._settings.brotli)

    @cached_property
    def browser_cache_ttl(self) -> BrowserCacheTTLResourceWithStreamingResponse:
        return BrowserCacheTTLResourceWithStreamingResponse(self._settings.browser_cache_ttl)

    @cached_property
    def browser_check(self) -> BrowserCheckResourceWithStreamingResponse:
        return BrowserCheckResourceWithStreamingResponse(self._settings.browser_check)

    @cached_property
    def cache_level(self) -> CacheLevelResourceWithStreamingResponse:
        return CacheLevelResourceWithStreamingResponse(self._settings.cache_level)

    @cached_property
    def challenge_ttl(self) -> ChallengeTTLResourceWithStreamingResponse:
        return ChallengeTTLResourceWithStreamingResponse(self._settings.challenge_ttl)

    @cached_property
    def ciphers(self) -> CiphersWithStreamingResponse:
        return CiphersWithStreamingResponse(self._settings.ciphers)

    @cached_property
    def development_mode(self) -> DevelopmentModeResourceWithStreamingResponse:
        return DevelopmentModeResourceWithStreamingResponse(self._settings.development_mode)

    @cached_property
    def early_hints(self) -> EarlyHintsWithStreamingResponse:
        return EarlyHintsWithStreamingResponse(self._settings.early_hints)

    @cached_property
    def email_obfuscation(self) -> EmailObfuscationResourceWithStreamingResponse:
        return EmailObfuscationResourceWithStreamingResponse(self._settings.email_obfuscation)

    @cached_property
    def h2_prioritization(self) -> H2PrioritizationResourceWithStreamingResponse:
        return H2PrioritizationResourceWithStreamingResponse(self._settings.h2_prioritization)

    @cached_property
    def hotlink_protection(self) -> HotlinkProtectionResourceWithStreamingResponse:
        return HotlinkProtectionResourceWithStreamingResponse(self._settings.hotlink_protection)

    @cached_property
    def http2(self) -> HTTP2ResourceWithStreamingResponse:
        return HTTP2ResourceWithStreamingResponse(self._settings.http2)

    @cached_property
    def http3(self) -> HTTP3ResourceWithStreamingResponse:
        return HTTP3ResourceWithStreamingResponse(self._settings.http3)

    @cached_property
    def image_resizing(self) -> ImageResizingResourceWithStreamingResponse:
        return ImageResizingResourceWithStreamingResponse(self._settings.image_resizing)

    @cached_property
    def ip_geolocation(self) -> IPGeolocationResourceWithStreamingResponse:
        return IPGeolocationResourceWithStreamingResponse(self._settings.ip_geolocation)

    @cached_property
    def ipv6(self) -> IPV6ResourceWithStreamingResponse:
        return IPV6ResourceWithStreamingResponse(self._settings.ipv6)

    @cached_property
    def min_tls_version(self) -> MinTLSVersionResourceWithStreamingResponse:
        return MinTLSVersionResourceWithStreamingResponse(self._settings.min_tls_version)

    @cached_property
    def minify(self) -> MinifyResourceWithStreamingResponse:
        return MinifyResourceWithStreamingResponse(self._settings.minify)

    @cached_property
    def mirage(self) -> MirageResourceWithStreamingResponse:
        return MirageResourceWithStreamingResponse(self._settings.mirage)

    @cached_property
    def mobile_redirect(self) -> MobileRedirectResourceWithStreamingResponse:
        return MobileRedirectResourceWithStreamingResponse(self._settings.mobile_redirect)

    @cached_property
    def nel(self) -> NELResourceWithStreamingResponse:
        return NELResourceWithStreamingResponse(self._settings.nel)

    @cached_property
    def opportunistic_encryption(self) -> OpportunisticEncryptionResourceWithStreamingResponse:
        return OpportunisticEncryptionResourceWithStreamingResponse(self._settings.opportunistic_encryption)

    @cached_property
    def opportunistic_onion(self) -> OpportunisticOnionResourceWithStreamingResponse:
        return OpportunisticOnionResourceWithStreamingResponse(self._settings.opportunistic_onion)

    @cached_property
    def orange_to_orange(self) -> OrangeToOrangeResourceWithStreamingResponse:
        return OrangeToOrangeResourceWithStreamingResponse(self._settings.orange_to_orange)

    @cached_property
    def origin_error_page_pass_thru(self) -> OriginErrorPagePassThruResourceWithStreamingResponse:
        return OriginErrorPagePassThruResourceWithStreamingResponse(self._settings.origin_error_page_pass_thru)

    @cached_property
    def origin_max_http_version(self) -> OriginMaxHTTPVersionResourceWithStreamingResponse:
        return OriginMaxHTTPVersionResourceWithStreamingResponse(self._settings.origin_max_http_version)

    @cached_property
    def polish(self) -> PolishResourceWithStreamingResponse:
        return PolishResourceWithStreamingResponse(self._settings.polish)

    @cached_property
    def prefetch_preload(self) -> PrefetchPreloadResourceWithStreamingResponse:
        return PrefetchPreloadResourceWithStreamingResponse(self._settings.prefetch_preload)

    @cached_property
    def proxy_read_timeout(self) -> ProxyReadTimeoutResourceWithStreamingResponse:
        return ProxyReadTimeoutResourceWithStreamingResponse(self._settings.proxy_read_timeout)

    @cached_property
    def pseudo_ipv4(self) -> PseudoIPV4ResourceWithStreamingResponse:
        return PseudoIPV4ResourceWithStreamingResponse(self._settings.pseudo_ipv4)

    @cached_property
    def response_buffering(self) -> ResponseBufferingResourceWithStreamingResponse:
        return ResponseBufferingResourceWithStreamingResponse(self._settings.response_buffering)

    @cached_property
    def rocket_loader(self) -> RocketLoaderResourceWithStreamingResponse:
        return RocketLoaderResourceWithStreamingResponse(self._settings.rocket_loader)

    @cached_property
    def security_headers(self) -> SecurityHeadersWithStreamingResponse:
        return SecurityHeadersWithStreamingResponse(self._settings.security_headers)

    @cached_property
    def security_level(self) -> SecurityLevelResourceWithStreamingResponse:
        return SecurityLevelResourceWithStreamingResponse(self._settings.security_level)

    @cached_property
    def server_side_excludes(self) -> ServerSideExcludesWithStreamingResponse:
        return ServerSideExcludesWithStreamingResponse(self._settings.server_side_excludes)

    @cached_property
    def sort_query_string_for_cache(self) -> SortQueryStringForCacheResourceWithStreamingResponse:
        return SortQueryStringForCacheResourceWithStreamingResponse(self._settings.sort_query_string_for_cache)

    @cached_property
    def ssl(self) -> SSLResourceWithStreamingResponse:
        return SSLResourceWithStreamingResponse(self._settings.ssl)

    @cached_property
    def ssl_recommender(self) -> SSLRecommenderResourceWithStreamingResponse:
        return SSLRecommenderResourceWithStreamingResponse(self._settings.ssl_recommender)

    @cached_property
    def tls_1_3(self) -> TLS1_3ResourceWithStreamingResponse:
        return TLS1_3ResourceWithStreamingResponse(self._settings.tls_1_3)

    @cached_property
    def tls_client_auth(self) -> TLSClientAuthResourceWithStreamingResponse:
        return TLSClientAuthResourceWithStreamingResponse(self._settings.tls_client_auth)

    @cached_property
    def true_client_ip_header(self) -> TrueClientIPHeaderResourceWithStreamingResponse:
        return TrueClientIPHeaderResourceWithStreamingResponse(self._settings.true_client_ip_header)

    @cached_property
    def waf(self) -> WAFResourceWithStreamingResponse:
        return WAFResourceWithStreamingResponse(self._settings.waf)

    @cached_property
    def webp(self) -> WebPResourceWithStreamingResponse:
        return WebPResourceWithStreamingResponse(self._settings.webp)

    @cached_property
    def websocket(self) -> WebsocketResourceWithStreamingResponse:
        return WebsocketResourceWithStreamingResponse(self._settings.websocket)

    @cached_property
    def font_settings(self) -> FontSettingsWithStreamingResponse:
        return FontSettingsWithStreamingResponse(self._settings.font_settings)


class AsyncSettingsWithStreamingResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

    @cached_property
    def zero_rtt(self) -> AsyncZeroRTTResourceWithStreamingResponse:
        return AsyncZeroRTTResourceWithStreamingResponse(self._settings.zero_rtt)

    @cached_property
    def advanced_ddos(self) -> AsyncAdvancedDDoSWithStreamingResponse:
        return AsyncAdvancedDDoSWithStreamingResponse(self._settings.advanced_ddos)

    @cached_property
    def always_online(self) -> AsyncAlwaysOnlineResourceWithStreamingResponse:
        return AsyncAlwaysOnlineResourceWithStreamingResponse(self._settings.always_online)

    @cached_property
    def always_use_https(self) -> AsyncAlwaysUseHTTPSWithStreamingResponse:
        return AsyncAlwaysUseHTTPSWithStreamingResponse(self._settings.always_use_https)

    @cached_property
    def automatic_https_rewrites(self) -> AsyncAutomaticHTTPSRewritesWithStreamingResponse:
        return AsyncAutomaticHTTPSRewritesWithStreamingResponse(self._settings.automatic_https_rewrites)

    @cached_property
    def automatic_platform_optimization(self) -> AsyncAutomaticPlatformOptimizationResourceWithStreamingResponse:
        return AsyncAutomaticPlatformOptimizationResourceWithStreamingResponse(
            self._settings.automatic_platform_optimization
        )

    @cached_property
    def brotli(self) -> AsyncBrotliResourceWithStreamingResponse:
        return AsyncBrotliResourceWithStreamingResponse(self._settings.brotli)

    @cached_property
    def browser_cache_ttl(self) -> AsyncBrowserCacheTTLResourceWithStreamingResponse:
        return AsyncBrowserCacheTTLResourceWithStreamingResponse(self._settings.browser_cache_ttl)

    @cached_property
    def browser_check(self) -> AsyncBrowserCheckResourceWithStreamingResponse:
        return AsyncBrowserCheckResourceWithStreamingResponse(self._settings.browser_check)

    @cached_property
    def cache_level(self) -> AsyncCacheLevelResourceWithStreamingResponse:
        return AsyncCacheLevelResourceWithStreamingResponse(self._settings.cache_level)

    @cached_property
    def challenge_ttl(self) -> AsyncChallengeTTLResourceWithStreamingResponse:
        return AsyncChallengeTTLResourceWithStreamingResponse(self._settings.challenge_ttl)

    @cached_property
    def ciphers(self) -> AsyncCiphersWithStreamingResponse:
        return AsyncCiphersWithStreamingResponse(self._settings.ciphers)

    @cached_property
    def development_mode(self) -> AsyncDevelopmentModeResourceWithStreamingResponse:
        return AsyncDevelopmentModeResourceWithStreamingResponse(self._settings.development_mode)

    @cached_property
    def early_hints(self) -> AsyncEarlyHintsWithStreamingResponse:
        return AsyncEarlyHintsWithStreamingResponse(self._settings.early_hints)

    @cached_property
    def email_obfuscation(self) -> AsyncEmailObfuscationResourceWithStreamingResponse:
        return AsyncEmailObfuscationResourceWithStreamingResponse(self._settings.email_obfuscation)

    @cached_property
    def h2_prioritization(self) -> AsyncH2PrioritizationResourceWithStreamingResponse:
        return AsyncH2PrioritizationResourceWithStreamingResponse(self._settings.h2_prioritization)

    @cached_property
    def hotlink_protection(self) -> AsyncHotlinkProtectionResourceWithStreamingResponse:
        return AsyncHotlinkProtectionResourceWithStreamingResponse(self._settings.hotlink_protection)

    @cached_property
    def http2(self) -> AsyncHTTP2ResourceWithStreamingResponse:
        return AsyncHTTP2ResourceWithStreamingResponse(self._settings.http2)

    @cached_property
    def http3(self) -> AsyncHTTP3ResourceWithStreamingResponse:
        return AsyncHTTP3ResourceWithStreamingResponse(self._settings.http3)

    @cached_property
    def image_resizing(self) -> AsyncImageResizingResourceWithStreamingResponse:
        return AsyncImageResizingResourceWithStreamingResponse(self._settings.image_resizing)

    @cached_property
    def ip_geolocation(self) -> AsyncIPGeolocationResourceWithStreamingResponse:
        return AsyncIPGeolocationResourceWithStreamingResponse(self._settings.ip_geolocation)

    @cached_property
    def ipv6(self) -> AsyncIPV6ResourceWithStreamingResponse:
        return AsyncIPV6ResourceWithStreamingResponse(self._settings.ipv6)

    @cached_property
    def min_tls_version(self) -> AsyncMinTLSVersionResourceWithStreamingResponse:
        return AsyncMinTLSVersionResourceWithStreamingResponse(self._settings.min_tls_version)

    @cached_property
    def minify(self) -> AsyncMinifyResourceWithStreamingResponse:
        return AsyncMinifyResourceWithStreamingResponse(self._settings.minify)

    @cached_property
    def mirage(self) -> AsyncMirageResourceWithStreamingResponse:
        return AsyncMirageResourceWithStreamingResponse(self._settings.mirage)

    @cached_property
    def mobile_redirect(self) -> AsyncMobileRedirectResourceWithStreamingResponse:
        return AsyncMobileRedirectResourceWithStreamingResponse(self._settings.mobile_redirect)

    @cached_property
    def nel(self) -> AsyncNELResourceWithStreamingResponse:
        return AsyncNELResourceWithStreamingResponse(self._settings.nel)

    @cached_property
    def opportunistic_encryption(self) -> AsyncOpportunisticEncryptionResourceWithStreamingResponse:
        return AsyncOpportunisticEncryptionResourceWithStreamingResponse(self._settings.opportunistic_encryption)

    @cached_property
    def opportunistic_onion(self) -> AsyncOpportunisticOnionResourceWithStreamingResponse:
        return AsyncOpportunisticOnionResourceWithStreamingResponse(self._settings.opportunistic_onion)

    @cached_property
    def orange_to_orange(self) -> AsyncOrangeToOrangeResourceWithStreamingResponse:
        return AsyncOrangeToOrangeResourceWithStreamingResponse(self._settings.orange_to_orange)

    @cached_property
    def origin_error_page_pass_thru(self) -> AsyncOriginErrorPagePassThruResourceWithStreamingResponse:
        return AsyncOriginErrorPagePassThruResourceWithStreamingResponse(self._settings.origin_error_page_pass_thru)

    @cached_property
    def origin_max_http_version(self) -> AsyncOriginMaxHTTPVersionResourceWithStreamingResponse:
        return AsyncOriginMaxHTTPVersionResourceWithStreamingResponse(self._settings.origin_max_http_version)

    @cached_property
    def polish(self) -> AsyncPolishResourceWithStreamingResponse:
        return AsyncPolishResourceWithStreamingResponse(self._settings.polish)

    @cached_property
    def prefetch_preload(self) -> AsyncPrefetchPreloadResourceWithStreamingResponse:
        return AsyncPrefetchPreloadResourceWithStreamingResponse(self._settings.prefetch_preload)

    @cached_property
    def proxy_read_timeout(self) -> AsyncProxyReadTimeoutResourceWithStreamingResponse:
        return AsyncProxyReadTimeoutResourceWithStreamingResponse(self._settings.proxy_read_timeout)

    @cached_property
    def pseudo_ipv4(self) -> AsyncPseudoIPV4ResourceWithStreamingResponse:
        return AsyncPseudoIPV4ResourceWithStreamingResponse(self._settings.pseudo_ipv4)

    @cached_property
    def response_buffering(self) -> AsyncResponseBufferingResourceWithStreamingResponse:
        return AsyncResponseBufferingResourceWithStreamingResponse(self._settings.response_buffering)

    @cached_property
    def rocket_loader(self) -> AsyncRocketLoaderResourceWithStreamingResponse:
        return AsyncRocketLoaderResourceWithStreamingResponse(self._settings.rocket_loader)

    @cached_property
    def security_headers(self) -> AsyncSecurityHeadersWithStreamingResponse:
        return AsyncSecurityHeadersWithStreamingResponse(self._settings.security_headers)

    @cached_property
    def security_level(self) -> AsyncSecurityLevelResourceWithStreamingResponse:
        return AsyncSecurityLevelResourceWithStreamingResponse(self._settings.security_level)

    @cached_property
    def server_side_excludes(self) -> AsyncServerSideExcludesWithStreamingResponse:
        return AsyncServerSideExcludesWithStreamingResponse(self._settings.server_side_excludes)

    @cached_property
    def sort_query_string_for_cache(self) -> AsyncSortQueryStringForCacheResourceWithStreamingResponse:
        return AsyncSortQueryStringForCacheResourceWithStreamingResponse(self._settings.sort_query_string_for_cache)

    @cached_property
    def ssl(self) -> AsyncSSLResourceWithStreamingResponse:
        return AsyncSSLResourceWithStreamingResponse(self._settings.ssl)

    @cached_property
    def ssl_recommender(self) -> AsyncSSLRecommenderResourceWithStreamingResponse:
        return AsyncSSLRecommenderResourceWithStreamingResponse(self._settings.ssl_recommender)

    @cached_property
    def tls_1_3(self) -> AsyncTLS1_3ResourceWithStreamingResponse:
        return AsyncTLS1_3ResourceWithStreamingResponse(self._settings.tls_1_3)

    @cached_property
    def tls_client_auth(self) -> AsyncTLSClientAuthResourceWithStreamingResponse:
        return AsyncTLSClientAuthResourceWithStreamingResponse(self._settings.tls_client_auth)

    @cached_property
    def true_client_ip_header(self) -> AsyncTrueClientIPHeaderResourceWithStreamingResponse:
        return AsyncTrueClientIPHeaderResourceWithStreamingResponse(self._settings.true_client_ip_header)

    @cached_property
    def waf(self) -> AsyncWAFResourceWithStreamingResponse:
        return AsyncWAFResourceWithStreamingResponse(self._settings.waf)

    @cached_property
    def webp(self) -> AsyncWebPResourceWithStreamingResponse:
        return AsyncWebPResourceWithStreamingResponse(self._settings.webp)

    @cached_property
    def websocket(self) -> AsyncWebsocketResourceWithStreamingResponse:
        return AsyncWebsocketResourceWithStreamingResponse(self._settings.websocket)

    @cached_property
    def font_settings(self) -> AsyncFontSettingsWithStreamingResponse:
        return AsyncFontSettingsWithStreamingResponse(self._settings.font_settings)
