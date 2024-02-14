# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.users.tokens import VerifyUserAPITokensVerifyTokenResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerifies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_user_api_tokens_verify_token(self, client: Cloudflare) -> None:
        verify = client.users.tokens.verifies.user_api_tokens_verify_token()
        assert_matches_type(VerifyUserAPITokensVerifyTokenResponse, verify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_user_api_tokens_verify_token(self, client: Cloudflare) -> None:
        response = client.users.tokens.verifies.with_raw_response.user_api_tokens_verify_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify = response.parse()
        assert_matches_type(VerifyUserAPITokensVerifyTokenResponse, verify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_user_api_tokens_verify_token(self, client: Cloudflare) -> None:
        with client.users.tokens.verifies.with_streaming_response.user_api_tokens_verify_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify = response.parse()
            assert_matches_type(VerifyUserAPITokensVerifyTokenResponse, verify, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVerifies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_api_tokens_verify_token(self, async_client: AsyncCloudflare) -> None:
        verify = await async_client.users.tokens.verifies.user_api_tokens_verify_token()
        assert_matches_type(VerifyUserAPITokensVerifyTokenResponse, verify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_user_api_tokens_verify_token(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.tokens.verifies.with_raw_response.user_api_tokens_verify_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify = await response.parse()
        assert_matches_type(VerifyUserAPITokensVerifyTokenResponse, verify, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_user_api_tokens_verify_token(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.tokens.verifies.with_streaming_response.user_api_tokens_verify_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify = await response.parse()
            assert_matches_type(VerifyUserAPITokensVerifyTokenResponse, verify, path=["response"])

        assert cast(Any, response.is_closed) is True
