# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.network_interconnects import (
    CNIGetResponse,
    CNIListResponse,
    CNICreateResponse,
    CNIUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCNIs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        cni = client.network_interconnects.cnis.create(
            account_id="account_id",
            account="account",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
        )
        assert_matches_type(CNICreateResponse, cni, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        cni = client.network_interconnects.cnis.create(
            account_id="account_id",
            account="account",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
            bgp={
                "customer_asn": 0,
                "extra_prefixes": ["string"],
                "md5_key": "md5_key",
            },
        )
        assert_matches_type(CNICreateResponse, cni, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.network_interconnects.cnis.with_raw_response.create(
            account_id="account_id",
            account="account",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cni = response.parse()
        assert_matches_type(CNICreateResponse, cni, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.network_interconnects.cnis.with_streaming_response.create(
            account_id="account_id",
            account="account",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cni = response.parse()
            assert_matches_type(CNICreateResponse, cni, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.network_interconnects.cnis.with_raw_response.create(
                account_id="",
                account="account",
                interconnect="interconnect",
                magic={
                    "conduit_name": "conduit_name",
                    "description": "description",
                    "mtu": 0,
                },
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        cni = client.network_interconnects.cnis.update(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account="account",
            cust_ip="192.168.3.4/31",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
            p2p_ip="192.168.3.4/31",
        )
        assert_matches_type(CNIUpdateResponse, cni, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        cni = client.network_interconnects.cnis.update(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account="account",
            cust_ip="192.168.3.4/31",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
            p2p_ip="192.168.3.4/31",
            bgp={
                "customer_asn": 0,
                "extra_prefixes": ["string"],
                "md5_key": "md5_key",
            },
        )
        assert_matches_type(CNIUpdateResponse, cni, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.network_interconnects.cnis.with_raw_response.update(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account="account",
            cust_ip="192.168.3.4/31",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
            p2p_ip="192.168.3.4/31",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cni = response.parse()
        assert_matches_type(CNIUpdateResponse, cni, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.network_interconnects.cnis.with_streaming_response.update(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account="account",
            cust_ip="192.168.3.4/31",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
            p2p_ip="192.168.3.4/31",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cni = response.parse()
            assert_matches_type(CNIUpdateResponse, cni, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.network_interconnects.cnis.with_raw_response.update(
                cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account="account",
                cust_ip="192.168.3.4/31",
                interconnect="interconnect",
                magic={
                    "conduit_name": "conduit_name",
                    "description": "description",
                    "mtu": 0,
                },
                p2p_ip="192.168.3.4/31",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cni` but received ''"):
            client.network_interconnects.cnis.with_raw_response.update(
                cni="",
                account_id="account_id",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account="account",
                cust_ip="192.168.3.4/31",
                interconnect="interconnect",
                magic={
                    "conduit_name": "conduit_name",
                    "description": "description",
                    "mtu": 0,
                },
                p2p_ip="192.168.3.4/31",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        cni = client.network_interconnects.cnis.list(
            account_id="account_id",
        )
        assert_matches_type(CNIListResponse, cni, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        cni = client.network_interconnects.cnis.list(
            account_id="account_id",
            cursor=0,
            limit=0,
            slot="slot",
        )
        assert_matches_type(CNIListResponse, cni, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.network_interconnects.cnis.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cni = response.parse()
        assert_matches_type(CNIListResponse, cni, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.network_interconnects.cnis.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cni = response.parse()
            assert_matches_type(CNIListResponse, cni, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.network_interconnects.cnis.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        cni = client.network_interconnects.cnis.delete(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert cni is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.network_interconnects.cnis.with_raw_response.delete(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cni = response.parse()
        assert cni is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.network_interconnects.cnis.with_streaming_response.delete(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cni = response.parse()
            assert cni is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.network_interconnects.cnis.with_raw_response.delete(
                cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cni` but received ''"):
            client.network_interconnects.cnis.with_raw_response.delete(
                cni="",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        cni = client.network_interconnects.cnis.get(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CNIGetResponse, cni, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.network_interconnects.cnis.with_raw_response.get(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cni = response.parse()
        assert_matches_type(CNIGetResponse, cni, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.network_interconnects.cnis.with_streaming_response.get(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cni = response.parse()
            assert_matches_type(CNIGetResponse, cni, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.network_interconnects.cnis.with_raw_response.get(
                cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cni` but received ''"):
            client.network_interconnects.cnis.with_raw_response.get(
                cni="",
                account_id="account_id",
            )


class TestAsyncCNIs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        cni = await async_client.network_interconnects.cnis.create(
            account_id="account_id",
            account="account",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
        )
        assert_matches_type(CNICreateResponse, cni, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cni = await async_client.network_interconnects.cnis.create(
            account_id="account_id",
            account="account",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
            bgp={
                "customer_asn": 0,
                "extra_prefixes": ["string"],
                "md5_key": "md5_key",
            },
        )
        assert_matches_type(CNICreateResponse, cni, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.network_interconnects.cnis.with_raw_response.create(
            account_id="account_id",
            account="account",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cni = await response.parse()
        assert_matches_type(CNICreateResponse, cni, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.network_interconnects.cnis.with_streaming_response.create(
            account_id="account_id",
            account="account",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cni = await response.parse()
            assert_matches_type(CNICreateResponse, cni, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.network_interconnects.cnis.with_raw_response.create(
                account_id="",
                account="account",
                interconnect="interconnect",
                magic={
                    "conduit_name": "conduit_name",
                    "description": "description",
                    "mtu": 0,
                },
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        cni = await async_client.network_interconnects.cnis.update(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account="account",
            cust_ip="192.168.3.4/31",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
            p2p_ip="192.168.3.4/31",
        )
        assert_matches_type(CNIUpdateResponse, cni, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cni = await async_client.network_interconnects.cnis.update(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account="account",
            cust_ip="192.168.3.4/31",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
            p2p_ip="192.168.3.4/31",
            bgp={
                "customer_asn": 0,
                "extra_prefixes": ["string"],
                "md5_key": "md5_key",
            },
        )
        assert_matches_type(CNIUpdateResponse, cni, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.network_interconnects.cnis.with_raw_response.update(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account="account",
            cust_ip="192.168.3.4/31",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
            p2p_ip="192.168.3.4/31",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cni = await response.parse()
        assert_matches_type(CNIUpdateResponse, cni, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.network_interconnects.cnis.with_streaming_response.update(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account="account",
            cust_ip="192.168.3.4/31",
            interconnect="interconnect",
            magic={
                "conduit_name": "conduit_name",
                "description": "description",
                "mtu": 0,
            },
            p2p_ip="192.168.3.4/31",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cni = await response.parse()
            assert_matches_type(CNIUpdateResponse, cni, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.network_interconnects.cnis.with_raw_response.update(
                cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account="account",
                cust_ip="192.168.3.4/31",
                interconnect="interconnect",
                magic={
                    "conduit_name": "conduit_name",
                    "description": "description",
                    "mtu": 0,
                },
                p2p_ip="192.168.3.4/31",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cni` but received ''"):
            await async_client.network_interconnects.cnis.with_raw_response.update(
                cni="",
                account_id="account_id",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account="account",
                cust_ip="192.168.3.4/31",
                interconnect="interconnect",
                magic={
                    "conduit_name": "conduit_name",
                    "description": "description",
                    "mtu": 0,
                },
                p2p_ip="192.168.3.4/31",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        cni = await async_client.network_interconnects.cnis.list(
            account_id="account_id",
        )
        assert_matches_type(CNIListResponse, cni, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cni = await async_client.network_interconnects.cnis.list(
            account_id="account_id",
            cursor=0,
            limit=0,
            slot="slot",
        )
        assert_matches_type(CNIListResponse, cni, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.network_interconnects.cnis.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cni = await response.parse()
        assert_matches_type(CNIListResponse, cni, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.network_interconnects.cnis.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cni = await response.parse()
            assert_matches_type(CNIListResponse, cni, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.network_interconnects.cnis.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        cni = await async_client.network_interconnects.cnis.delete(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert cni is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.network_interconnects.cnis.with_raw_response.delete(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cni = await response.parse()
        assert cni is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.network_interconnects.cnis.with_streaming_response.delete(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cni = await response.parse()
            assert cni is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.network_interconnects.cnis.with_raw_response.delete(
                cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cni` but received ''"):
            await async_client.network_interconnects.cnis.with_raw_response.delete(
                cni="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        cni = await async_client.network_interconnects.cnis.get(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CNIGetResponse, cni, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.network_interconnects.cnis.with_raw_response.get(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cni = await response.parse()
        assert_matches_type(CNIGetResponse, cni, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.network_interconnects.cnis.with_streaming_response.get(
            cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cni = await response.parse()
            assert_matches_type(CNIGetResponse, cni, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.network_interconnects.cnis.with_raw_response.get(
                cni="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cni` but received ''"):
            await async_client.network_interconnects.cnis.with_raw_response.get(
                cni="",
                account_id="account_id",
            )
