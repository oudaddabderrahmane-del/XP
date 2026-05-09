def generate_motherboards() -> list[dict]:
    products = []

    def add(subcat, name, brand, model, price, ff, socket, chipset, mem_slots, max_mem, pcie, m2, wifi, lan, mem_type):
        products.append({"name": name, "brand": brand, "category": "Motherboard", "subcategory_slug": subcat, "manufacturer": brand, "model": model, "price": price, "specs": {"form_factor": ff, "socket": socket, "chipset": chipset, "memory_slots": mem_slots, "max_memory": max_mem, "pcie_slots": pcie, "m2_slots": m2, "wifi": wifi or "None", "lan": lan}, "compatibility": {"socket": socket, "form_factor": ff, "memory_type": mem_type}})

    # Intel Z790
    for args in [
        ("motherboards-intel", "ASUS ROG Maximus Z790 Hero", "ASUS", "ROG Maximus Z790 Hero", 499.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASUS ROG Maximus Z790 Apex", "ASUS", "ROG Maximus Z790 Apex", 599.99, "ATX", "LGA1700", "Z790", 2, "96GB DDR5", "2x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASUS ROG STRIX Z790-E Gaming WiFi", "ASUS", "ROG STRIX Z790-E", 429.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASUS ROG STRIX Z790-F Gaming WiFi", "ASUS", "ROG STRIX Z790-F", 379.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "1x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASUS TUF Gaming Z790-Plus WiFi", "ASUS", "TUF Gaming Z790-Plus", 249.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "1x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASUS Prime Z790-A WiFi", "ASUS", "Prime Z790-A", 279.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "1x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "MSI MEG Z790 ACE", "MSI", "MEG Z790 ACE", 499.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "MSI MPG Z790 CARBON WiFi", "MSI", "MPG Z790 CARBON", 399.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "MSI MPG Z790 EDGE WiFi", "MSI", "MPG Z790 EDGE", 329.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "1x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "MSI MAG Z790 Tomahawk WiFi", "MSI", "MAG Z790 Tomahawk", 259.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "1x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "MSI Z790-P Pro", "MSI", "Z790-P Pro", 199.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, None, "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "Gigabyte Z790 AORUS Xtreme", "Gigabyte", "Z790 AORUS Xtreme", 749.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 7", "10Gb Ethernet", "DDR5"),
        ("motherboards-intel", "Gigabyte Z790 AORUS Master", "Gigabyte", "Z790 AORUS Master", 479.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "Gigabyte Z790 AORUS Elite AX", "Gigabyte", "Z790 AORUS Elite AX", 249.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "1x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "Gigabyte Z790 Gaming X AX", "Gigabyte", "Z790 Gaming X AX", 229.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASRock Z790 Taichi", "ASRock", "Z790 Taichi", 449.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASRock Z790 Steel Legend WiFi", "ASRock", "Z790 Steel Legend", 249.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASRock Z790 Pro RS", "ASRock", "Z790 Pro RS", 199.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, None, "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASRock Z790 LiveMixer", "ASRock", "Z790 LiveMixer", 229.99, "ATX", "LGA1700", "Z790", 4, "192GB DDR5", "1x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        # Z690
        ("motherboards-intel", "ASUS ROG Maximus Z690 Hero", "ASUS", "ROG Maximus Z690 Hero", 399.99, "ATX", "LGA1700", "Z690", 4, "128GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASUS ROG STRIX Z690-E Gaming WiFi", "ASUS", "ROG STRIX Z690-E", 329.99, "ATX", "LGA1700", "Z690", 4, "128GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "MSI MPG Z690 CARBON WiFi", "MSI", "MPG Z690 CARBON", 299.99, "ATX", "LGA1700", "Z690", 4, "128GB DDR5", "2x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "MSI MAG Z690 Tomahawk WiFi", "MSI", "MAG Z690 Tomahawk", 219.99, "ATX", "LGA1700", "Z690", 4, "128GB DDR5", "1x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "Gigabyte Z690 AORUS Elite AX", "Gigabyte", "Z690 AORUS Elite AX", 209.99, "ATX", "LGA1700", "Z690", 4, "128GB DDR5", "1x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASRock Z690 Extreme", "ASRock", "Z690 Extreme", 249.99, "ATX", "LGA1700", "Z690", 4, "128GB DDR5", "2x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        # B760
        ("motherboards-intel", "ASUS ROG STRIX B760-F Gaming WiFi", "ASUS", "ROG STRIX B760-F", 219.99, "ATX", "LGA1700", "B760", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASUS TUF Gaming B760-Plus WiFi", "ASUS", "TUF Gaming B760-Plus", 189.99, "ATX", "LGA1700", "B760", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASUS Prime B760-Plus", "ASUS", "Prime B760-Plus", 149.99, "ATX", "LGA1700", "B760", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, None, "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "MSI MAG B760 Tomahawk WiFi", "MSI", "MAG B760 Tomahawk", 199.99, "ATX", "LGA1700", "B760", 4, "256GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "MSI PRO B760-P WiFi", "MSI", "PRO B760-P", 159.99, "ATX", "LGA1700", "B760", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "Gigabyte B760 AORUS Elite AX", "Gigabyte", "B760 AORUS Elite AX", 179.99, "ATX", "LGA1700", "B760", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "Gigabyte B760 Gaming X AX", "Gigabyte", "B760 Gaming X AX", 169.99, "ATX", "LGA1700", "B760", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASRock B760 Pro RS", "ASRock", "B760 Pro RS", 139.99, "ATX", "LGA1700", "B760", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, None, "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASRock B760 Steel Legend WiFi", "ASRock", "B760 Steel Legend", 179.99, "ATX", "LGA1700", "B760", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        # H610 budget
        ("motherboards-intel", "ASUS Prime H610M-A D4", "ASUS", "Prime H610M-A", 99.99, "Micro ATX", "LGA1700", "H610", 2, "64GB DDR4", "1x PCIe 4.0 x16", 1, None, "1Gb Ethernet", "DDR4"),
        ("motherboards-intel", "MSI PRO H610M-G DDR4", "MSI", "PRO H610M-G", 89.99, "Micro ATX", "LGA1700", "H610", 2, "64GB DDR4", "1x PCIe 4.0 x16", 1, None, "1Gb Ethernet", "DDR4"),
        ("motherboards-intel", "Gigabyte H610M H DDR4", "Gigabyte", "H610M H", 79.99, "Micro ATX", "LGA1700", "H610", 2, "64GB DDR4", "1x PCIe 4.0 x16", 1, None, "1Gb Ethernet", "DDR4"),
    ]:
        add(*args)

    # AMD X670E/X670
    for args in [
        ("motherboards-amd", "ASUS ROG Crosshair X670E Hero", "ASUS", "ROG Crosshair X670E Hero", 499.99, "ATX", "AM5", "X670E", 4, "192GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "ASUS ROG Crosshair X670E Gene", "ASUS", "ROG Crosshair X670E Gene", 399.99, "Micro ATX", "AM5", "X670E", 2, "96GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "ASUS ROG STRIX X670E-E Gaming WiFi", "ASUS", "ROG STRIX X670E-E", 449.99, "ATX", "AM5", "X670E", 4, "192GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "ASUS TUF Gaming X670E-Plus WiFi", "ASUS", "TUF Gaming X670E-Plus", 279.99, "ATX", "AM5", "X670E", 4, "192GB DDR5", "2x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "ASUS Prime X670E-Pro WiFi", "ASUS", "Prime X670E-Pro", 249.99, "ATX", "AM5", "X670E", 4, "192GB DDR5", "2x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "MSI MEG X670E ACE", "MSI", "MEG X670E ACE", 599.99, "ATX", "AM5", "X670E", 4, "192GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "MSI MPG X670E CARBON WiFi", "MSI", "MPG X670E CARBON", 399.99, "ATX", "AM5", "X670E", 4, "192GB DDR5", "2x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "MSI MAG X670E Tomahawk WiFi", "MSI", "MAG X670E Tomahawk", 289.99, "ATX", "AM5", "X670E", 4, "192GB DDR5", "1x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "MSI PRO X670-P WiFi", "MSI", "PRO X670-P", 229.99, "ATX", "AM5", "X670", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "Gigabyte X670E AORUS Xtreme", "Gigabyte", "X670E AORUS Xtreme", 699.99, "ATX", "AM5", "X670E", 4, "192GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 7", "10Gb Ethernet", "DDR5"),
        ("motherboards-amd", "Gigabyte X670E AORUS Master", "Gigabyte", "X670E AORUS Master", 479.99, "ATX", "AM5", "X670E", 4, "192GB DDR5", "2x PCIe 5.0 x16", 4, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "Gigabyte X670 AORUS Elite AX", "Gigabyte", "X670 AORUS Elite AX", 249.99, "ATX", "AM5", "X670", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "ASRock X670E Taichi", "ASRock", "X670E Taichi", 479.99, "ATX", "AM5", "X670E", 4, "192GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "ASRock X670E Steel Legend", "ASRock", "X670E Steel Legend", 299.99, "ATX", "AM5", "X670E", 4, "192GB DDR5", "2x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "ASRock X670E Pro RS", "ASRock", "X670E Pro RS", 229.99, "ATX", "AM5", "X670E", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, None, "2.5Gb Ethernet", "DDR5"),
        # B650/B650E
        ("motherboards-amd", "ASUS ROG STRIX B650E-E Gaming WiFi", "ASUS", "ROG STRIX B650E-E", 299.99, "ATX", "AM5", "B650E", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "ASUS ROG STRIX B650-A Gaming WiFi", "ASUS", "ROG STRIX B650-A", 249.99, "ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "ASUS TUF Gaming B650-Plus WiFi", "ASUS", "TUF Gaming B650-Plus", 189.99, "ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "ASUS Prime B650-Plus", "ASUS", "Prime B650-Plus", 139.99, "ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, None, "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "MSI MAG B650 Tomahawk WiFi", "MSI", "MAG B650 Tomahawk", 219.99, "ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "MSI MPG B650 CARBON WiFi", "MSI", "MPG B650 CARBON", 299.99, "ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 4, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "MSI PRO B650-P WiFi", "MSI", "PRO B650-P", 159.99, "ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "Gigabyte B650 AORUS Elite AX", "Gigabyte", "B650 AORUS Elite AX", 199.99, "ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "Gigabyte B650 AORUS Pro AX", "Gigabyte", "B650 AORUS Pro AX", 229.99, "ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "Gigabyte B650 Gaming X AX", "Gigabyte", "B650 Gaming X AX", 179.99, "ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "Gigabyte B650 Eagle AX", "Gigabyte", "B650 Eagle AX", 159.99, "ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "ASRock B650E Taichi", "ASRock", "B650E Taichi", 349.99, "ATX", "AM5", "B650E", 4, "192GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "ASRock B650 Pro RS", "ASRock", "B650 Pro RS", 149.99, "ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, None, "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "ASRock B650 Steel Legend WiFi", "ASRock", "B650 Steel Legend", 199.99, "ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-amd", "ASRock B650 PG Lightning", "ASRock", "B650 PG Lightning", 169.99, "ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, None, "2.5Gb Ethernet", "DDR5"),
        # A620
        ("motherboards-amd", "ASUS Prime A620-Plus", "ASUS", "Prime A620-Plus", 99.99, "ATX", "AM5", "A620", 4, "192GB DDR5", "1x PCIe 4.0 x16", 1, None, "1Gb Ethernet", "DDR5"),
        ("motherboards-amd", "MSI PRO A620M-E", "MSI", "PRO A620M-E", 79.99, "Micro ATX", "AM5", "A620", 2, "96GB DDR5", "1x PCIe 4.0 x16", 1, None, "1Gb Ethernet", "DDR5"),
        ("motherboards-amd", "Gigabyte A620M Gaming X", "Gigabyte", "A620M Gaming X", 89.99, "Micro ATX", "AM5", "A620", 2, "96GB DDR5", "1x PCIe 4.0 x16", 1, None, "1Gb Ethernet", "DDR5"),
        ("motherboards-amd", "ASRock A620M Pro RS", "ASRock", "A620M Pro RS", 94.99, "Micro ATX", "AM5", "A620", 2, "96GB DDR5", "1x PCIe 4.0 x16", 2, None, "2.5Gb Ethernet", "DDR5"),
        # Micro ATX
        ("motherboards-micro-atx", "ASUS TUF Gaming B760M-Plus WiFi", "ASUS", "TUF Gaming B760M-Plus", 179.99, "Micro ATX", "LGA1700", "B760", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-micro-atx", "MSI MAG B760M Mortar WiFi", "MSI", "MAG B760M Mortar", 179.99, "Micro ATX", "LGA1700", "B760", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-micro-atx", "MSI PRO B760M-A WiFi", "MSI", "PRO B760M-A", 149.99, "Micro ATX", "LGA1700", "B760", 2, "96GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-micro-atx", "Gigabyte B760M AORUS Elite AX", "Gigabyte", "B760M AORUS Elite AX", 169.99, "Micro ATX", "LGA1700", "B760", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-micro-atx", "ASRock B760M Pro RS D4", "ASRock", "B760M Pro RS", 129.99, "Micro ATX", "LGA1700", "B760", 4, "128GB DDR4", "1x PCIe 5.0 x16", 2, None, "2.5Gb Ethernet", "DDR4"),
        ("motherboards-micro-atx", "ASUS TUF Gaming B650M-Plus WiFi", "ASUS", "TUF Gaming B650M-Plus", 199.99, "Micro ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-micro-atx", "MSI MAG B650M Mortar WiFi", "MSI", "MAG B650M Mortar", 199.99, "Micro ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-micro-atx", "Gigabyte B650M AORUS Elite AX", "Gigabyte", "B650M AORUS Elite AX", 179.99, "Micro ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-micro-atx", "ASRock B650M Pro RS", "ASRock", "B650M Pro RS", 139.99, "Micro ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, None, "2.5Gb Ethernet", "DDR5"),
        # Mini ITX
        ("motherboards-mini-itx", "ASUS ROG STRIX B760-I Gaming WiFi", "ASUS", "ROG STRIX B760-I", 229.99, "Mini ITX", "LGA1700", "B760", 2, "96GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-mini-itx", "ASUS ROG STRIX Z790-I Gaming WiFi", "ASUS", "ROG STRIX Z790-I", 399.99, "Mini ITX", "LGA1700", "Z790", 2, "96GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-mini-itx", "MSI MPG B760I EDGE WiFi", "MSI", "MPG B760I EDGE", 199.99, "Mini ITX", "LGA1700", "B760", 2, "96GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-mini-itx", "Gigabyte B760I AORUS Pro", "Gigabyte", "B760I AORUS Pro", 189.99, "Mini ITX", "LGA1700", "B760", 2, "96GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-mini-itx", "ASRock Z790M-ITX WiFi", "ASRock", "Z790M-ITX", 279.99, "Mini ITX", "LGA1700", "Z790", 2, "96GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-mini-itx", "ASUS ROG STRIX B650E-I Gaming WiFi", "ASUS", "ROG STRIX B650E-I", 299.99, "Mini ITX", "AM5", "B650E", 2, "96GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-mini-itx", "MSI MPG B650I EDGE WiFi", "MSI", "MPG B650I EDGE", 249.99, "Mini ITX", "AM5", "B650", 2, "96GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-mini-itx", "Gigabyte B650I AORUS Ultra", "Gigabyte", "B650I AORUS Ultra", 249.99, "Mini ITX", "AM5", "B650", 2, "96GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-mini-itx", "ASRock B650E PG-ITX WiFi", "ASRock", "B650E PG-ITX", 259.99, "Mini ITX", "AM5", "B650E", 2, "96GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-mini-itx", "ASRock A620I Lightning WiFi", "ASRock", "A620I Lightning", 149.99, "Mini ITX", "AM5", "A620", 2, "96GB DDR5", "1x PCIe 4.0 x16", 1, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
    ]:
        add(*args)

    # Z890 (Arrow Lake LGA1851)
    for args in [
        ("motherboards-intel", "ASUS ROG Maximus Z890 Hero", "ASUS", "ROG Maximus Z890 Hero", 599.99, "ATX", "LGA1851", "Z890", 4, "256GB DDR5", "2x PCIe 5.0 x16", 6, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASUS ROG STRIX Z890-E Gaming WiFi", "ASUS", "ROG STRIX Z890-E", 499.99, "ATX", "LGA1851", "Z890", 4, "256GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASUS ROG STRIX Z890-F Gaming WiFi", "ASUS", "ROG STRIX Z890-F", 429.99, "ATX", "LGA1851", "Z890", 4, "256GB DDR5", "1x PCIe 5.0 x16", 4, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASUS TUF Gaming Z890-Plus WiFi", "ASUS", "TUF Gaming Z890-Plus", 299.99, "ATX", "LGA1851", "Z890", 4, "256GB DDR5", "1x PCIe 5.0 x16", 4, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "MSI MEG Z890 ACE", "MSI", "MEG Z890 ACE", 599.99, "ATX", "LGA1851", "Z890", 4, "256GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 7", "5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "MSI MPG Z890 CARBON WiFi", "MSI", "MPG Z890 CARBON", 429.99, "ATX", "LGA1851", "Z890", 4, "256GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "MSI MAG Z890 Tomahawk WiFi", "MSI", "MAG Z890 Tomahawk", 299.99, "ATX", "LGA1851", "Z890", 4, "256GB DDR5", "1x PCIe 5.0 x16", 4, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "MSI Z890-P Pro", "MSI", "Z890-P Pro", 229.99, "ATX", "LGA1851", "Z890", 4, "256GB DDR5", "1x PCIe 5.0 x16", 3, None, "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "Gigabyte Z890 AORUS Master", "Gigabyte", "Z890 AORUS Master", 529.99, "ATX", "LGA1851", "Z890", 4, "256GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "Gigabyte Z890 AORUS Elite AX", "Gigabyte", "Z890 AORUS Elite AX", 299.99, "ATX", "LGA1851", "Z890", 4, "256GB DDR5", "1x PCIe 5.0 x16", 4, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASRock Z890 Taichi", "ASRock", "Z890 Taichi", 529.99, "ATX", "LGA1851", "Z890", 4, "256GB DDR5", "2x PCIe 5.0 x16", 5, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASRock Z890 Pro RS", "ASRock", "Z890 Pro RS", 229.99, "ATX", "LGA1851", "Z890", 4, "256GB DDR5", "1x PCIe 5.0 x16", 3, None, "2.5Gb Ethernet", "DDR5"),
        # B860
        ("motherboards-intel", "ASUS ROG STRIX B860-F Gaming WiFi", "ASUS", "ROG STRIX B860-F", 279.99, "ATX", "LGA1851", "B860", 4, "256GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASUS TUF Gaming B860-Plus WiFi", "ASUS", "TUF Gaming B860-Plus", 229.99, "ATX", "LGA1851", "B860", 4, "256GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "MSI MAG B860 Tomahawk WiFi", "MSI", "MAG B860 Tomahawk", 249.99, "ATX", "LGA1851", "B860", 4, "256GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "Gigabyte B860 AORUS Elite AX", "Gigabyte", "B860 AORUS Elite AX", 229.99, "ATX", "LGA1851", "B860", 4, "256GB DDR5", "1x PCIe 5.0 x16", 3, "WiFi 7", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-intel", "ASRock B860 Pro RS", "ASRock", "B860 Pro RS", 179.99, "ATX", "LGA1851", "B860", 4, "256GB DDR5", "1x PCIe 5.0 x16", 2, None, "2.5Gb Ethernet", "DDR5"),
        # Additional AMD AM5 Micro ATX
        ("motherboards-micro-atx", "ASUS TUF Gaming B650M-E WiFi", "ASUS", "TUF Gaming B650M-E", 159.99, "Micro ATX", "AM5", "B650", 2, "96GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-micro-atx", "Gigabyte B650M Gaming Plus WiFi", "Gigabyte", "B650M Gaming Plus", 149.99, "Micro ATX", "AM5", "B650", 2, "96GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-micro-atx", "ASRock B650M Pro RS WiFi", "ASRock", "B650M Pro RS WiFi", 149.99, "Micro ATX", "AM5", "B650", 4, "192GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        # Additional Mini ITX
        ("motherboards-mini-itx", "Gigabyte Z790I AORUS Pro", "Gigabyte", "Z790I AORUS Pro", 299.99, "Mini ITX", "LGA1700", "Z790", 2, "96GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
        ("motherboards-mini-itx", "MSI MPG Z790I EDGE WiFi", "MSI", "MPG Z790I EDGE", 289.99, "Mini ITX", "LGA1700", "Z790", 2, "96GB DDR5", "1x PCIe 5.0 x16", 2, "WiFi 6E", "2.5Gb Ethernet", "DDR5"),
    ]:
        add(*args)

    return products
