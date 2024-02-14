# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import (
    HealthcheckGetResponse,
    HealthcheckDeleteResponse,
    HealthcheckUpdateResponse,
    HealthcheckHealthChecksListHealthChecksResponse,
    HealthcheckHealthChecksCreateHealthCheckResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHealthchecks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        healthcheck = client.healthchecks.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )
        assert_matches_type(HealthcheckUpdateResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        healthcheck = client.healthchecks.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(HealthcheckUpdateResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.healthchecks.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthcheck = response.parse()
        assert_matches_type(HealthcheckUpdateResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.healthchecks.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthcheck = response.parse()
            assert_matches_type(HealthcheckUpdateResponse, healthcheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.healthchecks.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
                address="www.example.com",
                name="server-1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.healthchecks.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                address="www.example.com",
                name="server-1",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        healthcheck = client.healthchecks.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(HealthcheckDeleteResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.healthchecks.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthcheck = response.parse()
        assert_matches_type(HealthcheckDeleteResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.healthchecks.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthcheck = response.parse()
            assert_matches_type(HealthcheckDeleteResponse, healthcheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.healthchecks.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.healthchecks.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        healthcheck = client.healthchecks.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(HealthcheckGetResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.healthchecks.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthcheck = response.parse()
        assert_matches_type(HealthcheckGetResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.healthchecks.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthcheck = response.parse()
            assert_matches_type(HealthcheckGetResponse, healthcheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.healthchecks.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.healthchecks.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_health_checks_create_health_check(self, client: Cloudflare) -> None:
        healthcheck = client.healthchecks.health_checks_create_health_check(
            "023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )
        assert_matches_type(HealthcheckHealthChecksCreateHealthCheckResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_health_checks_create_health_check_with_all_params(self, client: Cloudflare) -> None:
        healthcheck = client.healthchecks.health_checks_create_health_check(
            "023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(HealthcheckHealthChecksCreateHealthCheckResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_health_checks_create_health_check(self, client: Cloudflare) -> None:
        response = client.healthchecks.with_raw_response.health_checks_create_health_check(
            "023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthcheck = response.parse()
        assert_matches_type(HealthcheckHealthChecksCreateHealthCheckResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_health_checks_create_health_check(self, client: Cloudflare) -> None:
        with client.healthchecks.with_streaming_response.health_checks_create_health_check(
            "023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthcheck = response.parse()
            assert_matches_type(HealthcheckHealthChecksCreateHealthCheckResponse, healthcheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_health_checks_create_health_check(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.healthchecks.with_raw_response.health_checks_create_health_check(
                "",
                address="www.example.com",
                name="server-1",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_health_checks_list_health_checks(self, client: Cloudflare) -> None:
        healthcheck = client.healthchecks.health_checks_list_health_checks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[HealthcheckHealthChecksListHealthChecksResponse], healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_health_checks_list_health_checks(self, client: Cloudflare) -> None:
        response = client.healthchecks.with_raw_response.health_checks_list_health_checks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthcheck = response.parse()
        assert_matches_type(Optional[HealthcheckHealthChecksListHealthChecksResponse], healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_health_checks_list_health_checks(self, client: Cloudflare) -> None:
        with client.healthchecks.with_streaming_response.health_checks_list_health_checks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthcheck = response.parse()
            assert_matches_type(
                Optional[HealthcheckHealthChecksListHealthChecksResponse], healthcheck, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_health_checks_list_health_checks(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.healthchecks.with_raw_response.health_checks_list_health_checks(
                "",
            )


class TestAsyncHealthchecks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        healthcheck = await async_client.healthchecks.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )
        assert_matches_type(HealthcheckUpdateResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        healthcheck = await async_client.healthchecks.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(HealthcheckUpdateResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.healthchecks.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthcheck = await response.parse()
        assert_matches_type(HealthcheckUpdateResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.healthchecks.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthcheck = await response.parse()
            assert_matches_type(HealthcheckUpdateResponse, healthcheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.healthchecks.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
                address="www.example.com",
                name="server-1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.healthchecks.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                address="www.example.com",
                name="server-1",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        healthcheck = await async_client.healthchecks.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(HealthcheckDeleteResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.healthchecks.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthcheck = await response.parse()
        assert_matches_type(HealthcheckDeleteResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.healthchecks.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthcheck = await response.parse()
            assert_matches_type(HealthcheckDeleteResponse, healthcheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.healthchecks.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.healthchecks.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        healthcheck = await async_client.healthchecks.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(HealthcheckGetResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.healthchecks.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthcheck = await response.parse()
        assert_matches_type(HealthcheckGetResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.healthchecks.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthcheck = await response.parse()
            assert_matches_type(HealthcheckGetResponse, healthcheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.healthchecks.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.healthchecks.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_health_checks_create_health_check(self, async_client: AsyncCloudflare) -> None:
        healthcheck = await async_client.healthchecks.health_checks_create_health_check(
            "023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )
        assert_matches_type(HealthcheckHealthChecksCreateHealthCheckResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_health_checks_create_health_check_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        healthcheck = await async_client.healthchecks.health_checks_create_health_check(
            "023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(HealthcheckHealthChecksCreateHealthCheckResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_health_checks_create_health_check(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.healthchecks.with_raw_response.health_checks_create_health_check(
            "023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthcheck = await response.parse()
        assert_matches_type(HealthcheckHealthChecksCreateHealthCheckResponse, healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_health_checks_create_health_check(self, async_client: AsyncCloudflare) -> None:
        async with async_client.healthchecks.with_streaming_response.health_checks_create_health_check(
            "023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthcheck = await response.parse()
            assert_matches_type(HealthcheckHealthChecksCreateHealthCheckResponse, healthcheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_health_checks_create_health_check(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.healthchecks.with_raw_response.health_checks_create_health_check(
                "",
                address="www.example.com",
                name="server-1",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_health_checks_list_health_checks(self, async_client: AsyncCloudflare) -> None:
        healthcheck = await async_client.healthchecks.health_checks_list_health_checks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[HealthcheckHealthChecksListHealthChecksResponse], healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_health_checks_list_health_checks(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.healthchecks.with_raw_response.health_checks_list_health_checks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthcheck = await response.parse()
        assert_matches_type(Optional[HealthcheckHealthChecksListHealthChecksResponse], healthcheck, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_health_checks_list_health_checks(self, async_client: AsyncCloudflare) -> None:
        async with async_client.healthchecks.with_streaming_response.health_checks_list_health_checks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthcheck = await response.parse()
            assert_matches_type(
                Optional[HealthcheckHealthChecksListHealthChecksResponse], healthcheck, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_health_checks_list_health_checks(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.healthchecks.with_raw_response.health_checks_list_health_checks(
                "",
            )
