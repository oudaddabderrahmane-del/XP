def generate_cases() -> list[dict]:
    products = []

    def add(subcat, name, brand, model, price, specs, compat):
        products.append({"name": name, "brand": brand, "category": "Case", "subcategory_slug": subcat, "manufacturer": brand, "model": model, "price": price, "specs": specs, "compatibility": compat})

    # Mid Tower
    add("cases-mid-tower", "Corsair 4000D Airflow", "Corsair", "4000D Airflow", 89.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "psu_length_max": "220mm", "gpu_length_max": "360mm", "cooler_height_max": "170mm", "fan_slots": "6x 120mm / 4x 140mm", "drive_bays": "2x 3.5, 2x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Corsair 4000X RGB", "Corsair", "4000X RGB", 109.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "360mm", "cooler_height_max": "170mm", "fan_slots": "6x 120mm / 4x 140mm", "drive_bays": "2x 3.5, 2x 2.5", "rgb": True},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Corsair 5000D Airflow", "Corsair", "5000D Airflow", 149.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "420mm", "cooler_height_max": "170mm", "fan_slots": "10x 120mm / 4x 140mm", "drive_bays": "2x 3.5, 4x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Corsair 5000X RGB", "Corsair", "5000X RGB", 179.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "420mm", "cooler_height_max": "170mm", "fan_slots": "10x 120mm / 4x 140mm", "drive_bays": "2x 3.5, 4x 2.5", "rgb": True},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "NZXT H7 Flow", "NZXT", "H7 Flow", 129.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "400mm", "cooler_height_max": "185mm", "fan_slots": "3x 120mm / 3x 140mm", "drive_bays": "2x 3.5, 2x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "NZXT H5 Flow", "NZXT", "H5 Flow", 94.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "365mm", "cooler_height_max": "165mm", "fan_slots": "2x 140mm / 1x 120mm", "drive_bays": "1x 3.5, 1x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "NZXT H5 Elite", "NZXT", "H5 Elite", 124.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "365mm", "cooler_height_max": "165mm", "fan_slots": "2x 140mm / 1x 120mm", "drive_bays": "1x 3.5, 1x 2.5", "rgb": True},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Lian Li O11 Dynamic EVO", "Lian Li", "O11 Dynamic EVO", 149.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "420mm", "cooler_height_max": "155mm", "fan_slots": "10x 120mm / 4x 140mm", "drive_bays": "2x 3.5, 3x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Lian Li O11 Dynamic Mini", "Lian Li", "O11 Dynamic Mini", 119.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "395mm", "cooler_height_max": "170mm", "fan_slots": "7x 120mm", "drive_bays": "1x 3.5, 2x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Lian Li Lancool 207", "Lian Li", "Lancool 207", 89.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "390mm", "cooler_height_max": "172mm", "fan_slots": "6x 120mm / 3x 140mm", "drive_bays": "2x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Lian Li Lancool 216", "Lian Li", "Lancool 216", 99.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "392mm", "cooler_height_max": "176mm", "fan_slots": "7x 120mm / 3x 140mm", "drive_bays": "2x 3.5, 2x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Fractal Design Pop Air", "Fractal Design", "Pop Air", 89.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "380mm", "cooler_height_max": "170mm", "fan_slots": "5x 120mm / 3x 140mm", "drive_bays": "2x 3.5, 2x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Fractal Design North", "Fractal Design", "North", 129.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "355mm", "cooler_height_max": "171mm", "fan_slots": "5x 120mm / 3x 140mm", "drive_bays": "2x 3.5, 2x 2.5", "material": "Walnut + Steel"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Fractal Design Meshify 2", "Fractal Design", "Meshify 2", 99.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "395mm", "cooler_height_max": "185mm", "fan_slots": "9x 120mm / 7x 140mm", "drive_bays": "2x 3.5, 4x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Fractal Design Define 7", "Fractal Design", "Define 7", 174.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "395mm", "cooler_height_max": "185mm", "fan_slots": "7x 120mm / 7x 140mm", "drive_bays": "6x 3.5, 2x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Cooler Master TD500 Mesh", "Cooler Master", "TD500 Mesh", 84.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "410mm", "cooler_height_max": "165mm", "fan_slots": "7x 120mm / 4x 140mm", "drive_bays": "2x 3.5, 2x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Cooler Master MasterBox Q300L", "Cooler Master", "MasterBox Q300L", 39.99,
        {"form_factor": "Mid Tower", "motherboard_support": "Micro ATX, Mini ITX", "gpu_length_max": "360mm", "cooler_height_max": "156mm", "fan_slots": "5x 120mm", "drive_bays": "1x 3.5, 1x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Phanteks Eclipse G360A", "Phanteks", "Eclipse G360A", 69.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "400mm", "cooler_height_max": "165mm", "fan_slots": "6x 120mm / 3x 140mm", "drive_bays": "2x 3.5, 2x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Phanteks Eclipse P400A Digital", "Phanteks", "Eclipse P400A Digital", 79.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "420mm", "cooler_height_max": "160mm", "fan_slots": "7x 120mm / 4x 140mm", "drive_bays": "2x 3.5, 3x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Phanteks Eclipse G500A", "Phanteks", "Eclipse G500A", 109.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "435mm", "cooler_height_max": "185mm", "fan_slots": "11x 120mm / 7x 140mm", "drive_bays": "2x 3.5, 5x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Phanteks NV5", "Phanteks", "NV5", 99.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "440mm", "cooler_height_max": "180mm", "fan_slots": "8x 120mm / 3x 140mm", "drive_bays": "2x 3.5, 3x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Phanteks NV7", "Phanteks", "NV7", 249.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "480mm", "cooler_height_max": "180mm", "fan_slots": "14x 120mm / 10x 140mm", "drive_bays": "2x 3.5, 7x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "be quiet! Pure Base 500DX", "be quiet!", "Pure Base 500DX", 99.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "369mm", "cooler_height_max": "165mm", "fan_slots": "5x 120mm / 4x 140mm", "drive_bays": "2x 3.5, 4x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "be quiet! Silent Base 802", "be quiet!", "Silent Base 802", 149.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "398mm", "cooler_height_max": "185mm", "fan_slots": "5x 120mm / 5x 140mm", "drive_bays": "2x 3.5, 5x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "ASUS ROG Helios", "ASUS", "ROG Helios", 299.99,
        {"form_factor": "Mid Tower", "motherboard_support": "E-ATX, ATX, Micro ATX, Mini ITX", "gpu_length_max": "450mm", "cooler_height_max": "190mm", "fan_slots": "9x 120mm / 6x 140mm", "drive_bays": "4x 3.5, 6x 2.5", "rgb": True},
        {"form_factor": "Mid Tower", "motherboard": "E-ATX, ATX, Micro ATX, Mini ITX"})

    # Full Tower
    add("cases-full-tower", "Fractal Design Meshify 2 XL", "Fractal Design", "Meshify 2 XL", 199.99,
        {"form_factor": "Full Tower", "motherboard_support": "E-ATX, ATX, Micro ATX, Mini ITX", "gpu_length_max": "470mm", "cooler_height_max": "185mm", "fan_slots": "11x 120mm / 8x 140mm", "drive_bays": "6x 3.5, 4x 2.5"},
        {"form_factor": "Full Tower", "motherboard": "E-ATX, ATX, Micro ATX, Mini ITX"})
    add("cases-full-tower", "Fractal Design Define 7 XL", "Fractal Design", "Define 7 XL", 219.99,
        {"form_factor": "Full Tower", "motherboard_support": "E-ATX, ATX, Micro ATX, Mini ITX", "gpu_length_max": "480mm", "cooler_height_max": "185mm", "fan_slots": "9x 120mm / 9x 140mm", "drive_bays": "8x 3.5, 4x 2.5"},
        {"form_factor": "Full Tower", "motherboard": "E-ATX, ATX, Micro ATX, Mini ITX"})
    add("cases-full-tower", "Corsair 7000D Airflow", "Corsair", "7000D Airflow", 199.99,
        {"form_factor": "Full Tower", "motherboard_support": "E-ATX, ATX, Micro ATX, Mini ITX", "gpu_length_max": "460mm", "cooler_height_max": "190mm", "fan_slots": "13x 120mm / 8x 140mm", "drive_bays": "3x 3.5, 6x 2.5"},
        {"form_factor": "Full Tower", "motherboard": "E-ATX, ATX, Micro ATX, Mini ITX"})
    add("cases-full-tower", "Corsair 7000X RGB", "Corsair", "7000X RGB", 249.99,
        {"form_factor": "Full Tower", "motherboard_support": "E-ATX, ATX, Micro ATX, Mini ITX", "gpu_length_max": "460mm", "cooler_height_max": "190mm", "fan_slots": "13x 120mm / 8x 140mm", "drive_bays": "3x 3.5, 6x 2.5", "rgb": True},
        {"form_factor": "Full Tower", "motherboard": "E-ATX, ATX, Micro ATX, Mini ITX"})
    add("cases-full-tower", "Lian Li O11 Dynamic EVO XL", "Lian Li", "O11 Dynamic EVO XL", 199.99,
        {"form_factor": "Full Tower", "motherboard_support": "E-ATX, ATX, Micro ATX, Mini ITX", "gpu_length_max": "480mm", "cooler_height_max": "195mm", "fan_slots": "13x 120mm / 5x 140mm", "drive_bays": "2x 3.5, 4x 2.5"},
        {"form_factor": "Full Tower", "motherboard": "E-ATX, ATX, Micro ATX, Mini ITX"})
    add("cases-full-tower", "NZXT H9 Flow", "NZXT", "H9 Flow", 149.99,
        {"form_factor": "Full Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "435mm", "cooler_height_max": "185mm", "fan_slots": "10x 120mm / 4x 140mm", "drive_bays": "2x 3.5, 2x 2.5"},
        {"form_factor": "Full Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-full-tower", "NZXT H9 Elite", "NZXT", "H9 Elite", 189.99,
        {"form_factor": "Full Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "435mm", "cooler_height_max": "185mm", "fan_slots": "10x 120mm / 4x 140mm", "drive_bays": "2x 3.5, 2x 2.5", "rgb": True},
        {"form_factor": "Full Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-full-tower", "Phanteks Enthoo Pro 2", "Phanteks", "Enthoo Pro 2", 149.99,
        {"form_factor": "Full Tower", "motherboard_support": "E-ATX, ATX, Micro ATX, Mini ITX", "gpu_length_max": "490mm", "cooler_height_max": "200mm", "fan_slots": "13x 120mm / 9x 140mm", "drive_bays": "4x 3.5, 11x 2.5"},
        {"form_factor": "Full Tower", "motherboard": "E-ATX, ATX, Micro ATX, Mini ITX"})
    add("cases-full-tower", "be quiet! Dark Base Pro 901", "be quiet!", "Dark Base Pro 901", 269.99,
        {"form_factor": "Full Tower", "motherboard_support": "E-ATX, ATX, Micro ATX, Mini ITX", "gpu_length_max": "446mm", "cooler_height_max": "190mm", "fan_slots": "7x 120mm / 7x 140mm", "drive_bays": "3x 3.5, 8x 2.5", "rgb": True},
        {"form_factor": "Full Tower", "motherboard": "E-ATX, ATX, Micro ATX, Mini ITX"})

    # Mini ITX
    add("cases-mini-itx", "Cooler Master MasterBox NR200P", "Cooler Master", "MasterBox NR200P", 99.99,
        {"form_factor": "Mini ITX", "motherboard_support": "Mini ITX", "gpu_length_max": "330mm", "cooler_height_max": "155mm", "fan_slots": "5x 120mm", "drive_bays": "2x 3.5, 2x 2.5"},
        {"form_factor": "Mini ITX", "motherboard": "Mini ITX"})
    add("cases-mini-itx", "Cooler Master NR200P Max", "Cooler Master", "NR200P Max", 179.99,
        {"form_factor": "Mini ITX", "motherboard_support": "Mini ITX", "gpu_length_max": "330mm", "cooler_height_max": "105mm", "fan_slots": "3x 120mm", "drive_bays": "1x 3.5, 2x 2.5", "psu_included": "850W Gold SFX"},
        {"form_factor": "Mini ITX", "motherboard": "Mini ITX"})
    add("cases-mini-itx", "Fractal Design Terra", "Fractal Design", "Terra", 179.99,
        {"form_factor": "Mini ITX", "motherboard_support": "Mini ITX", "gpu_length_max": "322mm", "cooler_height_max": "77mm", "fan_slots": "2x 120mm", "material": "Anodized Aluminum + Walnut"},
        {"form_factor": "Mini ITX", "motherboard": "Mini ITX"})
    add("cases-mini-itx", "Fractal Design Ridge", "Fractal Design", "Ridge", 139.99,
        {"form_factor": "Mini ITX", "motherboard_support": "Mini ITX", "gpu_length_max": "335mm", "cooler_height_max": "70mm", "fan_slots": "4x 120mm", "drive_bays": "2x 3.5"},
        {"form_factor": "Mini ITX", "motherboard": "Mini ITX"})
    add("cases-mini-itx", "NZXT H1 V2", "NZXT", "H1 V2", 149.99,
        {"form_factor": "Mini ITX", "motherboard_support": "Mini ITX", "gpu_length_max": "324mm", "cooler_height_max": "70mm", "fan_slots": "1x 140mm", "psu_included": "750W Gold SFX"},
        {"form_factor": "Mini ITX", "motherboard": "Mini ITX"})
    add("cases-mini-itx", "Lian Li A4-H2O", "Lian Li", "A4-H2O", 149.99,
        {"form_factor": "Mini ITX", "motherboard_support": "Mini ITX", "gpu_length_max": "322mm", "cooler_height_max": "55mm", "fan_slots": "2x 120mm"},
        {"form_factor": "Mini ITX", "motherboard": "Mini ITX"})
    add("cases-mini-itx", "Corsair 2000D Airflow", "Corsair", "2000D Airflow", 99.99,
        {"form_factor": "Mini ITX", "motherboard_support": "Mini ITX", "gpu_length_max": "365mm", "cooler_height_max": "156mm", "fan_slots": "5x 120mm / 2x 140mm", "drive_bays": "1x 3.5, 2x 2.5"},
        {"form_factor": "Mini ITX", "motherboard": "Mini ITX"})
    add("cases-mini-itx", "Phanteks Evolv Shift 2", "Phanteks", "Evolv Shift 2", 109.99,
        {"form_factor": "Mini ITX", "motherboard_support": "Mini ITX", "gpu_length_max": "335mm", "cooler_height_max": "82mm", "fan_slots": "2x 120mm", "drive_bays": "2x 2.5"},
        {"form_factor": "Mini ITX", "motherboard": "Mini ITX"})
    add("cases-mini-itx", "Fractal Design Node 202", "Fractal Design", "Node 202", 79.99,
        {"form_factor": "Mini ITX", "motherboard_support": "Mini ITX", "gpu_length_max": "310mm", "cooler_height_max": "56mm", "fan_slots": "2x 120mm", "drive_bays": "1x 3.5, 2x 2.5"},
        {"form_factor": "Mini ITX", "motherboard": "Mini ITX"})

    # Additional Mid Tower
    add("cases-mid-tower", "Corsair 3500X", "Corsair", "3500X", 99.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "410mm", "cooler_height_max": "180mm", "fan_slots": "10x 120mm / 4x 140mm", "drive_bays": "2x 3.5, 3x 2.5", "rgb": True},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Corsair 2500X", "Corsair", "2500X", 89.99,
        {"form_factor": "Mid Tower", "motherboard_support": "Micro ATX, Mini ITX", "gpu_length_max": "400mm", "cooler_height_max": "170mm", "fan_slots": "8x 120mm / 3x 140mm", "drive_bays": "2x 3.5, 2x 2.5", "rgb": True},
        {"form_factor": "Mid Tower", "motherboard": "Micro ATX, Mini ITX"})
    add("cases-mid-tower", "NZXT H7 Elite", "NZXT", "H7 Elite", 179.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "400mm", "cooler_height_max": "185mm", "fan_slots": "3x 140mm / 1x 120mm", "drive_bays": "2x 3.5, 2x 2.5", "rgb": True},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "NZXT H5 Flow (2024)", "NZXT", "H5 Flow (2024)", 74.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "390mm", "cooler_height_max": "165mm", "fan_slots": "6x 120mm / 2x 140mm", "drive_bays": "1x 3.5, 1x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Lian Li O11 Vision", "Lian Li", "O11 Vision", 159.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "455mm", "cooler_height_max": "165mm", "fan_slots": "10x 120mm / 4x 140mm", "drive_bays": "2x 3.5, 3x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Lian Li Lancool 217", "Lian Li", "Lancool 217", 119.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "420mm", "cooler_height_max": "185mm", "fan_slots": "8x 120mm / 4x 140mm", "drive_bays": "2x 3.5, 3x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Fractal Design Pop XL", "Fractal Design", "Pop XL", 119.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "405mm", "cooler_height_max": "175mm", "fan_slots": "5x 120mm / 3x 140mm", "drive_bays": "4x 3.5, 2x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Fractal Design North XL", "Fractal Design", "North XL", 169.99,
        {"form_factor": "Mid Tower", "motherboard_support": "E-ATX, ATX, Micro ATX, Mini ITX", "gpu_length_max": "375mm", "cooler_height_max": "185mm", "fan_slots": "5x 140mm / 3x 120mm", "drive_bays": "2x 3.5, 2x 2.5", "material": "Walnut + Steel"},
        {"form_factor": "Mid Tower", "motherboard": "E-ATX, ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "Cooler Master MasterBox Q500L", "Cooler Master", "MasterBox Q500L", 49.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "410mm", "cooler_height_max": "160mm", "fan_slots": "6x 120mm / 4x 140mm", "drive_bays": "2x 3.5, 2x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    add("cases-mid-tower", "be quiet! Silent Base 501", "be quiet!", "Silent Base 501", 119.99,
        {"form_factor": "Mid Tower", "motherboard_support": "ATX, Micro ATX, Mini ITX", "gpu_length_max": "395mm", "cooler_height_max": "180mm", "fan_slots": "5x 120mm / 5x 140mm", "drive_bays": "2x 3.5, 4x 2.5"},
        {"form_factor": "Mid Tower", "motherboard": "ATX, Micro ATX, Mini ITX"})
    # Additional Full Tower
    add("cases-full-tower", "Lian Li O11 Dynamic EVO RGB", "Lian Li", "O11 Dynamic EVO RGB", 199.99,
        {"form_factor": "Full Tower", "motherboard_support": "E-ATX, ATX, Micro ATX, Mini ITX", "gpu_length_max": "460mm", "cooler_height_max": "195mm", "fan_slots": "13x 120mm / 5x 140mm", "drive_bays": "2x 3.5, 4x 2.5", "rgb": True},
        {"form_factor": "Full Tower", "motherboard": "E-ATX, ATX, Micro ATX, Mini ITX"})
    add("cases-full-tower", "Cooler Master Cosmos C700M", "Cooler Master", "Cosmos C700M", 299.99,
        {"form_factor": "Full Tower", "motherboard_support": "E-ATX, ATX, Micro ATX, Mini ITX", "gpu_length_max": "490mm", "cooler_height_max": "198mm", "fan_slots": "9x 120mm / 7x 140mm", "drive_bays": "4x 3.5, 7x 2.5", "rgb": True},
        {"form_factor": "Full Tower", "motherboard": "E-ATX, ATX, Micro ATX, Mini ITX"})
    # Additional Mini ITX
    add("cases-mini-itx", "Cooler Master MasterBox NR200", "Cooler Master", "MasterBox NR200", 79.99,
        {"form_factor": "Mini ITX", "motherboard_support": "Mini ITX", "gpu_length_max": "330mm", "cooler_height_max": "155mm", "fan_slots": "5x 120mm", "drive_bays": "2x 3.5, 2x 2.5"},
        {"form_factor": "Mini ITX", "motherboard": "Mini ITX"})
    add("cases-mini-itx", "Lian Li A3-mATX", "Lian Li", "A3-mATX", 69.99,
        {"form_factor": "Mini ITX", "motherboard_support": "Mini ITX, Micro ATX", "gpu_length_max": "400mm", "cooler_height_max": "165mm", "fan_slots": "7x 120mm / 2x 140mm", "drive_bays": "1x 3.5, 2x 2.5"},
        {"form_factor": "Mini ITX", "motherboard": "Mini ITX, Micro ATX"})
    add("cases-mini-itx", "HYTE Revolt 3", "HYTE", "Revolt 3", 129.99,
        {"form_factor": "Mini ITX", "motherboard_support": "Mini ITX", "gpu_length_max": "335mm", "cooler_height_max": "76mm", "fan_slots": "2x 140mm / 1x 120mm", "drive_bays": "2x 2.5"},
        {"form_factor": "Mini ITX", "motherboard": "Mini ITX"})
    add("cases-mini-itx", "SSUPD Meshlicious", "SSUPD", "Meshlicious", 119.99,
        {"form_factor": "Mini ITX", "motherboard_support": "Mini ITX", "gpu_length_max": "336mm", "cooler_height_max": "73mm", "fan_slots": "4x 120mm / 2x 140mm"},
        {"form_factor": "Mini ITX", "motherboard": "Mini ITX"})

    return products
