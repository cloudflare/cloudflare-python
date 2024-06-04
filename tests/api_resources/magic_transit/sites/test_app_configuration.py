# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.magic_transit.sites import (
    AppConfigurationListResponse,
    AppConfigurationCreateResponse,
    AppConfigurationDeleteResponse,
    AppConfigurationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAppConfiguration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        app_configuration = client.magic_transit.sites.app_configuration.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
        )
        assert_matches_type(Optional[AppConfigurationCreateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.app_configuration.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = response.parse()
        assert_matches_type(Optional[AppConfigurationCreateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.app_configuration.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = response.parse()
            assert_matches_type(Optional[AppConfigurationCreateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.create(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        app_configuration = client.magic_transit.sites.app_configuration.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_app_id="cloudflare",
        )
        assert_matches_type(Optional[AppConfigurationCreateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.app_configuration.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_app_id="cloudflare",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = response.parse()
        assert_matches_type(Optional[AppConfigurationCreateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.app_configuration.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_app_id="cloudflare",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = response.parse()
            assert_matches_type(Optional[AppConfigurationCreateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                managed_app_id="cloudflare",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.create(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                managed_app_id="cloudflare",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        app_configuration = client.magic_transit.sites.app_configuration.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.app_configuration.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = response.parse()
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.app_configuration.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = response.parse()
            assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_path_params_update_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_config_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        app_configuration = client.magic_transit.sites.app_configuration.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.app_configuration.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = response.parse()
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.app_configuration.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = response.parse()
            assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_path_params_update_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_config_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_method_update_overload_3(self, client: Cloudflare) -> None:
        app_configuration = client.magic_transit.sites.app_configuration.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
        )
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_raw_response_update_overload_3(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.app_configuration.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = response.parse()
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_streaming_response_update_overload_3(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.app_configuration.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = response.parse()
            assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_path_params_update_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_config_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_method_update_overload_4(self, client: Cloudflare) -> None:
        app_configuration = client.magic_transit.sites.app_configuration.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_app_id="cloudflare",
        )
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_raw_response_update_overload_4(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.app_configuration.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_app_id="cloudflare",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = response.parse()
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_streaming_response_update_overload_4(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.app_configuration.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_app_id="cloudflare",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = response.parse()
            assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_path_params_update_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                managed_app_id="cloudflare",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
                managed_app_id="cloudflare",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_config_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                managed_app_id="cloudflare",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_method_update_overload_5(self, client: Cloudflare) -> None:
        app_configuration = client.magic_transit.sites.app_configuration.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
            managed_app_id="string",
        )
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_raw_response_update_overload_5(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.app_configuration.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
            managed_app_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = response.parse()
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_streaming_response_update_overload_5(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.app_configuration.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
            managed_app_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = response.parse()
            assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_path_params_update_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
                managed_app_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
                managed_app_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_config_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
                managed_app_id="string",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_method_update_overload_6(self, client: Cloudflare) -> None:
        app_configuration = client.magic_transit.sites.app_configuration.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="string",
            managed_app_id="cloudflare",
        )
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_raw_response_update_overload_6(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.app_configuration.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="string",
            managed_app_id="cloudflare",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = response.parse()
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_streaming_response_update_overload_6(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.app_configuration.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="string",
            managed_app_id="cloudflare",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = response.parse()
            assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    def test_path_params_update_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_app_id="string",
                managed_app_id="cloudflare",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
                account_app_id="string",
                managed_app_id="cloudflare",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_config_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_app_id="string",
                managed_app_id="cloudflare",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        app_configuration = client.magic_transit.sites.app_configuration.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[AppConfigurationListResponse], app_configuration, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.app_configuration.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = response.parse()
        assert_matches_type(SyncSinglePage[AppConfigurationListResponse], app_configuration, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.app_configuration.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = response.parse()
            assert_matches_type(SyncSinglePage[AppConfigurationListResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.list(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        app_configuration = client.magic_transit.sites.app_configuration.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppConfigurationDeleteResponse], app_configuration, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.app_configuration.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = response.parse()
        assert_matches_type(Optional[AppConfigurationDeleteResponse], app_configuration, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.app_configuration.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = response.parse()
            assert_matches_type(Optional[AppConfigurationDeleteResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_config_id` but received ''"):
            client.magic_transit.sites.app_configuration.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncAppConfiguration:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        app_configuration = await async_client.magic_transit.sites.app_configuration.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
        )
        assert_matches_type(Optional[AppConfigurationCreateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.app_configuration.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = await response.parse()
        assert_matches_type(Optional[AppConfigurationCreateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.app_configuration.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = await response.parse()
            assert_matches_type(Optional[AppConfigurationCreateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.create(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        app_configuration = await async_client.magic_transit.sites.app_configuration.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_app_id="cloudflare",
        )
        assert_matches_type(Optional[AppConfigurationCreateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.app_configuration.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_app_id="cloudflare",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = await response.parse()
        assert_matches_type(Optional[AppConfigurationCreateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.app_configuration.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_app_id="cloudflare",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = await response.parse()
            assert_matches_type(Optional[AppConfigurationCreateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                managed_app_id="cloudflare",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.create(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                managed_app_id="cloudflare",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        app_configuration = await async_client.magic_transit.sites.app_configuration.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = await response.parse()
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.app_configuration.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = await response.parse()
            assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_config_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        app_configuration = await async_client.magic_transit.sites.app_configuration.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = await response.parse()
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.app_configuration.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = await response.parse()
            assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_config_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        app_configuration = await async_client.magic_transit.sites.app_configuration.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
        )
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = await response.parse()
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.app_configuration.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = await response.parse()
            assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_config_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        app_configuration = await async_client.magic_transit.sites.app_configuration.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_app_id="cloudflare",
        )
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_app_id="cloudflare",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = await response.parse()
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.app_configuration.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_app_id="cloudflare",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = await response.parse()
            assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                managed_app_id="cloudflare",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
                managed_app_id="cloudflare",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_config_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                managed_app_id="cloudflare",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        app_configuration = await async_client.magic_transit.sites.app_configuration.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
            managed_app_id="string",
        )
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
            managed_app_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = await response.parse()
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.app_configuration.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="ac60d3d0435248289d446cedd870bcf4",
            managed_app_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = await response.parse()
            assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_path_params_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
                managed_app_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
                managed_app_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_config_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_app_id="ac60d3d0435248289d446cedd870bcf4",
                managed_app_id="string",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_method_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        app_configuration = await async_client.magic_transit.sites.app_configuration.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="string",
            managed_app_id="cloudflare",
        )
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_raw_response_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="string",
            managed_app_id="cloudflare",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = await response.parse()
        assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_streaming_response_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.app_configuration.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_app_id="string",
            managed_app_id="cloudflare",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = await response.parse()
            assert_matches_type(Optional[AppConfigurationUpdateResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9360388260/job/25765690361?pr=482#step:5:7212"
    )
    @parametrize
    async def test_path_params_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_app_id="string",
                managed_app_id="cloudflare",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
                account_app_id="string",
                managed_app_id="cloudflare",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_config_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_app_id="string",
                managed_app_id="cloudflare",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        app_configuration = await async_client.magic_transit.sites.app_configuration.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[AppConfigurationListResponse], app_configuration, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.app_configuration.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = await response.parse()
        assert_matches_type(AsyncSinglePage[AppConfigurationListResponse], app_configuration, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.app_configuration.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = await response.parse()
            assert_matches_type(AsyncSinglePage[AppConfigurationListResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.list(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        app_configuration = await async_client.magic_transit.sites.app_configuration.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppConfigurationDeleteResponse], app_configuration, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.app_configuration.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_configuration = await response.parse()
        assert_matches_type(Optional[AppConfigurationDeleteResponse], app_configuration, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.app_configuration.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_configuration = await response.parse()
            assert_matches_type(Optional[AppConfigurationDeleteResponse], app_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_config_id` but received ''"):
            await async_client.magic_transit.sites.app_configuration.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
