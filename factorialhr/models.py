import datetime
import enum

import pydantic


class HalfDay(enum.StrEnum):
    beggining_of_day = "beggining_of_day"
    end_of_day = "end_of_day"


class Employee(pydantic.BaseModel):
    id: int
    first_name: str
    last_name: str
    full_name: str
    email: str
    birthday: datetime.date | None
    terminated_on: datetime.date | None
    termination_reason: str | None
    termination_reason_type: str | None
    termination_observations: str | None
    identifier: str | None
    identifier_type: str | None
    gender: str | None
    nationality: str | None
    bank_number: str | None
    country: str | None
    city: str | None
    state: str | None
    postal_code: str | None
    address_line_1: str | None
    address_line_2: str | None
    swift_bic: str | None
    company_id: int
    legal_entity_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    manager_id: int | None
    timeoff_manager_id: int | None
    social_security_number: str | None
    timeoff_policy_id: int
    team_ids: list[int]
    phone_number: str | None
    company_identifier: str | None


class Webhook(pydantic.BaseModel):
    id: int
    subscription_type: str
    name: str | None
    challenge: str | None
    target_url: str
    company_id: int | None


class Location(pydantic.BaseModel):
    id: int
    name: str | None  # TODO: check which ones are required
    country: str | None
    phone_number: str | None
    state: str | None
    city: str | None
    address_line_1: str | None
    address_line_2: str | None
    postal_code: str | None
    timezone: str | None
    company_holidays_ids: list[int]


class CompanyHoliday(pydantic.BaseModel):
    id: int
    summary: str | None  # TODO: check which ones are required
    description: str | None
    date: datetime.date
    half_day: HalfDay | None
    location_id: int | None


class Team(pydantic.BaseModel):
    id: int
    name: str
    employee_ids: list[int]
    lead_ids: list[int]
    description: str | None
    avatar: str | None


class Folder(pydantic.BaseModel):
    id: int
    company_id: int
    name: str
    active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime


class Document(pydantic.BaseModel):
    id: int
    employee_id: int | None
    company_id: int
    folder_id: int | None
    url: str
    filename: str
    public: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime


class LegalEntity(pydantic.BaseModel):
    id: int
    city: str | None
    state: str | None
    postal_code: str | None
    address_line_1: str | None
    address_line_2: str | None
    country: str | None
    company_id: int
    legal_name: str | None
    currency: str | None


class Key(pydantic.BaseModel):
    id: int
    name: str
    token_digest: str
    created_at: datetime.datetime


class Task(pydantic.BaseModel):
    id: int
    name: str
    content: str | None
    due_on: datetime.date | None
    assignee_ids: list[int]
    completed_at: datetime.datetime | None


class File(pydantic.BaseModel):
    id: int
    task_id: int
    filename: str
    path: str


class CustomFieldChoiceOption(pydantic.BaseModel):
    id: int
    label: str
    value: str
    is_active: bool


class CustomFieldType(enum.StrEnum):
    text = "text"
    long_text = "long_text"
    number = "number"
    single_choice = "single_choice"


class CustomField(pydantic.BaseModel):
    id: int
    label: str
    identifier: str
    position: int | None
    required: bool
    field_type: CustomFieldType
    min_value: int | None
    max_value: int | None
    choice_options: CustomFieldChoiceOption


class CustomFieldValue(pydantic.BaseModel):
    id: int
    label: str
    value: str
    field_id: int
    slug_id: int
    slug_name: str
    required: bool
    instance_id: int


class PostType(enum.StrEnum):
    event = "event"
    announcement = "announcement"
    first_day = "first_day"
    birthday = "birthday"
    workiversary = "workiversary"


class Post(pydantic.BaseModel):
    id: int
    title: str
    description: str
    type: PostType
    allow_comments_and_reactions: bool
    location: str | None
    published_at: datetime.datetime
    starts_at: datetime.datetime | None
    ends_at: datetime.datetime | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    visits_count: int
    comments_count: int
    reactions_count: int
    cover_image_url: str | None
    author_id: int
    posts_group_id: int
    target_id: int


class Attendance(pydantic.BaseModel):
    id: int
    employee_id: int
    clock_in: datetime.datetime
    clock_out: datetime.datetime | None
    observations: str | None
    half_day: HalfDay | None
    in_location_latitude: float | None
    in_location_longitude: float | None
    in_location_accuracy: float | None
    out_location_latitude: float | None
    out_location_longitude: float | None
    out_location_accuracy: float | None
    workable: bool
    automatic_clock_in: bool
    automatic_clock_out: bool | None


