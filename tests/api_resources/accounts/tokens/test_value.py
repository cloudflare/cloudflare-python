# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValue:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        value = client.accounts.tokens.value.update(
            token_id="ed17574386854bf78a67040be0a770b0",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            body={},
        )
        assert_matches_type(str, value, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.accounts.tokens.value.with_raw_response.update(
            token_id="ed17574386854bf78a67040be0a770b0",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert_matches_type(str, value, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.accounts.tokens.value.with_streaming_response.update(
            token_id="ed17574386854bf78a67040be0a770b0",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert_matches_type(str, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.tokens.value.with_raw_response.update(
                token_id="ed17574386854bf78a67040be0a770b0",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            client.accounts.tokens.value.with_raw_response.update(
                token_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
                body={},
            )


class TestAsyncValue:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        value = await async_client.accounts.tokens.value.update(
            token_id="ed17574386854bf78a67040be0a770b0",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            body={},
        )
        assert_matches_type(str, value, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.accounts.tokens.value.with_raw_response.update(
            token_id="ed17574386854bf78a67040be0a770b0",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert_matches_type(str, value, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.accounts.tokens.value.with_streaming_response.update(
            token_id="ed17574386854bf78a67040be0a770b0",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert_matches_type(str, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.tokens.value.with_raw_response.update(
                token_id="ed17574386854bf78a67040be0a770b0",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            await async_client.accounts.tokens.value.with_raw_response.update(
                token_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
                body={},
            )
