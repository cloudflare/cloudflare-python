# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.email_routing import RoutingGetResponse, RoutingEnableResponse, RoutingDisableResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRouting:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_disable(self, client: Cloudflare) -> None:
        routing = client.email_routing.routing.disable(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RoutingDisableResponse, routing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_disable(self, client: Cloudflare) -> None:
        response = client.email_routing.routing.with_raw_response.disable(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = response.parse()
        assert_matches_type(RoutingDisableResponse, routing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_disable(self, client: Cloudflare) -> None:
        with client.email_routing.routing.with_streaming_response.disable(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = response.parse()
            assert_matches_type(RoutingDisableResponse, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_disable(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.email_routing.routing.with_raw_response.disable(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_enable(self, client: Cloudflare) -> None:
        routing = client.email_routing.routing.enable(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RoutingEnableResponse, routing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_enable(self, client: Cloudflare) -> None:
        response = client.email_routing.routing.with_raw_response.enable(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = response.parse()
        assert_matches_type(RoutingEnableResponse, routing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_enable(self, client: Cloudflare) -> None:
        with client.email_routing.routing.with_streaming_response.enable(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = response.parse()
            assert_matches_type(RoutingEnableResponse, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_enable(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.email_routing.routing.with_raw_response.enable(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        routing = client.email_routing.routing.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RoutingGetResponse, routing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.email_routing.routing.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = response.parse()
        assert_matches_type(RoutingGetResponse, routing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_routing.routing.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = response.parse()
            assert_matches_type(RoutingGetResponse, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.email_routing.routing.with_raw_response.get(
                "",
            )


class TestAsyncRouting:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_disable(self, async_client: AsyncCloudflare) -> None:
        routing = await async_client.email_routing.routing.disable(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RoutingDisableResponse, routing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_routing.routing.with_raw_response.disable(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = await response.parse()
        assert_matches_type(RoutingDisableResponse, routing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_routing.routing.with_streaming_response.disable(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = await response.parse()
            assert_matches_type(RoutingDisableResponse, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_disable(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.email_routing.routing.with_raw_response.disable(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_enable(self, async_client: AsyncCloudflare) -> None:
        routing = await async_client.email_routing.routing.enable(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RoutingEnableResponse, routing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_routing.routing.with_raw_response.enable(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = await response.parse()
        assert_matches_type(RoutingEnableResponse, routing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_routing.routing.with_streaming_response.enable(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = await response.parse()
            assert_matches_type(RoutingEnableResponse, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_enable(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.email_routing.routing.with_raw_response.enable(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        routing = await async_client.email_routing.routing.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RoutingGetResponse, routing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_routing.routing.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = await response.parse()
        assert_matches_type(RoutingGetResponse, routing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_routing.routing.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = await response.parse()
            assert_matches_type(RoutingGetResponse, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.email_routing.routing.with_raw_response.get(
                "",
            )
