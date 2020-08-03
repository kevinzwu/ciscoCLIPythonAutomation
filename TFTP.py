from Exscript.util.start import quickstart
from Exscript.util.match import first_match
from Exscript import Host, Account
from Exscript.util.start import start
from Exscript.util.file import get_hosts_from_file

account1 = Account('YOURUSERNAME', 'YOURPASSWORD')
host1 = get_hosts_from_file('LISTOFIP.txt')
#host1 = Host('ssh://IPADDRESS')

def do_something(job, host, conn):

    conn.execute('sh run | i hostname')
    output= conn.response.split('\n')
    #print(output)

    name = ''

    for x in output:
        if(x.startswith('hostname')):
            y = x.replace("\r",'')
            z = y.replace("hostname ",'')
            name = z

    print(name)

    conn.execute('copy running-config tftp\nSERVERADDRESS\n' + name + '_backup')

    '''
    conn.execute('\n')
    conn.execute('networktftp.nsdecatur.local')
    conn.execute('\n')
    conn.execute(name + '_backup')
    conn.execute('\n')
    '''

start(account1, host1, do_something, max_threads=3)