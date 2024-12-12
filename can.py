import aiohttp
import json
import os
import asyncio
from tls_client import Session
import re, requests
import time

k1 = 'ur self acc token'
k2 = 'vanity receiver server id'
k3 = 'ur acc password'

o1 = {
    'z1': 'tager server vanity',
}

def x1() -> int: 
        x2 = None
        try:
            x3 = re.findall(r'<script\s+src="([^"]+\.js)"\s+defer>\s*</script>', requests.get("https://discord.com/login").text)
            for x4 in x3:
                x5 = requests.get(f"https://discord.com/{x4}")
                if "buildNumber" not in x5.text:
                    continue
                else:
                    x2 = x5.text.split('build_number:"')[1].split('"')[0]
                    break
            return x2
        except:
            return None

class A1:
    def __init__(self, k1: str) -> None:
        self.k1 = k1
        self.x6 = None
        self.x7 = None
        self.x8 = None
        self.x9 = []
        self.x10 = None
        self.session = Session(client_identifier='chrome_117', random_tls_extension_order=True)

    def y1(self, k3, x11, x12):
        x13 = "https://discord.com/api/v9/mfa/finish"
        x14 = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': self.k1,
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'priority': 'u=1, i',
        'referer': 'https://discord.com/channels/@me',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-discord-timezone': 'America/New_York',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyOC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI4LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMyODY5NywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
    }
        x15 = {
            'ticket': x11,
            'mfa_type': 'password',
            'data': k3,
        }
        try:
            x16 = self.session.post(x13, json=x15, headers=x14, cookies=x12)
            return x16.json()['token'], x16.cookies.get('__Secure-recent_mfa')
        except:
            return None

    async def y2(self, x17, k3):
        x18 = f"https://discord.com/api/v9/guilds/{k2}/vanity-url"
        x19 = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': self.k1,
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'priority': 'u=1, i',
        'referer': 'https://discord.com/channels/@me',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-discord-timezone': 'America/New_York',
        'x-discord-mfa-authorization': self.x10,
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyOC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI4LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMyODY5NywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
        }
    
        try:
            x20 = self.session.patch(x18, json={'code': x17}, headers=x19)
            if x20.status_code == 200:
                print(f"Sniped Vanity {x17}")
            elif 'mfa' in x20.text:
                    
                    x21 = x20.json()['mfa']['ticket']
                    x22 = x20.cookies
                    x23, x24 = self.y1(k3, x21, x22)
                    self.x10 = x23
                    if not x23:
                        print("Failed to get MFA token")
                        return
                    x25 = {
                    '__Secure-recent_mfa': x24,
                    '__dcfduid': x22.get('__dcfduid'),
                    '__sdcfduid': x22.get('__sdcfduid'),
                    '__cfruid': x22.get('__cfruid'),
                    '_cfuvid': x22.get('_cfuvid'),
                    }
                    x19['x-discord-mfa-authorization'] = self.x10
                    x26 = self.session.patch(x18, json={'code': x17}, headers=x19, cookies=x25)
                    if x26.status_code == 200:
                        print(f"Sniped Vanity {x17}")
        except:
            print(x20.json())

    async def y3(self):
        try:
            async with aiohttp.ClientSession() as x27:
                async with x27.ws_connect("wss://gateway.discord.gg/?encoding=json&v=9") as x28:
                    await self.y4(x28)
                    self.x9 = [self.y5(x28)]
                    await asyncio.gather(*self.x9)
        except Exception as x29:
            print(f"Error starting connection: {x29}")

    async def y4(self, x28):
        try:
            await x28.send_json({

            "op": 2,
            "d": {
                "token": self.k1,
                "capabilities": 30717,
                "properties": {
                        "os": "Windows",
                        "browser": "Chrome",
                        "device": "Desktop",
                        "system_locale": "en-US",
                        "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
                        "browser_version": f"117.0.0.0",
                        "os_version": "10",
                        "referrer": "",
                        "referring_domain": "",
                        "referrer_current": "",
                        "referring_domain_current": "",
                        "release_channel": "stable",
                        "client_build_number": int(x1()),
                        "client_event_source": None
                },
                "presence": {
                    "afk": False,
                    "since": time.time(),
                    "activities": [{
                        "name": 'running sniper',
                        "type": 0,
                    }],
                    "status": "unknown"
                },
                "compress": False,
                "client_state": {
                    "guild_versions": {}
                }
            }
        })
        except Exception as x30:
            print(f"Error sending initial presence: {x30}")


    async def y6(self, x28):
        while True:
            try:
                async for x31 in x28:
                    x32 = json.loads(x31.data)
                
                    if "s" in x32:
                        self.x6 = x32["s"]
                    if "resume_gateway_url" in x32:
                        self.x7 = x32["d"]["session_id"]
                        self.x8 = x32["d"]["resume_gateway_url"] + '/?encoding=json&v=9'
                        print("online with -> " + self.x7)

            except Exception as x33:
                print(f"Error during event handling: {x33}")

    async def y5(self, x28):
        try:
            async for x31 in x28:
                    x32 = json.loads(x31.data)
                    
                    if x32["op"] == 10:
                        x34 = int(x32["d"]["heartbeat_interval"]) / 1000
                        asyncio.create_task(self.y7(x28, x34))

                    if x32['t'] == 'GUILD_UPDATE':
                        if x32['d']['id'] in o1 and o1[x32['d']['id']] != x32['d']['vanity_url_code']:
                            await self.y2(o1[x32['d']['id']], k3)

        except Exception as x35:
            print(f"Event handling err: {x35}")

    async def y7(self, x28, x34):
        try:
            while True:
                x36 = {"op": 1, "d": self.x6}
                await x28.send_json(x36)
                await asyncio.sleep(x34)
        except Exception as x37:
            print(f"Heartbeat err: {x37}")

async def z2():
    os.system('cls' if os.name=='nt' else 'clear')
    try:
        
        x38 = A1(k1)
        await x38.y3()


            
    except Exception as x39:
        print(f"Err: {x39}")

if __name__ == "__main__":
    asyncio.run(z2())
