import pathlib
from poetry.core.packages.package import Package


class PackageService:
    @staticmethod
    def collect_meta_data(package: Package) -> dict:
        package: dict = {
            "name": PackageService.get_check_field(package.name),
            "version": PackageService.get_check_field(package.version),
            "packages": list(
                map(
                    lambda dependency: PackageService.get_check_field(dependency.name),
                    package.all_requires
                )
            ),
            "url": PackageService.get_check_field(package.repository_url),
            "license": PackageService.get_check_field(package.license),
            "author": PackageService.get_check_field(package.author_name),
            "author_email": PackageService.get_check_field(package.author_email),
            "description": PackageService.get_check_field(package.description),
        }
        return package
    
    @staticmethod
    def get_check_field(field):
        return field if field else ''


class SetupPyGenerator:
    """
    This class creates a file
    """

    def __init__(self, filename, meta_data: dict):
        self.file = pathlib.Path(filename)
        self.meta_data = meta_data

    def generate_file_py(self) -> None:
        self.file.touch(exist_ok=True)
        file_data: str = f"""from setuptools import setup

            
setup(
    name="{self.meta_data.get('name', '')}",
    version="{self.meta_data.get('version', '0.1.0')}",
    packages="{self.meta_data.get('packages', '')}",
    url="{self.meta_data.get('url', '')}",
    license="{self.meta_data.get('license', '')}",
    author="{self.meta_data.get('author', '')}",
    author_email="{self.meta_data.get('author_email', '')}",
    description="{self.meta_data.get('description', '')}",
)
"""
        self.file.write_text(
            file_data
        )
