
# 1 solution
netsh winsock reset catalog  (Reset WINSOCK entries to installation defaults)
netsh int ipv4 reset reset.log (Reset IPv4 TCP/IP stack to installation defaults)

# 2 solution
netsh int tcp set heuristics disabled
netsh int tcp set global autotuninglevel=disabled
netsh int tcp set global rss=enabled

# 3 solution
check firewall/antivirus




