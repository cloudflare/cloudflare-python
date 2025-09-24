# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.smart_shield import (
    SmartShieldGetResponse,
    SmartShieldUpdateResponse,
    SmartShieldGetHealthcheckResponse,
    SmartShieldEditHealthcheckResponse,
    SmartShieldListHealthchecksResponse,
    SmartShieldCreateHealthcheckResponse,
    SmartShieldDeleteHealthcheckResponse,
    SmartShieldUpdateHealthcheckResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSmartShield:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        smart_shield = client.smart_shield.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SmartShieldUpdateResponse, smart_shield, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        smart_shield = client.smart_shield.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            cache_reserve={"value": "on"},
            regional_tiered_cache={"value": "on"},
            smart_routing={"value": "on"},
            smart_tiered_cache={"value": "on"},
        )
        assert_matches_type(SmartShieldUpdateResponse, smart_shield, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.smart_shield.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = response.parse()
        assert_matches_type(SmartShieldUpdateResponse, smart_shield, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.smart_shield.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = response.parse()
            assert_matches_type(SmartShieldUpdateResponse, smart_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.smart_shield.with_raw_response.update(
                zone_id="",
            )

    @parametrize
    def test_method_create_healthcheck(self, client: Cloudflare) -> None:
        smart_shield = client.smart_shield.create_healthcheck(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )
        assert_matches_type(SmartShieldCreateHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    def test_method_create_healthcheck_with_all_params(self, client: Cloudflare) -> None:
        smart_shield = client.smart_shield.create_healthcheck(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
            check_regions=["WEU", "ENAM"],
            consecutive_fails=0,
            consecutive_successes=0,
            description="Health check for www.example.com",
            http_config={
                "allow_insecure": True,
                "expected_body": "success",
                "expected_codes": ["2xx", "302"],
                "follow_redirects": True,
                "header": {
                    "Host": ["example.com"],
                    "X-App-ID": ["abc123"],
                },
                "method": "GET",
                "path": "/health",
                "port": 0,
            },
            interval=0,
            retries=0,
            suspended=True,
            tcp_config={
                "method": "connection_established",
                "port": 0,
            },
            api_timeout=0,
            type="HTTPS",
        )
        assert_matches_type(SmartShieldCreateHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    def test_raw_response_create_healthcheck(self, client: Cloudflare) -> None:
        response = client.smart_shield.with_raw_response.create_healthcheck(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = response.parse()
        assert_matches_type(SmartShieldCreateHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    def test_streaming_response_create_healthcheck(self, client: Cloudflare) -> None:
        with client.smart_shield.with_streaming_response.create_healthcheck(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = response.parse()
            assert_matches_type(SmartShieldCreateHealthcheckResponse, smart_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_healthcheck(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.smart_shield.with_raw_response.create_healthcheck(
                zone_id="",
                address="www.example.com",
                name="server-1",
            )

    @parametrize
    def test_method_delete_healthcheck(self, client: Cloudflare) -> None:
        smart_shield = client.smart_shield.delete_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SmartShieldDeleteHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    def test_raw_response_delete_healthcheck(self, client: Cloudflare) -> None:
        response = client.smart_shield.with_raw_response.delete_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = response.parse()
        assert_matches_type(SmartShieldDeleteHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    def test_streaming_response_delete_healthcheck(self, client: Cloudflare) -> None:
        with client.smart_shield.with_streaming_response.delete_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = response.parse()
            assert_matches_type(SmartShieldDeleteHealthcheckResponse, smart_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_healthcheck(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.smart_shield.with_raw_response.delete_healthcheck(
                healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `healthcheck_id` but received ''"):
            client.smart_shield.with_raw_response.delete_healthcheck(
                healthcheck_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit_healthcheck(self, client: Cloudflare) -> None:
        smart_shield = client.smart_shield.edit_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )
        assert_matches_type(SmartShieldEditHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    def test_method_edit_healthcheck_with_all_params(self, client: Cloudflare) -> None:
        smart_shield = client.smart_shield.edit_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
            check_regions=["WEU", "ENAM"],
            consecutive_fails=0,
            consecutive_successes=0,
            description="Health check for www.example.com",
            http_config={
                "allow_insecure": True,
                "expected_body": "success",
                "expected_codes": ["2xx", "302"],
                "follow_redirects": True,
                "header": {
                    "Host": ["example.com"],
                    "X-App-ID": ["abc123"],
                },
                "method": "GET",
                "path": "/health",
                "port": 0,
            },
            interval=0,
            retries=0,
            suspended=True,
            tcp_config={
                "method": "connection_established",
                "port": 0,
            },
            api_timeout=0,
            type="HTTPS",
        )
        assert_matches_type(SmartShieldEditHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    def test_raw_response_edit_healthcheck(self, client: Cloudflare) -> None:
        response = client.smart_shield.with_raw_response.edit_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = response.parse()
        assert_matches_type(SmartShieldEditHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    def test_streaming_response_edit_healthcheck(self, client: Cloudflare) -> None:
        with client.smart_shield.with_streaming_response.edit_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = response.parse()
            assert_matches_type(SmartShieldEditHealthcheckResponse, smart_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_healthcheck(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.smart_shield.with_raw_response.edit_healthcheck(
                healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                address="www.example.com",
                name="server-1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `healthcheck_id` but received ''"):
            client.smart_shield.with_raw_response.edit_healthcheck(
                healthcheck_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                address="www.example.com",
                name="server-1",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        smart_shield = client.smart_shield.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SmartShieldGetResponse, smart_shield, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.smart_shield.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = response.parse()
        assert_matches_type(SmartShieldGetResponse, smart_shield, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.smart_shield.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = response.parse()
            assert_matches_type(SmartShieldGetResponse, smart_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.smart_shield.with_raw_response.get(
                zone_id="",
            )

    @parametrize
    def test_method_get_healthcheck(self, client: Cloudflare) -> None:
        smart_shield = client.smart_shield.get_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SmartShieldGetHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    def test_raw_response_get_healthcheck(self, client: Cloudflare) -> None:
        response = client.smart_shield.with_raw_response.get_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = response.parse()
        assert_matches_type(SmartShieldGetHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    def test_streaming_response_get_healthcheck(self, client: Cloudflare) -> None:
        with client.smart_shield.with_streaming_response.get_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = response.parse()
            assert_matches_type(SmartShieldGetHealthcheckResponse, smart_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_healthcheck(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.smart_shield.with_raw_response.get_healthcheck(
                healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `healthcheck_id` but received ''"):
            client.smart_shield.with_raw_response.get_healthcheck(
                healthcheck_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list_healthchecks(self, client: Cloudflare) -> None:
        smart_shield = client.smart_shield.list_healthchecks(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            SyncV4PagePaginationArray[SmartShieldListHealthchecksResponse], smart_shield, path=["response"]
        )

    @parametrize
    def test_method_list_healthchecks_with_all_params(self, client: Cloudflare) -> None:
        smart_shield = client.smart_shield.list_healthchecks(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=5,
        )
        assert_matches_type(
            SyncV4PagePaginationArray[SmartShieldListHealthchecksResponse], smart_shield, path=["response"]
        )

    @parametrize
    def test_raw_response_list_healthchecks(self, client: Cloudflare) -> None:
        response = client.smart_shield.with_raw_response.list_healthchecks(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = response.parse()
        assert_matches_type(
            SyncV4PagePaginationArray[SmartShieldListHealthchecksResponse], smart_shield, path=["response"]
        )

    @parametrize
    def test_streaming_response_list_healthchecks(self, client: Cloudflare) -> None:
        with client.smart_shield.with_streaming_response.list_healthchecks(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = response.parse()
            assert_matches_type(
                SyncV4PagePaginationArray[SmartShieldListHealthchecksResponse], smart_shield, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_healthchecks(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.smart_shield.with_raw_response.list_healthchecks(
                zone_id="",
            )

    @parametrize
    def test_method_update_healthcheck(self, client: Cloudflare) -> None:
        smart_shield = client.smart_shield.update_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            errors=[
                {
                    "code": 1000,
                    "message": "message",
                }
            ],
            messages=[
                {
                    "code": 1000,
                    "message": "message",
                }
            ],
            result={},
            success=True,
        )
        assert_matches_type(SmartShieldUpdateHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    def test_method_update_healthcheck_with_all_params(self, client: Cloudflare) -> None:
        smart_shield = client.smart_shield.update_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            errors=[
                {
                    "code": 1000,
                    "message": "message",
                    "documentation_url": "documentation_url",
                    "source": {"pointer": "pointer"},
                }
            ],
            messages=[
                {
                    "code": 1000,
                    "message": "message",
                    "documentation_url": "documentation_url",
                    "source": {"pointer": "pointer"},
                }
            ],
            result={
                "address": "www.example.com",
                "check_regions": ["WEU", "ENAM"],
                "consecutive_fails": 0,
                "consecutive_successes": 0,
                "description": "Health check for www.example.com",
                "http_config": {
                    "allow_insecure": True,
                    "expected_body": "success",
                    "expected_codes": ["2xx", "302"],
                    "follow_redirects": True,
                    "header": {
                        "Host": ["example.com"],
                        "X-App-ID": ["abc123"],
                    },
                    "method": "GET",
                    "path": "/health",
                    "port": 0,
                },
                "interval": 0,
                "name": "server-1",
                "retries": 0,
                "suspended": True,
                "tcp_config": {
                    "method": "connection_established",
                    "port": 0,
                },
                "timeout": 0,
                "type": "HTTPS",
            },
            success=True,
        )
        assert_matches_type(SmartShieldUpdateHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    def test_raw_response_update_healthcheck(self, client: Cloudflare) -> None:
        response = client.smart_shield.with_raw_response.update_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            errors=[
                {
                    "code": 1000,
                    "message": "message",
                }
            ],
            messages=[
                {
                    "code": 1000,
                    "message": "message",
                }
            ],
            result={},
            success=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = response.parse()
        assert_matches_type(SmartShieldUpdateHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    def test_streaming_response_update_healthcheck(self, client: Cloudflare) -> None:
        with client.smart_shield.with_streaming_response.update_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            errors=[
                {
                    "code": 1000,
                    "message": "message",
                }
            ],
            messages=[
                {
                    "code": 1000,
                    "message": "message",
                }
            ],
            result={},
            success=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = response.parse()
            assert_matches_type(SmartShieldUpdateHealthcheckResponse, smart_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_healthcheck(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.smart_shield.with_raw_response.update_healthcheck(
                healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                errors=[
                    {
                        "code": 1000,
                        "message": "message",
                    }
                ],
                messages=[
                    {
                        "code": 1000,
                        "message": "message",
                    }
                ],
                result={},
                success=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `healthcheck_id` but received ''"):
            client.smart_shield.with_raw_response.update_healthcheck(
                healthcheck_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                errors=[
                    {
                        "code": 1000,
                        "message": "message",
                    }
                ],
                messages=[
                    {
                        "code": 1000,
                        "message": "message",
                    }
                ],
                result={},
                success=True,
            )


class TestAsyncSmartShield:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        smart_shield = await async_client.smart_shield.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SmartShieldUpdateResponse, smart_shield, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        smart_shield = await async_client.smart_shield.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            cache_reserve={"value": "on"},
            regional_tiered_cache={"value": "on"},
            smart_routing={"value": "on"},
            smart_tiered_cache={"value": "on"},
        )
        assert_matches_type(SmartShieldUpdateResponse, smart_shield, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.smart_shield.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = await response.parse()
        assert_matches_type(SmartShieldUpdateResponse, smart_shield, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.smart_shield.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = await response.parse()
            assert_matches_type(SmartShieldUpdateResponse, smart_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.smart_shield.with_raw_response.update(
                zone_id="",
            )

    @parametrize
    async def test_method_create_healthcheck(self, async_client: AsyncCloudflare) -> None:
        smart_shield = await async_client.smart_shield.create_healthcheck(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )
        assert_matches_type(SmartShieldCreateHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    async def test_method_create_healthcheck_with_all_params(self, async_client: AsyncCloudflare) -> None:
        smart_shield = await async_client.smart_shield.create_healthcheck(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
            check_regions=["WEU", "ENAM"],
            consecutive_fails=0,
            consecutive_successes=0,
            description="Health check for www.example.com",
            http_config={
                "allow_insecure": True,
                "expected_body": "success",
                "expected_codes": ["2xx", "302"],
                "follow_redirects": True,
                "header": {
                    "Host": ["example.com"],
                    "X-App-ID": ["abc123"],
                },
                "method": "GET",
                "path": "/health",
                "port": 0,
            },
            interval=0,
            retries=0,
            suspended=True,
            tcp_config={
                "method": "connection_established",
                "port": 0,
            },
            api_timeout=0,
            type="HTTPS",
        )
        assert_matches_type(SmartShieldCreateHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    async def test_raw_response_create_healthcheck(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.smart_shield.with_raw_response.create_healthcheck(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = await response.parse()
        assert_matches_type(SmartShieldCreateHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    async def test_streaming_response_create_healthcheck(self, async_client: AsyncCloudflare) -> None:
        async with async_client.smart_shield.with_streaming_response.create_healthcheck(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = await response.parse()
            assert_matches_type(SmartShieldCreateHealthcheckResponse, smart_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_healthcheck(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.smart_shield.with_raw_response.create_healthcheck(
                zone_id="",
                address="www.example.com",
                name="server-1",
            )

    @parametrize
    async def test_method_delete_healthcheck(self, async_client: AsyncCloudflare) -> None:
        smart_shield = await async_client.smart_shield.delete_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SmartShieldDeleteHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    async def test_raw_response_delete_healthcheck(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.smart_shield.with_raw_response.delete_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = await response.parse()
        assert_matches_type(SmartShieldDeleteHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    async def test_streaming_response_delete_healthcheck(self, async_client: AsyncCloudflare) -> None:
        async with async_client.smart_shield.with_streaming_response.delete_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = await response.parse()
            assert_matches_type(SmartShieldDeleteHealthcheckResponse, smart_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_healthcheck(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.smart_shield.with_raw_response.delete_healthcheck(
                healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `healthcheck_id` but received ''"):
            await async_client.smart_shield.with_raw_response.delete_healthcheck(
                healthcheck_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit_healthcheck(self, async_client: AsyncCloudflare) -> None:
        smart_shield = await async_client.smart_shield.edit_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )
        assert_matches_type(SmartShieldEditHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    async def test_method_edit_healthcheck_with_all_params(self, async_client: AsyncCloudflare) -> None:
        smart_shield = await async_client.smart_shield.edit_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
            check_regions=["WEU", "ENAM"],
            consecutive_fails=0,
            consecutive_successes=0,
            description="Health check for www.example.com",
            http_config={
                "allow_insecure": True,
                "expected_body": "success",
                "expected_codes": ["2xx", "302"],
                "follow_redirects": True,
                "header": {
                    "Host": ["example.com"],
                    "X-App-ID": ["abc123"],
                },
                "method": "GET",
                "path": "/health",
                "port": 0,
            },
            interval=0,
            retries=0,
            suspended=True,
            tcp_config={
                "method": "connection_established",
                "port": 0,
            },
            api_timeout=0,
            type="HTTPS",
        )
        assert_matches_type(SmartShieldEditHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    async def test_raw_response_edit_healthcheck(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.smart_shield.with_raw_response.edit_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = await response.parse()
        assert_matches_type(SmartShieldEditHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    async def test_streaming_response_edit_healthcheck(self, async_client: AsyncCloudflare) -> None:
        async with async_client.smart_shield.with_streaming_response.edit_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = await response.parse()
            assert_matches_type(SmartShieldEditHealthcheckResponse, smart_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_healthcheck(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.smart_shield.with_raw_response.edit_healthcheck(
                healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                address="www.example.com",
                name="server-1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `healthcheck_id` but received ''"):
            await async_client.smart_shield.with_raw_response.edit_healthcheck(
                healthcheck_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                address="www.example.com",
                name="server-1",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        smart_shield = await async_client.smart_shield.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SmartShieldGetResponse, smart_shield, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.smart_shield.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = await response.parse()
        assert_matches_type(SmartShieldGetResponse, smart_shield, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.smart_shield.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = await response.parse()
            assert_matches_type(SmartShieldGetResponse, smart_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.smart_shield.with_raw_response.get(
                zone_id="",
            )

    @parametrize
    async def test_method_get_healthcheck(self, async_client: AsyncCloudflare) -> None:
        smart_shield = await async_client.smart_shield.get_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SmartShieldGetHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    async def test_raw_response_get_healthcheck(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.smart_shield.with_raw_response.get_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = await response.parse()
        assert_matches_type(SmartShieldGetHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    async def test_streaming_response_get_healthcheck(self, async_client: AsyncCloudflare) -> None:
        async with async_client.smart_shield.with_streaming_response.get_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = await response.parse()
            assert_matches_type(SmartShieldGetHealthcheckResponse, smart_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_healthcheck(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.smart_shield.with_raw_response.get_healthcheck(
                healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `healthcheck_id` but received ''"):
            await async_client.smart_shield.with_raw_response.get_healthcheck(
                healthcheck_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list_healthchecks(self, async_client: AsyncCloudflare) -> None:
        smart_shield = await async_client.smart_shield.list_healthchecks(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            AsyncV4PagePaginationArray[SmartShieldListHealthchecksResponse], smart_shield, path=["response"]
        )

    @parametrize
    async def test_method_list_healthchecks_with_all_params(self, async_client: AsyncCloudflare) -> None:
        smart_shield = await async_client.smart_shield.list_healthchecks(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=5,
        )
        assert_matches_type(
            AsyncV4PagePaginationArray[SmartShieldListHealthchecksResponse], smart_shield, path=["response"]
        )

    @parametrize
    async def test_raw_response_list_healthchecks(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.smart_shield.with_raw_response.list_healthchecks(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = await response.parse()
        assert_matches_type(
            AsyncV4PagePaginationArray[SmartShieldListHealthchecksResponse], smart_shield, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list_healthchecks(self, async_client: AsyncCloudflare) -> None:
        async with async_client.smart_shield.with_streaming_response.list_healthchecks(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = await response.parse()
            assert_matches_type(
                AsyncV4PagePaginationArray[SmartShieldListHealthchecksResponse], smart_shield, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_healthchecks(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.smart_shield.with_raw_response.list_healthchecks(
                zone_id="",
            )

    @parametrize
    async def test_method_update_healthcheck(self, async_client: AsyncCloudflare) -> None:
        smart_shield = await async_client.smart_shield.update_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            errors=[
                {
                    "code": 1000,
                    "message": "message",
                }
            ],
            messages=[
                {
                    "code": 1000,
                    "message": "message",
                }
            ],
            result={},
            success=True,
        )
        assert_matches_type(SmartShieldUpdateHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    async def test_method_update_healthcheck_with_all_params(self, async_client: AsyncCloudflare) -> None:
        smart_shield = await async_client.smart_shield.update_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            errors=[
                {
                    "code": 1000,
                    "message": "message",
                    "documentation_url": "documentation_url",
                    "source": {"pointer": "pointer"},
                }
            ],
            messages=[
                {
                    "code": 1000,
                    "message": "message",
                    "documentation_url": "documentation_url",
                    "source": {"pointer": "pointer"},
                }
            ],
            result={
                "address": "www.example.com",
                "check_regions": ["WEU", "ENAM"],
                "consecutive_fails": 0,
                "consecutive_successes": 0,
                "description": "Health check for www.example.com",
                "http_config": {
                    "allow_insecure": True,
                    "expected_body": "success",
                    "expected_codes": ["2xx", "302"],
                    "follow_redirects": True,
                    "header": {
                        "Host": ["example.com"],
                        "X-App-ID": ["abc123"],
                    },
                    "method": "GET",
                    "path": "/health",
                    "port": 0,
                },
                "interval": 0,
                "name": "server-1",
                "retries": 0,
                "suspended": True,
                "tcp_config": {
                    "method": "connection_established",
                    "port": 0,
                },
                "timeout": 0,
                "type": "HTTPS",
            },
            success=True,
        )
        assert_matches_type(SmartShieldUpdateHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    async def test_raw_response_update_healthcheck(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.smart_shield.with_raw_response.update_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            errors=[
                {
                    "code": 1000,
                    "message": "message",
                }
            ],
            messages=[
                {
                    "code": 1000,
                    "message": "message",
                }
            ],
            result={},
            success=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_shield = await response.parse()
        assert_matches_type(SmartShieldUpdateHealthcheckResponse, smart_shield, path=["response"])

    @parametrize
    async def test_streaming_response_update_healthcheck(self, async_client: AsyncCloudflare) -> None:
        async with async_client.smart_shield.with_streaming_response.update_healthcheck(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            errors=[
                {
                    "code": 1000,
                    "message": "message",
                }
            ],
            messages=[
                {
                    "code": 1000,
                    "message": "message",
                }
            ],
            result={},
            success=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_shield = await response.parse()
            assert_matches_type(SmartShieldUpdateHealthcheckResponse, smart_shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_healthcheck(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.smart_shield.with_raw_response.update_healthcheck(
                healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                errors=[
                    {
                        "code": 1000,
                        "message": "message",
                    }
                ],
                messages=[
                    {
                        "code": 1000,
                        "message": "message",
                    }
                ],
                result={},
                success=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `healthcheck_id` but received ''"):
            await async_client.smart_shield.with_raw_response.update_healthcheck(
                healthcheck_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                errors=[
                    {
                        "code": 1000,
                        "message": "message",
                    }
                ],
                messages=[
                    {
                        "code": 1000,
                        "message": "message",
                    }
                ],
                result={},
                success=True,
            )
