# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types import ActivationCheckPutZonesZoneIDActivationCheckResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActivationChecks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_put_zones_zone_id_activation_check(self, client: Cloudflare) -> None:
        activation_check = client.activation_checks.put_zones_zone_id_activation_check(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ActivationCheckPutZonesZoneIDActivationCheckResponse, activation_check, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_put_zones_zone_id_activation_check(self, client: Cloudflare) -> None:
        response = client.activation_checks.with_raw_response.put_zones_zone_id_activation_check(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activation_check = response.parse()
        assert_matches_type(ActivationCheckPutZonesZoneIDActivationCheckResponse, activation_check, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_put_zones_zone_id_activation_check(self, client: Cloudflare) -> None:
        with client.activation_checks.with_streaming_response.put_zones_zone_id_activation_check(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activation_check = response.parse()
            assert_matches_type(
                ActivationCheckPutZonesZoneIDActivationCheckResponse, activation_check, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_put_zones_zone_id_activation_check(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.activation_checks.with_raw_response.put_zones_zone_id_activation_check(
                "",
            )


class TestAsyncActivationChecks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_put_zones_zone_id_activation_check(self, async_client: AsyncCloudflare) -> None:
        activation_check = await async_client.activation_checks.put_zones_zone_id_activation_check(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ActivationCheckPutZonesZoneIDActivationCheckResponse, activation_check, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_put_zones_zone_id_activation_check(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.activation_checks.with_raw_response.put_zones_zone_id_activation_check(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activation_check = await response.parse()
        assert_matches_type(ActivationCheckPutZonesZoneIDActivationCheckResponse, activation_check, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_put_zones_zone_id_activation_check(self, async_client: AsyncCloudflare) -> None:
        async with async_client.activation_checks.with_streaming_response.put_zones_zone_id_activation_check(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activation_check = await response.parse()
            assert_matches_type(
                ActivationCheckPutZonesZoneIDActivationCheckResponse, activation_check, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_put_zones_zone_id_activation_check(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.activation_checks.with_raw_response.put_zones_zone_id_activation_check(
                "",
            )
