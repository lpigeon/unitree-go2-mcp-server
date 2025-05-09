import socket
import json
import websocket
import base64

class WebSocketManager:
    def __init__(self, ip: str, port: int, local_ip: str):
        self.ip = ip
        self.port = port
        self.local_ip = local_ip
        self.ws = None

    def connect(self):
        if self.ws is None or not self.ws.connected:
            sock = socket.create_connection((self.ip, self.port), source_address=(self.local_ip, 0))
            ws = websocket.WebSocket()
            ws.sock = sock
            ws.connect(f"ws://{self.ip}:{self.port}")
            self.ws = ws
            print("[WebSocket] Connected")

    def send(self, message: dict):
        self.connect()
        if self.ws:
            try:
                # Ensure message is JSON serializable
                json_msg = json.dumps(message)
                self.ws.send(json_msg)
            except TypeError as e:
                print(f"[WebSocket] JSON serialization error: {e}")
                self.close()
            except Exception as e:
                print(f"[WebSocket] Send error: {e}")
                self.close()


    def receive_binary(self) -> bytes:
        self.connect()
        if self.ws:
            try:
                raw = self.ws.recv()  # raw is JSON string (type: str)
                return raw
            except Exception as e:
                print(f"Receive error: {e}")
                self.close()
        return b""
    
    def get_topics(self) -> list[tuple[str, str]]:
        self.connect()
        if self.ws:
            try:
                self.send({
                    "op": "call_service",
                    "service": "/rosapi/topics",
                    "id": "get_topics_request_1"
                })
                response = self.receive_binary()
                print(f"[WebSocket] Received response: {response}")
                if response:
                    data = json.loads(response)
                    if "values" in data:
                        topics = data["values"].get("topics", [])
                        types = data["values"].get("types", [])
                        if topics and types and len(topics) == len(types):
                            return list(zip(topics, types))
                        else:
                            print("[WebSocket] Mismatch in topics and types length")
            except json.JSONDecodeError as e:
                print(f"[WebSocket] JSON decode error: {e}")
            except Exception as e:
                print(f"[WebSocket] Error: {e}")
        return []

    def close(self):
        if self.ws and self.ws.connected:
            try:
                self.ws.close()
                print("[WebSocket] Closed")
            except Exception as e:
                print(f"[WebSocket] Close error: {e}")
            finally:
                self.ws = None
