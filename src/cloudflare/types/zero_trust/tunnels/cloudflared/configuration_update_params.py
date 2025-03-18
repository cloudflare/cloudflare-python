# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = [
    "ConfigurationUpdateParams",
    "Config",
    "ConfigIngress",
    "ConfigIngressOriginRequest",
    "ConfigIngressOriginRequestAccess",
    "ConfigOriginRequest",
    "ConfigOriginRequestAccess",
]


class ConfigurationUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    config: Config
    """The tunnel configuration and ingress rules."""


class ConfigIngressOriginRequestAccess(TypedDict, total=False):
    aud_tag: Required[Annotated[List[str], PropertyInfo(alias="audTag")]]
    """Access applications that are allowed to reach this hostname for this Tunnel.

    Audience tags can be identified in the dashboard or via the List Access policies
    API.
    """

    team_name: Required[Annotated[str, PropertyInfo(alias="teamName")]]

    required: bool
    """Deny traffic that has not fulfilled Access authorization."""


class ConfigIngressOriginRequest(TypedDict, total=False):
    access: ConfigIngressOriginRequestAccess
    """
    For all L7 requests to this hostname, cloudflared will validate each request's
    Cf-Access-Jwt-Assertion request header.
    """

    ca_pool: Annotated[str, PropertyInfo(alias="caPool")]
    """Path to the certificate authority (CA) for the certificate of your origin.

    This option should be used only if your certificate is not signed by Cloudflare.
    """

    connect_timeout: Annotated[int, PropertyInfo(alias="connectTimeout")]
    """Timeout for establishing a new TCP connection to your origin server.

    This excludes the time taken to establish TLS, which is controlled by
    tlsTimeout.
    """

    disable_chunked_encoding: Annotated[bool, PropertyInfo(alias="disableChunkedEncoding")]
    """Disables chunked transfer encoding. Useful if you are running a WSGI server."""

    http2_origin: Annotated[bool, PropertyInfo(alias="http2Origin")]
    """Attempt to connect to origin using HTTP2. Origin must be configured as https."""

    http_host_header: Annotated[str, PropertyInfo(alias="httpHostHeader")]
    """Sets the HTTP Host header on requests sent to the local service."""

    keep_alive_connections: Annotated[int, PropertyInfo(alias="keepAliveConnections")]
    """Maximum number of idle keepalive connections between Tunnel and your origin.

    This does not restrict the total number of concurrent connections.
    """

    keep_alive_timeout: Annotated[int, PropertyInfo(alias="keepAliveTimeout")]
    """Timeout after which an idle keepalive connection can be discarded."""

    no_happy_eyeballs: Annotated[bool, PropertyInfo(alias="noHappyEyeballs")]
    """
    Disable the “happy eyeballs” algorithm for IPv4/IPv6 fallback if your local
    network has misconfigured one of the protocols.
    """

    no_tls_verify: Annotated[bool, PropertyInfo(alias="noTLSVerify")]
    """Disables TLS verification of the certificate presented by your origin.

    Will allow any certificate from the origin to be accepted.
    """

    origin_server_name: Annotated[str, PropertyInfo(alias="originServerName")]
    """Hostname that cloudflared should expect from your origin server certificate."""

    proxy_type: Annotated[str, PropertyInfo(alias="proxyType")]
    """
    cloudflared starts a proxy server to translate HTTP traffic into TCP when
    proxying, for example, SSH or RDP. This configures what type of proxy will be
    started. Valid options are: "" for the regular proxy and "socks" for a SOCKS5
    proxy.
    """

    tcp_keep_alive: Annotated[int, PropertyInfo(alias="tcpKeepAlive")]
    """
    The timeout after which a TCP keepalive packet is sent on a connection between
    Tunnel and the origin server.
    """

    tls_timeout: Annotated[int, PropertyInfo(alias="tlsTimeout")]
    """
    Timeout for completing a TLS handshake to your origin server, if you have chosen
    to connect Tunnel to an HTTPS server.
    """