class ContractVersion(pydantic.BaseModel):
    # TODO: it looks like that fields are added based on language
    id: int
    employee_id: int
    country: str | None
    job_title: str | None
    role: str | None
    level: str | None
    effective_on: datetime.date
    starts_on: datetime.date
    ends_on: datetime.date | None
    has_payroll: bool
    salary_amount: int
    salary_frequency: str
    working_week_days: str
    working_hours: int
    working_hours_frequency: str
    es_has_teleworking_contract: bool
    es_cotization_group: str | None
    es_contract_observations: str | None
    es_job_description: str | None
    es_trial_period_ends_on: str | None
    es_contract_type_id: int | None
    es_working_day_type_id: int | None
    es_education_level_id: int | None
    es_professional_category_id: int | None
    fr_employee_type: str | None
    fr_forfait_jours: bool
    fr_jours_par_an: int | None
    fr_coefficient: int | None
    fr_contract_type_id: int | None
    fr_level_id: int | None
    fr_step_id: int | None
    fr_mutual_id: int | None
    fr_professional_category_id: int | None
    fr_work_type_id: int | None
    compensation_ids: list[int]
    de_contract_type_id: int | None


class CustomTable(pydantic.BaseModel):
    id: int
    name: str
    created_at: datetime.datetime
    topic_name: str
    custom_resources_topic_id: int
    reportable: bool
    hidden: bool


class CustomTableField(pydantic.BaseModel):
    id: int
    label: str
    position: int


class Event(pydantic.BaseModel):
    id: str
    type: str
    name: str
    datetime: datetime.datetime
    resource_id: int


class Workplace(pydantic.BaseModel):
    id: int
    name: str
    country: str
    phone_number: str | None
    state: str | None
    city: str | None
    address_line_1: str | None
    address_line_2: str | None
    postal_code: str | None
    company_id: int
    payroll_policy_id: int | None
    main: bool
    timezone: str


class LeaveType(pydantic.BaseModel):
    id: int
    accrues: bool
    active: bool
    approval_required: bool
    attachment: bool
    color: str
    identifier: str
    name: str
    visibility: bool
    workable: bool
    half_days_units_enabled: bool
    max_days_in_cents: int | None
    min_days_in_cents: int | None


class Leave(pydantic.BaseModel):
    id: int
    approved: bool
    description: str | None
    employee_id: int
    start_on: datetime.date
    finish_on: datetime.date
    half_day: HalfDay | None
    leave_type_id: int
    leave_type_name: str | None
    employee_full_name: str


class JobPostingStatus(enum.StrEnum):
    draft = "draft"
    published = "published"
    archived = "archived"


class JobPosting(pydantic.BaseModel):
    id: int
    created_at: datetime.datetime
    title: str
    description: str
    remote: bool
    status: str
    schedule_type: str
    team_id: int
    location_id: int
    ats_company_id: int
    salary_format: str
    salary_from_amount_in_cents: int
    salary_to_amount_in_cents: int
    cv_requirement: str
    cover_letter_requirement: str
    phone_requirement: str
    photo_requirement: str
    personal_url_requirement: str
    use_ats_questions: bool


class Candidate(pydantic.BaseModel):
    id: int
    first_name: str
    last_name: str
    full_name: str
    email: str
    talent_pool: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    source: str


class TimeOffPolicy(pydantic.BaseModel):
    id: int
    main: bool
    name: str
    default_allowance_id: int
    description: str | None
    allowance_incidences: int
    company_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


class CompensationType(enum.StrEnum):
    fixed = "fixed"
    up_to = "up_to"


class CompensationRecurrence(enum.StrEnum):
    monthly = "monthly"
    every_2_months = "every_2_months"
    every_3_months = "every_3_months"
    every_4_months = "every_4_months"
    every_5_months = "every_5_months"
    every_6_months = "every_6_months"
    every_7_months = "every_7_months"
    every_8_months = "every_8_months"
    every_9_months = "every_9_months"
    every_10_months = "every_10_months"
    every_11_months = "every_11_months"
    every_12_months = "every_12_months"


class Unit(enum.StrEnum):
    money = "money"
    units = "units"


class Calculation(enum.StrEnum):
    current_period = "current_period"
    previous_period = "previous_period"


class Compensation(pydantic.BaseModel):
    id: int
    contract_version_id: int
    description: str | None
    compensation_type: CompensationType | None
    amount: int
    recurrence: CompensationRecurrence | None
    first_payment_on: datetime.date
    sync_with_supplements: bool
    contracts_taxonomy_id: int
    payroll_policy_id: int | None
    recurrence_count: int
    starts_on: datetime.date | None
    unit: Unit | None
    calculation: Calculation | None


class Taxonomy(pydantic.BaseModel):
    id: int
    name: str
    archived: bool
    default: bool
    legal_entity_id: int
