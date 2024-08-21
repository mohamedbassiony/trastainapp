from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESS = "file_validate_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    DATABASE_CONNECTED = "database_connedted_firebase_successfully"
    DATA_SAVED_FAILED = "data_saved_failed"
    DATA_SAVED_SUCCESS = "data_saved_success"