from setuptools import setup

dependencies = [
    "blspy==1.0.5",  # Signature library
    "chiavdf==1.0.2",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.4",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.10",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.4",  # Colorizes terminal output
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "fasteners==0.16.3",  # For interprocess file locking
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the chia processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==8.0.4",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
    "watchdog==2.1.3",  # Filesystem event watching - watches keyring.yaml
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="melon-blockchain",
    author="Mariano Sorgente",
    author_email="admin@melon-network.de",
    description="melon blockchain full node, farmer, timelord, and wallet.",
    url="https://melon-network.de/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="melon blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "melon",
        "melon.cmds",
        "melon.clvm",
        "melon.consensus",
        "melon.daemon",
        "melon.full_node",
        "melon.timelord",
        "melon.farmer",
        "melon.harvester",
        "melon.introducer",
        "melon.plotting",
        "melon.pools",
        "melon.protocols",
        "melon.rpc",
        "melon.server",
        "melon.simulator",
        "melon.types.blockchain_format",
        "melon.types",
        "melon.util",
        "melon.wallet",
        "melon.wallet.puzzles",
        "melon.wallet.rl_wallet",
        "melon.wallet.cc_wallet",
        "melon.wallet.did_wallet",
        "melon.wallet.settings",
        "melon.wallet.trading",
        "melon.wallet.util",
        "melon.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "melon = melon.cmds.melon:main",
            "melon_wallet = melon.server.start_wallet:main",
            "melon_full_node = melon.server.start_full_node:main",
            "melon_harvester = melon.server.start_harvester:main",
            "melon_farmer = melon.server.start_farmer:main",
            "melon_introducer = melon.server.start_introducer:main",
            "melon_timelord = melon.server.start_timelord:main",
            "melon_timelord_launcher = melon.timelord.timelord_launcher:main",
            "melon_full_node_simulator = melon.simulator.start_simulator:main",
        ]
    },
    package_data={
        "melon": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp"],
        "melon.util": ["initial-*.yaml", "english.txt"],
        "melon.ssl": ["melon_ca.crt", "melon_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
