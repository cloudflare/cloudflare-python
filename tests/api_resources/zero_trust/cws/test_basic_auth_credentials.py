# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncCursorPagination, AsyncCursorPagination
from cloudflare.types.zero_trust.cws import (
    BasicAuthCredential,
    BasicAuthCredentialDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBasicAuthCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        basic_auth_credential = client.zero_trust.cws.basic_auth_credentials.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            username="x",
        )
        assert_matches_type(BasicAuthCredential, basic_auth_credential, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.basic_auth_credentials.with_raw_response.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            username="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        basic_auth_credential = response.parse()
        assert_matches_type(BasicAuthCredential, basic_auth_credential, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.basic_auth_credentials.with_streaming_response.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            username="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            basic_auth_credential = response.parse()
            assert_matches_type(BasicAuthCredential, basic_auth_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.with_raw_response.create(
                account_id="",
                username="x",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        basic_auth_credential = client.zero_trust.cws.basic_auth_credentials.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPagination[BasicAuthCredential], basic_auth_credential, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        basic_auth_credential = client.zero_trust.cws.basic_auth_credentials.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            cursor="cursor",
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            order="username",
            per_page=1,
            username="username",
        )
        assert_matches_type(SyncCursorPagination[BasicAuthCredential], basic_auth_credential, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.basic_auth_credentials.with_raw_response.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        basic_auth_credential = response.parse()
        assert_matches_type(SyncCursorPagination[BasicAuthCredential], basic_auth_credential, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.basic_auth_credentials.with_streaming_response.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            basic_auth_credential = response.parse()
            assert_matches_type(SyncCursorPagination[BasicAuthCredential], basic_auth_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        basic_auth_credential = client.zero_trust.cws.basic_auth_credentials.delete(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(BasicAuthCredentialDeleteResponse, basic_auth_credential, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.basic_auth_credentials.with_raw_response.delete(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        basic_auth_credential = response.parse()
        assert_matches_type(BasicAuthCredentialDeleteResponse, basic_auth_credential, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.basic_auth_credentials.with_streaming_response.delete(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            basic_auth_credential = response.parse()
            assert_matches_type(BasicAuthCredentialDeleteResponse, basic_auth_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.with_raw_response.delete(
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.with_raw_response.delete(
                credential_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        basic_auth_credential = client.zero_trust.cws.basic_auth_credentials.get(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(BasicAuthCredential, basic_auth_credential, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.basic_auth_credentials.with_raw_response.get(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        basic_auth_credential = response.parse()
        assert_matches_type(BasicAuthCredential, basic_auth_credential, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.basic_auth_credentials.with_streaming_response.get(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            basic_auth_credential = response.parse()
            assert_matches_type(BasicAuthCredential, basic_auth_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.with_raw_response.get(
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            client.zero_trust.cws.basic_auth_credentials.with_raw_response.get(
                credential_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )


class TestAsyncBasicAuthCredentials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        basic_auth_credential = await async_client.zero_trust.cws.basic_auth_credentials.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            username="x",
        )
        assert_matches_type(BasicAuthCredential, basic_auth_credential, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.basic_auth_credentials.with_raw_response.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            username="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        basic_auth_credential = await response.parse()
        assert_matches_type(BasicAuthCredential, basic_auth_credential, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.basic_auth_credentials.with_streaming_response.create(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            username="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            basic_auth_credential = await response.parse()
            assert_matches_type(BasicAuthCredential, basic_auth_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.with_raw_response.create(
                account_id="",
                username="x",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        basic_auth_credential = await async_client.zero_trust.cws.basic_auth_credentials.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPagination[BasicAuthCredential], basic_auth_credential, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        basic_auth_credential = await async_client.zero_trust.cws.basic_auth_credentials.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            cursor="cursor",
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            order="username",
            per_page=1,
            username="username",
        )
        assert_matches_type(AsyncCursorPagination[BasicAuthCredential], basic_auth_credential, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.basic_auth_credentials.with_raw_response.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        basic_auth_credential = await response.parse()
        assert_matches_type(AsyncCursorPagination[BasicAuthCredential], basic_auth_credential, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.basic_auth_credentials.with_streaming_response.list(
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            basic_auth_credential = await response.parse()
            assert_matches_type(AsyncCursorPagination[BasicAuthCredential], basic_auth_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        basic_auth_credential = await async_client.zero_trust.cws.basic_auth_credentials.delete(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(BasicAuthCredentialDeleteResponse, basic_auth_credential, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.basic_auth_credentials.with_raw_response.delete(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        basic_auth_credential = await response.parse()
        assert_matches_type(BasicAuthCredentialDeleteResponse, basic_auth_credential, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.basic_auth_credentials.with_streaming_response.delete(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            basic_auth_credential = await response.parse()
            assert_matches_type(BasicAuthCredentialDeleteResponse, basic_auth_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.with_raw_response.delete(
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.with_raw_response.delete(
                credential_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        basic_auth_credential = await async_client.zero_trust.cws.basic_auth_credentials.get(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(BasicAuthCredential, basic_auth_credential, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.basic_auth_credentials.with_raw_response.get(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        basic_auth_credential = await response.parse()
        assert_matches_type(BasicAuthCredential, basic_auth_credential, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.basic_auth_credentials.with_streaming_response.get(
            credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            basic_auth_credential = await response.parse()
            assert_matches_type(BasicAuthCredential, basic_auth_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.with_raw_response.get(
                credential_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            await async_client.zero_trust.cws.basic_auth_credentials.with_raw_response.get(
                credential_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )
