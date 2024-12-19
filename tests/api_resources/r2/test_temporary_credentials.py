# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.r2 import TemporaryCredentialCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemporaryCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        temporary_credential = client.r2.temporary_credentials.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket="example-bucket",
            parent_access_key_id="example-access-key-id",
            permission="admin-read-write",
            ttl_seconds=3600,
        )
        assert_matches_type(TemporaryCredentialCreateResponse, temporary_credential, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        temporary_credential = client.r2.temporary_credentials.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket="example-bucket",
            parent_access_key_id="example-access-key-id",
            permission="admin-read-write",
            ttl_seconds=3600,
            objects=["example-object"],
            prefixes=["example-prefix/"],
        )
        assert_matches_type(TemporaryCredentialCreateResponse, temporary_credential, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.r2.temporary_credentials.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket="example-bucket",
            parent_access_key_id="example-access-key-id",
            permission="admin-read-write",
            ttl_seconds=3600,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        temporary_credential = response.parse()
        assert_matches_type(TemporaryCredentialCreateResponse, temporary_credential, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.r2.temporary_credentials.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket="example-bucket",
            parent_access_key_id="example-access-key-id",
            permission="admin-read-write",
            ttl_seconds=3600,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            temporary_credential = response.parse()
            assert_matches_type(TemporaryCredentialCreateResponse, temporary_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.temporary_credentials.with_raw_response.create(
                account_id="",
                bucket="example-bucket",
                parent_access_key_id="example-access-key-id",
                permission="admin-read-write",
                ttl_seconds=3600,
            )


class TestAsyncTemporaryCredentials:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        temporary_credential = await async_client.r2.temporary_credentials.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket="example-bucket",
            parent_access_key_id="example-access-key-id",
            permission="admin-read-write",
            ttl_seconds=3600,
        )
        assert_matches_type(TemporaryCredentialCreateResponse, temporary_credential, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        temporary_credential = await async_client.r2.temporary_credentials.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket="example-bucket",
            parent_access_key_id="example-access-key-id",
            permission="admin-read-write",
            ttl_seconds=3600,
            objects=["example-object"],
            prefixes=["example-prefix/"],
        )
        assert_matches_type(TemporaryCredentialCreateResponse, temporary_credential, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.temporary_credentials.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket="example-bucket",
            parent_access_key_id="example-access-key-id",
            permission="admin-read-write",
            ttl_seconds=3600,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        temporary_credential = await response.parse()
        assert_matches_type(TemporaryCredentialCreateResponse, temporary_credential, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.temporary_credentials.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket="example-bucket",
            parent_access_key_id="example-access-key-id",
            permission="admin-read-write",
            ttl_seconds=3600,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            temporary_credential = await response.parse()
            assert_matches_type(TemporaryCredentialCreateResponse, temporary_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.temporary_credentials.with_raw_response.create(
                account_id="",
                bucket="example-bucket",
                parent_access_key_id="example-access-key-id",
                permission="admin-read-write",
                ttl_seconds=3600,
            )
