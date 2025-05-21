# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.r2.super_slurper import (
    ConnectivityPrecheckSourceResponse,
    ConnectivityPrecheckTargetResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectivityPrecheck:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_source_overload_1(self, client: Cloudflare) -> None:
        connectivity_precheck = client.r2.super_slurper.connectivity_precheck.source(
            account_id="account_id",
        )
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    def test_method_source_with_all_params_overload_1(self, client: Cloudflare) -> None:
        connectivity_precheck = client.r2.super_slurper.connectivity_precheck.source(
            account_id="account_id",
            bucket="bucket",
            endpoint="endpoint",
            secret={
                "access_key_id": "accessKeyId",
                "secret_access_key": "secretAccessKey",
            },
            vendor="s3",
        )
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    def test_raw_response_source_overload_1(self, client: Cloudflare) -> None:
        response = client.r2.super_slurper.connectivity_precheck.with_raw_response.source(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_precheck = response.parse()
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    def test_streaming_response_source_overload_1(self, client: Cloudflare) -> None:
        with client.r2.super_slurper.connectivity_precheck.with_streaming_response.source(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_precheck = response.parse()
            assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_source_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.super_slurper.connectivity_precheck.with_raw_response.source(
                account_id="",
            )

    @parametrize
    def test_method_source_overload_2(self, client: Cloudflare) -> None:
        connectivity_precheck = client.r2.super_slurper.connectivity_precheck.source(
            account_id="account_id",
        )
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    def test_method_source_with_all_params_overload_2(self, client: Cloudflare) -> None:
        connectivity_precheck = client.r2.super_slurper.connectivity_precheck.source(
            account_id="account_id",
            bucket="bucket",
            secret={
                "client_email": "clientEmail",
                "private_key": "privateKey",
            },
            vendor="gcs",
        )
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    def test_raw_response_source_overload_2(self, client: Cloudflare) -> None:
        response = client.r2.super_slurper.connectivity_precheck.with_raw_response.source(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_precheck = response.parse()
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    def test_streaming_response_source_overload_2(self, client: Cloudflare) -> None:
        with client.r2.super_slurper.connectivity_precheck.with_streaming_response.source(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_precheck = response.parse()
            assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_source_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.super_slurper.connectivity_precheck.with_raw_response.source(
                account_id="",
            )

    @parametrize
    def test_method_source_overload_3(self, client: Cloudflare) -> None:
        connectivity_precheck = client.r2.super_slurper.connectivity_precheck.source(
            account_id="account_id",
        )
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    def test_method_source_with_all_params_overload_3(self, client: Cloudflare) -> None:
        connectivity_precheck = client.r2.super_slurper.connectivity_precheck.source(
            account_id="account_id",
            bucket="bucket",
            jurisdiction="default",
            secret={
                "access_key_id": "accessKeyId",
                "secret_access_key": "secretAccessKey",
            },
            vendor="r2",
        )
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    def test_raw_response_source_overload_3(self, client: Cloudflare) -> None:
        response = client.r2.super_slurper.connectivity_precheck.with_raw_response.source(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_precheck = response.parse()
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    def test_streaming_response_source_overload_3(self, client: Cloudflare) -> None:
        with client.r2.super_slurper.connectivity_precheck.with_streaming_response.source(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_precheck = response.parse()
            assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_source_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.super_slurper.connectivity_precheck.with_raw_response.source(
                account_id="",
            )

    @parametrize
    def test_method_target(self, client: Cloudflare) -> None:
        connectivity_precheck = client.r2.super_slurper.connectivity_precheck.target(
            account_id="account_id",
        )
        assert_matches_type(Optional[ConnectivityPrecheckTargetResponse], connectivity_precheck, path=["response"])

    @parametrize
    def test_method_target_with_all_params(self, client: Cloudflare) -> None:
        connectivity_precheck = client.r2.super_slurper.connectivity_precheck.target(
            account_id="account_id",
            bucket="bucket",
            jurisdiction="default",
            secret={
                "access_key_id": "accessKeyId",
                "secret_access_key": "secretAccessKey",
            },
            vendor="r2",
        )
        assert_matches_type(Optional[ConnectivityPrecheckTargetResponse], connectivity_precheck, path=["response"])

    @parametrize
    def test_raw_response_target(self, client: Cloudflare) -> None:
        response = client.r2.super_slurper.connectivity_precheck.with_raw_response.target(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_precheck = response.parse()
        assert_matches_type(Optional[ConnectivityPrecheckTargetResponse], connectivity_precheck, path=["response"])

    @parametrize
    def test_streaming_response_target(self, client: Cloudflare) -> None:
        with client.r2.super_slurper.connectivity_precheck.with_streaming_response.target(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_precheck = response.parse()
            assert_matches_type(Optional[ConnectivityPrecheckTargetResponse], connectivity_precheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_target(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.super_slurper.connectivity_precheck.with_raw_response.target(
                account_id="",
            )


class TestAsyncConnectivityPrecheck:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_source_overload_1(self, async_client: AsyncCloudflare) -> None:
        connectivity_precheck = await async_client.r2.super_slurper.connectivity_precheck.source(
            account_id="account_id",
        )
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    async def test_method_source_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        connectivity_precheck = await async_client.r2.super_slurper.connectivity_precheck.source(
            account_id="account_id",
            bucket="bucket",
            endpoint="endpoint",
            secret={
                "access_key_id": "accessKeyId",
                "secret_access_key": "secretAccessKey",
            },
            vendor="s3",
        )
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    async def test_raw_response_source_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.super_slurper.connectivity_precheck.with_raw_response.source(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_precheck = await response.parse()
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    async def test_streaming_response_source_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.super_slurper.connectivity_precheck.with_streaming_response.source(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_precheck = await response.parse()
            assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_source_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.super_slurper.connectivity_precheck.with_raw_response.source(
                account_id="",
            )

    @parametrize
    async def test_method_source_overload_2(self, async_client: AsyncCloudflare) -> None:
        connectivity_precheck = await async_client.r2.super_slurper.connectivity_precheck.source(
            account_id="account_id",
        )
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    async def test_method_source_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        connectivity_precheck = await async_client.r2.super_slurper.connectivity_precheck.source(
            account_id="account_id",
            bucket="bucket",
            secret={
                "client_email": "clientEmail",
                "private_key": "privateKey",
            },
            vendor="gcs",
        )
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    async def test_raw_response_source_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.super_slurper.connectivity_precheck.with_raw_response.source(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_precheck = await response.parse()
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    async def test_streaming_response_source_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.super_slurper.connectivity_precheck.with_streaming_response.source(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_precheck = await response.parse()
            assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_source_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.super_slurper.connectivity_precheck.with_raw_response.source(
                account_id="",
            )

    @parametrize
    async def test_method_source_overload_3(self, async_client: AsyncCloudflare) -> None:
        connectivity_precheck = await async_client.r2.super_slurper.connectivity_precheck.source(
            account_id="account_id",
        )
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    async def test_method_source_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        connectivity_precheck = await async_client.r2.super_slurper.connectivity_precheck.source(
            account_id="account_id",
            bucket="bucket",
            jurisdiction="default",
            secret={
                "access_key_id": "accessKeyId",
                "secret_access_key": "secretAccessKey",
            },
            vendor="r2",
        )
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    async def test_raw_response_source_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.super_slurper.connectivity_precheck.with_raw_response.source(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_precheck = await response.parse()
        assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

    @parametrize
    async def test_streaming_response_source_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.super_slurper.connectivity_precheck.with_streaming_response.source(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_precheck = await response.parse()
            assert_matches_type(Optional[ConnectivityPrecheckSourceResponse], connectivity_precheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_source_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.super_slurper.connectivity_precheck.with_raw_response.source(
                account_id="",
            )

    @parametrize
    async def test_method_target(self, async_client: AsyncCloudflare) -> None:
        connectivity_precheck = await async_client.r2.super_slurper.connectivity_precheck.target(
            account_id="account_id",
        )
        assert_matches_type(Optional[ConnectivityPrecheckTargetResponse], connectivity_precheck, path=["response"])

    @parametrize
    async def test_method_target_with_all_params(self, async_client: AsyncCloudflare) -> None:
        connectivity_precheck = await async_client.r2.super_slurper.connectivity_precheck.target(
            account_id="account_id",
            bucket="bucket",
            jurisdiction="default",
            secret={
                "access_key_id": "accessKeyId",
                "secret_access_key": "secretAccessKey",
            },
            vendor="r2",
        )
        assert_matches_type(Optional[ConnectivityPrecheckTargetResponse], connectivity_precheck, path=["response"])

    @parametrize
    async def test_raw_response_target(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.super_slurper.connectivity_precheck.with_raw_response.target(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_precheck = await response.parse()
        assert_matches_type(Optional[ConnectivityPrecheckTargetResponse], connectivity_precheck, path=["response"])

    @parametrize
    async def test_streaming_response_target(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.super_slurper.connectivity_precheck.with_streaming_response.target(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_precheck = await response.parse()
            assert_matches_type(Optional[ConnectivityPrecheckTargetResponse], connectivity_precheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_target(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.super_slurper.connectivity_precheck.with_raw_response.target(
                account_id="",
            )
