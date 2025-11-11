# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.token_validation.configuration import CredentialUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        credential = client.token_validation.configuration.credentials.update(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            keys=[
                {
                    "alg": "ES256",
                    "crv": "P-256",
                    "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                    "kty": "EC",
                    "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                    "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                }
            ],
        )
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.token_validation.configuration.credentials.with_raw_response.update(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            keys=[
                {
                    "alg": "ES256",
                    "crv": "P-256",
                    "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                    "kty": "EC",
                    "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                    "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.token_validation.configuration.credentials.with_streaming_response.update(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            keys=[
                {
                    "alg": "ES256",
                    "crv": "P-256",
                    "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                    "kty": "EC",
                    "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                    "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.token_validation.configuration.credentials.with_raw_response.update(
                config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
                zone_id="",
                keys=[
                    {
                        "alg": "ES256",
                        "crv": "P-256",
                        "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                        "kty": "EC",
                        "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                        "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.token_validation.configuration.credentials.with_raw_response.update(
                config_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                keys=[
                    {
                        "alg": "ES256",
                        "crv": "P-256",
                        "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                        "kty": "EC",
                        "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                        "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                    }
                ],
            )


class TestAsyncCredentials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        credential = await async_client.token_validation.configuration.credentials.update(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            keys=[
                {
                    "alg": "ES256",
                    "crv": "P-256",
                    "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                    "kty": "EC",
                    "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                    "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                }
            ],
        )
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.token_validation.configuration.credentials.with_raw_response.update(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            keys=[
                {
                    "alg": "ES256",
                    "crv": "P-256",
                    "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                    "kty": "EC",
                    "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                    "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.token_validation.configuration.credentials.with_streaming_response.update(
            config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            keys=[
                {
                    "alg": "ES256",
                    "crv": "P-256",
                    "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                    "kty": "EC",
                    "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                    "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.token_validation.configuration.credentials.with_raw_response.update(
                config_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
                zone_id="",
                keys=[
                    {
                        "alg": "ES256",
                        "crv": "P-256",
                        "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                        "kty": "EC",
                        "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                        "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.token_validation.configuration.credentials.with_raw_response.update(
                config_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                keys=[
                    {
                        "alg": "ES256",
                        "crv": "P-256",
                        "kid": "38013f13-c266-4eec-a72a-92ec92779f21",
                        "kty": "EC",
                        "x": "KN53JRwN3wCjm2o39bvZUX2VdrsHzS8pxOAGjm8m7EQ",
                        "y": "lnkkzIxaveggz-HFhcMWW15nxvOj0Z_uQsXbpK0GFcY",
                    }
                ],
            )
