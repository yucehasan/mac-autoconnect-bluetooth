import asyncio
from bleak import BleakScanner, BleakClient

NAME = "" # Name of the device to find

async def find_mouse():
    """Scan and find nearby Bluetooth Low Energy (BLE) devices."""
    devices = await BleakScanner.discover()
    
    print("Discovered BLE Devices:")
    for device in devices:
        if device.name and NAME in device.name:
            print(f"Name: {device.name}, Address: {device.address}")
            return device.address
    
    return None

async def connect_mouse(device_address):
    """Connect to a Bluetooth Low Energy (BLE) device using its address."""
    async with BleakClient(device_address) as client:
        print(f"Connecting to {device_address}...")
        await client.connect()
            

def main():
    device_address = asyncio.run(find_mouse())
    if device_address:
        asyncio.run(connect_mouse(device_address))
    else:
        print(f"Could not find a device named {NAME}.")
        
        
if __name__ == "__main__":
    main()