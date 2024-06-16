from datetime import datetime
from dataclasses import dataclass


@dataclass
class ActivityModel:
    service: str
    endpoint: str
    method: str
    created_at: datetime

    def __str__(self) -> str:
        msg = f"{self.created_at} {self.service}: "
        msg += f"{self.method} {self.endpoint}"
        return msg
