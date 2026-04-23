# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "PresetUpdateParams",
    "Config",
    "ConfigMaxVideoStreams",
    "ConfigMedia",
    "ConfigMediaScreenshare",
    "ConfigMediaVideo",
    "Permissions",
    "PermissionsChat",
    "PermissionsChatPrivate",
    "PermissionsChatPublic",
    "PermissionsConnectedMeetings",
    "PermissionsMedia",
    "PermissionsMediaAudio",
    "PermissionsMediaScreenshare",
    "PermissionsMediaVideo",
    "PermissionsPlugins",
    "PermissionsPluginsConfig",
    "PermissionsPluginsConfigUnionMember1",
    "PermissionsPolls",
    "UI",
    "UIDesignTokens",
    "UIDesignTokensColors",
    "UIDesignTokensColorsBackground",
    "UIDesignTokensColorsBrand",
]


class PresetUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]
    """The app identifier tag."""

    config: Config

    name: str
    """Name of the preset"""

    permissions: Permissions

    ui: UI


class ConfigMaxVideoStreams(TypedDict, total=False):
    """Maximum number of streams that are visible on a device"""

    desktop: int
    """Maximum number of video streams visible on desktop devices"""

    mobile: int
    """Maximum number of streams visible on mobile devices"""


class ConfigMediaScreenshare(TypedDict, total=False):
    """Configuration options for participant screen shares"""

    frame_rate: int
    """Frame rate of screen share"""

    quality: Literal["hd", "vga", "qvga"]
    """Quality of screen share"""


class ConfigMediaVideo(TypedDict, total=False):
    """Configuration options for participant videos"""

    frame_rate: int
    """Frame rate of participants' video"""

    quality: Literal["hd", "vga", "qvga"]
    """Video quality of participants"""


class ConfigMedia(TypedDict, total=False):
    """Media configuration options. eg: Video quality"""

    screenshare: ConfigMediaScreenshare
    """Configuration options for participant screen shares"""

    video: ConfigMediaVideo
    """Configuration options for participant videos"""


class Config(TypedDict, total=False):
    max_screenshare_count: int
    """Maximum number of screen shares that can be active at a given time"""

    max_video_streams: ConfigMaxVideoStreams
    """Maximum number of streams that are visible on a device"""

    media: ConfigMedia
    """Media configuration options. eg: Video quality"""

    view_type: Literal["GROUP_CALL", "WEBINAR", "AUDIO_ROOM"]
    """Type of the meeting"""


class PermissionsChatPrivate(TypedDict, total=False):
    can_receive: bool

    can_send: bool

    files: bool

    text: bool


class PermissionsChatPublic(TypedDict, total=False):
    can_send: bool
    """Can send messages in general"""

    files: bool
    """Can send file messages"""

    text: bool
    """Can send text messages"""


class PermissionsChat(TypedDict, total=False):
    """Chat permissions"""

    private: PermissionsChatPrivate

    public: PermissionsChatPublic


class PermissionsConnectedMeetings(TypedDict, total=False):
    can_alter_connected_meetings: bool

    can_switch_connected_meetings: bool

    can_switch_to_parent_meeting: bool


class PermissionsMediaAudio(TypedDict, total=False):
    """Audio permissions"""

    can_produce: Literal["ALLOWED", "NOT_ALLOWED", "CAN_REQUEST"]
    """Can produce audio"""


class PermissionsMediaScreenshare(TypedDict, total=False):
    """Screenshare permissions"""

    can_produce: Literal["ALLOWED", "NOT_ALLOWED", "CAN_REQUEST"]
    """Can produce screen share video"""


class PermissionsMediaVideo(TypedDict, total=False):
    """Video permissions"""

    can_produce: Literal["ALLOWED", "NOT_ALLOWED", "CAN_REQUEST"]
    """Can produce video"""


class PermissionsMedia(TypedDict, total=False):
    """Media permissions"""

    audio: PermissionsMediaAudio
    """Audio permissions"""

    screenshare: PermissionsMediaScreenshare
    """Screenshare permissions"""

    video: PermissionsMediaVideo
    """Video permissions"""


class PermissionsPluginsConfigUnionMember1(TypedDict, total=False):
    access_control: Literal["FULL_ACCESS", "VIEW_ONLY"]

    handles_view_only: bool


PermissionsPluginsConfig: TypeAlias = Union[str, PermissionsPluginsConfigUnionMember1]


class PermissionsPlugins(TypedDict, total=False):
    """Plugin permissions"""

    can_close: bool
    """Can close plugins that are already open"""

    can_edit_config: bool
    """Can edit plugin config"""

    can_start: bool
    """Can start plugins"""

    config: PermissionsPluginsConfig


class PermissionsPolls(TypedDict, total=False):
    """Poll permissions"""

    can_create: bool
    """Can create polls"""

    can_view: bool
    """Can view polls"""

    can_vote: bool
    """Can vote on polls"""


class Permissions(TypedDict, total=False):
    accept_waiting_requests: bool
    """Whether this participant can accept waiting requests"""

    can_accept_production_requests: bool

    can_change_participant_permissions: bool

    can_edit_display_name: bool

    can_livestream: bool

    can_record: bool

    can_spotlight: bool

    chat: PermissionsChat
    """Chat permissions"""

    connected_meetings: PermissionsConnectedMeetings

    disable_participant_audio: bool

    disable_participant_screensharing: bool

    disable_participant_video: bool

    hidden_participant: bool
    """Whether this participant is visible to others or not"""

    is_recorder: bool

    kick_participant: bool

    media: PermissionsMedia
    """Media permissions"""

    pin_participant: bool

    plugins: PermissionsPlugins
    """Plugin permissions"""

    polls: PermissionsPolls
    """Poll permissions"""

    recorder_type: Literal["RECORDER", "LIVESTREAMER", "NONE"]
    """Type of the recording peer"""

    show_participant_list: bool

    waiting_room_type: Literal["SKIP", "ON_PRIVILEGED_USER_ENTRY", "SKIP_ON_ACCEPT"]
    """Waiting room type"""


class UIDesignTokensColorsBackground(TypedDict, total=False):
    _1000: Annotated[str, PropertyInfo(alias="1000")]

    _600: Annotated[str, PropertyInfo(alias="600")]

    _700: Annotated[str, PropertyInfo(alias="700")]

    _800: Annotated[str, PropertyInfo(alias="800")]

    _900: Annotated[str, PropertyInfo(alias="900")]


class UIDesignTokensColorsBrand(TypedDict, total=False):
    _300: Annotated[str, PropertyInfo(alias="300")]

    _400: Annotated[str, PropertyInfo(alias="400")]

    _500: Annotated[str, PropertyInfo(alias="500")]

    _600: Annotated[str, PropertyInfo(alias="600")]

    _700: Annotated[str, PropertyInfo(alias="700")]


class UIDesignTokensColors(TypedDict, total=False):
    background: UIDesignTokensColorsBackground

    brand: UIDesignTokensColorsBrand

    danger: str

    success: str

    text: str

    text_on_brand: str

    video_bg: str

    warning: str


class UIDesignTokens(TypedDict, total=False):
    border_radius: Literal["rounded"]

    border_width: Literal["thin"]

    colors: UIDesignTokensColors

    logo: str

    spacing_base: float

    theme: Literal["dark"]


class UI(TypedDict, total=False):
    config_diff: object

    design_tokens: UIDesignTokens
