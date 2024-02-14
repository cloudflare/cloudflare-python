# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.settings import OriginMaxHTTPVersionUpdateResponse, OriginMaxHTTPVersionGetResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.settings import origin_max_http_version_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOriginMaxHTTPVersion:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        origin_max_http_version = client.settings.origin_max_http_version.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="2",
        )
        assert_matches_type(OriginMaxHTTPVersionUpdateResponse, origin_max_http_version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.settings.origin_max_http_version.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_max_http_version = response.parse()
        assert_matches_type(OriginMaxHTTPVersionUpdateResponse, origin_max_http_version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.settings.origin_max_http_version.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_max_http_version = response.parse()
            assert_matches_type(OriginMaxHTTPVersionUpdateResponse, origin_max_http_version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.settings.origin_max_http_version.with_raw_response.update(
                "",
                value="2",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        origin_max_http_version = client.settings.origin_max_http_version.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OriginMaxHTTPVersionGetResponse, origin_max_http_version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.settings.origin_max_http_version.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_max_http_version = response.parse()
        assert_matches_type(OriginMaxHTTPVersionGetResponse, origin_max_http_version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.settings.origin_max_http_version.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_max_http_version = response.parse()
            assert_matches_type(OriginMaxHTTPVersionGetResponse, origin_max_http_version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.settings.origin_max_http_version.with_raw_response.get(
                "",
            )


class TestAsyncOriginMaxHTTPVersion:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        origin_max_http_version = await async_client.settings.origin_max_http_version.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="2",
        )
        assert_matches_type(OriginMaxHTTPVersionUpdateResponse, origin_max_http_version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.settings.origin_max_http_version.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_max_http_version = await response.parse()
        assert_matches_type(OriginMaxHTTPVersionUpdateResponse, origin_max_http_version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.settings.origin_max_http_version.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_max_http_version = await response.parse()
            assert_matches_type(OriginMaxHTTPVersionUpdateResponse, origin_max_http_version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.settings.origin_max_http_version.with_raw_response.update(
                "",
                value="2",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        origin_max_http_version = await async_client.settings.origin_max_http_version.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OriginMaxHTTPVersionGetResponse, origin_max_http_version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.settings.origin_max_http_version.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_max_http_version = await response.parse()
        assert_matches_type(OriginMaxHTTPVersionGetResponse, origin_max_http_version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.settings.origin_max_http_version.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_max_http_version = await response.parse()
            assert_matches_type(OriginMaxHTTPVersionGetResponse, origin_max_http_version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.settings.origin_max_http_version.with_raw_response.get(
                "",
            )
