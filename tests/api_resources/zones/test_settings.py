# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zones import (
    SettingGetResponse,
    SettingEditResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_edit_overload_1(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="0rtt",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_1(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="0rtt",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_1(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="0rtt",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="0rtt",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="0rtt",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_2(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="advanced_ddos",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_2(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="advanced_ddos",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_2(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="advanced_ddos",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="advanced_ddos",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="advanced_ddos",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_3(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="aegis",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_method_edit_with_all_params_overload_3(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="aegis",
            value={
                "enabled": True,
                "pool_id": "pool-id",
            },
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_3(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="aegis",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_3(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="aegis",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="aegis",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="aegis",
            )

    @parametrize
    def test_method_edit_overload_4(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="always_online",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_4(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="always_online",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_4(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="always_online",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="always_online",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="always_online",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_5(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="always_use_https",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_5(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="always_use_https",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_5(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="always_use_https",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="always_use_https",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="always_use_https",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_6(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="automatic_https_rewrites",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_6(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="automatic_https_rewrites",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_6(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="automatic_https_rewrites",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="automatic_https_rewrites",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="automatic_https_rewrites",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_7(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="brotli",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_7(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="brotli",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_7(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="brotli",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="brotli",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="brotli",
                value="off",
            )

    @parametrize
    def test_method_edit_overload_8(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="browser_cache_ttl",
            value=0,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_8(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="browser_cache_ttl",
            value=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_8(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="browser_cache_ttl",
            value=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="browser_cache_ttl",
                value=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="browser_cache_ttl",
                value=0,
            )

    @parametrize
    def test_method_edit_overload_9(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="browser_check",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_9(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="browser_check",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_9(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="browser_check",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_9(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="browser_check",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="browser_check",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_10(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="cache_level",
            value="aggressive",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_10(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="cache_level",
            value="aggressive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_10(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="cache_level",
            value="aggressive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_10(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="cache_level",
                value="aggressive",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="cache_level",
                value="aggressive",
            )

    @parametrize
    def test_method_edit_overload_11(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="challenge_ttl",
            value=300,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_11(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="challenge_ttl",
            value=300,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_11(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="challenge_ttl",
            value=300,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_11(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="challenge_ttl",
                value=300,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="challenge_ttl",
                value=300,
            )

    @parametrize
    def test_method_edit_overload_12(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ciphers",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_12(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ciphers",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_12(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ciphers",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_12(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="ciphers",
                value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="ciphers",
                value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
            )

    @parametrize
    def test_method_edit_overload_13(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="cname_flattening",
            value="flatten_at_root",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_13(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="cname_flattening",
            value="flatten_at_root",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_13(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="cname_flattening",
            value="flatten_at_root",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_13(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="cname_flattening",
                value="flatten_at_root",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="cname_flattening",
                value="flatten_at_root",
            )

    @parametrize
    def test_method_edit_overload_14(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="development_mode",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_14(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="development_mode",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_14(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="development_mode",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_14(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="development_mode",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="development_mode",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_15(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="early_hints",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_15(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="early_hints",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_15(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="early_hints",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_15(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="early_hints",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="early_hints",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_16(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="edge_cache_ttl",
            value=30,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_16(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="edge_cache_ttl",
            value=30,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_16(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="edge_cache_ttl",
            value=30,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_16(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="edge_cache_ttl",
                value=30,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="edge_cache_ttl",
                value=30,
            )

    @parametrize
    def test_method_edit_overload_17(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="email_obfuscation",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_17(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="email_obfuscation",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_17(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="email_obfuscation",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_17(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="email_obfuscation",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="email_obfuscation",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_18(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="h2_prioritization",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_18(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="h2_prioritization",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_18(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="h2_prioritization",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_18(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="h2_prioritization",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="h2_prioritization",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_19(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="hotlink_protection",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_19(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="hotlink_protection",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_19(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="hotlink_protection",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_19(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="hotlink_protection",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="hotlink_protection",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_20(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="http2",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_20(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="http2",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_20(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="http2",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_20(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="http2",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="http2",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_21(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="http3",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_21(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="http3",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_21(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="http3",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_21(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="http3",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="http3",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_22(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="image_resizing",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_22(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="image_resizing",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_22(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="image_resizing",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_22(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="image_resizing",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="image_resizing",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_23(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ip_geolocation",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_23(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ip_geolocation",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_23(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ip_geolocation",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_23(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="ip_geolocation",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="ip_geolocation",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_24(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ipv6",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_24(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ipv6",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_24(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ipv6",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_24(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="ipv6",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="ipv6",
                value="off",
            )

    @parametrize
    def test_method_edit_overload_25(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="max_upload",
            value=100,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_25(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="max_upload",
            value=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_25(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="max_upload",
            value=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_25(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="max_upload",
                value=100,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="max_upload",
                value=100,
            )

    @parametrize
    def test_method_edit_overload_26(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="min_tls_version",
            value="1.0",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_26(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="min_tls_version",
            value="1.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_26(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="min_tls_version",
            value="1.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_26(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="min_tls_version",
                value="1.0",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="min_tls_version",
                value="1.0",
            )

    @parametrize
    def test_method_edit_overload_27(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="mirage",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_27(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="mirage",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_27(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="mirage",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_27(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="mirage",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="mirage",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_28(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="nel",
            value={},
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_method_edit_with_all_params_overload_28(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="nel",
            value={"enabled": False},
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_28(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="nel",
            value={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_28(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="nel",
            value={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_28(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="nel",
                value={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="nel",
                value={},
            )

    @parametrize
    def test_method_edit_overload_29(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="opportunistic_encryption",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_29(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="opportunistic_encryption",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_29(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="opportunistic_encryption",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_29(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="opportunistic_encryption",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="opportunistic_encryption",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_30(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="opportunistic_onion",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_30(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="opportunistic_onion",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_30(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="opportunistic_onion",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_30(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="opportunistic_onion",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="opportunistic_onion",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_31(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="orange_to_orange",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_31(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="orange_to_orange",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_31(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="orange_to_orange",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_31(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="orange_to_orange",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="orange_to_orange",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_32(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_error_page_pass_thru",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_32(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_error_page_pass_thru",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_32(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_error_page_pass_thru",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_32(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="origin_error_page_pass_thru",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="origin_error_page_pass_thru",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_33(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_h2_max_streams",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_method_edit_with_all_params_overload_33(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_h2_max_streams",
            value=50,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_33(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_h2_max_streams",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_33(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_h2_max_streams",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_33(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="origin_h2_max_streams",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="origin_h2_max_streams",
            )

    @parametrize
    def test_method_edit_overload_34(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_max_http_version",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_method_edit_with_all_params_overload_34(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_max_http_version",
            value="2",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_34(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_max_http_version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_34(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_max_http_version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_34(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="origin_max_http_version",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="origin_max_http_version",
            )

    @parametrize
    def test_method_edit_overload_35(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="polish",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_35(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="polish",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_35(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="polish",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_35(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="polish",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="polish",
                value="off",
            )

    @parametrize
    def test_method_edit_overload_36(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="prefetch_preload",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_36(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="prefetch_preload",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_36(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="prefetch_preload",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_36(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="prefetch_preload",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="prefetch_preload",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_37(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="privacy_pass",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_37(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="privacy_pass",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_37(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="privacy_pass",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_37(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="privacy_pass",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="privacy_pass",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_38(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="proxy_read_timeout",
            value=0,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_38(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="proxy_read_timeout",
            value=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_38(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="proxy_read_timeout",
            value=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_38(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="proxy_read_timeout",
                value=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="proxy_read_timeout",
                value=0,
            )

    @parametrize
    def test_method_edit_overload_39(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="pseudo_ipv4",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_39(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="pseudo_ipv4",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_39(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="pseudo_ipv4",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_39(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="pseudo_ipv4",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="pseudo_ipv4",
                value="off",
            )

    @parametrize
    def test_method_edit_overload_40(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="replace_insecure_js",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_40(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="replace_insecure_js",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_40(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="replace_insecure_js",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_40(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="replace_insecure_js",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="replace_insecure_js",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_41(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="response_buffering",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_41(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="response_buffering",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_41(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="response_buffering",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_41(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="response_buffering",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="response_buffering",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_42(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="rocket_loader",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_42(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="rocket_loader",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_42(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="rocket_loader",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_42(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="rocket_loader",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="rocket_loader",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_43(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="automatic_platform_optimization",
            value={
                "cache_by_device_type": False,
                "cf": True,
                "enabled": True,
                "hostnames": ["www.example.com", "example.com", "shop.example.com"],
                "wordpress": True,
                "wp_plugin": True,
            },
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_43(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="automatic_platform_optimization",
            value={
                "cache_by_device_type": False,
                "cf": True,
                "enabled": True,
                "hostnames": ["www.example.com", "example.com", "shop.example.com"],
                "wordpress": True,
                "wp_plugin": True,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_43(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="automatic_platform_optimization",
            value={
                "cache_by_device_type": False,
                "cf": True,
                "enabled": True,
                "hostnames": ["www.example.com", "example.com", "shop.example.com"],
                "wordpress": True,
                "wp_plugin": True,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_43(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="automatic_platform_optimization",
                value={
                    "cache_by_device_type": False,
                    "cf": True,
                    "enabled": True,
                    "hostnames": ["www.example.com", "example.com", "shop.example.com"],
                    "wordpress": True,
                    "wp_plugin": True,
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="automatic_platform_optimization",
                value={
                    "cache_by_device_type": False,
                    "cf": True,
                    "enabled": True,
                    "hostnames": ["www.example.com", "example.com", "shop.example.com"],
                    "wordpress": True,
                    "wp_plugin": True,
                },
            )

    @parametrize
    def test_method_edit_overload_44(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="security_header",
            value={},
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_method_edit_with_all_params_overload_44(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="security_header",
            value={
                "strict_transport_security": {
                    "enabled": True,
                    "include_subdomains": True,
                    "max_age": 86400,
                    "nosniff": True,
                    "preload": True,
                }
            },
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_44(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="security_header",
            value={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_44(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="security_header",
            value={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_44(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="security_header",
                value={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="security_header",
                value={},
            )

    @parametrize
    def test_method_edit_overload_45(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="security_level",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_45(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="security_level",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_45(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="security_level",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_45(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="security_level",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="security_level",
                value="off",
            )

    @parametrize
    def test_method_edit_overload_46(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="server_side_exclude",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_46(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="server_side_exclude",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_46(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="server_side_exclude",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_46(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="server_side_exclude",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="server_side_exclude",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_47(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="sha1_support",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_47(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="sha1_support",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_47(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="sha1_support",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_47(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="sha1_support",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="sha1_support",
                value="off",
            )

    @parametrize
    def test_method_edit_overload_48(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="sort_query_string_for_cache",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_48(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="sort_query_string_for_cache",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_48(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="sort_query_string_for_cache",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_48(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="sort_query_string_for_cache",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="sort_query_string_for_cache",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_49(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ssl",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_49(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ssl",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_49(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ssl",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_49(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="ssl",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="ssl",
                value="off",
            )

    @parametrize
    def test_method_edit_overload_50(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_method_edit_with_all_params_overload_50(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ssl_recommender",
            enabled=True,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_50(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_50(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_50(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit_overload_51(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_1_2_only",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_51(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_1_2_only",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_51(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_1_2_only",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_51(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="tls_1_2_only",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="tls_1_2_only",
                value="off",
            )

    @parametrize
    def test_method_edit_overload_52(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_1_3",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_52(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_1_3",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_52(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_1_3",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_52(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="tls_1_3",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="tls_1_3",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_53(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_client_auth",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_53(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_client_auth",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_53(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_client_auth",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_53(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="tls_client_auth",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="tls_client_auth",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_54(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="true_client_ip_header",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_54(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="true_client_ip_header",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_54(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="true_client_ip_header",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_54(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="true_client_ip_header",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="true_client_ip_header",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_55(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="waf",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_55(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="waf",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_55(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="waf",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_55(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="waf",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="waf",
                value="on",
            )

    @parametrize
    def test_method_edit_overload_56(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="webp",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_56(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="webp",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_56(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="webp",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_56(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="webp",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="webp",
                value="off",
            )

    @parametrize
    def test_method_edit_overload_57(self, client: Cloudflare) -> None:
        setting = client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="websockets",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_57(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="websockets",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_57(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="websockets",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_overload_57(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="websockets",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="websockets",
                value="off",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        setting = client.zones.settings.get(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SettingGetResponse], setting, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zones.settings.with_raw_response.get(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingGetResponse], setting, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zones.settings.with_streaming_response.get(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingGetResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.with_raw_response.get(
                setting_id="always_online",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            client.zones.settings.with_raw_response.get(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="0rtt",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="0rtt",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="0rtt",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="0rtt",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="0rtt",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="advanced_ddos",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="advanced_ddos",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="advanced_ddos",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="advanced_ddos",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="advanced_ddos",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="aegis",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="aegis",
            value={
                "enabled": True,
                "pool_id": "pool-id",
            },
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="aegis",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="aegis",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="aegis",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="aegis",
            )

    @parametrize
    async def test_method_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="always_online",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="always_online",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="always_online",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="always_online",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="always_online",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_5(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="always_use_https",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="always_use_https",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="always_use_https",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="always_use_https",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="always_use_https",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_6(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="automatic_https_rewrites",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="automatic_https_rewrites",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="automatic_https_rewrites",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="automatic_https_rewrites",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="automatic_https_rewrites",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_7(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="brotli",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="brotli",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="brotli",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="brotli",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="brotli",
                value="off",
            )

    @parametrize
    async def test_method_edit_overload_8(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="browser_cache_ttl",
            value=0,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="browser_cache_ttl",
            value=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="browser_cache_ttl",
            value=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="browser_cache_ttl",
                value=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="browser_cache_ttl",
                value=0,
            )

    @parametrize
    async def test_method_edit_overload_9(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="browser_check",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="browser_check",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_9(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="browser_check",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_9(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="browser_check",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="browser_check",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_10(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="cache_level",
            value="aggressive",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="cache_level",
            value="aggressive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_10(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="cache_level",
            value="aggressive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_10(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="cache_level",
                value="aggressive",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="cache_level",
                value="aggressive",
            )

    @parametrize
    async def test_method_edit_overload_11(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="challenge_ttl",
            value=300,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="challenge_ttl",
            value=300,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_11(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="challenge_ttl",
            value=300,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_11(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="challenge_ttl",
                value=300,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="challenge_ttl",
                value=300,
            )

    @parametrize
    async def test_method_edit_overload_12(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ciphers",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_12(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ciphers",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_12(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ciphers",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_12(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="ciphers",
                value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="ciphers",
                value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
            )

    @parametrize
    async def test_method_edit_overload_13(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="cname_flattening",
            value="flatten_at_root",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_13(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="cname_flattening",
            value="flatten_at_root",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_13(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="cname_flattening",
            value="flatten_at_root",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_13(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="cname_flattening",
                value="flatten_at_root",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="cname_flattening",
                value="flatten_at_root",
            )

    @parametrize
    async def test_method_edit_overload_14(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="development_mode",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_14(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="development_mode",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_14(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="development_mode",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_14(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="development_mode",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="development_mode",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_15(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="early_hints",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_15(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="early_hints",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_15(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="early_hints",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_15(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="early_hints",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="early_hints",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_16(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="edge_cache_ttl",
            value=30,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_16(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="edge_cache_ttl",
            value=30,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_16(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="edge_cache_ttl",
            value=30,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_16(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="edge_cache_ttl",
                value=30,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="edge_cache_ttl",
                value=30,
            )

    @parametrize
    async def test_method_edit_overload_17(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="email_obfuscation",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_17(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="email_obfuscation",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_17(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="email_obfuscation",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_17(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="email_obfuscation",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="email_obfuscation",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_18(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="h2_prioritization",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_18(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="h2_prioritization",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_18(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="h2_prioritization",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_18(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="h2_prioritization",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="h2_prioritization",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_19(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="hotlink_protection",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_19(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="hotlink_protection",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_19(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="hotlink_protection",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_19(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="hotlink_protection",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="hotlink_protection",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_20(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="http2",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_20(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="http2",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_20(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="http2",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_20(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="http2",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="http2",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_21(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="http3",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_21(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="http3",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_21(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="http3",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_21(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="http3",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="http3",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_22(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="image_resizing",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_22(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="image_resizing",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_22(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="image_resizing",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_22(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="image_resizing",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="image_resizing",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_23(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ip_geolocation",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_23(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ip_geolocation",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_23(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ip_geolocation",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_23(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="ip_geolocation",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="ip_geolocation",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_24(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ipv6",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_24(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ipv6",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_24(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ipv6",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_24(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="ipv6",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="ipv6",
                value="off",
            )

    @parametrize
    async def test_method_edit_overload_25(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="max_upload",
            value=100,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_25(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="max_upload",
            value=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_25(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="max_upload",
            value=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_25(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="max_upload",
                value=100,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="max_upload",
                value=100,
            )

    @parametrize
    async def test_method_edit_overload_26(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="min_tls_version",
            value="1.0",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_26(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="min_tls_version",
            value="1.0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_26(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="min_tls_version",
            value="1.0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_26(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="min_tls_version",
                value="1.0",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="min_tls_version",
                value="1.0",
            )

    @parametrize
    async def test_method_edit_overload_27(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="mirage",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_27(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="mirage",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_27(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="mirage",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_27(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="mirage",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="mirage",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_28(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="nel",
            value={},
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params_overload_28(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="nel",
            value={"enabled": False},
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_28(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="nel",
            value={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_28(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="nel",
            value={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_28(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="nel",
                value={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="nel",
                value={},
            )

    @parametrize
    async def test_method_edit_overload_29(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="opportunistic_encryption",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_29(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="opportunistic_encryption",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_29(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="opportunistic_encryption",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_29(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="opportunistic_encryption",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="opportunistic_encryption",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_30(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="opportunistic_onion",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_30(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="opportunistic_onion",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_30(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="opportunistic_onion",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_30(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="opportunistic_onion",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="opportunistic_onion",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_31(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="orange_to_orange",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_31(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="orange_to_orange",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_31(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="orange_to_orange",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_31(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="orange_to_orange",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="orange_to_orange",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_32(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_error_page_pass_thru",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_32(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_error_page_pass_thru",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_32(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_error_page_pass_thru",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_32(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="origin_error_page_pass_thru",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="origin_error_page_pass_thru",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_33(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_h2_max_streams",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params_overload_33(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_h2_max_streams",
            value=50,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_33(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_h2_max_streams",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_33(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_h2_max_streams",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_33(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="origin_h2_max_streams",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="origin_h2_max_streams",
            )

    @parametrize
    async def test_method_edit_overload_34(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_max_http_version",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params_overload_34(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_max_http_version",
            value="2",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_34(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_max_http_version",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_34(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="origin_max_http_version",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_34(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="origin_max_http_version",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="origin_max_http_version",
            )

    @parametrize
    async def test_method_edit_overload_35(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="polish",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_35(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="polish",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_35(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="polish",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_35(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="polish",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="polish",
                value="off",
            )

    @parametrize
    async def test_method_edit_overload_36(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="prefetch_preload",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_36(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="prefetch_preload",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_36(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="prefetch_preload",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_36(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="prefetch_preload",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="prefetch_preload",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_37(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="privacy_pass",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_37(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="privacy_pass",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_37(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="privacy_pass",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_37(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="privacy_pass",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="privacy_pass",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_38(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="proxy_read_timeout",
            value=0,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_38(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="proxy_read_timeout",
            value=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_38(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="proxy_read_timeout",
            value=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_38(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="proxy_read_timeout",
                value=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="proxy_read_timeout",
                value=0,
            )

    @parametrize
    async def test_method_edit_overload_39(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="pseudo_ipv4",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_39(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="pseudo_ipv4",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_39(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="pseudo_ipv4",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_39(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="pseudo_ipv4",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="pseudo_ipv4",
                value="off",
            )

    @parametrize
    async def test_method_edit_overload_40(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="replace_insecure_js",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_40(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="replace_insecure_js",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_40(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="replace_insecure_js",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_40(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="replace_insecure_js",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="replace_insecure_js",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_41(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="response_buffering",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_41(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="response_buffering",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_41(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="response_buffering",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_41(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="response_buffering",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="response_buffering",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_42(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="rocket_loader",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_42(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="rocket_loader",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_42(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="rocket_loader",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_42(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="rocket_loader",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="rocket_loader",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_43(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="automatic_platform_optimization",
            value={
                "cache_by_device_type": False,
                "cf": True,
                "enabled": True,
                "hostnames": ["www.example.com", "example.com", "shop.example.com"],
                "wordpress": True,
                "wp_plugin": True,
            },
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_43(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="automatic_platform_optimization",
            value={
                "cache_by_device_type": False,
                "cf": True,
                "enabled": True,
                "hostnames": ["www.example.com", "example.com", "shop.example.com"],
                "wordpress": True,
                "wp_plugin": True,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_43(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="automatic_platform_optimization",
            value={
                "cache_by_device_type": False,
                "cf": True,
                "enabled": True,
                "hostnames": ["www.example.com", "example.com", "shop.example.com"],
                "wordpress": True,
                "wp_plugin": True,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_43(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="automatic_platform_optimization",
                value={
                    "cache_by_device_type": False,
                    "cf": True,
                    "enabled": True,
                    "hostnames": ["www.example.com", "example.com", "shop.example.com"],
                    "wordpress": True,
                    "wp_plugin": True,
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="automatic_platform_optimization",
                value={
                    "cache_by_device_type": False,
                    "cf": True,
                    "enabled": True,
                    "hostnames": ["www.example.com", "example.com", "shop.example.com"],
                    "wordpress": True,
                    "wp_plugin": True,
                },
            )

    @parametrize
    async def test_method_edit_overload_44(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="security_header",
            value={},
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params_overload_44(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="security_header",
            value={
                "strict_transport_security": {
                    "enabled": True,
                    "include_subdomains": True,
                    "max_age": 86400,
                    "nosniff": True,
                    "preload": True,
                }
            },
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_44(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="security_header",
            value={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_44(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="security_header",
            value={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_44(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="security_header",
                value={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="security_header",
                value={},
            )

    @parametrize
    async def test_method_edit_overload_45(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="security_level",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_45(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="security_level",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_45(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="security_level",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_45(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="security_level",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="security_level",
                value="off",
            )

    @parametrize
    async def test_method_edit_overload_46(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="server_side_exclude",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_46(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="server_side_exclude",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_46(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="server_side_exclude",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_46(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="server_side_exclude",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="server_side_exclude",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_47(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="sha1_support",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_47(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="sha1_support",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_47(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="sha1_support",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_47(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="sha1_support",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="sha1_support",
                value="off",
            )

    @parametrize
    async def test_method_edit_overload_48(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="sort_query_string_for_cache",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_48(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="sort_query_string_for_cache",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_48(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="sort_query_string_for_cache",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_48(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="sort_query_string_for_cache",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="sort_query_string_for_cache",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_49(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ssl",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_49(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ssl",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_49(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ssl",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_49(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="ssl",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="ssl",
                value="off",
            )

    @parametrize
    async def test_method_edit_overload_50(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params_overload_50(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="ssl_recommender",
            enabled=True,
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_50(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_50(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_50(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit_overload_51(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_1_2_only",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_51(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_1_2_only",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_51(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_1_2_only",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_51(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="tls_1_2_only",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="tls_1_2_only",
                value="off",
            )

    @parametrize
    async def test_method_edit_overload_52(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_1_3",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_52(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_1_3",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_52(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_1_3",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_52(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="tls_1_3",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="tls_1_3",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_53(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_client_auth",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_53(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_client_auth",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_53(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="tls_client_auth",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_53(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="tls_client_auth",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="tls_client_auth",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_54(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="true_client_ip_header",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_54(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="true_client_ip_header",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_54(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="true_client_ip_header",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_54(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="true_client_ip_header",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="true_client_ip_header",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_55(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="waf",
            value="on",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_55(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="waf",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_55(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="waf",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_55(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="waf",
                value="on",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="waf",
                value="on",
            )

    @parametrize
    async def test_method_edit_overload_56(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="webp",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_56(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="webp",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_56(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="webp",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_56(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="webp",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="webp",
                value="off",
            )

    @parametrize
    async def test_method_edit_overload_57(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="websockets",
            value="off",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_57(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="websockets",
            value="off",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_57(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.edit(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="websockets",
            value="off",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_overload_57(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="always_online",
                zone_id="",
                id="websockets",
                value="off",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.edit(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="websockets",
                value="off",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zones.settings.get(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SettingGetResponse], setting, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.with_raw_response.get(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingGetResponse], setting, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.with_streaming_response.get(
            setting_id="always_online",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingGetResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.with_raw_response.get(
                setting_id="always_online",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_id` but received ''"):
            await async_client.zones.settings.with_raw_response.get(
                setting_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
