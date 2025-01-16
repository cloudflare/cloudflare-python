# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.dlp.email import (
    AccountMappingGetResponse,
    AccountMappingCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountMapping:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        account_mapping = client.zero_trust.dlp.email.account_mapping.create(
            account_id="account_id",
            auth_requirements={
                "allowed_microsoft_organizations": ["string"],
                "type": "Org",
            },
        )
        assert_matches_type(Optional[AccountMappingCreateResponse], account_mapping, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.email.account_mapping.with_raw_response.create(
            account_id="account_id",
            auth_requirements={
                "allowed_microsoft_organizations": ["string"],
                "type": "Org",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_mapping = response.parse()
        assert_matches_type(Optional[AccountMappingCreateResponse], account_mapping, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.email.account_mapping.with_streaming_response.create(
            account_id="account_id",
            auth_requirements={
                "allowed_microsoft_organizations": ["string"],
                "type": "Org",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_mapping = response.parse()
            assert_matches_type(Optional[AccountMappingCreateResponse], account_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.email.account_mapping.with_raw_response.create(
                account_id="",
                auth_requirements={
                    "allowed_microsoft_organizations": ["string"],
                    "type": "Org",
                },
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        account_mapping = client.zero_trust.dlp.email.account_mapping.get(
            account_id="account_id",
        )
        assert_matches_type(Optional[AccountMappingGetResponse], account_mapping, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.email.account_mapping.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_mapping = response.parse()
        assert_matches_type(Optional[AccountMappingGetResponse], account_mapping, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.email.account_mapping.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_mapping = response.parse()
            assert_matches_type(Optional[AccountMappingGetResponse], account_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.email.account_mapping.with_raw_response.get(
                account_id="",
            )


class TestAsyncAccountMapping:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        account_mapping = await async_client.zero_trust.dlp.email.account_mapping.create(
            account_id="account_id",
            auth_requirements={
                "allowed_microsoft_organizations": ["string"],
                "type": "Org",
            },
        )
        assert_matches_type(Optional[AccountMappingCreateResponse], account_mapping, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.email.account_mapping.with_raw_response.create(
            account_id="account_id",
            auth_requirements={
                "allowed_microsoft_organizations": ["string"],
                "type": "Org",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_mapping = await response.parse()
        assert_matches_type(Optional[AccountMappingCreateResponse], account_mapping, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.email.account_mapping.with_streaming_response.create(
            account_id="account_id",
            auth_requirements={
                "allowed_microsoft_organizations": ["string"],
                "type": "Org",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_mapping = await response.parse()
            assert_matches_type(Optional[AccountMappingCreateResponse], account_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.email.account_mapping.with_raw_response.create(
                account_id="",
                auth_requirements={
                    "allowed_microsoft_organizations": ["string"],
                    "type": "Org",
                },
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        account_mapping = await async_client.zero_trust.dlp.email.account_mapping.get(
            account_id="account_id",
        )
        assert_matches_type(Optional[AccountMappingGetResponse], account_mapping, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.email.account_mapping.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_mapping = await response.parse()
        assert_matches_type(Optional[AccountMappingGetResponse], account_mapping, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.email.account_mapping.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_mapping = await response.parse()
            assert_matches_type(Optional[AccountMappingGetResponse], account_mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.email.account_mapping.with_raw_response.get(
                account_id="",
            )
