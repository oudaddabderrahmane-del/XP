def generate_cooling() -> list[dict]:
    products = []

    def add(subcat, name, brand, model, price, specs, compat):
        products.append({"name": name, "brand": brand, "category": "Cooling", "subcategory_slug": subcat, "manufacturer": brand, "model": model, "price": price, "specs": specs, "compatibility": compat})

    # Air coolers
    add("cooling-air", "Noctua NH-D15 Chromax Black", "Noctua", "NH-D15", 109.99,
        {"type": "Air Cooler", "form_factor": "Dual Tower", "fan_size": "140mm x2", "height": "165mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "250W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "165mm"})
    add("cooling-air", "Noctua NH-U12A Chromax", "Noctua", "NH-U12A", 99.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "120mm x2", "height": "158mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "200W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "158mm"})
    add("cooling-air", "Noctua NH-U12S", "Noctua", "NH-U12S", 69.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "120mm", "height": "158mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "180W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "158mm"})
    add("cooling-air", "Noctua NH-L9x65", "Noctua", "NH-L9x65", 59.99,
        {"type": "Air Cooler", "form_factor": "Low Profile", "fan_size": "92mm", "height": "65mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "95W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "65mm"})
    add("cooling-air", "be quiet! Dark Rock Pro 5", "be quiet!", "Dark Rock Pro 5", 99.99,
        {"type": "Air Cooler", "form_factor": "Dual Tower", "fan_size": "135mm + 120mm", "height": "168mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "270W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "168mm"})
    add("cooling-air", "be quiet! Dark Rock 5", "be quiet!", "Dark Rock 5", 69.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "135mm", "height": "159mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "200W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "159mm"})
    add("cooling-air", "be quiet! Shadow Rock 3", "be quiet!", "Shadow Rock 3", 49.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "120mm", "height": "161mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "190W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "161mm"})
    add("cooling-air", "Deepcool AK620", "Deepcool", "AK620", 64.99,
        {"type": "Air Cooler", "form_factor": "Dual Tower", "fan_size": "120mm x2", "height": "157mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "260W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "157mm"})
    add("cooling-air", "Deepcool AK400", "Deepcool", "AK400", 34.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "120mm", "height": "155mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "180W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "155mm"})
    add("cooling-air", "Cooler Master Hyper 212 Halo", "Cooler Master", "Hyper 212 Halo", 49.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "120mm", "height": "152mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "180W", "rgb": True},
        {"socket": "LGA1700, AM5, AM4", "max_height": "152mm"})
    add("cooling-air", "Thermalright Peerless Assassin 120", "Thermalright", "Peerless Assassin 120", 39.99,
        {"type": "Air Cooler", "form_factor": "Dual Tower", "fan_size": "120mm x2", "height": "157mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "250W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "157mm"})
    add("cooling-air", "Thermalright Phantom Spirit 120", "Thermalright", "Phantom Spirit 120", 37.99,
        {"type": "Air Cooler", "form_factor": "Dual Tower", "fan_size": "120mm x2", "height": "154mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "260W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "154mm"})
    add("cooling-air", "Arctic Freezer 34 eSports", "Arctic", "Freezer 34 eSports", 39.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "120mm", "height": "157mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "200W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "157mm"})
    add("cooling-air", "Arctic Freezer 36", "Arctic", "Freezer 36", 34.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "120mm", "height": "159mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "180W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "159mm"})

    # AIO Liquid Coolers
    for args in [
        ("Corsair H150i Elite Capellix XT 360mm", "Corsair", "H150i Elite Capellix XT", 179.99, "360mm", "120mm x3", True),
        ("Corsair H100i Elite Capellix XT 240mm", "Corsair", "H100i Elite Capellix XT", 149.99, "240mm", "120mm x2", True),
        ("Corsair H170i Elite 420mm", "Corsair", "H170i Elite", 229.99, "420mm", "140mm x3", True),
        ("Corsair H60x 120mm", "Corsair", "H60x", 79.99, "120mm", "120mm", False),
        ("Corsair H100x 240mm", "Corsair", "H100x", 99.99, "240mm", "120mm x2", False),
        ("Corsair H150x 360mm", "Corsair", "H150x", 149.99, "360mm", "120mm x3", False),
        ("NZXT Kraken X73 360mm", "NZXT", "Kraken X73", 199.99, "360mm", "120mm x3", True),
        ("NZXT Kraken X63 280mm", "NZXT", "Kraken X63", 169.99, "280mm", "140mm x2", True),
        ("NZXT Kraken X53 240mm", "NZXT", "Kraken X53", 139.99, "240mm", "120mm x2", True),
        ("NZXT Kraken Elite 360mm", "NZXT", "Kraken Elite 360", 279.99, "360mm", "120mm x3", True),
        ("NZXT Kraken 240", "NZXT", "Kraken 240", 139.99, "240mm", "120mm x2", True),
        ("Arctic Liquid Freezer III 420mm", "Arctic", "Liquid Freezer III 420", 159.99, "420mm", "140mm x3", False),
        ("Arctic Liquid Freezer III 360mm", "Arctic", "Liquid Freezer III 360", 134.99, "360mm", "120mm x3", False),
        ("Arctic Liquid Freezer III 280mm", "Arctic", "Liquid Freezer III 280", 119.99, "280mm", "140mm x2", False),
        ("Arctic Liquid Freezer III 240mm", "Arctic", "Liquid Freezer III 240", 99.99, "240mm", "120mm x2", False),
        ("Cooler Master MasterLiquid ML360 Atmos", "Cooler Master", "ML360 Atmos", 149.99, "360mm", "120mm x3", True),
        ("Cooler Master MasterLiquid ML240 Atmos", "Cooler Master", "ML240 Atmos", 119.99, "240mm", "120mm x2", True),
        ("Cooler Master PL240 Flux", "Cooler Master", "PL240 Flux", 99.99, "240mm", "120mm x2", True),
        ("Lian Li Galahad II Trinity 360mm", "Lian Li", "Galahad II Trinity 360", 149.99, "360mm", "120mm x3", True),
        ("Lian Li Galahad II Trinity 240mm", "Lian Li", "Galahad II Trinity 240", 129.99, "240mm", "120mm x2", True),
    ]:
        name, brand, model, price, rad, fans, rgb = args
        add("cooling-aio", name, brand, model, price,
            {"type": "AIO Liquid Cooler", "radiator_size": rad, "fan_size": fans, "socket_support": "LGA1700, LGA1200, AM5, AM4", "rgb": rgb, "pump_speed": "2000 RPM"},
            {"socket": "LGA1700, AM5, AM4", "radiator_support": rad})

    # Custom Water Cooling
    add("cooling-custom-water", "EK-Quantum Surface P360M", "EKWB", "Quantum Surface P360M", 129.99,
        {"type": "Custom Water Cooling Radiator", "material": "Copper/Brass", "form_factor": "360mm", "fpi": 22, "port_threads": "G1/4"},
        {"form_factor": "360mm", "thread": "G1/4"})
    add("cooling-custom-water", "EK-Quantum Surface P280M", "EKWB", "Quantum Surface P280M", 99.99,
        {"type": "Custom Water Cooling Radiator", "material": "Copper/Brass", "form_factor": "280mm", "fpi": 22, "port_threads": "G1/4"},
        {"form_factor": "280mm", "thread": "G1/4"})
    add("cooling-custom-water", "EK-Quantum Surface X360M", "EKWB", "Quantum Surface X360M", 149.99,
        {"type": "Custom Water Cooling Radiator", "material": "Copper/Brass", "form_factor": "360mm", "fpi": 16, "port_threads": "G1/4"},
        {"form_factor": "360mm", "thread": "G1/4"})
    add("cooling-custom-water", "EK-Quantum Velocity CPU Block", "EKWB", "Quantum Velocity", 199.99,
        {"type": "Custom Water Cooling CPU Block", "material": "Acetal/Nickel", "socket_support": "LGA1700, LGA1200, AM5, AM4", "rgb": True},
        {"socket": "LGA1700, AM5, AM4"})
    add("cooling-custom-water", "EK-Quantum Kinetic FLT 120 Pump/Res", "EKWB", "Quantum Kinetic FLT 120", 129.99,
        {"type": "Custom Water Cooling Pump/Reservoir", "material": "Acrylic", "form_factor": "120mm", "pump_speed": "4800 RPM", "rgb": True},
        {"form_factor": "120mm"})
    add("cooling-custom-water", "Corsair Hydro X XD5 Pump/Res", "Corsair", "Hydro X XD5", 159.99,
        {"type": "Custom Water Cooling Pump/Reservoir", "material": "Acetal/Acrylic", "pump_speed": "5000 RPM", "rgb": True},
        {"form_factor": "120mm"})
    add("cooling-custom-water", "Corsair Hydro X XR5 360mm Radiator", "Corsair", "Hydro X XR5", 89.99,
        {"type": "Custom Water Cooling Radiator", "material": "Copper", "form_factor": "360mm", "fpi": 20, "port_threads": "G1/4"},
        {"form_factor": "360mm", "thread": "G1/4"})

    # Additional Air Coolers
    add("cooling-air", "Noctua NH-D12L", "Noctua", "NH-D12L", 79.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "120mm", "height": "145mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "180W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "145mm"})
    add("cooling-air", "Noctua NH-L9i", "Noctua", "NH-L9i", 49.99,
        {"type": "Air Cooler", "form_factor": "Low Profile", "fan_size": "92mm", "height": "37mm", "socket_support": "LGA1700, LGA1200", "tdp_rating": "95W"},
        {"socket": "LGA1700, LGA1200", "max_height": "37mm"})
    add("cooling-air", "be quiet! Pure Rock 2", "be quiet!", "Pure Rock 2", 44.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "120mm", "height": "155mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "150W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "155mm"})
    add("cooling-air", "Cooler Master Hyper 620S", "Cooler Master", "Hyper 620S", 44.99,
        {"type": "Air Cooler", "form_factor": "Dual Tower", "fan_size": "120mm x2", "height": "156mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "230W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "156mm"})
    add("cooling-air", "ID-Cooling SE-226-XT", "ID-Cooling", "SE-226-XT", 39.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "120mm", "height": "156mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "200W", "rgb": True},
        {"socket": "LGA1700, AM5, AM4", "max_height": "156mm"})
    add("cooling-air", "Scythe Fuma 3", "Scythe", "Fuma 3", 59.99,
        {"type": "Air Cooler", "form_factor": "Dual Tower", "fan_size": "120mm x2", "height": "154mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "250W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "154mm"})
    add("cooling-air", "Vetroo V5", "Vetroo", "V5", 29.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "120mm", "height": "156mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "180W", "rgb": True},
        {"socket": "LGA1700, AM5, AM4", "max_height": "156mm"})

    # Additional AIOs
    add("cooling-aio", "MSI MAG CoreLiquid M360", "MSI", "MAG CoreLiquid M360", 139.99,
        {"type": "AIO Liquid Cooler", "radiator_size": "360mm", "fan_size": "120mm x3", "socket_support": "LGA1700, LGA1200, AM5, AM4", "rgb": True, "pump_speed": "2000 RPM"},
        {"socket": "LGA1700, AM5, AM4", "radiator_support": "360mm"})
    add("cooling-aio", "MSI MAG CoreLiquid M240", "MSI", "MAG CoreLiquid M240", 109.99,
        {"type": "AIO Liquid Cooler", "radiator_size": "240mm", "fan_size": "120mm x2", "socket_support": "LGA1700, LGA1200, AM5, AM4", "rgb": True, "pump_speed": "2000 RPM"},
        {"socket": "LGA1700, AM5, AM4", "radiator_support": "240mm"})
    add("cooling-aio", "Deepcool LS720", "Deepcool", "LS720", 119.99,
        {"type": "AIO Liquid Cooler", "radiator_size": "360mm", "fan_size": "120mm x3", "socket_support": "LGA1700, LGA1200, AM5, AM4", "rgb": True, "pump_speed": "2000 RPM"},
        {"socket": "LGA1700, AM5, AM4", "radiator_support": "360mm"})
    add("cooling-aio", "Deepcool LS520", "Deepcool", "LS520", 94.99,
        {"type": "AIO Liquid Cooler", "radiator_size": "240mm", "fan_size": "120mm x2", "socket_support": "LGA1700, LGA1200, AM5, AM4", "rgb": True, "pump_speed": "2000 RPM"},
        {"socket": "LGA1700, AM5, AM4", "radiator_support": "240mm"})
    add("cooling-aio", "Thermaltake TOUGHLIQUID Ultra 360", "Thermaltake", "TOUGHLIQUID Ultra 360", 269.99,
        {"type": "AIO Liquid Cooler", "radiator_size": "360mm", "fan_size": "120mm x3", "socket_support": "LGA1700, LGA1200, AM5, AM4", "rgb": True, "display": "2.1 LCD"},
        {"socket": "LGA1700, AM5, AM4", "radiator_support": "360mm"})
    add("cooling-aio", "Alphacool Eisbaer Aurora 360", "Alphacool", "Eisbaer Aurora 360", 159.99,
        {"type": "AIO Liquid Cooler", "radiator_size": "360mm", "fan_size": "120mm x3", "socket_support": "LGA1700, LGA1200, AM5, AM4", "rgb": True, "pump_speed": "2200 RPM"},
        {"socket": "LGA1700, AM5, AM4", "radiator_support": "360mm"})

    # Additional Custom Water
    add("cooling-custom-water", "Watercool Heatkiller IV Pro CPU Block", "Watercool", "Heatkiller IV Pro", 149.99,
        {"type": "Custom Water Cooling CPU Block", "material": "Nickel/Acetal", "socket_support": "LGA1700, LGA1200, AM5, AM4", "rgb": True},
        {"socket": "LGA1700, AM5, AM4"})
    add("cooling-custom-water", "Alphacool Core 1 CPU Block", "Alphacool", "Core 1", 109.99,
        {"type": "Custom Water Cooling CPU Block", "material": "PMMA/Nickel", "socket_support": "LGA1700, LGA1200, AM5, AM4"},
        {"socket": "LGA1700, AM5, AM4"})
    add("cooling-custom-water", "Aquacomputer cuplex Kryos NEXT", "Aquacomputer", "cuplex Kryos NEXT", 169.99,
        {"type": "Custom Water Cooling CPU Block", "material": "Acetal/Nickel", "socket_support": "LGA1700, LGA1200, AM5, AM4", "rgb": True},
        {"socket": "LGA1700, AM5, AM4"})
    add("cooling-custom-water", "Alphacool Eisblock Aurora GPU Block", "Alphacool", "Eisblock Aurora", 159.99,
        {"type": "Custom Water Cooling GPU Block", "material": "Nickel/Acetal", "socket_support": "NVIDIA RTX 40/50 Series", "rgb": True},
        {"socket": "NVIDIA RTX 40/50 Series"})

    # More air coolers
    add("cooling-air", "Noctua NH-U9S Chromax", "Noctua", "NH-U9S", 64.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "92mm", "height": "125mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "150W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "125mm"})
    add("cooling-air", "be quiet! Shadow Rock LP", "be quiet!", "Shadow Rock LP", 49.99,
        {"type": "Air Cooler", "form_factor": "Low Profile", "fan_size": "120mm", "height": "97mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "150W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "97mm"})
    add("cooling-air", "Deepcool AK500", "Deepcool", "AK500", 54.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "120mm", "height": "158mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "220W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "158mm"})
    add("cooling-air", "Deepcool AG400", "Deepcool", "AG400", 24.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "120mm", "height": "150mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "150W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "150mm"})
    add("cooling-air", "Thermalright Assassin X 120 Refined SE", "Thermalright", "Assassin X 120", 24.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "120mm", "height": "154mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "180W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "154mm"})
    add("cooling-air", "Cooler Master Hyper 212 Spectrum V3", "Cooler Master", "Hyper 212 Spectrum V3", 44.99,
        {"type": "Air Cooler", "form_factor": "Single Tower", "fan_size": "120mm", "height": "155mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "180W", "rgb": True},
        {"socket": "LGA1700, AM5, AM4", "max_height": "155mm"})
    add("cooling-air", "Corsair A115", "Corsair", "A115", 99.99,
        {"type": "Air Cooler", "form_factor": "Dual Tower", "fan_size": "140mm x2", "height": "168mm", "socket_support": "LGA1700, LGA1200, AM5, AM4", "tdp_rating": "260W"},
        {"socket": "LGA1700, AM5, AM4", "max_height": "168mm"})
    # More AIOs
    add("cooling-aio", "MSI MEG CoreLiquid S360", "MSI", "MEG CoreLiquid S360", 199.99,
        {"type": "AIO Liquid Cooler", "radiator_size": "360mm", "fan_size": "120mm x3", "socket_support": "LGA1700, LGA1200, AM5, AM4", "rgb": True, "display": "2.4 LCD"},
        {"socket": "LGA1700, AM5, AM4", "radiator_support": "360mm"})
    add("cooling-aio", "Corsair H150i RGB Elite", "Corsair", "H150i RGB Elite", 169.99,
        {"type": "AIO Liquid Cooler", "radiator_size": "360mm", "fan_size": "120mm x3", "socket_support": "LGA1700, LGA1200, AM5, AM4", "rgb": True, "pump_speed": "2000 RPM"},
        {"socket": "LGA1700, AM5, AM4", "radiator_support": "360mm"})
    add("cooling-aio", "NZXT Kraken X53 240mm RGB", "NZXT", "Kraken X53 RGB", 159.99,
        {"type": "AIO Liquid Cooler", "radiator_size": "240mm", "fan_size": "120mm x2", "socket_support": "LGA1700, LGA1200, AM5, AM4", "rgb": True, "pump_speed": "2000 RPM"},
        {"socket": "LGA1700, AM5, AM4", "radiator_support": "240mm"})
    add("cooling-aio", "Cooler Master MasterLiquid PL360 Flux", "Cooler Master", "PL360 Flux", 129.99,
        {"type": "AIO Liquid Cooler", "radiator_size": "360mm", "fan_size": "120mm x3", "socket_support": "LGA1700, LGA1200, AM5, AM4", "rgb": True, "pump_speed": "2000 RPM"},
        {"socket": "LGA1700, AM5, AM4", "radiator_support": "360mm"})
    add("cooling-aio", "Lian Li Galahad II LCD 360mm", "Lian Li", "Galahad II LCD 360", 249.99,
        {"type": "AIO Liquid Cooler", "radiator_size": "360mm", "fan_size": "120mm x3", "socket_support": "LGA1700, LGA1200, AM5, AM4", "rgb": True, "display": "2.88 LCD"},
        {"socket": "LGA1700, AM5, AM4", "radiator_support": "360mm"})
    # More custom water
    add("cooling-custom-water", "EK-Quantum Vector² FE RTX 4090 GPU Block", "EKWB", "Vector² FE RTX 4090", 299.99,
        {"type": "Custom Water Cooling GPU Block", "material": "Nickel/Acetal", "socket_support": "NVIDIA RTX 4090 FE", "rgb": True},
        {"socket": "NVIDIA RTX 4090 FE"})
    add("cooling-custom-water", "Corsair Hydro X XD3 Pump/Res", "Corsair", "Hydro X XD3", 124.99,
        {"type": "Custom Water Cooling Pump/Reservoir", "material": "Acetal", "pump_speed": "4800 RPM", "rgb": True},
        {"form_factor": "120mm"})
    add("cooling-custom-water", "Watercool MO-RA3 420 Radiator", "Watercool", "MO-RA3 420", 299.99,
        {"type": "Custom Water Cooling Radiator", "material": "Copper", "form_factor": "External 420mm", "fpi": 10, "port_threads": "G1/4"},
        {"form_factor": "External", "thread": "G1/4"})

    return products
