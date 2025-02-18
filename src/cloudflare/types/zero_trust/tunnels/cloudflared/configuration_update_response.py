# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "ConfigurationUpdateResponse",
    "Config",
    "ConfigIngress",
    "ConfigIngressOriginRequest",
    "ConfigIngressOriginRequestAccess",
    "ConfigOriginRequest",
    "ConfigOriginRequestAccess",
    "ConfigWARPRouting",
]


class ConfigIngressOriginRequestAccess(BaseModel):
    aud_tag: List[str] = FieldInfo(alias="audTag")
    """Access applications that are allowed to reach this hostname for this Tunnel.

    Audience tags can be identified in the dashboard or via the List Access policies
    API.
    """

    team_name: str = FieldInfo(alias="teamName")

    required: Optional[bool] = None
    """Deny traffic that has not fulfilled Access authorization."""


class ConfigIngressOriginRequest(BaseModel):
    access: Optional[ConfigIngressOriginRequestAccess] = None
    """
    For all L7 requests to this hostname, cloudflared will validate each request's
    Cf-Access-Jwt-Assertion request header.
    """

    ca_pool: Optional[str] = FieldInfo(alias="caPool", default=None)
    """Path to the certificate authority (CA) for the certificate of your origin.

    This option should be used only if your certificate is not signed by Cloudflare.
    """

    connect_timeout: Optional[int] = FieldInfo(alias="connectTimeout", default=None)
    """Timeout for establishing a new TCP connection to your origin server.

    This excludes the time taken to establish TLS, which is controlled by
    tlsTimeout.
    """

    disable_chunked_encoding: Optional[bool] = FieldInfo(alias="disableChunkedEncoding", default=None)
    """Disables chunked transfer encoding. Useful if you are running a WSGI server."""

    http2_origin: Optional[bool] = FieldInfo(alias="http2Origin", default=None)
    """Attempt to connect to origin using HTTP2. Origin must be configured as https."""

    http_host_header: Optional[str] = FieldInfo(alias="httpHostHeader", default=None)
    """Sets the HTTP Host header on requests sent to the local service."""

    keep_alive_connections: Optional[int] = FieldInfo(alias="keepAliveConnections", default=None)
    """Maximum number of idle keepalive connections between Tunnel and your origin.

    This does not restrict the total number of concurrent connections.
    """

    keep_alive_timeout: Optional[int] = FieldInfo(alias="keepAliveTimeout", default=None)
    """Timeout after which an idle keepalive connection can be discarded."""

    no_happy_eyeballs: Optional[bool] = FieldInfo(alias="noHappyEyeballs", default=None)
    """
    Disable the “happy eyeballs” algorithm for IPv4/IPv6 fallback if your local
    network has misconfigured one of the protocols.
    """

    no_tls_verify: Optional[bool] = FieldInfo(alias="noTLSVerify", default=None)
    """Disables TLS verification of the certificate presented by your origin.

    Will allow any certificate from the origin to be accepted.
    """

    origin_server_name: Optional[str] = FieldInfo(alias="originServerName", default=None)
    """Hostname that cloudflared should expect from your origin server certificate."""

    proxy_type: Optional[str] = FieldInfo(alias="proxyType", default=None)
    """
    cloudflared starts a proxy server to translate HTTP traffic into TCP when
    proxying, for example, SSH or RDP. This configures what type of proxy will be
    started. Valid options are: "" for the regular proxy and "socks" for a SOCKS5
    proxy.
    """

    tcp_keep_alive: Optional[int] = FieldInfo(alias="tcpKeepAlive", default=None)
    """
    The timeout after which a TCP keepalive packet is sent on a connection between
    Tunnel and the origin server.
    """

    tls_timeout: Optional[int] = FieldInfo(alias="tlsTimeout", default=None)
    """
    Timeout for completing a TLS handshake to your origin server, if you have chosen
    to connect Tunnel to an HTTPS server.
    """


class ConfigIngress(BaseModel):
    hostname: str
    """Public hostname for this service."""

    service: str
    """Protocol and address of destination server.

    Supported protocols: http://, https://, unix://, tcp://, ssh://, rdp://,
    unix+tls://, smb://. Alternatively can return a HTTP status code
    http_status:[code] e.g. 'http_status:404'.
    """

    origin_request: Optional[ConfigIngressOriginRequest] = FieldInfo(alias="originRequest", default=None)
    """
    Configuration parameters for the public hostname specific connection settings
    between cloudflared and origin server.
    """

    path: Optional[str] = None
    """Requests with this path route to this public hostname."""


