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

    model_config = pydantic.ConfigDict(frozen=True)

    #: Access identifier of the author, refers to /employees/employees endpoint
    author_id: int | None = pydantic.Field(
        default=None,
        description='Access identifier of the author, refers to /employees/employees endpoint',
    )
    #: Company identifier, refers to /api/me endpoint
    company_id: int | None = pydantic.Field(default=None, description='Company identifier, refers to /api/me endpoint')
    #: Document content type
    content_type: str | None = pydantic.Field(default=None, description='Document content type')
    #: Creation date of the document
    created_at: datetime.datetime = pydantic.Field(description='Creation date of the document')
    #: Employee identifier associated to the document
    employee_id: int | None = pydantic.Field(default=None, description='Employee identifier associated to the document')
    #: Document extension
    extension: str | None = pydantic.Field(default=None, description='Document extension')
    #: Document file size in bytes
    file_size: int | None = pydantic.Field(default=None, description='Document file size in bytes')
    #: Name of the document
    filename: str = pydantic.Field(description='Name of the document')
    #: Folder identifier, references to documents/folders endpoint
    folder_id: int | None = pydantic.Field(
        default=None,
        description='Folder identifier, references to documents/folders endpoint',
    )
    #: Document identifier
    id: int = pydantic.Field(description='Document identifier')
    #: Flag that indicates if the document is a company document
    is_company_document: bool | None = pydantic.Field(
        default=None,
        description='Flag that indicates if the document is a company document',
    )
    #: Flag that indicates if the document is a management document
    is_management_document: bool | None = pydantic.Field(
        default=None,
        description='Flag that indicates if the document is a management document',
    )
    #: Flag that indicates if the document is pending assignment
    is_pending_assignment: bool | None = pydantic.Field(
        default=None,
        description='Flag that indicates if the document is pending assignment',
    )
    #: Leave identifier associated to the document, refers to /timeoff/leaves endpoint
    leave_id: int | None = pydantic.Field(
        default=None,
        description='Leave identifier associated to the document, refers to /timeoff/leaves endpoint',
    )
    #: Flag to indicate if the document is public
    public: bool = pydantic.Field(description='Flag to indicate if the document is public')
    #: Document signature status
    signature_status: SignatureStatus | None = pydantic.Field(default=None, description='Document signature status')
    #: List of signee access identifiers associated to the document, refers to /employees/employees endpoint
    signees: Sequence[int] | None = pydantic.Field(
        default=None,
        description='List of signee access identifiers associated to the document, refers to /employees/employees endpoint',  # noqa: E501
    )
    #: Document space
    space: str = pydantic.Field(description='Document space')
    #: Last update date of the document
    updated_at: datetime.datetime = pydantic.Field(description='Last update date of the document')
    #: Deletion date of the document
    deleted_at: datetime.datetime | None = pydantic.Field(default=None, description='Deletion date of the document')


class DownloadUrl(pydantic.BaseModel):
    """Model for documents_download_url."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Document identifier
    id: int = pydantic.Field(description='Document identifier')
    #: Temporal document url
    url: str = pydantic.Field(description='Temporal document url')


class Folder(pydantic.BaseModel):
    """Model for documents_folder."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Whether the folder is active or not
    active: bool = pydantic.Field(description='Whether the folder is active or not')
    #: Company ID of the folder
    company_id: int | None = pydantic.Field(default=None, description='Company ID of the folder')
    #: Folder ID
    id: int = pydantic.Field(description='Folder ID')
    #: Folder name
    name: str = pydantic.Field(description='Folder name')
    #: Id of the parent folder
    parent_folder_id: int | None = pydantic.Field(default=None, description='Id of the parent folder')
    #: The space of the folder is related to the place where the folder is displayed
    space: str = pydantic.Field(
        description='The space of the folder is related to the place where the folder is displayed',
    )


