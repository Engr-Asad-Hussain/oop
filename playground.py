from abc import ABC, abstractmethod
from math import pi
from pathlib import Path
from typing import Any
from zipfile import ZipFile


# Example of Single-Responsibility-Principle by Robert C. Martin
class FileManager:
    encoding = "utf-8"

    def __init__(self, filename: str) -> None:
        self.path = Path(filename)

    def read(self):
        return self.path.read_text(self.encoding)

    def write(self, data: str):
        return self.path.write_text(data, self.encoding)


class ZipFileManager:
    def __init__(self, filename: str) -> None:
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()


# Example of Open-Close-Principle by Bertrand Meyer
class Shape(ABC):
    def __init__(self, shape_type: str) -> None:
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: int, height: int) -> None:
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: int) -> None:
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self) -> float:
        return pi * self.radius**2


class Square(Shape):
    def __init__(self, side: int) -> None:
        super().__init__("Square")
        self.side = side

    def calculate_area(self) -> float:
        return self.side**2


# Example of Liskov-Substitution-Principle by Barbara Liskov
class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height


class Square(Shape):
    def __init__(self, side: int) -> None:
        self.side = side

    def calculate_area(self) -> float:
        return self.side**2


def total_area(shapes: list[Square | Rectangle]):
    return sum([shape.calculate_area() for shape in shapes])


# Example of Interface-Segregation-Principle by Uncle Bob
class Print(ABC):
    @abstractmethod
    def print(self):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self):
        pass


class Scan(ABC):
    @abstractmethod
    def scan(self):
        pass


class OldPrinter(Print):
    def print(self):
        print("Printing prints by OldPrinter")


class ModernPrinter(Print, Fax, Scan):
    def print(self):
        print("Printing prints by ModernPrinter")

    def fax(self):
        print("Printing faxs by ModernPrinter")

    def scan(self):
        print("Printing scans by ModernPrinter")


# Example of Dependency-Inversion-Principle by Uncle Bob
class DataSource(ABC):
    @abstractmethod
    def get_data(self, user_id: int) -> dict[str, Any]:
        pass


class Backend(DataSource):
    def get_data(self, user_id: int) -> dict[str, Any]:
        return {"userId": user_id, "items": []}


class ThirdPartyLibrary(DataSource):
    def get_data(self, user_id: int) -> dict[str, Any]:
        return {"userId": user_id, "items": ["distance", "speed", "velocity"]}


class Frontend:
    def __init__(self, resource: DataSource) -> None:
        self.resource = resource

    def display_data(self, user_id: int = 2021) -> dict[str, Any]:
        return self.resource.get_data(user_id)
