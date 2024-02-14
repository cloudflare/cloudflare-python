# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DefaultGetResponse",
    "Settings",
    "SettingsContextEnricher",
    "Tools",
    "ToolsZarazManagedComponent",
    "ToolsZarazManagedComponentActions",
    "ToolsZarazManagedComponentNeoEvent",
    "ToolsZarazCustomManagedComponent",
    "ToolsZarazCustomManagedComponentWorker",
    "ToolsZarazCustomManagedComponentActions",
    "ToolsZarazCustomManagedComponentNeoEvent",
    "Triggers",
    "TriggersExcludeRule",
    "TriggersExcludeRuleZarazLoadRule",
    "TriggersExcludeRuleZarazClickListenerRule",
    "TriggersExcludeRuleZarazClickListenerRuleSettings",
    "TriggersExcludeRuleZarazTimerRule",
    "TriggersExcludeRuleZarazTimerRuleSettings",
    "TriggersExcludeRuleZarazFormSubmissionRule",
    "TriggersExcludeRuleZarazFormSubmissionRuleSettings",
    "TriggersExcludeRuleZarazVariableMatchRule",
    "TriggersExcludeRuleZarazVariableMatchRuleSettings",
    "TriggersExcludeRuleZarazScrollDepthRule",
    "TriggersExcludeRuleZarazScrollDepthRuleSettings",
    "TriggersExcludeRuleZarazElementVisibilityRule",
    "TriggersExcludeRuleZarazElementVisibilityRuleSettings",
    "TriggersLoadRule",
    "TriggersLoadRuleZarazLoadRule",
    "TriggersLoadRuleZarazClickListenerRule",
    "TriggersLoadRuleZarazClickListenerRuleSettings",
    "TriggersLoadRuleZarazTimerRule",
    "TriggersLoadRuleZarazTimerRuleSettings",
    "TriggersLoadRuleZarazFormSubmissionRule",
    "TriggersLoadRuleZarazFormSubmissionRuleSettings",
    "TriggersLoadRuleZarazVariableMatchRule",
    "TriggersLoadRuleZarazVariableMatchRuleSettings",
    "TriggersLoadRuleZarazScrollDepthRule",
    "TriggersLoadRuleZarazScrollDepthRuleSettings",
    "TriggersLoadRuleZarazElementVisibilityRule",
    "TriggersLoadRuleZarazElementVisibilityRuleSettings",
    "Variables",
    "VariablesUnionMember0",
    "VariablesUnionMember1",
    "VariablesUnionMember1Value",
    "Consent",
    "ConsentButtonTextTranslations",
    "ConsentPurposes",
    "ConsentPurposesWithTranslations",
]


class SettingsContextEnricher(BaseModel):
    escaped_worker_name: str = FieldInfo(alias="escapedWorkerName")

    worker_tag: str = FieldInfo(alias="workerTag")


class Settings(BaseModel):
    auto_inject_script: bool = FieldInfo(alias="autoInjectScript")
    """Automatic injection of Zaraz scripts enabled."""

    context_enricher: Optional[SettingsContextEnricher] = FieldInfo(alias="contextEnricher", default=None)
    """Details of the worker that receives and edits Zaraz Context object."""

    cookie_domain: Optional[str] = FieldInfo(alias="cookieDomain", default=None)
    """The domain Zaraz will use for writing and reading its cookies."""

    ecommerce: Optional[bool] = None
    """Ecommerce API enabled."""

    events_api_path: Optional[str] = FieldInfo(alias="eventsApiPath", default=None)
    """Custom endpoint for server-side track events."""

    hide_external_referer: Optional[bool] = FieldInfo(alias="hideExternalReferer", default=None)
    """Hiding external referrer URL enabled."""

    hide_ip_address: Optional[bool] = FieldInfo(alias="hideIPAddress", default=None)
    """Trimming IP address enabled."""

    hide_query_params: Optional[bool] = FieldInfo(alias="hideQueryParams", default=None)
    """Removing URL query params enabled."""

    hide_user_agent: Optional[bool] = FieldInfo(alias="hideUserAgent", default=None)
    """Removing sensitive data from User Aagent string enabled."""

    init_path: Optional[str] = FieldInfo(alias="initPath", default=None)
    """Custom endpoint for Zaraz init script."""

    inject_iframes: Optional[bool] = FieldInfo(alias="injectIframes", default=None)
    """Injection of Zaraz scripts into iframes enabled."""

    mc_root_path: Optional[str] = FieldInfo(alias="mcRootPath", default=None)
    """Custom path for Managed Components server functionalities."""

    script_path: Optional[str] = FieldInfo(alias="scriptPath", default=None)
    """Custom endpoint for Zaraz main script."""

    track_path: Optional[str] = FieldInfo(alias="trackPath", default=None)
    """Custom endpoint for Zaraz tracking requests."""


class ToolsZarazManagedComponentActions(BaseModel):
    action_type: str = FieldInfo(alias="actionType")
    """Tool event type"""

    blocking_triggers: List[str] = FieldInfo(alias="blockingTriggers")
    """List of blocking triggers IDs"""

    data: object
    """Event payload"""

    firing_triggers: List[str] = FieldInfo(alias="firingTriggers")
    """List of firing triggers IDs"""


class ToolsZarazManagedComponentNeoEvent(BaseModel):
    action_type: str = FieldInfo(alias="actionType")
    """Tool event type"""

    blocking_triggers: List[str] = FieldInfo(alias="blockingTriggers")
    """List of blocking triggers IDs"""

    data: object
    """Event payload"""

    firing_triggers: List[str] = FieldInfo(alias="firingTriggers")
    """List of firing triggers IDs"""


class ToolsZarazManagedComponent(BaseModel):
    blocking_triggers: List[str] = FieldInfo(alias="blockingTriggers")
    """List of blocking trigger IDs"""

    component: str
    """Tool's internal name"""

    default_fields: Dict[str, Union[str, bool]] = FieldInfo(alias="defaultFields")
    """Default fields for tool's actions"""

    enabled: bool
    """Whether tool is enabled"""

    name: str
    """Tool's name defined by the user"""

    permissions: List[str]
    """List of permissions granted to the component"""

    settings: Dict[str, Union[str, bool]]
    """Tool's settings"""

    type: Literal["component"]

    actions: Optional[Dict[str, ToolsZarazManagedComponentActions]] = None
    """Actions configured on a tool. Either this or neoEvents field is required."""

    default_purpose: Optional[str] = FieldInfo(alias="defaultPurpose", default=None)
    """Default consent purpose ID"""

    neo_events: Optional[List[ToolsZarazManagedComponentNeoEvent]] = FieldInfo(alias="neoEvents", default=None)
    """DEPRECATED - List of actions configured on a tool.

    Either this or actions field is required. If both are present, actions field
    will take precedence.
    """


class ToolsZarazCustomManagedComponentWorker(BaseModel):
    escaped_worker_name: str = FieldInfo(alias="escapedWorkerName")

    worker_tag: str = FieldInfo(alias="workerTag")


class ToolsZarazCustomManagedComponentActions(BaseModel):
    action_type: str = FieldInfo(alias="actionType")
    """Tool event type"""

    blocking_triggers: List[str] = FieldInfo(alias="blockingTriggers")
    """List of blocking triggers IDs"""

    data: object
    """Event payload"""

    firing_triggers: List[str] = FieldInfo(alias="firingTriggers")
    """List of firing triggers IDs"""


class ToolsZarazCustomManagedComponentNeoEvent(BaseModel):
    action_type: str = FieldInfo(alias="actionType")
    """Tool event type"""

    blocking_triggers: List[str] = FieldInfo(alias="blockingTriggers")
    """List of blocking triggers IDs"""

    data: object
    """Event payload"""

    firing_triggers: List[str] = FieldInfo(alias="firingTriggers")
    """List of firing triggers IDs"""


class ToolsZarazCustomManagedComponent(BaseModel):
    blocking_triggers: List[str] = FieldInfo(alias="blockingTriggers")
    """List of blocking trigger IDs"""

    component: str
    """Tool's internal name"""

    default_fields: Dict[str, Union[str, bool]] = FieldInfo(alias="defaultFields")
    """Default fields for tool's actions"""

    enabled: bool
    """Whether tool is enabled"""

    name: str
    """Tool's name defined by the user"""

    permissions: List[str]
    """List of permissions granted to the component"""

    settings: Dict[str, Union[str, bool]]
    """Tool's settings"""

    type: Literal["custom-mc"]

    worker: ToolsZarazCustomManagedComponentWorker
    """Cloudflare worker that acts as a managed component"""

    actions: Optional[Dict[str, ToolsZarazCustomManagedComponentActions]] = None
    """Actions configured on a tool. Either this or neoEvents field is required."""

    default_purpose: Optional[str] = FieldInfo(alias="defaultPurpose", default=None)
    """Default consent purpose ID"""

    neo_events: Optional[List[ToolsZarazCustomManagedComponentNeoEvent]] = FieldInfo(alias="neoEvents", default=None)
    """DEPRECATED - List of actions configured on a tool.

    Either this or actions field is required. If both are present, actions field
    will take precedence.
    """


Tools = Union[ToolsZarazManagedComponent, ToolsZarazCustomManagedComponent]


class TriggersExcludeRuleZarazLoadRule(BaseModel):
    id: str

    match: str

    op: Literal[
        "CONTAINS",
        "EQUALS",
        "STARTS_WITH",
        "ENDS_WITH",
        "MATCH_REGEX",
        "NOT_MATCH_REGEX",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
    ]

    value: str


