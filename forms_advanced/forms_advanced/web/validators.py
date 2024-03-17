from django.core.exceptions import ValidationError


def validate_email(email):
    if '@' not in email:
        raise ValidationError('Email should contain @ character')


class FileSizeValidator:
    def __init__(self, max_file_size):
        self.max_file_size = max_file_size

    def __call__(self, value):
        if value.size > self.max_file_size:
            raise ValidationError(f"The file size should be less than {self.max_file_size}")

# validate_email("miro@abv.bg")

# FileSizeValidator(5)(file)
