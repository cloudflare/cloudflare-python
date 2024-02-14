# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.page_shields import (
    ConnectionGetResponse,
    ConnectionPageShieldListPageShieldConnectionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        connection = client.page_shields.connections.get(
            "c9ef84a6bf5e47138c75d95e2f933e8f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConnectionGetResponse, connection, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.page_shields.connections.with_raw_response.get(
            "c9ef84a6bf5e47138c75d95e2f933e8f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionGetResponse, connection, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.page_shields.connections.with_streaming_response.get(
            "c9ef84a6bf5e47138c75d95e2f933e8f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionGetResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.page_shields.connections.with_raw_response.get(
                "c9ef84a6bf5e47138c75d95e2f933e8f",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.page_shields.connections.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_page_shield_list_page_shield_connections(self, client: Cloudflare) -> None:
        connection = client.page_shields.connections.page_shield_list_page_shield_connections(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[ConnectionPageShieldListPageShieldConnectionsResponse], connection, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_page_shield_list_page_shield_connections_with_all_params(self, client: Cloudflare) -> None:
        connection = client.page_shields.connections.page_shield_list_page_shield_connections(
            "023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            exclude_cdn_cgi=True,
            exclude_urls="blog.cloudflare.com,www.example",
            export="csv",
            hosts="blog.cloudflare.com,www.example*,*cloudflare.com",
            order_by="first_seen_at",
            page="2",
            page_url="example.com/page,*/checkout,example.com/*,*checkout*",
            per_page=100,
            prioritize_malicious=True,
            status="active,inactive",
            urls="blog.cloudflare.com,www.example",
        )
        assert_matches_type(
            Optional[ConnectionPageShieldListPageShieldConnectionsResponse], connection, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_page_shield_list_page_shield_connections(self, client: Cloudflare) -> None:
        response = client.page_shields.connections.with_raw_response.page_shield_list_page_shield_connections(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(
            Optional[ConnectionPageShieldListPageShieldConnectionsResponse], connection, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_page_shield_list_page_shield_connections(self, client: Cloudflare) -> None:
        with client.page_shields.connections.with_streaming_response.page_shield_list_page_shield_connections(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(
                Optional[ConnectionPageShieldListPageShieldConnectionsResponse], connection, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_page_shield_list_page_shield_connections(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.page_shields.connections.with_raw_response.page_shield_list_page_shield_connections(
                "",
            )


class TestAsyncConnections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        connection = await async_client.page_shields.connections.get(
            "c9ef84a6bf5e47138c75d95e2f933e8f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConnectionGetResponse, connection, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.page_shields.connections.with_raw_response.get(
            "c9ef84a6bf5e47138c75d95e2f933e8f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionGetResponse, connection, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.page_shields.connections.with_streaming_response.get(
            "c9ef84a6bf5e47138c75d95e2f933e8f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionGetResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.page_shields.connections.with_raw_response.get(
                "c9ef84a6bf5e47138c75d95e2f933e8f",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.page_shields.connections.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_page_shield_list_page_shield_connections(self, async_client: AsyncCloudflare) -> None:
        connection = await async_client.page_shields.connections.page_shield_list_page_shield_connections(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[ConnectionPageShieldListPageShieldConnectionsResponse], connection, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_page_shield_list_page_shield_connections_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        connection = await async_client.page_shields.connections.page_shield_list_page_shield_connections(
            "023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            exclude_cdn_cgi=True,
            exclude_urls="blog.cloudflare.com,www.example",
            export="csv",
            hosts="blog.cloudflare.com,www.example*,*cloudflare.com",
            order_by="first_seen_at",
            page="2",
            page_url="example.com/page,*/checkout,example.com/*,*checkout*",
            per_page=100,
            prioritize_malicious=True,
            status="active,inactive",
            urls="blog.cloudflare.com,www.example",
        )
        assert_matches_type(
            Optional[ConnectionPageShieldListPageShieldConnectionsResponse], connection, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_page_shield_list_page_shield_connections(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.page_shields.connections.with_raw_response.page_shield_list_page_shield_connections(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(
            Optional[ConnectionPageShieldListPageShieldConnectionsResponse], connection, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_page_shield_list_page_shield_connections(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.page_shields.connections.with_streaming_response.page_shield_list_page_shield_connections(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(
                Optional[ConnectionPageShieldListPageShieldConnectionsResponse], connection, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_page_shield_list_page_shield_connections(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.page_shields.connections.with_raw_response.page_shield_list_page_shield_connections(
                "",
            )
