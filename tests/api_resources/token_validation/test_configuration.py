# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.token_validation import (
    TokenConfig,
    ConfigurationEditResponse,
    ConfigurationDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfiguration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        configuration = client.token_validation.configuration.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            credentials={
                "keys": [
                    {
                        "alg": "ES256",
                        "crv": "P-256",
                        "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                        "kty": "EC",
                        "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                        "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                    }
                ]
            },
            description="Long description for Token Validation Configuration",
            title="Example Token Validation Configuration",
            token_sources=['http.request.headers["x-auth"][0]', 'http.request.cookies["Authorization"][0]'],
            token_type="JWT",
        )
        assert_matches_type(TokenConfig, configuration, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.token_validation.configuration.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            credentials={
                "keys": [
                    {
                        "alg": "ES256",
                        "crv": "P-256",
                        "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                        "kty": "EC",
                        "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                        "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                    }
                ]
            },
            description="Long description for Token Validation Configuration",
            title="Example Token Validation Configuration",
            token_sources=['http.request.headers["x-auth"][0]', 'http.request.cookies["Authorization"][0]'],
            token_type="JWT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(TokenConfig, configuration, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.token_validation.configuration.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            credentials={
                "keys": [
                    {
                        "alg": "ES256",
                        "crv": "P-256",
                        "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                        "kty": "EC",
                        "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                        "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                    }
                ]
            },
            description="Long description for Token Validation Configuration",
            title="Example Token Validation Configuration",
            token_sources=['http.request.headers["x-auth"][0]', 'http.request.cookies["Authorization"][0]'],
            token_type="JWT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(TokenConfig, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.token_validation.configuration.with_raw_response.create(
                zone_id="",
                credentials={
                    "keys": [
                        {
                            "alg": "ES256",
                            "crv": "P-256",
                            "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                            "kty": "EC",
                            "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                            "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                        }
                    ]
                },
                description="Long description for Token Validation Configuration",
                title="Example Token Validation Configuration",
                token_sources=['http.request.headers["x-auth"][0]', 'http.request.cookies["Authorization"][0]'],
                token_type="JWT",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        configuration = client.token_validation.configuration.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[TokenConfig], configuration, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        configuration = client.token_validation.configuration.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[TokenConfig], configuration, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.token_validation.configuration.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[TokenConfig], configuration, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.token_validation.configuration.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[TokenConfig], configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.token_validation.configuration.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        configuration = client.token_validation.configuration.delete(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConfigurationDeleteResponse, configuration, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.token_validation.configuration.with_raw_response.delete(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationDeleteResponse, configuration, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.token_validation.configuration.with_streaming_response.delete(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationDeleteResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.token_validation.configuration.with_raw_response.delete(
                config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.token_validation.configuration.with_raw_response.delete(
                config_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        configuration = client.token_validation.configuration.edit(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConfigurationEditResponse, configuration, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        configuration = client.token_validation.configuration.edit(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="Long description for Token Validation Configuration",
            title="Example Token Validation Configuration",
            token_sources=['http.request.headers["x-auth"][0]', 'http.request.cookies["Authorization"][0]'],
        )
        assert_matches_type(ConfigurationEditResponse, configuration, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.token_validation.configuration.with_raw_response.edit(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationEditResponse, configuration, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.token_validation.configuration.with_streaming_response.edit(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationEditResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.token_validation.configuration.with_raw_response.edit(
                config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.token_validation.configuration.with_raw_response.edit(
                config_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        configuration = client.token_validation.configuration.get(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TokenConfig, configuration, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.token_validation.configuration.with_raw_response.get(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(TokenConfig, configuration, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.token_validation.configuration.with_streaming_response.get(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(TokenConfig, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.token_validation.configuration.with_raw_response.get(
                config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.token_validation.configuration.with_raw_response.get(
                config_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncConfiguration:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.token_validation.configuration.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            credentials={
                "keys": [
                    {
                        "alg": "ES256",
                        "crv": "P-256",
                        "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                        "kty": "EC",
                        "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                        "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                    }
                ]
            },
            description="Long description for Token Validation Configuration",
            title="Example Token Validation Configuration",
            token_sources=['http.request.headers["x-auth"][0]', 'http.request.cookies["Authorization"][0]'],
            token_type="JWT",
        )
        assert_matches_type(TokenConfig, configuration, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.token_validation.configuration.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            credentials={
                "keys": [
                    {
                        "alg": "ES256",
                        "crv": "P-256",
                        "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                        "kty": "EC",
                        "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                        "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                    }
                ]
            },
            description="Long description for Token Validation Configuration",
            title="Example Token Validation Configuration",
            token_sources=['http.request.headers["x-auth"][0]', 'http.request.cookies["Authorization"][0]'],
            token_type="JWT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(TokenConfig, configuration, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.token_validation.configuration.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            credentials={
                "keys": [
                    {
                        "alg": "ES256",
                        "crv": "P-256",
                        "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                        "kty": "EC",
                        "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                        "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                    }
                ]
            },
            description="Long description for Token Validation Configuration",
            title="Example Token Validation Configuration",
            token_sources=['http.request.headers["x-auth"][0]', 'http.request.cookies["Authorization"][0]'],
            token_type="JWT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(TokenConfig, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.token_validation.configuration.with_raw_response.create(
                zone_id="",
                credentials={
                    "keys": [
                        {
                            "alg": "ES256",
                            "crv": "P-256",
                            "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                            "kty": "EC",
                            "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                            "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                        }
                    ]
                },
                description="Long description for Token Validation Configuration",
                title="Example Token Validation Configuration",
                token_sources=['http.request.headers["x-auth"][0]', 'http.request.cookies["Authorization"][0]'],
                token_type="JWT",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.token_validation.configuration.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[TokenConfig], configuration, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.token_validation.configuration.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[TokenConfig], configuration, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.token_validation.configuration.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[TokenConfig], configuration, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.token_validation.configuration.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[TokenConfig], configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.token_validation.configuration.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.token_validation.configuration.delete(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConfigurationDeleteResponse, configuration, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.token_validation.configuration.with_raw_response.delete(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationDeleteResponse, configuration, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.token_validation.configuration.with_streaming_response.delete(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationDeleteResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.token_validation.configuration.with_raw_response.delete(
                config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.token_validation.configuration.with_raw_response.delete(
                config_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.token_validation.configuration.edit(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ConfigurationEditResponse, configuration, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.token_validation.configuration.edit(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="Long description for Token Validation Configuration",
            title="Example Token Validation Configuration",
            token_sources=['http.request.headers["x-auth"][0]', 'http.request.cookies["Authorization"][0]'],
        )
        assert_matches_type(ConfigurationEditResponse, configuration, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.token_validation.configuration.with_raw_response.edit(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationEditResponse, configuration, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.token_validation.configuration.with_streaming_response.edit(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationEditResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.token_validation.configuration.with_raw_response.edit(
                config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.token_validation.configuration.with_raw_response.edit(
                config_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.token_validation.configuration.get(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TokenConfig, configuration, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.token_validation.configuration.with_raw_response.get(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(TokenConfig, configuration, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.token_validation.configuration.with_streaming_response.get(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(TokenConfig, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.token_validation.configuration.with_raw_response.get(
                config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.token_validation.configuration.with_raw_response.get(
                config_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
