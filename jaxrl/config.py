"""Agent configuration."""

import enum
from dataclasses import dataclass
from typing import Optional, Tuple, Type

from jaxrl import agents


@dataclass(frozen=True)
class SACConfig:
    agent_cls: Type[agents.Agent] = agents.SAC
    num_qs: int = 2
    actor_lr: float = 3e-4
    critic_lr: float = 3e-4
    temp_lr: float = 3e-4
    hidden_dims: Tuple[int, ...] = (256, 256, 256)
    num_min_qs: Optional[int] = None
    critic_dropout_rate: Optional[float] = None
    critic_layer_norm: bool = False
    tau: float = 0.005
    target_entropy: Optional[float] = None
    init_temperature: float = 1.0
    backup_entropy: bool = True


@dataclass(frozen=True)
class TD3Config:
    agent_cls: Type[agents.Agent] = agents.TD3
    num_qs: int = 2
    actor_lr: float = 3e-4
    critic_lr: float = 3e-4
    hidden_dims: Tuple[int, ...] = (256, 256, 256)
    num_min_qs: Optional[int] = None
    critic_dropout_rate: Optional[float] = None
    critic_layer_norm: bool = False
    tau: float = 0.005
    sigma: float = 0.1
    target_sigma: float = 0.2
    noise_clip: float = 0.5


@enum.unique
class Algo(enum.Enum):
    """Enumeration of supported algorithms."""

    SAC = SACConfig()
    SAC_DROQ = SACConfig(critic_dropout_rate=0.01, critic_layer_norm=True)
    SAC_REDQ = SACConfig(num_qs=10, num_min_qs=2)
    TD3 = TD3Config()
    TD3_DROQ = TD3Config(critic_dropout_rate=0.01, critic_layer_norm=True)
    TD3_REDQ = TD3Config(num_qs=10, num_min_qs=2)
