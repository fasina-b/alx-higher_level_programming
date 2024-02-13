#!/usr/bin/python3
"""Defines a base class."""
import json
import csv
import turtle


class Base:
    """Represent the base model for project classes.

    This serves as the foundation for other classes.

    Attributes:
        __nb_objects (int): The total number of instances created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identity of the new instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serialize a list of dictionaries to JSON.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON representation of the list.
        """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON serialization of objects to a file.

        Args:
            list_objs (list): A list of Base instances.
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            if list_objs:
                json_data = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(json_data))
            else:
                file.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """Deserialize a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON representation of a list of dictionaries.

        Returns:
            list: Deserialized list of dictionaries.
        """
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """Create an instance from a dictionary.

        Args:
            **dictionary (dict): Key/value pairs of attributes.

        Returns:
            Base: An instance of Base with attributes set.
        """
        instance = cls.__new__(cls)
        if cls.__name__ == "Rectangle":
            instance.__init__(1, 1)
        else:
            instance.__init__(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file.

        Returns:
            list: List of instances loaded from the file.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as file:
                json_data = Base.from_json_string(file.read())
                return [cls.create(**data) for data in json_data]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write CSV serialization of objects to a file.

        Args:
            list_objs (list): A list of Base instances.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.csv_fieldnames())
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Load instances from a CSV file.

        Returns:
            list: List of instances loaded from the file.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                return [cls.create(**row) for row in reader]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects.
            list_squares (list): A list of Square objects.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        for obj_list, color in [(list_rectangles, "#ffffff"),
                                (list_squares, "#b5e3d8")]:
            turt.color(color)
            for obj in obj_list:
                turt.showturtle()
                turt.up()
                turt.goto(obj.x, obj.y)
                turt.down()
                for _ in range(2):
                    turt.forward(obj.width)
                    turt.left(90)
                    turt.forward(obj.height)
                    turt.left(90)
                turt.hideturtle()

        turtle.exitonclick()
