# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.realtime_kit import (
    PresetGetResponse,
    PresetCreateResponse,
    PresetDeleteResponse,
    PresetUpdateResponse,
    PresetGetPresetByIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPresets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        preset = client.realtime_kit.presets.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "max_screenshare_count": 0,
                "max_video_streams": {
                    "desktop": 0,
                    "mobile": 0,
                },
                "media": {
                    "screenshare": {
                        "frame_rate": 0,
                        "quality": "hd",
                    },
                    "video": {
                        "frame_rate": 30,
                        "quality": "hd",
                    },
                },
                "view_type": "GROUP_CALL",
            },
            name="name",
            ui={
                "design_tokens": {
                    "border_radius": "rounded",
                    "border_width": "thin",
                    "colors": {
                        "background": {
                            "_600": "600",
                            "_700": "700",
                            "_800": "800",
                            "_900": "900",
                            "_1000": "1000",
                        },
                        "brand": {
                            "_300": "300",
                            "_400": "400",
                            "_500": "500",
                            "_600": "600",
                            "_700": "700",
                        },
                        "danger": "danger",
                        "success": "success",
                        "text": "text",
                        "text_on_brand": "text_on_brand",
                        "video_bg": "video_bg",
                        "warning": "warning",
                    },
                    "logo": "logo",
                    "spacing_base": 0,
                    "theme": "dark",
                }
            },
        )
        assert_matches_type(PresetCreateResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        preset = client.realtime_kit.presets.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "max_screenshare_count": 0,
                "max_video_streams": {
                    "desktop": 0,
                    "mobile": 0,
                },
                "media": {
                    "screenshare": {
                        "frame_rate": 0,
                        "quality": "hd",
                    },
                    "video": {
                        "frame_rate": 30,
                        "quality": "hd",
                    },
                    "audio": {
                        "enable_high_bitrate": True,
                        "enable_stereo": True,
                    },
                },
                "view_type": "GROUP_CALL",
            },
            name="name",
            ui={
                "design_tokens": {
                    "border_radius": "rounded",
                    "border_width": "thin",
                    "colors": {
                        "background": {
                            "_600": "600",
                            "_700": "700",
                            "_800": "800",
                            "_900": "900",
                            "_1000": "1000",
                        },
                        "brand": {
                            "_300": "300",
                            "_400": "400",
                            "_500": "500",
                            "_600": "600",
                            "_700": "700",
                        },
                        "danger": "danger",
                        "success": "success",
                        "text": "text",
                        "text_on_brand": "text_on_brand",
                        "video_bg": "video_bg",
                        "warning": "warning",
                    },
                    "logo": "logo",
                    "spacing_base": 0,
                    "theme": "dark",
                },
                "config_diff": {},
            },
            permissions={
                "accept_waiting_requests": True,
                "can_accept_production_requests": True,
                "can_change_participant_permissions": True,
                "can_edit_display_name": True,
                "can_livestream": True,
                "can_record": True,
                "can_spotlight": True,
                "chat": {
                    "private": {
                        "can_receive": True,
                        "can_send": True,
                        "files": True,
                        "text": True,
                    },
                    "public": {
                        "can_send": True,
                        "files": True,
                        "text": True,
                    },
                },
                "connected_meetings": {
                    "can_alter_connected_meetings": True,
                    "can_switch_connected_meetings": True,
                    "can_switch_to_parent_meeting": True,
                },
                "disable_participant_audio": True,
                "disable_participant_screensharing": True,
                "disable_participant_video": True,
                "hidden_participant": True,
                "kick_participant": True,
                "media": {
                    "audio": {"can_produce": "ALLOWED"},
                    "screenshare": {"can_produce": "ALLOWED"},
                    "video": {"can_produce": "ALLOWED"},
                },
                "pin_participant": True,
                "plugins": {
                    "can_close": True,
                    "can_edit_config": True,
                    "can_start": True,
                    "config": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                "polls": {
                    "can_create": True,
                    "can_view": True,
                    "can_vote": True,
                },
                "recorder_type": "RECORDER",
                "show_participant_list": True,
                "waiting_room_type": "SKIP",
                "is_recorder": True,
            },
        )
        assert_matches_type(PresetCreateResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.realtime_kit.presets.with_raw_response.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "max_screenshare_count": 0,
                "max_video_streams": {
                    "desktop": 0,
                    "mobile": 0,
                },
                "media": {
                    "screenshare": {
                        "frame_rate": 0,
                        "quality": "hd",
                    },
                    "video": {
                        "frame_rate": 30,
                        "quality": "hd",
                    },
                },
                "view_type": "GROUP_CALL",
            },
            name="name",
            ui={
                "design_tokens": {
                    "border_radius": "rounded",
                    "border_width": "thin",
                    "colors": {
                        "background": {
                            "_600": "600",
                            "_700": "700",
                            "_800": "800",
                            "_900": "900",
                            "_1000": "1000",
                        },
                        "brand": {
                            "_300": "300",
                            "_400": "400",
                            "_500": "500",
                            "_600": "600",
                            "_700": "700",
                        },
                        "danger": "danger",
                        "success": "success",
                        "text": "text",
                        "text_on_brand": "text_on_brand",
                        "video_bg": "video_bg",
                        "warning": "warning",
                    },
                    "logo": "logo",
                    "spacing_base": 0,
                    "theme": "dark",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preset = response.parse()
        assert_matches_type(PresetCreateResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.realtime_kit.presets.with_streaming_response.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "max_screenshare_count": 0,
                "max_video_streams": {
                    "desktop": 0,
                    "mobile": 0,
                },
                "media": {
                    "screenshare": {
                        "frame_rate": 0,
                        "quality": "hd",
                    },
                    "video": {
                        "frame_rate": 30,
                        "quality": "hd",
                    },
                },
                "view_type": "GROUP_CALL",
            },
            name="name",
            ui={
                "design_tokens": {
                    "border_radius": "rounded",
                    "border_width": "thin",
                    "colors": {
                        "background": {
                            "_600": "600",
                            "_700": "700",
                            "_800": "800",
                            "_900": "900",
                            "_1000": "1000",
                        },
                        "brand": {
                            "_300": "300",
                            "_400": "400",
                            "_500": "500",
                            "_600": "600",
                            "_700": "700",
                        },
                        "danger": "danger",
                        "success": "success",
                        "text": "text",
                        "text_on_brand": "text_on_brand",
                        "video_bg": "video_bg",
                        "warning": "warning",
                    },
                    "logo": "logo",
                    "spacing_base": 0,
                    "theme": "dark",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preset = response.parse()
            assert_matches_type(PresetCreateResponse, preset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.presets.with_raw_response.create(
                app_id="app_id",
                account_id="",
                config={
                    "max_screenshare_count": 0,
                    "max_video_streams": {
                        "desktop": 0,
                        "mobile": 0,
                    },
                    "media": {
                        "screenshare": {
                            "frame_rate": 0,
                            "quality": "hd",
                        },
                        "video": {
                            "frame_rate": 30,
                            "quality": "hd",
                        },
                    },
                    "view_type": "GROUP_CALL",
                },
                name="name",
                ui={
                    "design_tokens": {
                        "border_radius": "rounded",
                        "border_width": "thin",
                        "colors": {
                            "background": {
                                "_600": "600",
                                "_700": "700",
                                "_800": "800",
                                "_900": "900",
                                "_1000": "1000",
                            },
                            "brand": {
                                "_300": "300",
                                "_400": "400",
                                "_500": "500",
                                "_600": "600",
                                "_700": "700",
                            },
                            "danger": "danger",
                            "success": "success",
                            "text": "text",
                            "text_on_brand": "text_on_brand",
                            "video_bg": "video_bg",
                            "warning": "warning",
                        },
                        "logo": "logo",
                        "spacing_base": 0,
                        "theme": "dark",
                    }
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.presets.with_raw_response.create(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                config={
                    "max_screenshare_count": 0,
                    "max_video_streams": {
                        "desktop": 0,
                        "mobile": 0,
                    },
                    "media": {
                        "screenshare": {
                            "frame_rate": 0,
                            "quality": "hd",
                        },
                        "video": {
                            "frame_rate": 30,
                            "quality": "hd",
                        },
                    },
                    "view_type": "GROUP_CALL",
                },
                name="name",
                ui={
                    "design_tokens": {
                        "border_radius": "rounded",
                        "border_width": "thin",
                        "colors": {
                            "background": {
                                "_600": "600",
                                "_700": "700",
                                "_800": "800",
                                "_900": "900",
                                "_1000": "1000",
                            },
                            "brand": {
                                "_300": "300",
                                "_400": "400",
                                "_500": "500",
                                "_600": "600",
                                "_700": "700",
                            },
                            "danger": "danger",
                            "success": "success",
                            "text": "text",
                            "text_on_brand": "text_on_brand",
                            "video_bg": "video_bg",
                            "warning": "warning",
                        },
                        "logo": "logo",
                        "spacing_base": 0,
                        "theme": "dark",
                    }
                },
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        preset = client.realtime_kit.presets.update(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(PresetUpdateResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        preset = client.realtime_kit.presets.update(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            config={
                "max_screenshare_count": 0,
                "max_video_streams": {
                    "desktop": 0,
                    "mobile": 0,
                },
                "media": {
                    "screenshare": {
                        "frame_rate": 0,
                        "quality": "hd",
                    },
                    "video": {
                        "frame_rate": 30,
                        "quality": "hd",
                    },
                },
                "view_type": "GROUP_CALL",
            },
            name="name",
            permissions={
                "accept_waiting_requests": True,
                "can_accept_production_requests": True,
                "can_change_participant_permissions": True,
                "can_edit_display_name": True,
                "can_livestream": True,
                "can_record": True,
                "can_spotlight": True,
                "chat": {
                    "private": {
                        "can_receive": True,
                        "can_send": True,
                        "files": True,
                        "text": True,
                    },
                    "public": {
                        "can_send": True,
                        "files": True,
                        "text": True,
                    },
                },
                "connected_meetings": {
                    "can_alter_connected_meetings": True,
                    "can_switch_connected_meetings": True,
                    "can_switch_to_parent_meeting": True,
                },
                "disable_participant_audio": True,
                "disable_participant_screensharing": True,
                "disable_participant_video": True,
                "hidden_participant": True,
                "is_recorder": True,
                "kick_participant": True,
                "media": {
                    "audio": {"can_produce": "ALLOWED"},
                    "screenshare": {"can_produce": "ALLOWED"},
                    "video": {"can_produce": "ALLOWED"},
                },
                "pin_participant": True,
                "plugins": {
                    "can_close": True,
                    "can_edit_config": True,
                    "can_start": True,
                    "config": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                "polls": {
                    "can_create": True,
                    "can_view": True,
                    "can_vote": True,
                },
                "recorder_type": "RECORDER",
                "show_participant_list": True,
                "waiting_room_type": "SKIP",
            },
            ui={
                "config_diff": {},
                "design_tokens": {
                    "border_radius": "rounded",
                    "border_width": "thin",
                    "colors": {
                        "background": {
                            "_600": "600",
                            "_700": "700",
                            "_800": "800",
                            "_900": "900",
                            "_1000": "1000",
                        },
                        "brand": {
                            "_300": "300",
                            "_400": "400",
                            "_500": "500",
                            "_600": "600",
                            "_700": "700",
                        },
                        "danger": "danger",
                        "success": "success",
                        "text": "text",
                        "text_on_brand": "text_on_brand",
                        "video_bg": "video_bg",
                        "warning": "warning",
                    },
                    "logo": "logo",
                    "spacing_base": 0,
                    "theme": "dark",
                },
            },
        )
        assert_matches_type(PresetUpdateResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.realtime_kit.presets.with_raw_response.update(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preset = response.parse()
        assert_matches_type(PresetUpdateResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.realtime_kit.presets.with_streaming_response.update(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preset = response.parse()
            assert_matches_type(PresetUpdateResponse, preset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.presets.with_raw_response.update(
                preset_id="preset_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.presets.with_raw_response.update(
                preset_id="preset_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preset_id` but received ''"):
            client.realtime_kit.presets.with_raw_response.update(
                preset_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        preset = client.realtime_kit.presets.delete(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(PresetDeleteResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.realtime_kit.presets.with_raw_response.delete(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preset = response.parse()
        assert_matches_type(PresetDeleteResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.realtime_kit.presets.with_streaming_response.delete(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preset = response.parse()
            assert_matches_type(PresetDeleteResponse, preset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.presets.with_raw_response.delete(
                preset_id="preset_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.presets.with_raw_response.delete(
                preset_id="preset_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preset_id` but received ''"):
            client.realtime_kit.presets.with_raw_response.delete(
                preset_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        preset = client.realtime_kit.presets.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PresetGetResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        preset = client.realtime_kit.presets.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page_no=0,
            per_page=0,
        )
        assert_matches_type(PresetGetResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.realtime_kit.presets.with_raw_response.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preset = response.parse()
        assert_matches_type(PresetGetResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.realtime_kit.presets.with_streaming_response.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preset = response.parse()
            assert_matches_type(PresetGetResponse, preset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.presets.with_raw_response.get(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.presets.with_raw_response.get(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_preset_by_id(self, client: Cloudflare) -> None:
        preset = client.realtime_kit.presets.get_preset_by_id(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(PresetGetPresetByIDResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_preset_by_id(self, client: Cloudflare) -> None:
        response = client.realtime_kit.presets.with_raw_response.get_preset_by_id(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preset = response.parse()
        assert_matches_type(PresetGetPresetByIDResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_preset_by_id(self, client: Cloudflare) -> None:
        with client.realtime_kit.presets.with_streaming_response.get_preset_by_id(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preset = response.parse()
            assert_matches_type(PresetGetPresetByIDResponse, preset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_preset_by_id(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.presets.with_raw_response.get_preset_by_id(
                preset_id="preset_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.presets.with_raw_response.get_preset_by_id(
                preset_id="preset_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preset_id` but received ''"):
            client.realtime_kit.presets.with_raw_response.get_preset_by_id(
                preset_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )


class TestAsyncPresets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        preset = await async_client.realtime_kit.presets.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "max_screenshare_count": 0,
                "max_video_streams": {
                    "desktop": 0,
                    "mobile": 0,
                },
                "media": {
                    "screenshare": {
                        "frame_rate": 0,
                        "quality": "hd",
                    },
                    "video": {
                        "frame_rate": 30,
                        "quality": "hd",
                    },
                },
                "view_type": "GROUP_CALL",
            },
            name="name",
            ui={
                "design_tokens": {
                    "border_radius": "rounded",
                    "border_width": "thin",
                    "colors": {
                        "background": {
                            "_600": "600",
                            "_700": "700",
                            "_800": "800",
                            "_900": "900",
                            "_1000": "1000",
                        },
                        "brand": {
                            "_300": "300",
                            "_400": "400",
                            "_500": "500",
                            "_600": "600",
                            "_700": "700",
                        },
                        "danger": "danger",
                        "success": "success",
                        "text": "text",
                        "text_on_brand": "text_on_brand",
                        "video_bg": "video_bg",
                        "warning": "warning",
                    },
                    "logo": "logo",
                    "spacing_base": 0,
                    "theme": "dark",
                }
            },
        )
        assert_matches_type(PresetCreateResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        preset = await async_client.realtime_kit.presets.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "max_screenshare_count": 0,
                "max_video_streams": {
                    "desktop": 0,
                    "mobile": 0,
                },
                "media": {
                    "screenshare": {
                        "frame_rate": 0,
                        "quality": "hd",
                    },
                    "video": {
                        "frame_rate": 30,
                        "quality": "hd",
                    },
                    "audio": {
                        "enable_high_bitrate": True,
                        "enable_stereo": True,
                    },
                },
                "view_type": "GROUP_CALL",
            },
            name="name",
            ui={
                "design_tokens": {
                    "border_radius": "rounded",
                    "border_width": "thin",
                    "colors": {
                        "background": {
                            "_600": "600",
                            "_700": "700",
                            "_800": "800",
                            "_900": "900",
                            "_1000": "1000",
                        },
                        "brand": {
                            "_300": "300",
                            "_400": "400",
                            "_500": "500",
                            "_600": "600",
                            "_700": "700",
                        },
                        "danger": "danger",
                        "success": "success",
                        "text": "text",
                        "text_on_brand": "text_on_brand",
                        "video_bg": "video_bg",
                        "warning": "warning",
                    },
                    "logo": "logo",
                    "spacing_base": 0,
                    "theme": "dark",
                },
                "config_diff": {},
            },
            permissions={
                "accept_waiting_requests": True,
                "can_accept_production_requests": True,
                "can_change_participant_permissions": True,
                "can_edit_display_name": True,
                "can_livestream": True,
                "can_record": True,
                "can_spotlight": True,
                "chat": {
                    "private": {
                        "can_receive": True,
                        "can_send": True,
                        "files": True,
                        "text": True,
                    },
                    "public": {
                        "can_send": True,
                        "files": True,
                        "text": True,
                    },
                },
                "connected_meetings": {
                    "can_alter_connected_meetings": True,
                    "can_switch_connected_meetings": True,
                    "can_switch_to_parent_meeting": True,
                },
                "disable_participant_audio": True,
                "disable_participant_screensharing": True,
                "disable_participant_video": True,
                "hidden_participant": True,
                "kick_participant": True,
                "media": {
                    "audio": {"can_produce": "ALLOWED"},
                    "screenshare": {"can_produce": "ALLOWED"},
                    "video": {"can_produce": "ALLOWED"},
                },
                "pin_participant": True,
                "plugins": {
                    "can_close": True,
                    "can_edit_config": True,
                    "can_start": True,
                    "config": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                "polls": {
                    "can_create": True,
                    "can_view": True,
                    "can_vote": True,
                },
                "recorder_type": "RECORDER",
                "show_participant_list": True,
                "waiting_room_type": "SKIP",
                "is_recorder": True,
            },
        )
        assert_matches_type(PresetCreateResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.presets.with_raw_response.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "max_screenshare_count": 0,
                "max_video_streams": {
                    "desktop": 0,
                    "mobile": 0,
                },
                "media": {
                    "screenshare": {
                        "frame_rate": 0,
                        "quality": "hd",
                    },
                    "video": {
                        "frame_rate": 30,
                        "quality": "hd",
                    },
                },
                "view_type": "GROUP_CALL",
            },
            name="name",
            ui={
                "design_tokens": {
                    "border_radius": "rounded",
                    "border_width": "thin",
                    "colors": {
                        "background": {
                            "_600": "600",
                            "_700": "700",
                            "_800": "800",
                            "_900": "900",
                            "_1000": "1000",
                        },
                        "brand": {
                            "_300": "300",
                            "_400": "400",
                            "_500": "500",
                            "_600": "600",
                            "_700": "700",
                        },
                        "danger": "danger",
                        "success": "success",
                        "text": "text",
                        "text_on_brand": "text_on_brand",
                        "video_bg": "video_bg",
                        "warning": "warning",
                    },
                    "logo": "logo",
                    "spacing_base": 0,
                    "theme": "dark",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preset = await response.parse()
        assert_matches_type(PresetCreateResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.presets.with_streaming_response.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "max_screenshare_count": 0,
                "max_video_streams": {
                    "desktop": 0,
                    "mobile": 0,
                },
                "media": {
                    "screenshare": {
                        "frame_rate": 0,
                        "quality": "hd",
                    },
                    "video": {
                        "frame_rate": 30,
                        "quality": "hd",
                    },
                },
                "view_type": "GROUP_CALL",
            },
            name="name",
            ui={
                "design_tokens": {
                    "border_radius": "rounded",
                    "border_width": "thin",
                    "colors": {
                        "background": {
                            "_600": "600",
                            "_700": "700",
                            "_800": "800",
                            "_900": "900",
                            "_1000": "1000",
                        },
                        "brand": {
                            "_300": "300",
                            "_400": "400",
                            "_500": "500",
                            "_600": "600",
                            "_700": "700",
                        },
                        "danger": "danger",
                        "success": "success",
                        "text": "text",
                        "text_on_brand": "text_on_brand",
                        "video_bg": "video_bg",
                        "warning": "warning",
                    },
                    "logo": "logo",
                    "spacing_base": 0,
                    "theme": "dark",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preset = await response.parse()
            assert_matches_type(PresetCreateResponse, preset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.presets.with_raw_response.create(
                app_id="app_id",
                account_id="",
                config={
                    "max_screenshare_count": 0,
                    "max_video_streams": {
                        "desktop": 0,
                        "mobile": 0,
                    },
                    "media": {
                        "screenshare": {
                            "frame_rate": 0,
                            "quality": "hd",
                        },
                        "video": {
                            "frame_rate": 30,
                            "quality": "hd",
                        },
                    },
                    "view_type": "GROUP_CALL",
                },
                name="name",
                ui={
                    "design_tokens": {
                        "border_radius": "rounded",
                        "border_width": "thin",
                        "colors": {
                            "background": {
                                "_600": "600",
                                "_700": "700",
                                "_800": "800",
                                "_900": "900",
                                "_1000": "1000",
                            },
                            "brand": {
                                "_300": "300",
                                "_400": "400",
                                "_500": "500",
                                "_600": "600",
                                "_700": "700",
                            },
                            "danger": "danger",
                            "success": "success",
                            "text": "text",
                            "text_on_brand": "text_on_brand",
                            "video_bg": "video_bg",
                            "warning": "warning",
                        },
                        "logo": "logo",
                        "spacing_base": 0,
                        "theme": "dark",
                    }
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.presets.with_raw_response.create(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                config={
                    "max_screenshare_count": 0,
                    "max_video_streams": {
                        "desktop": 0,
                        "mobile": 0,
                    },
                    "media": {
                        "screenshare": {
                            "frame_rate": 0,
                            "quality": "hd",
                        },
                        "video": {
                            "frame_rate": 30,
                            "quality": "hd",
                        },
                    },
                    "view_type": "GROUP_CALL",
                },
                name="name",
                ui={
                    "design_tokens": {
                        "border_radius": "rounded",
                        "border_width": "thin",
                        "colors": {
                            "background": {
                                "_600": "600",
                                "_700": "700",
                                "_800": "800",
                                "_900": "900",
                                "_1000": "1000",
                            },
                            "brand": {
                                "_300": "300",
                                "_400": "400",
                                "_500": "500",
                                "_600": "600",
                                "_700": "700",
                            },
                            "danger": "danger",
                            "success": "success",
                            "text": "text",
                            "text_on_brand": "text_on_brand",
                            "video_bg": "video_bg",
                            "warning": "warning",
                        },
                        "logo": "logo",
                        "spacing_base": 0,
                        "theme": "dark",
                    }
                },
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        preset = await async_client.realtime_kit.presets.update(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(PresetUpdateResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        preset = await async_client.realtime_kit.presets.update(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            config={
                "max_screenshare_count": 0,
                "max_video_streams": {
                    "desktop": 0,
                    "mobile": 0,
                },
                "media": {
                    "screenshare": {
                        "frame_rate": 0,
                        "quality": "hd",
                    },
                    "video": {
                        "frame_rate": 30,
                        "quality": "hd",
                    },
                },
                "view_type": "GROUP_CALL",
            },
            name="name",
            permissions={
                "accept_waiting_requests": True,
                "can_accept_production_requests": True,
                "can_change_participant_permissions": True,
                "can_edit_display_name": True,
                "can_livestream": True,
                "can_record": True,
                "can_spotlight": True,
                "chat": {
                    "private": {
                        "can_receive": True,
                        "can_send": True,
                        "files": True,
                        "text": True,
                    },
                    "public": {
                        "can_send": True,
                        "files": True,
                        "text": True,
                    },
                },
                "connected_meetings": {
                    "can_alter_connected_meetings": True,
                    "can_switch_connected_meetings": True,
                    "can_switch_to_parent_meeting": True,
                },
                "disable_participant_audio": True,
                "disable_participant_screensharing": True,
                "disable_participant_video": True,
                "hidden_participant": True,
                "is_recorder": True,
                "kick_participant": True,
                "media": {
                    "audio": {"can_produce": "ALLOWED"},
                    "screenshare": {"can_produce": "ALLOWED"},
                    "video": {"can_produce": "ALLOWED"},
                },
                "pin_participant": True,
                "plugins": {
                    "can_close": True,
                    "can_edit_config": True,
                    "can_start": True,
                    "config": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                "polls": {
                    "can_create": True,
                    "can_view": True,
                    "can_vote": True,
                },
                "recorder_type": "RECORDER",
                "show_participant_list": True,
                "waiting_room_type": "SKIP",
            },
            ui={
                "config_diff": {},
                "design_tokens": {
                    "border_radius": "rounded",
                    "border_width": "thin",
                    "colors": {
                        "background": {
                            "_600": "600",
                            "_700": "700",
                            "_800": "800",
                            "_900": "900",
                            "_1000": "1000",
                        },
                        "brand": {
                            "_300": "300",
                            "_400": "400",
                            "_500": "500",
                            "_600": "600",
                            "_700": "700",
                        },
                        "danger": "danger",
                        "success": "success",
                        "text": "text",
                        "text_on_brand": "text_on_brand",
                        "video_bg": "video_bg",
                        "warning": "warning",
                    },
                    "logo": "logo",
                    "spacing_base": 0,
                    "theme": "dark",
                },
            },
        )
        assert_matches_type(PresetUpdateResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.presets.with_raw_response.update(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preset = await response.parse()
        assert_matches_type(PresetUpdateResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.presets.with_streaming_response.update(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preset = await response.parse()
            assert_matches_type(PresetUpdateResponse, preset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.presets.with_raw_response.update(
                preset_id="preset_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.presets.with_raw_response.update(
                preset_id="preset_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preset_id` but received ''"):
            await async_client.realtime_kit.presets.with_raw_response.update(
                preset_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        preset = await async_client.realtime_kit.presets.delete(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(PresetDeleteResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.presets.with_raw_response.delete(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preset = await response.parse()
        assert_matches_type(PresetDeleteResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.presets.with_streaming_response.delete(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preset = await response.parse()
            assert_matches_type(PresetDeleteResponse, preset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.presets.with_raw_response.delete(
                preset_id="preset_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.presets.with_raw_response.delete(
                preset_id="preset_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preset_id` but received ''"):
            await async_client.realtime_kit.presets.with_raw_response.delete(
                preset_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        preset = await async_client.realtime_kit.presets.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PresetGetResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        preset = await async_client.realtime_kit.presets.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page_no=0,
            per_page=0,
        )
        assert_matches_type(PresetGetResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.presets.with_raw_response.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preset = await response.parse()
        assert_matches_type(PresetGetResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.presets.with_streaming_response.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preset = await response.parse()
            assert_matches_type(PresetGetResponse, preset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.presets.with_raw_response.get(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.presets.with_raw_response.get(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_preset_by_id(self, async_client: AsyncCloudflare) -> None:
        preset = await async_client.realtime_kit.presets.get_preset_by_id(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(PresetGetPresetByIDResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_preset_by_id(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.presets.with_raw_response.get_preset_by_id(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preset = await response.parse()
        assert_matches_type(PresetGetPresetByIDResponse, preset, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_preset_by_id(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.presets.with_streaming_response.get_preset_by_id(
            preset_id="preset_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preset = await response.parse()
            assert_matches_type(PresetGetPresetByIDResponse, preset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_preset_by_id(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.presets.with_raw_response.get_preset_by_id(
                preset_id="preset_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.presets.with_raw_response.get_preset_by_id(
                preset_id="preset_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preset_id` but received ''"):
            await async_client.realtime_kit.presets.with_raw_response.get_preset_by_id(
                preset_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )
