# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.intel.sinkholes import (
    IngressGetResponse,
    IngressCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIngresses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        ingress = client.intel.sinkholes.ingresses.create(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="cidr",
        )
        assert_matches_type(Optional[IngressCreateResponse], ingress, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.intel.sinkholes.ingresses.with_raw_response.create(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="cidr",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = response.parse()
        assert_matches_type(Optional[IngressCreateResponse], ingress, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.intel.sinkholes.ingresses.with_streaming_response.create(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="cidr",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = response.parse()
            assert_matches_type(Optional[IngressCreateResponse], ingress, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.intel.sinkholes.ingresses.with_raw_response.create(
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
                zone_id="",
                cidr="cidr",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sinkhole_id` but received ''"):
            client.intel.sinkholes.ingresses.with_raw_response.create(
                sinkhole_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                cidr="cidr",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        ingress = client.intel.sinkholes.ingresses.update(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            cidr="cidr",
        )
        assert_matches_type(object, ingress, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.intel.sinkholes.ingresses.with_raw_response.update(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            cidr="cidr",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = response.parse()
        assert_matches_type(object, ingress, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.intel.sinkholes.ingresses.with_streaming_response.update(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            cidr="cidr",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = response.parse()
            assert_matches_type(object, ingress, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.intel.sinkholes.ingresses.with_raw_response.update(
                ingress_id="de32ae5203724ed08dcc26e971a4d22f",
                zone_id="",
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
                cidr="cidr",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sinkhole_id` but received ''"):
            client.intel.sinkholes.ingresses.with_raw_response.update(
                ingress_id="de32ae5203724ed08dcc26e971a4d22f",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                sinkhole_id="",
                cidr="cidr",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ingress_id` but received ''"):
            client.intel.sinkholes.ingresses.with_raw_response.update(
                ingress_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
                cidr="cidr",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        ingress = client.intel.sinkholes.ingresses.delete(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
        )
        assert_matches_type(object, ingress, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.intel.sinkholes.ingresses.with_raw_response.delete(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = response.parse()
        assert_matches_type(object, ingress, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.intel.sinkholes.ingresses.with_streaming_response.delete(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = response.parse()
            assert_matches_type(object, ingress, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.intel.sinkholes.ingresses.with_raw_response.delete(
                ingress_id="de32ae5203724ed08dcc26e971a4d22f",
                zone_id="",
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sinkhole_id` but received ''"):
            client.intel.sinkholes.ingresses.with_raw_response.delete(
                ingress_id="de32ae5203724ed08dcc26e971a4d22f",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                sinkhole_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ingress_id` but received ''"):
            client.intel.sinkholes.ingresses.with_raw_response.delete(
                ingress_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ingress = client.intel.sinkholes.ingresses.get(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
        )
        assert_matches_type(Optional[IngressGetResponse], ingress, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.intel.sinkholes.ingresses.with_raw_response.get(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = response.parse()
        assert_matches_type(Optional[IngressGetResponse], ingress, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.intel.sinkholes.ingresses.with_streaming_response.get(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = response.parse()
            assert_matches_type(Optional[IngressGetResponse], ingress, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.intel.sinkholes.ingresses.with_raw_response.get(
                ingress_id="de32ae5203724ed08dcc26e971a4d22f",
                zone_id="",
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sinkhole_id` but received ''"):
            client.intel.sinkholes.ingresses.with_raw_response.get(
                ingress_id="de32ae5203724ed08dcc26e971a4d22f",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                sinkhole_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ingress_id` but received ''"):
            client.intel.sinkholes.ingresses.with_raw_response.get(
                ingress_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            )


class TestAsyncIngresses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        ingress = await async_client.intel.sinkholes.ingresses.create(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="cidr",
        )
        assert_matches_type(Optional[IngressCreateResponse], ingress, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.sinkholes.ingresses.with_raw_response.create(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="cidr",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = await response.parse()
        assert_matches_type(Optional[IngressCreateResponse], ingress, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.sinkholes.ingresses.with_streaming_response.create(
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="cidr",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = await response.parse()
            assert_matches_type(Optional[IngressCreateResponse], ingress, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.intel.sinkholes.ingresses.with_raw_response.create(
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
                zone_id="",
                cidr="cidr",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sinkhole_id` but received ''"):
            await async_client.intel.sinkholes.ingresses.with_raw_response.create(
                sinkhole_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                cidr="cidr",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        ingress = await async_client.intel.sinkholes.ingresses.update(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            cidr="cidr",
        )
        assert_matches_type(object, ingress, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.sinkholes.ingresses.with_raw_response.update(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            cidr="cidr",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = await response.parse()
        assert_matches_type(object, ingress, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.sinkholes.ingresses.with_streaming_response.update(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            cidr="cidr",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = await response.parse()
            assert_matches_type(object, ingress, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.intel.sinkholes.ingresses.with_raw_response.update(
                ingress_id="de32ae5203724ed08dcc26e971a4d22f",
                zone_id="",
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
                cidr="cidr",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sinkhole_id` but received ''"):
            await async_client.intel.sinkholes.ingresses.with_raw_response.update(
                ingress_id="de32ae5203724ed08dcc26e971a4d22f",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                sinkhole_id="",
                cidr="cidr",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ingress_id` but received ''"):
            await async_client.intel.sinkholes.ingresses.with_raw_response.update(
                ingress_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
                cidr="cidr",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        ingress = await async_client.intel.sinkholes.ingresses.delete(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
        )
        assert_matches_type(object, ingress, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.sinkholes.ingresses.with_raw_response.delete(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = await response.parse()
        assert_matches_type(object, ingress, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.sinkholes.ingresses.with_streaming_response.delete(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = await response.parse()
            assert_matches_type(object, ingress, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.intel.sinkholes.ingresses.with_raw_response.delete(
                ingress_id="de32ae5203724ed08dcc26e971a4d22f",
                zone_id="",
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sinkhole_id` but received ''"):
            await async_client.intel.sinkholes.ingresses.with_raw_response.delete(
                ingress_id="de32ae5203724ed08dcc26e971a4d22f",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                sinkhole_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ingress_id` but received ''"):
            await async_client.intel.sinkholes.ingresses.with_raw_response.delete(
                ingress_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ingress = await async_client.intel.sinkholes.ingresses.get(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
        )
        assert_matches_type(Optional[IngressGetResponse], ingress, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.sinkholes.ingresses.with_raw_response.get(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ingress = await response.parse()
        assert_matches_type(Optional[IngressGetResponse], ingress, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.sinkholes.ingresses.with_streaming_response.get(
            ingress_id="de32ae5203724ed08dcc26e971a4d22f",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ingress = await response.parse()
            assert_matches_type(Optional[IngressGetResponse], ingress, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.intel.sinkholes.ingresses.with_raw_response.get(
                ingress_id="de32ae5203724ed08dcc26e971a4d22f",
                zone_id="",
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sinkhole_id` but received ''"):
            await async_client.intel.sinkholes.ingresses.with_raw_response.get(
                ingress_id="de32ae5203724ed08dcc26e971a4d22f",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                sinkhole_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ingress_id` but received ''"):
            await async_client.intel.sinkholes.ingresses.with_raw_response.get(
                ingress_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                sinkhole_id="93defa6e909e464e8c89a85859f36d3c",
            )
