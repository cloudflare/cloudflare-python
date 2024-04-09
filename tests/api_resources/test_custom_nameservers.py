# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import (
    CustomNameserver,
    CustomNameserverGetResponse,
    CustomNameserverDeleteResponse,
    CustomNameserverVerifyResponse,
    CustomNameserverAvailabiltyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomNameservers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        custom_nameserver = client.custom_nameservers.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        )
        assert_matches_type(CustomNameserver, custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        custom_nameserver = client.custom_nameservers.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
            ns_set=1,
        )
        assert_matches_type(CustomNameserver, custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.custom_nameservers.with_raw_response.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = response.parse()
        assert_matches_type(CustomNameserver, custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.custom_nameservers.with_streaming_response.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = response.parse()
            assert_matches_type(CustomNameserver, custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.custom_nameservers.with_raw_response.create(
                account_id="",
                ns_name="ns1.example.com",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        custom_nameserver = client.custom_nameservers.delete(
            "ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            body={},
        )
        assert_matches_type(Optional[CustomNameserverDeleteResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.custom_nameservers.with_raw_response.delete(
            "ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = response.parse()
        assert_matches_type(Optional[CustomNameserverDeleteResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.custom_nameservers.with_streaming_response.delete(
            "ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = response.parse()
            assert_matches_type(Optional[CustomNameserverDeleteResponse], custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.custom_nameservers.with_raw_response.delete(
                "ns1.example.com",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_ns_id` but received ''"):
            client.custom_nameservers.with_raw_response.delete(
                "",
                account_id="372e67954025e0ba6aaa6d586b9e0b59",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_availabilty(self, client: Cloudflare) -> None:
        custom_nameserver = client.custom_nameservers.availabilty(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(Optional[CustomNameserverAvailabiltyResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_availabilty(self, client: Cloudflare) -> None:
        response = client.custom_nameservers.with_raw_response.availabilty(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = response.parse()
        assert_matches_type(Optional[CustomNameserverAvailabiltyResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_availabilty(self, client: Cloudflare) -> None:
        with client.custom_nameservers.with_streaming_response.availabilty(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = response.parse()
            assert_matches_type(Optional[CustomNameserverAvailabiltyResponse], custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_availabilty(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.custom_nameservers.with_raw_response.availabilty(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        custom_nameserver = client.custom_nameservers.get(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(Optional[CustomNameserverGetResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.custom_nameservers.with_raw_response.get(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = response.parse()
        assert_matches_type(Optional[CustomNameserverGetResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.custom_nameservers.with_streaming_response.get(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = response.parse()
            assert_matches_type(Optional[CustomNameserverGetResponse], custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.custom_nameservers.with_raw_response.get(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_verify(self, client: Cloudflare) -> None:
        custom_nameserver = client.custom_nameservers.verify(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            body={},
        )
        assert_matches_type(Optional[CustomNameserverVerifyResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_verify(self, client: Cloudflare) -> None:
        response = client.custom_nameservers.with_raw_response.verify(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = response.parse()
        assert_matches_type(Optional[CustomNameserverVerifyResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_verify(self, client: Cloudflare) -> None:
        with client.custom_nameservers.with_streaming_response.verify(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = response.parse()
            assert_matches_type(Optional[CustomNameserverVerifyResponse], custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_verify(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.custom_nameservers.with_raw_response.verify(
                account_id="",
                body={},
            )


class TestAsyncCustomNameservers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        custom_nameserver = await async_client.custom_nameservers.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        )
        assert_matches_type(CustomNameserver, custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom_nameserver = await async_client.custom_nameservers.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
            ns_set=1,
        )
        assert_matches_type(CustomNameserver, custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_nameservers.with_raw_response.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = await response.parse()
        assert_matches_type(CustomNameserver, custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_nameservers.with_streaming_response.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = await response.parse()
            assert_matches_type(CustomNameserver, custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.custom_nameservers.with_raw_response.create(
                account_id="",
                ns_name="ns1.example.com",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        custom_nameserver = await async_client.custom_nameservers.delete(
            "ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            body={},
        )
        assert_matches_type(Optional[CustomNameserverDeleteResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_nameservers.with_raw_response.delete(
            "ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = await response.parse()
        assert_matches_type(Optional[CustomNameserverDeleteResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_nameservers.with_streaming_response.delete(
            "ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = await response.parse()
            assert_matches_type(Optional[CustomNameserverDeleteResponse], custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.custom_nameservers.with_raw_response.delete(
                "ns1.example.com",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_ns_id` but received ''"):
            await async_client.custom_nameservers.with_raw_response.delete(
                "",
                account_id="372e67954025e0ba6aaa6d586b9e0b59",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_availabilty(self, async_client: AsyncCloudflare) -> None:
        custom_nameserver = await async_client.custom_nameservers.availabilty(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(Optional[CustomNameserverAvailabiltyResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_availabilty(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_nameservers.with_raw_response.availabilty(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = await response.parse()
        assert_matches_type(Optional[CustomNameserverAvailabiltyResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_availabilty(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_nameservers.with_streaming_response.availabilty(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = await response.parse()
            assert_matches_type(Optional[CustomNameserverAvailabiltyResponse], custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_availabilty(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.custom_nameservers.with_raw_response.availabilty(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        custom_nameserver = await async_client.custom_nameservers.get(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(Optional[CustomNameserverGetResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_nameservers.with_raw_response.get(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = await response.parse()
        assert_matches_type(Optional[CustomNameserverGetResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_nameservers.with_streaming_response.get(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = await response.parse()
            assert_matches_type(Optional[CustomNameserverGetResponse], custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.custom_nameservers.with_raw_response.get(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_verify(self, async_client: AsyncCloudflare) -> None:
        custom_nameserver = await async_client.custom_nameservers.verify(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            body={},
        )
        assert_matches_type(Optional[CustomNameserverVerifyResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_nameservers.with_raw_response.verify(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = await response.parse()
        assert_matches_type(Optional[CustomNameserverVerifyResponse], custom_nameserver, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_nameservers.with_streaming_response.verify(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = await response.parse()
            assert_matches_type(Optional[CustomNameserverVerifyResponse], custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_verify(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.custom_nameservers.with_raw_response.verify(
                account_id="",
                body={},
            )
