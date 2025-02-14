# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.tunnels.cloudflared import (
    ConfigurationGetResponse,
    ConfigurationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        configuration = client.zero_trust.tunnels.cloudflared.configurations.update(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        configuration = client.zero_trust.tunnels.cloudflared.configurations.update(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "ingress": [
                    {
                        "hostname": "tunnel.example.com",
                        "service": "https://localhost:8001",
                        "origin_request": {
                            "access": {
                                "aud_tag": ["string"],
                                "team_name": "teamName",
                                "required": True,
                            },
                            "ca_pool": "caPool",
                            "connect_timeout": 0,
                            "disable_chunked_encoding": True,
                            "http2_origin": True,
                            "http_host_header": "httpHostHeader",
                            "keep_alive_connections": 0,
                            "keep_alive_timeout": 0,
                            "no_happy_eyeballs": True,
                            "no_tls_verify": True,
                            "origin_server_name": "originServerName",
                            "proxy_type": "proxyType",
                            "tcp_keep_alive": 0,
                            "tls_timeout": 0,
                        },
                        "path": "subpath",
                    }
                ],
                "origin_request": {
                    "access": {
                        "aud_tag": ["string"],
                        "team_name": "teamName",
                        "required": True,
                    },
                    "ca_pool": "caPool",
                    "connect_timeout": 0,
                    "disable_chunked_encoding": True,
                    "http2_origin": True,
                    "http_host_header": "httpHostHeader",
                    "keep_alive_connections": 0,
                    "keep_alive_timeout": 0,
                    "no_happy_eyeballs": True,
                    "no_tls_verify": True,
                    "origin_server_name": "originServerName",
                    "proxy_type": "proxyType",
                    "tcp_keep_alive": 0,
                    "tls_timeout": 0,
                },
            },
        )
        assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.tunnels.cloudflared.configurations.with_raw_response.update(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.tunnels.cloudflared.configurations.with_streaming_response.update(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.tunnels.cloudflared.configurations.with_raw_response.update(
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            client.zero_trust.tunnels.cloudflared.configurations.with_raw_response.update(
                tunnel_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        configuration = client.zero_trust.tunnels.cloudflared.configurations.get(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ConfigurationGetResponse], configuration, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.tunnels.cloudflared.configurations.with_raw_response.get(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(Optional[ConfigurationGetResponse], configuration, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.tunnels.cloudflared.configurations.with_streaming_response.get(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(Optional[ConfigurationGetResponse], configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.tunnels.cloudflared.configurations.with_raw_response.get(
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            client.zero_trust.tunnels.cloudflared.configurations.with_raw_response.get(
                tunnel_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncConfigurations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.zero_trust.tunnels.cloudflared.configurations.update(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.zero_trust.tunnels.cloudflared.configurations.update(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "ingress": [
                    {
                        "hostname": "tunnel.example.com",
                        "service": "https://localhost:8001",
                        "origin_request": {
                            "access": {
                                "aud_tag": ["string"],
                                "team_name": "teamName",
                                "required": True,
                            },
                            "ca_pool": "caPool",
                            "connect_timeout": 0,
                            "disable_chunked_encoding": True,
                            "http2_origin": True,
                            "http_host_header": "httpHostHeader",
                            "keep_alive_connections": 0,
                            "keep_alive_timeout": 0,
                            "no_happy_eyeballs": True,
                            "no_tls_verify": True,
                            "origin_server_name": "originServerName",
                            "proxy_type": "proxyType",
                            "tcp_keep_alive": 0,
                            "tls_timeout": 0,
                        },
                        "path": "subpath",
                    }
                ],
                "origin_request": {
                    "access": {
                        "aud_tag": ["string"],
                        "team_name": "teamName",
                        "required": True,
                    },
                    "ca_pool": "caPool",
                    "connect_timeout": 0,
                    "disable_chunked_encoding": True,
                    "http2_origin": True,
                    "http_host_header": "httpHostHeader",
                    "keep_alive_connections": 0,
                    "keep_alive_timeout": 0,
                    "no_happy_eyeballs": True,
                    "no_tls_verify": True,
                    "origin_server_name": "originServerName",
                    "proxy_type": "proxyType",
                    "tcp_keep_alive": 0,
                    "tls_timeout": 0,
                },
            },
        )
        assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.tunnels.cloudflared.configurations.with_raw_response.update(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.tunnels.cloudflared.configurations.with_streaming_response.update(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(Optional[ConfigurationUpdateResponse], configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.tunnels.cloudflared.configurations.with_raw_response.update(
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            await async_client.zero_trust.tunnels.cloudflared.configurations.with_raw_response.update(
                tunnel_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.zero_trust.tunnels.cloudflared.configurations.get(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ConfigurationGetResponse], configuration, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.tunnels.cloudflared.configurations.with_raw_response.get(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(Optional[ConfigurationGetResponse], configuration, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.tunnels.cloudflared.configurations.with_streaming_response.get(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(Optional[ConfigurationGetResponse], configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.tunnels.cloudflared.configurations.with_raw_response.get(
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            await async_client.zero_trust.tunnels.cloudflared.configurations.with_raw_response.get(
                tunnel_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
