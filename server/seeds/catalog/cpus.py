def generate_cpus() -> list[dict]:
    products = []

    # AMD Ryzen 9000 (Zen 5) - AM5
    for name, model, price, tdp, cores, threads, base, boost, cache, power_str in [
        ("AMD Ryzen 9 9950X", "Ryzen 9 9950X", 649.99, 170, 16, 32, "4.3 GHz", "5.7 GHz", "64MB", "170W"),
        ("AMD Ryzen 9 9900X", "Ryzen 9 9900X", 499.99, 120, 12, 24, "4.4 GHz", "5.6 GHz", "64MB", "120W"),
        ("AMD Ryzen 7 9800X3D", "Ryzen 7 9800X3D", 479.99, 120, 8, 16, "4.7 GHz", "5.2 GHz", "96MB (3D V-Cache)", "120W"),
        ("AMD Ryzen 7 9700X", "Ryzen 7 9700X", 359.99, 65, 8, 16, "3.8 GHz", "5.5 GHz", "32MB", "65W"),
        ("AMD Ryzen 5 9600X", "Ryzen 5 9600X", 279.99, 65, 6, 12, "3.9 GHz", "5.4 GHz", "32MB", "65W"),
    ]:
        products.append({"name": name, "brand": "AMD", "category": "CPU", "subcategory_slug": "cpus-amd-ryzen", "manufacturer": "AMD", "model": model, "price": price, "power_consumption": tdp, "specs": {"architecture": "Zen 5", "cores": cores, "threads": threads, "base_clock": base, "boost_clock": boost, "socket": "AM5", "l3_cache": cache, "tdp": power_str}, "compatibility": {"socket": "AM5", "chipset": "X870E, X670E, B650, A620", "memory_type": "DDR5"}})

    # AMD Ryzen 7000 (Zen 4) - AM5
    for name, model, price, tdp, cores, threads, base, boost, cache, power_str in [
        ("AMD Ryzen 9 7950X", "Ryzen 9 7950X", 549.99, 170, 16, 32, "4.5 GHz", "5.7 GHz", "64MB", "170W"),
        ("AMD Ryzen 9 7950X3D", "Ryzen 9 7950X3D", 699.99, 120, 16, 32, "4.2 GHz", "5.7 GHz", "128MB (3D V-Cache)", "120W"),
        ("AMD Ryzen 9 7900X", "Ryzen 9 7900X", 449.99, 170, 12, 24, "4.7 GHz", "5.6 GHz", "64MB", "170W"),
        ("AMD Ryzen 9 7900X3D", "Ryzen 9 7900X3D", 599.99, 120, 12, 24, "4.4 GHz", "5.6 GHz", "128MB (3D V-Cache)", "120W"),
        ("AMD Ryzen 7 7800X3D", "Ryzen 7 7800X3D", 389.99, 120, 8, 16, "4.2 GHz", "5.0 GHz", "96MB (3D V-Cache)", "120W"),
        ("AMD Ryzen 7 7700X", "Ryzen 7 7700X", 349.99, 105, 8, 16, "4.5 GHz", "5.4 GHz", "32MB", "105W"),
        ("AMD Ryzen 5 7600X", "Ryzen 5 7600X", 219.99, 105, 6, 12, "4.7 GHz", "5.3 GHz", "32MB", "105W"),
        ("AMD Ryzen 5 7600", "Ryzen 5 7600", 199.99, 65, 6, 12, "3.8 GHz", "5.1 GHz", "32MB", "65W"),
    ]:
        products.append({"name": name, "brand": "AMD", "category": "CPU", "subcategory_slug": "cpus-amd-ryzen", "manufacturer": "AMD", "model": model, "price": price, "power_consumption": tdp, "specs": {"architecture": "Zen 4", "cores": cores, "threads": threads, "base_clock": base, "boost_clock": boost, "socket": "AM5", "l3_cache": cache, "tdp": power_str}, "compatibility": {"socket": "AM5", "chipset": "X670E, B650, A620", "memory_type": "DDR5"}})

    # AMD Ryzen 5000 (Zen 3) - AM4
    for name, model, price, tdp, cores, threads, base, boost, cache, power_str in [
        ("AMD Ryzen 9 5950X", "Ryzen 9 5950X", 499.99, 105, 16, 32, "3.4 GHz", "4.9 GHz", "64MB", "105W"),
        ("AMD Ryzen 9 5900X", "Ryzen 9 5900X", 399.99, 105, 12, 24, "3.7 GHz", "4.8 GHz", "64MB", "105W"),
        ("AMD Ryzen 7 5800X3D", "Ryzen 7 5800X3D", 329.99, 105, 8, 16, "3.4 GHz", "4.5 GHz", "96MB (3D V-Cache)", "105W"),
        ("AMD Ryzen 7 5800X", "Ryzen 7 5800X", 299.99, 105, 8, 16, "3.8 GHz", "4.7 GHz", "32MB", "105W"),
        ("AMD Ryzen 5 5600X", "Ryzen 5 5600X", 199.99, 65, 6, 12, "3.7 GHz", "4.6 GHz", "32MB", "65W"),
        ("AMD Ryzen 5 5600", "Ryzen 5 5600", 179.99, 65, 6, 12, "3.5 GHz", "4.4 GHz", "32MB", "65W"),
        ("AMD Ryzen 3 5100", "Ryzen 3 5100", 99.99, 65, 4, 8, "3.8 GHz", "4.2 GHz", "16MB", "65W"),
    ]:
        products.append({"name": name, "brand": "AMD", "category": "CPU", "subcategory_slug": "cpus-amd-ryzen", "manufacturer": "AMD", "model": model, "price": price, "power_consumption": tdp, "specs": {"architecture": "Zen 3", "cores": cores, "threads": threads, "base_clock": base, "boost_clock": boost, "socket": "AM4", "l3_cache": cache, "tdp": power_str}, "compatibility": {"socket": "AM4", "chipset": "X570, B550, A520", "memory_type": "DDR4"}})

    # AMD Threadripper
    for name, model, price, tdp, cores, threads, base, boost, cache, power_str in [
        ("AMD Threadripper 7980X", "Threadripper 7980X", 4999.99, 350, 64, 128, "3.2 GHz", "5.1 GHz", "384MB", "350W"),
        ("AMD Threadripper 7970X", "Threadripper 7970X", 2999.99, 350, 32, 64, "3.5 GHz", "5.3 GHz", "160MB", "350W"),
        ("AMD Threadripper 7960X", "Threadripper 7960X", 2499.99, 350, 24, 48, "3.7 GHz", "5.3 GHz", "152MB", "350W"),
    ]:
        products.append({"name": name, "brand": "AMD", "category": "CPU", "subcategory_slug": "cpus-amd-ryzen", "manufacturer": "AMD", "model": model, "price": price, "power_consumption": tdp, "specs": {"architecture": "Zen 4", "cores": cores, "threads": threads, "base_clock": base, "boost_clock": boost, "socket": "sTR5", "l3_cache": cache, "tdp": power_str}, "compatibility": {"socket": "sTR5", "chipset": "TRX50, WRX90", "memory_type": "DDR5"}})

    # Intel Core Ultra 200 (Arrow Lake) - LGA1851
    for name, model, price, tdp, cores_str, threads, base, boost, cache, power_str in [
        ("Intel Core Ultra 9 285K", "Core Ultra 9 285K", 589.99, 250, "24 (8P+16E)", 24, "3.7 GHz", "5.7 GHz", "36MB", "250W"),
        ("Intel Core Ultra 7 265K", "Core Ultra 7 265K", 399.99, 250, "20 (8P+12E)", 20, "3.9 GHz", "5.5 GHz", "30MB", "250W"),
        ("Intel Core Ultra 7 265KF", "Core Ultra 7 265KF", 379.99, 250, "20 (8P+12E)", 20, "3.9 GHz", "5.5 GHz", "30MB", "250W"),
        ("Intel Core Ultra 5 245K", "Core Ultra 5 245K", 299.99, 159, "14 (6P+8E)", 14, "4.2 GHz", "5.2 GHz", "24MB", "159W"),
        ("Intel Core Ultra 5 245KF", "Core Ultra 5 245KF", 279.99, 159, "14 (6P+8E)", 14, "4.2 GHz", "5.2 GHz", "24MB", "159W"),
    ]:
        products.append({"name": name, "brand": "Intel", "category": "CPU", "subcategory_slug": "cpus-intel-core", "manufacturer": "Intel", "model": model, "price": price, "power_consumption": tdp, "specs": {"architecture": "Arrow Lake", "cores": cores_str, "threads": threads, "base_clock": base, "boost_clock": boost, "socket": "LGA1851", "l3_cache": cache, "tdp": power_str}, "compatibility": {"socket": "LGA1851", "chipset": "Z890, B860", "memory_type": "DDR5"}})

    # Intel 14th Gen (Raptor Lake Refresh) - LGA1700
    for name, model, price, tdp, cores_str, threads, base, boost, cache, power_str in [
        ("Intel Core i9-14900K", "Core i9-14900K", 589.99, 253, "24 (8P+16E)", 32, "3.2 GHz", "6.0 GHz", "36MB", "253W"),
        ("Intel Core i9-14900KF", "Core i9-14900KF", 559.99, 253, "24 (8P+16E)", 32, "3.2 GHz", "6.0 GHz", "36MB", "253W"),
        ("Intel Core i9-14900", "Core i9-14900", 549.99, 219, "24 (8P+16E)", 32, "2.0 GHz", "5.8 GHz", "36MB", "219W"),
        ("Intel Core i9-14900F", "Core i9-14900F", 519.99, 219, "24 (8P+16E)", 32, "2.0 GHz", "5.8 GHz", "36MB", "219W"),
        ("Intel Core i9-14900T", "Core i9-14900T", 529.99, 35, "24 (8P+16E)", 32, "1.1 GHz", "5.5 GHz", "36MB", "35W"),
        ("Intel Core i7-14700K", "Core i7-14700K", 409.99, 253, "20 (8P+12E)", 28, "3.4 GHz", "5.6 GHz", "33MB", "253W"),
        ("Intel Core i7-14700KF", "Core i7-14700KF", 384.99, 253, "20 (8P+12E)", 28, "3.4 GHz", "5.6 GHz", "33MB", "253W"),
        ("Intel Core i7-14700", "Core i7-14700", 369.99, 219, "20 (8P+12E)", 28, "2.1 GHz", "5.4 GHz", "33MB", "219W"),
        ("Intel Core i7-14700F", "Core i7-14700F", 349.99, 219, "20 (8P+12E)", 28, "2.1 GHz", "5.4 GHz", "33MB", "219W"),
        ("Intel Core i5-14600K", "Core i5-14600K", 319.99, 181, "14 (6P+8E)", 20, "3.5 GHz", "5.3 GHz", "24MB", "181W"),
        ("Intel Core i5-14600KF", "Core i5-14600KF", 299.99, 181, "14 (6P+8E)", 20, "3.5 GHz", "5.3 GHz", "24MB", "181W"),
        ("Intel Core i5-14500", "Core i5-14500", 219.99, 154, "14 (6P+8E)", 20, "2.6 GHz", "5.0 GHz", "24MB", "154W"),
        ("Intel Core i5-14400", "Core i5-14400", 189.99, 148, "10 (6P+4E)", 16, "2.5 GHz", "4.7 GHz", "20MB", "148W"),
        ("Intel Core i5-14400F", "Core i5-14400F", 169.99, 148, "10 (6P+4E)", 16, "2.5 GHz", "4.7 GHz", "20MB", "148W"),
        ("Intel Core i3-14100", "Core i3-14100", 149.99, 110, "4 (4P+0E)", 8, "3.5 GHz", "4.7 GHz", "12MB", "110W"),
        ("Intel Core i3-14100F", "Core i3-14100F", 119.99, 110, "4 (4P+0E)", 8, "3.5 GHz", "4.7 GHz", "12MB", "110W"),
    ]:
        products.append({"name": name, "brand": "Intel", "category": "CPU", "subcategory_slug": "cpus-intel-core", "manufacturer": "Intel", "model": model, "price": price, "power_consumption": tdp, "specs": {"architecture": "Raptor Lake Refresh", "cores": cores_str, "threads": threads, "base_clock": base, "boost_clock": boost, "socket": "LGA1700", "l3_cache": cache, "tdp": power_str}, "compatibility": {"socket": "LGA1700", "chipset": "Z790, Z690, B760, H610", "memory_type": "DDR5, DDR4"}})

    # Intel 13th Gen (Raptor Lake) - LGA1700
    for name, model, price, tdp, cores_str, threads, base, boost, cache, power_str in [
        ("Intel Core i9-13900K", "Core i9-13900K", 549.99, 253, "24 (8P+16E)", 32, "3.0 GHz", "5.8 GHz", "36MB", "253W"),
        ("Intel Core i9-13900KF", "Core i9-13900KF", 519.99, 253, "24 (8P+16E)", 32, "3.0 GHz", "5.8 GHz", "36MB", "253W"),
        ("Intel Core i9-13900", "Core i9-13900", 499.99, 219, "24 (8P+16E)", 32, "2.0 GHz", "5.6 GHz", "36MB", "219W"),
        ("Intel Core i7-13700K", "Core i7-13700K", 379.99, 253, "16 (8P+8E)", 24, "3.4 GHz", "5.4 GHz", "30MB", "253W"),
        ("Intel Core i7-13700KF", "Core i7-13700KF", 349.99, 253, "16 (8P+8E)", 24, "3.4 GHz", "5.4 GHz", "30MB", "253W"),
        ("Intel Core i7-13700", "Core i7-13700", 349.99, 219, "16 (8P+8E)", 24, "2.1 GHz", "5.2 GHz", "30MB", "219W"),
        ("Intel Core i5-13600K", "Core i5-13600K", 289.99, 181, "14 (6P+8E)", 20, "3.5 GHz", "5.1 GHz", "24MB", "181W"),
        ("Intel Core i5-13600KF", "Core i5-13600KF", 269.99, 181, "14 (6P+8E)", 20, "3.5 GHz", "5.1 GHz", "24MB", "181W"),
        ("Intel Core i5-13500", "Core i5-13500", 239.99, 154, "14 (6P+8E)", 20, "2.5 GHz", "4.8 GHz", "24MB", "154W"),
        ("Intel Core i5-13400", "Core i5-13400", 219.99, 148, "10 (6P+4E)", 16, "2.5 GHz", "4.6 GHz", "20MB", "148W"),
        ("Intel Core i5-13400F", "Core i5-13400F", 199.99, 148, "10 (6P+4E)", 16, "2.5 GHz", "4.6 GHz", "20MB", "148W"),
        ("Intel Core i3-13100", "Core i3-13100", 139.99, 110, "4 (4P+0E)", 8, "3.4 GHz", "4.5 GHz", "12MB", "110W"),
        ("Intel Core i3-13100F", "Core i3-13100F", 119.99, 110, "4 (4P+0E)", 8, "3.4 GHz", "4.5 GHz", "12MB", "110W"),
    ]:
        products.append({"name": name, "brand": "Intel", "category": "CPU", "subcategory_slug": "cpus-intel-core", "manufacturer": "Intel", "model": model, "price": price, "power_consumption": tdp, "specs": {"architecture": "Raptor Lake", "cores": cores_str, "threads": threads, "base_clock": base, "boost_clock": boost, "socket": "LGA1700", "l3_cache": cache, "tdp": power_str}, "compatibility": {"socket": "LGA1700", "chipset": "Z790, Z690, B760, H610", "memory_type": "DDR5, DDR4"}})

    # Intel 12th Gen (Alder Lake) - LGA1700
    for name, model, price, tdp, cores_str, threads, base, boost, cache, power_str in [
        ("Intel Core i9-12900K", "Core i9-12900K", 399.99, 241, "16 (8P+8E)", 24, "3.2 GHz", "5.2 GHz", "30MB", "241W"),
        ("Intel Core i9-12900KF", "Core i9-12900KF", 379.99, 241, "16 (8P+8E)", 24, "3.2 GHz", "5.2 GHz", "30MB", "241W"),
        ("Intel Core i9-12900", "Core i9-12900", 359.99, 202, "16 (8P+8E)", 24, "2.4 GHz", "5.1 GHz", "30MB", "202W"),
        ("Intel Core i7-12700K", "Core i7-12700K", 299.99, 190, "12 (8P+4E)", 20, "3.6 GHz", "5.0 GHz", "25MB", "190W"),
        ("Intel Core i7-12700KF", "Core i7-12700KF", 279.99, 190, "12 (8P+4E)", 20, "3.6 GHz", "5.0 GHz", "25MB", "190W"),
        ("Intel Core i7-12700", "Core i7-12700", 269.99, 180, "12 (8P+4E)", 20, "2.1 GHz", "4.9 GHz", "25MB", "180W"),
        ("Intel Core i5-12600K", "Core i5-12600K", 229.99, 150, "10 (6P+4E)", 16, "3.7 GHz", "4.9 GHz", "20MB", "150W"),
        ("Intel Core i5-12600KF", "Core i5-12600KF", 209.99, 150, "10 (6P+4E)", 16, "3.7 GHz", "4.9 GHz", "20MB", "150W"),
        ("Intel Core i5-12400", "Core i5-12400", 179.99, 117, "6 (6P+0E)", 12, "2.5 GHz", "4.4 GHz", "18MB", "117W"),
        ("Intel Core i5-12400F", "Core i5-12400F", 149.99, 117, "6 (6P+0E)", 12, "2.5 GHz", "4.4 GHz", "18MB", "117W"),
        ("Intel Core i3-12100", "Core i3-12100", 119.99, 89, "4 (4P+0E)", 8, "3.3 GHz", "4.3 GHz", "12MB", "89W"),
        ("Intel Core i3-12100F", "Core i3-12100F", 99.99, 89, "4 (4P+0E)", 8, "3.3 GHz", "4.3 GHz", "12MB", "89W"),
    ]:
        products.append({"name": name, "brand": "Intel", "category": "CPU", "subcategory_slug": "cpus-intel-core", "manufacturer": "Intel", "model": model, "price": price, "power_consumption": tdp, "specs": {"architecture": "Alder Lake", "cores": cores_str, "threads": threads, "base_clock": base, "boost_clock": boost, "socket": "LGA1700", "l3_cache": cache, "tdp": power_str}, "compatibility": {"socket": "LGA1700", "chipset": "Z690, B660, H610", "memory_type": "DDR5, DDR4"}})

    # Server CPUs
    for name, model, price, tdp, cores, threads, base, boost, socket, cache, power_str, arch in [
        ("AMD EPYC 9654", "EPYC 9654", 11850.00, 360, 96, 192, "2.4 GHz", "3.7 GHz", "SP5", "384MB", "360W", "Zen 4"),
        ("AMD EPYC 9554", "EPYC 9554", 8800.00, 360, 64, 128, "2.55 GHz", "3.75 GHz", "SP5", "256MB", "360W", "Zen 4"),
        ("AMD EPYC 9454", "EPYC 9454", 5250.00, 300, 48, 96, "2.75 GHz", "3.8 GHz", "SP5", "256MB", "300W", "Zen 4"),
        ("AMD EPYC 9354", "EPYC 9354", 3580.00, 280, 32, 64, "3.25 GHz", "3.8 GHz", "SP5", "256MB", "280W", "Zen 4"),
        ("AMD EPYC 9254", "EPYC 9254", 2485.00, 200, 24, 48, "2.9 GHz", "4.15 GHz", "SP5", "128MB", "200W", "Zen 4"),
        ("AMD EPYC 9174F", "EPYC 9174F", 3850.00, 320, 16, 32, "4.1 GHz", "4.4 GHz", "SP5", "256MB", "320W", "Zen 4"),
        ("Intel Xeon Platinum 8592+", "Xeon Platinum 8592+", 8900.00, 350, 64, 128, "1.9 GHz", "3.9 GHz", "LGA4677", "128MB", "350W", "Emerald Rapids"),
        ("Intel Xeon Platinum 8490H", "Xeon Platinum 8490H", 17850.00, 350, 60, 120, "1.9 GHz", "3.5 GHz", "LGA4677", "112MB", "350W", "Sapphire Rapids"),
        ("Intel Xeon Gold 6558Q", "Xeon Gold 6558Q", 4200.00, 350, 48, 96, "2.1 GHz", "3.9 GHz", "LGA4677", "120MB", "350W", "Emerald Rapids"),
        ("Intel Xeon Gold 6438M", "Xeon Gold 6438M", 3200.00, 260, 32, 64, "2.1 GHz", "3.9 GHz", "LGA4677", "112MB", "260W", "Sapphire Rapids"),
        ("Intel Xeon Silver 4516Y+", "Xeon Silver 4516Y+", 1800.00, 225, 24, 48, "2.2 GHz", "3.8 GHz", "LGA4677", "64MB", "225W", "Emerald Rapids"),
        ("Intel Xeon Silver 4416+", "Xeon Silver 4416+", 1200.00, 200, 20, 40, "2.0 GHz", "3.9 GHz", "LGA4677", "60MB", "200W", "Sapphire Rapids"),
        ("Intel Xeon E-2488", "Xeon E-2488", 650.00, 95, 8, 16, "3.2 GHz", "5.6 GHz", "LGA1700", "24MB", "95W", "Raptor Lake"),
        ("Intel Xeon E-2434", "Xeon E-2434", 350.00, 65, 4, 8, "3.4 GHz", "5.0 GHz", "LGA1700", "12MB", "65W", "Raptor Lake"),
    ]:
        brand = "AMD" if "AMD" in name else "Intel"
        products.append({"name": name, "brand": brand, "category": "CPU", "subcategory_slug": "cpus-server", "manufacturer": brand, "model": model, "price": price, "power_consumption": tdp, "specs": {"architecture": arch, "cores": cores, "threads": threads, "base_clock": base, "boost_clock": boost, "socket": socket, "l3_cache": cache, "tdp": power_str}, "compatibility": {"socket": socket, "chipset": "Server Platform", "memory_type": "DDR5"}})

    # Budget CPUs
    for name, model, price, tdp, cores, threads, base, boost, socket, cache in [
        ("Intel Pentium Gold G7400", "Pentium G7400", 84.99, 46, 2, 4, "3.7 GHz", "3.7 GHz", "LGA1700", "6MB"),
        ("Intel Celeron G6900", "Celeron G6900", 49.99, 46, 2, 2, "3.4 GHz", "3.4 GHz", "LGA1700", "4MB"),
        ("Intel Pentium Gold G6605", "Pentium G6605", 79.99, 58, 2, 4, "4.3 GHz", "4.3 GHz", "LGA1200", "4MB"),
        ("Intel Celeron G5925", "Celeron G5925", 49.99, 58, 2, 2, "3.6 GHz", "3.6 GHz", "LGA1200", "2MB"),
        ("AMD Athlon 3000G", "Athlon 3000G", 49.99, 35, 2, 4, "3.5 GHz", "3.5 GHz", "AM4", "4MB"),
        ("AMD Athlon 200GE", "Athlon 200GE", 54.99, 35, 2, 4, "3.2 GHz", "3.2 GHz", "AM4", "4MB"),
        ("AMD Ryzen 3 4100", "Ryzen 3 4100", 119.99, 65, 4, 8, "3.8 GHz", "4.0 GHz", "AM4", "4MB"),
        ("AMD Ryzen 5 4500", "Ryzen 5 4500", 129.99, 65, 6, 12, "3.6 GHz", "4.1 GHz", "AM4", "8MB"),
    ]:
        products.append({"name": name, "brand": "Intel" if "Intel" in name else "AMD", "category": "CPU", "subcategory_slug": "cpus-intel-core" if "Intel" in name else "cpus-amd-ryzen", "manufacturer": "Intel" if "Intel" in name else "AMD", "model": model, "price": price, "power_consumption": tdp, "specs": {"architecture": "Budget", "cores": cores, "threads": threads, "base_clock": base, "boost_clock": boost, "socket": socket, "l3_cache": cache, "tdp": f"{tdp}W"}, "compatibility": {"socket": socket, "chipset": "Entry Level", "memory_type": "DDR4, DDR5" if "LGA1700" in socket else "DDR4"}})

    # Intel Core Ultra 200 non-K
    for name, model, price, tdp, cores_str, threads, base, boost in [
        ("Intel Core Ultra 7 265", "Core Ultra 7 265", 349.99, 175, "20 (8P+12E)", 20, "2.5 GHz", "5.3 GHz"),
    ]:
        products.append({"name": name, "brand": "Intel", "category": "CPU", "subcategory_slug": "cpus-intel-core", "manufacturer": "Intel", "model": model, "price": price, "power_consumption": tdp, "specs": {"architecture": "Arrow Lake", "cores": cores_str, "threads": threads, "base_clock": base, "boost_clock": boost, "socket": "LGA1851", "l3_cache": "30MB", "tdp": f"{tdp}W"}, "compatibility": {"socket": "LGA1851", "chipset": "Z890, B860", "memory_type": "DDR5"}})

    # AMD Ryzen 5000 additional
    for name, model, price, tdp, cores, threads, base, boost, cache, power_str in [
        ("AMD Ryzen 7 5700X3D", "Ryzen 7 5700X3D", 249.99, 105, 8, 16, "3.0 GHz", "4.1 GHz", "96MB (3D V-Cache)", "105W"),
        ("AMD Ryzen 7 5700X", "Ryzen 7 5700X", 219.99, 65, 8, 16, "3.4 GHz", "4.6 GHz", "32MB", "65W"),
        ("AMD Ryzen 5 5500", "Ryzen 5 5500", 124.99, 65, 6, 12, "3.6 GHz", "4.2 GHz", "16MB", "65W"),
        ("AMD Ryzen 5 4600G", "Ryzen 5 4600G", 109.99, 65, 6, 12, "3.7 GHz", "4.2 GHz", "8MB", "65W"),
        ("AMD Ryzen 5 5600GT", "Ryzen 5 5600GT", 139.99, 65, 6, 12, "3.6 GHz", "4.6 GHz", "16MB", "65W"),
        ("AMD Ryzen 7 8700F", "Ryzen 7 8700F", 279.99, 65, 8, 16, "4.1 GHz", "5.0 GHz", "16MB", "65W"),
        ("AMD Ryzen 5 8400F", "Ryzen 5 8400F", 169.99, 65, 6, 12, "4.2 GHz", "4.7 GHz", "16MB", "65W"),
    ]:
        products.append({"name": name, "brand": "AMD", "category": "CPU", "subcategory_slug": "cpus-amd-ryzen", "manufacturer": "AMD", "model": model, "price": price, "power_consumption": tdp, "specs": {"architecture": "Zen 3" if "5" in model[model.find('5'):model.find('5')+1] and not any(x in model for x in ['8400F','8700F']) else "Zen 4", "cores": cores, "threads": threads, "base_clock": base, "boost_clock": boost, "socket": "AM4", "l3_cache": cache, "tdp": power_str}, "compatibility": {"socket": "AM4", "chipset": "X570, B550, A520", "memory_type": "DDR4"}})

    # Intel N100/N150 budget
    for name, model, price, tdp, cores, threads in [
        ("Intel Processor N100", "N100", 39.99, 6, 4, 4),
        ("Intel Processor N150", "N150", 44.99, 6, 4, 4),
        ("Intel Processor N200", "N200", 49.99, 6, 4, 4),
        ("Intel Core i3-N305", "Core i3-N305", 89.99, 15, 8, 8),
    ]:
        products.append({"name": name, "brand": "Intel", "category": "CPU", "subcategory_slug": "cpus-intel-core", "manufacturer": "Intel", "model": model, "price": price, "power_consumption": tdp, "specs": {"architecture": "Alder Lake-N", "cores": cores, "threads": threads, "base_clock": "0.8 GHz", "boost_clock": "3.4 GHz", "socket": "FCBGA1264", "l3_cache": "6MB", "tdp": f"{tdp}W"}, "compatibility": {"socket": "FCBGA1264", "chipset": "Integrated", "memory_type": "DDR4, DDR5"}})

    return products
