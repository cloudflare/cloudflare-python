# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.zaraz import PublishCreateResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zaraz import publish_create_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPublish:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        publish = client.zaraz.publish.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="Config with enabled ecommerce tracking",
        )
        assert_matches_type(str, publish, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zaraz.publish.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="Config with enabled ecommerce tracking",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        publish = response.parse()
        assert_matches_type(str, publish, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zaraz.publish.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="Config with enabled ecommerce tracking",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            publish = response.parse()
            assert_matches_type(str, publish, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zaraz.publish.with_raw_response.create(
                "",
                body="Config with enabled ecommerce tracking",
            )


class TestAsyncPublish:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        publish = await async_client.zaraz.publish.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="Config with enabled ecommerce tracking",
        )
        assert_matches_type(str, publish, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zaraz.publish.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="Config with enabled ecommerce tracking",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        publish = await response.parse()
        assert_matches_type(str, publish, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zaraz.publish.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="Config with enabled ecommerce tracking",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            publish = await response.parse()
            assert_matches_type(str, publish, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zaraz.publish.with_raw_response.create(
                "",
                body="Config with enabled ecommerce tracking",
            )
