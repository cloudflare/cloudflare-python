# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.access.service_tokens import RotateAccessServiceTokensRotateAServiceTokenResponse

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


class TestRotates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_access_service_tokens_rotate_a_service_token(self, client: Cloudflare) -> None:
        rotate = client.access.service_tokens.rotates.access_service_tokens_rotate_a_service_token(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RotateAccessServiceTokensRotateAServiceTokenResponse, rotate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_access_service_tokens_rotate_a_service_token(self, client: Cloudflare) -> None:
        response = client.access.service_tokens.rotates.with_raw_response.access_service_tokens_rotate_a_service_token(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rotate = response.parse()
        assert_matches_type(RotateAccessServiceTokensRotateAServiceTokenResponse, rotate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_access_service_tokens_rotate_a_service_token(self, client: Cloudflare) -> None:
        with client.access.service_tokens.rotates.with_streaming_response.access_service_tokens_rotate_a_service_token(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rotate = response.parse()
            assert_matches_type(RotateAccessServiceTokensRotateAServiceTokenResponse, rotate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_access_service_tokens_rotate_a_service_token(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.access.service_tokens.rotates.with_raw_response.access_service_tokens_rotate_a_service_token(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.service_tokens.rotates.with_raw_response.access_service_tokens_rotate_a_service_token(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncRotates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_service_tokens_rotate_a_service_token(self, async_client: AsyncCloudflare) -> None:
        rotate = await async_client.access.service_tokens.rotates.access_service_tokens_rotate_a_service_token(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RotateAccessServiceTokensRotateAServiceTokenResponse, rotate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_access_service_tokens_rotate_a_service_token(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.access.service_tokens.rotates.with_raw_response.access_service_tokens_rotate_a_service_token(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rotate = await response.parse()
        assert_matches_type(RotateAccessServiceTokensRotateAServiceTokenResponse, rotate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_access_service_tokens_rotate_a_service_token(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.access.service_tokens.rotates.with_streaming_response.access_service_tokens_rotate_a_service_token(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rotate = await response.parse()
            assert_matches_type(RotateAccessServiceTokensRotateAServiceTokenResponse, rotate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_access_service_tokens_rotate_a_service_token(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.access.service_tokens.rotates.with_raw_response.access_service_tokens_rotate_a_service_token(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.service_tokens.rotates.with_raw_response.access_service_tokens_rotate_a_service_token(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
