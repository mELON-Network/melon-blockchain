from melon.util.ints import uint32, uint64

# 1 melon coin = 1,000,000,000 = 1 billion mojo.
_mojo_per_melon = 1000000000
_blocks_per_year = 1681920  # 32 * 6 * 24 * 365


def calculate_pool_reward(height: uint32) -> uint64:
    """
    Returns the pool reward at a certain block height. The pool earns 4/5 of the reward in each block. If the farmer
    is solo farming, they act as the pool, and therefore earn the entire block reward.
    These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """

    if height == 0:
        return uint64(int((8 / 10) * 13370000 * _mojo_per_melon))
    elif height < 2 * _blocks_per_year:
        return uint64(int((8 / 10) * 10 * _mojo_per_melon))
    elif height < 4 * _blocks_per_year:
        return uint64(int((4 / 10) * 10 * _mojo_per_melon))
    elif height < 8 * _blocks_per_year:
        return uint64(int((2 / 10) * 10 * _mojo_per_melon))
    else:
        return uint64(int((1 / 10) * 10 * _mojo_per_melon))


def calculate_base_farmer_reward(height: uint32) -> uint64:
    """
    Returns the base farmer reward at a certain block height.
    The base fee reward is 1/5 of total block reward

    Returns the coinbase reward at a certain block height. These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously. Bonus to the dev who contributed starting the blockchain !
    """
    if height == 0:
        return uint64(int((2 / 10) * 13370000 * _mojo_per_melon))
    elif height < 2 * _blocks_per_year:
        return uint64(int((1 / 10) * 10 * _mojo_per_melon))
    elif height < 4 * _blocks_per_year:
        return uint64(int((0.5 / 10) * 10 * _mojo_per_melon))
    elif height < 8 * _blocks_per_year:
        return uint64(int((0.25 / 10) * 10 * _mojo_per_melon))
    else:
        return uint64(int((0.125 / 10) * 10 * _mojo_per_melon))

def calculate_base_elonwallet_reward(height: uint32) -> uint64:
    """
    Elon Rewards: 10% per block
    """
    if height == 0:
        return uint64(int((10 / 10) * 0 * _mojo_per_melon))
    elif height < 2 * _blocks_per_year:
        return uint64(int((1 / 10) * 10 * _mojo_per_melon))
    elif height < 4 * _blocks_per_year:
        return uint64(int((0.5 / 10) * 10 * _mojo_per_melon))
    elif height < 8 * _blocks_per_year:
        return uint64(int((0.25 / 10) * 10 * _mojo_per_melon))
    else:
        return uint64(int((0.125 / 10) * 10 * _mojo_per_melon))
