# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.api_gateway import (
    Configuration,
    ConfigurationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        configuration = client.api_gateway.configurations.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auth_id_characteristics=[
                {
                    "name": "authorization",
                    "type": "header",
                }
            ],
        )
        assert_matches_type(ConfigurationUpdateResponse, configuration, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.api_gateway.configurations.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auth_id_characteristics=[
                {
                    "name": "authorization",
                    "type": "header",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationUpdateResponse, configuration, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.api_gateway.configurations.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auth_id_characteristics=[
                {
                    "name": "authorization",
                    "type": "header",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationUpdateResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.configurations.with_raw_response.update(
                zone_id="",
                auth_id_characteristics=[
                    {
                        "name": "authorization",
                        "type": "header",
                    }
                ],
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        configuration = client.api_gateway.configurations.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Configuration, configuration, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        configuration = client.api_gateway.configurations.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            properties=["auth_id_characteristics"],
        )
        assert_matches_type(Configuration, configuration, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.api_gateway.configurations.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(Configuration, configuration, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.api_gateway.configurations.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(Configuration, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.configurations.with_raw_response.get(
                zone_id="",
            )


class TestAsyncConfigurations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.api_gateway.configurations.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auth_id_characteristics=[
                {
                    "name": "authorization",
                    "type": "header",
                }
            ],
        )
        assert_matches_type(ConfigurationUpdateResponse, configuration, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.configurations.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auth_id_characteristics=[
                {
                    "name": "authorization",
                    "type": "header",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationUpdateResponse, configuration, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.configurations.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auth_id_characteristics=[
                {
                    "name": "authorization",
                    "type": "header",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationUpdateResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.configurations.with_raw_response.update(
                zone_id="",
                auth_id_characteristics=[
                    {
                        "name": "authorization",
                        "type": "header",
                    }
                ],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.api_gateway.configurations.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Configuration, configuration, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.api_gateway.configurations.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            properties=["auth_id_characteristics"],
        )
        assert_matches_type(Configuration, configuration, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.configurations.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(Configuration, configuration, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.configurations.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(Configuration, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.configurations.with_raw_response.get(
                zone_id="",
            )
