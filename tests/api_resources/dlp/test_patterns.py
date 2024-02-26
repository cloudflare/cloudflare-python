# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dlp import PatternValidateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPatterns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_validate(self, client: Cloudflare) -> None:
        pattern = client.dlp.patterns.validate(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            regex="^4[0-9]{6,}$",
        )
        assert_matches_type(PatternValidateResponse, pattern, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_validate(self, client: Cloudflare) -> None:
        response = client.dlp.patterns.with_raw_response.validate(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            regex="^4[0-9]{6,}$",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pattern = response.parse()
        assert_matches_type(PatternValidateResponse, pattern, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_validate(self, client: Cloudflare) -> None:
        with client.dlp.patterns.with_streaming_response.validate(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            regex="^4[0-9]{6,}$",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pattern = response.parse()
            assert_matches_type(PatternValidateResponse, pattern, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_validate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlp.patterns.with_raw_response.validate(
                account_id="",
                regex="^4[0-9]{6,}$",
            )


class TestAsyncPatterns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_validate(self, async_client: AsyncCloudflare) -> None:
        pattern = await async_client.dlp.patterns.validate(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            regex="^4[0-9]{6,}$",
        )
        assert_matches_type(PatternValidateResponse, pattern, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlp.patterns.with_raw_response.validate(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            regex="^4[0-9]{6,}$",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pattern = await response.parse()
        assert_matches_type(PatternValidateResponse, pattern, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dlp.patterns.with_streaming_response.validate(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            regex="^4[0-9]{6,}$",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pattern = await response.parse()
            assert_matches_type(PatternValidateResponse, pattern, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_validate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlp.patterns.with_raw_response.validate(
                account_id="",
                regex="^4[0-9]{6,}$",
            )
