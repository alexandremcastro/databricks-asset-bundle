def get_catalog(project: str) -> str:
    """
    Returns the catalog name for the given projects.

    Args:
        project (str): The project identifier.

    Returns:
        str: The catalog name associated with the project.
    """
    if project == "nyc-analysis":
        catalog: str = "samples"

        return catalog
    

def get_schema(project: str) -> str:
    """
    Returns the schema name for the given project.

    Args:
        project (str): The project identifier.

    Returns:
        str: The schema name associated with the project.
    """
    if project == "nyc-analysis":
        schema: str = "nyctaxi"

        return schema
    

def get_table(project: str) -> str:
    """
    Returns the table name for the given project.

    Args:
        project (str): The project identifier.

    Returns:
        str: The table name associated with the project.
    """
    if project == "nyc-analysis":
        table: str = "trips"

        return table
    
def get_path(project: str) -> str:
    """
    Constructs the fully qualified table path for the given project.

    Args:
        project (str): The project identifier.

    Returns:
        str: The fully qualified table path in the format 'catalog.schema.table'.
    """
    catalog: str = get_catalog(project)
    schema: str = get_schema(project)
    table: str = get_table(project)

    path: str = f"{catalog}.{schema}.{table}"

    return path
