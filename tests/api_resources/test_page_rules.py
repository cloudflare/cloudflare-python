# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.page_rules import (
    PageRule,
    PageRuleListResponse,
    PageRuleDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPageRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        page_rule = client.page_rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}],
            targets=[{}],
        )
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        page_rule = client.page_rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "id": "browser_check",
                    "value": "on",
                }
            ],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
            priority=0,
            status="active",
        )
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.page_rules.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}],
            targets=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_rule = response.parse()
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.page_rules.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}],
            targets=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_rule = response.parse()
            assert_matches_type(Optional[PageRule], page_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.page_rules.with_raw_response.create(
                zone_id="",
                actions=[{}],
                targets=[{}],
            )

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        page_rule = client.page_rules.update(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}],
            targets=[{}],
        )
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        page_rule = client.page_rules.update(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "id": "browser_check",
                    "value": "on",
                }
            ],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
            priority=0,
            status="active",
        )
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.page_rules.with_raw_response.update(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}],
            targets=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_rule = response.parse()
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.page_rules.with_streaming_response.update(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}],
            targets=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_rule = response.parse()
            assert_matches_type(Optional[PageRule], page_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.page_rules.with_raw_response.update(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                actions=[{}],
                targets=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
            client.page_rules.with_raw_response.update(
                pagerule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}],
                targets=[{}],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        page_rule = client.page_rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PageRuleListResponse], page_rule, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        page_rule = client.page_rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            match="any",
            order="status",
            status="active",
        )
        assert_matches_type(Optional[PageRuleListResponse], page_rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.page_rules.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_rule = response.parse()
        assert_matches_type(Optional[PageRuleListResponse], page_rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.page_rules.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_rule = response.parse()
            assert_matches_type(Optional[PageRuleListResponse], page_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.page_rules.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        page_rule = client.page_rules.delete(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PageRuleDeleteResponse], page_rule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.page_rules.with_raw_response.delete(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_rule = response.parse()
        assert_matches_type(Optional[PageRuleDeleteResponse], page_rule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.page_rules.with_streaming_response.delete(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_rule = response.parse()
            assert_matches_type(Optional[PageRuleDeleteResponse], page_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.page_rules.with_raw_response.delete(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
            client.page_rules.with_raw_response.delete(
                pagerule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        page_rule = client.page_rules.edit(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        page_rule = client.page_rules.edit(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "id": "browser_check",
                    "value": "on",
                }
            ],
            priority=0,
            status="active",
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
        )
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.page_rules.with_raw_response.edit(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_rule = response.parse()
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.page_rules.with_streaming_response.edit(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_rule = response.parse()
            assert_matches_type(Optional[PageRule], page_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.page_rules.with_raw_response.edit(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
            client.page_rules.with_raw_response.edit(
                pagerule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        page_rule = client.page_rules.get(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.page_rules.with_raw_response.get(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_rule = response.parse()
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.page_rules.with_streaming_response.get(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_rule = response.parse()
            assert_matches_type(Optional[PageRule], page_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.page_rules.with_raw_response.get(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
            client.page_rules.with_raw_response.get(
                pagerule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPageRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        page_rule = await async_client.page_rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}],
            targets=[{}],
        )
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        page_rule = await async_client.page_rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "id": "browser_check",
                    "value": "on",
                }
            ],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
            priority=0,
            status="active",
        )
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.page_rules.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}],
            targets=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_rule = await response.parse()
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.page_rules.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}],
            targets=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_rule = await response.parse()
            assert_matches_type(Optional[PageRule], page_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.page_rules.with_raw_response.create(
                zone_id="",
                actions=[{}],
                targets=[{}],
            )

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        page_rule = await async_client.page_rules.update(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}],
            targets=[{}],
        )
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        page_rule = await async_client.page_rules.update(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "id": "browser_check",
                    "value": "on",
                }
            ],
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
            priority=0,
            status="active",
        )
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.page_rules.with_raw_response.update(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}],
            targets=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_rule = await response.parse()
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.page_rules.with_streaming_response.update(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{}],
            targets=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_rule = await response.parse()
            assert_matches_type(Optional[PageRule], page_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="generated params are incorrect")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.page_rules.with_raw_response.update(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                actions=[{}],
                targets=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
            await async_client.page_rules.with_raw_response.update(
                pagerule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{}],
                targets=[{}],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        page_rule = await async_client.page_rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PageRuleListResponse], page_rule, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        page_rule = await async_client.page_rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            match="any",
            order="status",
            status="active",
        )
        assert_matches_type(Optional[PageRuleListResponse], page_rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.page_rules.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_rule = await response.parse()
        assert_matches_type(Optional[PageRuleListResponse], page_rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.page_rules.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_rule = await response.parse()
            assert_matches_type(Optional[PageRuleListResponse], page_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.page_rules.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        page_rule = await async_client.page_rules.delete(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PageRuleDeleteResponse], page_rule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.page_rules.with_raw_response.delete(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_rule = await response.parse()
        assert_matches_type(Optional[PageRuleDeleteResponse], page_rule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.page_rules.with_streaming_response.delete(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_rule = await response.parse()
            assert_matches_type(Optional[PageRuleDeleteResponse], page_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.page_rules.with_raw_response.delete(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
            await async_client.page_rules.with_raw_response.delete(
                pagerule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        page_rule = await async_client.page_rules.edit(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        page_rule = await async_client.page_rules.edit(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "id": "browser_check",
                    "value": "on",
                }
            ],
            priority=0,
            status="active",
            targets=[
                {
                    "constraint": {
                        "operator": "matches",
                        "value": "*example.com/images/*",
                    },
                    "target": "url",
                }
            ],
        )
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.page_rules.with_raw_response.edit(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_rule = await response.parse()
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.page_rules.with_streaming_response.edit(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_rule = await response.parse()
            assert_matches_type(Optional[PageRule], page_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.page_rules.with_raw_response.edit(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
            await async_client.page_rules.with_raw_response.edit(
                pagerule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        page_rule = await async_client.page_rules.get(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.page_rules.with_raw_response.get(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page_rule = await response.parse()
        assert_matches_type(Optional[PageRule], page_rule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.page_rules.with_streaming_response.get(
            pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page_rule = await response.parse()
            assert_matches_type(Optional[PageRule], page_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.page_rules.with_raw_response.get(
                pagerule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pagerule_id` but received ''"):
            await async_client.page_rules.with_raw_response.get(
                pagerule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
