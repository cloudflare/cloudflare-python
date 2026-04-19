# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.resource_tagging import (
    ZoneTagGetResponse,
    ZoneTagUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestZoneTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        zone_tag = client.resource_tagging.zone_tags.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        )
        assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Cloudflare) -> None:
        zone_tag = client.resource_tagging.zone_tags.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
            tags={
                "environment": "production",
                "team": "engineering",
            },
            if_match='"v1:RBNvo1WzZ4oRRq0W9-hkng"',
        )
        assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.resource_tagging.zone_tags.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone_tag = response.parse()
        assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Cloudflare) -> None:
        with client.resource_tagging.zone_tags.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone_tag = response.parse()
            assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.resource_tagging.zone_tags.with_raw_response.update(
                zone_id="",
                resource_id="023e105f4ecef8ad9ca31a8372d0c353",
                resource_type="zone",
            )

    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        zone_tag = client.resource_tagging.zone_tags.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            access_application_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        )
        assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Cloudflare) -> None:
        zone_tag = client.resource_tagging.zone_tags.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            access_application_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
            tags={
                "environment": "production",
                "team": "engineering",
            },
            if_match='"v1:RBNvo1WzZ4oRRq0W9-hkng"',
        )
        assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.resource_tagging.zone_tags.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            access_application_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone_tag = response.parse()
        assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Cloudflare) -> None:
        with client.resource_tagging.zone_tags.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            access_application_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone_tag = response.parse()
            assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.resource_tagging.zone_tags.with_raw_response.update(
                zone_id="",
                access_application_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                resource_id="023e105f4ecef8ad9ca31a8372d0c353",
                resource_type="zone",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        zone_tag = client.resource_tagging.zone_tags.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert zone_tag is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        zone_tag = client.resource_tagging.zone_tags.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            if_match='"v1:RBNvo1WzZ4oRRq0W9-hkng"',
        )
        assert zone_tag is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.resource_tagging.zone_tags.with_raw_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone_tag = response.parse()
        assert zone_tag is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.resource_tagging.zone_tags.with_streaming_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone_tag = response.parse()
            assert zone_tag is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.resource_tagging.zone_tags.with_raw_response.delete(
                zone_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        zone_tag = client.resource_tagging.zone_tags.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        )
        assert_matches_type(Optional[ZoneTagGetResponse], zone_tag, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        zone_tag = client.resource_tagging.zone_tags.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
            access_application_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Optional[ZoneTagGetResponse], zone_tag, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.resource_tagging.zone_tags.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone_tag = response.parse()
        assert_matches_type(Optional[ZoneTagGetResponse], zone_tag, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.resource_tagging.zone_tags.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone_tag = response.parse()
            assert_matches_type(Optional[ZoneTagGetResponse], zone_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.resource_tagging.zone_tags.with_raw_response.get(
                zone_id="",
                resource_id="023e105f4ecef8ad9ca31a8372d0c353",
                resource_type="zone",
            )


class TestAsyncZoneTags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        zone_tag = await async_client.resource_tagging.zone_tags.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        )
        assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        zone_tag = await async_client.resource_tagging.zone_tags.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
            tags={
                "environment": "production",
                "team": "engineering",
            },
            if_match='"v1:RBNvo1WzZ4oRRq0W9-hkng"',
        )
        assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_tagging.zone_tags.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone_tag = await response.parse()
        assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_tagging.zone_tags.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone_tag = await response.parse()
            assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.resource_tagging.zone_tags.with_raw_response.update(
                zone_id="",
                resource_id="023e105f4ecef8ad9ca31a8372d0c353",
                resource_type="zone",
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        zone_tag = await async_client.resource_tagging.zone_tags.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            access_application_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        )
        assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        zone_tag = await async_client.resource_tagging.zone_tags.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            access_application_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
            tags={
                "environment": "production",
                "team": "engineering",
            },
            if_match='"v1:RBNvo1WzZ4oRRq0W9-hkng"',
        )
        assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_tagging.zone_tags.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            access_application_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone_tag = await response.parse()
        assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_tagging.zone_tags.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            access_application_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone_tag = await response.parse()
            assert_matches_type(Optional[ZoneTagUpdateResponse], zone_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.resource_tagging.zone_tags.with_raw_response.update(
                zone_id="",
                access_application_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                resource_id="023e105f4ecef8ad9ca31a8372d0c353",
                resource_type="zone",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        zone_tag = await async_client.resource_tagging.zone_tags.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert zone_tag is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        zone_tag = await async_client.resource_tagging.zone_tags.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            if_match='"v1:RBNvo1WzZ4oRRq0W9-hkng"',
        )
        assert zone_tag is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_tagging.zone_tags.with_raw_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone_tag = await response.parse()
        assert zone_tag is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_tagging.zone_tags.with_streaming_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone_tag = await response.parse()
            assert zone_tag is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.resource_tagging.zone_tags.with_raw_response.delete(
                zone_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        zone_tag = await async_client.resource_tagging.zone_tags.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        )
        assert_matches_type(Optional[ZoneTagGetResponse], zone_tag, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        zone_tag = await async_client.resource_tagging.zone_tags.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
            access_application_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Optional[ZoneTagGetResponse], zone_tag, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_tagging.zone_tags.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone_tag = await response.parse()
        assert_matches_type(Optional[ZoneTagGetResponse], zone_tag, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_tagging.zone_tags.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_id="023e105f4ecef8ad9ca31a8372d0c353",
            resource_type="zone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone_tag = await response.parse()
            assert_matches_type(Optional[ZoneTagGetResponse], zone_tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.resource_tagging.zone_tags.with_raw_response.get(
                zone_id="",
                resource_id="023e105f4ecef8ad9ca31a8372d0c353",
                resource_type="zone",
            )
