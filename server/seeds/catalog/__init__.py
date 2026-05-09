from seeds.catalog.cpus import generate_cpus
from seeds.catalog.gpus import generate_gpus
from seeds.catalog.ram import generate_ram
from seeds.catalog.storage import generate_storage
from seeds.catalog.motherboards import generate_motherboards
from seeds.catalog.psus import generate_psus
from seeds.catalog.cooling import generate_cooling
from seeds.catalog.cases import generate_cases


def generate_all_catalog() -> list[dict]:
    parts = []
    parts.extend(generate_cpus())
    parts.extend(generate_gpus())
    parts.extend(generate_ram())
    parts.extend(generate_storage())
    parts.extend(generate_motherboards())
    parts.extend(generate_psus())
    parts.extend(generate_cooling())
    parts.extend(generate_cases())
    return parts