class ConfigOriginRequestAccess(BaseModel):
    aud_tag: List[str] = FieldInfo(alias="audTag")
    """Access applications that are allowed to reach this hostname for this Tunnel.

    Audience tags can be identified in the dashboard or via the List Access policies
    API.
    """

    team_name: str = FieldInfo(alias="teamName")

    required: Optional[bool] = None
    """Deny traffic that has not fulfilled Access authorization."""


class ConfigOriginRequest(BaseModel):
    access: Optional[ConfigOriginRequestAccess] = None
    """
    For all L7 requests to this hostname, cloudflared will validate each request's
    Cf-Access-Jwt-Assertion request header.
    """

    ca_pool: Optional[str] = FieldInfo(alias="caPool", default=None)
    """Path to the certificate authority (CA) for the certificate of your origin.

    This option should be used only if your certificate is not signed by Cloudflare.
    """

    connect_timeout: Optional[int] = FieldInfo(alias="connectTimeout", default=None)
    """Timeout for establishing a new TCP connection to your origin server.

    This excludes the time taken to establish TLS, which is controlled by
    tlsTimeout.
    """

    disable_chunked_encoding: Optional[bool] = FieldInfo(alias="disableChunkedEncoding", default=None)
    """Disables chunked transfer encoding. Useful if you are running a WSGI server."""

    http2_origin: Optional[bool] = FieldInfo(alias="http2Origin", default=None)
    """Attempt to connect to origin using HTTP2. Origin must be configured as https."""

    http_host_header: Optional[str] = FieldInfo(alias="httpHostHeader", default=None)
    """Sets the HTTP Host header on requests sent to the local service."""

    keep_alive_connections: Optional[int] = FieldInfo(alias="keepAliveConnections", default=None)
    """Maximum number of idle keepalive connections between Tunnel and your origin.

    This does not restrict the total number of concurrent connections.
    """

    keep_alive_timeout: Optional[int] = FieldInfo(alias="keepAliveTimeout", default=None)
    """Timeout after which an idle keepalive connection can be discarded."""

    no_happy_eyeballs: Optional[bool] = FieldInfo(alias="noHappyEyeballs", default=None)
    """
    Disable the “happy eyeballs” algorithm for IPv4/IPv6 fallback if your local
    network has misconfigured one of the protocols.
    """

    no_tls_verify: Optional[bool] = FieldInfo(alias="noTLSVerify", default=None)
    """Disables TLS verification of the certificate presented by your origin.

    Will allow any certificate from the origin to be accepted.
    """

    origin_server_name: Optional[str] = FieldInfo(alias="originServerName", default=None)
    """Hostname that cloudflared should expect from your origin server certificate."""

    proxy_type: Optional[str] = FieldInfo(alias="proxyType", default=None)
    """
    cloudflared starts a proxy server to translate HTTP traffic into TCP when
    proxying, for example, SSH or RDP. This configures what type of proxy will be
    started. Valid options are: "" for the regular proxy and "socks" for a SOCKS5
    proxy.
    """

    tcp_keep_alive: Optional[int] = FieldInfo(alias="tcpKeepAlive", default=None)
    """
    The timeout after which a TCP keepalive packet is sent on a connection between
    Tunnel and the origin server.
    """

    tls_timeout: Optional[int] = FieldInfo(alias="tlsTimeout", default=None)
    """
    Timeout for completing a TLS handshake to your origin server, if you have chosen
    to connect Tunnel to an HTTPS server.
    """


class ConfigWARPRouting(BaseModel):
    enabled: Optional[bool] = None


class Config(BaseModel):
    ingress: Optional[List[ConfigIngress]] = None
    """List of public hostname definitions.

    At least one ingress rule needs to be defined for the tunnel.
    """

    origin_request: Optional[ConfigOriginRequest] = FieldInfo(alias="originRequest", default=None)
    """
    Configuration parameters for the public hostname specific connection settings
    between cloudflared and origin server.
    """

    warp_routing: Optional[ConfigWARPRouting] = FieldInfo(alias="warp-routing", default=None)
    """Enable private network access from WARP users to private network routes.

    This is enabled if the tunnel has an assigned route.
    """


class ConfigurationUpdateResponse(BaseModel):
    account_id: Optional[str] = None
    """Identifier"""

    config: Optional[Config] = None
    """The tunnel configuration and ingress rules."""

    created_at: Optional[datetime] = None

    source: Optional[Literal["local", "cloudflare"]] = None
    """Indicates if this is a locally or remotely configured tunnel.

    If `local`, manage the tunnel using a YAML file on the origin machine. If
    `cloudflare`, manage the tunnel's configuration on the Zero Trust dashboard.
    """

    tunnel_id: Optional[str] = None
    """UUID of the tunnel."""

    version: Optional[int] = None
    """The version of the Tunnel Configuration."""
