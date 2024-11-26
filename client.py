import asyncio
import websockets

async def client():
    uri = "ws://localhost:8765"
    
    async with websockets.connect(uri) as websocket:
        while True:
            command = input("Enter a command: ")
            
            if command.lower() == 'exit':
                print("Exiting...")
                break
            
            try:
                await websocket.send(command)
                
                response = await websocket.recv()
                print(f"Server response: {response}")

            except websockets.exceptions.ConnectionClosed:
                print("Connection closed by server.")

        await websocket.close()

if __name__ == "__main__":
    asyncio.run(client())
