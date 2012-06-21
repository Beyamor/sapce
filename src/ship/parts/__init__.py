from types import PART_TYPES

def make_part( context, part_data, position ):

	if part_data is not None and part_data.name in PART_TYPES:
		return PART_TYPES[part_data.name]( context, part_data, position )
	else:
		return None
