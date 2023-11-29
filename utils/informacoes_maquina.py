import psutil as ps


def get_mac_address():
    for key in ps.net_if_addrs().keys():
        if key.lower().startswith('e'):
            return ps.net_if_addrs()[key][0].address


def get_ipv6():
    for key in ps.net_if_addrs().keys():
        if key.lower().startswith('e'):
            return ps.net_if_addrs()[key][2].address
