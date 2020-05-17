#!/usr/bin/env python3
import cgxinit
from cloudgenix import jd, jd_detailed
import sys
import logging


def listPerPrefixARP(cgx,args,sites):
    """
    list the PerPrefixARP objects for all IONs
    """
    for element in cgx.get.elements().cgx_content["items"]:

        # check if element is a spoke
        if element["site_id"] in sites:
            log.info("Listing PerPrefixARP for {element} at {site}".format( element=element["name"], site=sites[element["site_id"]]))
            for extension in cgx.get.element_extensions(element["site_id"], element["id"]).cgx_content["items"]:
                if extension["namespace"] == "fcconfig":
                    jd(extension)

def updatePerPrefixARP(cgx,args,sites):
    """
    change per Prefix ARP according to the args input
    """
    # for every elemnt, check if it should be changed and if it should do the required change
    for element in cgx.get.elements().cgx_content["items"]:

        # if element ID isn't in the sites list, its a hub and we can ignore it
        if not element["site_id"] in sites:
            continue

        # first check if extension exist
        log.info("{element} at {site} is being configured".format(
            element=element["name"], site=sites[element["site_id"]]))
        fcconfig = None
        for extension in cgx.get.element_extensions(element["site_id"], element["id"]).cgx_content["items"]:
            if extension["namespace"] == "fcconfig":
                fcconfig = extension
                log.info("-- already have fcconfig")
                break

        # if alg do not exists create on
        if not fcconfig:
            log.info("-- creating fcconfig namespace")
            ext = {
                "name": "fc config",
                "namespace": "fcconfig",
                "entity_id": "8844",
                "disabled": False,
                "conf": {
                    "arp_per_prefix_router_failure" : args["enable"]
                }
            }
            r = cgx.post.element_extensions(
                element["site_id"], element["id"], ext)
            if not r:
                jd_detailed(r)
                raise ValueError("cant create fcconfig extenstion")
        else:
            # set the new value
            fcconfig["conf"]["arp_per_prefix_router_failure"] = args["enable"]

            # update the rules
            log.info("-- updating fcconfig entry")
            r = cgx.put.element_extensions(element["site_id"], element["id"], fcconfig["id"],fcconfig)
            if not r:
                jd_detailed(r)
                raise ValueError("cant update fcconfig extension")


if __name__ == "__main__":
    # init cloudgenix object and get command line arguments
    cgx, args = cgxinit.go()

    #init logging
    logging.basicConfig(level=logging.INFO)
    log=logging.getLogger("PerPrefixARP")

    # check params
    if not args["list"]:
        if not args["all"] and not args["site_file"]:
            log.error("Both --all and --site_file arguments are missing. One, and only one for them is required")
            log.error("You can also use --list without any other arguments")
            sys.exit(-1)
    # cuild a site list from the site file
    site_list=[]
    if args["site_file"]:
        site_list=args["site_file"].read().splitlines()
    #build site list
    sites={}
    for site in cgx.get.sites().cgx_content["items"]:
        # we only care about spoke sites as hub sites don't do NAT
        if site["element_cluster_role"] == "SPOKE":
            # check if site belong to the site list
            if args["list"] or args["scope_all"] or site["name"] in site_list:
                sites[site["id"]] = site["name"]
    if args["list"]:
        listPerPrefixARP(cgx,args,sites)
    else:
        updatePerPrefixARP(cgx,args,sites)
