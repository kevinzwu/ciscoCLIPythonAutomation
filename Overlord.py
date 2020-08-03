from Exscript.util.start import quickstart
from Exscript.util.match import first_match
from Exscript import Host, Account
from Exscript.util.start import start
from Exscript.util.file import get_hosts_from_file

account1 = Account('YOURUSERNAME', 'YOURPASSWORD')
host1 = get_hosts_from_file('LISTOFIP.txt')
#host1 = Host('ssh://IPADDRESS')

def do_something(job, host, conn):

    conn.execute('sh run | i username')
    output= conn.response.split('\n')
    #print(output)

    final = []

    for x in output:
        if(x.startswith('username')):
            y = x.replace("\r",'')
            final.append(y)

    conn.execute('conf t')
    #print(final)

    for x in final:
        noUser = 'no ' + x
        print(noUser)
        conn.execute(noUser + '\n')
        #conn.execute('')


    print(final)

    #conn.execute('conf t')

    conn.execute('username YOURUSERNAME privilege 15 password YOURPASSWORD')

    conn.execute('end')
    conn.execute('wr mem')

start(account1, host1, do_something, max_threads=3)