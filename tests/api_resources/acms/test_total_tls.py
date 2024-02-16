# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.acms import TotalTLSGetResponse, TotalTLSUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTotalTLS:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        total_tls = client.acms.total_tls.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )
        assert_matches_type(TotalTLSUpdateResponse, total_tls, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        total_tls = client.acms.total_tls.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            certificate_authority="google",
        )
        assert_matches_type(TotalTLSUpdateResponse, total_tls, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.acms.total_tls.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        total_tls = response.parse()
        assert_matches_type(TotalTLSUpdateResponse, total_tls, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.acms.total_tls.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            total_tls = response.parse()
            assert_matches_type(TotalTLSUpdateResponse, total_tls, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.acms.total_tls.with_raw_response.update(
                "",
                enabled=True,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        total_tls = client.acms.total_tls.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TotalTLSGetResponse, total_tls, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.acms.total_tls.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        total_tls = response.parse()
        assert_matches_type(TotalTLSGetResponse, total_tls, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.acms.total_tls.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            total_tls = response.parse()
            assert_matches_type(TotalTLSGetResponse, total_tls, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.acms.total_tls.with_raw_response.get(
                "",
            )


class TestAsyncTotalTLS:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        total_tls = await async_client.acms.total_tls.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )
        assert_matches_type(TotalTLSUpdateResponse, total_tls, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        total_tls = await async_client.acms.total_tls.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            certificate_authority="google",
        )
        assert_matches_type(TotalTLSUpdateResponse, total_tls, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.acms.total_tls.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        total_tls = await response.parse()
        assert_matches_type(TotalTLSUpdateResponse, total_tls, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.acms.total_tls.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            total_tls = await response.parse()
            assert_matches_type(TotalTLSUpdateResponse, total_tls, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.acms.total_tls.with_raw_response.update(
                "",
                enabled=True,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        total_tls = await async_client.acms.total_tls.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TotalTLSGetResponse, total_tls, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.acms.total_tls.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        total_tls = await response.parse()
        assert_matches_type(TotalTLSGetResponse, total_tls, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.acms.total_tls.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            total_tls = await response.parse()
            assert_matches_type(TotalTLSGetResponse, total_tls, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.acms.total_tls.with_raw_response.get(
                "",
            )