class TriggersExcludeRuleZarazClickListenerRuleSettings(BaseModel):
    selector: str

    type: Literal["xpath", "css"]

    wait_for_tags: int = FieldInfo(alias="waitForTags")


class TriggersExcludeRuleZarazClickListenerRule(BaseModel):
    id: str

    action: Literal["clickListener"]

    settings: TriggersExcludeRuleZarazClickListenerRuleSettings


class TriggersExcludeRuleZarazTimerRuleSettings(BaseModel):
    interval: int

    limit: int


class TriggersExcludeRuleZarazTimerRule(BaseModel):
    id: str

    action: Literal["timer"]

    settings: TriggersExcludeRuleZarazTimerRuleSettings


class TriggersExcludeRuleZarazFormSubmissionRuleSettings(BaseModel):
    selector: str

    validate_: bool = FieldInfo(alias="validate")


class TriggersExcludeRuleZarazFormSubmissionRule(BaseModel):
    id: str

    action: Literal["formSubmission"]

    settings: TriggersExcludeRuleZarazFormSubmissionRuleSettings


class TriggersExcludeRuleZarazVariableMatchRuleSettings(BaseModel):
    match: str

    variable: str


class TriggersExcludeRuleZarazVariableMatchRule(BaseModel):
    id: str

    action: Literal["variableMatch"]

    settings: TriggersExcludeRuleZarazVariableMatchRuleSettings


class TriggersExcludeRuleZarazScrollDepthRuleSettings(BaseModel):
    positions: str


class TriggersExcludeRuleZarazScrollDepthRule(BaseModel):
    id: str

    action: Literal["scrollDepth"]

    settings: TriggersExcludeRuleZarazScrollDepthRuleSettings


class TriggersExcludeRuleZarazElementVisibilityRuleSettings(BaseModel):
    selector: str


class TriggersExcludeRuleZarazElementVisibilityRule(BaseModel):
    id: str

    action: Literal["elementVisibility"]

    settings: TriggersExcludeRuleZarazElementVisibilityRuleSettings


TriggersExcludeRule = Union[
    TriggersExcludeRuleZarazLoadRule,
    TriggersExcludeRuleZarazClickListenerRule,
    TriggersExcludeRuleZarazTimerRule,
    TriggersExcludeRuleZarazFormSubmissionRule,
    TriggersExcludeRuleZarazVariableMatchRule,
    TriggersExcludeRuleZarazScrollDepthRule,
    TriggersExcludeRuleZarazElementVisibilityRule,
]


class TriggersLoadRuleZarazLoadRule(BaseModel):
    id: str

    match: str

    op: Literal[
        "CONTAINS",
        "EQUALS",
        "STARTS_WITH",
        "ENDS_WITH",
        "MATCH_REGEX",
        "NOT_MATCH_REGEX",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
    ]

    value: str


class TriggersLoadRuleZarazClickListenerRuleSettings(BaseModel):
    selector: str

    type: Literal["xpath", "css"]

    wait_for_tags: int = FieldInfo(alias="waitForTags")


class TriggersLoadRuleZarazClickListenerRule(BaseModel):
    id: str

    action: Literal["clickListener"]

    settings: TriggersLoadRuleZarazClickListenerRuleSettings


class TriggersLoadRuleZarazTimerRuleSettings(BaseModel):
    interval: int

    limit: int


class TriggersLoadRuleZarazTimerRule(BaseModel):
    id: str

    action: Literal["timer"]

    settings: TriggersLoadRuleZarazTimerRuleSettings


class TriggersLoadRuleZarazFormSubmissionRuleSettings(BaseModel):
    selector: str

    validate_: bool = FieldInfo(alias="validate")


class TriggersLoadRuleZarazFormSubmissionRule(BaseModel):
    id: str

    action: Literal["formSubmission"]

    settings: TriggersLoadRuleZarazFormSubmissionRuleSettings


class TriggersLoadRuleZarazVariableMatchRuleSettings(BaseModel):
    match: str

    variable: str


class TriggersLoadRuleZarazVariableMatchRule(BaseModel):
    id: str

    action: Literal["variableMatch"]

    settings: TriggersLoadRuleZarazVariableMatchRuleSettings


class TriggersLoadRuleZarazScrollDepthRuleSettings(BaseModel):
    positions: str


class TriggersLoadRuleZarazScrollDepthRule(BaseModel):
    id: str

    action: Literal["scrollDepth"]

    settings: TriggersLoadRuleZarazScrollDepthRuleSettings


class TriggersLoadRuleZarazElementVisibilityRuleSettings(BaseModel):
    selector: str


