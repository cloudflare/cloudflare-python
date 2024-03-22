# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from .nel import (
    NEL,
    AsyncNEL,
    NELWithRawResponse,
    AsyncNELWithRawResponse,
    NELWithStreamingResponse,
    AsyncNELWithStreamingResponse,
)
from .ssl import (
    SSL,
    AsyncSSL,
    SSLWithRawResponse,
    AsyncSSLWithRawResponse,
    SSLWithStreamingResponse,
    AsyncSSLWithStreamingResponse,
)
from .waf import (
    WAF,
    AsyncWAF,
    WAFWithRawResponse,
    AsyncWAFWithRawResponse,
    WAFWithStreamingResponse,
    AsyncWAFWithStreamingResponse,
)
from .ipv6 import (
    IPV6,
    AsyncIPV6,
    IPV6WithRawResponse,
    AsyncIPV6WithRawResponse,
    IPV6WithStreamingResponse,
    AsyncIPV6WithStreamingResponse,
)
from .webp import (
    WebP,
    AsyncWebP,
    WebPWithRawResponse,
    AsyncWebPWithRawResponse,
    WebPWithStreamingResponse,
    AsyncWebPWithStreamingResponse,
)
from .http2 import (
    HTTP2,
    AsyncHTTP2,
    HTTP2WithRawResponse,
    AsyncHTTP2WithRawResponse,
    HTTP2WithStreamingResponse,
    AsyncHTTP2WithStreamingResponse,
)
from .http3 import (
    HTTP3,
    AsyncHTTP3,
    HTTP3WithRawResponse,
    AsyncHTTP3WithRawResponse,
    HTTP3WithStreamingResponse,
    AsyncHTTP3WithStreamingResponse,
)
from .brotli import (
    Brotli,
    AsyncBrotli,
    BrotliWithRawResponse,
    AsyncBrotliWithRawResponse,
    BrotliWithStreamingResponse,
    AsyncBrotliWithStreamingResponse,
)
from .minify import (
    Minify,
    AsyncMinify,
    MinifyWithRawResponse,
    AsyncMinifyWithRawResponse,
    MinifyWithStreamingResponse,
    AsyncMinifyWithStreamingResponse,
)
from .mirage import (
    Mirage,
    AsyncMirage,
    MirageWithRawResponse,
    AsyncMirageWithRawResponse,
    MirageWithStreamingResponse,
    AsyncMirageWithStreamingResponse,
)
from .polish import (
    Polish,
    AsyncPolish,
    PolishWithRawResponse,
    AsyncPolishWithRawResponse,
    PolishWithStreamingResponse,
    AsyncPolishWithStreamingResponse,
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
    TLS1_3,
    AsyncTLS1_3,
    TLS1_3WithRawResponse,
    AsyncTLS1_3WithRawResponse,
    TLS1_3WithStreamingResponse,
    AsyncTLS1_3WithStreamingResponse,
)
from .zero_rtt import (
    ZeroRTT,
    AsyncZeroRTT,
    ZeroRTTWithRawResponse,
    AsyncZeroRTTWithRawResponse,
    ZeroRTTWithStreamingResponse,
    AsyncZeroRTTWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .websocket import (
    Websocket,
    AsyncWebsocket,
    WebsocketWithRawResponse,
    AsyncWebsocketWithRawResponse,
    WebsocketWithStreamingResponse,
    AsyncWebsocketWithStreamingResponse,
)
from ...._compat import cached_property
from .cache_level import (
    CacheLevel,
    AsyncCacheLevel,
    CacheLevelWithRawResponse,
    AsyncCacheLevelWithRawResponse,
    CacheLevelWithStreamingResponse,
    AsyncCacheLevelWithStreamingResponse,
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
    PseudoIPV4,
    AsyncPseudoIPV4,
    PseudoIPV4WithRawResponse,
    AsyncPseudoIPV4WithRawResponse,
    PseudoIPV4WithStreamingResponse,
    AsyncPseudoIPV4WithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from .advanced_ddos import (
    AdvancedDDOS,
    AsyncAdvancedDDOS,
    AdvancedDDOSWithRawResponse,
    AsyncAdvancedDDOSWithRawResponse,
    AdvancedDDOSWithStreamingResponse,
    AsyncAdvancedDDOSWithStreamingResponse,
)
from .always_online import (
    AlwaysOnline,
    AsyncAlwaysOnline,
    AlwaysOnlineWithRawResponse,
    AsyncAlwaysOnlineWithRawResponse,
    AlwaysOnlineWithStreamingResponse,
    AsyncAlwaysOnlineWithStreamingResponse,
)
from .browser_check import (
    BrowserCheck,
    AsyncBrowserCheck,
    BrowserCheckWithRawResponse,
    AsyncBrowserCheckWithRawResponse,
    BrowserCheckWithStreamingResponse,
    AsyncBrowserCheckWithStreamingResponse,
)
from .challenge_ttl import (
    ChallengeTTL,
    AsyncChallengeTTL,
    ChallengeTTLWithRawResponse,
    AsyncChallengeTTLWithRawResponse,
    ChallengeTTLWithStreamingResponse,
    AsyncChallengeTTLWithStreamingResponse,
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
    RocketLoader,
    AsyncRocketLoader,
    RocketLoaderWithRawResponse,
    AsyncRocketLoaderWithRawResponse,
    RocketLoaderWithStreamingResponse,
    AsyncRocketLoaderWithStreamingResponse,
)
from ....types.zones import SettingGetResponse, SettingEditResponse, setting_edit_params
from .image_resizing import (
    ImageResizing,
    AsyncImageResizing,
    ImageResizingWithRawResponse,
    AsyncImageResizingWithRawResponse,
    ImageResizingWithStreamingResponse,
    AsyncImageResizingWithStreamingResponse,
)
from .ip_geolocation import (
    IPGeolocation,
    AsyncIPGeolocation,
    IPGeolocationWithRawResponse,
    AsyncIPGeolocationWithRawResponse,
    IPGeolocationWithStreamingResponse,
    AsyncIPGeolocationWithStreamingResponse,
)
from .security_level import (
    SecurityLevel,
    AsyncSecurityLevel,
    SecurityLevelWithRawResponse,
    AsyncSecurityLevelWithRawResponse,
    SecurityLevelWithStreamingResponse,
    AsyncSecurityLevelWithStreamingResponse,
)
from ...._base_client import (
    make_request_options,
)
from .min_tls_version import (
    MinTLSVersion,
    AsyncMinTLSVersion,
    MinTLSVersionWithRawResponse,
    AsyncMinTLSVersionWithRawResponse,
    MinTLSVersionWithStreamingResponse,
    AsyncMinTLSVersionWithStreamingResponse,
)
from .mobile_redirect import (
    MobileRedirect,
    AsyncMobileRedirect,
    MobileRedirectWithRawResponse,
    AsyncMobileRedirectWithRawResponse,
    MobileRedirectWithStreamingResponse,
    AsyncMobileRedirectWithStreamingResponse,
)
from .ssl_recommender import (
    SSLRecommender,
    AsyncSSLRecommender,
    SSLRecommenderWithRawResponse,
    AsyncSSLRecommenderWithRawResponse,
    SSLRecommenderWithStreamingResponse,
    AsyncSSLRecommenderWithStreamingResponse,
)
from .tls_client_auth import (
    TLSClientAuth,
    AsyncTLSClientAuth,
    TLSClientAuthWithRawResponse,
    AsyncTLSClientAuthWithRawResponse,
    TLSClientAuthWithStreamingResponse,
    AsyncTLSClientAuthWithStreamingResponse,
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
    DevelopmentMode,
    AsyncDevelopmentMode,
    DevelopmentModeWithRawResponse,
    AsyncDevelopmentModeWithRawResponse,
    DevelopmentModeWithStreamingResponse,
    AsyncDevelopmentModeWithStreamingResponse,
)
from .orange_to_orange import (
    OrangeToOrange,
    AsyncOrangeToOrange,
    OrangeToOrangeWithRawResponse,
    AsyncOrangeToOrangeWithRawResponse,
    OrangeToOrangeWithStreamingResponse,
    AsyncOrangeToOrangeWithStreamingResponse,
)
from .prefetch_preload import (
    PrefetchPreload,
    AsyncPrefetchPreload,
    PrefetchPreloadWithRawResponse,
    AsyncPrefetchPreloadWithRawResponse,
    PrefetchPreloadWithStreamingResponse,
    AsyncPrefetchPreloadWithStreamingResponse,
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
    BrowserCacheTTL,
    AsyncBrowserCacheTTL,
    BrowserCacheTTLWithRawResponse,
    AsyncBrowserCacheTTLWithRawResponse,
    BrowserCacheTTLWithStreamingResponse,
    AsyncBrowserCacheTTLWithStreamingResponse,
)
from .email_obfuscation import (
    EmailObfuscation,
    AsyncEmailObfuscation,
    EmailObfuscationWithRawResponse,
    AsyncEmailObfuscationWithRawResponse,
    EmailObfuscationWithStreamingResponse,
    AsyncEmailObfuscationWithStreamingResponse,
)
from .h2_prioritization import (
    H2Prioritization,
    AsyncH2Prioritization,
    H2PrioritizationWithRawResponse,
    AsyncH2PrioritizationWithRawResponse,
    H2PrioritizationWithStreamingResponse,
    AsyncH2PrioritizationWithStreamingResponse,
)
from .hotlink_protection import (
    HotlinkProtection,
    AsyncHotlinkProtection,
    HotlinkProtectionWithRawResponse,
    AsyncHotlinkProtectionWithRawResponse,
    HotlinkProtectionWithStreamingResponse,
    AsyncHotlinkProtectionWithStreamingResponse,
)
from .proxy_read_timeout import (
    ProxyReadTimeout,
    AsyncProxyReadTimeout,
    ProxyReadTimeoutWithRawResponse,
    AsyncProxyReadTimeoutWithRawResponse,
    ProxyReadTimeoutWithStreamingResponse,
    AsyncProxyReadTimeoutWithStreamingResponse,
)
from .response_buffering import (
    ResponseBuffering,
    AsyncResponseBuffering,
    ResponseBufferingWithRawResponse,
    AsyncResponseBufferingWithRawResponse,
    ResponseBufferingWithStreamingResponse,
    AsyncResponseBufferingWithStreamingResponse,
)
from .opportunistic_onion import (
    OpportunisticOnion,
    AsyncOpportunisticOnion,
    OpportunisticOnionWithRawResponse,
    AsyncOpportunisticOnionWithRawResponse,
    OpportunisticOnionWithStreamingResponse,
    AsyncOpportunisticOnionWithStreamingResponse,
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
    TrueClientIPHeader,
    AsyncTrueClientIPHeader,
    TrueClientIPHeaderWithRawResponse,
    AsyncTrueClientIPHeaderWithRawResponse,
    TrueClientIPHeaderWithStreamingResponse,
    AsyncTrueClientIPHeaderWithStreamingResponse,
)
from .origin_max_http_version import (
    OriginMaxHTTPVersion,
    AsyncOriginMaxHTTPVersion,
    OriginMaxHTTPVersionWithRawResponse,
    AsyncOriginMaxHTTPVersionWithRawResponse,
    OriginMaxHTTPVersionWithStreamingResponse,
    AsyncOriginMaxHTTPVersionWithStreamingResponse,
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
    OpportunisticEncryption,
    AsyncOpportunisticEncryption,
    OpportunisticEncryptionWithRawResponse,
    AsyncOpportunisticEncryptionWithRawResponse,
    OpportunisticEncryptionWithStreamingResponse,
    AsyncOpportunisticEncryptionWithStreamingResponse,
)
from .origin_error_page_pass_thru import (
    OriginErrorPagePassThru,
    AsyncOriginErrorPagePassThru,
    OriginErrorPagePassThruWithRawResponse,
    AsyncOriginErrorPagePassThruWithRawResponse,
    OriginErrorPagePassThruWithStreamingResponse,
    AsyncOriginErrorPagePassThruWithStreamingResponse,
)
from .sort_query_string_for_cache import (
    SortQueryStringForCache,
    AsyncSortQueryStringForCache,
    SortQueryStringForCacheWithRawResponse,
    AsyncSortQueryStringForCacheWithRawResponse,
    SortQueryStringForCacheWithStreamingResponse,
    AsyncSortQueryStringForCacheWithStreamingResponse,
)
from .automatic_platform_optimization import (
    AutomaticPlatformOptimization,
    AsyncAutomaticPlatformOptimization,
    AutomaticPlatformOptimizationWithRawResponse,
    AsyncAutomaticPlatformOptimizationWithRawResponse,
    AutomaticPlatformOptimizationWithStreamingResponse,
    AsyncAutomaticPlatformOptimizationWithStreamingResponse,
)

__all__ = ["Settings", "AsyncSettings"]


class Settings(SyncAPIResource):
    @cached_property
    def zero_rtt(self) -> ZeroRTT:
        return ZeroRTT(self._client)

    @cached_property
    def advanced_ddos(self) -> AdvancedDDOS:
        return AdvancedDDOS(self._client)

    @cached_property
    def always_online(self) -> AlwaysOnline:
        return AlwaysOnline(self._client)

    @cached_property
    def always_use_https(self) -> AlwaysUseHTTPS:
        return AlwaysUseHTTPS(self._client)

    @cached_property
    def automatic_https_rewrites(self) -> AutomaticHTTPSRewrites:
        return AutomaticHTTPSRewrites(self._client)

    @cached_property
    def automatic_platform_optimization(self) -> AutomaticPlatformOptimization:
        return AutomaticPlatformOptimization(self._client)

    @cached_property
    def brotli(self) -> Brotli:
        return Brotli(self._client)

    @cached_property
    def browser_cache_ttl(self) -> BrowserCacheTTL:
        return BrowserCacheTTL(self._client)

    @cached_property
    def browser_check(self) -> BrowserCheck:
        return BrowserCheck(self._client)

    @cached_property
    def cache_level(self) -> CacheLevel:
        return CacheLevel(self._client)

    @cached_property
    def challenge_ttl(self) -> ChallengeTTL:
        return ChallengeTTL(self._client)

    @cached_property
    def ciphers(self) -> Ciphers:
        return Ciphers(self._client)

    @cached_property
    def development_mode(self) -> DevelopmentMode:
        return DevelopmentMode(self._client)

    @cached_property
    def early_hints(self) -> EarlyHints:
        return EarlyHints(self._client)

    @cached_property
    def email_obfuscation(self) -> EmailObfuscation:
        return EmailObfuscation(self._client)

    @cached_property
    def h2_prioritization(self) -> H2Prioritization:
        return H2Prioritization(self._client)

    @cached_property
    def hotlink_protection(self) -> HotlinkProtection:
        return HotlinkProtection(self._client)

    @cached_property
    def http2(self) -> HTTP2:
        return HTTP2(self._client)

    @cached_property
    def http3(self) -> HTTP3:
        return HTTP3(self._client)

    @cached_property
    def image_resizing(self) -> ImageResizing:
        return ImageResizing(self._client)

    @cached_property
    def ip_geolocation(self) -> IPGeolocation:
        return IPGeolocation(self._client)

    @cached_property
    def ipv6(self) -> IPV6:
        return IPV6(self._client)

    @cached_property
    def min_tls_version(self) -> MinTLSVersion:
        return MinTLSVersion(self._client)

    @cached_property
    def minify(self) -> Minify:
        return Minify(self._client)

    @cached_property
    def mirage(self) -> Mirage:
        return Mirage(self._client)

    @cached_property
    def mobile_redirect(self) -> MobileRedirect:
        return MobileRedirect(self._client)

    @cached_property
    def nel(self) -> NEL:
        return NEL(self._client)

    @cached_property
    def opportunistic_encryption(self) -> OpportunisticEncryption:
        return OpportunisticEncryption(self._client)

    @cached_property
    def opportunistic_onion(self) -> OpportunisticOnion:
        return OpportunisticOnion(self._client)

    @cached_property
    def orange_to_orange(self) -> OrangeToOrange:
        return OrangeToOrange(self._client)

    @cached_property
    def origin_error_page_pass_thru(self) -> OriginErrorPagePassThru:
        return OriginErrorPagePassThru(self._client)

    @cached_property
    def origin_max_http_version(self) -> OriginMaxHTTPVersion:
        return OriginMaxHTTPVersion(self._client)

    @cached_property
    def polish(self) -> Polish:
        return Polish(self._client)

    @cached_property
    def prefetch_preload(self) -> PrefetchPreload:
        return PrefetchPreload(self._client)

    @cached_property
    def proxy_read_timeout(self) -> ProxyReadTimeout:
        return ProxyReadTimeout(self._client)

    @cached_property
    def pseudo_ipv4(self) -> PseudoIPV4:
        return PseudoIPV4(self._client)

    @cached_property
    def response_buffering(self) -> ResponseBuffering:
        return ResponseBuffering(self._client)

    @cached_property
    def rocket_loader(self) -> RocketLoader:
        return RocketLoader(self._client)

    @cached_property
    def security_headers(self) -> SecurityHeaders:
        return SecurityHeaders(self._client)

    @cached_property
    def security_level(self) -> SecurityLevel:
        return SecurityLevel(self._client)

    @cached_property
    def server_side_excludes(self) -> ServerSideExcludes:
        return ServerSideExcludes(self._client)

    @cached_property
    def sort_query_string_for_cache(self) -> SortQueryStringForCache:
        return SortQueryStringForCache(self._client)

    @cached_property
    def ssl(self) -> SSL:
        return SSL(self._client)

    @cached_property
    def ssl_recommender(self) -> SSLRecommender:
        return SSLRecommender(self._client)

    @cached_property
    def tls_1_3(self) -> TLS1_3:
        return TLS1_3(self._client)

    @cached_property
    def tls_client_auth(self) -> TLSClientAuth:
        return TLSClientAuth(self._client)

    @cached_property
    def true_client_ip_header(self) -> TrueClientIPHeader:
        return TrueClientIPHeader(self._client)

    @cached_property
    def waf(self) -> WAF:
        return WAF(self._client)

    @cached_property
    def webp(self) -> WebP:
        return WebP(self._client)

    @cached_property
    def websocket(self) -> Websocket:
        return Websocket(self._client)

    @cached_property
    def font_settings(self) -> FontSettings:
        return FontSettings(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        items: Iterable[setting_edit_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Edit settings for a zone.

        Args:
          zone_id: Identifier

          items: One or more zone setting objects. Must contain an ID and a value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings",
            body=maybe_transform({"items": items}, setting_edit_params.SettingEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SettingEditResponse]], ResultWrapper[SettingEditResponse]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingGetResponse]:
        """
        Available settings for your user in relation to a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SettingGetResponse]], ResultWrapper[SettingGetResponse]),
        )


class AsyncSettings(AsyncAPIResource):
    @cached_property
    def zero_rtt(self) -> AsyncZeroRTT:
        return AsyncZeroRTT(self._client)

    @cached_property
    def advanced_ddos(self) -> AsyncAdvancedDDOS:
        return AsyncAdvancedDDOS(self._client)

    @cached_property
    def always_online(self) -> AsyncAlwaysOnline:
        return AsyncAlwaysOnline(self._client)

    @cached_property
    def always_use_https(self) -> AsyncAlwaysUseHTTPS:
        return AsyncAlwaysUseHTTPS(self._client)

    @cached_property
    def automatic_https_rewrites(self) -> AsyncAutomaticHTTPSRewrites:
        return AsyncAutomaticHTTPSRewrites(self._client)

    @cached_property
    def automatic_platform_optimization(self) -> AsyncAutomaticPlatformOptimization:
        return AsyncAutomaticPlatformOptimization(self._client)

    @cached_property
    def brotli(self) -> AsyncBrotli:
        return AsyncBrotli(self._client)

    @cached_property
    def browser_cache_ttl(self) -> AsyncBrowserCacheTTL:
        return AsyncBrowserCacheTTL(self._client)

    @cached_property
    def browser_check(self) -> AsyncBrowserCheck:
        return AsyncBrowserCheck(self._client)

    @cached_property
    def cache_level(self) -> AsyncCacheLevel:
        return AsyncCacheLevel(self._client)

    @cached_property
    def challenge_ttl(self) -> AsyncChallengeTTL:
        return AsyncChallengeTTL(self._client)

    @cached_property
    def ciphers(self) -> AsyncCiphers:
        return AsyncCiphers(self._client)

    @cached_property
    def development_mode(self) -> AsyncDevelopmentMode:
        return AsyncDevelopmentMode(self._client)

    @cached_property
    def early_hints(self) -> AsyncEarlyHints:
        return AsyncEarlyHints(self._client)

    @cached_property
    def email_obfuscation(self) -> AsyncEmailObfuscation:
        return AsyncEmailObfuscation(self._client)

    @cached_property
    def h2_prioritization(self) -> AsyncH2Prioritization:
        return AsyncH2Prioritization(self._client)

    @cached_property
    def hotlink_protection(self) -> AsyncHotlinkProtection:
        return AsyncHotlinkProtection(self._client)

    @cached_property
    def http2(self) -> AsyncHTTP2:
        return AsyncHTTP2(self._client)

    @cached_property
    def http3(self) -> AsyncHTTP3:
        return AsyncHTTP3(self._client)

    @cached_property
    def image_resizing(self) -> AsyncImageResizing:
        return AsyncImageResizing(self._client)

    @cached_property
    def ip_geolocation(self) -> AsyncIPGeolocation:
        return AsyncIPGeolocation(self._client)

    @cached_property
    def ipv6(self) -> AsyncIPV6:
        return AsyncIPV6(self._client)

    @cached_property
    def min_tls_version(self) -> AsyncMinTLSVersion:
        return AsyncMinTLSVersion(self._client)

    @cached_property
    def minify(self) -> AsyncMinify:
        return AsyncMinify(self._client)

    @cached_property
    def mirage(self) -> AsyncMirage:
        return AsyncMirage(self._client)

    @cached_property
    def mobile_redirect(self) -> AsyncMobileRedirect:
        return AsyncMobileRedirect(self._client)

    @cached_property
    def nel(self) -> AsyncNEL:
        return AsyncNEL(self._client)

    @cached_property
    def opportunistic_encryption(self) -> AsyncOpportunisticEncryption:
        return AsyncOpportunisticEncryption(self._client)

    @cached_property
    def opportunistic_onion(self) -> AsyncOpportunisticOnion:
        return AsyncOpportunisticOnion(self._client)

    @cached_property
    def orange_to_orange(self) -> AsyncOrangeToOrange:
        return AsyncOrangeToOrange(self._client)

    @cached_property
    def origin_error_page_pass_thru(self) -> AsyncOriginErrorPagePassThru:
        return AsyncOriginErrorPagePassThru(self._client)

    @cached_property
    def origin_max_http_version(self) -> AsyncOriginMaxHTTPVersion:
        return AsyncOriginMaxHTTPVersion(self._client)

    @cached_property
    def polish(self) -> AsyncPolish:
        return AsyncPolish(self._client)

    @cached_property
    def prefetch_preload(self) -> AsyncPrefetchPreload:
        return AsyncPrefetchPreload(self._client)

    @cached_property
    def proxy_read_timeout(self) -> AsyncProxyReadTimeout:
        return AsyncProxyReadTimeout(self._client)

    @cached_property
    def pseudo_ipv4(self) -> AsyncPseudoIPV4:
        return AsyncPseudoIPV4(self._client)

    @cached_property
    def response_buffering(self) -> AsyncResponseBuffering:
        return AsyncResponseBuffering(self._client)

    @cached_property
    def rocket_loader(self) -> AsyncRocketLoader:
        return AsyncRocketLoader(self._client)

    @cached_property
    def security_headers(self) -> AsyncSecurityHeaders:
        return AsyncSecurityHeaders(self._client)

    @cached_property
    def security_level(self) -> AsyncSecurityLevel:
        return AsyncSecurityLevel(self._client)

    @cached_property
    def server_side_excludes(self) -> AsyncServerSideExcludes:
        return AsyncServerSideExcludes(self._client)

    @cached_property
    def sort_query_string_for_cache(self) -> AsyncSortQueryStringForCache:
        return AsyncSortQueryStringForCache(self._client)

    @cached_property
    def ssl(self) -> AsyncSSL:
        return AsyncSSL(self._client)

    @cached_property
    def ssl_recommender(self) -> AsyncSSLRecommender:
        return AsyncSSLRecommender(self._client)

    @cached_property
    def tls_1_3(self) -> AsyncTLS1_3:
        return AsyncTLS1_3(self._client)

    @cached_property
    def tls_client_auth(self) -> AsyncTLSClientAuth:
        return AsyncTLSClientAuth(self._client)

    @cached_property
    def true_client_ip_header(self) -> AsyncTrueClientIPHeader:
        return AsyncTrueClientIPHeader(self._client)

    @cached_property
    def waf(self) -> AsyncWAF:
        return AsyncWAF(self._client)

    @cached_property
    def webp(self) -> AsyncWebP:
        return AsyncWebP(self._client)

    @cached_property
    def websocket(self) -> AsyncWebsocket:
        return AsyncWebsocket(self._client)

    @cached_property
    def font_settings(self) -> AsyncFontSettings:
        return AsyncFontSettings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        items: Iterable[setting_edit_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Edit settings for a zone.

        Args:
          zone_id: Identifier

          items: One or more zone setting objects. Must contain an ID and a value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings",
            body=await async_maybe_transform({"items": items}, setting_edit_params.SettingEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SettingEditResponse]], ResultWrapper[SettingEditResponse]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingGetResponse]:
        """
        Available settings for your user in relation to a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SettingGetResponse]], ResultWrapper[SettingGetResponse]),
        )


class SettingsWithRawResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

        self.edit = to_raw_response_wrapper(
            settings.edit,
        )
        self.get = to_raw_response_wrapper(
            settings.get,
        )

    @cached_property
    def zero_rtt(self) -> ZeroRTTWithRawResponse:
        return ZeroRTTWithRawResponse(self._settings.zero_rtt)

    @cached_property
    def advanced_ddos(self) -> AdvancedDDOSWithRawResponse:
        return AdvancedDDOSWithRawResponse(self._settings.advanced_ddos)

    @cached_property
    def always_online(self) -> AlwaysOnlineWithRawResponse:
        return AlwaysOnlineWithRawResponse(self._settings.always_online)

    @cached_property
    def always_use_https(self) -> AlwaysUseHTTPSWithRawResponse:
        return AlwaysUseHTTPSWithRawResponse(self._settings.always_use_https)

    @cached_property
    def automatic_https_rewrites(self) -> AutomaticHTTPSRewritesWithRawResponse:
        return AutomaticHTTPSRewritesWithRawResponse(self._settings.automatic_https_rewrites)

    @cached_property
    def automatic_platform_optimization(self) -> AutomaticPlatformOptimizationWithRawResponse:
        return AutomaticPlatformOptimizationWithRawResponse(self._settings.automatic_platform_optimization)

    @cached_property
    def brotli(self) -> BrotliWithRawResponse:
        return BrotliWithRawResponse(self._settings.brotli)

    @cached_property
    def browser_cache_ttl(self) -> BrowserCacheTTLWithRawResponse:
        return BrowserCacheTTLWithRawResponse(self._settings.browser_cache_ttl)

    @cached_property
    def browser_check(self) -> BrowserCheckWithRawResponse:
        return BrowserCheckWithRawResponse(self._settings.browser_check)

    @cached_property
    def cache_level(self) -> CacheLevelWithRawResponse:
        return CacheLevelWithRawResponse(self._settings.cache_level)

    @cached_property
    def challenge_ttl(self) -> ChallengeTTLWithRawResponse:
        return ChallengeTTLWithRawResponse(self._settings.challenge_ttl)

    @cached_property
    def ciphers(self) -> CiphersWithRawResponse:
        return CiphersWithRawResponse(self._settings.ciphers)

    @cached_property
    def development_mode(self) -> DevelopmentModeWithRawResponse:
        return DevelopmentModeWithRawResponse(self._settings.development_mode)

    @cached_property
    def early_hints(self) -> EarlyHintsWithRawResponse:
        return EarlyHintsWithRawResponse(self._settings.early_hints)

    @cached_property
    def email_obfuscation(self) -> EmailObfuscationWithRawResponse:
        return EmailObfuscationWithRawResponse(self._settings.email_obfuscation)

    @cached_property
    def h2_prioritization(self) -> H2PrioritizationWithRawResponse:
        return H2PrioritizationWithRawResponse(self._settings.h2_prioritization)

    @cached_property
    def hotlink_protection(self) -> HotlinkProtectionWithRawResponse:
        return HotlinkProtectionWithRawResponse(self._settings.hotlink_protection)

    @cached_property
    def http2(self) -> HTTP2WithRawResponse:
        return HTTP2WithRawResponse(self._settings.http2)

    @cached_property
    def http3(self) -> HTTP3WithRawResponse:
        return HTTP3WithRawResponse(self._settings.http3)

    @cached_property
    def image_resizing(self) -> ImageResizingWithRawResponse:
        return ImageResizingWithRawResponse(self._settings.image_resizing)

    @cached_property
    def ip_geolocation(self) -> IPGeolocationWithRawResponse:
        return IPGeolocationWithRawResponse(self._settings.ip_geolocation)

    @cached_property
    def ipv6(self) -> IPV6WithRawResponse:
        return IPV6WithRawResponse(self._settings.ipv6)

    @cached_property
    def min_tls_version(self) -> MinTLSVersionWithRawResponse:
        return MinTLSVersionWithRawResponse(self._settings.min_tls_version)

    @cached_property
    def minify(self) -> MinifyWithRawResponse:
        return MinifyWithRawResponse(self._settings.minify)

    @cached_property
    def mirage(self) -> MirageWithRawResponse:
        return MirageWithRawResponse(self._settings.mirage)

    @cached_property
    def mobile_redirect(self) -> MobileRedirectWithRawResponse:
        return MobileRedirectWithRawResponse(self._settings.mobile_redirect)

    @cached_property
    def nel(self) -> NELWithRawResponse:
        return NELWithRawResponse(self._settings.nel)

    @cached_property
    def opportunistic_encryption(self) -> OpportunisticEncryptionWithRawResponse:
        return OpportunisticEncryptionWithRawResponse(self._settings.opportunistic_encryption)

    @cached_property
    def opportunistic_onion(self) -> OpportunisticOnionWithRawResponse:
        return OpportunisticOnionWithRawResponse(self._settings.opportunistic_onion)

    @cached_property
    def orange_to_orange(self) -> OrangeToOrangeWithRawResponse:
        return OrangeToOrangeWithRawResponse(self._settings.orange_to_orange)

    @cached_property
    def origin_error_page_pass_thru(self) -> OriginErrorPagePassThruWithRawResponse:
        return OriginErrorPagePassThruWithRawResponse(self._settings.origin_error_page_pass_thru)

    @cached_property
    def origin_max_http_version(self) -> OriginMaxHTTPVersionWithRawResponse:
        return OriginMaxHTTPVersionWithRawResponse(self._settings.origin_max_http_version)

    @cached_property
    def polish(self) -> PolishWithRawResponse:
        return PolishWithRawResponse(self._settings.polish)

    @cached_property
    def prefetch_preload(self) -> PrefetchPreloadWithRawResponse:
        return PrefetchPreloadWithRawResponse(self._settings.prefetch_preload)

    @cached_property
    def proxy_read_timeout(self) -> ProxyReadTimeoutWithRawResponse:
        return ProxyReadTimeoutWithRawResponse(self._settings.proxy_read_timeout)

    @cached_property
    def pseudo_ipv4(self) -> PseudoIPV4WithRawResponse:
        return PseudoIPV4WithRawResponse(self._settings.pseudo_ipv4)

    @cached_property
    def response_buffering(self) -> ResponseBufferingWithRawResponse:
        return ResponseBufferingWithRawResponse(self._settings.response_buffering)

    @cached_property
    def rocket_loader(self) -> RocketLoaderWithRawResponse:
        return RocketLoaderWithRawResponse(self._settings.rocket_loader)

    @cached_property
    def security_headers(self) -> SecurityHeadersWithRawResponse:
        return SecurityHeadersWithRawResponse(self._settings.security_headers)

    @cached_property
    def security_level(self) -> SecurityLevelWithRawResponse:
        return SecurityLevelWithRawResponse(self._settings.security_level)

    @cached_property
    def server_side_excludes(self) -> ServerSideExcludesWithRawResponse:
        return ServerSideExcludesWithRawResponse(self._settings.server_side_excludes)

    @cached_property
    def sort_query_string_for_cache(self) -> SortQueryStringForCacheWithRawResponse:
        return SortQueryStringForCacheWithRawResponse(self._settings.sort_query_string_for_cache)

    @cached_property
    def ssl(self) -> SSLWithRawResponse:
        return SSLWithRawResponse(self._settings.ssl)

    @cached_property
    def ssl_recommender(self) -> SSLRecommenderWithRawResponse:
        return SSLRecommenderWithRawResponse(self._settings.ssl_recommender)

    @cached_property
    def tls_1_3(self) -> TLS1_3WithRawResponse:
        return TLS1_3WithRawResponse(self._settings.tls_1_3)

    @cached_property
    def tls_client_auth(self) -> TLSClientAuthWithRawResponse:
        return TLSClientAuthWithRawResponse(self._settings.tls_client_auth)

    @cached_property
    def true_client_ip_header(self) -> TrueClientIPHeaderWithRawResponse:
        return TrueClientIPHeaderWithRawResponse(self._settings.true_client_ip_header)

    @cached_property
    def waf(self) -> WAFWithRawResponse:
        return WAFWithRawResponse(self._settings.waf)

    @cached_property
    def webp(self) -> WebPWithRawResponse:
        return WebPWithRawResponse(self._settings.webp)

    @cached_property
    def websocket(self) -> WebsocketWithRawResponse:
        return WebsocketWithRawResponse(self._settings.websocket)

    @cached_property
    def font_settings(self) -> FontSettingsWithRawResponse:
        return FontSettingsWithRawResponse(self._settings.font_settings)


class AsyncSettingsWithRawResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

        self.edit = async_to_raw_response_wrapper(
            settings.edit,
        )
        self.get = async_to_raw_response_wrapper(
            settings.get,
        )

    @cached_property
    def zero_rtt(self) -> AsyncZeroRTTWithRawResponse:
        return AsyncZeroRTTWithRawResponse(self._settings.zero_rtt)

    @cached_property
    def advanced_ddos(self) -> AsyncAdvancedDDOSWithRawResponse:
        return AsyncAdvancedDDOSWithRawResponse(self._settings.advanced_ddos)

    @cached_property
    def always_online(self) -> AsyncAlwaysOnlineWithRawResponse:
        return AsyncAlwaysOnlineWithRawResponse(self._settings.always_online)

    @cached_property
    def always_use_https(self) -> AsyncAlwaysUseHTTPSWithRawResponse:
        return AsyncAlwaysUseHTTPSWithRawResponse(self._settings.always_use_https)

    @cached_property
    def automatic_https_rewrites(self) -> AsyncAutomaticHTTPSRewritesWithRawResponse:
        return AsyncAutomaticHTTPSRewritesWithRawResponse(self._settings.automatic_https_rewrites)

    @cached_property
    def automatic_platform_optimization(self) -> AsyncAutomaticPlatformOptimizationWithRawResponse:
        return AsyncAutomaticPlatformOptimizationWithRawResponse(self._settings.automatic_platform_optimization)

    @cached_property
    def brotli(self) -> AsyncBrotliWithRawResponse:
        return AsyncBrotliWithRawResponse(self._settings.brotli)

    @cached_property
    def browser_cache_ttl(self) -> AsyncBrowserCacheTTLWithRawResponse:
        return AsyncBrowserCacheTTLWithRawResponse(self._settings.browser_cache_ttl)

    @cached_property
    def browser_check(self) -> AsyncBrowserCheckWithRawResponse:
        return AsyncBrowserCheckWithRawResponse(self._settings.browser_check)

    @cached_property
    def cache_level(self) -> AsyncCacheLevelWithRawResponse:
        return AsyncCacheLevelWithRawResponse(self._settings.cache_level)

    @cached_property
    def challenge_ttl(self) -> AsyncChallengeTTLWithRawResponse:
        return AsyncChallengeTTLWithRawResponse(self._settings.challenge_ttl)

    @cached_property
    def ciphers(self) -> AsyncCiphersWithRawResponse:
        return AsyncCiphersWithRawResponse(self._settings.ciphers)

    @cached_property
    def development_mode(self) -> AsyncDevelopmentModeWithRawResponse:
        return AsyncDevelopmentModeWithRawResponse(self._settings.development_mode)

    @cached_property
    def early_hints(self) -> AsyncEarlyHintsWithRawResponse:
        return AsyncEarlyHintsWithRawResponse(self._settings.early_hints)

    @cached_property
    def email_obfuscation(self) -> AsyncEmailObfuscationWithRawResponse:
        return AsyncEmailObfuscationWithRawResponse(self._settings.email_obfuscation)

    @cached_property
    def h2_prioritization(self) -> AsyncH2PrioritizationWithRawResponse:
        return AsyncH2PrioritizationWithRawResponse(self._settings.h2_prioritization)

    @cached_property
    def hotlink_protection(self) -> AsyncHotlinkProtectionWithRawResponse:
        return AsyncHotlinkProtectionWithRawResponse(self._settings.hotlink_protection)

    @cached_property
    def http2(self) -> AsyncHTTP2WithRawResponse:
        return AsyncHTTP2WithRawResponse(self._settings.http2)

    @cached_property
    def http3(self) -> AsyncHTTP3WithRawResponse:
        return AsyncHTTP3WithRawResponse(self._settings.http3)

    @cached_property
    def image_resizing(self) -> AsyncImageResizingWithRawResponse:
        return AsyncImageResizingWithRawResponse(self._settings.image_resizing)

    @cached_property
    def ip_geolocation(self) -> AsyncIPGeolocationWithRawResponse:
        return AsyncIPGeolocationWithRawResponse(self._settings.ip_geolocation)

    @cached_property
    def ipv6(self) -> AsyncIPV6WithRawResponse:
        return AsyncIPV6WithRawResponse(self._settings.ipv6)

    @cached_property
    def min_tls_version(self) -> AsyncMinTLSVersionWithRawResponse:
        return AsyncMinTLSVersionWithRawResponse(self._settings.min_tls_version)

    @cached_property
    def minify(self) -> AsyncMinifyWithRawResponse:
        return AsyncMinifyWithRawResponse(self._settings.minify)

    @cached_property
    def mirage(self) -> AsyncMirageWithRawResponse:
        return AsyncMirageWithRawResponse(self._settings.mirage)

    @cached_property
    def mobile_redirect(self) -> AsyncMobileRedirectWithRawResponse:
        return AsyncMobileRedirectWithRawResponse(self._settings.mobile_redirect)

    @cached_property
    def nel(self) -> AsyncNELWithRawResponse:
        return AsyncNELWithRawResponse(self._settings.nel)

    @cached_property
    def opportunistic_encryption(self) -> AsyncOpportunisticEncryptionWithRawResponse:
        return AsyncOpportunisticEncryptionWithRawResponse(self._settings.opportunistic_encryption)

    @cached_property
    def opportunistic_onion(self) -> AsyncOpportunisticOnionWithRawResponse:
        return AsyncOpportunisticOnionWithRawResponse(self._settings.opportunistic_onion)

    @cached_property
    def orange_to_orange(self) -> AsyncOrangeToOrangeWithRawResponse:
        return AsyncOrangeToOrangeWithRawResponse(self._settings.orange_to_orange)

    @cached_property
    def origin_error_page_pass_thru(self) -> AsyncOriginErrorPagePassThruWithRawResponse:
        return AsyncOriginErrorPagePassThruWithRawResponse(self._settings.origin_error_page_pass_thru)

    @cached_property
    def origin_max_http_version(self) -> AsyncOriginMaxHTTPVersionWithRawResponse:
        return AsyncOriginMaxHTTPVersionWithRawResponse(self._settings.origin_max_http_version)

    @cached_property
    def polish(self) -> AsyncPolishWithRawResponse:
        return AsyncPolishWithRawResponse(self._settings.polish)

    @cached_property
    def prefetch_preload(self) -> AsyncPrefetchPreloadWithRawResponse:
        return AsyncPrefetchPreloadWithRawResponse(self._settings.prefetch_preload)

    @cached_property
    def proxy_read_timeout(self) -> AsyncProxyReadTimeoutWithRawResponse:
        return AsyncProxyReadTimeoutWithRawResponse(self._settings.proxy_read_timeout)

    @cached_property
    def pseudo_ipv4(self) -> AsyncPseudoIPV4WithRawResponse:
        return AsyncPseudoIPV4WithRawResponse(self._settings.pseudo_ipv4)

    @cached_property
    def response_buffering(self) -> AsyncResponseBufferingWithRawResponse:
        return AsyncResponseBufferingWithRawResponse(self._settings.response_buffering)

    @cached_property
    def rocket_loader(self) -> AsyncRocketLoaderWithRawResponse:
        return AsyncRocketLoaderWithRawResponse(self._settings.rocket_loader)

    @cached_property
    def security_headers(self) -> AsyncSecurityHeadersWithRawResponse:
        return AsyncSecurityHeadersWithRawResponse(self._settings.security_headers)

    @cached_property
    def security_level(self) -> AsyncSecurityLevelWithRawResponse:
        return AsyncSecurityLevelWithRawResponse(self._settings.security_level)

    @cached_property
    def server_side_excludes(self) -> AsyncServerSideExcludesWithRawResponse:
        return AsyncServerSideExcludesWithRawResponse(self._settings.server_side_excludes)

    @cached_property
    def sort_query_string_for_cache(self) -> AsyncSortQueryStringForCacheWithRawResponse:
        return AsyncSortQueryStringForCacheWithRawResponse(self._settings.sort_query_string_for_cache)

    @cached_property
    def ssl(self) -> AsyncSSLWithRawResponse:
        return AsyncSSLWithRawResponse(self._settings.ssl)

    @cached_property
    def ssl_recommender(self) -> AsyncSSLRecommenderWithRawResponse:
        return AsyncSSLRecommenderWithRawResponse(self._settings.ssl_recommender)

    @cached_property
    def tls_1_3(self) -> AsyncTLS1_3WithRawResponse:
        return AsyncTLS1_3WithRawResponse(self._settings.tls_1_3)

    @cached_property
    def tls_client_auth(self) -> AsyncTLSClientAuthWithRawResponse:
        return AsyncTLSClientAuthWithRawResponse(self._settings.tls_client_auth)

    @cached_property
    def true_client_ip_header(self) -> AsyncTrueClientIPHeaderWithRawResponse:
        return AsyncTrueClientIPHeaderWithRawResponse(self._settings.true_client_ip_header)

    @cached_property
    def waf(self) -> AsyncWAFWithRawResponse:
        return AsyncWAFWithRawResponse(self._settings.waf)

    @cached_property
    def webp(self) -> AsyncWebPWithRawResponse:
        return AsyncWebPWithRawResponse(self._settings.webp)

    @cached_property
    def websocket(self) -> AsyncWebsocketWithRawResponse:
        return AsyncWebsocketWithRawResponse(self._settings.websocket)

    @cached_property
    def font_settings(self) -> AsyncFontSettingsWithRawResponse:
        return AsyncFontSettingsWithRawResponse(self._settings.font_settings)


class SettingsWithStreamingResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

        self.edit = to_streamed_response_wrapper(
            settings.edit,
        )
        self.get = to_streamed_response_wrapper(
            settings.get,
        )

    @cached_property
    def zero_rtt(self) -> ZeroRTTWithStreamingResponse:
        return ZeroRTTWithStreamingResponse(self._settings.zero_rtt)

    @cached_property
    def advanced_ddos(self) -> AdvancedDDOSWithStreamingResponse:
        return AdvancedDDOSWithStreamingResponse(self._settings.advanced_ddos)

    @cached_property
    def always_online(self) -> AlwaysOnlineWithStreamingResponse:
        return AlwaysOnlineWithStreamingResponse(self._settings.always_online)

    @cached_property
    def always_use_https(self) -> AlwaysUseHTTPSWithStreamingResponse:
        return AlwaysUseHTTPSWithStreamingResponse(self._settings.always_use_https)

    @cached_property
    def automatic_https_rewrites(self) -> AutomaticHTTPSRewritesWithStreamingResponse:
        return AutomaticHTTPSRewritesWithStreamingResponse(self._settings.automatic_https_rewrites)

    @cached_property
    def automatic_platform_optimization(self) -> AutomaticPlatformOptimizationWithStreamingResponse:
        return AutomaticPlatformOptimizationWithStreamingResponse(self._settings.automatic_platform_optimization)

    @cached_property
    def brotli(self) -> BrotliWithStreamingResponse:
        return BrotliWithStreamingResponse(self._settings.brotli)

    @cached_property
    def browser_cache_ttl(self) -> BrowserCacheTTLWithStreamingResponse:
        return BrowserCacheTTLWithStreamingResponse(self._settings.browser_cache_ttl)

    @cached_property
    def browser_check(self) -> BrowserCheckWithStreamingResponse:
        return BrowserCheckWithStreamingResponse(self._settings.browser_check)

    @cached_property
    def cache_level(self) -> CacheLevelWithStreamingResponse:
        return CacheLevelWithStreamingResponse(self._settings.cache_level)

    @cached_property
    def challenge_ttl(self) -> ChallengeTTLWithStreamingResponse:
        return ChallengeTTLWithStreamingResponse(self._settings.challenge_ttl)

    @cached_property
    def ciphers(self) -> CiphersWithStreamingResponse:
        return CiphersWithStreamingResponse(self._settings.ciphers)

    @cached_property
    def development_mode(self) -> DevelopmentModeWithStreamingResponse:
        return DevelopmentModeWithStreamingResponse(self._settings.development_mode)

    @cached_property
    def early_hints(self) -> EarlyHintsWithStreamingResponse:
        return EarlyHintsWithStreamingResponse(self._settings.early_hints)

    @cached_property
    def email_obfuscation(self) -> EmailObfuscationWithStreamingResponse:
        return EmailObfuscationWithStreamingResponse(self._settings.email_obfuscation)

    @cached_property
    def h2_prioritization(self) -> H2PrioritizationWithStreamingResponse:
        return H2PrioritizationWithStreamingResponse(self._settings.h2_prioritization)

    @cached_property
    def hotlink_protection(self) -> HotlinkProtectionWithStreamingResponse:
        return HotlinkProtectionWithStreamingResponse(self._settings.hotlink_protection)

    @cached_property
    def http2(self) -> HTTP2WithStreamingResponse:
        return HTTP2WithStreamingResponse(self._settings.http2)

    @cached_property
    def http3(self) -> HTTP3WithStreamingResponse:
        return HTTP3WithStreamingResponse(self._settings.http3)

    @cached_property
    def image_resizing(self) -> ImageResizingWithStreamingResponse:
        return ImageResizingWithStreamingResponse(self._settings.image_resizing)

    @cached_property
    def ip_geolocation(self) -> IPGeolocationWithStreamingResponse:
        return IPGeolocationWithStreamingResponse(self._settings.ip_geolocation)

    @cached_property
    def ipv6(self) -> IPV6WithStreamingResponse:
        return IPV6WithStreamingResponse(self._settings.ipv6)

    @cached_property
    def min_tls_version(self) -> MinTLSVersionWithStreamingResponse:
        return MinTLSVersionWithStreamingResponse(self._settings.min_tls_version)

    @cached_property
    def minify(self) -> MinifyWithStreamingResponse:
        return MinifyWithStreamingResponse(self._settings.minify)

    @cached_property
    def mirage(self) -> MirageWithStreamingResponse:
        return MirageWithStreamingResponse(self._settings.mirage)

    @cached_property
    def mobile_redirect(self) -> MobileRedirectWithStreamingResponse:
        return MobileRedirectWithStreamingResponse(self._settings.mobile_redirect)

    @cached_property
    def nel(self) -> NELWithStreamingResponse:
        return NELWithStreamingResponse(self._settings.nel)

    @cached_property
    def opportunistic_encryption(self) -> OpportunisticEncryptionWithStreamingResponse:
        return OpportunisticEncryptionWithStreamingResponse(self._settings.opportunistic_encryption)

    @cached_property
    def opportunistic_onion(self) -> OpportunisticOnionWithStreamingResponse:
        return OpportunisticOnionWithStreamingResponse(self._settings.opportunistic_onion)

    @cached_property
    def orange_to_orange(self) -> OrangeToOrangeWithStreamingResponse:
        return OrangeToOrangeWithStreamingResponse(self._settings.orange_to_orange)

    @cached_property
    def origin_error_page_pass_thru(self) -> OriginErrorPagePassThruWithStreamingResponse:
        return OriginErrorPagePassThruWithStreamingResponse(self._settings.origin_error_page_pass_thru)

    @cached_property
    def origin_max_http_version(self) -> OriginMaxHTTPVersionWithStreamingResponse:
        return OriginMaxHTTPVersionWithStreamingResponse(self._settings.origin_max_http_version)

    @cached_property
    def polish(self) -> PolishWithStreamingResponse:
        return PolishWithStreamingResponse(self._settings.polish)

    @cached_property
    def prefetch_preload(self) -> PrefetchPreloadWithStreamingResponse:
        return PrefetchPreloadWithStreamingResponse(self._settings.prefetch_preload)

    @cached_property
    def proxy_read_timeout(self) -> ProxyReadTimeoutWithStreamingResponse:
        return ProxyReadTimeoutWithStreamingResponse(self._settings.proxy_read_timeout)

    @cached_property
    def pseudo_ipv4(self) -> PseudoIPV4WithStreamingResponse:
        return PseudoIPV4WithStreamingResponse(self._settings.pseudo_ipv4)

    @cached_property
    def response_buffering(self) -> ResponseBufferingWithStreamingResponse:
        return ResponseBufferingWithStreamingResponse(self._settings.response_buffering)

    @cached_property
    def rocket_loader(self) -> RocketLoaderWithStreamingResponse:
        return RocketLoaderWithStreamingResponse(self._settings.rocket_loader)

    @cached_property
    def security_headers(self) -> SecurityHeadersWithStreamingResponse:
        return SecurityHeadersWithStreamingResponse(self._settings.security_headers)

    @cached_property
    def security_level(self) -> SecurityLevelWithStreamingResponse:
        return SecurityLevelWithStreamingResponse(self._settings.security_level)

    @cached_property
    def server_side_excludes(self) -> ServerSideExcludesWithStreamingResponse:
        return ServerSideExcludesWithStreamingResponse(self._settings.server_side_excludes)

    @cached_property
    def sort_query_string_for_cache(self) -> SortQueryStringForCacheWithStreamingResponse:
        return SortQueryStringForCacheWithStreamingResponse(self._settings.sort_query_string_for_cache)

    @cached_property
    def ssl(self) -> SSLWithStreamingResponse:
        return SSLWithStreamingResponse(self._settings.ssl)

    @cached_property
    def ssl_recommender(self) -> SSLRecommenderWithStreamingResponse:
        return SSLRecommenderWithStreamingResponse(self._settings.ssl_recommender)

    @cached_property
    def tls_1_3(self) -> TLS1_3WithStreamingResponse:
        return TLS1_3WithStreamingResponse(self._settings.tls_1_3)

    @cached_property
    def tls_client_auth(self) -> TLSClientAuthWithStreamingResponse:
        return TLSClientAuthWithStreamingResponse(self._settings.tls_client_auth)

    @cached_property
    def true_client_ip_header(self) -> TrueClientIPHeaderWithStreamingResponse:
        return TrueClientIPHeaderWithStreamingResponse(self._settings.true_client_ip_header)

    @cached_property
    def waf(self) -> WAFWithStreamingResponse:
        return WAFWithStreamingResponse(self._settings.waf)

    @cached_property
    def webp(self) -> WebPWithStreamingResponse:
        return WebPWithStreamingResponse(self._settings.webp)

    @cached_property
    def websocket(self) -> WebsocketWithStreamingResponse:
        return WebsocketWithStreamingResponse(self._settings.websocket)

    @cached_property
    def font_settings(self) -> FontSettingsWithStreamingResponse:
        return FontSettingsWithStreamingResponse(self._settings.font_settings)


class AsyncSettingsWithStreamingResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

        self.edit = async_to_streamed_response_wrapper(
            settings.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            settings.get,
        )

    @cached_property
    def zero_rtt(self) -> AsyncZeroRTTWithStreamingResponse:
        return AsyncZeroRTTWithStreamingResponse(self._settings.zero_rtt)

    @cached_property
    def advanced_ddos(self) -> AsyncAdvancedDDOSWithStreamingResponse:
        return AsyncAdvancedDDOSWithStreamingResponse(self._settings.advanced_ddos)

    @cached_property
    def always_online(self) -> AsyncAlwaysOnlineWithStreamingResponse:
        return AsyncAlwaysOnlineWithStreamingResponse(self._settings.always_online)

    @cached_property
    def always_use_https(self) -> AsyncAlwaysUseHTTPSWithStreamingResponse:
        return AsyncAlwaysUseHTTPSWithStreamingResponse(self._settings.always_use_https)

    @cached_property
    def automatic_https_rewrites(self) -> AsyncAutomaticHTTPSRewritesWithStreamingResponse:
        return AsyncAutomaticHTTPSRewritesWithStreamingResponse(self._settings.automatic_https_rewrites)

    @cached_property
    def automatic_platform_optimization(self) -> AsyncAutomaticPlatformOptimizationWithStreamingResponse:
        return AsyncAutomaticPlatformOptimizationWithStreamingResponse(self._settings.automatic_platform_optimization)

    @cached_property
    def brotli(self) -> AsyncBrotliWithStreamingResponse:
        return AsyncBrotliWithStreamingResponse(self._settings.brotli)

    @cached_property
    def browser_cache_ttl(self) -> AsyncBrowserCacheTTLWithStreamingResponse:
        return AsyncBrowserCacheTTLWithStreamingResponse(self._settings.browser_cache_ttl)

    @cached_property
    def browser_check(self) -> AsyncBrowserCheckWithStreamingResponse:
        return AsyncBrowserCheckWithStreamingResponse(self._settings.browser_check)

    @cached_property
    def cache_level(self) -> AsyncCacheLevelWithStreamingResponse:
        return AsyncCacheLevelWithStreamingResponse(self._settings.cache_level)

    @cached_property
    def challenge_ttl(self) -> AsyncChallengeTTLWithStreamingResponse:
        return AsyncChallengeTTLWithStreamingResponse(self._settings.challenge_ttl)

    @cached_property
    def ciphers(self) -> AsyncCiphersWithStreamingResponse:
        return AsyncCiphersWithStreamingResponse(self._settings.ciphers)

    @cached_property
    def development_mode(self) -> AsyncDevelopmentModeWithStreamingResponse:
        return AsyncDevelopmentModeWithStreamingResponse(self._settings.development_mode)

    @cached_property
    def early_hints(self) -> AsyncEarlyHintsWithStreamingResponse:
        return AsyncEarlyHintsWithStreamingResponse(self._settings.early_hints)

    @cached_property
    def email_obfuscation(self) -> AsyncEmailObfuscationWithStreamingResponse:
        return AsyncEmailObfuscationWithStreamingResponse(self._settings.email_obfuscation)

    @cached_property
    def h2_prioritization(self) -> AsyncH2PrioritizationWithStreamingResponse:
        return AsyncH2PrioritizationWithStreamingResponse(self._settings.h2_prioritization)

    @cached_property
    def hotlink_protection(self) -> AsyncHotlinkProtectionWithStreamingResponse:
        return AsyncHotlinkProtectionWithStreamingResponse(self._settings.hotlink_protection)

    @cached_property
    def http2(self) -> AsyncHTTP2WithStreamingResponse:
        return AsyncHTTP2WithStreamingResponse(self._settings.http2)

    @cached_property
    def http3(self) -> AsyncHTTP3WithStreamingResponse:
        return AsyncHTTP3WithStreamingResponse(self._settings.http3)

    @cached_property
    def image_resizing(self) -> AsyncImageResizingWithStreamingResponse:
        return AsyncImageResizingWithStreamingResponse(self._settings.image_resizing)

    @cached_property
    def ip_geolocation(self) -> AsyncIPGeolocationWithStreamingResponse:
        return AsyncIPGeolocationWithStreamingResponse(self._settings.ip_geolocation)

    @cached_property
    def ipv6(self) -> AsyncIPV6WithStreamingResponse:
        return AsyncIPV6WithStreamingResponse(self._settings.ipv6)

    @cached_property
    def min_tls_version(self) -> AsyncMinTLSVersionWithStreamingResponse:
        return AsyncMinTLSVersionWithStreamingResponse(self._settings.min_tls_version)

    @cached_property
    def minify(self) -> AsyncMinifyWithStreamingResponse:
        return AsyncMinifyWithStreamingResponse(self._settings.minify)

    @cached_property
    def mirage(self) -> AsyncMirageWithStreamingResponse:
        return AsyncMirageWithStreamingResponse(self._settings.mirage)

    @cached_property
    def mobile_redirect(self) -> AsyncMobileRedirectWithStreamingResponse:
        return AsyncMobileRedirectWithStreamingResponse(self._settings.mobile_redirect)

    @cached_property
    def nel(self) -> AsyncNELWithStreamingResponse:
        return AsyncNELWithStreamingResponse(self._settings.nel)

    @cached_property
    def opportunistic_encryption(self) -> AsyncOpportunisticEncryptionWithStreamingResponse:
        return AsyncOpportunisticEncryptionWithStreamingResponse(self._settings.opportunistic_encryption)

    @cached_property
    def opportunistic_onion(self) -> AsyncOpportunisticOnionWithStreamingResponse:
        return AsyncOpportunisticOnionWithStreamingResponse(self._settings.opportunistic_onion)

    @cached_property
    def orange_to_orange(self) -> AsyncOrangeToOrangeWithStreamingResponse:
        return AsyncOrangeToOrangeWithStreamingResponse(self._settings.orange_to_orange)

    @cached_property
    def origin_error_page_pass_thru(self) -> AsyncOriginErrorPagePassThruWithStreamingResponse:
        return AsyncOriginErrorPagePassThruWithStreamingResponse(self._settings.origin_error_page_pass_thru)

    @cached_property
    def origin_max_http_version(self) -> AsyncOriginMaxHTTPVersionWithStreamingResponse:
        return AsyncOriginMaxHTTPVersionWithStreamingResponse(self._settings.origin_max_http_version)

    @cached_property
    def polish(self) -> AsyncPolishWithStreamingResponse:
        return AsyncPolishWithStreamingResponse(self._settings.polish)

    @cached_property
    def prefetch_preload(self) -> AsyncPrefetchPreloadWithStreamingResponse:
        return AsyncPrefetchPreloadWithStreamingResponse(self._settings.prefetch_preload)

    @cached_property
    def proxy_read_timeout(self) -> AsyncProxyReadTimeoutWithStreamingResponse:
        return AsyncProxyReadTimeoutWithStreamingResponse(self._settings.proxy_read_timeout)

    @cached_property
    def pseudo_ipv4(self) -> AsyncPseudoIPV4WithStreamingResponse:
        return AsyncPseudoIPV4WithStreamingResponse(self._settings.pseudo_ipv4)

    @cached_property
    def response_buffering(self) -> AsyncResponseBufferingWithStreamingResponse:
        return AsyncResponseBufferingWithStreamingResponse(self._settings.response_buffering)

    @cached_property
    def rocket_loader(self) -> AsyncRocketLoaderWithStreamingResponse:
        return AsyncRocketLoaderWithStreamingResponse(self._settings.rocket_loader)

    @cached_property
    def security_headers(self) -> AsyncSecurityHeadersWithStreamingResponse:
        return AsyncSecurityHeadersWithStreamingResponse(self._settings.security_headers)

    @cached_property
    def security_level(self) -> AsyncSecurityLevelWithStreamingResponse:
        return AsyncSecurityLevelWithStreamingResponse(self._settings.security_level)

    @cached_property
    def server_side_excludes(self) -> AsyncServerSideExcludesWithStreamingResponse:
        return AsyncServerSideExcludesWithStreamingResponse(self._settings.server_side_excludes)

    @cached_property
    def sort_query_string_for_cache(self) -> AsyncSortQueryStringForCacheWithStreamingResponse:
        return AsyncSortQueryStringForCacheWithStreamingResponse(self._settings.sort_query_string_for_cache)

    @cached_property
    def ssl(self) -> AsyncSSLWithStreamingResponse:
        return AsyncSSLWithStreamingResponse(self._settings.ssl)

    @cached_property
    def ssl_recommender(self) -> AsyncSSLRecommenderWithStreamingResponse:
        return AsyncSSLRecommenderWithStreamingResponse(self._settings.ssl_recommender)

    @cached_property
    def tls_1_3(self) -> AsyncTLS1_3WithStreamingResponse:
        return AsyncTLS1_3WithStreamingResponse(self._settings.tls_1_3)

    @cached_property
    def tls_client_auth(self) -> AsyncTLSClientAuthWithStreamingResponse:
        return AsyncTLSClientAuthWithStreamingResponse(self._settings.tls_client_auth)

    @cached_property
    def true_client_ip_header(self) -> AsyncTrueClientIPHeaderWithStreamingResponse:
        return AsyncTrueClientIPHeaderWithStreamingResponse(self._settings.true_client_ip_header)

    @cached_property
    def waf(self) -> AsyncWAFWithStreamingResponse:
        return AsyncWAFWithStreamingResponse(self._settings.waf)

    @cached_property
    def webp(self) -> AsyncWebPWithStreamingResponse:
        return AsyncWebPWithStreamingResponse(self._settings.webp)

    @cached_property
    def websocket(self) -> AsyncWebsocketWithStreamingResponse:
        return AsyncWebsocketWithStreamingResponse(self._settings.websocket)

    @cached_property
    def font_settings(self) -> AsyncFontSettingsWithStreamingResponse:
        return AsyncFontSettingsWithStreamingResponse(self._settings.font_settings)
