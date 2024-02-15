# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.firewalls.waf import (
    OverrideUpdateResponse,
    OverrideDeleteResponse,
    OverrideGetResponse,
    OverrideWAFOverridesCreateAWAFOverrideResponse,
    OverrideWAFOverridesListWAFOverridesResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.firewalls.waf import override_update_params
from cloudflare.types.firewalls.waf import override_waf_overrides_create_a_waf_override_params
from cloudflare.types.firewalls.waf import override_waf_overrides_list_waf_overrides_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOverrides:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        override = client.firewalls.waf.overrides.update(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[OverrideUpdateResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.firewalls.waf.overrides.with_raw_response.update(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(Optional[OverrideUpdateResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.firewalls.waf.overrides.with_streaming_response.update(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(Optional[OverrideUpdateResponse], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.waf.overrides.with_raw_response.update(
                "de677e5818985db1285d0e80225f06e5",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewalls.waf.overrides.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        override = client.firewalls.waf.overrides.delete(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OverrideDeleteResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.firewalls.waf.overrides.with_raw_response.delete(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(Optional[OverrideDeleteResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.firewalls.waf.overrides.with_streaming_response.delete(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(Optional[OverrideDeleteResponse], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.waf.overrides.with_raw_response.delete(
                "de677e5818985db1285d0e80225f06e5",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewalls.waf.overrides.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        override = client.firewalls.waf.overrides.get(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OverrideGetResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.firewalls.waf.overrides.with_raw_response.get(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(Optional[OverrideGetResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.firewalls.waf.overrides.with_streaming_response.get(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(Optional[OverrideGetResponse], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.waf.overrides.with_raw_response.get(
                "de677e5818985db1285d0e80225f06e5",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewalls.waf.overrides.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_waf_overrides_create_a_waf_override(self, client: Cloudflare) -> None:
        override = client.firewalls.waf.overrides.waf_overrides_create_a_waf_override(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[OverrideWAFOverridesCreateAWAFOverrideResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_waf_overrides_create_a_waf_override(self, client: Cloudflare) -> None:
        response = client.firewalls.waf.overrides.with_raw_response.waf_overrides_create_a_waf_override(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(Optional[OverrideWAFOverridesCreateAWAFOverrideResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_waf_overrides_create_a_waf_override(self, client: Cloudflare) -> None:
        with client.firewalls.waf.overrides.with_streaming_response.waf_overrides_create_a_waf_override(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(Optional[OverrideWAFOverridesCreateAWAFOverrideResponse], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_waf_overrides_create_a_waf_override(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.waf.overrides.with_raw_response.waf_overrides_create_a_waf_override(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_waf_overrides_list_waf_overrides(self, client: Cloudflare) -> None:
        override = client.firewalls.waf.overrides.waf_overrides_list_waf_overrides(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OverrideWAFOverridesListWAFOverridesResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_waf_overrides_list_waf_overrides_with_all_params(self, client: Cloudflare) -> None:
        override = client.firewalls.waf.overrides.waf_overrides_list_waf_overrides(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=5,
        )
        assert_matches_type(Optional[OverrideWAFOverridesListWAFOverridesResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_waf_overrides_list_waf_overrides(self, client: Cloudflare) -> None:
        response = client.firewalls.waf.overrides.with_raw_response.waf_overrides_list_waf_overrides(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(Optional[OverrideWAFOverridesListWAFOverridesResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_waf_overrides_list_waf_overrides(self, client: Cloudflare) -> None:
        with client.firewalls.waf.overrides.with_streaming_response.waf_overrides_list_waf_overrides(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(Optional[OverrideWAFOverridesListWAFOverridesResponse], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_waf_overrides_list_waf_overrides(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.waf.overrides.with_raw_response.waf_overrides_list_waf_overrides(
                "",
            )


class TestAsyncOverrides:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        override = await async_client.firewalls.waf.overrides.update(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[OverrideUpdateResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.waf.overrides.with_raw_response.update(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(Optional[OverrideUpdateResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.waf.overrides.with_streaming_response.update(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(Optional[OverrideUpdateResponse], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.waf.overrides.with_raw_response.update(
                "de677e5818985db1285d0e80225f06e5",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewalls.waf.overrides.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        override = await async_client.firewalls.waf.overrides.delete(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OverrideDeleteResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.waf.overrides.with_raw_response.delete(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(Optional[OverrideDeleteResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.waf.overrides.with_streaming_response.delete(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(Optional[OverrideDeleteResponse], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.waf.overrides.with_raw_response.delete(
                "de677e5818985db1285d0e80225f06e5",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewalls.waf.overrides.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        override = await async_client.firewalls.waf.overrides.get(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OverrideGetResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.waf.overrides.with_raw_response.get(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(Optional[OverrideGetResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.waf.overrides.with_streaming_response.get(
            "de677e5818985db1285d0e80225f06e5",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(Optional[OverrideGetResponse], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.waf.overrides.with_raw_response.get(
                "de677e5818985db1285d0e80225f06e5",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewalls.waf.overrides.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_waf_overrides_create_a_waf_override(self, async_client: AsyncCloudflare) -> None:
        override = await async_client.firewalls.waf.overrides.waf_overrides_create_a_waf_override(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[OverrideWAFOverridesCreateAWAFOverrideResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_waf_overrides_create_a_waf_override(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.waf.overrides.with_raw_response.waf_overrides_create_a_waf_override(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(Optional[OverrideWAFOverridesCreateAWAFOverrideResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_waf_overrides_create_a_waf_override(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.waf.overrides.with_streaming_response.waf_overrides_create_a_waf_override(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(Optional[OverrideWAFOverridesCreateAWAFOverrideResponse], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_waf_overrides_create_a_waf_override(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.waf.overrides.with_raw_response.waf_overrides_create_a_waf_override(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_waf_overrides_list_waf_overrides(self, async_client: AsyncCloudflare) -> None:
        override = await async_client.firewalls.waf.overrides.waf_overrides_list_waf_overrides(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OverrideWAFOverridesListWAFOverridesResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_waf_overrides_list_waf_overrides_with_all_params(self, async_client: AsyncCloudflare) -> None:
        override = await async_client.firewalls.waf.overrides.waf_overrides_list_waf_overrides(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=5,
        )
        assert_matches_type(Optional[OverrideWAFOverridesListWAFOverridesResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_waf_overrides_list_waf_overrides(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.waf.overrides.with_raw_response.waf_overrides_list_waf_overrides(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(Optional[OverrideWAFOverridesListWAFOverridesResponse], override, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_waf_overrides_list_waf_overrides(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.waf.overrides.with_streaming_response.waf_overrides_list_waf_overrides(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(Optional[OverrideWAFOverridesListWAFOverridesResponse], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_waf_overrides_list_waf_overrides(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.waf.overrides.with_raw_response.waf_overrides_list_waf_overrides(
                "",
            )
