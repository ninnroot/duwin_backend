from .main import schema
from graphql.utils import schema_printer


def generate_schema():
    x = open("schema.graphql", "w")

    x.write(schema_printer.print_schema(schema))
    x.close()
