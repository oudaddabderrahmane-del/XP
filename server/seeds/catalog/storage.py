def generate_storage() -> list[dict]:
    products = []

    # NVMe SSDs
    for brand, model, specs, price, power in [
        ("Samsung", "990 Pro", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7450 MB/s", "write_speed": "6900 MB/s", "type": "TLC NAND"}, 109.99, 7.8),
        ("Samsung", "990 Pro", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7450 MB/s", "write_speed": "6900 MB/s", "type": "TLC NAND"}, 189.99, 7.8),
        ("Samsung", "990 Pro", {"capacity": "4TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7450 MB/s", "write_speed": "6900 MB/s", "type": "TLC NAND"}, 349.99, 8.5),
        ("Samsung", "990 EVO", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "5000 MB/s", "write_speed": "4200 MB/s", "type": "TLC NAND"}, 79.99, 5.5),
        ("Samsung", "990 EVO", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "5000 MB/s", "write_speed": "4200 MB/s", "type": "TLC NAND"}, 139.99, 5.5),
        ("Samsung", "980 Pro", {"capacity": "500GB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "6900 MB/s", "write_speed": "5000 MB/s", "type": "TLC NAND"}, 59.99, 6.5),
        ("Samsung", "980 Pro", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7000 MB/s", "write_speed": "5000 MB/s", "type": "TLC NAND"}, 89.99, 6.5),
        ("Samsung", "980 Pro", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7000 MB/s", "write_speed": "5100 MB/s", "type": "TLC NAND"}, 159.99, 7.5),
        ("Samsung", "9100 Pro", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "14900 MB/s", "write_speed": "9500 MB/s", "type": "TLC NAND"}, 249.99, 9.5),
        ("Samsung", "9100 Pro", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "14900 MB/s", "write_speed": "10000 MB/s", "type": "TLC NAND"}, 399.99, 10.5),
        ("Western Digital", "Black SN850X", {"capacity": "500GB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7300 MB/s", "write_speed": "4000 MB/s", "type": "TLC NAND"}, 69.99, 6.5),
        ("Western Digital", "Black SN850X", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7300 MB/s", "write_speed": "6300 MB/s", "type": "TLC NAND"}, 109.99, 7.5),
        ("Western Digital", "Black SN850X", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7300 MB/s", "write_speed": "6600 MB/s", "type": "TLC NAND"}, 189.99, 7.5),
        ("Western Digital", "Black SN850X", {"capacity": "4TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7300 MB/s", "write_speed": "6600 MB/s", "type": "TLC NAND"}, 399.99, 8.5),
        ("Western Digital", "Blue SN580", {"capacity": "500GB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "4150 MB/s", "write_speed": "2600 MB/s", "type": "TLC NAND"}, 44.99, 4.5),
        ("Western Digital", "Blue SN580", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "4150 MB/s", "write_speed": "4150 MB/s", "type": "TLC NAND"}, 74.99, 5.0),
        ("Western Digital", "Blue SN580", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "4150 MB/s", "write_speed": "4150 MB/s", "type": "TLC NAND"}, 139.99, 5.5),
        ("Crucial", "T700", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "12400 MB/s", "write_speed": "11800 MB/s", "type": "TLC NAND"}, 229.99, 9.5),
        ("Crucial", "T700", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "12400 MB/s", "write_speed": "11800 MB/s", "type": "TLC NAND"}, 399.99, 10.5),
        ("Crucial", "T500", {"capacity": "500GB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7300 MB/s", "write_speed": "3500 MB/s", "type": "TLC NAND"}, 59.99, 5.5),
        ("Crucial", "T500", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7300 MB/s", "write_speed": "6800 MB/s", "type": "TLC NAND"}, 99.99, 6.5),
        ("Crucial", "T500", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7300 MB/s", "write_speed": "7000 MB/s", "type": "TLC NAND"}, 179.99, 7.5),
        ("Crucial", "P3 Plus", {"capacity": "500GB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "5000 MB/s", "write_speed": "3600 MB/s", "type": "QLC NAND"}, 39.99, 5.5),
        ("Crucial", "P3 Plus", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "5000 MB/s", "write_speed": "4200 MB/s", "type": "QLC NAND"}, 69.99, 6.0),
        ("Crucial", "P3 Plus", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "5000 MB/s", "write_speed": "4200 MB/s", "type": "QLC NAND"}, 129.99, 6.5),
        ("SK Hynix", "Platinum P41", {"capacity": "500GB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7000 MB/s", "write_speed": "4700 MB/s", "type": "TLC NAND"}, 79.99, 6.5),
        ("SK Hynix", "Platinum P41", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7000 MB/s", "write_speed": "6500 MB/s", "type": "TLC NAND"}, 129.99, 7.5),
        ("SK Hynix", "Platinum P41", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7000 MB/s", "write_speed": "6500 MB/s", "type": "TLC NAND"}, 229.99, 8.0),
        ("TeamGroup", "T-Force Cardea Z540", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "13000 MB/s", "write_speed": "10000 MB/s", "type": "TLC NAND"}, 269.99, 10.5),
        ("TeamGroup", "T-Force Cardea Z540", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "13000 MB/s", "write_speed": "10200 MB/s", "type": "TLC NAND"}, 449.99, 11.5),
        ("Seagate", "FireCuda 540", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "10000 MB/s", "write_speed": "10000 MB/s", "type": "TLC NAND"}, 229.99, 9.5),
        ("Seagate", "FireCuda 540", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "10000 MB/s", "write_speed": "10000 MB/s", "type": "TLC NAND"}, 399.99, 10.5),
        ("Seagate", "FireCuda 530", {"capacity": "500GB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7000 MB/s", "write_speed": "3000 MB/s", "type": "TLC NAND"}, 59.99, 5.5),
        ("Seagate", "FireCuda 530", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7300 MB/s", "write_speed": "6000 MB/s", "type": "TLC NAND"}, 99.99, 6.5),
        ("Seagate", "FireCuda 530", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7300 MB/s", "write_speed": "6900 MB/s", "type": "TLC NAND"}, 179.99, 7.5),
        ("Kingston", "KC3000", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7000 MB/s", "write_speed": "6000 MB/s", "type": "TLC NAND"}, 89.99, 6.5),
        ("Kingston", "KC3000", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7000 MB/s", "write_speed": "7000 MB/s", "type": "TLC NAND"}, 169.99, 7.5),
        ("Kingston", "NV3", {"capacity": "500GB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "6000 MB/s", "write_speed": "4000 MB/s", "type": "TLC NAND"}, 49.99, 5.0),
        ("Kingston", "NV3", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "6000 MB/s", "write_speed": "5000 MB/s", "type": "TLC NAND"}, 79.99, 5.5),
        ("Kingston", "NV3", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "6000 MB/s", "write_speed": "5000 MB/s", "type": "TLC NAND"}, 149.99, 6.0),
    ]:
        cap = specs["capacity"]
        products.append({"name": f"{brand} {model} {cap} NVMe", "brand": brand, "category": "Storage", "subcategory_slug": "storage-nvme-ssd", "manufacturer": brand, "model": model, "price": price, "power_consumption": power, "specs": specs, "compatibility": {"interface": specs["interface"], "form_factor": "M.2 2280"}})

    # SATA SSDs
    for brand, model, specs, price, power in [
        ("Samsung", "870 EVO", {"capacity": "250GB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "530 MB/s", "type": "TLC NAND"}, 34.99, 2.5),
        ("Samsung", "870 EVO", {"capacity": "500GB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "530 MB/s", "type": "TLC NAND"}, 49.99, 2.5),
        ("Samsung", "870 EVO", {"capacity": "1TB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "530 MB/s", "type": "TLC NAND"}, 79.99, 3.5),
        ("Samsung", "870 EVO", {"capacity": "2TB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "530 MB/s", "type": "TLC NAND"}, 149.99, 3.5),
        ("Samsung", "870 EVO", {"capacity": "4TB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "530 MB/s", "type": "TLC NAND"}, 299.99, 4.5),
        ("Samsung", "870 QVO", {"capacity": "1TB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "530 MB/s", "type": "QLC NAND"}, 54.99, 3.5),
        ("Samsung", "870 QVO", {"capacity": "2TB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "530 MB/s", "type": "QLC NAND"}, 99.99, 3.5),
        ("Samsung", "870 QVO", {"capacity": "4TB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "530 MB/s", "type": "QLC NAND"}, 199.99, 4.5),
        ("Crucial", "MX500", {"capacity": "500GB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "510 MB/s", "type": "TLC NAND"}, 44.99, 2.5),
        ("Crucial", "MX500", {"capacity": "1TB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "510 MB/s", "type": "TLC NAND"}, 74.99, 3.5),
        ("Crucial", "MX500", {"capacity": "2TB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "510 MB/s", "type": "TLC NAND"}, 139.99, 3.5),
        ("Western Digital", "Blue SA510", {"capacity": "500GB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "520 MB/s", "type": "TLC NAND"}, 39.99, 2.5),
        ("Western Digital", "Blue SA510", {"capacity": "1TB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "520 MB/s", "type": "TLC NAND"}, 64.99, 3.5),
        ("Western Digital", "Blue SA510", {"capacity": "2TB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "520 MB/s", "type": "TLC NAND"}, 119.99, 3.5),
        ("TeamGroup", "CX2", {"capacity": "500GB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "480 MB/s", "type": "TLC NAND"}, 29.99, 2.5),
        ("TeamGroup", "CX2", {"capacity": "1TB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "500 MB/s", "type": "TLC NAND"}, 49.99, 3.5),
    ]:
        cap = specs["capacity"]
        products.append({"name": f"{brand} {model} {cap} SATA SSD", "brand": brand, "category": "Storage", "subcategory_slug": "storage-sata-ssd", "manufacturer": brand, "model": model, "price": price, "power_consumption": power, "specs": specs, "compatibility": {"interface": "SATA III", "form_factor": "2.5 inch"}})

    # HDDs
    for brand, model, specs, price, power in [
        ("Seagate", "Barracuda", {"capacity": "1TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "64MB"}, 34.99, 5.5),
        ("Seagate", "Barracuda", {"capacity": "2TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "256MB"}, 49.99, 6.5),
        ("Seagate", "Barracuda", {"capacity": "4TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "5400 RPM", "cache": "256MB"}, 69.99, 6.5),
        ("Seagate", "Barracuda", {"capacity": "8TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "5400 RPM", "cache": "256MB"}, 119.99, 7.5),
        ("Seagate", "IronWolf Pro", {"capacity": "4TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "256MB"}, 119.99, 7.5),
        ("Seagate", "IronWolf Pro", {"capacity": "8TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "256MB"}, 199.99, 8.5),
        ("Seagate", "IronWolf Pro", {"capacity": "16TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "512MB"}, 349.99, 9.5),
        ("Seagate", "IronWolf Pro", {"capacity": "24TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "512MB"}, 499.99, 10.5),
        ("Western Digital", "Blue", {"capacity": "1TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "64MB"}, 34.99, 5.5),
        ("Western Digital", "Blue", {"capacity": "2TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "256MB"}, 49.99, 6.5),
        ("Western Digital", "Blue", {"capacity": "4TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "5400 RPM", "cache": "256MB"}, 69.99, 6.5),
        ("Western Digital", "Black", {"capacity": "2TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "256MB"}, 99.99, 7.5),
        ("Western Digital", "Black", {"capacity": "4TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "256MB"}, 159.99, 8.5),
        ("Western Digital", "Red Pro", {"capacity": "4TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "256MB"}, 129.99, 7.5),
        ("Western Digital", "Red Pro", {"capacity": "8TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "256MB"}, 229.99, 8.5),
        ("Western Digital", "Red Pro", {"capacity": "20TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "512MB"}, 429.99, 9.5),
        ("Seagate", "Exos X20", {"capacity": "20TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "512MB"}, 399.99, 10.5),
        ("Seagate", "Exos X18", {"capacity": "16TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "256MB"}, 329.99, 9.5),
    ]:
        cap = specs["capacity"]
        products.append({"name": f"{brand} {model} {cap} HDD", "brand": brand, "category": "Storage", "subcategory_slug": "storage-hdd", "manufacturer": brand, "model": model, "price": price, "power_consumption": power, "specs": specs, "compatibility": {"interface": "SATA III", "form_factor": "3.5 inch"}})

    # Additional NVMe SSDs
    for brand, model, specs, price, power in [
        ("Samsung", "990 EVO Plus", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "7250 MB/s", "write_speed": "6300 MB/s", "type": "TLC NAND"}, 99.99, 6.5),
        ("Samsung", "990 EVO Plus", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "7250 MB/s", "write_speed": "6300 MB/s", "type": "TLC NAND"}, 179.99, 7.0),
        ("Samsung", "990 EVO Plus", {"capacity": "4TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "7250 MB/s", "write_speed": "6300 MB/s", "type": "TLC NAND"}, 349.99, 8.0),
        ("Western Digital", "Black SN7100", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "10000 MB/s", "write_speed": "8500 MB/s", "type": "TLC NAND"}, 149.99, 8.5),
        ("Western Digital", "Black SN7100", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "10000 MB/s", "write_speed": "8500 MB/s", "type": "TLC NAND"}, 259.99, 9.5),
        ("Corsair", "MP700 Pro", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "12400 MB/s", "write_speed": "11800 MB/s", "type": "TLC NAND"}, 249.99, 10.0),
        ("Corsair", "MP700 Pro", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "12400 MB/s", "write_speed": "11800 MB/s", "type": "TLC NAND"}, 429.99, 11.0),
        ("Corsair", "MP600 Elite", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7000 MB/s", "write_speed": "6200 MB/s", "type": "TLC NAND"}, 99.99, 6.5),
        ("Corsair", "MP600 Elite", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7000 MB/s", "write_speed": "6800 MB/s", "type": "TLC NAND"}, 179.99, 7.5),
        ("ADATA", "XPG Gammix S70 Blade", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7400 MB/s", "write_speed": "6400 MB/s", "type": "TLC NAND"}, 84.99, 6.5),
        ("ADATA", "XPG Gammix S70 Blade", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7400 MB/s", "write_speed": "6800 MB/s", "type": "TLC NAND"}, 159.99, 7.5),
        ("Solidigm", "P44 Pro", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7000 MB/s", "write_speed": "6500 MB/s", "type": "TLC NAND"}, 129.99, 7.0),
        ("Solidigm", "P44 Pro", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7000 MB/s", "write_speed": "6500 MB/s", "type": "TLC NAND"}, 229.99, 8.0),
        ("Sabrent", "Rocket 4 Plus", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7100 MB/s", "write_speed": "6600 MB/s", "type": "TLC NAND"}, 99.99, 6.5),
        ("Sabrent", "Rocket 4 Plus", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7100 MB/s", "write_speed": "6600 MB/s", "type": "TLC NAND"}, 179.99, 7.5),
        ("Sabrent", "Rocket 5", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "13000 MB/s", "write_speed": "10000 MB/s", "type": "TLC NAND"}, 299.99, 11.0),
        ("Sabrent", "Rocket 5", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "13000 MB/s", "write_speed": "10000 MB/s", "type": "TLC NAND"}, 499.99, 12.0),
    ]:
        cap = specs["capacity"]
        products.append({"name": f"{brand} {model} {cap} NVMe", "brand": brand, "category": "Storage", "subcategory_slug": "storage-nvme-ssd", "manufacturer": brand, "model": model, "price": price, "power_consumption": power, "specs": specs, "compatibility": {"interface": specs["interface"], "form_factor": "M.2 2280"}})

    # Extra NVMe drives
    for brand, model, specs, price, power in [
        ("Samsung", "990 Pro", {"capacity": "500GB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "6900 MB/s", "write_speed": "5000 MB/s", "type": "TLC NAND"}, 69.99, 5.5),
        ("Samsung", "9100 Pro", {"capacity": "4TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "14900 MB/s", "write_speed": "10000 MB/s", "type": "TLC NAND"}, 699.99, 12.0),
        ("Western Digital", "Black SN850X", {"capacity": "500GB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7300 MB/s", "write_speed": "4000 MB/s", "type": "TLC NAND"}, 69.99, 6.5),
        ("Crucial", "T700", {"capacity": "4TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "12400 MB/s", "write_speed": "11800 MB/s", "type": "TLC NAND"}, 699.99, 12.0),
        ("SK Hynix", "Platinum P41", {"capacity": "4TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7000 MB/s", "write_speed": "6500 MB/s", "type": "TLC NAND"}, 449.99, 9.0),
        ("Seagate", "FireCuda 540", {"capacity": "4TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "10000 MB/s", "write_speed": "10000 MB/s", "type": "TLC NAND"}, 699.99, 12.0),
        ("Kingston", "KC3000", {"capacity": "4TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7000 MB/s", "write_speed": "7000 MB/s", "type": "TLC NAND"}, 349.99, 8.5),
        ("Corsair", "MP700 Pro", {"capacity": "4TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "12400 MB/s", "write_speed": "11800 MB/s", "type": "TLC NAND"}, 749.99, 12.0),
        ("ADATA", "XPG Gammix S70 Blade", {"capacity": "4TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7400 MB/s", "write_speed": "6800 MB/s", "type": "TLC NAND"}, 329.99, 8.5),
        ("Sabrent", "Rocket 5", {"capacity": "4TB", "form_factor": "M.2 2280", "interface": "PCIe 5.0 x4 NVMe", "read_speed": "13000 MB/s", "write_speed": "10000 MB/s", "type": "TLC NAND"}, 899.99, 13.0),
        ("TeamGroup", "MP44", {"capacity": "1TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7400 MB/s", "write_speed": "6200 MB/s", "type": "TLC NAND"}, 79.99, 6.0),
        ("TeamGroup", "MP44", {"capacity": "2TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7400 MB/s", "write_speed": "6200 MB/s", "type": "TLC NAND"}, 149.99, 7.0),
        ("TeamGroup", "MP44", {"capacity": "4TB", "form_factor": "M.2 2280", "interface": "PCIe 4.0 x4 NVMe", "read_speed": "7400 MB/s", "write_speed": "6200 MB/s", "type": "TLC NAND"}, 299.99, 8.0),
        ("Samsung", "870 EVO", {"capacity": "8TB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "530 MB/s", "type": "TLC NAND"}, 599.99, 5.5),
        ("Crucial", "MX500", {"capacity": "4TB", "form_factor": "2.5 inch", "interface": "SATA III", "read_speed": "560 MB/s", "write_speed": "510 MB/s", "type": "TLC NAND"}, 299.99, 4.5),
        ("Seagate", "Barracuda", {"capacity": "16TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "5400 RPM", "cache": "512MB"}, 259.99, 8.5),
        ("Seagate", "Barracuda", {"capacity": "22TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "512MB"}, 399.99, 9.5),
        ("Western Digital", "Blue", {"capacity": "8TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "5400 RPM", "cache": "256MB"}, 129.99, 7.5),
        ("Western Digital", "Red Pro", {"capacity": "24TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "512MB"}, 499.99, 10.5),
        ("Seagate", "SkyHawk AI", {"capacity": "16TB", "form_factor": "3.5 inch", "interface": "SATA III", "rpm": "7200 RPM", "cache": "512MB"}, 319.99, 9.5),
    ]:
        cap = specs["capacity"]
        products.append({"name": f"{brand} {model} {cap} {'NVMe' if 'NVMe' in specs.get('interface','') else ('SSD' if 'SATA' in specs.get('interface','') and 'SSD' not in model else 'HDD')}", "brand": brand, "category": "Storage", "subcategory_slug": "storage-nvme-ssd" if "NVMe" in specs.get('interface','') else "storage-sata-ssd" if 'SATA' in specs.get('interface','') else "storage-hdd", "manufacturer": brand, "model": model, "price": price, "power_consumption": power, "specs": specs, "compatibility": {"interface": specs.get('interface','SATA III'), "form_factor": specs["form_factor"]}})

    return products
