from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "melon_harvester melon_timelord_launcher melon_timelord melon_farmer melon_full_node melon_wallet".split(),
    "node": "melon_full_node".split(),
    "harvester": "melon_harvester".split(),
    "farmer": "melon_harvester melon_farmer melon_full_node melon_wallet".split(),
    "farmer-no-wallet": "melon_harvester melon_farmer melon_full_node".split(),
    "farmer-only": "melon_farmer".split(),
    "timelord": "melon_timelord_launcher melon_timelord melon_full_node".split(),
    "timelord-only": "melon_timelord".split(),
    "timelord-launcher-only": "melon_timelord_launcher".split(),
    "wallet": "melon_wallet melon_full_node".split(),
    "wallet-only": "melon_wallet".split(),
    "introducer": "melon_introducer".split(),
    "simulator": "melon_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
