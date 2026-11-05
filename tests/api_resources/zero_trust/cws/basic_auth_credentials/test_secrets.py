# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncCursorPagination, AsyncCursorPagination
from cloudflare.types.zero_trust.cws.basic_auth_credentials import (
    BasicAuthSecret,
    SecretDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        secret = client.zero_trust.cws.basic_auth_credentials.secrets.create(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            password="x",
        )
        assert_matches_type(BasicAuthSecret, secret, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        secret = client.zero_trust.cws.basic_auth_credentials.secrets.create(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            password="x",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BasicAuthSecret, secret, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.create(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            password="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(BasicAuthSecret, secret, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.basic_auth_credentials.secrets.with_streaming_response.create(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            password="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(BasicAuthSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.create(
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                password="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.create(
                credential_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                password="x",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        secret = client.zero_trust.cws.basic_auth_credentials.secrets.list(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPagination[BasicAuthSecret], secret, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        secret = client.zero_trust.cws.basic_auth_credentials.secrets.list(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            cursor="cursor",
            direction="asc",
            order="created_at",
            per_page=1,
        )
        assert_matches_type(SyncCursorPagination[BasicAuthSecret], secret, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.list(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SyncCursorPagination[BasicAuthSecret], secret, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.basic_auth_credentials.secrets.with_streaming_response.list(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SyncCursorPagination[BasicAuthSecret], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.list(
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.list(
                credential_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        secret = client.zero_trust.cws.basic_auth_credentials.secrets.delete(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SecretDeleteResponse, secret, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.delete(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretDeleteResponse, secret, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.basic_auth_credentials.secrets.with_streaming_response.delete(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretDeleteResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.delete(
                secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.delete(
                secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                credential_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.delete(
                secret_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        secret = client.zero_trust.cws.basic_auth_credentials.secrets.get(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BasicAuthSecret, secret, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.get(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(BasicAuthSecret, secret, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.basic_auth_credentials.secrets.with_streaming_response.get(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(BasicAuthSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.get(
                secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.get(
                secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                credential_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.get(
                secret_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.zero_trust.cws.basic_auth_credentials.secrets.create(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            password="x",
        )
        assert_matches_type(BasicAuthSecret, secret, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.zero_trust.cws.basic_auth_credentials.secrets.create(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            password="x",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BasicAuthSecret, secret, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.create(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            password="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(BasicAuthSecret, secret, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.basic_auth_credentials.secrets.with_streaming_response.create(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            password="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(BasicAuthSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.create(
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                password="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.create(
                credential_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                password="x",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.zero_trust.cws.basic_auth_credentials.secrets.list(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPagination[BasicAuthSecret], secret, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.zero_trust.cws.basic_auth_credentials.secrets.list(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            cursor="cursor",
            direction="asc",
            order="created_at",
            per_page=1,
        )
        assert_matches_type(AsyncCursorPagination[BasicAuthSecret], secret, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.list(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(AsyncCursorPagination[BasicAuthSecret], secret, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.basic_auth_credentials.secrets.with_streaming_response.list(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(AsyncCursorPagination[BasicAuthSecret], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.list(
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.list(
                credential_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.zero_trust.cws.basic_auth_credentials.secrets.delete(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SecretDeleteResponse, secret, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.delete(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretDeleteResponse, secret, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.basic_auth_credentials.secrets.with_streaming_response.delete(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretDeleteResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.delete(
                secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.delete(
                secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                credential_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.delete(
                secret_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.zero_trust.cws.basic_auth_credentials.secrets.get(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BasicAuthSecret, secret, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.get(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(BasicAuthSecret, secret, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.basic_auth_credentials.secrets.with_streaming_response.get(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(BasicAuthSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.get(
                secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.get(
                secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                credential_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.secrets.with_raw_response.get(
                secret_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