class ConfigIngress(TypedDict, total=False):
    hostname: Required[str]
    """Public hostname for this service."""

    service: Required[str]
    """Protocol and address of destination server.

    Supported protocols: http://, https://, unix://, tcp://, ssh://, rdp://,
    unix+tls://, smb://. Alternatively can return a HTTP status code
    http_status:[code] e.g. 'http_status:404'.
    """

    origin_request: Annotated[ConfigIngressOriginRequest, PropertyInfo(alias="originRequest")]
    """
    Configuration parameters for the public hostname specific connection settings
    between cloudflared and origin server.
    """

    path: str
    """Requests with this path route to this public hostname."""


class ConfigOriginRequestAccess(TypedDict, total=False):
    aud_tag: Required[Annotated[List[str], PropertyInfo(alias="audTag")]]
    """Access applications that are allowed to reach this hostname for this Tunnel.

    Audience tags can be identified in the dashboard or via the List Access policies
    API.
    """

    team_name: Required[Annotated[str, PropertyInfo(alias="teamName")]]

    required: bool
    """Deny traffic that has not fulfilled Access authorization."""


class ConfigOriginRequest(TypedDict, total=False):
    access: ConfigOriginRequestAccess
    """
    For all L7 requests to this hostname, cloudflared will validate each request's
    Cf-Access-Jwt-Assertion request header.
    """

    ca_pool: Annotated[str, PropertyInfo(alias="caPool")]
    """Path to the certificate authority (CA) for the certificate of your origin.

    This option should be used only if your certificate is not signed by Cloudflare.
    """

    connect_timeout: Annotated[int, PropertyInfo(alias="connectTimeout")]
    """Timeout for establishing a new TCP connection to your origin server.

    This excludes the time taken to establish TLS, which is controlled by
    tlsTimeout.
    """

    disable_chunked_encoding: Annotated[bool, PropertyInfo(alias="disableChunkedEncoding")]
    """Disables chunked transfer encoding. Useful if you are running a WSGI server."""

    http2_origin: Annotated[bool, PropertyInfo(alias="http2Origin")]
    """Attempt to connect to origin using HTTP2. Origin must be configured as https."""

    http_host_header: Annotated[str, PropertyInfo(alias="httpHostHeader")]
    """Sets the HTTP Host header on requests sent to the local service."""

    keep_alive_connections: Annotated[int, PropertyInfo(alias="keepAliveConnections")]
    """Maximum number of idle keepalive connections between Tunnel and your origin.

    This does not restrict the total number of concurrent connections.
    """

    keep_alive_timeout: Annotated[int, PropertyInfo(alias="keepAliveTimeout")]
    """Timeout after which an idle keepalive connection can be discarded."""

    no_happy_eyeballs: Annotated[bool, PropertyInfo(alias="noHappyEyeballs")]
    """
    Disable the “happy eyeballs” algorithm for IPv4/IPv6 fallback if your local
    network has misconfigured one of the protocols.
    """

    no_tls_verify: Annotated[bool, PropertyInfo(alias="noTLSVerify")]
    """Disables TLS verification of the certificate presented by your origin.

    Will allow any certificate from the origin to be accepted.
    """

    origin_server_name: Annotated[str, PropertyInfo(alias="originServerName")]
    """Hostname that cloudflared should expect from your origin server certificate."""

    proxy_type: Annotated[str, PropertyInfo(alias="proxyType")]
    """
    cloudflared starts a proxy server to translate HTTP traffic into TCP when
    proxying, for example, SSH or RDP. This configures what type of proxy will be
    started. Valid options are: "" for the regular proxy and "socks" for a SOCKS5
    proxy.
    """

    tcp_keep_alive: Annotated[int, PropertyInfo(alias="tcpKeepAlive")]
    """
    The timeout after which a TCP keepalive packet is sent on a connection between
    Tunnel and the origin server.
    """

    tls_timeout: Annotated[int, PropertyInfo(alias="tlsTimeout")]
    """
    Timeout for completing a TLS handshake to your origin server, if you have chosen
    to connect Tunnel to an HTTPS server.
    """


class Config(TypedDict, total=False):
    ingress: Iterable[ConfigIngress]
    """List of public hostname definitions.

    At least one ingress rule needs to be defined for the tunnel.
    """

    origin_request: Annotated[ConfigOriginRequest, PropertyInfo(alias="originRequest")]
    """
    Configuration parameters for the public hostname specific connection settings
    between cloudflared and origin server.
    """
