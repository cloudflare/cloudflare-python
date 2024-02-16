# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import CustomNListResponse, CustomNCreateResponse, CustomNDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomNs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        custom_n = client.custom_ns.create(
            "372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        )
        assert_matches_type(CustomNCreateResponse, custom_n, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        custom_n = client.custom_ns.create(
            "372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
            ns_set=1,
        )
        assert_matches_type(CustomNCreateResponse, custom_n, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.custom_ns.with_raw_response.create(
            "372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_n = response.parse()
        assert_matches_type(CustomNCreateResponse, custom_n, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.custom_ns.with_streaming_response.create(
            "372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_n = response.parse()
            assert_matches_type(CustomNCreateResponse, custom_n, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.custom_ns.with_raw_response.create(
                "",
                ns_name="ns1.example.com",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        custom_n = client.custom_ns.list(
            "372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(Optional[CustomNListResponse], custom_n, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.custom_ns.with_raw_response.list(
            "372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_n = response.parse()
        assert_matches_type(Optional[CustomNListResponse], custom_n, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.custom_ns.with_streaming_response.list(
            "372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_n = response.parse()
            assert_matches_type(Optional[CustomNListResponse], custom_n, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.custom_ns.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        custom_n = client.custom_ns.delete(
            "ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(Optional[CustomNDeleteResponse], custom_n, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.custom_ns.with_raw_response.delete(
            "ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_n = response.parse()
        assert_matches_type(Optional[CustomNDeleteResponse], custom_n, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.custom_ns.with_streaming_response.delete(
            "ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_n = response.parse()
            assert_matches_type(Optional[CustomNDeleteResponse], custom_n, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.custom_ns.with_raw_response.delete(
                "ns1.example.com",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_ns_id` but received ''"):
            client.custom_ns.with_raw_response.delete(
                "",
                account_id="372e67954025e0ba6aaa6d586b9e0b59",
            )


class TestAsyncCustomNs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        custom_n = await async_client.custom_ns.create(
            "372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        )
        assert_matches_type(CustomNCreateResponse, custom_n, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom_n = await async_client.custom_ns.create(
            "372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
            ns_set=1,
        )
        assert_matches_type(CustomNCreateResponse, custom_n, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_ns.with_raw_response.create(
            "372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_n = await response.parse()
        assert_matches_type(CustomNCreateResponse, custom_n, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_ns.with_streaming_response.create(
            "372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_n = await response.parse()
            assert_matches_type(CustomNCreateResponse, custom_n, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.custom_ns.with_raw_response.create(
                "",
                ns_name="ns1.example.com",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        custom_n = await async_client.custom_ns.list(
            "372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(Optional[CustomNListResponse], custom_n, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_ns.with_raw_response.list(
            "372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_n = await response.parse()
        assert_matches_type(Optional[CustomNListResponse], custom_n, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_ns.with_streaming_response.list(
            "372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_n = await response.parse()
            assert_matches_type(Optional[CustomNListResponse], custom_n, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.custom_ns.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        custom_n = await async_client.custom_ns.delete(
            "ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(Optional[CustomNDeleteResponse], custom_n, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_ns.with_raw_response.delete(
            "ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_n = await response.parse()
        assert_matches_type(Optional[CustomNDeleteResponse], custom_n, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_ns.with_streaming_response.delete(
            "ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_n = await response.parse()
            assert_matches_type(Optional[CustomNDeleteResponse], custom_n, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.custom_ns.with_raw_response.delete(
                "ns1.example.com",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_ns_id` but received ''"):
            await async_client.custom_ns.with_raw_response.delete(
                "",
                account_id="372e67954025e0ba6aaa6d586b9e0b59",
            )
