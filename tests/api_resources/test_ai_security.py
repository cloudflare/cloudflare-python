# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.ai_security import AISecurityGetResponse, AISecurityUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAISecurity:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        ai_security = client.ai_security.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AISecurityUpdateResponse, ai_security, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        ai_security = client.ai_security.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )
        assert_matches_type(AISecurityUpdateResponse, ai_security, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.ai_security.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_security = response.parse()
        assert_matches_type(AISecurityUpdateResponse, ai_security, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.ai_security.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_security = response.parse()
            assert_matches_type(AISecurityUpdateResponse, ai_security, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ai_security.with_raw_response.update(
                zone_id="",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ai_security = client.ai_security.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AISecurityGetResponse, ai_security, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.ai_security.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_security = response.parse()
        assert_matches_type(AISecurityGetResponse, ai_security, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.ai_security.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_security = response.parse()
            assert_matches_type(AISecurityGetResponse, ai_security, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ai_security.with_raw_response.get(
                zone_id="",
            )


class TestAsyncAISecurity:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        ai_security = await async_client.ai_security.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AISecurityUpdateResponse, ai_security, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ai_security = await async_client.ai_security.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )
        assert_matches_type(AISecurityUpdateResponse, ai_security, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_security.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_security = await response.parse()
        assert_matches_type(AISecurityUpdateResponse, ai_security, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_security.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_security = await response.parse()
            assert_matches_type(AISecurityUpdateResponse, ai_security, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ai_security.with_raw_response.update(
                zone_id="",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ai_security = await async_client.ai_security.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AISecurityGetResponse, ai_security, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_security.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_security = await response.parse()
        assert_matches_type(AISecurityGetResponse, ai_security, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_security.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_security = await response.parse()
            assert_matches_type(AISecurityGetResponse, ai_security, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ai_security.with_raw_response.get(
                zone_id="",
            )
