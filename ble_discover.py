import asyncio

from bleak import BleakScanner, BleakClient


async def discover_devices():
    devices = await BleakScanner.discover()
    for device in devices:
        if device.name is None:
            continue
        if device.name[0:2] != "BB":
            continue

        print(f"Device Name: {device.name}, Address: {device.address}, {dir(device)}")

        ble_device = await BleakScanner.find_device_by_address(device.address)
        print("ble_device", ble_device)
        print("ble_device", dir(ble_device))
        print("ble_device.metadata", ble_device.metadata)
        print("ble_device.details", ble_device.details)

        MODEL_NBR_UUID = "2A24"

        # 3async with BleakClient(ble_device) as client:
        #    print(client)
        async with BleakClient(device.address) as client:
            model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))


if __name__ == "__main__":
    asyncio.run(discover_devices())