class TriggersLoadRuleZarazElementVisibilityRule(BaseModel):
    id: str

    action: Literal["elementVisibility"]

    settings: TriggersLoadRuleZarazElementVisibilityRuleSettings


TriggersLoadRule = Union[
    TriggersLoadRuleZarazLoadRule,
    TriggersLoadRuleZarazClickListenerRule,
    TriggersLoadRuleZarazTimerRule,
    TriggersLoadRuleZarazFormSubmissionRule,
    TriggersLoadRuleZarazVariableMatchRule,
    TriggersLoadRuleZarazScrollDepthRule,
    TriggersLoadRuleZarazElementVisibilityRule,
]


class Triggers(BaseModel):
    exclude_rules: List[TriggersExcludeRule] = FieldInfo(alias="excludeRules")
    """Rules defining when the trigger is not fired."""

    load_rules: List[TriggersLoadRule] = FieldInfo(alias="loadRules")
    """Rules defining when the trigger is fired."""

    name: str
    """Trigger name."""

    description: Optional[str] = None
    """Trigger description."""

    system: Optional[Literal["pageload"]] = None


class VariablesUnionMember0(BaseModel):
    name: str

    type: Literal["string", "secret"]

    value: str


class VariablesUnionMember1Value(BaseModel):
    escaped_worker_name: str = FieldInfo(alias="escapedWorkerName")

    worker_tag: str = FieldInfo(alias="workerTag")


class VariablesUnionMember1(BaseModel):
    name: str

    type: Literal["worker"]

    value: VariablesUnionMember1Value


Variables = Union[VariablesUnionMember0, VariablesUnionMember1]


class ConsentButtonTextTranslations(BaseModel):
    accept_all: Dict[str, str]
    """Object where keys are language codes"""

    confirm_my_choices: Dict[str, str]
    """Object where keys are language codes"""

    reject_all: Dict[str, str]
    """Object where keys are language codes"""


class ConsentPurposes(BaseModel):
    description: str

    name: str


class ConsentPurposesWithTranslations(BaseModel):
    description: Dict[str, str]
    """Object where keys are language codes"""

    name: Dict[str, str]
    """Object where keys are language codes"""

    order: int


class Consent(BaseModel):
    enabled: bool

    button_text_translations: Optional[ConsentButtonTextTranslations] = FieldInfo(
        alias="buttonTextTranslations", default=None
    )

    company_email: Optional[str] = FieldInfo(alias="companyEmail", default=None)

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)

    company_street_address: Optional[str] = FieldInfo(alias="companyStreetAddress", default=None)

    consent_modal_intro_html: Optional[str] = FieldInfo(alias="consentModalIntroHTML", default=None)

    consent_modal_intro_html_with_translations: Optional[Dict[str, str]] = FieldInfo(
        alias="consentModalIntroHTMLWithTranslations", default=None
    )
    """Object where keys are language codes"""

    cookie_name: Optional[str] = FieldInfo(alias="cookieName", default=None)

    custom_css: Optional[str] = FieldInfo(alias="customCSS", default=None)

    custom_intro_disclaimer_dismissed: Optional[bool] = FieldInfo(alias="customIntroDisclaimerDismissed", default=None)

    default_language: Optional[str] = FieldInfo(alias="defaultLanguage", default=None)

    hide_modal: Optional[bool] = FieldInfo(alias="hideModal", default=None)

    purposes: Optional[Dict[str, ConsentPurposes]] = None
    """Object where keys are purpose alpha-numeric IDs"""

    purposes_with_translations: Optional[Dict[str, ConsentPurposesWithTranslations]] = FieldInfo(
        alias="purposesWithTranslations", default=None
    )
    """Object where keys are purpose alpha-numeric IDs"""


class DefaultGetResponse(BaseModel):
    data_layer: bool = FieldInfo(alias="dataLayer")
    """Data layer compatibility mode enabled."""

    debug_key: str = FieldInfo(alias="debugKey")
    """The key for Zaraz debug mode."""

    settings: Settings
    """General Zaraz settings."""

    tools: Dict[str, Tools]
    """
    Tools set up under Zaraz configuration, where key is the alpha-numeric tool ID
    and value is the tool configuration object.
    """

    triggers: Dict[str, Triggers]
    """
    Triggers set up under Zaraz configuration, where key is the trigger
    alpha-numeric ID and value is the trigger configuration.
    """

    variables: Dict[str, Variables]
    """
    Variables set up under Zaraz configuration, where key is the variable
    alpha-numeric ID and value is the variable configuration. Values of variables of
    type secret are not included.
    """

    zaraz_version: int = FieldInfo(alias="zarazVersion")
    """Zaraz internal version of the config."""

    consent: Optional[Consent] = None
    """Consent management configuration."""

    history_change: Optional[bool] = FieldInfo(alias="historyChange", default=None)
    """Single Page Application support enabled."""
