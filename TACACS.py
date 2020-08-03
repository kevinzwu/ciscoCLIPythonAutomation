from Exscript.util.start import quickstart
from Exscript.util.match import first_match
from Exscript import Host, Account
from Exscript.util.start import start
from Exscript.util.file import get_hosts_from_file

account1 = Account('YOURUSERNAME', 'YOURPASSWORD')
host1 = get_hosts_from_file('LISTOFIP.txt')
#host1 = Host('ssh://IPADDRESS')

def do_something(job, host, conn):

    conn.execute('sh run | i tacacs-server host')
    output= conn.response.split('\n')
    #print(output)

    final = []

    for x in output:
        if(x.startswith('tacacs-server host')):
            y = x.replace("\r",'')
            final.append(y)

    conn.execute('conf t')
    count = len(final)
    print(len(final))
    #print(final)

    for x in final:
        noUser = 'no ' + x
        print(noUser)
        conn.execute(noUser + '\n')
        #conn.execute('')


    print(final)

    #conn.execute('conf t')

    if(count==0):
        conn.execute('aaa group server tacacs+ ISE')
        conn.execute('server name GROUPNAME')
        conn.execute('exit')

        conn.execute('aaa authentication login default group ISE local')

        conn.execute('tacacs-server directed-request')
        conn.execute('no tacacs-server key 7 14461C0F5D037A2D743027277207')

        conn.execute('tacacs server GROUPNAME')
        conn.execute('address ipv4 IPADDRESS')
        conn.execute('key 7 KEY')

    else:
        conn.execute('aaa authentication login default group tacacs+ local')

        conn.execute('tacacs-server host IPADDRESS')

    conn.execute('end')
    conn.execute('wr mem')

start(account1, host1, do_something, max_threads=3)