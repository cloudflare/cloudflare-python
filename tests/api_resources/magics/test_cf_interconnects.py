# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.magics import (
    CfInterconnectUpdateResponse,
    CfInterconnectGetResponse,
    CfInterconnectMagicInterconnectsListInterconnectsResponse,
    CfInterconnectMagicInterconnectsUpdateMultipleInterconnectsResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magics import cf_interconnect_update_params
from cloudflare.types.magics import cf_interconnect_magic_interconnects_update_multiple_interconnects_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCfInterconnects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        cf_interconnect = client.magics.cf_interconnects.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        cf_interconnect = client.magics.cf_interconnects.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="Tunnel for Interconnect to ORD",
            gre={"cloudflare_endpoint": "203.0.113.1"},
            health_check={
                "enabled": True,
                "rate": "low",
                "target": "203.0.113.1",
                "type": "request",
            },
            interface_address="192.0.2.0/31",
            mtu=0,
        )
        assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magics.cf_interconnects.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = response.parse()
        assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magics.cf_interconnects.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = response.parse()
            assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.cf_interconnects.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magics.cf_interconnects.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        cf_interconnect = client.magics.cf_interconnects.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CfInterconnectGetResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magics.cf_interconnects.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = response.parse()
        assert_matches_type(CfInterconnectGetResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magics.cf_interconnects.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = response.parse()
            assert_matches_type(CfInterconnectGetResponse, cf_interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.cf_interconnects.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magics.cf_interconnects.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_interconnects_list_interconnects(self, client: Cloudflare) -> None:
        cf_interconnect = client.magics.cf_interconnects.magic_interconnects_list_interconnects(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            CfInterconnectMagicInterconnectsListInterconnectsResponse, cf_interconnect, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_interconnects_list_interconnects(self, client: Cloudflare) -> None:
        response = client.magics.cf_interconnects.with_raw_response.magic_interconnects_list_interconnects(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = response.parse()
        assert_matches_type(
            CfInterconnectMagicInterconnectsListInterconnectsResponse, cf_interconnect, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_interconnects_list_interconnects(self, client: Cloudflare) -> None:
        with client.magics.cf_interconnects.with_streaming_response.magic_interconnects_list_interconnects(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = response.parse()
            assert_matches_type(
                CfInterconnectMagicInterconnectsListInterconnectsResponse, cf_interconnect, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_magic_interconnects_list_interconnects(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.cf_interconnects.with_raw_response.magic_interconnects_list_interconnects(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_interconnects_update_multiple_interconnects(self, client: Cloudflare) -> None:
        cf_interconnect = client.magics.cf_interconnects.magic_interconnects_update_multiple_interconnects(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(
            CfInterconnectMagicInterconnectsUpdateMultipleInterconnectsResponse, cf_interconnect, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_interconnects_update_multiple_interconnects(self, client: Cloudflare) -> None:
        response = client.magics.cf_interconnects.with_raw_response.magic_interconnects_update_multiple_interconnects(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = response.parse()
        assert_matches_type(
            CfInterconnectMagicInterconnectsUpdateMultipleInterconnectsResponse, cf_interconnect, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_interconnects_update_multiple_interconnects(self, client: Cloudflare) -> None:
        with client.magics.cf_interconnects.with_streaming_response.magic_interconnects_update_multiple_interconnects(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = response.parse()
            assert_matches_type(
                CfInterconnectMagicInterconnectsUpdateMultipleInterconnectsResponse, cf_interconnect, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_magic_interconnects_update_multiple_interconnects(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.cf_interconnects.with_raw_response.magic_interconnects_update_multiple_interconnects(
                "",
                body={},
            )


class TestAsyncCfInterconnects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        cf_interconnect = await async_client.magics.cf_interconnects.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cf_interconnect = await async_client.magics.cf_interconnects.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="Tunnel for Interconnect to ORD",
            gre={"cloudflare_endpoint": "203.0.113.1"},
            health_check={
                "enabled": True,
                "rate": "low",
                "target": "203.0.113.1",
                "type": "request",
            },
            interface_address="192.0.2.0/31",
            mtu=0,
        )
        assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.cf_interconnects.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = await response.parse()
        assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magics.cf_interconnects.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = await response.parse()
            assert_matches_type(CfInterconnectUpdateResponse, cf_interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.cf_interconnects.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magics.cf_interconnects.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        cf_interconnect = await async_client.magics.cf_interconnects.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CfInterconnectGetResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.cf_interconnects.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = await response.parse()
        assert_matches_type(CfInterconnectGetResponse, cf_interconnect, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magics.cf_interconnects.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = await response.parse()
            assert_matches_type(CfInterconnectGetResponse, cf_interconnect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.cf_interconnects.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magics.cf_interconnects.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_interconnects_list_interconnects(self, async_client: AsyncCloudflare) -> None:
        cf_interconnect = await async_client.magics.cf_interconnects.magic_interconnects_list_interconnects(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            CfInterconnectMagicInterconnectsListInterconnectsResponse, cf_interconnect, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_interconnects_list_interconnects(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.cf_interconnects.with_raw_response.magic_interconnects_list_interconnects(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = await response.parse()
        assert_matches_type(
            CfInterconnectMagicInterconnectsListInterconnectsResponse, cf_interconnect, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_interconnects_list_interconnects(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.magics.cf_interconnects.with_streaming_response.magic_interconnects_list_interconnects(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = await response.parse()
            assert_matches_type(
                CfInterconnectMagicInterconnectsListInterconnectsResponse, cf_interconnect, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_magic_interconnects_list_interconnects(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.cf_interconnects.with_raw_response.magic_interconnects_list_interconnects(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_interconnects_update_multiple_interconnects(
        self, async_client: AsyncCloudflare
    ) -> None:
        cf_interconnect = await async_client.magics.cf_interconnects.magic_interconnects_update_multiple_interconnects(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(
            CfInterconnectMagicInterconnectsUpdateMultipleInterconnectsResponse, cf_interconnect, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_interconnects_update_multiple_interconnects(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.magics.cf_interconnects.with_raw_response.magic_interconnects_update_multiple_interconnects(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cf_interconnect = await response.parse()
        assert_matches_type(
            CfInterconnectMagicInterconnectsUpdateMultipleInterconnectsResponse, cf_interconnect, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_interconnects_update_multiple_interconnects(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.magics.cf_interconnects.with_streaming_response.magic_interconnects_update_multiple_interconnects(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cf_interconnect = await response.parse()
            assert_matches_type(
                CfInterconnectMagicInterconnectsUpdateMultipleInterconnectsResponse, cf_interconnect, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_magic_interconnects_update_multiple_interconnects(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.cf_interconnects.with_raw_response.magic_interconnects_update_multiple_interconnects(
                "",
                body={},
            )
