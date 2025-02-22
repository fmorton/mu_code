import asyncio
from bleak import BleakScanner, BleakClient

async def detect_ble_device_type(device_address):
    try:
        device = await BleakScanner.find_device_by_address(device_address)
        if device:
            print(f"Device found: {device.name} ({device.address})")

            async with BleakClient(device) as client:
                if client.is_connected:
                    print("Connected")
                    services = await client.get_services()
                    for service in services:
                        print(f"  Service: {service.uuid}")
                        if "180A" in service.uuid:  # Check for Device Information Service
                            for char in service.characteristics:
                                print(f"    Characteristic: {char.uuid}")
                                if "2A29" in char.uuid:  # Check for Manufacturer Name String
                                    manufacturer_bytes = await client.read_gatt_char(char.uuid)
                                    manufacturer = manufacturer_bytes.decode("utf-8")
                                    print(f"    Manufacturer: {manufacturer}")

                else:
                    print("Failed to connect")

        else:
            print("Device not found")
    except Exception as e:
         print(f"An error occurred: {e}")

device_address = "DE22C91F-84A3-944D-8653-021AB96CB12A" # Replace with the actual device address
asyncio.run(detect_ble_device_type(device_address))
