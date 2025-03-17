# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.waiting_rooms import (
    WaitingRoom,
    WaitingRoomDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWaitingRooms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        waiting_room = client.waiting_rooms.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        )
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        waiting_room = client.waiting_rooms.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
            additional_routes=[
                {
                    "host": "shop2.example.com",
                    "path": "/shop2/checkout",
                }
            ],
            cookie_attributes={
                "samesite": "auto",
                "secure": "auto",
            },
            cookie_suffix="abcd",
            custom_page_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Queue all enabled {{/waitTimeKnown}}",
            default_template_language="en-US",
            description="Production - DO NOT MODIFY",
            disable_session_renewal=False,
            enabled_origin_commands=["revoke"],
            json_response_enabled=False,
            path="/shop/checkout",
            queue_all=True,
            queueing_method="fifo",
            queueing_status_code=200,
            session_duration=1,
            suspended=True,
            turnstile_action="log",
            turnstile_mode="off",
        )
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waiting_room = response.parse()
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.waiting_rooms.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waiting_room = response.parse()
            assert_matches_type(WaitingRoom, waiting_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.with_raw_response.create(
                zone_id="",
                host="shop.example.com",
                name="production_webinar",
                new_users_per_minute=200,
                total_active_users=200,
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        waiting_room = client.waiting_rooms.update(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        )
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        waiting_room = client.waiting_rooms.update(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
            additional_routes=[
                {
                    "host": "shop2.example.com",
                    "path": "/shop2/checkout",
                }
            ],
            cookie_attributes={
                "samesite": "auto",
                "secure": "auto",
            },
            cookie_suffix="abcd",
            custom_page_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Queue all enabled {{/waitTimeKnown}}",
            default_template_language="en-US",
            description="Production - DO NOT MODIFY",
            disable_session_renewal=False,
            enabled_origin_commands=["revoke"],
            json_response_enabled=False,
            path="/shop/checkout",
            queue_all=True,
            queueing_method="fifo",
            queueing_status_code=200,
            session_duration=1,
            suspended=True,
            turnstile_action="log",
            turnstile_mode="off",
        )
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.with_raw_response.update(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waiting_room = response.parse()
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.waiting_rooms.with_streaming_response.update(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waiting_room = response.parse()
            assert_matches_type(WaitingRoom, waiting_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.with_raw_response.update(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
                host="shop.example.com",
                name="production_webinar",
                new_users_per_minute=200,
                total_active_users=200,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.with_raw_response.update(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                host="shop.example.com",
                name="production_webinar",
                new_users_per_minute=200,
                total_active_users=200,
            )

    @pytest.mark.skip(
        reason="TODO: investigate path combination CI failures - https://github.com/cloudflare/cloudflare-python/actions/runs/13889017239/job/38857790771?pr=2359#step:5:3197"
    )
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        waiting_room = client.waiting_rooms.list(
            account_id="account_id",
        )
        assert_matches_type(SyncV4PagePaginationArray[WaitingRoom], waiting_room, path=["response"])

    @pytest.mark.skip(
        reason="TODO: investigate path combination CI failures - https://github.com/cloudflare/cloudflare-python/actions/runs/13889017239/job/38857790771?pr=2359#step:5:3197"
    )
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        waiting_room = client.waiting_rooms.list(
            account_id="account_id",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[WaitingRoom], waiting_room, path=["response"])

    @pytest.mark.skip(
        reason="TODO: investigate path combination CI failures - https://github.com/cloudflare/cloudflare-python/actions/runs/13889017239/job/38857790771?pr=2359#step:5:3197"
    )
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waiting_room = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[WaitingRoom], waiting_room, path=["response"])

    @pytest.mark.skip(
        reason="TODO: investigate path combination CI failures - https://github.com/cloudflare/cloudflare-python/actions/runs/13889017239/job/38857790771?pr=2359#step:5:3197"
    )
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.waiting_rooms.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waiting_room = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[WaitingRoom], waiting_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="TODO: investigate path combination CI failures - https://github.com/cloudflare/cloudflare-python/actions/runs/13889017239/job/38857790771?pr=2359#step:5:3197"
    )
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.waiting_rooms.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.waiting_rooms.with_raw_response.list(
                account_id="account_id",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        waiting_room = client.waiting_rooms.delete(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WaitingRoomDeleteResponse, waiting_room, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.with_raw_response.delete(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waiting_room = response.parse()
        assert_matches_type(WaitingRoomDeleteResponse, waiting_room, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.waiting_rooms.with_streaming_response.delete(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waiting_room = response.parse()
            assert_matches_type(WaitingRoomDeleteResponse, waiting_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.with_raw_response.delete(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.with_raw_response.delete(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        waiting_room = client.waiting_rooms.edit(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        )
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        waiting_room = client.waiting_rooms.edit(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
            additional_routes=[
                {
                    "host": "shop2.example.com",
                    "path": "/shop2/checkout",
                }
            ],
            cookie_attributes={
                "samesite": "auto",
                "secure": "auto",
            },
            cookie_suffix="abcd",
            custom_page_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Queue all enabled {{/waitTimeKnown}}",
            default_template_language="en-US",
            description="Production - DO NOT MODIFY",
            disable_session_renewal=False,
            enabled_origin_commands=["revoke"],
            json_response_enabled=False,
            path="/shop/checkout",
            queue_all=True,
            queueing_method="fifo",
            queueing_status_code=200,
            session_duration=1,
            suspended=True,
            turnstile_action="log",
            turnstile_mode="off",
        )
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.with_raw_response.edit(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waiting_room = response.parse()
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.waiting_rooms.with_streaming_response.edit(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waiting_room = response.parse()
            assert_matches_type(WaitingRoom, waiting_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.with_raw_response.edit(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
                host="shop.example.com",
                name="production_webinar",
                new_users_per_minute=200,
                total_active_users=200,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.with_raw_response.edit(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                host="shop.example.com",
                name="production_webinar",
                new_users_per_minute=200,
                total_active_users=200,
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        waiting_room = client.waiting_rooms.get(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.with_raw_response.get(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waiting_room = response.parse()
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.waiting_rooms.with_streaming_response.get(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waiting_room = response.parse()
            assert_matches_type(WaitingRoom, waiting_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.with_raw_response.get(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.with_raw_response.get(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncWaitingRooms:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        waiting_room = await async_client.waiting_rooms.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        )
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        waiting_room = await async_client.waiting_rooms.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
            additional_routes=[
                {
                    "host": "shop2.example.com",
                    "path": "/shop2/checkout",
                }
            ],
            cookie_attributes={
                "samesite": "auto",
                "secure": "auto",
            },
            cookie_suffix="abcd",
            custom_page_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Queue all enabled {{/waitTimeKnown}}",
            default_template_language="en-US",
            description="Production - DO NOT MODIFY",
            disable_session_renewal=False,
            enabled_origin_commands=["revoke"],
            json_response_enabled=False,
            path="/shop/checkout",
            queue_all=True,
            queueing_method="fifo",
            queueing_status_code=200,
            session_duration=1,
            suspended=True,
            turnstile_action="log",
            turnstile_mode="off",
        )
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waiting_room = await response.parse()
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waiting_room = await response.parse()
            assert_matches_type(WaitingRoom, waiting_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.with_raw_response.create(
                zone_id="",
                host="shop.example.com",
                name="production_webinar",
                new_users_per_minute=200,
                total_active_users=200,
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        waiting_room = await async_client.waiting_rooms.update(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        )
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        waiting_room = await async_client.waiting_rooms.update(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
            additional_routes=[
                {
                    "host": "shop2.example.com",
                    "path": "/shop2/checkout",
                }
            ],
            cookie_attributes={
                "samesite": "auto",
                "secure": "auto",
            },
            cookie_suffix="abcd",
            custom_page_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Queue all enabled {{/waitTimeKnown}}",
            default_template_language="en-US",
            description="Production - DO NOT MODIFY",
            disable_session_renewal=False,
            enabled_origin_commands=["revoke"],
            json_response_enabled=False,
            path="/shop/checkout",
            queue_all=True,
            queueing_method="fifo",
            queueing_status_code=200,
            session_duration=1,
            suspended=True,
            turnstile_action="log",
            turnstile_mode="off",
        )
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.with_raw_response.update(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waiting_room = await response.parse()
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.with_streaming_response.update(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waiting_room = await response.parse()
            assert_matches_type(WaitingRoom, waiting_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.with_raw_response.update(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
                host="shop.example.com",
                name="production_webinar",
                new_users_per_minute=200,
                total_active_users=200,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.with_raw_response.update(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                host="shop.example.com",
                name="production_webinar",
                new_users_per_minute=200,
                total_active_users=200,
            )

    @pytest.mark.skip(
        reason="TODO: investigate path combination CI failures - https://github.com/cloudflare/cloudflare-python/actions/runs/13889017239/job/38857790771?pr=2359#step:5:3197"
    )
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        waiting_room = await async_client.waiting_rooms.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncV4PagePaginationArray[WaitingRoom], waiting_room, path=["response"])

    @pytest.mark.skip(
        reason="TODO: investigate path combination CI failures - https://github.com/cloudflare/cloudflare-python/actions/runs/13889017239/job/38857790771?pr=2359#step:5:3197"
    )
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        waiting_room = await async_client.waiting_rooms.list(
            account_id="account_id",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[WaitingRoom], waiting_room, path=["response"])

    @pytest.mark.skip(
        reason="TODO: investigate path combination CI failures - https://github.com/cloudflare/cloudflare-python/actions/runs/13889017239/job/38857790771?pr=2359#step:5:3197"
    )
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waiting_room = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[WaitingRoom], waiting_room, path=["response"])

    @pytest.mark.skip(
        reason="TODO: investigate path combination CI failures - https://github.com/cloudflare/cloudflare-python/actions/runs/13889017239/job/38857790771?pr=2359#step:5:3197"
    )
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waiting_room = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[WaitingRoom], waiting_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="TODO: investigate path combination CI failures - https://github.com/cloudflare/cloudflare-python/actions/runs/13889017239/job/38857790771?pr=2359#step:5:3197"
    )
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.waiting_rooms.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.waiting_rooms.with_raw_response.list(
                account_id="account_id",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        waiting_room = await async_client.waiting_rooms.delete(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WaitingRoomDeleteResponse, waiting_room, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.with_raw_response.delete(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waiting_room = await response.parse()
        assert_matches_type(WaitingRoomDeleteResponse, waiting_room, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.with_streaming_response.delete(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waiting_room = await response.parse()
            assert_matches_type(WaitingRoomDeleteResponse, waiting_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.with_raw_response.delete(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.with_raw_response.delete(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        waiting_room = await async_client.waiting_rooms.edit(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        )
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        waiting_room = await async_client.waiting_rooms.edit(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
            additional_routes=[
                {
                    "host": "shop2.example.com",
                    "path": "/shop2/checkout",
                }
            ],
            cookie_attributes={
                "samesite": "auto",
                "secure": "auto",
            },
            cookie_suffix="abcd",
            custom_page_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Queue all enabled {{/waitTimeKnown}}",
            default_template_language="en-US",
            description="Production - DO NOT MODIFY",
            disable_session_renewal=False,
            enabled_origin_commands=["revoke"],
            json_response_enabled=False,
            path="/shop/checkout",
            queue_all=True,
            queueing_method="fifo",
            queueing_status_code=200,
            session_duration=1,
            suspended=True,
            turnstile_action="log",
            turnstile_mode="off",
        )
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.with_raw_response.edit(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waiting_room = await response.parse()
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.with_streaming_response.edit(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="shop.example.com",
            name="production_webinar",
            new_users_per_minute=200,
            total_active_users=200,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waiting_room = await response.parse()
            assert_matches_type(WaitingRoom, waiting_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.with_raw_response.edit(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
                host="shop.example.com",
                name="production_webinar",
                new_users_per_minute=200,
                total_active_users=200,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.with_raw_response.edit(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                host="shop.example.com",
                name="production_webinar",
                new_users_per_minute=200,
                total_active_users=200,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        waiting_room = await async_client.waiting_rooms.get(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.with_raw_response.get(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        waiting_room = await response.parse()
        assert_matches_type(WaitingRoom, waiting_room, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.with_streaming_response.get(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            waiting_room = await response.parse()
            assert_matches_type(WaitingRoom, waiting_room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.with_raw_response.get(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.with_raw_response.get(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
