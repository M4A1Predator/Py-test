import shlex
import subprocess
from time import sleep
from xml.etree.ElementTree import Element, ElementTree, SubElement


class Pping():

    @staticmethod
    def ping_site(site):
        cmd = shlex.split("ping {} -n 1".format(site))
        output = ""
        try:
            ot = subprocess.check_output(cmd)
            ot = ot.decode("UTF-8")
            # print(ot)
            output = ot

        except subprocess.CalledProcessError as e:
            erri = bytes(e.output)
            erri = erri.decode("UTF-8")
            output = erri
        # print(output)
        if output.find("Average = ") != -1:
            avgpos = ot.find("Average = ")
            output = ot[avgpos + len("Average = "):ot.find("ms", avgpos + len("Average = "))+2]
        elif output.find("timed out") != -1:
            output = "timed out".format(site)
        elif output.find("host unreachable") != -1:
            output = "unreachable".format(site)
        else:
            output = "failed to ping {}".format(site)

        return output

    @staticmethod
    def ping_loop(site):
        info = ""
        sites = ""
        for i in site:
            sites += i+"\t\t"

        print(sites)
        bar_cout = 0
        while True:
            for i in site:
                info += Pping.ping_site(i).rjust(len(i))+"\t\t"
            print(info)
            info = ""
            bar_cout += 1
            if bar_cout == 150:
                print(sites)
                bar_cout = 0
            sleep(1)



et = ElementTree()
et.parse("pinglist.xml")
root = et.getroot()
ping_list = []

for i in root:
    ping_list.append(i.text)

Pping.ping_loop(ping_list)


# site1 = "google.com"
# site2 = "twitch.tv"
# site3 = "facebook.com"
#
# Pping.ping_loop(site1, site2, site3)

# print(site1.ljust(len(site1)), site2.ljust(len(site2)), site3.rjust(len(site3)), sep="\t\t")
# print("512ms".rjust(len(site1)), "timed out".rjust(len(site2)), "51ms".rjust(len(site3)), sep="\t\t")

