from Exscript.util.start import quickstart
from Exscript.util.match import first_match
from Exscript import Host, Account
from Exscript.util.start import start
from Exscript.util.file import get_hosts_from_file

account1 = Account('YOURUSERNAME', 'YOURPASSWORD')
host1 = get_hosts_from_file('LISTOFIP.txt')
#host1 = Host('ssh://IPADDRESS')

def do_something(job, host, conn):

    conn.execute('conf t')

#ntp server
    conn.execute('ntp server 10.10.10.10')

    conn.execute('end')
    conn.execute('wr mem')

start(account1, host1, do_something, max_threads=3)