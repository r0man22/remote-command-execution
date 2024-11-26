import asyncio
from websockets import serve
import subprocess

def execute_command(command):
	try:
		result = subprocess.run(command, shell=True, text=True, capture_output=True)
		return result.stdout
	except subprocess.CalledProcessError as e:
		return e

async def handle_client(websocket):
	async for command in websocket:
		print(f"Executing: {command}")
		output = execute_command(command)
		await websocket.send(output)

async def main():
	async with serve(handle_client, "localhost", 8765):
		await asyncio.Future()

if __name__ == "__main__":
	asyncio.run(main())
