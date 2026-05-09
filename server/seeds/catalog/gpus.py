def generate_gpus() -> list[dict]:
    products = []

    def add_nvidia(series_list, subcat, pcie_ver):
        for name_base, specs_base, price, tdp, psu, slot in series_list:
            s = dict(specs_base)
            s["pcie_version"] = pcie_ver
            model_short = name_base.replace("NVIDIA GeForce ", "")
            products.append({"name": name_base, "brand": "NVIDIA", "category": "GPU", "subcategory_slug": subcat, "manufacturer": "NVIDIA", "model": model_short, "price": price, "power_consumption": tdp, "specs": s, "compatibility": {"pcie_version": pcie_ver, "required_psu": psu, "slot_size": slot}})
            for aib in ["ASUS ROG", "MSI Gaming", "Gigabyte AORUS", "Zotac Gaming", "PNY XLR8"]:
                mult = {"ASUS ROG": 1.15, "MSI Gaming": 1.08, "Gigabyte AORUS": 1.10, "Zotac Gaming": 0.97, "PNY XLR8": 0.95}
                s2 = dict(specs_base)
                s2["pcie_version"] = pcie_ver
                s2["aib_partner"] = aib
                aib_name = f"{aib} {model_short}"
                products.append({"name": aib_name, "brand": aib.split()[0], "category": "GPU", "subcategory_slug": subcat, "manufacturer": aib.split()[0], "model": f"{aib} {model_short}", "price": round(price * mult.get(aib, 1.0), 2), "power_consumption": tdp, "specs": s2, "compatibility": {"pcie_version": pcie_ver, "required_psu": psu, "slot_size": slot}})

    def add_amd(series_list, subcat):
        for name_base, specs_base, price, tdp, psu, slot in series_list:
            s = dict(specs_base)
            s["pcie_version"] = "4.0"
            model_short = name_base.replace("AMD Radeon ", "")
            products.append({"name": name_base, "brand": "AMD", "category": "GPU", "subcategory_slug": subcat, "manufacturer": "AMD", "model": model_short, "price": price, "power_consumption": tdp, "specs": s, "compatibility": {"pcie_version": "4.0", "required_psu": psu, "slot_size": slot}})

    def add_amd_aib(series_list, subcat):
        for name_base, specs_base, price, tdp, psu, slot in series_list:
            model_short = name_base.replace("AMD Radeon ", "")
            for aib in ["ASUS ROG", "MSI Gaming", "Sapphire Nitro+", "PowerColor Red Devil", "XFX Speedster"]:
                mult = {"ASUS ROG": 1.12, "MSI Gaming": 1.06, "Sapphire Nitro+": 1.05, "PowerColor Red Devil": 1.04, "XFX Speedster": 1.02}
                s2 = dict(specs_base)
                s2["pcie_version"] = "4.0"
                s2["aib_partner"] = aib
                aib_name = f"{aib} {model_short}"
                products.append({"name": aib_name, "brand": aib.split()[0], "category": "GPU", "subcategory_slug": subcat, "manufacturer": aib.split()[0], "model": f"{aib} {model_short}", "price": round(price * mult.get(aib, 1.0), 2), "power_consumption": tdp, "specs": s2, "compatibility": {"pcie_version": "4.0", "required_psu": psu, "slot_size": slot}})

    rtx50 = [
        ("NVIDIA GeForce RTX 5090", {"architecture": "Blackwell", "cuda_cores": 24576, "memory": "32GB GDDR7", "memory_bus": 512, "boost_clock": "2.9 GHz"}, 1999.99, 575, "1000W", "3.5 slot"),
        ("NVIDIA GeForce RTX 5080", {"architecture": "Blackwell", "cuda_cores": 18432, "memory": "24GB GDDR7", "memory_bus": 384, "boost_clock": "2.8 GHz"}, 1499.99, 400, "850W", "3 slot"),
        ("NVIDIA GeForce RTX 5070 Ti", {"architecture": "Blackwell", "cuda_cores": 10880, "memory": "16GB GDDR7", "memory_bus": 256, "boost_clock": "2.65 GHz"}, 849.99, 310, "750W", "2.5 slot"),
        ("NVIDIA GeForce RTX 5070", {"architecture": "Blackwell", "cuda_cores": 8704, "memory": "12GB GDDR7", "memory_bus": 192, "boost_clock": "2.5 GHz"}, 649.99, 260, "700W", "2.5 slot"),
    ]
    add_nvidia(rtx50, "gpus-nvidia-rtx", "5.0")

    rtx40 = [
        ("NVIDIA GeForce RTX 4090", {"architecture": "Ada Lovelace", "cuda_cores": 16384, "memory": "24GB GDDR6X", "memory_bus": 384, "boost_clock": "2.52 GHz"}, 1599.99, 450, "850W", "3 slot"),
        ("NVIDIA GeForce RTX 4080 Super", {"architecture": "Ada Lovelace", "cuda_cores": 10240, "memory": "16GB GDDR6X", "memory_bus": 256, "boost_clock": "2.55 GHz"}, 999.99, 320, "750W", "2.5 slot"),
        ("NVIDIA GeForce RTX 4080", {"architecture": "Ada Lovelace", "cuda_cores": 9728, "memory": "16GB GDDR6X", "memory_bus": 256, "boost_clock": "2.51 GHz"}, 899.99, 320, "750W", "2.5 slot"),
        ("NVIDIA GeForce RTX 4070 Ti Super", {"architecture": "Ada Lovelace", "cuda_cores": 8448, "memory": "16GB GDDR6X", "memory_bus": 256, "boost_clock": "2.61 GHz"}, 799.99, 285, "700W", "2.5 slot"),
        ("NVIDIA GeForce RTX 4070 Ti", {"architecture": "Ada Lovelace", "cuda_cores": 7680, "memory": "12GB GDDR6X", "memory_bus": 192, "boost_clock": "2.61 GHz"}, 749.99, 285, "700W", "2.5 slot"),
        ("NVIDIA GeForce RTX 4070 Super", {"architecture": "Ada Lovelace", "cuda_cores": 7168, "memory": "12GB GDDR6X", "memory_bus": 192, "boost_clock": "2.48 GHz"}, 599.99, 220, "650W", "2 slot"),
        ("NVIDIA GeForce RTX 4070", {"architecture": "Ada Lovelace", "cuda_cores": 5888, "memory": "12GB GDDR6X", "memory_bus": 192, "boost_clock": "2.48 GHz"}, 549.99, 200, "650W", "2 slot"),
        ("NVIDIA GeForce RTX 4060 Ti 16GB", {"architecture": "Ada Lovelace", "cuda_cores": 4352, "memory": "16GB GDDR6", "memory_bus": 128, "boost_clock": "2.54 GHz"}, 449.99, 160, "550W", "2 slot"),
        ("NVIDIA GeForce RTX 4060 Ti 8GB", {"architecture": "Ada Lovelace", "cuda_cores": 4352, "memory": "8GB GDDR6", "memory_bus": 128, "boost_clock": "2.54 GHz"}, 399.99, 160, "550W", "2 slot"),
        ("NVIDIA GeForce RTX 4060", {"architecture": "Ada Lovelace", "cuda_cores": 3072, "memory": "8GB GDDR6", "memory_bus": 128, "boost_clock": "2.46 GHz"}, 299.99, 115, "550W", "2 slot"),
    ]
    add_nvidia(rtx40, "gpus-nvidia-rtx", "4.0")

    rtx30 = [
        ("NVIDIA GeForce RTX 3090 Ti", {"architecture": "Ampere", "cuda_cores": 10752, "memory": "24GB GDDR6X", "memory_bus": 384, "boost_clock": "1.86 GHz"}, 1099.99, 450, "850W", "3 slot"),
        ("NVIDIA GeForce RTX 3090", {"architecture": "Ampere", "cuda_cores": 10496, "memory": "24GB GDDR6X", "memory_bus": 384, "boost_clock": "1.70 GHz"}, 899.99, 350, "750W", "3 slot"),
        ("NVIDIA GeForce RTX 3080 Ti", {"architecture": "Ampere", "cuda_cores": 10240, "memory": "12GB GDDR6X", "memory_bus": 384, "boost_clock": "1.67 GHz"}, 799.99, 350, "750W", "2.5 slot"),
        ("NVIDIA GeForce RTX 3080 12GB", {"architecture": "Ampere", "cuda_cores": 8960, "memory": "12GB GDDR6X", "memory_bus": 384, "boost_clock": "1.71 GHz"}, 749.99, 350, "750W", "2.5 slot"),
        ("NVIDIA GeForce RTX 3080", {"architecture": "Ampere", "cuda_cores": 8704, "memory": "10GB GDDR6X", "memory_bus": 320, "boost_clock": "1.71 GHz"}, 699.99, 320, "750W", "2.5 slot"),
        ("NVIDIA GeForce RTX 3070 Ti", {"architecture": "Ampere", "cuda_cores": 6144, "memory": "8GB GDDR6X", "memory_bus": 256, "boost_clock": "1.77 GHz"}, 499.99, 290, "650W", "2 slot"),
        ("NVIDIA GeForce RTX 3070", {"architecture": "Ampere", "cuda_cores": 5888, "memory": "8GB GDDR6", "memory_bus": 256, "boost_clock": "1.73 GHz"}, 399.99, 220, "650W", "2 slot"),
        ("NVIDIA GeForce RTX 3060 Ti", {"architecture": "Ampere", "cuda_cores": 4864, "memory": "8GB GDDR6", "memory_bus": 256, "boost_clock": "1.67 GHz"}, 299.99, 200, "600W", "2 slot"),
        ("NVIDIA GeForce RTX 3060 12GB", {"architecture": "Ampere", "cuda_cores": 3584, "memory": "12GB GDDR6", "memory_bus": 192, "boost_clock": "1.78 GHz"}, 249.99, 170, "550W", "2 slot"),
        ("NVIDIA GeForce RTX 3060 8GB", {"architecture": "Ampere", "cuda_cores": 3584, "memory": "8GB GDDR6", "memory_bus": 128, "boost_clock": "1.78 GHz"}, 229.99, 170, "550W", "2 slot"),
    ]
    add_nvidia(rtx30, "gpus-nvidia-rtx", "4.0")

    # AMD RX 7000
    rx7000 = [
        ("AMD Radeon RX 7900 XTX", {"architecture": "RDNA 3", "stream_processors": 6144, "memory": "24GB GDDR6", "memory_bus": 384, "boost_clock": "2.5 GHz"}, 999.99, 355, "850W", "2.5 slot"),
        ("AMD Radeon RX 7900 XT", {"architecture": "RDNA 3", "stream_processors": 5376, "memory": "20GB GDDR6", "memory_bus": 320, "boost_clock": "2.4 GHz"}, 799.99, 315, "750W", "2.5 slot"),
        ("AMD Radeon RX 7800 XT", {"architecture": "RDNA 3", "stream_processors": 3840, "memory": "16GB GDDR6", "memory_bus": 256, "boost_clock": "2.4 GHz"}, 499.99, 263, "700W", "2.5 slot"),
        ("AMD Radeon RX 7700 XT", {"architecture": "RDNA 3", "stream_processors": 3456, "memory": "12GB GDDR6", "memory_bus": 192, "boost_clock": "2.5 GHz"}, 449.99, 245, "700W", "2 slot"),
        ("AMD Radeon RX 7600 XT", {"architecture": "RDNA 3", "stream_processors": 2048, "memory": "16GB GDDR6", "memory_bus": 128, "boost_clock": "2.8 GHz"}, 329.99, 190, "600W", "2 slot"),
        ("AMD Radeon RX 7600", {"architecture": "RDNA 3", "stream_processors": 2048, "memory": "8GB GDDR6", "memory_bus": 128, "boost_clock": "2.7 GHz"}, 269.99, 165, "550W", "2 slot"),
    ]
    add_amd(rx7000, "gpus-amd-radeon")
    add_amd_aib(rx7000, "gpus-amd-radeon")

    # RTX 20 series (Super/Ti variants)
    rtx20 = [
        ("NVIDIA GeForce RTX 2080 Ti", {"architecture": "Turing", "cuda_cores": 4352, "memory": "11GB GDDR6", "memory_bus": 352, "boost_clock": "1.55 GHz"}, 699.99, 250, "650W", "2.5 slot"),
        ("NVIDIA GeForce RTX 2080 Super", {"architecture": "Turing", "cuda_cores": 3072, "memory": "8GB GDDR6", "memory_bus": 256, "boost_clock": "1.82 GHz"}, 499.99, 250, "650W", "2 slot"),
        ("NVIDIA GeForce RTX 2080", {"architecture": "Turing", "cuda_cores": 2944, "memory": "8GB GDDR6", "memory_bus": 256, "boost_clock": "1.71 GHz"}, 449.99, 215, "650W", "2 slot"),
        ("NVIDIA GeForce RTX 2070 Super", {"architecture": "Turing", "cuda_cores": 2560, "memory": "8GB GDDR6", "memory_bus": 256, "boost_clock": "1.77 GHz"}, 399.99, 215, "650W", "2 slot"),
        ("NVIDIA GeForce RTX 2070", {"architecture": "Turing", "cuda_cores": 2304, "memory": "8GB GDDR6", "memory_bus": 256, "boost_clock": "1.62 GHz"}, 349.99, 175, "550W", "2 slot"),
        ("NVIDIA GeForce RTX 2060 Super", {"architecture": "Turing", "cuda_cores": 2176, "memory": "8GB GDDR6", "memory_bus": 256, "boost_clock": "1.65 GHz"}, 299.99, 175, "550W", "2 slot"),
        ("NVIDIA GeForce RTX 2060", {"architecture": "Turing", "cuda_cores": 1920, "memory": "6GB GDDR6", "memory_bus": 192, "boost_clock": "1.68 GHz"}, 249.99, 160, "500W", "2 slot"),
    ]
    add_nvidia(rtx20, "gpus-nvidia-rtx", "3.0")

    # AMD RX 6000
    rx6000 = [
        ("AMD Radeon RX 6950 XT", {"architecture": "RDNA 2", "stream_processors": 5120, "memory": "16GB GDDR6", "memory_bus": 256, "boost_clock": "2.3 GHz"}, 499.99, 335, "850W", "2.5 slot"),
        ("AMD Radeon RX 6900 XT", {"architecture": "RDNA 2", "stream_processors": 5120, "memory": "16GB GDDR6", "memory_bus": 256, "boost_clock": "2.3 GHz"}, 449.99, 300, "750W", "2.5 slot"),
        ("AMD Radeon RX 6800 XT", {"architecture": "RDNA 2", "stream_processors": 4608, "memory": "16GB GDDR6", "memory_bus": 256, "boost_clock": "2.3 GHz"}, 399.99, 300, "750W", "2.5 slot"),
        ("AMD Radeon RX 6800", {"architecture": "RDNA 2", "stream_processors": 3840, "memory": "16GB GDDR6", "memory_bus": 256, "boost_clock": "2.1 GHz"}, 349.99, 250, "650W", "2 slot"),
        ("AMD Radeon RX 6750 XT", {"architecture": "RDNA 2", "stream_processors": 2560, "memory": "12GB GDDR6", "memory_bus": 192, "boost_clock": "2.6 GHz"}, 299.99, 250, "650W", "2 slot"),
        ("AMD Radeon RX 6700 XT", {"architecture": "RDNA 2", "stream_processors": 2560, "memory": "12GB GDDR6", "memory_bus": 192, "boost_clock": "2.4 GHz"}, 249.99, 230, "650W", "2 slot"),
        ("AMD Radeon RX 6650 XT", {"architecture": "RDNA 2", "stream_processors": 2048, "memory": "8GB GDDR6", "memory_bus": 128, "boost_clock": "2.6 GHz"}, 199.99, 180, "500W", "2 slot"),
    ]
    add_amd(rx6000, "gpus-amd-radeon")
    add_amd_aib(rx6000, "gpus-amd-radeon")

    # Intel ARC
    for name, specs_base, price, tdp, psu, slot in [
        ("Intel Arc A770 16GB", {"architecture": "Alchemist", "xmx_cores": 512, "memory": "16GB GDDR6", "memory_bus": 256, "boost_clock": "2.1 GHz"}, 329.99, 225, "650W", "2 slot"),
        ("Intel Arc A770 8GB", {"architecture": "Alchemist", "xmx_cores": 512, "memory": "8GB GDDR6", "memory_bus": 256, "boost_clock": "2.1 GHz"}, 299.99, 225, "650W", "2 slot"),
        ("Intel Arc A750", {"architecture": "Alchemist", "xmx_cores": 448, "memory": "8GB GDDR6", "memory_bus": 256, "boost_clock": "2.05 GHz"}, 249.99, 225, "600W", "2 slot"),
        ("Intel Arc A580", {"architecture": "Alchemist", "xmx_cores": 384, "memory": "8GB GDDR6", "memory_bus": 256, "boost_clock": "1.7 GHz"}, 179.99, 175, "500W", "2 slot"),
        ("Intel Arc B580", {"architecture": "Battlemage", "xmx_cores": 384, "memory": "12GB GDDR6", "memory_bus": 192, "boost_clock": "2.2 GHz"}, 249.99, 190, "600W", "2 slot"),
        ("Intel Arc B570", {"architecture": "Battlemage", "xmx_cores": 320, "memory": "10GB GDDR6", "memory_bus": 160, "boost_clock": "2.1 GHz"}, 219.99, 170, "550W", "2 slot"),
    ]:
        s = dict(specs_base)
        s["pcie_version"] = "4.0"
        products.append({"name": name, "brand": "Intel", "category": "GPU", "subcategory_slug": "gpus-intel-arc", "manufacturer": "Intel", "model": name.replace("Intel Arc ", ""), "price": price, "power_consumption": tdp, "specs": s, "compatibility": {"pcie_version": "4.0", "required_psu": psu, "slot_size": slot}})

    return products