class DocumentsEndpoint(Endpoint):
    """Endpoint for documents/documents operations."""

    endpoint = 'documents/documents'

    async def all(self, **kwargs) -> ListApiResponse[Document]:
        """Get all documents records.

        Official documentation: `documents/documents <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-documents-documents>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Document]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Document)

    async def get(self, **kwargs) -> MetaApiResponse[Document]:
        """Get documents with pagination metadata.

        Official documentation: `documents/documents <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-documents-documents>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Document]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Document)

    async def get_by_id(self, document_id: int | str, **kwargs) -> Document:
        """Get a specific document by ID.

        Official documentation: `documents/documents <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-documents-documents>`_

        :param document_id: The unique identifier.
        :type document_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Document
        """
        data = await self.api.get(self.endpoint, document_id, **kwargs)
        return pydantic.TypeAdapter(Document).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Document:
        """Create a new document.

        Official documentation: `documents/documents <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-documents-documents>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Document
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Document).validate_python(response)

    async def update(self, document_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Document:
        """Update a document.

        Official documentation: `documents/documents <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-documents-documents>`_

        :param document_id: The unique identifier of the record to update.
        :type document_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: Document
        """
        response = await self.api.put(self.endpoint, document_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Document).validate_python(response)

    async def delete(self, document_id: int | str, **kwargs) -> Document:
        """Delete a document.

        Official documentation: `documents/documents <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-documents-documents>`_

        :param document_id: The unique identifier of the record to delete.
        :type document_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: Document
        """
        response = await self.api.delete(self.endpoint, document_id, **kwargs)
        return pydantic.TypeAdapter(Document).validate_python(response)

    async def move_to_trash_bin(self, document_ids: Sequence[int], **kwargs) -> Sequence[Document]:
        """Move documents to trash bin.

        Official documentation: `documents/documents <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-documents-documents>`_

        :param document_ids: The unique identifier.
        :type document_ids: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Sequence[Document]
        """
        response = await self.api.post(
            self.endpoint,
            'move_to_trash_bin',
            json={'document_ids': document_ids},
            **kwargs,
        )
        return [pydantic.TypeAdapter(Document).validate_python(doc) for doc in response]

    async def restore_from_trash_bin(self, document_ids: Sequence[int], **kwargs) -> Sequence[Document]:
        """Restore documents from trash bin.

        Official documentation: `documents/documents <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-documents-documents>`_

        :param document_ids: The unique identifier.
        :type document_ids: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Sequence[Document]
        """
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
        """Bulk create download URLs for documents.

        Official documentation: `documents/download_urls <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-documents-download-urls>`_

        :param document_ids: The unique identifier.
        :type document_ids: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Sequence[DownloadUrl]
        """
        response = await self.api.post(self.endpoint, 'bulk_create', json={'ids': document_ids}, **kwargs)
        return [pydantic.TypeAdapter(DownloadUrl).validate_python(url) for url in response]


class FoldersEndpoint(Endpoint):
    """Endpoint for documents/folders operations."""

    endpoint = 'documents/folders'

    async def all(self, **kwargs) -> ListApiResponse[Folder]:
        """Get all folders records.

        Official documentation: `documents/folders <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-documents-folders>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Folder]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(raw_data=data, model_type=Folder)

    async def get(self, **kwargs) -> MetaApiResponse[Folder]:
        """Get folders with pagination metadata.

        Official documentation: `documents/folders <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-documents-folders>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Folder]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(raw_meta=response['meta'], raw_data=response['data'], model_type=Folder)

    async def get_by_id(self, folder_id: int | str, **kwargs) -> Folder:
        """Get a specific folder by ID.

        Official documentation: `documents/folders <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-documents-folders>`_

        :param folder_id: The unique identifier.
        :type folder_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Folder
        """
        data = await self.api.get(self.endpoint, folder_id, **kwargs)
        return pydantic.TypeAdapter(Folder).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Folder:
        """Create a new folder.

        Official documentation: `documents/folders <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-documents-folders>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Folder
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Folder).validate_python(response)

    async def update(self, folder_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Folder:
        """Update a folder.

        Official documentation: `documents/folders <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-documents-folders>`_

        :param folder_id: The unique identifier of the record to update.
        :type folder_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: Folder
        """
        response = await self.api.put(self.endpoint, folder_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Folder).validate_python(response)
