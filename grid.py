"""Disposable grid-metadata fixture."""
def normalize_grid(metadata):
    """Return the canonical grid projection, raising ValueError if invalid."""
    if not isinstance(metadata, dict) or 'grid' not in metadata:
        raise ValueError('metadata must contain grid')
    grid = metadata['grid']
    fields = ('rows', 'columns', 'version')
    if not isinstance(grid, dict) or set(grid) != set(fields):
        raise ValueError('grid must contain exactly rows, columns and version')
    for field in fields:
        value = grid[field]
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f'grid {field} must be a positive integer')
    return {field: grid[field] for field in fields}
