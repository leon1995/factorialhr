import datetime
import typing
from collections.abc import Mapping, Sequence
from enum import StrEnum

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class SignatureStatus(StrEnum):
    """Enum for document signature status."""

    PENDING = 'pending'
    PARTIALLY_SIGNED = 'partially_signed'
    DECLINED = 'declined'
    COMPLETED = 'completed'
    BOUNCED_EMAIL = 'bounced_email'
    CANCELLED = 'cancelled'
    ERROR = 'error'
    EXPIRED = 'expired'


class Document(pydantic.BaseModel):
    """Model for documents_document."""

    author_id: int | None = pydantic.Field(
        default=None,
        description='Access identifier of the author, refers to /employees/employees endpoint',
    )
    company_id: int | None = pydantic.Field(default=None, description='Company identifier, refers to /api/me endpoint')
    content_type: str | None = pydantic.Field(default=None, description='Document content type')
    created_at: datetime.datetime = pydantic.Field(description='Creation date of the document')
    employee_id: int | None = pydantic.Field(default=None, description='Employee identifier associated to the document')
    extension: str | None = pydantic.Field(default=None, description='Document extension')
    file_size: int | None = pydantic.Field(default=None, description='Document file size in bytes')
    filename: str = pydantic.Field(description='Name of the document')
    folder_id: int | None = pydantic.Field(
        default=None,
        description='Folder identifier, references to documents/folders endpoint',
    )
    id: int = pydantic.Field(description='Document identifier')
    is_company_document: bool | None = pydantic.Field(
        default=None,
        description='Flag that indicates if the document is a company document',
    )
    is_management_document: bool | None = pydantic.Field(
        default=None,
        description='Flag that indicates if the document is a management document',
    )
    is_pending_assignment: bool | None = pydantic.Field(
        default=None,
        description='Flag that indicates if the document is pending assignment',
    )
    leave_id: int | None = pydantic.Field(
        default=None,
        description='Leave identifier associated to the document, refers to /timeoff/leaves endpoint',
    )
    public: bool = pydantic.Field(description='Flag to indicate if the document is public')
    signature_status: SignatureStatus | None = pydantic.Field(default=None, description='Document signature status')
    signees: Sequence[int] | None = pydantic.Field(
        default=None,
        description='List of signee access identifiers associated to the document, refers to /employees/employees endpoint',  # noqa: E501
    )
    space: str = pydantic.Field(description='Document space')
    updated_at: datetime.datetime = pydantic.Field(description='Last update date of the document')
    deleted_at: datetime.datetime | None = pydantic.Field(default=None, description='Deletion date of the document')


class DownloadUrl(pydantic.BaseModel):
    """Model for documents_download_url."""

    id: int = pydantic.Field(description='Document identifier')
    url: str = pydantic.Field(description='Temporal document url')


class Folder(pydantic.BaseModel):
    """Model for documents_folder."""

    active: bool = pydantic.Field(description='Whether the folder is active or not')
    company_id: int | None = pydantic.Field(default=None, description='Company ID of the folder')
    id: int = pydantic.Field(description='Folder ID')
    name: str = pydantic.Field(description='Folder name')
    parent_folder_id: int | None = pydantic.Field(default=None, description='Id of the parent folder')
    space: str = pydantic.Field(
        description='The space of the folder is related to the place where the folder is displayed',
    )


class DocumentsEndpoint(Endpoint):
    """Endpoint for documents/documents operations."""

    endpoint = 'documents/documents'

    async def all(self, **kwargs) -> ListApiResponse[Document]:
        """Get all documents records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Document)

    async def get(self, **kwargs) -> MetaApiResponse[Document]:
        """Get documents with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Document)

    async def get_by_id(self, document_id: int | str, **kwargs) -> Document:
        """Get a specific document by ID."""
        data = await self.api.get(self.endpoint, document_id, **kwargs)
        return pydantic.TypeAdapter(Document).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Document:
        """Create a new document."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Document).validate_python(response)

    async def update(self, document_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Document:
        """Update a document."""
        response = await self.api.put(self.endpoint, document_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Document).validate_python(response)

    async def delete(self, document_id: int | str, **kwargs) -> Document:
        """Delete a document."""
        response = await self.api.delete(self.endpoint, document_id, **kwargs)
        return pydantic.TypeAdapter(Document).validate_python(response)

    async def move_to_trash_bin(self, document_ids: Sequence[int], **kwargs) -> Sequence[Document]:
        """Move documents to trash bin."""
        response = await self.api.post(
            self.endpoint,
            'move_to_trash_bin',
            json={'document_ids': document_ids},
            **kwargs,
        )
        return [pydantic.TypeAdapter(Document).validate_python(doc) for doc in response]

    async def restore_from_trash_bin(self, document_ids: Sequence[int], **kwargs) -> Sequence[Document]:
        """Restore documents from trash bin."""
        response = await self.api.post(
            self.endpoint,
            'restore_from_trash_bin',
            json={'document_ids': document_ids},
            **kwargs,
        )
        return [pydantic.TypeAdapter(Document).validate_python(doc) for doc in response]


class DownloadUrlsEndpoint(Endpoint):
    """Endpoint for documents/download_urls operations."""

    endpoint = 'documents/download_urls'

    async def bulk_create(self, document_ids: Sequence[int], **kwargs) -> Sequence[DownloadUrl]:
        """Bulk create download URLs for documents."""
        response = await self.api.post(self.endpoint, 'bulk_create', json={'ids': document_ids}, **kwargs)
        return [pydantic.TypeAdapter(DownloadUrl).validate_python(url) for url in response]


class FoldersEndpoint(Endpoint):
    """Endpoint for documents/folders operations."""

    endpoint = 'documents/folders'

    async def all(self, **kwargs) -> ListApiResponse[Folder]:
        """Get all folders records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Folder)

    async def get(self, **kwargs) -> MetaApiResponse[Folder]:
        """Get folders with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Folder)

    async def get_by_id(self, folder_id: int | str, **kwargs) -> Folder:
        """Get a specific folder by ID."""
        data = await self.api.get(self.endpoint, folder_id, **kwargs)
        return pydantic.TypeAdapter(Folder).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Folder:
        """Create a new folder."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Folder).validate_python(response)

    async def update(self, folder_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Folder:
        """Update a folder."""
        response = await self.api.put(self.endpoint, folder_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Folder).validate_python(response)
